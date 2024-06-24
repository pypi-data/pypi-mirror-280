"""General API for rotate and combine tables (Danish: Roter og kombiner borde)."""

import argparse
import datetime as dti
import os
import pathlib
import sys
from typing import Generator, Iterable, Union, no_type_check

from roter import (
    APP_ALIAS,
    COMMA,
    ENCODING,
    TS_FORMAT,
    VERSION_INFO,
    log,
)

PathLike = Union[str, pathlib.Path]

ENCODING_ERRORS_POLICY = 'ignore'
NL = '\n'


def load_markdown_line_stream(resource: PathLike, encoding: str = ENCODING) -> Generator[str, None, None]:
    """Load the markdown resource to harvest from."""
    with open(resource, 'rt', encoding=encoding) as handle:
        return (line.strip() for line in handle.readlines())


def dump_markdown(lines: Iterable[str], resource: PathLike, encoding: str = ENCODING) -> None:
    """Dump the markdown lines into a file."""
    with open(resource, 'wt', encoding=encoding) as handle:
        handle.write(NL.join(lines))


def main(options: argparse.Namespace) -> int:
    """Visit the folder tree below root and yield the taxonomy."""
    log.info(f'Turning and combining tables')
    soft = {}
    for path in options.paths:
        log.info(f'parsing tables in {path}')
        if not path.is_file():
            log.warning(f'ignoring non-existing file ({path})')

        for slot, line in enumerate(load_markdown_line_stream(path), start=1):
            try:
                cells = line.strip('|').strip().split('|')
                key_text = cells[options.child_column_pos - 1].strip()
                parent_set_text = cells[options.parents_column_pos - 1].strip()
                key = key_text.strip()
                if options.child.lower() in key.lower() or '---' in key:
                    continue
                parent_set = sorted(set(entry.strip() for entry in parent_set_text.strip().split('<br>')))
                if key in soft:
                    log.debug(f'key {key} is a duplicate on line {slot} (with parents {parent_set})')
                soft[key] = parent_set
            except (IndexError, ValueError):
                pass

    parents = sorted(set(parent for k, v in soft.items() for parent in v))

    upstream = {}
    for parent in parents:
        upstream[parent] = []
        for downstream, upstreams in soft.items():
            if parent in upstreams:
                upstream[parent].append(downstream)
                upstream[parent].sort()

    with open(options.out_path, 'rt', encoding=ENCODING) as handle:
        lines = [line.strip() for line in handle.readlines()]

    inject_regions = {
        'combined': {
            'begin': -1,
            'end': -1,
        },
        'inverted': {
            'begin': -1,
            'end': -1,
        }
    }
    for slot, line in enumerate(lines):
        if line.startswith(options.markers_combined[0]):
            inject_regions['combined']['begin'] = slot
            log.debug(f'found line begin offset inject region for combined at line {slot + 1}')
        if line.startswith(options.markers_combined[1]):
            inject_regions['combined']['end'] = slot
            log.debug(f'found line end offset inject region for combined at line {slot + 1}')
        if line.startswith(options.markers_inverted[0]):
            inject_regions['inverted']['begin'] = slot
            log.debug(f'found line begin offset inject region for inverted at line {slot + 1}')
        if line.startswith(options.markers_inverted[1]):
            inject_regions['inverted']['end'] = slot
            log.debug(f'found line end offset inject region for inverted at line {slot + 1}')

    if inject_regions['combined']['begin'] == -1 or inject_regions['combined']['begin'] >= inject_regions['combined']['end']:
        log.error(f'combined region is invalid ({inject_regions['combined']})')
        return 1

    if inject_regions['inverted']['begin'] == -1 or inject_regions['inverted']['begin'] >= inject_regions['inverted']['end']:
        log.error(f'inverted region is invalid ({inject_regions['inverted']})')
        return 1

    out_lines_combined = [
        f'| {options.child}  | {options.parents} |',
        '|:-------|:--------------------|',
    ]
    for child in sorted(soft):
        parents = soft[child]
        out_lines_combined.append(f'| {child} | {" <br>".join(parents)} |')

    log.info('## Combined')
    for line in out_lines_combined:
        log.info(line)

    lines[inject_regions['combined']['begin']] += NL + NL.join(out_lines_combined)

    out_lines_inverted = [
        f'| {options.parent} | {options.children} |',
        '|:-------|:--------------------|',
    ]
    for parent, children in upstream.items():
        out_lines_inverted.append(f'| {parent} | {" <br>".join(children)} |')

    log.info('## Inverted')
    for line in out_lines_inverted:
        log.info(line)

    lines[inject_regions['inverted']['begin']] += NL + NL.join(out_lines_inverted)
    lines.append('')

    for slot in range(inject_regions['inverted']['begin'] + 1, inject_regions['inverted']['end']-3):
        del lines[slot]
    for slot in range(inject_regions['combined']['begin'] + 1, inject_regions['combined']['end']-2):
        del lines[slot]

    dump_markdown(lines, options.out_path)


    log.info('Done.')

    return 0
