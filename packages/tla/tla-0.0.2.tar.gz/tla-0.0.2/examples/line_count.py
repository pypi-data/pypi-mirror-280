"""Count nonempty, comment, blank lines in a TLA+ file."""
import argparse as _arg

import tla


_COMMENT_TOKENS = {
    'UNILINE_COMMENT',
    'MULTILINE_COMMENT'}


def count_lines(
        text:
            str
        ) -> dict[
            str, int]:
    """Return count of nonempty, comment, blank lines."""
    lexer = tla.Lexer()
    tokens = list(lexer.parse(text))
    comment_rows = set()
    nonempty_rows = set()
    other_rows = set()
    for token in tokens:
        start_row = token.row
        nonempty_rows.add(start_row)
        if token.symbol not in _COMMENT_TOKENS:
            other_rows.add(start_row)
            continue
        if token.symbol == 'UNILINE_COMMENT':
            comment_rows.add(start_row)
        if token.symbol != 'MULTILINE_COMMENT':
            raise AssertionError(token)
        n_newlines = token.value.count('\n')
        for diff in range(n_newlines + 1):
            row = start_row + diff
            comment_rows.add(row)
            nonempty_rows.add(row)
    n_nonempty = len(nonempty_rows)
    only_comment = comment_rows - other_rows
    n_comments = len(only_comment)
    n_lines = text.count('\n')
    if not text.endswith('\n'):
        n_lines += 1
    n_blank = n_lines - n_nonempty
    n_other = n_nonempty - len(only_comment)
    return dict(
        n_lines=n_lines,
        n_comments=n_comments,
        n_blank=n_blank,
        n_other=n_other)


def _main():
    """Entry point."""
    args = _parse_args()
    filename = args.filename
    with open(filename, 'r') as fd:
        text = fd.read()
    line_stats = count_lines(text)
    lines = '\n'.join(
        f'{k} = {v}'
        for k, v in line_stats.items())
    print(lines)


def _parse_args(
        ) -> _arg.Namespace:
    """Return program arguments."""
    parser = _arg.ArgumentParser(
        description='Line statistics for TLA+ files.')
    parser.add_argument(
        'filename',
        type=str,
        help='A TLA+ file.')
    return parser.parse_args()


if __name__ == '__main__':
    _main()
