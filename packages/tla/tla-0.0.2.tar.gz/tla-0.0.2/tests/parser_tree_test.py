"""Parser testing."""
import tla._ast as _ast
import tla._lre as _lr
import tla._pprint as _pp


def test_set_of_tuples():
    text = r'''
        A \X B \X C
        '''
    expr = _lr.parse_expr(text)
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == '\\X', expr.operator
    assert len(expr.arguments) == 3, expr.arguments
    arg_a, arg_b, arg_c = expr.arguments
    assert_operator_name(arg_a, 'A')
    assert_operator_name(arg_b, 'B')
    assert_operator_name(arg_c, 'C')
    # print
    text = _pp.pformat_ast(expr)
    print(text)


def test_set_theory_operators():
    text = r'''
        A \cap B \cup C
        '''
    expr = _lr.parse_expr(text)
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == '\\cup', expr.operator
    assert len(expr.arguments) == 2, len(expr.arguments)
    ab, arg_c = expr.arguments
    # expression `C`
    assert_operator_name(arg_c, 'C')
    # expression `A \cap B`
    assert ab.symbol.name == 'OPERATOR_APPLICATION', (
        ab.symbol)
    assert ab.operator == '\\cap', ab.operator
    assert len(ab.arguments) == 2, len(ab.arguments)
    arg_a, arg_b = ab.arguments
    assert_operator_name(arg_a, 'A')
    assert_operator_name(arg_b, 'B')
    # print
    text = _pp.pformat_ast(expr)
    print(text)


def test_keyword_unary_operators():
    text = r'''
        ---- MODULE unary_operators ----
        domain == DOMAIN f
        enabled == ENABLED action
        subsets == SUBSET S
        unchanged == UNCHANGED vars
        set_union == UNION R
        ====
        '''
    module = _lr.parse(text)
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'unary_operators', module.name
    assert len(module.units) == 5, module.units
    # DOMAIN
    domain_def = module.units[0]
    assert_op_def(domain_def, 'domain')
    expr = domain_def.definiens
    assert_unary_op_app(expr, 'DOMAIN')
    arg, = expr.arguments
    assert_operator_name(arg, 'f')
    # ENABLED
    enabled_def = module.units[1]
    assert_op_def(enabled_def, 'enabled')
    expr = enabled_def.definiens
    assert_unary_op_app(expr, 'ENABLED')
    arg, = expr.arguments
    assert_operator_name(arg, 'action')
    # SUBSET
    subset_def = module.units[2]
    assert_op_def(subset_def, 'subsets')
    expr = subset_def.definiens
    assert_unary_op_app(expr, 'SUBSET')
    arg, = expr.arguments
    assert_operator_name(arg, 'S')
    # UNCHANGED
    unchanged_def = module.units[3]
    assert_op_def(unchanged_def, 'unchanged')
    expr = unchanged_def.definiens
    assert_unary_op_app(expr, 'UNCHANGED')
    arg, = expr.arguments
    assert_operator_name(arg, 'vars')
    # UNION
    set_union_def = module.units[4]
    assert_op_def(set_union_def, 'set_union')
    expr = set_union_def.definiens
    assert_unary_op_app(expr, 'UNION')
    arg, = expr.arguments
    assert_operator_name(arg, 'R')
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_unary_minus_as_argument():
    text = r'''
        op(-.)
        '''
    expr = _lr.parse_expr(text)
    assert_unary_op_app(expr, 'op')
    arg, = expr.arguments
    assert arg.symbol.name == 'OPERATOR_APPLICATION', (
        arg.symbol)
    assert arg.operator == '-.', arg.operator
    assert arg.arguments is None, arg.arguments
    # print
    text = _pp.pformat_ast(expr)
    print(text)


def test_unary_minus_as_operator():
    parser = _lr.ExprParser()
    text = r'''
        - 1
        '''
    expr = parser.parse(text)
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == '-', expr.operator
    assert len(expr.arguments) == 1, len(expr.arguments)
    arg, = expr.arguments
    assert arg.symbol.name == 'INTEGRAL_NUMERAL', (
        arg.symbol)
    assert arg.value == '1', arg.value
    # print
    text = _pp.pformat_ast(expr)
    print(text)


def test_set_slice_operator():
    parser = _lr.ExprParser()
    text = r'''
        {x \in S: y \in R}
        '''
    expr = parser.parse(text)
    assert expr.symbol.name == 'SET_SLICE', expr.symbol
    x_in_s = expr.declaration
    y_in_r = expr.predicate
    # declarations
    assert_binary_op_app(x_in_s, r'\in')
    args = x_in_s.arguments
    x, s = args
    assert_operator_name(x, 'x')
    assert_operator_name(s, 'S')
    # predicate
    assert_binary_op_app(y_in_r, r'\in')
    args = y_in_r.arguments
    y, r = args
    assert_operator_name(y, 'y')
    assert_operator_name(r, 'R')


def test_set_comprehension_operator():
    parser = _lr.ExprParser()
    text = r'''
        {x: x \in R}
        '''
    expr = parser.parse(text)
    assert expr.symbol.name == 'SET_COMPREHENSION', (
        expr.symbol)
    assert_operator_name(expr.item, 'x')
    assert len(expr.declarations)
    x_in_r = expr.declarations[0]
    # declarations
    assert_binary_op_app(x_in_r, r'\in')
    args = x_in_r.arguments
    x, r = args
    assert_operator_name(x, 'x')
    assert_operator_name(r, 'R')


def test_always_eventually():
    parser = _lr.ExprParser()
    text = r'''
        []<> P
        '''
    expr = parser.parse(text)
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == '[]', expr.operator
    assert len(expr.arguments) == 1, len(expr.arguments)
    arg, = expr.arguments
    assert arg.symbol.name == 'OPERATOR_APPLICATION', (
        arg.symbol)
    assert arg.operator == '<>', expr.operator
    assert len(arg.arguments) == 1, len(expr.arguments)
    p_op, = arg.arguments
    assert p_op.symbol.name == 'OPERATOR_APPLICATION', (
        p_op.symbol)
    assert p_op.operator == 'P', p_op.operator
    assert p_op.arguments is None, p_op.arguments
    # print
    text = _pp.pformat_ast(expr)
    print(text)


def test_eventually_always():
    parser = _lr.ExprParser()
    text = r'''
        <>[] P
        '''
    expr = parser.parse(text)
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == '<>', expr.operator
    assert len(expr.arguments) == 1, len(expr.arguments)
    arg, = expr.arguments
    assert arg.symbol.name == 'OPERATOR_APPLICATION', (
        arg.symbol)
    assert arg.operator == '[]', expr.operator
    assert len(arg.arguments) == 1, len(expr.arguments)
    p_op, = arg.arguments
    assert p_op.symbol.name == 'OPERATOR_APPLICATION', (
        p_op.symbol)
    assert p_op.operator == 'P', p_op.operator
    assert p_op.arguments is None, p_op.arguments
    # print
    text = _pp.pformat_ast(expr)
    print(text)


def test_identifiers_in_leaf_proofs():
    text = r'''
        ---- MODULE leaf_proof ----
        COROLLARY ASSUME TRUE PROVE TRUE
        <1>2. M!Op
            BY ONLY <1>1 DEF M!Op
        ====
        '''
    module = _lr.parse(text)
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'leaf_proof', module.name
    assert len(module.units) == 1, module.units
    theorem, = module.units
    assert theorem.symbol.name == 'THEOREM', (
        theorem.symbol)
    assert theorem.name is None, theorem.name
    assert theorem.theorem_keyword == 'COROLLARY', (
        theorem.theorem_keyword)
    goal = theorem.goal
    proof = theorem.proof
    # theorem goal `TRUE`
    assert goal.symbol.name == 'SEQUENT', goal.symbol
    asms = goal.assume
    assert len(asms) == 1, len(asms)
    assume, = asms
    assert_boolean_literal(assume, 'TRUE')
    assert_boolean_literal(goal.prove, 'TRUE')
    # proof
    assert proof.symbol.name == 'PROOF', proof.symbol
    assert proof.proof_keyword is None, proof.proof_keyword
    assert len(proof.steps) == 1, len(proof.steps)
    step_12, = proof.steps
    # step `<1>2`
    assert step_12.symbol.name == 'PROOF_STEP', (
        step_12.symbol)
    assert step_12.proof_keyword is None, (
        step_12.proof_keyword)
    assert step_12.name == '<1>2.', step_12.name
    main = step_12.main
    proof = step_12.proof
    # `M!Op`
    assert (main.symbol.name ==
        'SUBEXPRESSION_REFERENCE'), main.symbol
    assert len(main.items) == 2, len(main.items)
    assert_operator_name(main.items[0], 'M')
    assert main.items[1] == 'Op', main.items
    # `BY <1>1 DEF M!Op`
    assert proof.symbol.name == 'BY', proof.symbol
    assert proof.only is True, proof.only
    facts = proof.facts
    names = proof.names
    assert len(facts) == 1, facts
    assert len(names) == 1, names
    # `<1>1`
    step_11, = facts
    assert (step_11.symbol.name ==
        'OPERATOR_APPLICATION'), step_11.symbol
    assert step_11.operator == '<1>1', step_11.operator
    assert step_11.arguments is None, step_11.arguments
    # `DEF M!Op`
    name, = names
    assert (name.symbol.name ==
        'SUBEXPRESSION_REFERENCE'), name.symbol
    assert len(name.items) == 2, len(name.items)
    assert_operator_name(name.items[0], 'M')
    assert name.items[1] == 'Op', name.items
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_suffices_proof_step():
    text = r'''
        ---- MODULE suffices_pf_step ----
        THEOREM TRUE
        <1>1. SUFFICES \A n \in Nat:  n < n + 1
        ====
        '''
    module = _lr.parse(text)
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'suffices_pf_step', module.name
    assert len(module.units) == 1, module.units
    theorem, = module.units
    assert theorem.symbol.name == 'THEOREM', (
        theorem.symbol)
    assert theorem.name is None, theorem.name
    assert theorem.theorem_keyword == 'THEOREM', (
        theorem.theorem_keyword)
    expr = theorem.goal
    proof = theorem.proof
    # `TRUE`
    assert_boolean_literal(expr, 'TRUE')
    # proof
    assert proof.symbol.name == 'PROOF', proof.symbol
    assert proof.proof_keyword is None, proof.proof_keyword
    assert len(proof.steps) == 1, proof.steps
    step_11, = proof.steps
    # step `<1>1`
    assert step_11.symbol.name == 'PROOF_STEP', (
        step_11.symbol)
    assert step_11.name == '<1>1.', step_11.name
    assert step_11.proof is None, step_11.proof
    assert step_11.proof_keyword is None, (
        step_11.proof_keyword)
    main = step_11.main
    # `SUFFICES \A n \in Nat:  n < n + 1`
    assert main.symbol.name == 'SUFFICES', main.symbol
    expr = main.predicate
    # `\A n \in Nat:  n < n + 1`
    assert expr.symbol.name == 'QUANTIFICATION', (
        expr.symbol)
    assert expr.quantifier == '\\A', expr.quantifier
    assert len(expr.declarations) == 1, expr.declarations
    decl, = expr.declarations
    pred = expr.predicate
    # `n \in Nat`
    assert_binary_op_app(decl, '\\in')
    n, nat = decl.arguments
    assert_operator_name(n, 'n')
    assert_operator_name(nat, 'Nat')
    # `n < n + 1`
    assert_binary_op_app(pred, '<')
    n, n1 = pred.arguments
    assert_operator_name(n, 'n')
    assert_binary_op_app(n1, '+')
    n, one = n1.arguments
    assert_operator_name(n, 'n')
    assert one.symbol.name == 'INTEGRAL_NUMERAL', one
    assert one.value == '1', one.value
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_quantifier_vertical_expression():
    text = r'''
        ---- MODULE quantifier_vexpr ----
        THEOREM \E n \in Nat:  /\ P(n)
                               /\ \A m \in S:  ~ P(m)
        ====
        '''
    module = _lr.parse(text)
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'quantifier_vexpr', module.name
    assert len(module.units) == 1, module.units
    theorem, = module.units
    assert theorem.symbol.name == 'THEOREM', theorem.symbol
    assert theorem.theorem_keyword == 'THEOREM', (
        theorem.theorem_keyword)
    assert theorem.name is None, theorem.name
    assert theorem.proof is None, theorem.proof
    qexpr = theorem.goal
    # `\E n \in Nat: ...`
    assert qexpr.symbol.name == 'QUANTIFICATION', (
        qexpr.symbol)
    assert qexpr.quantifier == '\\E', qexpr.quantifier
    assert len(qexpr.declarations) == 1, qexpr.declarations
    decl, = qexpr.declarations
    vexpr = qexpr.predicate
    # `n \in Nat`
    assert_binary_op_app(decl, '\\in')
    n, nat = decl.arguments
    assert_operator_name(n, 'n')
    assert_operator_name(nat, 'Nat')
    # vertical conjunction
    assert vexpr.symbol.name == 'VERTICAL_LIST', (
        vexpr.symbol)
    assert vexpr.operator == '/\\', vexpr.operator
    assert len(vexpr.arguments) == 2, vexpr.arguments
    item_1, item_2 = vexpr.arguments
    # `/\ P(n)`
    assert item_1.symbol.name == 'VERTICAL_ITEM', (
        item_1.symbol)
    expr = item_1.expression
    assert_unary_op_app(expr, 'P')
    n, = expr.arguments
    assert_operator_name(n, 'n')
    # `/\ \A m \in S:  ~ P(m)`
    assert item_2.symbol.name == 'VERTICAL_ITEM', (
        item_2.symbol)
    qexpr = item_2.expression
    assert qexpr.symbol.name == 'QUANTIFICATION', (
        qexpr.symbol)
    assert qexpr.quantifier == '\\A', qexpr.quantifier
    assert len(qexpr.declarations) == 1, qexpr.declarations
    decl, = qexpr.declarations
    pred = qexpr.predicate
    # `m \in S`
    assert_binary_op_app(decl, '\\in')
    m, nat = decl.arguments
    assert_operator_name(m, 'm')
    assert_operator_name(nat, 'S')
    # `~ P(m)`
    assert_unary_op_app(pred, '~')
    pexpr, = pred.arguments
    assert_unary_op_app(pexpr, 'P')
    m, = pexpr.arguments
    assert_operator_name(m, 'm')
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_vertical_expr_proof_step():
    text = r'''
        ---- MODULE vexpr_pf_step ----
        PROPOSITION TRUE
        <1>1.
              /\ <<e>> # << >>
            OBVIOUS
        ====
        '''
    module = _lr.parse(text)
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'vexpr_pf_step', module.name
    assert len(module.units) == 1, module.units
    theorem, = module.units
    assert theorem.symbol.name == 'THEOREM', theorem.symbol
    assert theorem.name is None, theorem.name
    assert theorem.goal is not None
    assert theorem.proof is not None
    assert theorem.theorem_keyword == 'PROPOSITION', (
        theorem.theorem_keyword)
    goal = theorem.goal
    proof = theorem.proof
    # goal `TRUE`
    assert goal.symbol.name == 'BOOLEAN_LITERAL', (
        goal.symbol)
    assert goal.value == 'TRUE', goal.value
    # proof
    assert proof.symbol.name == 'PROOF', proof.symbol
    assert proof.proof_keyword is None, (
        proof.proof_keyword)
    assert len(proof.steps) == 1, len(proof.steps)
    step_11, = proof.steps
    assert step_11.symbol.name == 'PROOF_STEP', (
        step_11.symbol)
    assert step_11.proof_keyword is None, (
        step_11.proof_keyword)
    assert step_11.name == '<1>1.', step_11.name
    main = step_11.main
    proof = step_11.proof
    # step number
    # `/\ <<e>> # << >>`
    assert main.symbol.name == 'VERTICAL_LIST', main.symbol
    assert main.operator == '/\\', main.operator
    assert len(main.arguments) == 1, main.arguments
    vitem, = main.arguments
    assert vitem.symbol.name == 'VERTICAL_ITEM', (
        vitem.symbol)
    assert vitem.operator == '/\\', vitem.operator
    expr = vitem.expression
    # `<<e>> # << >>`
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == '#', expr.operator
    assert len(expr.arguments) == 2, expr.arguments
    e_tuple, empty_tuple = expr.arguments
    # `<<e>>`
    assert e_tuple.symbol.name == 'TUPLE', (
        e_tuple.symbol)
    assert len(e_tuple.items) == 1, e_tuple.items
    e, = e_tuple.items
    # `e`
    assert e.symbol.name == 'OPERATOR_APPLICATION', (
        e.symbol)
    assert e.operator == 'e', e.operator
    assert e.arguments is None, e.arguments
    # `<< >>`
    assert empty_tuple.symbol.name == 'TUPLE', (
        empty_tuple.symbol)
    assert len(empty_tuple.items) == 0, empty_tuple.items
    # `OBVIOUS`
    assert proof.symbol.name == 'OBVIOUS', proof.symbol
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_named_theorem():
    text = r'''
        ---- MODULE named_theorem ----
        LEMMA named ==
            TRUE
        ====
        '''
    module = _lr.parse(text)
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'named_theorem', module.name
    assert len(module.units) == 1, module.units
    theorem, = module.units
    assert theorem.symbol.name == 'THEOREM', theorem.symbol
    assert theorem.name == 'named', theorem.name
    assert theorem.proof is None, theorem.proof
    assert theorem.theorem_keyword == 'LEMMA', (
        theorem.theorem_keyword)
    goal = theorem.goal
    # `TRUE`
    assert goal.symbol.name == 'BOOLEAN_LITERAL', (
        goal.symbol)
    assert goal.value == 'TRUE', goal.value
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_quantifier_temporal():
    text = r'''
        ---- MODULE temporal_formula ----
        LOCAL L == \A r \in S:  SF_x(expr)
        ====
        '''
    module = _lr.parse(text)
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'temporal_formula', module.name
    assert len(module.units) == 1, module.units
    defn, = module.units
    assert defn.symbol.name == 'OPERATOR_DEFINITION', (
        defn.symbol)
    assert defn.name == 'L', defn.name
    assert defn.arity is None, defn.arity
    assert defn.local is True, defn.local
    assert defn.function is None, defn.function
    qexpr = defn.definiens
    # `\A r \in S:  SF_x(expr)`
    assert qexpr.symbol.name == 'QUANTIFICATION', (
        qexpr.symbol)
    assert qexpr.quantifier == '\\A', qexpr.quantifier
    assert len(qexpr.declarations) == 1, qexpr.declarations
    decl, = qexpr.declarations
    pred = qexpr.predicate
    # `r \in S`
    assert decl.symbol.name == 'OPERATOR_APPLICATION', (
        decl.symbol)
    assert decl.operator == '\\in', decl.operator
    assert len(decl.arguments) == 2, len(decl.arguments)
    arg_r, arg_s = decl.arguments
    assert arg_r.symbol.name == 'OPERATOR_APPLICATION', (
        arg_r.symbol)
    assert arg_r.operator == 'r', arg_r.operator
    assert arg_r.arguments is None, arg_r.arguments
    assert arg_s.symbol.name == 'OPERATOR_APPLICATION', (
        arg_s.symbol)
    assert arg_s.operator == 'S', arg_s.operator
    assert arg_s.arguments is None, arg_s.arguments
    # `SF_x(expr)`
    assert pred.symbol.name == 'FAIRNESS', pred.symbol
    assert pred.operator == 'SF_', pred.operator
    x = pred.subscript
    expr = pred.action
    # subscript `x`
    assert x.symbol.name == 'OPERATOR_APPLICATION', (
        x.symbol)
    assert x.operator == 'x', x.operator
    assert x.arguments is None, x.arguments
    # action `expr`
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == 'expr', expr.operator
    assert expr.arguments is None, expr.arguments
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_unary_minus_operator_definition():
    text = r'''
        ---- MODULE binary_operator_def ----
        -. A == 0 - A
        ----
        ====
        '''
    module = _lr.parse(text)
    assert module is not None
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'binary_operator_def', module.name
    assert len(module.units) == 2, len(module.units)
    # definition
    uminus_def, dash_line = module.units
    assert dash_line == '----', dash_line
    assert uminus_def.symbol.name == 'OPERATOR_DEFINITION', (
        uminus_def.symbol)
    assert uminus_def.name == '-.', oplus_def.name
    assert uminus_def.local is None, oplus_def.local
    assert uminus_def.function is None, oplus_def.function
    arity = uminus_def.arity
    definiens = uminus_def.definiens
    # arity
    assert len(arity) == 1, arity
    param_a, = arity
    # parameter `A`
    assert param_a.symbol.name == 'OPERATOR_APPLICATION', (
        param_a.symbol)
    assert param_a.operator == 'A', param_a.operator
    assert param_a.arguments is None, param_a.arguments
    # definiens `0 - A`
    assert (definiens.symbol.name ==
        'OPERATOR_APPLICATION'), definiens.symbol
    assert definiens.operator == '-', definiens
    assert len(definiens.arguments) == 2, len(
        definiens.arguments)
    zero, arg_a = definiens.arguments
    # argument `0`
    assert zero.symbol.name == 'INTEGRAL_NUMERAL', (
        zero.symbol)
    assert zero.value == '0', zero.value
    # argument `A`
    assert arg_a.symbol.name == 'OPERATOR_APPLICATION', (
        arg_a.symbol)
    assert arg_a.operator == 'A', arg_a.operator
    assert arg_a.arguments is None, arg_a.arguments
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_binary_operator_definition():
    text = r'''
        ---- MODULE binary_operator_def ----
        LOCAL A (+) B == TRUE
        ----
        ====
        '''
    module = _lr.parse(text)
    assert module is not None
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'binary_operator_def', module.name
    assert len(module.units) == 2, len(module.units)
    # definition
    oplus_def, dash_line = module.units
    assert dash_line == '----', dash_line
    assert oplus_def.symbol.name == 'OPERATOR_DEFINITION', (
        oplus_def.symbol)
    assert oplus_def.name == '(+)', oplus_def.name
    assert oplus_def.local is True, oplus_def.local
    assert oplus_def.function is None, oplus_def.function
    arity = oplus_def.arity
    definiens = oplus_def.definiens
    # arity
    assert len(arity) == 2, arity
    param_a, param_b = arity
    # parameter `A`
    assert param_a.symbol.name == 'OPERATOR_APPLICATION', (
        param_a.symbol)
    assert param_a.operator == 'A', param_a.operator
    assert param_a.arguments is None, param_a.arguments
    # parameter `B`
    assert param_b.symbol.name == 'OPERATOR_APPLICATION', (
        param_b.symbol)
    assert param_b.operator == 'B', param_b.operator
    assert param_b.arguments is None, param_b.arguments
    # definiens `TRUE`
    assert definiens.symbol.name == 'BOOLEAN_LITERAL', (
        definiens.symbol)
    assert definiens.value == 'TRUE', definiens
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_pipe_instantiation():
    text = r'''
        ---- MODULE pipe_inst ----
        INSTANCE M WITH | <- |, x <- | x
        ====
        '''
    module = _lr.parse(text)
    assert module is not None
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'pipe_inst', module.name
    assert len(module.units) == 1, len(module.units)
    # instance
    instance, = module.units
    assert instance.symbol.name == 'INSTANCE', (
        instance.symbol)
    assert instance.name == 'M', instance.name
    assert instance.local is None, instance.local
    with_ = instance.with_substitution
    assert len(with_) == 2, len(with_)
    pipe_sub, x_sub = with_
    # `| <- |`
    assert pipe_sub.symbol.name == 'WITH_INSTANTIATION', (
        pipe_sub.symbol)
    assert pipe_sub.name == '|', pipe_sub.name
    assert pipe_sub.expression == '|', pipe_sub.expression
    # `x <- x`
    assert x_sub.symbol.name == 'WITH_INSTANTIATION', (
        x_sub.symbol)
    assert x_sub.name == 'x', x_sub.name
    vexpr = x_sub.expression
    assert vexpr.symbol.name == 'VERTICAL_LIST', (
        vexpr.symbol)
    assert vexpr.operator == '|', vexpr.operator
    assert len(vexpr.arguments) == 1, vexpr.arguments
    vitem, = vexpr.arguments
    assert vitem.symbol.name == 'VERTICAL_ITEM', (
        vitem.symbol)
    assert vitem.operator == '|', vitem.operator
    expr = vitem.expression
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == 'x', expr.operator
    assert expr.arguments is None, expr.arguments
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_nested_proofs():
    module_name = 'case_proof_step'
    source = r'''
        ---- MODULE case_proof_step ----
        THEOREM TRUE
        PROOF
        <1>1. CASE x
            PROOF
            <2>1. x = 1
            <2> QED
                BY <2>1
        <1>2. CASE ~ x
            OBVIOUS
        <1> QED
        ====
        '''
    module = _lr.parse(source)
    assert module is not None
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'case_proof_step', module.name
    assert len(module.units) == 1, len(module.units)
    # theorem
    theorem, = module.units
    assert theorem.name is None, theorem.name
    assert theorem.theorem_keyword == 'THEOREM', (
        theorem.theorem_keyword)
    goal = theorem.goal
    proof = theorem.proof
    # theorem goal TRUE
    assert goal.symbol.name == 'BOOLEAN_LITERAL', (
        goal.symbol)
    assert goal.value == 'TRUE', goal.value
    # proof
    assert proof.symbol.name == 'PROOF'
    assert proof.proof_keyword is True, proof.proof_keyword
    assert len(proof.steps) == 3, len(proof.steps)
    step_11, step_12, step_1qed = proof.steps
    # step <1>1
    assert step_11.symbol.name == 'PROOF_STEP', (
        step_11.symbol.name)
    assert step_11.proof_keyword is True, (
        step_11.proof_keyword)
    assert step_11.name == '<1>1.', step_11.name
    main = step_11.main
    proof = step_11.proof
    # goal `CASE x`
    assert main.symbol.name == 'PROOF_CASE', main.symbol
    expr = main.expression
    # expression `x`
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == 'x', expr.operator
    assert expr.arguments is None, expr.arguments
    # nested proof of <1>1
    assert proof.symbol.name == 'PROOF', proof.symbol
    assert proof.proof_keyword is None, proof.proof_keyword
    assert len(proof.steps) == 2, len(proof.steps)
    step_21, step_2qed = proof.steps
    # step <2>1
    assert step_21.symbol.name == 'PROOF_STEP', (
        step_21.symbol)
    assert step_21.proof is None, step_21.proof
    assert step_21.proof_keyword is None, (
        step_21.proof_keyword)
    assert step_21.name == '<2>1.', step_21.name
    main = step_21.main
    # goal `x = 1`
    assert main.symbol.name == 'OPERATOR_APPLICATION', (
        main.symbol)
    assert main.operator == '=', main.operator
    assert len(main.arguments) == 2, len(main.arguments)
    x, one = main.arguments
    assert x.symbol.name == 'OPERATOR_APPLICATION', (
        x.symbol)
    assert x.operator == 'x', x.operator
    assert x.arguments is None, x.arguments
    assert one.symbol.name == 'INTEGRAL_NUMERAL', (
        one.symbol)
    assert one.value == '1', one.value
    # step <2> QED
    assert step_2qed.symbol.name == 'PROOF_STEP', (
        step_2qed.symbol)
    assert step_2qed.name == '<2>', step_2qed.name
    assert step_2qed.main == 'QED', step_2qed.main
    assert step_2qed.proof is not None, step_2qed.proof
    assert step_2qed.proof_keyword is None, (
        step_1qed.proof_keyword)
    # proof `BY <2>1`
    proof = step_2qed.proof
    assert proof.symbol.name == 'BY', proof.symbol
    assert proof.only is False, proof.only
    assert proof.names is None, proof.names
    assert len(proof.facts) == 1, proof.facts
    step_name, = proof.facts
    assert (step_name.symbol.name ==
        'OPERATOR_APPLICATION'), step_name.symbol
    assert step_name.operator == '<2>1', step_name.operator
    assert step_name.arguments is None, step_name.arguments
    # step <1>2
    assert step_12.symbol.name == 'PROOF_STEP', (
        step_12.symbol.name)
    assert step_12.name == '<1>2.', step_12.name
    assert step_12.proof_keyword is None, (
        step_12.proof_keyword)
    main = step_12.main
    proof = step_12.proof
    # goal `CASE ~ x`
    assert main.symbol.name == 'PROOF_CASE', main.symbol
    expr = main.expression
    # expression `~ x`
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == '~', expr.operator
    assert len(expr.arguments) == 1, len(expr.arguments)
    arg, = expr.arguments
    assert arg.symbol.name == 'OPERATOR_APPLICATION', (
        arg.symbol)
    assert arg.operator == 'x', arg.operator
    assert arg.arguments is None, arg.arguments
    # proof OBVIOUS
    assert proof.symbol.name == 'OBVIOUS', proof.symbol
    # step <1> QED
    assert step_1qed.symbol.name == 'PROOF_STEP', (
        step_1qed.symbol)
    assert step_1qed.name == '<1>', step_1qed
    assert step_1qed.main == 'QED', step_1qed.main
    assert step_1qed.proof is None, step_1qed.proof
    assert step_1qed.proof_keyword is None, (
        step_1qed.proof_keyword)
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_function_definition():
    module_name = 'function_definition'
    source = r'''
        ---- MODULE function_definition ----
        f[n \in Nat] == n + 1
        ====
        '''
    module = _lr.parse(source)
    assert module.symbol.name == 'MODULE', module
    assert module.name == module_name, module
    assert len(module.units) == 1, module
    f_def, = module.units
    # `f` definition
    assert (f_def.symbol.name ==
        'OPERATOR_DEFINITION'), f_def
    assert f_def.name == 'f', f_def
    assert f_def.arity is None, f_def
    assert f_def.local is None, f_def
    assert f_def.function is True, f_def
    # `f` definiens
    f_definiens = f_def.definiens
    assert (f_definiens.symbol.name ==
        'FUNCTION'), f_definiens
    # function constructor
    assert isinstance(
        f_definiens.declaration, list), f_definiens
    decl, = f_definiens.declaration
    expr = f_definiens.value
    # function declaration
    assert (decl.symbol.name ==
        'OPERATOR_APPLICATION'), decl
    assert decl.operator == '\\in', decl
    assert len(decl.arguments) == 2, decl
    n, nat = decl.arguments
    assert (n.symbol.name ==
        'OPERATOR_APPLICATION'), n
    assert n.arguments is None, n
    assert n.operator == 'n', n
    assert (nat.symbol.name ==
        'OPERATOR_APPLICATION'), nat
    assert nat.arguments is None, nat
    assert nat.operator == 'Nat', nat
    # function value
    assert (expr.symbol.name ==
        'OPERATOR_APPLICATION'), expr
    assert expr.operator == '+', expr
    assert len(expr.arguments) == 2, expr
    n, one = expr.arguments
    assert (n.symbol.name ==
        'OPERATOR_APPLICATION'), n
    assert n.arguments is None, n
    assert n.operator == 'n', n
    assert (one.symbol.name ==
        'INTEGRAL_NUMERAL'), one
    assert one.value == '1', one


def test_vertical_operators():
    module_name = 'vertical_after_infix'
    source = r'''
        ---- MODULE vertical_after_infix ----
        A == \/ b / /\ c
        ====
        '''
    module = _lr.parse(source)
    assert module.symbol.name == 'MODULE', module
    assert module.name == module_name, module
    assert len(module.units) == 1, module
    a_def, = module.units
    # `A` definition
    assert (a_def.symbol.name ==
        'OPERATOR_DEFINITION'), a_def
    assert a_def.name == 'A', a_def
    assert a_def.arity is None, a_def
    assert a_def.local is None, a_def
    # `A` definiens
    a_definiens = a_def.definiens
    assert (a_definiens.symbol.name ==
        'VERTICAL_LIST'), a_definiens
    assert a_definiens.operator == r'\/', a_definiens
    assert len(a_definiens.arguments) == 1, a_definiens
    # disjunct `\/ b / /\ c`
    disjunct, = a_definiens.arguments
    assert (disjunct.symbol.name ==
        'VERTICAL_ITEM'), item
    assert disjunct.operator == r'\/', disjunct
    # expression `b / /\ c`
    expr = disjunct.expression
    assert (expr.symbol.name ==
        'OPERATOR_APPLICATION'), expr
    assert expr.operator == '/', expr
    assert len(expr.arguments) == 2, expr
    b_expr, conj = expr.arguments
    # expression `b`
    assert (b_expr.symbol.name ==
        'OPERATOR_APPLICATION'), b_expr
    assert b_expr.operator == 'b', b_expr
    assert b_expr.arguments is None, b_expr
    # expression `/\ c`
    assert (conj.symbol.name ==
        'VERTICAL_LIST'), conj
    assert conj.operator == '/\\', conj
    assert len(conj.arguments) == 1, conj
    # conjunct `/\ c`
    conjunct, = conj.arguments
    assert (conjunct.symbol.name ==
        'VERTICAL_ITEM'), conjunct
    # expression `c`
    c_expr = conjunct.expression
    assert (c_expr.symbol.name ==
        'OPERATOR_APPLICATION'), c_expr
    assert c_expr.operator == 'c', c_expr
    assert c_expr.arguments is None, c_expr


def test_preamble_comments():
    module_name = 'preamble_comments'
    module_text = r'''
        A == 1
        ---- MODULE preamble_comments ----
        LOCAL B == 1
        ====
        A == 1
        '''
    module = _lr.parse(module_text)
    assert module.symbol.name == 'MODULE', module
    assert module.name == module_name, module
    assert len(module.units) == 1, module
    b_def, = module.units
    # `B` definition
    assert (b_def.symbol.name ==
        'OPERATOR_DEFINITION'), b_def
    assert b_def.name == 'B', b_def
    assert b_def.arity is None, b_def
    assert b_def.local is True, b_def
    # `B` definiens
    b_definiens = b_def.definiens
    assert (b_definiens.symbol.name ==
        'INTEGRAL_NUMERAL'), b_definiens
    assert b_definiens.value == '1', b_definiens


def test_lambda_inside_undelimited():
    module_name = 'lambda_inside_undelimited'
    source = rf'''
        ---- MODULE {module_name} ----
        B(r(_)) == r(1)
        A == \A x:  B(LAMBDA y: TRUE) /\ FALSE
        ====
        '''
    module = _lr.parse(source)
    assert module.symbol.name == 'MODULE', module
    assert module.name == module_name, module
    assert len(module.units) == 2, module
    b_def, a_def = module.units
    # `B` definition
    assert (b_def.symbol.name ==
        'OPERATOR_DEFINITION'), b_def
    assert b_def.name == 'B', b_def
    assert b_def.arity is not None, b_def
    assert b_def.local is None, b_def
    # `B` signature
    b_parameters = b_def.arity
    assert len(b_parameters) == 1, b_parameters
    # parameter `r`
    r_param, = b_parameters
    assert (r_param.symbol.name ==
        'OPERATOR_APPLICATION'), r_param
    assert r_param.operator == 'r', r_param
    assert r_param.arguments == ['_'], r_param
    # `B` definiens
    b_definiens = b_def.definiens
    assert (b_definiens.symbol.name ==
        'OPERATOR_APPLICATION'), b_definiens
    assert b_definiens.operator == 'r', b_definiens
    assert len(
        b_definiens.arguments) == 1, b_definiens
    # argument of `r(1)`
    one, = b_definiens.arguments
    assert one.symbol.name == 'INTEGRAL_NUMERAL', one
    assert one.value == '1', one
    # `B` definition
    assert (a_def.symbol.name ==
        'OPERATOR_DEFINITION'), a_def
    assert a_def.name == 'A', a_def
    assert a_def.arity is None, a_def
    assert a_def.local is None, a_def
    # `A` definiens
    a_definiens = a_def.definiens
    assert (a_definiens.symbol.name ==
        'QUANTIFICATION'), a_definiens
    assert a_definiens.quantifier == '\\A', a_definiens
    # quantifier declaree `x`
    a_declarations = a_definiens.declarations
    assert len(a_declarations) == 1, a_declarations
    x_declaration, = a_declarations
    assert (x_declaration.symbol.name ==
        'OPERATOR_APPLICATION'), x_declaration
    assert x_declaration.operator == 'x', x_declaration
    assert x_declaration.arguments is None, x_declaration
    # quantifier predicate
    a_predicate = a_definiens.predicate
    assert (a_predicate.symbol.name ==
        'OPERATOR_APPLICATION'), a_predicate
    assert a_predicate.operator == '/\\', a_predicate
    assert len(a_predicate.arguments) == 2, a_predicate
    arg1, arg2 = a_predicate.arguments
    # expression `B(LAMBDA y: TRUE)`
    assert (arg1.symbol.name ==
        'OPERATOR_APPLICATION'), arg1
    assert arg1.operator == 'B', arg1
    assert len(arg1.arguments) == 1, arg1
    # operator `LAMBDA y: TRUE`
    lambda_y, = arg1.arguments
    assert lambda_y.symbol.name == 'LAMBDA', lambda_y
    assert len(lambda_y.parameters) == 1, lambda_y
    # `LAMBDA` parameter: `y`
    y_param, = lambda_y.parameters
    assert (y_param.symbol.name ==
        'OPERATOR_APPLICATION'), y_param
    assert y_param.operator == 'y', y_param
    assert y_param.arguments is None, y_param
    # `LAMBDA` expression: `TRUE`
    lambda_expr = lambda_y.expression
    assert (lambda_expr.symbol.name ==
        'BOOLEAN_LITERAL'), lambda_expr
    assert lambda_expr.value == 'TRUE', lambda_expr
    # conjunct `FALSE`
    assert (arg2.symbol.name ==
        'BOOLEAN_LITERAL'), arg2
    assert arg2.value == 'FALSE', arg2


def test_nested_undelimited():
    source = r'''
        ---- MODULE let_quantification ----
        EXTENDS
            Integers

        A == LET
                b == FALSE
             IN
                \A x, y \in S:  b
        ====
        '''
    module = _lr.parse(source)
    assert module.symbol.name == 'MODULE', module
    assert module.name == 'let_quantification', module.name
    assert len(module.extendees) == 1, module.extendees
    integers, = module.extendees
    assert_operator_name(integers, 'Integers')
    assert len(module.units) == 1, module.units
    a_def, = module.units
    assert a_def.symbol.name == 'OPERATOR_DEFINITION', (
        a_def.symbol)
    assert a_def.name == 'A', a_def.name
    assert a_def.arity is None, a_def.arity
    assert a_def.local is None, a_def.local
    assert a_def.function is None, a_def.function
    let = a_def.definiens
    # `LET`
    assert let.symbol.name == 'LET', let.symbol
    assert len(let.definitions) == 1, let.definitions
    b_def, = let.definitions
    qexpr = let.expression
    # `b == FALSE`
    assert b_def.symbol.name == 'OPERATOR_DEFINITION', (
        b_def.symbol)
    assert b_def.arity is None, b_def.arity
    assert b_def.local is None, b_def.local
    assert b_def.function is None, b_def.function
    expr = b_def.definiens
    assert_boolean_literal(expr, 'FALSE')
    # `\A x, y \in S:  b`
    assert qexpr.symbol.name == 'QUANTIFICATION', (
        qexpr.symbol)
    assert qexpr.quantifier == '\\A', qexpr.quantifier
    assert len(qexpr.declarations) == 2, qexpr.declarations
    decls = qexpr.declarations
    pred = qexpr.predicate
    # `x, y \in S`
    x, y_in_s = decls
    assert_operator_name(x, 'x')
    assert_binary_op_app(y_in_s, '\\in')
    y, s = y_in_s.arguments
    assert_operator_name(y, 'y')
    assert_operator_name(s, 'S')
    # `b`
    assert_operator_name(pred, 'b')
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_let_expression():
    source = '''
        ---- MODULE let_expr ----
        THEOREM
            LET a == FALSE IN TRUE
        BY TRUE
        ====
        '''
    module = _lr.parse(source)
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'let_expr', module.name
    assert module.extendees is None, module.extendees
    assert len(module.units) == 1, module.units
    theorem, = module.units
    assert theorem.symbol.name == 'THEOREM', theorem.symbol
    assert theorem.name is None, theorem.name
    assert theorem.theorem_keyword == 'THEOREM', (
        theorem.theorem_keyword)
    let = theorem.goal
    proof = theorem.proof
    # theorem assertion
    assert let.symbol.name == 'LET', let.symbol
    assert len(let.definitions) == 1, len(let.definitions)
    defn, = let.definitions
    in_expr = let.expression
    # `a == FALSE`
    assert defn.symbol.name == 'OPERATOR_DEFINITION', (
        defn.symbol)
    assert defn.name == 'a', defn.name
    assert defn.arity is None, defn.arity
    assert defn.local is None, defn.local
    assert defn.function is None, defn.function
    expr = defn.definiens
    assert_boolean_literal(expr, 'FALSE')
    # `TRUE`
    assert_boolean_literal(in_expr, 'TRUE')
    # proof
    assert proof.symbol.name == 'PROOF', proof.symbol
    assert proof.proof_keyword is None, proof.proof_keyword
    assert len(proof.steps) == 1, proof.steps
    leaf_proof, = proof.steps
    assert leaf_proof.symbol.name == 'BY', (
        leaf_proof.symbol)
    assert leaf_proof.only is False, leaf_proof.only
    assert leaf_proof.names is None, leaf_proof.names
    assert len(leaf_proof.facts) == 1, leaf_proof.facts
    expr, = leaf_proof.facts
    assert_boolean_literal(expr, 'TRUE')
    # print
    text = _pp.pformat_ast(module)
    print(text)


def test_definition_inside_vertical_operator():
    parser = _lr.Parser()
    # module-scope definition indented less
    # than the preceeding vertical operator
    source = r'''
        ---- MODULE smaller_indent ----
        A == /\ 1
             /\ 2

        B == 3
        ====
        '''
    module = parser.parse(source)
    _check_def_inside_vop(
        module, 'smaller_indent')
    # module-scope definition indented more
    # than the preceeding vertical operator
    source = r'''
        ---- MODULE larger_indent ----
        A == /\ 1
             /\ 2

                B == 3
        ====
        '''
    module = parser.parse(source)
    _check_def_inside_vop(
        module, 'larger_indent')
    # definition on the same line
    # with a vertical operator
    source = r'''
        ---- MODULE same_line ----
        A == /\ 1
             /\ 2     B == 3
        ====
        '''
    module = parser.parse(source)
    _check_def_inside_vop(
        module, 'same_line')
    # definition inside `LET` that
    # is within a vertical operator
    source = r'''
        ---- MODULE let_inside_vertical ----
        A == /\ LET B == 3 IN B
        ====
        '''
    module = parser.parse(source)
    _check_def_inside_let(
        module, 'let_inside_vertical')


def _check_def_inside_let(
        module, module_name):
    # module
    assert module.symbol.name == 'MODULE', module
    assert module.name == module_name, module
    assert len(module.units) == 1, module
    # `A` definition
    a_def, = module.units
    assert (a_def.symbol.name ==
        'OPERATOR_DEFINITION'), a_def
    assert a_def.name == 'A', a_def
    assert a_def.arity is None, a_def
    assert a_def.local is None, a_def
    # `A` definiens
    a_definiens = a_def.definiens
    assert (a_definiens.symbol.name ==
        'VERTICAL_LIST'), a_definiens
    assert a_definiens.operator == '/\\', a_definiens
    assert len(a_definiens.arguments) == 1, a_definiens
    # first conjunct
    item, = a_definiens.arguments
    assert item.symbol.name == 'VERTICAL_ITEM', item
    assert item.operator == '/\\', item
    # `LET` expression
    let = item.expression
    assert let.symbol.name == 'LET', let
    assert len(let.definitions) == 1, let
    # `B` definition
    b_def, = let.definitions
    assert (b_def.symbol.name ==
        'OPERATOR_DEFINITION'), b_def
    assert b_def.name == 'B', b_def
    assert b_def.arity is None, b_def
    assert b_def.local is None, b_def
    # `B` definiens
    b_definiens = b_def.definiens
    assert (b_definiens.symbol.name ==
        'INTEGRAL_NUMERAL'), b_definiens
    assert b_definiens.value == '3', b_definiens
    # `IN` expression
    in_expr = let.expression
    assert (in_expr.symbol.name ==
        'OPERATOR_APPLICATION'), in_expr
    assert in_expr.operator == 'B', in_expr
    assert in_expr.arguments == None, in_expr


def _check_def_inside_vop(
        module, module_name):
    # module
    assert module.symbol.name == 'MODULE', module
    assert module.name == module_name, module
    assert len(module.units) == 2, module
    a_def, b_def = module.units
    # `A` definition
    assert (a_def.symbol.name ==
        'OPERATOR_DEFINITION'), a_def
    assert a_def.name == 'A', a_def
    assert a_def.arity is None, a_def
    assert a_def.local is None, a_def
    # `A` definiens
    a_definiens = a_def.definiens
    assert (a_definiens.symbol.name ==
        'VERTICAL_LIST'), a_definiens
    assert a_definiens.operator == '/\\', a_definiens
    assert len(a_definiens.arguments) == 2, a_definiens
    item_1, item_2 = a_definiens.arguments
    # first conjunct
    assert (item_1.symbol.name ==
        'VERTICAL_ITEM'), item_1
    assert item_1.operator == '/\\', item_1
    one = item_1.expression
    assert (one.symbol.name ==
        'INTEGRAL_NUMERAL'), one
    assert one.value == '1', one
    # second conjunct
    assert (item_2.symbol.name ==
        'VERTICAL_ITEM'), item_2
    assert item_2.operator == '/\\', item_2
    two = item_2.expression
    assert (two.symbol.name ==
        'INTEGRAL_NUMERAL'), two
    assert two.value == '2', two
    # `B` definition
    assert (b_def.symbol.name ==
        'OPERATOR_DEFINITION'), b_def
    assert b_def.name == 'B', b_def
    assert b_def.arity is None, b_def
    assert b_def.local is None, b_def
    # `B` definiens
    b_definiens = b_def.definiens
    assert (b_definiens.symbol.name ==
        'INTEGRAL_NUMERAL'), b_definiens
    assert b_definiens.value == '3', b_definiens


def test_optional_proof_keyword_define():
    # module-scope definition indented less
    # than the preceeding vertical operator
    source = '''
        ---- MODULE optional_DEFINE ----
        THEOREM TRUE
        <1> A == 1
            B == 2
        <1> QED

        C == 3
        ====
        '''
    module = _lr.parse(source)
    # module
    assert module.symbol.name == 'MODULE', module
    assert module.name == 'optional_DEFINE', module
    assert len(module.units) == 2, module
    thm, c_def = module.units
    # theorem
    assert thm.name is None, thm
    # theorem assertion
    goal = thm.goal
    assert (goal.symbol.name ==
        'BOOLEAN_LITERAL'), goal
    assert goal.value == 'TRUE', goal
    # proof
    proof = thm.proof
    assert proof.symbol.name == 'PROOF', proof
    assert len(proof.steps) == 2, proof
    # steps
    defs_step, qed_step = proof.steps
    # proof first step
    assert (defs_step.symbol.name ==
        'PROOF_STEP'), defs_step
    assert defs_step.proof is None, defs_step
    # step number of first step
    step_num = defs_step.name
    # definitions
    define_main = defs_step.main
    assert (define_main.symbol.name ==
        'DEFINE'), define_main
    assert len(
        define_main.definitions) == 2, define_main
    a_def, b_def = define_main.definitions
    # `A` definition
    assert (a_def.symbol.name ==
        'OPERATOR_DEFINITION'), a_def
    assert a_def.name == 'A', a_def
    assert a_def.arity is None, a_def
    assert a_def.local is None, a_def
    # `A` definiens
    a_definiens = a_def.definiens
    assert (a_definiens.symbol.name ==
        'INTEGRAL_NUMERAL'), a_definiens
    assert a_definiens.value == '1', a_definiens
    # `B` definition
    assert (b_def.symbol.name ==
        'OPERATOR_DEFINITION'), b_def
    assert b_def.name == 'B', b_def
    assert b_def.arity is None, b_def
    assert b_def.local is None, b_def
    # `B` definiens
    b_definiens = b_def.definiens
    assert (b_definiens.symbol.name ==
        'INTEGRAL_NUMERAL'), b_definiens
    assert b_definiens.value == '2', b_definiens
    # QED step
    assert qed_step.main == 'QED', qed_step


def test_dot_function_application_prime():
    # The expression in this test is from
    # page 284 of the book "Specifying Systems".
    module_name = 'dot_func_prime'
    source = f'''
        ---- MODULE {module_name} ----
        A == a + b.c[d]'
        ====
        '''
    module = _lr.parse(source)
    assert module.symbol.name == 'MODULE', module
    assert module.name == module_name, module
    assert len(module.units) == 1, module
    # `A` definition
    a_def, = module.units
    assert (a_def.symbol.name ==
        'OPERATOR_DEFINITION'), a_def
    assert a_def.name == 'A', a_def
    assert a_def.arity is None, a_def
    assert a_def.local is None, a_def
    # `A` definiens: `a + b.c[d]'`
    a_definiens = a_def.definiens
    assert (a_definiens.symbol.name ==
        'OPERATOR_APPLICATION'), a_definiens
    assert a_definiens.operator == '+', a_definiens
    assert len(a_definiens.arguments) == 2, a_definiens
    first, second = a_definiens.arguments
    # first summand: `a`
    assert (first.symbol.name ==
        'OPERATOR_APPLICATION'), first
    assert first.operator == 'a', first
    assert first.arguments is None, first
    # second summand: `b.c[d]'`
    assert (second.symbol.name ==
        'OPERATOR_APPLICATION'), second
    assert second.operator == "'", second
    assert len(second.arguments) == 1, second
    app, = second.arguments
    # function application `b.c[d]`
    assert (app.symbol.name ==
        'FUNCTION_APPLICATION'), app
    assert len(app.arguments) == 1, app
    func = app.function
    d_expr, = app.arguments
    # `d` expression
    assert (d_expr.symbol.name ==
        'OPERATOR_APPLICATION'), d_expr
    assert d_expr.operator == 'd', d_expr
    assert d_expr.arguments is None, d_expr
    # `b.c` expression
    assert func.symbol.name == 'FIELD', func
    b_expr = func.expression
    c_expr = func.name
    # expression `b`
    assert (b_expr.symbol.name ==
        'OPERATOR_APPLICATION'), b_expr
    assert b_expr.operator == 'b', b_expr
    assert b_expr.arguments is None, b_expr
    # field `c` of `b.c`
    assert c_expr == 'c', c_expr


def test_parsing_of_proofs():
    source = '''
        ---- MODULE theorem_and_proof ----
        THEOREM TRUE
        PROOF
        <1>1. TRUE
        <1> QED
        ====
        '''
    module = _lr.parse(source)
    assert module.symbol.name == 'MODULE', module
    assert module.name == 'theorem_and_proof', module
    assert len(module.units) == 1, module
    theorem, = module.units
    # `THEOREM`
    assert (theorem.symbol.name ==
        'THEOREM'), theorem
    assert theorem.name is None, theorem
    # goal of theorem
    goal = theorem.goal
    assert goal.symbol.name == 'BOOLEAN_LITERAL', goal
    assert goal.value == 'TRUE', goal
    # `PROOF`
    proof = theorem.proof
    assert proof.symbol.name == 'PROOF', proof
    assert len(proof.steps) == 2, proof
    step, qed_step = proof.steps
    # step `<1>1`
    assert (step.symbol.name ==
        'PROOF_STEP'), step
    assert step.proof is None, step
    # step number `<1>1.`
    assert step.name == '<1>1.', step.name
    # expression `TRUE` in step `<1>1`
    main = step.main
    # `QED` step
    assert (qed_step.symbol.name ==
        'PROOF_STEP'), qed_step
    assert qed_step.main == 'QED', qed_step
    assert qed_step.proof is None, qed_step
    # step number `<1>` of `QED` step
    assert qed_step.name == '<1>', qed_step
    # theorem with a leaf proof
    source = '''
        ---- MODULE theorem_and_proof ----
        THEOREM TRUE
        PROOF
        <1>1. TRUE
        <1> QED
            BY <1>1
        ====
        '''
    module = _lr.parse(source)
    theorem, = module.units
    proof = theorem.proof
    _, qed_step = proof.steps
    assert (qed_step.symbol.name ==
        'PROOF_STEP'), qed_step
    assert qed_step.main == 'QED', qed_step
    assert qed_step.proof is not None, qed_step
    # `BY`
    by = qed_step.proof
    assert (by.symbol.name == 'BY'), by
    assert by.names is None, by
    # expressions of `BY`
    facts = by.facts
    assert len(facts) == 1, facts
    # fact `<1>1` in the leaf proof `BY <1>1`
    fact, = facts
    assert (fact.symbol.name ==
        'OPERATOR_APPLICATION'), fact
    assert fact.operator == '<1>1', fact
    assert fact.arguments is None, fact


def test_record_fields():
    source = '''
        ---- MODULE record_fields ----
        A == LET b == FALSE IN b.c
        ====
        '''
    module = _lr.parse(source)
    assert module.symbol.name == 'MODULE', module.symbol
    assert module.name == 'record_fields', module.name
    assert len(module.units) == 1, module
    # `A` definition
    a_def, = module.units
    assert (a_def.symbol.name ==
        'OPERATOR_DEFINITION'), a_def
    assert a_def.name == 'A', a_def
    assert a_def.arity is None, a_def
    assert a_def.local is None, a_def
    # definiens of `A`
    a_definiens = a_def.definiens
    assert (a_definiens.symbol.name ==
        'LET'), a_definiens
    # definitions of `LET` expression
    definitions = a_definiens.definitions
    assert len(definitions) == 1, definitions
    # `b` definition
    b_def, = definitions
    assert (b_def.symbol.name ==
        'OPERATOR_DEFINITION'), b_def
    assert b_def.arity is None, b_def
    assert b_def.local is None, b_def
    # definiens of `b`
    b_definiens = b_def.definiens
    assert (b_definiens.symbol.name ==
        'BOOLEAN_LITERAL'), b_definiens
    assert b_definiens.value == 'FALSE', b_definiens
    # `IN` expression of `LET`
    b_c = a_definiens.expression
    assert (b_c.symbol.name ==
        'FIELD'), b_c
    assert b_c.name == 'c', b_c
    # expression `b`
    b_expr = b_c.expression
    assert (b_expr.symbol.name ==
        'OPERATOR_APPLICATION'), b_expr
    assert b_expr.operator == 'b', b_expr
    assert b_expr.arguments is None, b_expr
    # multiple dots
    parser = _lr.Parser()
    source = '''
        ---- MODULE record_fields ----
        A == a.b.c
        ====
        '''
    module = parser.parse(source)
    assert len(module.units) == 1, module
    a_def, = module.units
    assert (a_def.symbol.name ==
        'OPERATOR_DEFINITION'), a_def
    # expression `a.b.c`
    a_b_c = a_def.definiens
    assert (a_b_c.symbol.name == 'FIELD'), a_b_c
    assert a_b_c.name == 'c', a_b_c
    # expression `a.b`
    a_b = a_b_c.expression
    assert (a_b.symbol.name == 'FIELD'), a_b
    assert a_b.name == 'b', a_b
    # expression `a`
    a_expr = a_b.expression
    assert (a_expr.symbol.name ==
        'OPERATOR_APPLICATION'), a_expr
    assert a_expr.operator =='a', a_expr
    assert a_expr.arguments is None, a_expr


def test_neg_operator_precedence():
    source = r'''
        ---- MODULE experiment ----
        A == TRUE # ~ TRUE
        ====
        '''
    module = _lr.parse(source)
    assert module is not None
    assert len(module.units) == 1, module
    a_def, = module.units
    assert_op_def(a_def, 'A')
    expr = a_def.definiens
    assert_binary_op_app(expr, '#')
    true, neg_true = expr.arguments
    assert_boolean_literal(true, 'TRUE')
    assert_unary_op_app(neg_true, '~')
    true, = neg_true.arguments
    assert_boolean_literal(true, 'TRUE')


def test_unary_minus_operator_precedence():
    source = r'''
        ---- MODULE experiment ----
        A == 1 * - 2
        ====
        '''
    module = _lr.parse(source)
    assert module is not None
    assert len(module.units) == 1, module
    a_def, = module.units
    assert_op_def(a_def, 'A')
    expr = a_def.definiens
    assert_binary_op_app(expr, '*')
    one, minus_two = expr.arguments
    assert_integer_numeral(one, '1')
    assert_unary_op_app(minus_two, '-')
    two, = minus_two.arguments
    assert_integer_numeral(two, '2')


def assert_op_def(
        op_def,
        operator_name:
            str):
    """Assert definition of operator,

    without parameters.
    """
    assert op_def.symbol.name == 'OPERATOR_DEFINITION', (
        op_def.symbol)
    assert op_def.name == operator_name, op_def.name
    assert op_def.arity is None, op_def.arity
    assert op_def.local is None, op_def.local
    assert op_def.function is None, op_def.function


def assert_unary_op_app(
        expr,
        operator_name:
            str):
    """Assert unary operator application."""
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == operator_name, expr.operator
    assert len(expr.arguments) == 1, expr.arguments


def assert_binary_op_app(
        expr,
        operator_name:
            str):
    """Assert binary operator application."""
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == operator_name, expr.operator
    assert len(expr.arguments) == 2, expr.arguments


def assert_operator_name(
        expr,
        operator_name:
            str):
    """Assert nullary operator application."""
    assert expr.symbol.name == 'OPERATOR_APPLICATION', (
        expr.symbol)
    assert expr.operator == operator_name, expr.operator
    assert expr.arguments is None, expr.arguments


def assert_boolean_literal(
        expr,
        value:
            str):
    """Assert Boolean literal with `value`."""
    assert expr.symbol.name == 'BOOLEAN_LITERAL', expr.symbol
    assert expr.value == value, expr.value


def assert_integer_numeral(
        expr,
        value:
            str):
    """Assert integral numeral with `value`."""
    assert expr.symbol.name == 'INTEGRAL_NUMERAL', expr.symbol
    assert expr.value == value, expr.value


if __name__ == '__main__':
    # test_preamble_comments()
    # test_vertical_operators()
    test_set_of_tuples()
    # test_unary_minus_as_argument()
    # test_set_theory_operators()
    # test_keyword_unary_operators()
    # test_unary_minus_as_operator()
    # test_set_slice_operator()
    # test_set_comprehension_operator()
    # test_quantifier_vertical_expression()
    # test_vertical_expr_proof_step()
    # test_quantifier_vertical_expression()
    # test_named_theorem()
    # test_quantifier_temporal()
    # test_unary_minus_operator_definition()
    # test_binary_operator_definition()
    # test_nested_proofs()
    # test_pipe_instantiation()
    # test_lambda_inside_undelimited()
    # test_eventually_always()
    # test_let_expression()
    # test_definition_inside_vertical_operator()
    # test_optional_proof_keyword_define()
    # test_dot_function_application_prime()
    # test_parsing_of_proofs()
    # test_record_fields()
    # error_operator_precedence()
    print('tests completed')
