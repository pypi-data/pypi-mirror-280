"""CLI operations for rotate and combine tables (Danish: Roter og kombiner borde)."""

import argparse
import pathlib
import sys
from typing import Union

import roter.api as api
from roter import (
    APP_ALIAS,
    APP_NAME,
    APP_VERSION,
    CHILD_ATTRIBUTES,
    COMMA,
    MARKERS,
    PARENT_ATTRIBUTES,
    parse_csl_preserve_case
)


def parse_request(argv: list[str]) -> Union[int, argparse.Namespace]:
    """DRY."""
    parser = argparse.ArgumentParser(
        prog=APP_ALIAS, description=APP_NAME, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--table-files',
        '-t',
        dest='table_files',
        default='',
        help='Markdown files with tables to parse. Optional\n(default: positional table files value)',
        required=False,
    )
    parser.add_argument(
        'table_files_pos', nargs='?', default='', help='markdown files with tables to parse. Optional'
    )
    parser.add_argument(
        '--excludes',
        '-x',
        dest='excludes',
        default='',
        help='comma separated list of values to exclude paths\ncontaining the substring (default: empty string)',
    )
    parser.add_argument(
        '--out-path',
        '-o',
        dest='out_path',
        default=sys.stdout,
        help='output file path (stem) to inject combined and inverted markdown tables in between markers',
    )
    parser.add_argument(
        '--markers',
        '-m',
        dest='markers',
        type=str,
        default=MARKERS,
        help=f'comma separated begin/end markers in output file path (default: MARKERS)',
    )
    parser.add_argument(
        '--child-attributes',
        '-c',
        dest='child_attributes',
        type=str,
        default=CHILD_ATTRIBUTES,
        help=f'heading position and labels (singular and plural) for children related columns (default:{CHILD_ATTRIBUTES})',
    )
    parser.add_argument(
        '--parent-attributes',
        '-p',
        dest='parent_attributes',
        type=str,
        default=PARENT_ATTRIBUTES,
        help=f'heading position and labels (singular and plural) for parents related columns (default: {PARENT_ATTRIBUTES})',
    )
    parser.add_argument(
        '--version',
        '-V',
        dest='version_request',
        default=False,
        action='store_true',
        help='show version of the app and exit',
        required=False,
    )

    if not argv:
        print(f'{APP_NAME} version {APP_VERSION}')
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if options.version_request:
        print(f'{APP_NAME} version {APP_VERSION}')
        return 0

    if not options.table_files:
        if options.table_files_pos:
            options.table_files = options.table_files_pos
        else:
            parser.error('missing any paths to parse tables from')

    options.excludes_parsed = parse_csl(options.excludes) if options and options.excludes else []

    path_cands = (p.strip() for p in options.table_files.split() if p.strip())
    options.paths = (pathlib.Path(p) for p in path_cands if not any(x in p for x in options.excludes_parsed ))
    if not options.paths:
        parser.error('missing non-excluded paths to parse tables from')

    if options.out_path is sys.stdout:
        parser.error('missing output template to inject combined and inverted tables into')

    if options.markers.count(COMMA) != 4 - 1:
        parser.error('4 markers separated by comma are required to inject two tables')

    markers_seq = parse_csl_preserve_case(options.markers)
    if len(markers_seq) != 4:
        parser.error('4 non-empty markers are required to inject two tables')

    options.markers_combined = (markers_seq[0], markers_seq[1])
    options.markers_inverted = (markers_seq[2], markers_seq[3])

    child_seq = parse_csl_preserve_case(options.child_attributes)
    if len(child_seq) != 3:
        parser.error('3 non-empty child attributes are required to process the tables')
    try:
        options.child_column_pos = int(child_seq[0])
    except:  # noqa
        parser.error('child column position as integer in [1, N] is required to process the tables')
    options.child, options.children = child_seq[1], child_seq[2]

    parent_seq = parse_csl_preserve_case(options.parent_attributes)
    if len(parent_seq) != 3:
        parser.error('3 non-empty parent attributes are required to process the tables')
    try:
        options.parents_column_pos = int(parent_seq[0])
    except:  # noqa
        parser.error('parent column position as integer in [1, N] is required to process the tables')
    options.parent, options.parents = parent_seq[1], parent_seq[2]

    return options


def main(argv: Union[list[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return api.main(options)
