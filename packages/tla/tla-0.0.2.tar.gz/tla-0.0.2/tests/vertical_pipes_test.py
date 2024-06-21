"""Tests for vertical expressions with `|`."""
import tla._ast as _ast
import tla._lre as _lr


source = r'''
---- MODULE example ----

A == | B
     | C

========================
'''


def test_vertical_pipes():
    parser = _lr.Parser()
    tree = parser.parse(source)
    _ast.pprint_tree(tree)


if __name__ == '__main__':
    test_vertical_pipes()
