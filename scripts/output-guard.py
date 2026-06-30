#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH_PATTERN = re.compile(r'(?<![\w.-])(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+(?:\.[A-Za-z0-9_.-]+)?')
REQUIRED_ISSUE_FIELDS = [
    'Severity', 'Category', 'File', 'Symbol / route / config', 'Evidence',
    'Root cause', 'Minimal fix', 'Verification', 'Risk'
]
PLACEHOLDERS = {'', 'tbd', 'todo', '...', 'claimed', 'n/a?', 'unknown', 'none'}
FILE_NA = {'n/a', 'not applicable', 'none', '无', '-'}


def parse_issue_blocks(text: str) -> list[str]:
    parts = re.split(r'(?m)^### Issue:', text)
    return parts[1:] if len(parts) > 1 else []


def parse_fields(block: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r'^- ([^:]+):\s*(.*)$', line.strip())
        if match:
            fields[match.group(1).strip()] = match.group(2).strip()
    return fields


def is_placeholder(value: str) -> bool:
    return value.strip().lower() in PLACEHOLDERS or bool(re.fullmatch(r'[.\-_*\s]+', value.strip()))


def validate_issue_block(block: str) -> list[str]:
    errors: list[str] = []
    fields = parse_fields(block)
    for field in REQUIRED_ISSUE_FIELDS:
        if field not in fields:
            errors.append(f'Confirmed issue missing field: {field}')
        elif is_placeholder(fields[field]):
            errors.append(f'Confirmed issue field is placeholder/empty: {field}')

    file_value = fields.get('File', '').strip()
    if file_value and file_value.lower() not in FILE_NA and not is_placeholder(file_value):
        file_value = file_value.strip('`')
        if any(token in file_value for token in ['*', '<', '>', '[', ']']):
            errors.append(f'Issue File contains wildcard or template marker: {file_value}')
        elif not (ROOT / file_value).exists():
            errors.append(f'Issue File does not exist: {file_value}')

    evidence = fields.get('Evidence', '')
    if evidence and is_placeholder(evidence):
        errors.append('Issue Evidence is not concrete')
    return errors


def scan(text: str) -> list[str]:
    errors: list[str] = []
    for match in sorted(set(PATH_PATTERN.findall(text))):
        if match.startswith(('http/', 'https/')):
            continue
        candidate = ROOT / match.strip('`')
        if not candidate.exists() and not any(ch in match for ch in '*<>[]'):
            errors.append(f'Unverified path reference: {match}')

    for block in parse_issue_blocks(text):
        errors.extend(validate_issue_block(block))

    if re.search(r'\bDone\b|完成|已完成', text) and 'Verification' not in text and 'Validation passed' not in text:
        errors.append('Completion claim lacks explicit verification evidence')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description='Scan agent output for unverifiable claims and missing evidence fields')
    parser.add_argument('file', nargs='?')
    args = parser.parse_args()
    text = Path(args.file).read_text(encoding='utf-8') if args.file else sys.stdin.read()
    errors = scan(text)
    if errors:
        for error in errors:
            print('ERROR:', error)
        return 1
    print('Output guard passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
