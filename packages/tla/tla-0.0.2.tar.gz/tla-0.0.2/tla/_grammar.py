"""TLA+ context-free grammar with delimiters.

Definition also of operator precedence and associativity.
"""
import itertools as _itr
import typing as _ty

import tla._ast as _ast
import tla._utils as _utils


# The set of fixal operators
# that appear directly in the grammar.
EXCEPT_TOKEN_TYPES: _ty.Final = {
    'EQ', 'BSLASH_IN',
    'CARTESIAN', 'DASH',
    }
_utils.assert_len(
    EXCEPT_TOKEN_TYPES, 4)


class Grammar:
    """LR(1) grammar for parsing TLA+."""

    def __init__(
            self
            ) -> None:
        # self._make_operator_precedence_grammar()
        _utils.format_bnf_docstrings(self)
        _utils.check_bnf_grammar(self)
        self.tokens = None  # set by `Parser._build()`
        self.start = 'start'
        self.root_symbol = 'start'
        self._nodes = _ast.make_nodes()

    # NOTE: This method is unused, available for
    # building a context-free grammar for operators,
    # except for a few cases as for example `A # ~ B`.
    # These cases are handled by the
    # operator-precedence parser that results from
    # using an operator precedence table to
    # resolve shift-reduce ambiguities.
    def _make_operator_precedence_grammar(
            self
            ) -> None:
        """Add equalities about operators.

        These grammar equalities describe the
        precedence, associativity, fixity, and
        arity of prefix, infix, and postfix
        operators.
        """
        # Associativity and precedence of
        # prefix, infix, and postfix operators.
        # This tuple is used to generate the
        # part of the grammar that describes
        # the application of these operators.
        positioning = (
            'OP_1_INFIX',
            'OP_2_INFIX',
            'OP_3_LEFT',
            'OP_4_PREFIX',
            'OP_4_BEFORE',
            'op_5_eq_infix',
            'op_5_bslash_in_between',
            'OP_5_LEFT',
            'OP_5_INFIX',
            'OP_6_LEFT',
            'OP_7_INFIX',
            'OP_8_BEFORE',
            'OP_8_INFIX',
            'OP_8_LEFT',
            'OP_9_BEFORE',
            'OP_9_INFIX',
            'OP_9_LEFT',
            'OP_10_LEFT',
            'OP_10_INFIX',
            'set_of_tuples_between',
            'OP_11_LEFT',
            'op_11_dash_left',
            'op_12_dash_before',
            'OP_12_PREFIX',
                # for `DASH_DOT`
            'OP_13_INFIX',
            'OP_13_LEFT',
            'OP_14_INFIX',
            'OP_15_POSTFIX',
            'OP_15_AFTER',
            # the last name is not mapped
            # to a method automatically
            'function_application',
            )
        tokens_of_symbols = dict(
            op_5_eq_infix='EQ',
            op_5_bslash_in_between='BSLASH_IN',
            op_11_dash_left='DASH',
            op_12_dash_before='DASH',
            set_of_tuples_between='CARTESIAN',
            )
        _utils.make_operator_precedence_grammar(
            positioning, tokens_of_symbols, self)

    def __str__(
            self
            ) -> str:
        """Return grammar of TLA+.

        The grammar originates in
        method docstrings.
        """
        (_, _, _, grammar_text
            ) = _utils.collect_grammar_info(
                self,
                add_braces=False)
        return grammar_text.replace(
            '/\\', '\x20\x20', 1)

    def p_error(
            self,
            token):
        """Handle errors."""
        # tokens = list()
        # while True:
        #     token = self._parser.token()
        #     if token is None:
        #         break
        #     tokens.append(token)
        # rest = ' '.join(tokens)
        raise RuntimeError(
            f'Syntax error at `{token!r}`\n')

    def p_start(
            self, p):
        """start: tla_module"""
        p[0] = p[1]

    def p_module_that_extends(
            self, p):
        """tla_module:
            module_signature
            extends
            units
            EQ_LINE
        """
        p[0] = self._nodes.Module(
            name=p[1],
            extendees=p[2],
            units=p[3])

    def p_module_without_extends(
            self, p):
        """tla_module:
            module_signature
            units
            EQ_LINE
        """
        p[0] = self._nodes.Module(
            name=p[1],
            units=p[2])

    def p_module_with_extends_only(
            self, p):
        """tla_module:
            module_signature
            extends
            EQ_LINE
        """
        p[0] = self._nodes.Module(
            name=p[1],
            units=p[2])

    def p_empty_module(
            self, p):
        """tla_module:
            module_signature
            EQ_LINE
        """
        p[0] = self._nodes.Module(
            name=p[1])

    def p_module_signature(
            self, p):
        """module_signature:
            DASH_LINE expr DASH_LINE
        """
        p[0] = p[2].name

    def p_module_name(
            self, p):
        """expr: MODULE NAME"""
        # This allows `MODULE NAME` to
        # appear inside `DEF` sections
        p[0] = self._nodes.ModuleName(
            name=p[2])

    def p_extends_statement(
            self, p):
        """extends:
            EXTENDS exprs
        """
        p[0] = p[2]

    def p_units_append(
            self, p):
        """units: units unit"""
        p[1].append(p[2])
        p[0] = p[1]

    def p_units_start(
            self, p):
        """units: unit"""
        p[0] = [p[1]]

    def p_unit(
            self, p):
        """unit:
            | operator_def
            | variable_decl
            | constant_decl
            | recursive_decl
            | use_or_hide
            | theorem
            | axiom
            | tla_module
            | instance
            | DASH_LINE
        """
        p[0] = p[1]

    def p_variable_declaration(
            self, p):
        """variable_decl:
            variable_keyword exprs
        """
        p[0] = self._nodes.Variables(
            names=p[2])

    def p_constant_declaration(
            self, p):
        """constant_decl:
            constant_keyword exprs
        """
        p[0] = self._nodes.Constants(
            names=p[2])

    def p_recursive_declaration(
            self, p):
        """recursive_decl:
            RECURSIVE exprs
        """
        p[0] = self._nodes.RecursiveOperators(
            names=p[2])

    def p_keyword_variable(
            self, p):
        """variable_keyword:
            | VARIABLES
            | VARIABLE
        """
        p[0] = p[1]

    def p_keyword_constant(
            self, p):
        """constant_keyword:
            | CONSTANTS
            | CONSTANT
        """
        p[0] = p[1]

    def p_operator_definitions_append(
            self, p):
        """operator_defs:
            operator_defs operator_def
        """
        p[1].append(p[2])
        p[0] = p[1]

    def p_operator_definitions_start(
            self, p):
        """operator_defs: operator_def"""
        p[0] = [p[1]]

    def p_nonlocal_operator_definition(
            self, p):
        """operator_def:
            DEF_SIG
                expr DOUBLE_EQ
                    definiens
        """
        # NOTE: `expr` here for function definitions:
        # `f[x \in R, y \in S] == ...`
        sig = p[2]
        definiens = p[4]
        p[0] = self._make_operator_definition(
            sig, definiens)

    def _make_operator_definition(
            self,
            sig,
            definiens,
            local=None):
        """Return operator definition."""
        if sig.symbol.name == 'FUNCTION_APPLICATION':
            # function definition
            func_sig = sig.function
            if func_sig.arguments is not None:
                raise ValueError(sig)
            name = func_sig.operator
            exprs = sig.arguments
            definiens = self._nodes.Function(
                declaration=exprs,
                value=definiens)
                # NOTE: causes printing to differ
                # from parsed text
            arity = None
            function = True
        else:
            # operator definition
            name = sig.operator
            arity = sig.arguments
            function = None
        return self._nodes.OperatorDefinition(
            name=name,
            arity=arity,
            definiens=definiens,
            local=local,
            function=function)

    def p_local_operator_definition(
            self, p):
        """operator_def:
            DEF_SIG LOCAL
                expr DOUBLE_EQ
                    definiens
        """
        sig = p[3]
        definiens = p[5]
        local = True
        p[0] = self._make_operator_definition(
            sig, definiens, local)

    def p_operator_arity_without_args(
            self, p):
        """operator_arity:
            NAME
        """
        p[0] = self._nodes.OperatorApplication(
            operator=p[1])

    def p_operator_arity_with_args(
            self, p):
        """operator_arity:
            NAME LPAREN
                operator_arity_args
            RPAREN
        """
        # NOTE: pattern for higher-order operators
        p[0] = self._nodes.OperatorApplication(
            operator=p[1],
            arguments=p[3])

    def p_operator_arity_args_append(
            self, p):
        """operator_arity_args:
            operator_arity_args COMMA
            operator_arity_arg
        """
        p[0] = p[1]
        p[1].append(p[3])

    def p_operator_arity_args_start(
            self, p):
        """operator_arity_args:
            operator_arity_arg
        """
        p[0] = [p[1]]

    def p_operator_arity_arg(
            self, p):
        """operator_arity_arg:
            | operator_arity
            | UNDERSCORE
        """
        p[0] = p[1]

    def p_definiens(
            self, p):
        """definiens:
            | expr
            | instance
        """
        p[0] = p[1]

    def p_use_or_hide(
            self, p):
        """use_or_hide:
            | use_unit
            | hide_unit
        """
        p[0] = p[1]

    def p_use_unit_full(
            self, p):
        """use_unit:
            use_only
                exprs
                def_keyword name_list
        """
        p[0] = self._nodes.Use(
            only=p[1],
            facts=p[2],
            names=p[4])

    def p_use_unit_with_facts(
            self, p):
        """use_unit:
            use_only
                exprs
        """
        p[0] = self._nodes.Use(
            only=p[1],
            facts=p[2])

    def p_use_unit_with_defs(
            self, p):
        """use_unit:
            use_only
                def_keyword name_list
        """
        p[0] = self._nodes.Use(
            only=p[1],
            names=p[3])

    def p_module_unit_hide(
            self, p):
        """hide_unit:
            HIDE
                exprs
                def_keyword name_list
        """
        p[0] = self._nodes.Hide(
            facts=p[2],
            names=p[4])

    def p_use_without_only(
            self, p):
        """use_only: USE"""
        p[0] = False

    def p_use_with_only(
            self, p):
        """use_only: USE ONLY"""
        p[0] = True

    def p_name_list_append(
            self, p):
        """name_list:
            | name_list COMMA general_identifier
            | name_list COMMA module_name
            | name_list COMMA
                VERTICAL_OPERATOR
                LVERTICAL
        """
        p[1].append(p[3])
        p[0] = p[1]

    def p_name_list_start(
            self, p):
        """name_list:
            | general_identifier
            | module_name
            | VERTICAL_OPERATOR
              LVERTICAL
        """
        p[0] = [p[1]]

    def p_named_axiom(
            self, p):
        """axiom:
            axiom_keyword
                DEF_SIG NAME DOUBLE_EQ
                    expr
        """
        p[0] = self._nodes.Axiom(
            name=p[3],
            expression=p[5],
            axiom_keyword=p[1])

    def p_unnamed_axiom(
            self, p):
        """axiom: axiom_keyword expr"""
        p[0] = self._nodes.Axiom(
            expression=p[2],
            axiom_keyword=p[1])

    def p_axiom_keyword(
            self, p):
        """axiom_keyword:
            | AXIOM
            | ASSUME
            | ASSUMPTION
        """
        p[0] = p[1]

    def p_named_theorem(
            self, p):
        """theorem:
            | theorem_keyword
                DEF_SIG NAME DOUBLE_EQ
                    sequent
                    theorem_proof
            | theorem_keyword
                DEF_SIG NAME DOUBLE_EQ
                    expr
                    theorem_proof
        """
        p[0] = self._nodes.Theorem(
            theorem_keyword=p[1],
            name=p[3],
            goal=p[5],
            proof=p[6])

    def p_unnamed_theorem(
            self, p):
        """theorem:
            | theorem_keyword
                sequent
                theorem_proof
            | theorem_keyword
                expr
                theorem_proof
        """
        p[0] = self._nodes.Theorem(
            theorem_keyword=p[1],
            goal=p[2],
            proof=p[3])

    def p_named_theorem_without_proof(
            self, p):
        """theorem:
            | theorem_keyword
                DEF_SIG NAME DOUBLE_EQ
                    sequent
            | theorem_keyword
                DEF_SIG NAME DOUBLE_EQ
                    expr
        """
        p[0] = self._nodes.Theorem(
            theorem_keyword=p[1],
            name=p[3],
            goal=p[5])

    def p_unnamed_theorem_without_proof(
            self, p):
        """theorem:
            | theorem_keyword
                sequent
            | theorem_keyword
                expr
        """
        p[0] = self._nodes.Theorem(
            theorem_keyword=p[1],
            goal=p[2])

    def p_theorem_keyword(
            self, p):
        """theorem_keyword:
            | PROPOSITION
            | LEMMA
            | THEOREM
            | COROLLARY
        """
        p[0] = p[1]

    def p_sequent(
            self, p):
        """sequent:
            ASSUME asms
            PROVE expr
        """
        p[0] = self._nodes.Sequent(
            assume=p[2],
            prove=p[4])

    def p_assumptions_append(
            self, p):
        """asms: asms COMMA asm"""
        p[1].append(p[3])
        p[0] = p[1]

    def p_assumptions_start(
            self, p):
        """asms: asm"""
        p[0] = [p[1]]

    def p_assumption_new_decl(
            self, p):
        """asm: NEW asm_decl"""
        decl = p[2]
        p[0] = self._nodes.OperatorDeclaration(
            name=decl.name,
            level=decl.level,
            new_keyword=True)

    def p_assumption(
            self, p):
        """asm: asm_decl"""
        p[0] = p[1]

    def p_assumption_new_constant(
            self, p):
        """asm: NEW expr"""
        # read `tla._ast.op_decl_name_bound_arity()`
        #
        # TODO: check that this is one of:
        # - unbounded NAME
        # - bounded NAME
        # - unbounded non-nullary
        #   nonfixal declaration
        # - unbounded fixal declaration
        p[0] = self._nodes.OperatorDeclaration(
            name=p[2],
            new_keyword=True)

    def p_assumption_sequent(
            self, p):
        """asm:
            | sequent
            | expr
        """
        p[0] = p[1]

    def p_variable_declaration_in_sequent(
            self, p):
        """asm_decl: VARIABLE NAME"""
        p[0] = self._nodes.OperatorDeclaration(
            name=p[2],
            level='VARIABLE')

    def p_unbounded_constant_decl_in_sequent(
            self, p):
        """asm_decl: CONSTANT expr"""
        # method `tla._ast.op_decl_name_bound_arity()`
        # gets the name, bound, and arity from `expr`
        #
        # TODO: check that this is either:
        # - bounded nullary
        # - unbounded nullary
        # - unbounded non-nullary
        #   nonfixal declaration
        # - unbounded fixal declaration
        p[0] = self._nodes.OperatorDeclaration(
            name=p[2],
            level=p[1])

    def p_levely_declaration_in_sequent(
            self, p):
        """asm_decl: level_specifier expr"""
        # read `tla._ast.op_decl_name_bound_arity()`
        p[0] = self._nodes.OperatorDeclaration(
            name=p[2],
            level=p[1])

    def p_state_level_specifier(
            self, p):
        """level_specifier: STATE"""
        # The keyword `CONSTANT`, too,
        # is a level specifier.
        # The parser productions for
        # `CONSTANT` declarations in sequents
        # are in another area of the grammar
        # in order to avoid
        # shift/reduce ambiguities when
        # building the transitions table of
        # the LALR(1) parser.
        p[0] = 'STATE_LEVEL'

    def p_action_level_specifier(
            self, p):
        """level_specifier: ACTION"""
        p[0] = 'ACTION_LEVEL'

    def p_temporal_level_specifier(
            self, p):
        """level_specifier: TEMPORAL"""
        p[0] = 'TEMPORAL_LEVEL'

    def p_parentheses(
            self, p):
        """paren: LPAREN expr RPAREN"""
        p[0] = self._nodes.Parentheses(
            expression=p[2],)

    def p_instance_verbatim_local(
            self, p):
        """instance: LOCAL INSTANCE NAME"""
        p[0] = self._nodes.Instance(
            name=p[3],
            local=True)

    def p_instance_verbatim_nonlocal(
            self, p):
        """instance: INSTANCE NAME"""
        p[0] = self._nodes.Instance(
            name=p[2])

    def p_instance_with_substitution(
            self, p):
        """instance:
            INSTANCE NAME WITH substitutions
        """
        p[0] = self._nodes.Instance(
            name=p[2],
            with_substitution=p[4])

    def p_substitutions_append(
            self, p):
        """substitutions:
            substitutions COMMA sub
        """
        p[1].append(p[3])
        p[0] = p[1]

    def p_substitutions_start(
            self, p):
        """substitutions: sub"""
        p[0] = [p[1]]

    def p_substitution(
            self, p):
        """sub:
            | replaced_expr LARROW expr
            | replaced_expr LARROW
                vertical_op LVERTICAL RVERTICAL
        """
        name = p[1]
        if not isinstance(name, str):
            raise AssertionError(name)
        p[0] = self._nodes.WithInstantiation(
            name=name,
            expression=p[3])

    def p_replaced_expr(
            self, p):
        """replaced_expr :
            | NAME
            | OP_1_INFIX
            | OP_2_INFIX
            | OP_3_LEFT
            | OP_4_PREFIX
            | OP_4_BEFORE
            | EQ
            | BSLASH_IN
            | OP_5_LEFT
            | OP_5_INFIX
            | OP_6_LEFT
            | OP_7_INFIX
            | OP_8_BEFORE
            | OP_8_INFIX
            | OP_8_LEFT
            | OP_9_BEFORE
            | OP_9_INFIX
            | OP_9_LEFT
            | OP_10_LEFT
            | OP_10_INFIX
            | CARTESIAN
            | OP_11_LEFT
            | DASH
            | OP_12_PREFIX
            | OP_13_INFIX
            | OP_13_LEFT
            | OP_14_INFIX
            | OP_15_POSTFIX
            | OP_15_AFTER
            | VERTICAL_OPERATOR LVERTICAL
        """
        p[0] = p[1]

    def p_lambda(
            self, p):
        """expr:
            LAMBDA exprs COLON
                expr END_LAMBDA
        """
        parameters = p[2]
        for param in parameters:
            if param.arguments:
                raise ValueError(
                    'LAMBDA parameter: ',
                    param)
        p[0] = self._nodes.Lambda(
            parameters=parameters,
            expression=p[4])

    def p_undelimited(
            self, p):
        """undelimited_expr:
            | temporal_quantification
            | constant_quantification
            | choose_expr
            | let_expr
            | case_expr
            | ternary_expr
            | elif_expr
        """
        p[0] = p[1]

    def p_temporal_quantification(
            self, p):
        """temporal_quantification:
            temporal_quantifier exprs COLON
                expr
            end_temporal_quantifier
        """
        p[0] = self._nodes.TemporalQuantification(
            quantifier=p[1],
            declarations=p[2],
            predicate=p[4])

    def p_constant_quantification(
            self, p):
        """constant_quantification:
            quantifier exprs COLON
                expr
            end_quantifier
        """
        p[0] = self._nodes.Quantification(
            quantifier=p[1],
            declarations=p[2],
            predicate=p[4])

    def p_choose(
            self, p):
        """choose_expr:
            CHOOSE expr COLON expr
            END_CHOOSE
        """
        # The grammar symbol `tuple` is used
        # here, and analysis after parsing
        # will check that the items between
        # the angles are names.
        p[0] = self._nodes.Choose(
            declaration=p[2],
            predicate=p[4])

    def p_let_in(
            self, p):
        """let_expr:
            LET operator_defs
            IN expr
            END_LET
        """
        p[0] = self._nodes.Let(
            definitions=p[2],
            expression=p[4])

    def p_case_expr_without_default(
            self, p):
        """case_expr:
            CASE cases END_CASE
        """
        p[0] = self._nodes.Cases(
            cases=p[2])

    def p_case_expr_with_other(
            self, p):
        """case_expr:
            CASE cases other_case END_CASE
        """
        p[0] = self._nodes.Cases(
            cases=p[2],
            other=p[3])

    def p_cases_append(
            self, p):
        """cases:
            cases
            OP_4_BEFORE case
        """
        if p[2] != '[]':
            raise ValueError(
                'syntax error in CASE expression')
        p[1].append(p[3])
        p[0] = p[1]

    def p_cases_start(
            self, p):
        """cases: case"""
        p[0] = [p[1]]

    def p_rarrow_infix_non(
            self, p):
        """case: expr RARROW expr"""
        p[0] = self._nodes.CaseItem(
            predicate=p[1],
            expression=p[3])

    def p_other_case(
            self, p):
        """other_case:
            OP_4_BEFORE
                OTHER RARROW expr
        """
        if p[1] != '[]':
            raise ValueError(
                'syntax error in CASE expression')
        p[0] = p[4]

    def p_ternary(
            self, p):
        """ternary_expr:
            IF expr
                THEN expr
                ELSE expr
                END_IF
        """
        p[0] = self._nodes.If(
            predicate=p[2],
            then=p[4],
            else_=p[6])

    def p_conditional(
            self, p):
        """elif_expr:
            IF expr
                THEN expr
                elifs
                ELSE expr
                END_IF
        """
        case = self._nodes.IfItem(
            predicate=p[2],
            expression=p[4])
        cases = [case] + p[5]
        p[0] = self._nodes.Ifs(
            cases=cases,
            other=p[7])

    def p_elifs_append(
            self, p):
        """elifs: elifs elif_"""
        p[1].append(p[2])
        p[0] = p[1]

    def p_elifs_start(
            self, p):
        """elifs: elif_"""
        p[0] = [p[1]]

    def p_elif_(
            self, p):
        """elif_: ELIF expr THEN expr"""
        p[0] = self._nodes.IfItem(
            predicate=p[2],
            expression=p[4])

    def p_expr_op_1_infix_non(
            self, p):
        """expr: op_1_infix"""
        # The method `p_op_1_infix()` is
        # dynamically created by the
        # method `__init__()`.
        p[0] = p[1]

    def p_function_application(
            self, p):
        """function_application:
            function_application
                LBRACKET exprs RBRACKET
        """
        # The grammar symbol
        # `function_application` is used
        # in the grammar rule of the grammar
        # symbol `op_15_postfix`.
        #
        # The grammar symbol `op_15_postfix`
        # appears in the docstring of the
        # method `p_op_15_postfix()`,
        # which is dynamically created by
        # the method `__init__()`.
        p[0] = self._nodes.FunctionApplication(
            function=p[1],
            arguments=p[3])

    def p_function_application_skip(
            self, p):
        """function_application:
            op_record_field
        """
        # The precedence of record fields,
        # relative to function application,
        # is defined on page 284 of
        # the book "Specifying Systems".
        p[0] = p[1]

    def p_record_field(
            self, p):
        """op_record_field: fields"""
        p[0] = p[1]

    def p_fields(
            self, p):
        """fields: fields DOT NAME"""
        p[0] = self._nodes.Field(
            expression=p[1],
            name=p[3])

    def p_fields_start(
            self, p):
        """fields:
            | delimited_expr
            | general_identifier
        """
        p[0] = p[1]

    def p_record_field_skip(
            self, p):
        """op_record_field:
            | undelimited_expr
            | vitems
            | subscripted_expr
        """
        p[0] = p[1]

    def p_vertical_items(
            self, p):
        """vitems: vertical_items"""
        vertical_items = p[1]
        if not vertical_items:
            raise AssertionError(
                'empty vertical list')
        vertical_item, *_ = vertical_items
        op = vertical_item.operator
        # that all vertical items have the
        # same operator is checked after parsing
        p[0] = self._nodes.VerticalList(
            operator=op,
            arguments=p[1])

    def p_vertical_items_append(
            self, p):
        """vertical_items:
            vertical_items vertical_item
        """
        p[1].append(p[2])
        p[0] = p[1]

    def p_vertical_items_start(
            self, p):
        """vertical_items:
            vertical_item
        """
        p[0] = [p[1]]

    def p_vertical_item(
            self, p):
        """vertical_item:
            vertical_op
                LVERTICAL
                expr
                RVERTICAL
        """
        p[0] = self._nodes.VerticalItem(
            operator=p[1],
            expression=p[3])

    def p_vertical_operator(
            self, p):
        """vertical_op: VERTICAL_OPERATOR"""
        p[0] = p[1]

    def p_temporal_quantifier(
            self, p):
        """temporal_quantifier:
            | BSLASH_AA
            | BSLASH_EE
        """
        p[0] = p[1]

    def p_end_temporal_quantifier(
            self, p):
        """end_temporal_quantifier:
            | END_BSLASH_AA
            | END_BSLASH_EE
        """

    def p_quantifier(
            self, p):
        """quantifier:
            | BSLASH_A
            | BSLASH_E
        """
        p[0] = p[1]

    def p_end_quantifier(
            self, p):
        """end_quantifier:
            | END_BSLASH_A
            | END_BSLASH_E
        """

    def p_operator_application(
            self, p):
        """op_app:
            | nullary_app
            | unary_app
            | multiary_app
        """
        p[0] = p[1]

    def p_unary_operator_application(
            self, p):
        """unary_app: NAME LPAREN expr RPAREN"""
        args = [p[3]]
        p[0] = self._nodes.OperatorApplication(
            operator=p[1],
            arguments=args)

    def p_multiary_operator_application(
            self, p):
        """multiary_app:
            NAME LPAREN exprs_2 RPAREN"""
        p[0] = self._nodes.OperatorApplication(
            operator=p[1],
            arguments=p[3])

    def p_nullary_operator_application(
            self, p):
        """nullary_app: NAME"""
        p[0] = self._nodes.OperatorApplication(
            operator=p[1])

    def p_subscripted_expr(
            self, p):
        """subscripted_expr:
            | subscripted_action
            | fairness
        """
        p[0] = p[1]

    def p_subscripted_action(
            self, p):
        """subscripted_action:
            | LBRACKET expr
                RBRACKET_UNDERSCORE
                    subscript
            | DOUBLE_LANGLE expr
                DOUBLE_RANGLE_UNDERSCORE
                    subscript
            | LBRACKET expr
                RBRACKET_UNDERSCORE
                    NAME
            | DOUBLE_LANGLE expr
                DOUBLE_RANGLE_UNDERSCORE
                    NAME
        """
        p[0] = self._nodes.SubscriptedAction(
            operator=p[1],
            action=p[2],
            subscript=p[4])

    def p_fairness(
            self, p):
        """fairness:
            | WF_ subscript
                LPAREN expr RPAREN
            | SF_ subscript
                LPAREN expr RPAREN
            | WF_ NAME
                LPAREN expr RPAREN
            | SF_ NAME
                LPAREN expr RPAREN
        """
        subscript = p[2]
        if isinstance(subscript, str):
            subscript = self._nodes.OperatorApplication(
                operator=subscript)
        p[0] = self._nodes.Fairness(
            operator=p[1],
            subscript=subscript,
            action=p[4])

    def p_subscript_unary_op_application(
            self, p):
        """subscript: NAME LPAREN expr RPAREN"""
        args = [p[3]]
        p[0] = self._nodes.OperatorApplication(
            operator=p[1],
            arguments=args)

    def p_subscript_multiary_op_application(
            self, p):
        """subscript:
            NAME LPAREN exprs_2 RPAREN"""
        p[0] = self._nodes.OperatorApplication(
            operator=p[1],
            arguments=p[3])

    def p_subscript_delimited_expr(
            self, p):
        """subscript: delimited_expr"""
        p[0] = p[1]

    def p_delimited_expr(
            self, p):
        """delimited_expr:
            | set_enum
            | deferred_set
            | set_comprehension
            | set_slice
            | tuple
            | record
            | set_of_records
            | set_of_functions
            | value_map
            | paren
            | leaf
        """
        # | function_constructor
        p[0] = p[1]

    def p_empty_set_enumeration(
            self, p):
        """set_enum: LBRACE RBRACE"""
        p[0] = self._nodes.SetEnumeration(
            items=list())

    def p_set_enumeration(
            self, p):
        """set_enum: LBRACE exprs RBRACE"""
        p[0] = self._nodes.SetEnumeration(
            items=p[2])

    def p_deferred_set(
            self, p):
        """deferred_set:
            LBRACE expr COLON
                expr RBRACE
        """
        # Section 15.2.5 on page 289.
        first = p[2]
        second = p[4]
        op_1 = (
            hasattr(first, 'operator') and
            first.operator == '\\in')
        op_2 = (
            hasattr(second, 'operator') and
            second.operator == '\\in')
        match (op_1, op_2):
            case True, _:
                p[0] = self._nodes.SetSlice(
                    declaration=first,
                    predicate=second)
            case False, True:
                p[0] = self._nodes.SetComprehension(
                    item=first,
                    declarations=[second])
            case _:
                raise ValueError(
                    'At least one operator of '
                    '`{...: ...}` need be `\\in`. '
                    f'{first = }\n{second = }')

    def p_definitely_set_comprehension(
            self, p):
        """set_comprehension:
            LBRACE expr COLON
                exprs_2 RBRACE
        """
        p[0] = self._nodes.SetComprehension(
            item=p[2],
            declarations=p[4])

    def p_definitely_set_slice(
            self, p):
        """set_slice:
            LBRACE exprs_2 COLON
                expr RBRACE
        """
        raise ValueError(
            f'Syntax error {p[2]}')

    def p_set_of_functions(
            self, p):
        """set_of_functions:
            LBRACKET expr RARROW expr RBRACKET
        """
        p[0] = self._nodes.SetOfFunctions(
            domain=p[2],
            codomain=p[4])

    # def p_function_constructor(
    #         self, p):
    #     """function_constructor:
    #         LBRACKET exprs MAPSTO
    #             expr RBRACKET
    #     """
    #     p[0] = self._nodes.Function(
    #         declaration=p[2],
    #         value=p[4])

    def p_function_except(
            self, p):
        """value_map:
            LBRACKET expr EXCEPT
                modifications RBRACKET
        """
        p[0] = self._nodes.Except(
            function=p[2],
            changes=p[4])

    def p_modifications_append(
            self, p):
        """modifications:
            modifications COMMA modification
        """
        p[1].append(p[3])
        p[0] = p[1]

    def p_modifications_start(
            self, p):
        """modifications: modification"""
        p[0] = [p[1]]

    def p_modification(
            self, p):
        """modification:
            EXCLAMATION modificandum EQ expr
        """
        p[0] = self._nodes.FunctionChange(
            item=p[2],
            expression=p[4])

    def p_modificandum_append(
            self, p):
        """modificandum:
            modificandum func_value
        """
        p[1].append(p[2])
        p[0] = p[1]

    def p_modificandum_start(
            self, p):
        """modificandum: func_value"""
        p[0] = [p[1]]

    def p_except_bracket(
            self, p):
        """func_value: LBRACKET exprs RBRACKET"""
        p[0] = p[2]

    # NOTE: keywords too can occur here
    # `tla._preparser.switch_keywords_after_dot()`
    # changes keywords after `DOT` to `NAME`.
    def p_except_dot(
            self, p):
        """func_value: DOT NAME"""
        p[0] = p[2]

    def p_empty_tuple(
            self, p):
        """tuple: DOUBLE_LANGLE DOUBLE_RANGLE"""
        p[0] = self._nodes.Tuple(
            items=list())

    def p_tuple(
            self, p):
        """tuple: DOUBLE_LANGLE exprs DOUBLE_RANGLE"""
        p[0] = self._nodes.Tuple(
            items=p[2])

    def p_record(
            self, p):
        """record:
            LBRACKET mapsto_pairs RBRACKET
        """
        pairs = p[2]
        # function ?
        if len(pairs) == 1:
            decl = pairs[0].declaration
            is_func = (
                len(decl) > 1 or
                    # [x \in S, y \in R |-> ...]
                decl[0].arguments is not None)
                    # [x \in S |-> ...]
            if is_func:
                p[0] = pairs[0]
                return
        # record
        key_values = list()
        for pair in pairs:
            if len(pair.declaration) > 1:
                raise ValueError(t.declaration)
            decl = pair.declaration[0]
            if decl.arguments is not None:
                raise ValueError(decl)
            key = decl.operator
            value = pair.value
            key_value = (key, value)
            key_values.append(key_value)
        p[0] = self._nodes.Record(
            key_values=key_values)

    def p_set_of_records(
            self, p):
        """set_of_records:
            LBRACKET colon_pairs RBRACKET
        """
        p[0] = self._nodes.SetOfRecords(
            key_bounds=p[2])

    def p_mapsto_pairs_append(
            self, p):
        """mapsto_pairs:
            mapsto_pairs COMMA mapsto_pair
        """
        p[1].append(p[3])
        p[0] = p[1]

    def p_mapsto_pairs_start(
            self, p):
        """mapsto_pairs: mapsto_pair"""
        p[0] = [p[1]]

    def p_mapsto_pair(
            self, p):
        """mapsto_pair: exprs MAPSTO expr"""
        # NOTE: For converting to bounds:
        # `tla._ast.declarations_as_name_bounds()`
        # which takes
        # `x, y \in S` and returns
        # `[(x, S), `(y, S)]`
        p[0] = self._nodes.Function(
            declaration=p[1],
            value=p[3])

    def p_colon_pairs_append(
            self, p):
        """colon_pairs:
            colon_pairs COMMA colon_pair
        """
        p[1].append(p[3])
        p[0] = p[1]

    def p_colon_pairs_start(
            self, p):
        """colon_pairs: colon_pair"""
        p[0] = [p[1]]

    def p_colon_pair(
            self, p):
        """colon_pair: NAME COLON expr"""
        p[0] = self._nodes.KeyBound(
            name=p[1],
            bound=p[3])

    def p_exprs_1(
            self, p):
        """exprs: expr"""
        p[0] = [p[1]]

    def p_exprs_2(
            self, p):
        """exprs: exprs_2"""
        p[0] = p[1]

    def p_exprs_append(
            self, p):
        """exprs_2:
            exprs_2 COMMA expr
        """
        p[1].append(p[3])
        p[0] = p[1]

    def p_exprs_start(
            self, p):
        """exprs_2:
            expr COMMA expr
        """
        p[0] = [p[1], p[3]]

    def p_leaf(
            self, p):
        """leaf:
            | integer_literal
            | float_literal
            | string_literal
            | boolean_literal
            | set_of_booleans
            | set_of_strings
            | UNDERSCORE
        """
        p[0] = p[1]

    def p_integer_literal(
            self, p):
        """integer_literal:
            | DECIMAL_INTEGER
            | BINARY_INTEGER
            | OCTAL_INTEGER
            | HEXADECIMAL_INTEGER
        """
        # This is a numeral.
        # When a TLA+ module `EXTENDS`
        # `Naturals` or `Integers`,
        # then these numerals take
        # the usual integer meaning.
        p[0] = self._nodes.IntegralNumeral(
            value=p[1])

    def p_float_literal(
            self, p):
        """float_literal: FLOAT"""
        p[0] = self._nodes.FloatNumeral(
            value=p[1])

    def p_string_literal(
            self, p):
        """string_literal:
            | STRING_LITERAL
            | MULTILINE_STRING_LITERAL
        """
        p[0] = self._nodes.StringLiteral(
            value=p[1])

    def p_boolean_constant(
            self, p):
        """boolean_literal:
            | FALSE
            | TRUE
        """
        p[0] = self._nodes.BooleanLiteral(
            value=p[1])

    def p_set_of_boolean_constants(
            self, p):
        """set_of_booleans: BOOLEAN"""
        p[0] = self._nodes.SetOfBooleans()

    def p_set_of_strings(
            self, p):
        """set_of_strings: STRING"""
        p[0] = self._nodes.SetOfStrings()

    def p_theorem_proof_steps(
            self, p):
        """theorem_proof:
            PROOF proof_steps
        """
        p[0] = self._nodes.Proof(
            steps=p[2],
            proof_keyword=True)

    def p_theorem_leaf_proof(
            self, p):
        """theorem_proof:
            PROOF leaf_proof
        """
        p[0] = self._nodes.Proof(
            steps=[p[2]],
            proof_keyword=True)

    def p_theorem_proof_steps_without_keyword(
            self, p):
        """theorem_proof:
            proof_steps
        """
        p[0] = self._nodes.Proof(
            steps=p[1])

    def p_theorem_leaf_proof_without_keyword(
            self, p):
        """theorem_proof:
            leaf_proof
        """
        p[0] = self._nodes.Proof(
            steps=[p[1]])

    def p_theorem_proof_without_steps(
            self, p):
        """theorem_proof: PROOF"""
        p[0] = self._nodes.Proof(
            proof_keyword=True)

    def p_leaf_proof_with_facts_and_defs(
            self, p):
        """leaf_proof:
            by
                exprs
                def_keyword name_list
        """
        p[0] = self._nodes.By(
            only=p[1],
            facts=p[2],
            names=p[4])

    def p_leaf_proof_with_facts(
            self, p):
        """leaf_proof: by exprs"""
        p[0] = self._nodes.By(
            only=p[1],
            facts=p[2])

    def p_leaf_proof_with_defs(
            self, p):
        """leaf_proof:
            by
                def_keyword name_list
        """
        p[0] = self._nodes.By(
            only=p[1],
            names=p[3])

    def p_leaf_proof_obvious(
            self, p):
        """leaf_proof: OBVIOUS"""
        p[0] = self._nodes.Obvious()

    def p_leaf_proof_omitted(
            self, p):
        """leaf_proof: OMITTED"""
        p[0] = self._nodes.Omitted()

    def p_def_keyword(
            self, p):
        """def_keyword:
            | DEF
            | DEFS
        """
        p[0] = p[1]

    def p_by(
            self, p):
        """by: BY"""
        p[0] = False

    def p_by_only(
            self, p):
        """by: BY ONLY"""
        p[0] = True

    def p_proof_steps_append(
            self, p):
        """proof_steps:
            proof_steps proof_step
        """
        p[1].append(p[2])
        p[0] = p[1]

    def p_proof_steps_start(
            self, p):
        """proof_steps: proof_step"""
        p[0] = [p[1]]

    def p_proof_step_with_proof(
            self, p):
        """proof_step:
            | proof_goal PROOF leaf_proof
            | proof_goal leaf_proof
        """
        step_number, main = p[1]
        if p[2] == 'PROOF':
            proof = p[3]
            proof_keyword = True
        else:
            proof = p[2]
            proof_keyword = None
        p[0] = self._nodes.ProofStep(
            name=step_number,
            main=main,
            proof=proof,
            proof_keyword=proof_keyword)

    def p_proof_step_without_proof_pf_kw(
            self, p):
        """proof_step:
            proof_goal PROOF
        """
        step_number, main = p[1]
        p[0] = self._nodes.ProofStep(
            name=step_number,
            main=main,
            proof_keyword=True)

    def p_proof_step_without_proof(
            self, p):
        """proof_step:
            proof_goal
        """
        step_number, main = p[1]
        p[0] = self._nodes.ProofStep(
            name=step_number,
            main=main)

    def p_proof_step_main(
            self, p):
        """proof_goal:
            | assertion_proof_step
            | suffices_proof_step
            | case_proof_step
            | pick_proof_step
            | have_proof_step
            | take_proof_step
            | witness_proof_step
            | define_proof_step
            | instance_proof_step
            | use_proof_step
            | hide_proof_step
            | qed_proof_step
        """
        p[0] = p[1]

    def p_assertion_proof_step(
            self, p):
        """assertion_proof_step:
            | step_number sequent
            | step_number expr
        """
        p[0] = (p[1], p[2])

    def p_suffices_proof_step_sequent(
            self, p):
        """suffices_proof_step:
            step_number
                SUFFICES sequent
        """
        main = self._nodes.Suffices(
            predicate=p[3])
        p[0] = (p[1], main)

    def p_suffices_proof_step_expr(
            self, p):
        """suffices_proof_step:
            step_number
                SUFFICES expr
        """
        main = self._nodes.Suffices(
            predicate=p[3])
        p[0] = (p[1], main)

    def p_case_proof_step(
            self, p):
        """case_proof_step:
            step_number
                CASE
                    expr
                END_CASE
        """
        # because CASE is both undelimited
        # construct and proof step, and
        # `GeneratingParser` method
        # `_scopes_stack_append()` cannot
        # decide which
        main = self._nodes.ProofCase(
            expression=p[3])
        p[0] = (p[1], main)

    def p_pick_proof_step(
            self, p):
        """pick_proof_step:
            step_number
                PICK
                    exprs COLON
                        expr
                END_PICK
        """
        main = self._nodes.Pick(
            declarations=p[3],
            predicate=p[5])
        p[0] = (p[1], main)

    def p_have_proof_step(
            self, p):
        """have_proof_step:
            step_number
                HAVE expr
        """
        main = self._nodes.Have(
            expression=p[3])
        p[0] = (p[1], main)

    def p_proof_take(
            self, p):
        """take_proof_step:
            step_number
                TAKE exprs
        """
        main = self._nodes.Take(
            declarations=p[3])
        p[0] = (p[1], main)

    def p_proof_witness_step(
            self, p):
        """witness_proof_step:
            step_number
                WITNESS exprs
        """
        main = self._nodes.QuantifierWitness(
            expressions=p[3])
        p[0] = (p[1], main)

    def p_proof_define_step(
            self, p):
        """define_proof_step:
            step_number
                DEFINE operator_defs
                END_DEFINE
        """
        # The keyword `DEFINE` is
        # optional. The function
        # `_insert_proof_define_tokens()`
        # inserts `DEFINE` where it
        # has been omitted.
        main = self._nodes.Define(
            definitions=p[3])
        p[0] = (p[1], main)

    def p_instance_proof_step(
            self, p):
        """instance_proof_step:
            step_number instance
        """
        p[0] = (p[1], p[2])

    def p_proof_use_step(
            self, p):
        """use_proof_step:
            step_number use_unit
        """
        p[0] = (p[1], p[2])

    def p_proof_hide_step_full(
            self, p):
        """hide_proof_step:
            step_number
                HIDE
                    exprs
                    def_keyword name_list
        """
        main = self._nodes.Hide(
            facts=p[3],
            names=p[5])
        p[0] = (p[1], main)

    def p_proof_hide_step_with_facts(
            self, p):
        """hide_proof_step:
            step_number
                HIDE
                    exprs
        """
        main = self._nodes.Hide(
            facts=p[3])
        p[0] = (p[1], main)

    def p_proof_hide_step_with_defs(
            self, p):
        """hide_proof_step:
            step_number
                HIDE
                    def_keyword name_list
        """
        main = self._nodes.Hide(
            names=p[4])
        p[0] = (p[1], main)

    def p_qed_proof_step(
            self, p):
        """qed_proof_step:
            step_number
                QED
        """
        p[0] = (p[1], p[2])

    def p_proof_step_number(
            self, p):
        """step_number:
            | STEP_NUMBER
            | STEP_NUMBER_PLUS
            | STEP_NUMBER_ASTERISK
        """
        p[0] = p[1]

    def p_labeled_expr(
            self, p):
        """expr: op_app DOUBLE_COLON expr"""
        p[0] = self._nodes.OperatorApplication(
            operator=p[2],
            arguments=[p[1], p[3]])

    def p_general_identifier(
            self, p):
        """general_identifier: gid"""
        items = p[1]
        if len(items) == 1:
            op_app, = p[1]
            p[0] = op_app
            return
        if not items:
            raise ValueError(items)
        p[0] = self._nodes.SubexpressionReference(
            items=items)
            # NOTE: also `M!Op` where
            # `M == INSTANCE`
            # is represented here

    def p_gid_repeat_nullary_op_app(
            self, p):
        """gid:
            gid EXCLAMATION_NAME
        """
        name = p[2]
        p[1].append(name)
        p[0] = p[1]

    def p_gid_repeat_non_nullary_op_app(
            self, p):
        """gid:
            gid EXCLAMATION_NAME
                LPAREN exprs RPAREN
        """
        name = p[2]
        op_app = self._nodes.OperatorApplication(
            operator=name,
            arguments=p[4])
        p[1].append(op_app)
        p[0] = p[1]

    def p_gid_repeat_paren(
            self, p):
        """gid:
            gid EXCLAMATION
                LPAREN expr RPAREN
        """
        arguments = [p[4]]
        op_app = self._nodes.OperatorApplication(
            operator=None,
            arguments=arguments)
        p[1].append(op_app)
        p[0] = p[1]

    def p_gid_repeat_paren_exprs_2(
            self, p):
        """gid:
            gid EXCLAMATION
                LPAREN exprs_2 RPAREN
        """
        op_app = self._nodes.OperatorApplication(
            operator=None,
            arguments=p[4])
        p[1].append(op_app)
        p[0] = p[1]

    def p_gid_repeat_exclamation_symbol(
            self, p):
        """gid:
            gid exclamation_symbol
        """
        p[1].append(p[2])
        p[0] = p[1]

    def p_gid_repeat_exclamation_integer(
            self, p):
        """gid:
            gid EXCLAMATION DECIMAL_INTEGER
        """
        p[1].append(p[3])
        p[0] = p[1]

    def p_gid_start(
            self, p):
        """gid: op_app"""
        p[0] = [p[1]]

    def p_exclamation_symbol(
            self, p):
        """exclamation_symbol:
            | EXCLAMATION_AT
            | EXCLAMATION_COLON
            | EXCLAMATION_DOUBLE_LANGLE
            | EXCLAMATION_DOUBLE_RANGLE
        """
        p[0] = p[1]

    def p_symbol_at(
            self, p):
        """expr: AT"""
        p[0] = p[1]


class OperatorPrecedenceGrammar(Grammar):
    """LR(1) with operator-precedence table."""

    def __init__(
            self
            ) -> None:
        self.operator_precedence = [
            ('nonassoc', 'DOUBLE_COLON'),
                # labels
            ('nonassoc', 'OP_1_INFIX'),
            ('nonassoc', 'OP_2_INFIX'),
            ('left', 'OP_3_LEFT'),
            ('nonassoc', 'OP_4_PREFIX'),
            ('nonassoc', 'OP_4_BEFORE'),
            ('nonassoc', 'EQ'),
                # op_5_eq_infix
            ('left', 'BSLASH_IN'),
                # 'op_5_bslash_in_between',
            ('left', 'OP_5_LEFT'),
            ('nonassoc', 'OP_5_INFIX'),
            ('left', 'OP_6_LEFT'),
            ('nonassoc', 'OP_7_INFIX'),
            ('nonassoc', 'OP_8_BEFORE'),
            ('nonassoc', 'OP_8_INFIX'),
            ('left', 'OP_8_LEFT'),
            ('nonassoc', 'OP_9_BEFORE'),
            ('nonassoc', 'OP_9_INFIX'),
            ('left', 'OP_9_LEFT'),
            ('left', 'OP_10_LEFT'),
            ('nonassoc', 'OP_10_INFIX'),
            ('nonassoc', 'set_of_tuples'),
            ('left', 'CARTESIAN'),
                # 'set_of_tuples_between',
            ('left', 'OP_11_LEFT'),
            ('left', 'DASH'),
                # 'op_11_dash_left',
                # 'op_12_dash_before',
            ('nonassoc', 'OP_12_PREFIX'),
                # for `DASH_DOT`
            ('nonassoc', 'OP_13_INFIX'),
            ('left', 'OP_13_LEFT'),
            ('nonassoc', 'OP_14_INFIX'),
            ('nonassoc', 'OP_15_POSTFIX'),
            ('nonassoc', 'OP_15_AFTER')]
        super().__init__()

    def p_expr_binary_operator(
            self, p):
        """expr:
            | expr OP_1_INFIX expr
            | expr OP_2_INFIX expr
            | expr OP_3_LEFT expr
            | expr EQ expr
            | expr BSLASH_IN expr
            | expr OP_5_LEFT expr
            | expr OP_5_INFIX expr
            | expr OP_6_LEFT expr
            | expr OP_7_INFIX expr
            | expr OP_8_INFIX expr
            | expr OP_8_LEFT expr
            | expr OP_9_INFIX expr
            | expr OP_9_LEFT expr
            | expr OP_10_LEFT expr
            | expr OP_10_INFIX expr
            | expr OP_11_LEFT expr
            | expr DASH expr
            | expr OP_13_INFIX expr
            | expr OP_13_LEFT expr
            | expr OP_14_INFIX expr
        """
        op_lexeme = p[2]
        args = [p[1], p[3]]
        p[0] = self._nodes.OperatorApplication(
            operator=op_lexeme,
            arguments=args)

    def p_expr_prefix_operator(
            self, p):
        """expr:
            | OP_4_PREFIX expr
            | OP_4_BEFORE expr
            | OP_8_BEFORE expr
            | OP_9_BEFORE expr
            | DASH expr
            | OP_12_PREFIX expr
        """
        p[0] = self._nodes.OperatorApplication(
            operator=p[1],
            arguments=[p[2]])

    def p_expr_postfix_operator(
            self, p):
        """expr:
            | expr OP_15_POSTFIX
            | expr OP_15_AFTER
        """
        p[0] = self._nodes.OperatorApplication(
            operator=p[2],
            arguments=[p[1]])

    def p_expr_set_of_tuples(
            self, p):
        """expr: set_of_tuples"""
        op_lexeme, *args = p[1]
        p[0] = self._nodes.OperatorApplication(
            operator=op_lexeme,
            arguments=args)

    def p_set_of_tuples_repeat(
            self, p):
        """set_of_tuples:
            set_of_tuples CARTESIAN expr
        """
        p[1].append(p[3])
        p[0] = p[1]

    def p_set_of_tuples_start(
            self, p):
        """set_of_tuples:
            expr CARTESIAN expr
        """
        p[0] = [p[2], p[1], p[3]]

    def p_expr_function_application(
            self, p):
        """expr: function_application"""
        p[0] = p[1]
