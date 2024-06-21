"""Generation and coalescing of tokens.

This is a layer between lexer and parser.
"""
import collections.abc as _abc
import functools as _ft

import tla._langdef as _opdef
import tla._lex as _lex
import tla._utils as _utils


_PREFIXAL = _opdef.PREFIXAL
_INFIXAL = _opdef.INFIXAL
_POSTFIXAL = _opdef.POSTFIXAL
# Tokens that are step numbers.
STEP_NUMBER_TOKENS = {
    'STEP_NUMBER',
    'STEP_NUMBER_PLUS',
    'STEP_NUMBER_ASTERISK',
    }
_utils.assert_len(
    STEP_NUMBER_TOKENS, 3)
# A step number that follows any
# of these tokens is the start
# of a step. Otherwise, step numbers
# are identifiers (converted to
# token `NAME`).
_TOKENS_BEFORE_STEP_START = {
    # operators: POSTFIX
    'BOOLEAN',
    'FALSE',
    'OBVIOUS',
    'OMITTED',
    'PROOF',
    'QED',
    'STRING',
    'TRUE',
    'BINARY_INTEGER',
    'DECIMAL_INTEGER',
    'FLOAT',
    'HEXADECIMAL_INTEGER',
    'MULTILINE_STRING_LITERAL',
    'NAME',
    'OCTAL_INTEGER',
    'STEP_NUMBER',
    'STEP_NUMBER_ASTERISK',
    'STEP_NUMBER_PLUS',
    'STRING_LITERAL',
    'RPAREN',
    'RBRACE',
    'RBRACKET',
    'DOUBLE_RANGLE',
    }
_utils.assert_len(
    _TOKENS_BEFORE_STEP_START, 23)
MODULE_SCOPE_TOKENS = STEP_NUMBER_TOKENS | {
    'DEF_SIG',
    'EQ_LINE',
    'DASH_LINE',
    'VARIABLE',
    'VARIABLES',
    'CONSTANT',
    'CONSTANTS',
    'RECURSIVE',
    'ASSUMPTION',
    'ASSUME',
    'AXIOM',
    'THEOREM',
    'PROPOSITION',
    'PROOF',
    'PROVE',
    'LEMMA',
    'COROLLARY',
    'BY',
    'DEF',
    'DEFS',
    'OBVIOUS',
    'OMITTED',
    'USE',
    'HIDE',
    'INSTANCE',
        # `INSTANCE` occurs either:
        # - in module scope
        # - after `==`
        # - after `STEP_NUMBER`
    }
_utils.assert_len(
    MODULE_SCOPE_TOKENS,
    25 + len(STEP_NUMBER_TOKENS))
# Tokens that close a `DEFINE` section.
_DEFINE_CLOSING_TOKENS = (
    MODULE_SCOPE_TOKENS - {
        'DEF_SIG', 'INSTANCE'})
_utils.assert_len(
    _DEFINE_CLOSING_TOKENS,
    -2 + len(MODULE_SCOPE_TOKENS))
_BEFORE_POSTFIXAL = {
    'DEF',
    'DEFS',
    'COMMA',
    'LPAREN',
    'WITH',
    'LARROW',
    'EXCLAMATION',
    }
_utils.assert_len(
    _BEFORE_POSTFIXAL, 7)
_AFTER_PREFIXAL = MODULE_SCOPE_TOKENS | {
    'COMMA',
    'RPAREN',
    'LARROW',
    'EXCLAMATION',
    }
_utils.assert_len(
    _AFTER_PREFIXAL,
    4 + len(MODULE_SCOPE_TOKENS))


def preparse(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterable:
    """Prepare tokens for parser."""
    tokens = insert_def_starts_tokens(tokens)
    tokens = swap_local_keyword(tokens)
    tokens = join_as_one_token(tokens)
    tokens = switch_step_identifiers(tokens)
    tokens = switch_keywords_after_dot(tokens)
        # `L.WITH &` needs switching `WITH` to
        # `NAME` token before checking the
        # fixal operator `&`
    tokens = switch_fixal_operators(tokens)
    tokens = insert_proof_define_tokens(tokens)
    tokens = end_define_proof_steps(tokens)
    return tokens


def insert_def_starts_tokens(
        tokens:
            _abc.Iterable
        ) -> list:
    """Delimit start of definitions."""
    return _utils.pipe(
        tokens,
        _utils.reverse,
        _insert_def_sig_tokens_nonfix,
        _insert_def_sig_tokens_fixal,
        _utils.reverse)


def _insert_def_sig_tokens_fixal(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterable:
    r"""Insert `DEF_SIG` tokens.

    - `name infixal name ==`
    - `name ==`
    - `-. name ==`
    - `name postfixal ==`
    """
    stack = list()
    def make_def_sig(
            token):
        return _utils.make_lex_token(
            'DEF_SIG',
            row=token.row,
            column=token.column,
            start=token.start)
    last_tokens = list()
    for token in tokens:
        # prefix-operator definition
        is_prefix_def = (
            len(last_tokens) >= 2 and
            last_tokens[-2].symbol == 'DOUBLE_EQ' and
            last_tokens[-1].symbol == 'NAME' and
            token.value in _PREFIXAL)
        if is_prefix_def:
            yield token
            yield make_def_sig(token)
        # infix-operator definition
        is_infix_def = (
            len(last_tokens) >= 3 and
            last_tokens[-3].symbol == 'DOUBLE_EQ' and
            last_tokens[-2].symbol == 'NAME' and
            last_tokens[-1].value in _INFIXAL and
            token.symbol == 'NAME')
        if is_infix_def:
            yield token
            yield make_def_sig(token)
        # postfix-operator definition
        is_postfix_def = (
            len(last_tokens) >= 2 and
            last_tokens[-2].symbol == 'DOUBLE_EQ' and
            last_tokens[-1].value in _POSTFIXAL and
            token.symbol == 'NAME')
        if is_postfix_def:
            yield token
            yield make_def_sig(token)
        # nullary-operator definition
        is_nullary_def = (
            len(last_tokens) >= 2 and
            last_tokens[-2].symbol == 'DOUBLE_EQ' and
            last_tokens[-1].symbol == 'NAME' and
            not is_prefix_def and
            token.value not in _INFIXAL)
        if is_nullary_def:
            yield make_def_sig(token)
            yield token
        is_def = (
            is_prefix_def or
            is_infix_def or
            is_postfix_def or
            is_nullary_def)
        if not is_def:
            yield token
        last_tokens.append(token)
    if not stack:
        return
    raise ValueError(stack)


def _insert_def_sig_tokens_nonfix(
        tokens:
            _abc.Sequence
        ) -> _abc.Iterable:
    r"""Insert `DEF_SIG` tokens.

    Cases:
    - `name(...) ==`
    - `name[...] ==` (nesting of definition
        signatures can occur here, e.g.,
        `f[x \in LET -. r == r IN {-1}] == x`)

    `LOCAL` can precede any of these cases.

    @param tokens:
        sequence of tokens reversed from
        how they appear in the TLA+ source,
        i.e., in the lexer's output
    @return:
        sequence of tokens,
        in the same direction as the input
        (i.e., reversed from their order
         in the TLA+ source)
    """
    stack = list()
    def make_def_sig(
            token):
        return _utils.make_lex_token(
            'DEF_SIG',
            row=token.row,
            column=token.column,
            start=token.start)
    last_token = _utils.make_lex_token(None)
    for token in tokens:
        ts = token.symbol
        if (ts in ('RPAREN', 'RBRACKET') and
                last_token.symbol == 'DOUBLE_EQ'):
            stack.append(2)
            yield token
        elif not stack:
            yield token
        elif (ts in ('LPAREN', 'LBRACKET') and
                stack[-1] > 0):
            stack[-1] -= 1
            yield token
        elif (ts in ('RPAREN', 'RBRACKET') and
                stack[-1] > 0):
            stack[-1] += 1
            yield token
        elif ts == 'NAME' and stack[-1] == 1:
            stack.pop()
            yield token
            yield make_def_sig(token)
        elif stack[-1] != 0:
            yield token
        else:
            yield token
        last_token = token
    if not stack:
        return
    raise ValueError(stack)


def swap_local_keyword(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterable:
    """Swap `LOCAL DEF_SIG` to `DEF_SIG LOCAL`."""
    previous = None
    for token in tokens:
        ts = token.symbol
        if ts == 'LOCAL':
            previous = token
            continue
        swap = (
            previous is not None and
            token.symbol == 'DEF_SIG')
        if swap:
            yield token
            yield previous
        elif previous is not None:
            yield previous
            yield token
        else:
            yield token
        if previous is not None:
            previous = None
    if previous is not None:
        yield previous


def insert_proof_define_tokens(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterable:
    """Insert any missing `DEFINE` tokens."""
    last_token = _utils.make_lex_token(None)
    for token in tokens:
        if (token.symbol == 'DEF_SIG' and
                last_token.symbol in
                    STEP_NUMBER_TOKENS):
            # column information is not needed,
            # because `DEFINE` cannot follow
            # a vertical item
            yield _utils.make_lex_token('DEFINE')
        last_token = token
        yield token


def end_define_proof_steps(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterable:
    """Add `END_DEFINE` at end of `DEFINE`."""
    inside_define_step = False
    previous = _utils.make_lex_token(None)
    for token in tokens:
        ts = token.symbol
        pt = previous.symbol
        module_scope_instance = (
            ts == 'INSTANCE' and
            pt != 'DOUBLE_EQ')
        is_closing = (
            ts in _DEFINE_CLOSING_TOKENS or
            module_scope_instance)
        add_token = (
            inside_define_step and
            is_closing)
        if add_token:
            inside_define_step = False
            # column information is not needed,
            # because `END_DEFINE` ends also
            # vertical items, as a
            # non-blankspace token
            yield _utils.make_lex_token('END_DEFINE')
        if ts == 'DEFINE':
            inside_define_step = True
        previous = token
        yield token


def switch_step_identifiers(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterable:
    """Convert step identifiers to `NAME`.

    For occurrences of step identifiers
    within leaf proofs (`BY` proofs).
    """
    last_token = _utils.make_lex_token(None)
    for token in tokens:
        switch = (
            token.symbol in
                STEP_NUMBER_TOKENS and
            last_token.symbol not in
                _TOKENS_BEFORE_STEP_START and
            last_token.value not in
                _POSTFIXAL)
        if switch:
            token = _utils.copy_lex_token(
                token,
                symbol='NAME')
        last_token = token
        yield token


def join_as_one_token(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterable:
    """Map `<<TOK1, TOK2>>` to `<<TOK1_TOK2>>`.

    Coalescing:

    - `<<EXCLAMATION, AT>>`
      to `<<EXCLAMATION_AT>>`

    - `<<EXCLAMATION, COLON>>`
      to `<<EXCLAMATION_COLON>>`

    - `<<EXCLAMATION, DOUBLE_LANGLE>>`
      to `<<EXCLAMATION_DOUBLE_LANGLE>>`

    - `<<EXCLAMATION, NAME>>`
      to `<<EXCLAMATION_NAME>>`

    - `<<EXCLAMATION, DOUBLE_RANGLE>>`
      to `<<EXCLAMATION_DOUBLE_RANGLE>>`
    """
    toks = {
        'AT',
        'COLON',
        'DOUBLE_LANGLE',
        'DOUBLE_RANGLE',
        'NAME',
        }
    pairs = {
        f'EXCLAMATION_{s}'
        for s in toks}
    first = {'EXCLAMATION'}
    notoken = _utils.make_lex_token(None)
    last_token = notoken
    for token in tokens:
        a = last_token.symbol
        b = token.symbol
        token_type = f'{a}_{b}'
        if token_type in pairs:
            if token_type.startswith(
                    'EXCLAMATION'):
                token_value = token.value
            else:
                raise ValueError(token_type)
            yield _utils.copy_lex_token(
                last_token,
                symbol=token_type,
                value=token_value)
            last_token = notoken
            continue
        elif last_token.symbol in first:
            yield last_token
            last_token = token
        if token.symbol in first:
            last_token = token
            continue
        last_token = notoken
        yield token
    # This case can arise when the
    # start symbol of the grammar is
    # an expression. An expression
    # can end in a `NAME` token.
    if last_token != notoken:
        yield last_token


def switch_fixal_operators(
        tokens:
            _abc.Iterable
        ) -> list:
    """Convert fixal to `NAME`.

    For operators as arguments, for example:
    `Op(+, 1, 2)`

    The `+` is converted from an operator
    to `NAME`.
    """
    forward_scan = _ft.partial(
        _switch_scan,
        current=_INFIXAL | _POSTFIXAL,
        previous=_BEFORE_POSTFIXAL)
    reverse_scan = _ft.partial(
        _switch_scan,
        current=_PREFIXAL,
        previous=_AFTER_PREFIXAL)
    return _utils.pipe(
        tokens,
        forward_scan,
        _utils.reverse,
        reverse_scan,
        _switch_fixal_exclamation,
        _utils.reverse)


def switch_keywords_after_dot(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterable:
    """Map `DOT KEYWORD` to `DOT NAME`."""
    keywords = set(_opdef.KEYWORDS)
    keywords.update(['SF_', 'WF_'])
    return _switch_scan(
        tokens,
        current=keywords,
        previous={'DOT'})


def _switch_scan(
        tokens:
            _abc.Iterable,
        current:
            set[str],
        previous:
            set[str]
        ) -> _abc.Iterable:
    previous_token = _utils.make_lex_token(None)
    for token in tokens:
        switch = (
            token.value in current and
            previous_token.symbol in previous)
        if switch:
            token = _utils.copy_lex_token(
                token,
                symbol='NAME')
            assert token.symbol == 'NAME', token
        previous_token = token
        yield token


def _switch_fixal_exclamation(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterable:
    """Map fixal before `(...)!`, to `NAME`."""
    stack = list()
    last_token = None
    for token in tokens:
        ts = token.symbol
        if (ts == 'RPAREN' and
                last_token is not None and
                last_token.symbol.startswith(
                    'EXCLAMATION')):
            stack.append(1)
            yield token
        elif not stack:
            yield token
        elif ts == 'RPAREN':
            stack[-1] += 1
            yield token
        elif ts == 'LPAREN':
            stack[-1] -= 1
            yield token
        elif stack[-1] > 0:
            yield token
        elif (ts.startswith('OP_') and
                stack[-1] == 0):
            stack.pop()
            yield _utils.copy_lex_token(
                token,
                symbol='NAME')
        elif stack[-1] == 0:
            # A(...)!
            # already `NAME`, not fixal
            stack.pop()
            yield token
        else:
            yield token
        last_token = token
    if not stack:
        return
    raise ValueError(stack)


def filter_comments(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterator:
    """Omit tokens that are comments."""
    comments = _lex.COMMENT_TOKENS
    for token in tokens:
        if token.symbol in comments:
            continue
        yield token


def filter_outside_module(
        tokens:
            _abc.Iterable
        ) -> _abc.Iterable:
    """Omit tokens before and after root module."""
    tokens = list(tokens)
    module_count = 0
    for i, token in enumerate(tokens):
        if i + 1 >= len(tokens):
            next_symbol = None
        else:
            next_symbol = tokens[i + 1].symbol
        module_starts = (
            token.symbol == 'DASH_LINE' and
            next_symbol == 'MODULE')
        if module_starts:
            module_count += 1
        module_ends = (
            token.symbol == 'EQ_LINE')
        if module_ends and module_count > 1:
            module_count -= 1
        elif module_ends and module_count == 1:
            yield token
            break
        if module_count > 0:
            yield token
