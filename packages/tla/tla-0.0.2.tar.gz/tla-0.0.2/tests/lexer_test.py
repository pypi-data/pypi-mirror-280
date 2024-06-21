"""Tests of module `tla._lex`."""
import pprint
import textwrap as _tw

import tla._lex as _lex


module_example = r'''
comments
---- MODULE example ----
VARIABLE x

\* a one-line comment
\* a nested \* one-line comment

(* This is a multi-line comment. *)
(* This is a multi-line
comment. * (
*)
(* A nested
(* multi-line *)
comment. *)

a == 1.0
b == a + 2

A == x' = x + 1

P == SF_x(A)

THEOREM Thm ==
    ASSUME x = 1
    PROVE x + 1 = 2
PROOF
<1>1. x = 1
    OBVIOUS
<1>2. x + 1 = 1 + 1
    BY <1>1
<1>3. 1 + 1 = 2
    OBVIOUS
<1> QED
    BY <1>2, <1>3
====================
comments
'''


def test_lexing_module_example():
    lexer = _lex.Lexer()
    tokens = lexer.parse(module_example)
    for token in tokens:
        print(token)
    tv = _tokenize(module_example, lexer)
    tv_ = [
        ('NAME', 'comments'),
        ('DASH_LINE', '----'),
        ('MODULE', 'MODULE'),
        ('NAME', 'example'),
        ('DASH_LINE', '----'),
        ('VARIABLE', 'VARIABLE'),
        ('NAME', 'x'),
        ('UNILINE_COMMENT', '\\* a one-line comment\n'),
        ('UNILINE_COMMENT',
         '\\* a nested \\* one-line comment\n'),
        ('MULTILINE_COMMENT',
         '(* This is a multi-line comment. *)'),
        ('MULTILINE_COMMENT',
        '(* This is a multi-line\ncomment. * (\n*)'),
        ('MULTILINE_COMMENT',
        '(* A nested\n(* multi-line *)\ncomment. *)'),
        ('NAME', 'a'),
        ('DOUBLE_EQ', '=='),
        ('FLOAT', '1.0'),
        ('NAME', 'b'),
        ('DOUBLE_EQ', '=='),
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('DECIMAL_INTEGER', '2'),
        ('NAME', 'A'),
        ('DOUBLE_EQ', '=='),
        ('NAME', 'x'),
        ('PRIME', "'"),
        ('EQ', '='),
        ('NAME', 'x'),
        ('PLUS', '+'),
        ('DECIMAL_INTEGER', '1'),
        ('NAME', 'P'),
        ('DOUBLE_EQ', '=='),
        ('SF_', 'SF_'),
        ('NAME', 'x'),
        ('LPAREN', '('),
        ('NAME', 'A'),
        ('RPAREN', ')'),
        ('THEOREM', 'THEOREM'),
        ('NAME', 'Thm'),
        ('DOUBLE_EQ', '=='),
        ('ASSUME', 'ASSUME'),
        ('NAME', 'x'),
        ('EQ', '='),
        ('DECIMAL_INTEGER', '1'),
        ('PROVE', 'PROVE'),
        ('NAME', 'x'),
        ('PLUS', '+'),
        ('DECIMAL_INTEGER', '1'),
        ('EQ', '='),
        ('DECIMAL_INTEGER', '2'),
        ('PROOF', 'PROOF'),
        ('STEP_NUMBER', '<1>1.'),
        ('NAME', 'x'),
        ('EQ', '='),
        ('DECIMAL_INTEGER', '1'),
        ('OBVIOUS', 'OBVIOUS'),
        ('STEP_NUMBER', '<1>2.'),
        ('NAME', 'x'),
        ('PLUS', '+'),
        ('DECIMAL_INTEGER', '1'),
        ('EQ', '='),
        ('DECIMAL_INTEGER', '1'),
        ('PLUS', '+'),
        ('DECIMAL_INTEGER', '1'),
        ('BY', 'BY'),
        ('STEP_NUMBER', '<1>1'),
        ('STEP_NUMBER', '<1>3.'),
        ('DECIMAL_INTEGER', '1'),
        ('PLUS', '+'),
        ('DECIMAL_INTEGER', '1'),
        ('EQ', '='),
        ('DECIMAL_INTEGER', '2'),
        ('OBVIOUS', 'OBVIOUS'),
        ('STEP_NUMBER', '<1>'),
        ('QED', 'QED'),
        ('BY', 'BY'),
        ('STEP_NUMBER', '<1>2'),
        ('COMMA', ','),
        ('STEP_NUMBER', '<1>3'),
        ('EQ_LINE', '===================='),
        ('NAME', 'comments'),
        ]
    assert tv == tv_, tv


def test_lexing_nested_multiline_comments():
    lexer = _lex.Lexer()
    source = '''
        ------ MODULE nested_multiline -----
        (* outer comment
            (* inner comment *)
        *)
        =====
        '''
    tv = _tokenize(source, lexer)
    tv_ = [
        ('DASH_LINE', '------'),
        ('MODULE', 'MODULE'),
        ('NAME', 'nested_multiline'),
        ('DASH_LINE', '-----'),
        ('MULTILINE_COMMENT',
        '''(* outer comment
            (* inner comment *)
        *)'''),
        ('EQ_LINE', '=====')]
    assert tv == tv_, tv


def test_lexing_nested_uniline_comments():
    lexer = _lex.Lexer()
    source = r'''
        ---- MODULE nested_uniline -----
        \* outer comment \* inner comment
        ====
        '''
    tv = _tokenize(source, lexer)
    tv_ = [
        ('DASH_LINE', '----'),
        ('MODULE', 'MODULE'),
        ('NAME', 'nested_uniline'),
        ('DASH_LINE', '-----'),
        ('UNILINE_COMMENT',
            r'\* outer comment \* '
            'inner comment\n'),
        ('EQ_LINE', '====')]
    assert tv == tv_, tv


def test_uniline_inside_multiline_comments():
    lexer = _lex.Lexer()
    source = r'''
        ----- MODULE nested_mixed ----
        (* multiline comment \* uniline comment *)
        ======
        '''
    tv = _tokenize(source, lexer)
    tv_ = [
        ('DASH_LINE', '-----'),
        ('MODULE', 'MODULE'),
        ('NAME', 'nested_mixed'),
        ('DASH_LINE', '----'),
        ('MULTILINE_COMMENT',
            '(* multiline comment '
            r'\* uniline comment *)'),
        ('EQ_LINE', '======')]
    assert tv == tv_, tv


def test_multiline_inside_uniline_comments():
    lexer = _lex.Lexer()
    source = r'''
        ---- MODULE nested_mixed ----
        \* uniline comment (* multiline comment *)
        ====
        '''
    tv = _tokenize(source, lexer)
    tv_ = [
        ('DASH_LINE', '----'),
        ('MODULE', 'MODULE'),
        ('NAME', 'nested_mixed'),
        ('DASH_LINE', '----'),
        ('UNILINE_COMMENT',
            r'\* uniline comment '
            '(* multiline comment *)\n'),
        ('EQ_LINE', '====')]
    assert tv == tv_, tv


def test_string_meta_sequences():
    lexer = _lex.Lexer()
    source = r'''
        ---- MODULE string_meta ----
        quote == "\""
        literal == "\\"
        tab == "\t"
        line_feed == "\n"
        form_feed == "\f"
        carriage_return == "\r"
        ====
        '''
    tv = _tokenize(source, lexer)
    tv_ = [
        ('DASH_LINE', '----'),
        ('MODULE', 'MODULE'),
        ('NAME', 'string_meta'),
        ('DASH_LINE', '----'),
        # quote == "\""
        ('NAME', 'quote'),
        ('DOUBLE_EQ', '=='),
        ('STRING_LITERAL', r'"\""'),
        # literal == "\\"
        ('NAME', 'literal'),
        ('DOUBLE_EQ', '=='),
        ('STRING_LITERAL', r'"\\"'),
        # tab == "\t"
        ('NAME', 'tab'),
        ('DOUBLE_EQ', '=='),
        ('STRING_LITERAL', r'"\t"'),
        # line_feed == "\n"
        ('NAME', 'line_feed'),
        ('DOUBLE_EQ', '=='),
        ('STRING_LITERAL', r'"\n"'),
        # form_feed == "\f"
        ('NAME', 'form_feed'),
        ('DOUBLE_EQ', '=='),
        ('STRING_LITERAL', r'"\f"'),
        # carriage_return == "\r"
        ('NAME', 'carriage_return'),
        ('DOUBLE_EQ', '=='),
        ('STRING_LITERAL', r'"\r"'),
        ('EQ_LINE', '===='),
        ]
    assert tv == tv_, tv


def test_boolean_div_setminus():
    lexer = _lex.Lexer()
    source = r'''
        /\ a / b
        /\ \/ c \ d
        '''
    tv = _tokenize(source, lexer)
    tv_ = [
        # /\ a / b
        ('AND', '/\\'),
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        # /\ \/ c \ d
        ('AND', '/\\'),
        ('OR', '\\/'),
        ('NAME', 'c'),
        ('BSLASH', '\\'),
        ('NAME', 'd'),
        ]
    assert tv == tv_, tv


def test_operator_double_at():
    lexer = _lex.Lexer()
    # `@@`
    text = r'''
        f @@ g
        '''
    tv = _tokenize(text, lexer)
    tv_ = [
        ('NAME', 'f'),
        ('DOUBLE_AT', '@@'),
        ('NAME', 'g'),
        ]
    assert tv == tv_, tv
    # `@@@`
    text = r'''
        f @@@ g
        '''
    tv = _tokenize(text, lexer)
    tv_ = [
        ('NAME', 'f'),
        ('DOUBLE_AT', '@@'),
        ('AT', '@'),
        ('NAME', 'g'),
        ]
    assert tv == tv_, tv


def _tokenize(
        source:
            str,
        lexer
        ) -> list[
            tuple[str, str]]:
    """Return `list` of pairs `(type, value)`.

    @type lexer:
        the method `lexer.parse()`
        returns an iterator
    """
    return [
        (token.symbol, token.value)
        for token in
            lexer.parse(source)]


if __name__ == '__main__':
    # test_lexing_module_example()
    # test_lexing_nested_multiline_comments()
    # test_lexing_nested_uniline_comments()
    # test_uniline_inside_multiline_comments()
    # test_multiline_inside_uniline_comments()
    # test_string_meta_sequences()
    # test_boolean_div_setminus()
    test_operator_double_at()
