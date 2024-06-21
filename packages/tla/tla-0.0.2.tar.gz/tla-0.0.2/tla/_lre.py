"""LR machine that creates RVERTICAL, END_LET as needed."""
import argparse as _arg
import collections as _cl
import collections.abc as _abc
import functools as _ft
import os
import typing as _ty

import parstools._grammars as _grm
import parstools._introspection as _intro
import parstools._lex as _prs_lex
import parstools._lr.parser as _p
from parstools._lr.parser import (
    Result,
    CachedIterable,
    _ROOT,
    _END,
    _State,
    _Actions,
    _TreeMap)
import parstools._lr.utils as _lu

import tla._ast as _tla_ast
import tla._grammar as _tla_grm
import tla._langdef as _opdef
import tla._lex as _lex
import tla._preparser as _prp
import tla._utils as _utils


# auto-generated tokens by the parser,
# with effect similar to the LR end-marker
_AUTO_VIRTUAL_TOKENS: _ty.Final = {
    # 'VERTICAL_OPERATOR',
    # 'LVERTICAL',
    'RVERTICAL',
    # 'DEF_SIG',
    # 'EXCLAMATION_AT',
    # 'EXCLAMATION_COLON',
    # 'EXCLAMATION_DOUBLE_LANGLE',
    # 'EXCLAMATION_DOUBLE_RANGLE',
    # 'EXCLAMATION_NAME',
    # 'END_DEFINE',
    'END_BSLASH_A',
    'END_BSLASH_E',
    'END_BSLASH_AA',
    'END_BSLASH_EE',
    'END_CHOOSE',
    'END_LAMBDA',
    'END_IF',
    'END_CASE',
    'END_LET',
    'END_PICK',
    }
_TOKEN_PAIRS: _ty.Final = dict(
    LVERTICAL='RVERTICAL',
    LET='END_LET',
    BSLASH_A='END_BSLASH_A',
    BSLASH_E='END_BSLASH_E',
    BSLASH_AA='END_BSLASH_AA',
    BSLASH_EE='END_BSLASH_EE',
    CHOOSE='END_CHOOSE',
    LAMBDA='END_LAMBDA',
    IF='END_IF',
    CASE='END_CASE',
    PICK='END_PICK')
_UNDELIMITED_TOKENS = set(_TOKEN_PAIRS)
_UNDELIMITED_TOKENS.remove('LVERTICAL')
_LEXEME_PRECEDENCE = _opdef.LEXEME_PRECEDENCE
_TLA_OPERATOR_FIXITY = _opdef.TLA_OPERATOR_FIXITY
_EXCEPT_TOKEN_TYPES = _tla_grm.EXCEPT_TOKEN_TYPES
_VERTICAL_LEXEMES = _opdef.VERTICAL_LEXEMES


# If the token that precedes an operator
# is in the set `_LOOKBEHIND_TOKENS`,
# then the operator is vertical.
_LOOKBEHIND_TOKENS = {
    # The method
    # `OperatorLexer.__init__()`
    # adds infix and prefix operators
    # to this set.
    'ASSUME',
    'ASSUMPTION',
    'AXIOM',
    'BSLASH_IN',
    'BY',
    'COROLLARY',
    'CARTESIAN',
    'CASE',
    'COLON',
    'COMMA',
    'DOMAIN',
    'DOUBLE_EQ',
    'EQ',
    'ELIF',
    'ELSE',
    'ENABLED',
    'HAVE',
    'HIDE',
    'IF',
    'IN',
    'LBRACE',
    'LBRACKET',
    'DOUBLE_LANGLE',
    'LARROW',
    'LBRACKET_RBRACKET',
    'LEMMA',
    'LPAREN',
    'LVERTICAL',
    'MAPSTO',
    'ONLY',
    'OTHER',
    'PROPOSITION',
    'PROVE',
    'DOUBLE_RANGLE_UNDERSCORE',
    'RARROW',
    'RBRACKET_UNDERSCORE',
    'RVERTICAL',
    'SUBSET',
    'SUFFICES',
    'THEN',
    'THEOREM',
    'UNCHANGED',
    'UNION',
    'USE',
    'WF_',
    'WITNESS',
    'SF_',
    'STEP_NUMBER',
    'STEP_NUMBER_ASTERISK',
    'STEP_NUMBER_PLUS',
    }
_utils.assert_len(
    _LOOKBEHIND_TOKENS, 50)


class Grammar(
        _tla_grm.OperatorPrecedenceGrammar):
    """Stacks for undelimited constructs."""

    def __init__(
            self
            ) -> None:
        """Initialize state."""
        super().__init__()
        self.scopes_stack = list()
            # LET, LVERTICAL, quantification,
            # and other undelimited constructs
        self.columns_stack = list()
            # opening columns of
            # vertical operators

    def p_vertical_operator(
            self, p):
        """vertical_op: VERTICAL_OPERATOR"""
        # `_map_if_vertical()` creates
        # `VERTICAL_OPERATOR` tokens
        p[0] = p[1]
        self.scopes_stack.append(
            'LVERTICAL')
        trees = p[-1]
        if len(trees) != 1:
            raise AssertionError(trees)
        vertical_op, = trees
        self.columns_stack.append(
            vertical_op.column)
        # The LR parser via this method
        # changes the stacks only when
        # a `VERTICAL_OPERATOR` occurrence
        # that starts a vertical item.


class OperatorLexer:
    """Adapats token sequence for parser."""

    def __init__(
            self
            ) -> None:
        """Initialization."""
        self._lexer = _lex.Lexer()
        self._token_grouping, before_vertical = (
            self._make_token_types())
        self._before_vertical = before_vertical

    def _make_token_types(
            self
            ) -> dict:
        """Make grouping of tokens."""
        keywords = {
            v: v for v in _opdef.KEYWORDS}
        lexemes_to_tokens = (
            keywords |
            _lex.map_lexemes_to_tokens())
        before_vertical = set(_LOOKBEHIND_TOKENS)
        groups = dict()
        items = _LEXEME_PRECEDENCE.items()
        for lexeme, prec in items:
            old_type = lexemes_to_tokens[lexeme]
            if old_type in _EXCEPT_TOKEN_TYPES:
                continue
            new_type = self._type_of_prec(
                lexeme, prec)
            groups[old_type] = new_type
            self._update_lookbehind_token_types(
                new_type, before_vertical)
        return (
            groups,
            before_vertical)

    def _type_of_prec(
            self,
            lexeme:
                str,
            prec:
                _opdef.PrecRange
            ) -> str:
        """Return token type for precedence."""
        start, _ = prec
        items = _TLA_OPERATOR_FIXITY.items()
        for fixity, operators in items:
            if lexeme not in operators:
                continue
            return f'OP_{start}_{fixity}'.upper()

    _PREFIX_OR_INFIX: _ty.Final = {
        'PREFIX',
        'BEFORE',
        'INFIX',
        'LEFT',
        'BETWEEN',
        'RIGHT'}

    def _update_lookbehind_token_types(
            self,
            new_type,
            before_vertical):
        """Add prefix and infix operators to

        `before_vertical`.
        """
        if new_type is None:
            return
        *_, fixity = new_type.rpartition('_')
        if fixity in ('POSTFIX', 'AFTER'):
            return
        if fixity in self._PREFIX_OR_INFIX:
            before_vertical.add(new_type)
            return
        raise ValueError(
            new_type)

    def _group_tokens(
            self,
            tokens
            ) -> _abc.Iterable[
                _prs_lex.Token]:
        """Adapt token symbols."""
        group = self._token_grouping.get
        new_tokens = list()
        for token in tokens:
            ts = token.symbol
            new_type = group(ts, ts)
            new_token = _utils.copy_lex_token(
                token,
                symbol=new_type)
            new_tokens.append(new_token)
        return new_tokens

    def parse(
            self,
            text:
                str
            ) -> _abc.Iterable[
                _prs_lex.Token]:
        """Return tokenized `text`."""
        tokens = self._lexer.parse(text)
        tokens = _prp.filter_comments(tokens)
        tokens = _prp.filter_outside_module(tokens)
        tokens = self._group_tokens(tokens)
        tokens = _prp.preparse(tokens)
        return tokens


class GeneratingParser:
    """Shift-reduce parser.

    For a set of "virtual tokens",
    the parser generates them when
    they are missing from the input.

    This approach is correct for
    handling syntactic features of
    a number of languages.

    Actions are structured as:
    `dict[node, dict[lookahead, ...]]`
    """

    def __init__(
            self
            ) -> None:
        """Initialize."""
        # cache filename
        filename = 'tla_parser.json'
        path, _ = os.path.split(__file__)
        cache_filepath = os.path.join(
            path, filename)
        # LR tables
        self.grammar = Grammar()
        op_prec = self.grammar.operator_precedence
        parser = _intro.make_parser(
            self.grammar,
            operator_precedence=op_prec,
            cache_filepath=cache_filepath)
        self._initial: _State = parser._initial
        actions = self._restructure_actions(
            parser._actions)
        self._actions: _Actions = actions
        self._tree_map: _TreeMap = parser._tree_map
        # stacks
        lexer = OperatorLexer()
        self._before_vertical = lexer._before_vertical
        self._last_token = None

    def _restructure_actions(
            self,
            actions:
                dict
            ) -> dict:
        """Return nested dictionary."""
        actions_ns = _cl.defaultdict(dict)
        kvs = actions.items()
        for (node, symbol), action in kvs:
            actions_ns[
                node][symbol] = action
        return dict(actions_ns)

    def parse(
            self,
            items:
                _abc.Iterable[
                    Result]
            ) -> Result | None:
        """Reduce items to a tree."""
        sequence = list(items)
        end = Result(
            symbol=_END,
            value=_END)
        sequence.append(end)
        symbols = CachedIterable(sequence)
            # input stack
        results = list()
            # output stack
        path = [self._initial]
        shift_or_reduce = _ft.partial(
            self._shift_or_reduce,
            symbols=symbols,
            results=results,
            path=path)
        while symbols.peek() and path:
            self._map_if_vertical(symbols)
            self._generate_dedents(symbols)
            shift_or_reduce()
        if symbols.peek() or path:
            return None
        if len(results) != 1:
            raise AssertionError(results)
        if self.grammar.scopes_stack:
            raise AssertionError(
                self.grammar.scopes_stack)
        if self.grammar.columns_stack:
            raise AssertionError(
                self.grammar.columns_stack)
        return results[0]

    def _shift_or_reduce(
            self,
            symbols:
                list[
                    Result],
            results:
                list[
                    Result],
            path:
                list
            ) -> None:
        """Step of shift-reduce parser."""
        if not path:
            raise AssertionError(path)
        peek = symbols.peek()
        if peek is None:
            raise AssertionError(symbols)
        lookahead = peek.symbol
        # if isinstance(peek.value, str):
        #     print(peek)
        if lookahead == _ROOT:
            results.append(symbols.pop())
            treelet = symbols.pop()
            if treelet.symbol != _END:
                raise AssertionError(_END)
            path.pop()
            return
        node = path[-1]
        action = self._actions[node].get(lookahead)
        # generate virtual token ?
        generate = (
            action is None and
            self.grammar.scopes_stack)
        if generate:
            self._generate_virtual_tokens(
                node, symbols)
            return
        # parsing error ?
        if action is None:
            self._print_info(symbols, results)
            path.clear()
            return
        if action.equation is not None:
            eq = action.equation
            symbol, expansion = eq
            n_items = len(expansion)
            _p.popk(path, n_items)
            equation = str(eq)
            trees = _p.popk(results, n_items)
            if self._tree_map is not None:
                reduce = self._tree_map[equation]
                p = [None, *(
                    u.value
                    for u in trees),
                    trees]
                reduce(p)
                trees = p[0]
            result = Result(
                symbol=symbol,
                value=trees,
                equation=equation)
            symbols.append(result)
        elif action.state is not None:
            path.append(action.state)
            treelet = symbols.pop()
            results.append(treelet)
            self._scopes_stack_append(
                treelet.symbol)
            # leaf ?
            if isinstance(treelet.value, str):
                self._last_token = treelet
        else:
            raise AssertionError(
                node, lookahead, action)

    def _scopes_stack_append(
            self,
            symbol:
                str
            ) -> None:
        """Append if start of undelimited."""
        if symbol not in _UNDELIMITED_TOKENS:
            return
        self.grammar.scopes_stack.append(symbol)

    def _map_if_vertical(
            self,
            symbols:
                CachedIterable
            ) -> None:
        """Map tokens to vertical tokens.

        Create `VERTICAL_OPERATOR` tokens from
        infix operators in `_VERTICAL_LEXEMES`,
        if the occurrences are vertical.
        """
        # NOTE: an LR shift-reduce overlap
        # gave rise to this function
        token = symbols.peek()
        if token is None:
            return
        # nonleaf ?
        if not isinstance(token.value, str):
            return
        is_vertical = (
            token.symbol != 'VERTICAL_OPERATOR' and
                # avoid recursion
            token.value in _VERTICAL_LEXEMES and
            self._last_token.symbol in
                self._before_vertical)
                # tokens and not nonleafs
        if not is_vertical:
            return
        vertical_op = _utils.copy_lex_token(
            token,
            symbol='VERTICAL_OPERATOR')
        symbols.pop()
        lvertical = _prs_lex.Token(
            symbol='LVERTICAL',
            value='LVERTICAL',
            column=token.column + 1,
                # Avoid closing vertical expression
                # due to indentation.
                #
                # Using `token.column` would
                # generate an `RVERTICAL` before
                # shifting the `LVERTICAL`.
            row=token.row,
            start=None)
        symbols.append(lvertical)
        symbols.append(vertical_op)

    def _generate_virtual_tokens(
            self,
            node,
            symbols:
                list
            ) -> None:
        """Insert a suitable virtual token.

        Virtual tokens are listed in
        `_AUTO_VIRTUAL_TOKENS`.
        """
        scopes_stack = self.grammar.scopes_stack
        columns_stack = self.grammar.columns_stack
        node_actions = self._actions[node]
        vtokens = _AUTO_VIRTUAL_TOKENS.intersection(
            node_actions)
        stack_token = scopes_stack[-1]
        token_value = _TOKEN_PAIRS[stack_token]
        if token_value not in vtokens:
            raise AssertionError(
                token_value, vtokens,
                scopes_stack, columns_stack,
                symbols.peek())
        if stack_token == 'LVERTICAL':
            if not columns_stack:
                raise AssertionError(
                    scopes_stack)
            column = columns_stack[-1]
        else:
            column = None
        token = Result(
            symbol=token_value,
            value=token_value,
            column=column)
        symbols.append(token)
        self._pop_scope_assert(stack_token)
        # print(f'auto-generated: {token_value}')

    def _pop_scope_assert(
            self,
            symbol:
                str
            ) -> None:
        """Pop expected symbol."""
        scopes_stack = self.grammar.scopes_stack
        token_symbol = scopes_stack[-1]
        if token_symbol != symbol:
            raise AssertionError(
                token_symbol)
        scopes_stack.pop()
        columns_stack = self.grammar.columns_stack
        if symbol == 'LVERTICAL':
            columns_stack.pop()
        inv = (
            len(scopes_stack) >=
            len(columns_stack))
        if inv:
            return
        raise AssertionError(
            scopes_stack,
            columns_stack)

    def _generate_dedents(
            self,
            symbols
            ) -> None:
        """Insert dedents.

        Inserts `RVERTICAL` due to dedent.
        """
        scopes_stack = self.grammar.scopes_stack
        columns_stack = self.grammar.columns_stack
        if not columns_stack:
            return
        if not scopes_stack:
            raise AssertionError(columns_stack)
        # get box column
        box_column = columns_stack[-1]
        if box_column < 0:
            raise AssertionError(box_column)
        # get next-token column
        next_token = symbols.peek()
        not_generate = (
            next_token.symbol == 'RVERTICAL' or
                # CASE: nested vertical expressions,
                # avoid circular recursion
            next_token.column is None or
                # nonleaf next
            next_token.column > box_column)
                # no dedent
        if not_generate:
            return
        # dedent: generate `RVERTICAL`
        dedent = _prs_lex.Token(
            symbol='RVERTICAL',
            value='RVERTICAL',
            column=box_column,
            row=next_token.row,
            start=None)
        index = _utils.rindex(
            'LVERTICAL', scopes_stack)
        scopes_stack.pop(index)
        columns_stack.pop()
        symbols.append(dedent)
        # print('RVERTICAL by dedent')
        if len(scopes_stack) < len(columns_stack):
            raise AssertionError(
                len(scopes_stack),
                len(columns_stack))

    def _print_info(
            self,
            symbols,
            results
            ) -> None:
        """Print information."""
        next_symbols = list()
        for _ in range(2):
            if symbols.peek() is None:
                break
            next_symbols.append(symbols.pop())
        print(
            results[-1:],
            next_symbols,
            self.grammar.scopes_stack,
            self.grammar.columns_stack)


class Parser:
    """Parser of TLA+ modules."""

    def __init__(
            self
            ) -> None:
        self._lexer = None
        self._parser = None

    def parse(
            self,
            module_text:
                str
            ) -> tuple:
        """Return syntax tree from `module_text`."""
        if self._parser is None:
            self._lexer = OperatorLexer()
            self._parser = GeneratingParser()
        tokens = self._lexer.parse(module_text)
        result = self._parser.parse(tokens)
        if result is None:
            raise RuntimeError
        tree = result.value
        tree = _tla_ast.map_steps_to_proofs(tree)
        return tree


def lex(
        text:
            str
        ) -> list[
            _p.Result]:
    """Parse lexemes."""
    lexer = OperatorLexer()
    tokens = lexer.parse(text)
    tokens = list(tokens)
    # for token in tokens:
    #     print(token)
    return tokens


class ExprParser(
        Parser):
    """Parser of TLA+ expressions."""

    def parse(
            self,
            tla_expr:
                str
            ) -> _ty.Any:
        """Parse a TLA+ expression."""
        tla_module_text = f'''
            ---- MODULE name ----
            AXIOM name == \n{tla_expr}
            ====
            '''
        module_tree = super().parse(
            tla_module_text)
        expr_tree = module_tree.units[0].expression
        return expr_tree


def parse(
        module_text:
            str
        ) -> tuple:
    """Return syntax tree for `module_text`."""
    if not hasattr(parse, 'parser'):
        parse.parser = Parser()
    return parse.parser.parse(module_text)


def parse_expr(
        expr_text:
            str
        ) -> tuple:
    """Return syntax tree for `expr_text`."""
    if not hasattr(parse_expr, 'parser'):
        parse_expr.parser = ExprParser()
    return parse_expr.parser.parse(expr_text)


def _parse_file(
        filename:
            str
        ) -> None:
    """Parsing file `filename`."""
    with open(filename, 'r') as fd:
        file_text = fd.read()
    tree = parse(file_text)
    print(tree)
    _tla_ast.pprint_tree(tree)


def _main():
    """Entry point."""
    args = _parse_args()
    filename = args.filename
    _parse_file(filename)


def _parse_args(
        ) -> _arg.Namespace:
    """Return arguments."""
    parser = _arg.ArgumentParser()
    parser.add_argument(
        'filename',
        help='TLA+ file to parse')
    return parser.parse_args()


if __name__ == '__main__':
    _main()
