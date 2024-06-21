"""Syntax tree that represents TLA+."""
import argparse as _arg
import collections as _cl
import collections.abc as _abc
import enum
import functools as _ft
import itertools as _itr
import pprint as _pp
import shlex as _sh
import subprocess as _sbp
import time
import typing as _ty

import tla._lex as _lex
import tla._langdef as _opdef


_MIN_LINE_LEN = 4
_DASH_LINE = 'DASH_LINE'
_EQ_LINE = 'EQ_LINE'
_LPAREN = 'LPAREN'
_RPAREN = 'RPAREN'
_LBRACE = 'LBRACE'
_RBRACE = 'RBRACE'
_LBRACKET = 'LBRACKET'
_RBRACKET = 'RBRACKET'
_TLA_OPERATOR_FIXITY = _opdef.TLA_OPERATOR_FIXITY
_lexemes_to_tokens = _lex.map_lexemes_to_tokens()


NODE_SPECS = dict(
    AXIOM=
        'name, expression, axiom_keyword',
    BOOLEAN_LITERAL=
        'value',
    BY=
        'only, facts, names',
    CASES=
        'cases, other',
        # Represents both `CASE` and `ELIF`
        # constructs. The specific form is
        # considered concrete information
        # (tokeny).
    CASE_ITEM=
        'predicate, expression',
    CHOOSE=
        'declaration, predicate',
        # "predicate" here is for readability:
        # this expression may take values outside
        # of the set `BOOLEAN`
    CONSTANTS=
        'names',
    DEFINE=
        'definitions',
    EXCEPT=
        'function, changes',
    FAIRNESS=
        'operator, subscript, action',
    FIELD=
        'expression, name',
    FLOAT_NUMERAL=
        'value',
    FUNCTION=
        'declaration, value',
    FUNCTION_APPLICATION=
        'function, arguments',
    FUNCTION_CHANGE=
        'item, expression',
    HAVE=
        'expression',
    HIDE=
        'facts, names',
    IF=
        'predicate, then, else_',
    IFS=
        'cases, other',
    IF_ITEM=
        'predicate, expression',
    INSTANCE=
        'name, with_substitution, local',
    INTEGRAL_NUMERAL=
        'value',
    KEY_BOUND=
        'name, bound',
    LAMBDA=
        'parameters, expression',
    LET=
        'definitions, expression',
    MODULE=
        'name, extendees, units',
    MODULE_NAME=
        'name',
    OBVIOUS=
        '',
    OMITTED=
        '',
    OPERATOR_APPLICATION=
        'operator, arguments',
    OPERATOR_DECLARATION=
        'name, level, new_keyword',
    OPERATOR_DEFINITION=
        'name, arity, '
        'definiens, local, function',
            # `function` means
            # the form:
            # `f[...] == ...`
    PARAMETER_DECLARATION=
        'name, arity',
    PARENTHESES=
        'expression',
    PICK=
        'declarations, predicate',
    PROOF=
        'steps, proof_keyword',
    PROOF_CASE=
        'expression',
    PROOF_STEP=
        'name, main, proof, proof_keyword',
        # "proof step" distinguishes
        # from a pair of states in
        # the semantics
    QUANTIFICATION=
        'quantifier, declarations, predicate',
        # "predicate" here is for readability:
        # this expression may take values outside
        # of the set `BOOLEAN`
    QUANTIFIER_WITNESS=
        'expressions',
    RECORD=
        'key_values',
    RECURSIVE_OPERATORS=
        'names',
    SEQUENT=
        'assume, prove',
    SET_COMPREHENSION=
        'item, declarations',
        # expression ?
    SET_ENUMERATION=
        'items',
        # expressions ?
    SET_OF_BOOLEANS=
        '',
    SET_OF_FUNCTIONS=
        'domain, codomain',
    SET_OF_RECORDS=
        'key_bounds',
    SET_OF_STRINGS=
        '',
    SET_SLICE=
        'declaration, predicate',
    STRING_LITERAL=
        'value',
    SUBEXPRESSION_REFERENCE=
        'items',
    SUBSCRIPTED_ACTION=
        'operator, action, subscript',
    SUFFICES=
        'predicate',
    TAKE=
        'declarations',
    TEMPORAL_QUANTIFICATION=
        'quantifier, declarations, predicate',
        # "predicate" here is for readability:
        # this expression may take values outside
        # of the set `BOOLEAN`
    THEOREM=
        'name, goal, proof, theorem_keyword',
    TUPLE=
        'items',
    USE=
        'facts, names, only',
    VARIABLES=
        'names',
    VERTICAL_LIST=
        'operator, arguments',
    VERTICAL_ITEM=
        'operator, expression',
    WITH_INSTANTIATION=
        'name, expression'
    )


NodeTypes = enum.StrEnum(
    'NodeTypes',
    sorted(NODE_SPECS))


def make_nodes(
        ) -> _arg.Namespace:
    """Return syntax tree classes."""
    node_types = dict()
    items = NODE_SPECS.items()
    for node_name, attr_names in items:
        class_name = enum_to_class(node_name)
        node_enum = NodeTypes[node_name]
        # attribute names
        attr_names = [
            attr
            for attr in
                attr_names.split(',')
            if attr]
        attr_names = (
            'symbol',
            *attr_names,
            'node_index')
        # default values of attributes
        n_attrs = len(attr_names)
        defaults = (
            (node_enum,) +
            (None,) * (n_attrs - 1))
        attrs = ', '.join(attr_names)
        node_types[class_name] = _cl.namedtuple(
            class_name, attrs,
            defaults=defaults)
    return _arg.Namespace(
        **node_types)


def enum_to_class(
        enum_name:
            str
        ) -> str:
    """Return class name."""
    return enum_name.title().replace('_', '')


def class_to_enum(
        class_name:
            str
        ) -> str:
    """Return enumeration name."""
    def prepend(
            char:
                str
            ) -> str:
        if char.isupper():
            return f'_{char}'
        return char
    enum_name = ''.join(map(
        prepend, class_name))
    return enum_name[1:].upper()


_nodes = make_nodes()
_LEAF_PROOFS = {
    'BY',
    'OBVIOUS',
    'OMITTED'}


def map_steps_to_proofs(
        tree):
    """Map to nested proofs.

    Based on step numbers, lists of steps
    are mapped to hierarchical trees of
    proofs.
    """
    rec = map_steps_to_proofs
    match tree:
        case str() | bool() | None:
            return tree
        case tuple() if not hasattr(tree, 'symbol'):
            return tuple(map(rec, tree))
        case list():
            return list(map(rec, tree))
    enum_name = enum_to_class(
        tree.symbol.name)
    match enum_name:
        case 'Theorem':
            has_leaf_proof = (
                tree.proof is not None and
                len(tree.proof.steps) == 1 and
                tree.proof.steps[0].symbol.name in
                    _LEAF_PROOFS)
            if has_leaf_proof:
                proof = tree.proof
            else:
                proof = rec(tree.proof)
            return _nodes.Theorem(
                name=tree.name,
                goal=tree.goal,
                proof=proof,
                theorem_keyword=
                    tree.theorem_keyword)
        case 'ProofStep':
            proof = rec(tree.proof)
            return _nodes.ProofStep(
                name=tree.name,
                main=tree.main,
                proof=proof,
                proof_keyword=
                    tree.proof_keyword)
        case 'Proof':
            return make_steps_tree(tree)
        case _:
            symbol, *attrs = tree
            attrs = map(rec, attrs)
            cls = type(tree)
            return cls(symbol, *attrs)


def make_steps_tree(
        tree):
    """Return proof tree, from steps sequence."""
    steps_stack = [list()]
    current_level = 1
    steps = tree.steps
    end_step = _nodes.ProofStep(
        name='<1>')
        # used to cause the final popping
        # of levels in `steps_stack` into
        # the first level
    steps.append(end_step)
    for step in steps:
        proof = step.proof
        has_proof = (
            proof is not None and
            proof.symbol.name not in
                _LEAF_PROOFS)
        if has_proof:
            raise ValueError(
                'proof step already has '
                'nonleaf proof')
        level = _step_level(step)
        # print(f'{level = }')
        if level > current_level:
            # print('adding proof level')
            steps_stack.append(list())
            current_level = level
        elif level < current_level:
            while level < current_level:
                # print('popping proof level')
                proof_steps = steps_stack.pop()
                # get step of smaller level
                prev_level = steps_stack[-1]
                last_step = prev_level.pop()
                if last_step.proof is not None:
                    step_num = last_step.name.name
                    raise AssertionError(
                        f'`{step_num}` already has '
                        'a proof, that would be '
                        'overwritten by this '
                        'sequence of proof-steps.')
                current_level = _step_level(last_step)
                proof = _nodes.Proof(
                    steps=proof_steps)
                last_step = _nodes.ProofStep(
                    name=last_step.name,
                    main=last_step.main,
                    proof=proof,
                    proof_keyword=
                        last_step.proof_keyword)
                steps_stack[-1].append(
                    last_step)
        if level != current_level:
            raise AssertionError(
                level, current_level)
        steps_stack[-1].append(step)
    if len(steps_stack) > 1:
        raise AssertionError(
            len(steps_stack))
    proof_steps, = steps_stack
    proof_steps.pop()  # end-step
    return _nodes.Proof(
        steps=proof_steps,
        proof_keyword=tree.proof_keyword)


def _step_level(
        step
        ) -> int:
    """Return level of `step`."""
    label = step.name
    prefix, _ = label.split('>')
    level = int(prefix.lstrip('<'))
    return level


def op_decl_name_bound_arity(
        tree
        ) -> tuple:
    """Return details of `OperatorDeclaration`."""
    if tree.operator == '\\in':
        name, bound = tree.arguments
        arity = None
    else:
        name = tree.operator
        bound = None
        arity = tree.arguments
    if name.arguments is not None:
        raise AssertionError(name)
    name = name.operator
    return (
        name,
        bound,
        arity)


def declarations_as_name_bounds(
        expressions:
            list[tuple]
        ) -> list[tuple]:
    r"""Return names and bounds of declared variables.

    Also duplicates bounds, for example
    `x, y \in S` becomes
    `[(x, S), `(y, S)]`.
    """
    name_bounds = list()
    for expr in expressions:
        if expr.operator == '\\in':
            name, bound = expr.arguments
            name_bounds.append(
                (name, bound))
                # `name` can be a `Tuple`
        elif expr.arguments is None:
            name = expr
            bound = None
            name_bounds.append(
                (name, bound))
        else:
            raise ValueError(expr)
    # ditto bounds
    ditto_bounds = list()
    last_bound = None
    for name, bound in reversed(name_bounds):
        if bound is None:
            bound = last_bound
        last_bound = bound
        ditto_bounds.append(
            (name, bound))
    return list(reversed(ditto_bounds))


def _pformat_nt_tree(
        tree:
            tuple |
            list |
            str
        ) -> str:
    """Format `tree`."""
    d = _pformat_nt_tree_recurse(tree)
    return _pp.pformat(d, width=70)


def _pformat_nt_tree_recurse(
        tree):
    if (isinstance(tree, tuple) and
            hasattr(tree, '_fields')):
        return _pformat_namedtuple(tree)
    elif isinstance(tree, (tuple, list)):
        return _pformat_list(tree)
    else:
        return tree


def _pformat_namedtuple(
        nt):
    d = dict()
    for key in nt._fields:
        value = getattr(nt, key)
        d[key] = _pformat_nt_tree_recurse(value)
    return d


def _pformat_list(
        x):
    return [
        _pformat_nt_tree_recurse(v)
        for v in x]


def dump_tree_as_graph(
        tree:
            tuple,
        filename:
            str
        ) -> None:
    """Layout syntax tree as PDF."""
    graph = _tree_to_graph(tree)
    dot_text = list()
    for node, label in graph.nodes.items():
        node_dot = f'{node} [label="{label}"];'
        dot_text.append(node_dot)
    for node, other in graph.edges:
        edge_dot = f'{node} -> {other};'
        dot_text.append(edge_dot)
    dot_text = '\n'.join(dot_text)
    dot_text = f'digraph {{ {dot_text} }}'
    # write PDF file
    pdf_filename = f'{filename}.pdf'
    dot_filename = f'{filename}.dot'
    with open(dot_filename, 'w') as fd:
        fd.write(dot_text)
    prog = _sh.split(f'''
        dot -Tpdf
            -o {pdf_filename}
            {dot_filename}
        ''')
    _sbp.call(prog)


class DiGraph:
    """Graph with directed edges."""

    def __init__(
            self
            ) -> None:
        self.nodes = dict()
        self.edges = set()


def _tree_to_graph(
        tree):
    """Convert tree to graph."""
    graph = DiGraph()
    _tree_to_graph_recurse(tree, graph)
    return graph


def _tree_to_graph_recurse(
        tree:
            tuple |
            list |
            str,
        graph:
            DiGraph
        ) -> int:
    """Create graph node for `tree`."""
    u = len(graph.nodes)
    if isinstance(tree, tuple):
        label = f'{tree.symbol.name}'
        label = label.replace(
            '.', r'_').replace(
            '"', '').replace(
            '\\', '\\\\')
        graph.nodes[u] = label
    elif isinstance(tree, str):
        label = tree
        label = label.replace(
            '.', r'_').replace(
            '"', '').replace(
            '\\', '\\\\')
        graph.nodes[u] = label
    if isinstance(tree, (tuple, list)):
        for succ in tree:
            if succ is None:
                continue
            v = _tree_to_graph_recurse(
                succ, graph)
            graph.edges.add((u, v))
    return u


Token = _cl.namedtuple(
    'Token',
    'symbol, value, '
    'start_line, start_column, '
    'end_line, end_column, '
    'filename, ast_node_index',
        # symbol \in NodeTypes
        # value \in STRING
        # start = location of start of lexeme
        #     as number of characters from
        #     start of file
        # start \in STRING
        # end = location of end of lexeme
        #     as number of characters from
        #     start of file
        # end \in STRING
        # filename \in STRING
    defaults=(
        None, None, None, None,
        None, None, None, None)
        # defaults enable having undefined
        # location for tokens created when
        # concretizing a syntax tree,
        # before positional information
        # has yet been copied from
        # the input lexemes.
    )


def _make_token(
        value):
    return Token(value, value)


def _make_name_token(
        name):
    if not isinstance(name, str):
        raise AssertionError(name)
    return Token('NAME', name)


def tokenize_ast_root(
        tree:
            tuple,
        _node_index:
            int=0
        ) -> _abc.Iterator[
            Token]:
    """Yield tokens of syntax `tree`.

    Nodes are indexed by DFS preorder.

    The intention is to copy information
    from tokens of the input sequence,
    e.g., positional information,
    without changing the parser.
    """
    tree = _index_by_dfs(tree)
    yield from _tokenize_ast(tree)


def _tokenize_ast(
        tree:
            tuple
        ) -> _abc.Iterator[
            Token]:
    for token in _tokenize_ast_recurse(tree):
        if token.ast_node_index is not None:
            yield token
            continue
        if hasattr(tree, 'node_index'):
            node_index = tree.node_index
        else:
            node_index = None
        token = Token(
            symbol=token.symbol,
            value=token.value,
            start_line=token.start_line,
            start_column=token.start_column,
            end_line=token.end_line,
            end_column=token.end_column,
            filename=token.filename,
            ast_node_index=node_index)
        yield token


def _tokenize_ast_recurse(
        tree:
            tuple
        ) -> _abc.Iterator[
            Token]:
    """Yield tokens for `tree`."""
    match tree:
        case '_':
            yield Token('UNDERSCORE', '_')
            return
        case str() | bool() | None:
            raise AssertionError(tree)
        case list():
            raise AssertionError(tree)
    match enum_to_class(tree.symbol.name):
        case 'Axiom':
            yield _make_token('AXIOM')
            if tree.name:
                yield _make_name_token(tree.name)
                yield Token('DOUBLE_EQ', '==')
            yield from _tokenize_ast(
                tree.expression)
        case 'BooleanLiteral':
            yield _make_token(tree.value)
        case 'By':
            yield _make_token('BY')
            if tree.only:
                yield _make_token('ONLY')
            yield from _tokenize_comma_list(
                tree.facts)
            if tree.names:
                yield _make_token('DEF')
            yield from _tokenize_names(tree.names)
        case 'Cases':
            # for converting to an `ELIF` form
            # at the token level, map:
            # - `CASE` to `IF`,
            # - `->` to `THEN`,
            # - the pair `[]` `OTHER` to `ELSE`
            # - `[]` to `ELIF`
            yield _make_token('CASE')
            gen = _itr.chain.from_iterable(
                _tokenize_ast(case)
                for case in tree.cases)
            yield from gen
            yield _make_token('OTHER')
            yield from _tokenize_ast(tree.other)
        case 'CaseItem':
            yield from _tokenize_ast(tree.predicate)
            yield _make_token('RARROW', '->')
            yield from _tokenize_ast(tree.expression)
            yield _make_token('LBRACKET_RBRACKET', '[]')
        case 'Choose':
            yield _make_token('CHOOSE')
            _tokenize_ast(tree.declaration)
            yield Token('COLON', ':')
            yield from _tokenize_ast(
                tree.predicate)
        case 'Constants':
            yield _make_token('CONSTANT')
            yield from _tokenize_names(tree.names)
        case 'Define':
            yield _make_token('DEFINE')
            _tokenize_list(tree.definitions)
        case 'Except':
            yield Token(_LBRACKET, '[')
            yield from _tokenize_ast(tree.function)
            yield _make_token('EXCEPT')
            yield from _tokenize_comma_list(
                tree.changes)
            yield Token(_RBRACKET, ']')
        case 'Fairness':
            yield Token('WF', 'WF_')
            yield from _tokenize_ast(teee.subscript)
            yield Token(_LPAREN, '(')
            yield from _tokenize_ast(tree.action)
            yield Token(_RPAREN, ')')
        case 'Field':
            yield from _tokenize_ast(tree.expression)
            yield Token('DOT', '.')
            yield Token('NAME', tree.name)
        case 'FloatNumeral':
            yield Token('FLOAT', tree.value)
        case 'Function':
            yield Token(_LBRACKET, '[')
            yield from _tokenize_comma_list(
                tree.declaration)
            yield Token('MAPSTO', '|->')
            yield from _tokenize_ast(tree.value)
            yield Token(_RBRACKET, ']')
        case 'FunctionApplication':
            yield from _tokenize_ast(tree.function)
            yield Token(_LBRACKET, '[')
            yield from _tokenize_list(tree.arguments)
            yield Token(_RBRACKET, ']')
        case 'FunctionChange':
            yield Token('EXCLAMATION', '!')
            yield from _tokenize_ast(tree.item)
            yield Token('EQ', '=')
            yield from _tokenize_ast(tree.expression)
        case 'Have':
            yield _make_token('HAVE')
            yield from _tokenize_ast(
                tree.expression)
        case 'Hide':
            yield _make_token('HIDE')
            yield from _tokenize_comma_list(
                tree.facts)
            if tree.names:
                yield _make_token('DEF')
            yield from _tokenize_names(tree.names)
        case 'If':
            yield _make_token('IF')
            yield from _tokenize_ast(tree.predicate)
            yield _make_token('THEN')
            yield from _tokenize_ast(tree.then)
            yield _make_token('ELSE')
            yield from _tokenize_ast(tree.else_)
        case 'Instance':
            yield _make_token('INSTANCE')
            yield _make_name_token(tree.name)
            if tree.with_substitution is None:
                return
            yield _make_token('WITH')
            yield from _tokenize_list(
                tree.with_substitution)
        case 'VerticalList':
            for vertical_item in tree.arguments:
                yield from _tokenize_ast(
                    vertical_item)
        case 'VerticalItem':
            match tree.operator:
                case '/\\':
                    yield Token('AND', '/\\')
                case r'\/':
                    yield Token('OR', r'\/')
                case '|':
                    yield Token('PIPE', '|')
                case _:
                    raise ValueError(
                        tree.operator)
            yield from _tokenize_ast(
                tree.expression)
        case 'KeyBound':
            yield _make_name_token(tree.name)
            yield Token('COLON', ':')
            yield from _tokenize_ast(tree.bound)
        case 'Lambda':
            yield _make_token('LAMBDA')
            yield from _tokenize_comma_list(
                tree.parameters)
            yield Token('COLON', ':')
            yield from _tokenize_ast(
                tree.expression)
        case 'Let':
            yield _make_token('LET')
            yield from _tokenize_list(
                tree.definitions)
            yield _make_token('IN')
            yield from _tokenize_ast(
                tree.expression)
        case 'MapsTo':
            yield _make_name_token(tree.name)
            yield Token('MAPSTO', '|->')
            yield from _tokenize_ast(expression)
        case 'Module':
            yield Token(_DASH_LINE, _MIN_LINE_LEN * '-')
            yield Token('MODULE', 'MODULE')
            yield _make_name_token(tree.name)
            yield Token(_DASH_LINE, _MIN_LINE_LEN * '-')
            if tree.extendees:
                yield _make_token('EXTENDS')
            yield from _tokenize_comma_list(
                tree.extendees)
            for unit in tree.units:
                is_dash_line = (
                    isinstance(unit, str) and
                    unit.startswith('----'))
                if is_dash_line:
                    yield Token('DASH_LINE', unit)
                    continue
                yield from _tokenize_ast(unit)
            yield Token(_EQ_LINE, _MIN_LINE_LEN * '=')
        case 'ModuleName':
            yield Token('MODULE')
            yield _make_name_token(tree.name)
        case 'IntegralNumeral':
            # TODO: match prefix, and select
            # between decimal, binary, octal, hex
            yield Token('DECIMAL_INTEGER', tree.value)
        case 'Obvious':
            yield _make_token('OBVIOUS')
        case 'Omitted':
            yield _make_token('OMITTED')
        case 'OperatorApplication' if (
                tree.arguments is None):
            yield _make_name_token(tree.operator)
        case 'OperatorApplication':
            if isinstance(tree.operator, str):
                token_symbol = _lexemes_to_tokens.get(
                    tree.operator,
                    'NAME')
                token = Token(
                    symbol=token_symbol,
                    value=tree.operator)
                itr = tree.arguments
            else:
                itr = _tokenize_ast(tree.operator)
                token = next(itr)
            # TODO: between-operator `\X`
            if (token.value in
                    _TLA_OPERATOR_FIXITY['prefix'] or
                    token.value in
                        _TLA_OPERATOR_FIXITY['before']):
                # prefix
                arg, = tree.arguments
                yield token
                yield from _tokenize_ast(arg)
            # TODO: add all operators in this area
            elif (token.value in
                    _TLA_OPERATOR_FIXITY['infix'] or
                    token.value in
                        _TLA_OPERATOR_FIXITY['left'] or
                    token.value in
                        _TLA_OPERATOR_FIXITY['between']):
                # infix
                first, second = tree.arguments
                yield from _tokenize_ast(first)
                yield token
                yield from _tokenize_ast(second)
            elif (token.value in
                    _TLA_OPERATOR_FIXITY['postfix'] or
                    token.value in
                        _TLA_OPERATOR_FIXITY['after']):
                # postfix
                arg, = tree.arguments
                yield from _tokenize_ast(arg)
                yield token
            else:
                # nonfix
                yield token
                yield Token(_LPAREN, '(')
                yield from _tokenize_comma_list(itr)
                yield Token(_RPAREN, ')')
        case 'OperatorDeclaration':
            match tree.level:
                case None:
                    if not tree.new_keyword:
                        raise ValueError(tree)
                    level = None
                case (
                        'VARIABLE' |
                        'CONSTANT'|
                        'STATE' |
                        'ACTION' |
                        'TEMPORAL'):
                    level = tree.level
                case _:
                    raise ValueError(tree.level)
            if tree.new_keyword:
                yield _make_token('NEW')
            if level:
                yield _make_token(level)
            yield _make_name_token(tree.name)
            yield from _tokenize_arity(tree.arity)
            yield from _tokenize_bound(tree.bound)
        case 'OperatorDefinition':
            if tree.local:
                yield _make_token('LOCAL')
            yield _make_name_token(tree.name)
            if tree.arity is not None:
                yield Token(_LPAREN, '(')
                print(tree.arity)
                yield from _tokenize_comma_list(
                    tree.arity)
                yield Token(_RPAREN, ')')
            yield Token('DOUBLE_EQ', '==')
            yield from _tokenize_ast(tree.definiens)
        case 'OperatorName':
            raise NotImplementedError(
                'unused AST node type')
        case 'ParameterDeclaration':
            yield _make_name_token(tree.name)
            if tree.arity is None:
                return
            yield from _tokenize_ast(tree.arity)
        case 'Parentheses':
            yield Token(_LPAREN, '(')
            yield from _tokenize_ast(tree.expression)
            yield Token(_RPAREN, ')')
        case 'Pick':
            yield _make_token('PICK')
            yield from _tokenize_ast(tree.declarations)
            yield Token('COLON', ':')
            yield from _tokenize_ast(tree.predicate)
        case 'Proof':
            yield from _tokenize_list(tree.steps)
        case 'ProofCase':
            yield _make_token('CASE')
            yield from _tokenize_ast(tree.expression)
        case 'ProofStep':
            yield from _tokenize_ast(tree.name)
            yield from _tokenize_ast(tree.main)
            if tree.proof is None:
                return
            yield from _tokenize_ast(tree.proof)
        case 'Quantification':
            match tree.quantifier:
                case r'\A':
                    yield Token('BSLASH_A', r'\A')
                case r'\E':
                    yield Token('BSLASH_E', r'\E')
                case _:
                    raise ValueError(tree.quantifier)
            yield from _tokenize_comma_list(
                tree.declarations)
            yield Token('COLON', ':')
            yield from _tokenize_ast(tree.predicate)
        case 'QuantifierWitness':
            yield _make_token('WITNESS')
            yield from _tokenize_comma_list(
                tree.expressions)
        case 'Record':
            yield Token(_LBRACKET, '[')
            yield from _tokenize_ast(tree.key_values)
            yield Token(_RBRACKET, ']')
        case 'RecursiveOperators':
            yield _make_token('RECURSIVE')
            yield from _tokenize_names(tree.names)
        case 'Sequent':
            yield _make_token('ASSUME')
            yield from _tokenize_comma_list(
                tree.assume)
            yield _make_token('PROVE')
            yield from _tokenize_ast(tree.prove)
        case 'SetComprehension':
            yield Token(_LBRACE, '{')
            yield from _tokenize_ast(tree.item)
            yield Token('COLON', ':')
            yield from _tokenize_comma_list(
                tree.declarations)
            yield Token(_RBRACE, '}')
        case 'SetEnumeration':
            yield Token(_LBRACE, '{')
            yield from _tokenize_comma_list(tree.items)
            yield Token(_RBRACE, '}')
        case 'SetOfBoolean':
            yield _make_token('BOOLEAN')
        case 'SetOfFunctions':
            yield Token(_LBRACKET, '[')
            yield from _tokenize_ast(tree.domain)
            yield Token('RARROW', '->')
            yield from _tokenize_ast(tree.codomain)
            yield Token(_RBRACKET, ']')
        case 'SetOfRecords':
            yield Token(_LBRACKET, '[')
            yield from _tokenize_comma_list(
                tree.key_bounds)
            yield Token(_RBRACKET, ']')
        case 'SetOfStrings':
            yield _make_token('STRING')
        case 'SetSlice':
            yield Token(_LBRACE)
            for token in _tokenize_ast(tree.declaration):
                if token.symbol in {
                        'VARIABLE',
                        'CONSTANT', 'STATE', 'ACTION',
                        'TEMPORAL'}:
                    continue
                yield token
            yield Token('COLON', ':')
            yield from _tokenize_ast(tree.predicate)
            yield Token(_RBRACE)
        case 'StringLiteral':
            yield Token('STRING_LITERAL', tree.value)
        case 'SUBEXPRESSION_REFERENCE':
            for item in tree.items:
                yield from _tokenize_ast(item)
                yield Token('EXCLAMATION')
        case 'SubscriptedAction':
            match tree.operator:
                case '[':
                    opening = Token(_LBRACKET, '[')
                    closing = Token(
                        _RBRACKET_SUBSCRIPT, ']_')
                case '<<':
                    opening = Token(_LANGLE, '<<')
                    closing = Token(
                        _RANGLE_SUBSCRIPT, '>>_')
                case _:
                    raise ValueError(
                        tree.operator)
            yield opening
            yield from _tokenize_ast(tree.action)
            yield closing
            yield from _tokenize_ast(tree.subscript)
        case 'Suffices':
            yield _make_token('SUFFICES')
            yield from _tokenize_ast(tree.sequent)
        case 'Take':
            yield _make_token('TAKE')
            yield from _tokenize_comma_list(
                tree.declarations)
        case 'TemporalQuantification':
            match tree.quantifier:
                case '\\AA':
                    yield Token(
                        'SLASH_AA', '\\AA')
                case '\\EE':
                    yield Token(
                        'SLASH_EE', '\\EE')
                case _:
                    raise ValueError(
                        tree.quantifier)
            yield from _tokenize_names(
                tree.declarations)
            yield Token('COLON', ':')
            yield from _tokenize_ast(
                tree.predicate)
        case 'Theorem':
            yield _make_token('THEOREM')
            if tree.name:
                yield _make_name_token(tree.name)
                yield Token('DOUBLE_EQ', '==')
            yield from _tokenize_ast(tree.goal)
            if not tree.proof:
                return
            yield from _tokenize_ast(tree.proof)
        case 'Tuple':
            yield Token('DOUBLE_LANGLE', '<<')
            yield from _tokenize_comma_list(tree.items)
            yield Token('DOUBLE_RANGLE', '>>')
        case 'Use':
            yield _make_token('USE')
            if tree.only:
                yield _make_token('ONLY')
            yield from _tokenize_comma_list(tree.facts)
            if tree.names:
                yield _make_token('DEF')
            yield from _tokenize_names(tree.names)
        case 'Variables':
            yield _make_token('VARIABLE')
            yield from _tokenize_names(tree.names)
        case 'WithInstantiation':
            yield _make_name_token(tree.name)
            yield Token('LARROW', '<-')
            yield from _tokenize_ast(tree.expression)
        case _:
            raise ValueError(tree.symbol.name)


def _tokenize_bound(
        bound):
    if bound is None:
        return
    yield Token('BSLASH_IN', r'\in')
    yield from _tokenize_ast(bound)


def _tokenize_arity(
        arity):
    if arity is None:
        return
    if arity <= 0:
        raise ValueError(arity)
    yield Token(LPAREN, '(')
    yield from _tokenize_comma_list(
        '_' for _ in range(arity))
    yield Token(RPAREN, ')')


def _tokenize_list(
        container):
    if container is None:
        return
    for item in container:
        yield from _tokenize_ast(item)


def _tokenize_comma_list(
        iterable):
    if iterable is None:
        return
    first = True
    for item in iterable:
        if first:
            first = False
        else:
            yield Token('COMMA', ',')
        yield from _tokenize_ast(item)


def _tokenize_names(
        names):
    if names is None:
        return
    first = True
    for name in names:
        if first:
            first = False
        else:
            yield Token('COMMA', ',')
        match name:
            case str():
                yield _make_name_token(name)
            case _:
                yield from _tokenize_ast(name)


def _index_by_dfs(
        tree:
            tuple
        ) -> tuple:
    """Assign index attrbutes to nodes.

    The index value is the position of
    the node in a depth-first preorder
    traversal.

    If `tree` is an abstract syntax tree,
    then the indexing created by this
    function includes also nodes that
    are leaf attributes of namedtuples,
    strings, or lists.

    This is not an issue, because
    the indexing is unique, and this
    is the property that is used
    for mapping lexemes to AST nodes.
    """
    new_tree, _ = _index_by_dfs_recurse(
        tree,
        idx=0)
    return new_tree


def _index_by_dfs_recurse(
        tree,
        idx):
    node_index = idx
    idx += 1
    if isinstance(tree, tuple):
        successors = list()
        for succ in tree:
            new_succ, idx = _index_by_dfs_recurse(
                succ, idx)
            successors.append(new_succ)
        if hasattr(tree, 'node_index'):
            successors[-1] = node_index
            new_tree = type(tree)(*successors)
        else:
            new_tree = type(tree)(*successors)
    elif isinstance(tree, list):
        new_tree = list()
        for item in tree:
            new_item, idx = _index_by_dfs_recurse(
                item, idx)
            new_tree.append(new_item)
    else:
        new_tree = tree
    return new_tree, idx


def pprint_tree(
        tree):
    """Prettyprint syntax `tree`."""
    lines = pformat_tree(tree)
    print('\n'.join(lines))
    # _dump_tree_as_graph(tree)


def pformat_tree(
        tree):
    """Iterator of lines showing `tree`."""
    LINE = '\u2500' * 2
    BOTTOM_LEFT_CORNER = '\u2514'
    BRANCH = '\u251c'
    VERTICAL_LINE = '\u2502'
    END = f'{BOTTOM_LEFT_CORNER}{LINE}'
    SPACE = '\x20'
    if (isinstance(tree, tuple) and
            hasattr(tree, '_fields')):
        treed = tree._asdict()
    elif isinstance(tree, (list, tuple)):
        treed = {i: v for i, v in enumerate(tree)}
    else:
        yield f'{END} {tree}'
        return
    for i, u in enumerate(treed):
        prefix = (
            f'{BRANCH}{LINE}' if
                i < len(treed) - 1 else END)
        yield f'{prefix} {u}'
        if treed[u] is None:
            continue
        prefix = (VERTICAL_LINE if
            i < len(treed) - 1 else SPACE)
        for line in pformat_tree(treed[u]):
            yield f'{prefix}   {line}'
