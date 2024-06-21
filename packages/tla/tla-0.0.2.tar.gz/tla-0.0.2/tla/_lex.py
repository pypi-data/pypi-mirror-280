"""Lexer for TLA+."""
import argparse as _arg
import logging
import time

import parstools._lex as _lex
import tla._langdef as _langdef
import tla._utils as _utils


logger = logging.getLogger(__name__)


COMMENT_TOKENS = {
    'UNILINE_COMMENT':
        r' \\ \* [^\n]* \n',
    'MULTILINE_COMMENT':
        None,
        # `(* ... *)`
    }
_utils.assert_len(COMMENT_TOKENS, 2)
_LITERAL_LEXEMES = {
    'BINARY_INTEGER':
        r'''
        (
              \\b
            | \\B
        )
        [0-1]+
        ''',
    'DASH_LINE':
        r' \-\-\-\-(\-)* ',
    'EQ_LINE':
        r' ====(=)* ',
    'HEXADECIMAL_INTEGER':
        r'''
        (
              \\h
            | \\H
        )
        (
              [0-9]
            | [A-F]
        )+
        ''',
    'OCTAL_INTEGER':
        r'''
        (
              \\o
            | \\O
        )
        [0-7]+
        ''',
    'STEP_NUMBER':
        rf'''
        <[0-9]+>
        [a-zA-Z0-9_]*
        \.*
        ''',
    'STEP_NUMBER_ASTERISK':
        r'''
        <\*>
        \.*
        ''',
    'STEP_NUMBER_PLUS':
        r'''
        <\+>
        \.*
        ''',
    }
_utils.assert_len(_LITERAL_LEXEMES, 8)
_OTHER_TOKENS = {
    'FLOAT',
    'DECIMAL_INTEGER',
    'NAME',
    'MULTILINE_STRING_LITERAL',
    'SF_',
    'STRING_LITERAL',
    'WF_',
    }
_BSLASH_SUFFIXES = {
    'A',
    'AA',
    'approx',
    'asymp',
    'bigcirc',
    'bullet',
    'cap',
    'cdot',
    'circ',
        # synonym to `\o`
    'cong',
    'cup',
    'div',
    'doteq',
    'E',
    'EE',
    'equiv',
        # synonym to `<=>`
    'geq',
        # synonym to `>=`
    'gg',
    'in',
    'intersect',
        # synonym to `\cap`
    'land',
        # synonym to `/\`
    'leadsto',
        # synonym to `~>`
    'leq',
        # synonym to `<=`
    'll',
    'lnot',
        # synonym to `~`
    'lor',
        # synonym to `\/`
    'mod',
        # synonym to `%`
    'neg',
        # synonym to `~`
    'notin',
    'o',
    'odot',
        # synonym to `(.)`
    'ominus',
        # synonym to `(-)`
    'oplus',
        # synonym to `(+)`
    'oslash',
        # synonym to `(\)`
    'otimes',
        # synonym to `(\X)`
    'prec',
    'preceq',
    'propto',
    'setminus',
        # synonym to `\`
    'sim',
    'simeq',
    'sqcap',
    'sqcup',
    'sqsubset',
    'sqsubseteq',
    'sqsupset',
    'sqsupseteq',
    'star',
    'subset',
    'subseteq',
    'succ',
    'succeq',
    'supset',
    'supseteq',
    'times',
        # synonym to `\X`
    'union',
        # synonym to `\cup`
    'uplus',
    'wr',
    'X',
        # CARTESIAN
    }
_utils.assert_len(_BSLASH_SUFFIXES, 59)
_PICTORIAL_LEXEMES = {
    '=>':
        'EQ_RANGLE',
    '<=>':
        'LANGLE_EQ_RANGLE',
    '~':
        'TILDE',
    "'":
        'PRIME',
    '^+':
        'CIRCUMFLEX_PLUS',
    '^*':
        'CIRCUMFLEX_ASTERISK',
    '^#':
        'CIRCUMFLEX_HASHMARK',
    '(+)':
        'OPLUS',
    '(-)':
        'ODASH',
    '(/)':
        'OSLASH',
    '(.)':
        'ODOT',
    r'(\X)':
        'OCARTESIAN',
    '/':
        'SLASH',
    '//':
        'DOUBLE_SLASH',
    '\\':
        'BSLASH',
    '/\\':
        'AND',
    r'\/':
        'OR',
    '??':
        'DOUBLE_QUESTION',
    '.':
        'DOT',
    '..':
        'DOUBLE_DOT',
    '...':
        'TRIPLE_DOT',
    '=':
        'EQ',
    '==':
        'DOUBLE_EQ',
    '|':
        'PIPE',
    '||':
        'DOUBLE_PIPE',
    '&':
        'ET',
    '&&':
        'DOUBLE_ET',
    '$':
        'DOLLAR',
    '$$':
        'DOUBLE_DOLLAR',
    '@':
        'AT',
    '@@':
        'DOUBLE_AT',
    '+':
        'PLUS',
    '++':
        'DOUBLE_PLUS',
    '-.':
        'DASH_DOT',
    '-':
        'DASH',
    '--':
        'DOUBLE_DASH',
    '*':
        'ASTERISK',
    '**':
        'DOUBLE_ASTERISK',
    '^':
        'CIRCUMFLEX',
    '^^':
        'DOUBLE_CIRCUMFLEX',
    '!':
        'EXCLAMATION',
    '!!':
        'DOUBLE_EXCLAMATION',
    '%':
        'PERCENT',
    '%%':
        'DOUBLE_PERCENT',
    '/=':
        'NEQ',
    '#':
        'HASHMARK',
    '##':
        'DOUBLE_HASHMARK',
    '|-':
        'PIPE_DASH',
    '|=':
        'PIPE_EQ',
    '-|':
        'DASH_PIPE',
    '=|':
        'EQ_PIPE',
    ':':
        'COLON',
    '::':
        'DOUBLE_COLON',
    ':=':
        'COLON_EQ',
    '::=':
        'DOUBLE_COLON_EQ',
    '<:':
        'LANGLE_COLON',
    ':>':
        'COLON_RANGLE',
    ',':
        'COMMA',
    '<-':
        'LARROW',
    '->':
        'RARROW',
    '|->':
        'MAPSTO',
    '-+->':
        'ARROW_PLUS',
    '~>':
        'LEADSTO',
    '(':
        'LPAREN',
    ')':
        'RPAREN',
    '{':
        'LBRACE',
    '}':
        'RBRACE',
    '[':
        'LBRACKET',
    ']':
        'RBRACKET',
    ']_':
        'RBRACKET_UNDERSCORE',
    '[]':
        'LBRACKET_RBRACKET',
    '<':
        'LANGLE',
    '>':
        'RANGLE',
    '<>':
        'LANGLE_RANGLE',
    '<<':
        'DOUBLE_LANGLE',
    '>>':
        'DOUBLE_RANGLE',
    '>>_':
        'DOUBLE_RANGLE_UNDERSCORE',
    '=<':
        'EQ_LANGLE',
    '<=':
        'LANGLE_EQ',
    '>=':
        'RANGLE_EQ',
    '_':
        'UNDERSCORE',
    }
_utils.assert_len(_PICTORIAL_LEXEMES, 81)
_SYNONYMS = {
    '<=>':
        r'\equiv',
    '/\\':
        r'\land',
    r'\/':
        r'\lor',
    # '#':
    #     '/=',
    '\\':
        r'\setminus',
    r'\cap':
        r'\intersect',
    r'\cup':
        r'\union',
    r'\X':
        r'\times',
    '~>':
        r'\leadsto',
    '>=':
        r'\geq',
    '%':
        r'\mod',
    '(+)':
        r'\oplus',
    '(-)':
        r'\ominus',
    '(.)':
        r'\odot',
    '(/)':
        r'\oslash',
    r'(\X)':
        r'\otimes',
    r'\circ':
        r'\o',
    '~':
        (r'\neg', r'\lnot'),
    '=<':
        (r'\leq',),  # '<='
    }
_utils.assert_len(_SYNONYMS, 18)
_TOKEN_RENAMING = {
    'BSLASH_CAP':
        'CAP',
    'BSLASH_CIRC':
        'CIRC',
    'BSLASH_CUP':
        'CUP',
    'BSLASH_TIMES':
        'CARTESIAN',
    'BSLASH_X':
        'CARTESIAN',
    # 'HASHMARK':
    #     'NEQ',
    }
_utils.assert_len(_TOKEN_RENAMING, 5)


def map_lexemes_to_tokens(
        ) -> dict[
            str, str]:
    """Return mapping lexemes to token names."""
    lextok = {
        rf'\{s}':
            f'BSLASH_{s.upper()}'
        for s in _BSLASH_SUFFIXES}
    lextok |= _PICTORIAL_LEXEMES
    op_synonyms = _make_synonymous_lexemes()
    for op, synonyms in op_synonyms.items():
        for other in synonyms:
            token_name = lextok[op]
            _add_to_dict(other, token_name, lextok)
    def mapper(value):
        return _TOKEN_RENAMING.get(value, value)
    lextok = _utils.map_values(mapper, lextok)
    return lextok


def _make_synonymous_lexemes(
        ) -> dict[
            str, str]:
    """Return `dict` of synonyms."""
    def mapper(x):
        if isinstance(x, str):
            return (x,)
        return x
    return _utils.map_values(
        mapper, _SYNONYMS)


def _add_to_dict(
        key,
        value,
        mapping):
    """Set `mapping[key] = value`.

    Raise `AssertionError` if `key`
    is already in `mapping`.
    """
    add = (
        key not in mapping or
        _is_bslash_operator(key))
    if add:
        mapping[key] = value
        return
    raise AssertionError(
        f'{key = }, '
        f'{mapping = }')


# lexer states
_INITIAL_LEXER_STATE = 'initial'
_COMMENT_LEXER_STATE = 'multilinecomment'
_STRING_LEXER_STATE = 'string'
_MULTILINE_STRING_LEXER_STATE = 'multilinestring'


class Lexer(
        _lex.StatefulLexer):
    """Grammar to build TLA+ lexer."""

    lexing_states = (
        _INITIAL_LEXER_STATE,
        _COMMENT_LEXER_STATE,
        _STRING_LEXER_STATE,
        _MULTILINE_STRING_LEXER_STATE)

    def __init__(
            self
            ) -> None:
        self._lextok = map_lexemes_to_tokens()
        self.tokens = sorted(set().union(
            _langdef.KEYWORDS,
            COMMENT_TOKENS,
            _LITERAL_LEXEMES,
            _OTHER_TOKENS,
            self._lextok.values(),
            ))
        self.token_types = self.tokens
        self.states = (
            (_COMMENT_LEXER_STATE,
                'exclusive'),
            (_STRING_LEXER_STATE,
                'exclusive'),
            (_MULTILINE_STRING_LEXER_STATE,
                'exclusive'))
        self._keywords = set(_langdef.KEYWORDS)
        self._make_token_vars()
        # state
        self._comment_level: int = 0
        self._comment_start: int | None = None
        self._line_number: int = 0
        self._string_start: int | None = None
        super().__init__()

    def _make_token_vars(
            self
            ) -> None:
        regexes = dict(_LITERAL_LEXEMES)
        regexes.update(COMMENT_TOKENS)
        lextok = {
            k: v
            for k, v in self._lextok.items()
            if not _is_bslash_operator(k)}
        _utils.make_token_grammar(
            lextok, regexes, self)

    def parse(
            self,
            text:
                str):
        """Return tokens for `text`.

        To tokenize the lexeme `ELIF` as
        an identifier:

        ```python
        self._keywords.remove('ELIF')
        ```
        """
        # reset the lexer's state
        self._line_number = 0
        self._string_start = None
        tokens = super().parse(text)
        return _lex.add_row_column(
            text, tokens)

    def t_COMMENT(
            self,
            token):
        r' \( \* '
        self._comment_level = 1
        self.lexing_state = _COMMENT_LEXER_STATE
        self._comment_start = token.start

    def t_multilinecomment_left_paren(
            self,
            token):
        r' \( \* '
        self._comment_level += 1

    def t_multilinecomment_right_paren(
            self,
            token):
        r' \* \) '
        self._comment_level -= 1
        if self._comment_level < 0:
            raise AssertionError(
                self._comment_level)
        if self._comment_level > 0:
            return
        self.lexing_state = _INITIAL_LEXER_STATE
        # make token
        start = self._comment_start
        end = token.start + len(token.value)
        value = self.input_text[start:end]
        return _lex.Token(
            symbol='MULTILINE_COMMENT',
            value=value,
            start=start)

    def t_multilinecomment_newline(
            self,
            token):
        r' \n '
        self._line_number += 1

    def t_multilinecomment_other(
            self,
            token):
        r' [^\n(\*]+ '
        return None

    def t_multilinecomment_lparen(
            self,
            token):
        r' \( '
        return None

    def t_multilinecomment_asterisk(
            self,
            token):
        r' \* '
        return None

    def t_MULTILINE_STRING(
            self,
            token):
        r' """ '
        self._string_start = token.start
        self.lexing_state = _MULTILINE_STRING_LEXER_STATE

    def t_multilinestring_escaped_quotes(
            self,
            token):
        r"""
          \\ t
        | \\ n
        | \\ f
        | \\ r
        | \\ \\
        """

    def t_multilinestring_newline(
            self,
            token):
        r' \n '

    def t_multilinestring_other_characters(
            self,
            token):
        r' [^"\\]+ '

    def t_multilinestring_closing(
            self,
            token):
        r' """ '
        return self._collect_string(
            token, 'MULTILINE_STRING_LITERAL')

    def t_multilinestring_quotes(
            self,
            token):
        r"""
          ""
        | "
        """

    def t_STRING(
            self,
            token):
        r' " '
        self._string_start = token.start
        self.lexing_state = _STRING_LEXER_STATE

    def t_string_escaped_quotes(
            self,
            token):
        r"""
          \\ "
        | \\ t
        | \\ n
        | \\ f
        | \\ r
        | \\ \\
        """

    def t_string_newline(
            self,
            token):
        r' \n '
        raise ValueError(
            f'Newline within string {t}.')

    def t_string_other_characters(
            self,
            token):
        r' [^"\\]+ '

    def t_string_closing(
            self,
            token):
        r' " '
        return self._collect_string(
            token, 'STRING_LITERAL')

    def _collect_string(
            self,
            token,
            token_type):
        self.lexing_state = _INITIAL_LEXER_STATE
        # form token
        start = self._string_start
        end = token.start + len(token.value)
        value = self.input_text[start:end]
        return _lex.Token(
            symbol=token_type,
            value=value,
            start=start)

    def t_SF_WF(
            self,
            token):
        r"""
          SF_
        | WF_
        """
        return _lex.Token(
            symbol=token.value,
            value=token.value,
            start=token.start)

    def t_NAME(
            self,
            token):
        r"""
        [a-zA-Z_0-9]*
        [a-zA-Z]
        [a-zA-Z_0-9]*
        """
        if token.value in self._keywords:
            return _lex.Token(
                symbol=token.value,
                value=token.value,
                start=token.start)
        return token

    def t_BSLASH_TOKEN(
            self,
            token):
        r' \\ [a-zA-Z]+ '
        if token.value not in self._lextok:
            raise ValueError(
                f'`{token.value}` is not '
                'a known lexeme. Known lexemes '
                'of this form are in: '
                f'{self._lextok}')
        symbol = self._lextok[token.value]
        return _lex.Token(
            symbol=symbol,
            value=token.value,
            start=token.start)

    def t_FLOAT(
            self,
            token):
        r"""
        [0-9]+
        \.
        [0-9]+
        """
        return token

    def t_DECIMAL_INTEGER(
            self,
            token):
        ' [0-9]+ '
        return token

    t_omit = r' \x20* '

    def t_NEWLINE(
            self,
            token):
        r' \n+ '
        self._line_number += token.value.count('\n')

    def t_tab(
            self,
            token):
        r' \t '
        raise ValueError(
            r'TAB characters (`\t`) '
            'are unsupported.')


def _is_bslash_operator(
        lexeme):
    r"""True if `lexeme` matches `\[a-zA-Z]`."""
    return (
        lexeme.startswith('\\') and
        lexeme[1:].isalpha())


def _main():
    # read file
    args = _parse_args()
    filename = args.filename
    with open(filename, 'r') as fd:
        file_text = fd.read()
    # lex
    lexer = Lexer()
    t1 = time.perf_counter()
    tokens = lexer.parse(file_text)
    tokens = list(tokens)
    t2 = time.perf_counter()
    dt = t2 - t1
    for token in tokens:
        print(token)
    print(
        f'Success lexing file: {filename} '
        f'in {dt:2f} seconds')


def _parse_args(
        ) -> _arg.Namespace:
    """Return arguments."""
    parser = _arg.ArgumentParser()
    parser.add_argument(
        'filename',
        help='TLA+ file name to lex')
    return parser.parse_args()


if __name__ == '__main__':
    _main()
