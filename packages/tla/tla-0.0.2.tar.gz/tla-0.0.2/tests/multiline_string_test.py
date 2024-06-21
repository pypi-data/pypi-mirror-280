import tla._ast
import tla._lre as _lr


source = r'''
---- MODULE example ----
A == """
    This is a multiline string
    in TLA+
    """
========================
'''


def test_multiline_strings():
    parser = _lr.Parser()
    tree = parser.parse(source)
    print(tree)
    out = tla._ast.pprint_tree(tree)
    print(out)


if __name__ == '__main__':
    test_multiline_strings()
