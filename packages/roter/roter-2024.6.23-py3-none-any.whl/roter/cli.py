"""CLI operations for rotate and combine tables (Danish: Roter og kombiner borde)."""

import argparse
import pathlib
import sys
from typing import Union

import roter.api as api
from roter import APP_ALIAS, APP_NAME, APP_VERSION, COMMA, KNOWN_FORMATS, KNOWN_KEY_FUNCTIONS, MARKERS, parse_csl


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

    markers_seq = parse_csl(options.markers)
    if len(markers_seq) != 4:
        parser.error('4 non-empty markers are required to inject two tables')

    options.markers_combined = (markers_seq[0], markers_seq[1])
    options.markers_inverted = (markers_seq[2], markers_seq[3])

    return options


def main(argv: Union[list[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return api.main(options)
