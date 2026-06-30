#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

CANONICAL_LIFECYCLE = "init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete"
CANONICAL_PHASES = [
    ('init', 'project-init'),
    ('PRD', 'prd-authoring'),
    ('plan', 'implementation-planning'),
    ('execute', 'plan-execution'),
    ('code review', 'code-review-primary'),
    ('review fix loop', 'review-fix-loop'),
    ('second review', 'code-review-secondary'),
    ('multi-angle review', 'multi-angle-review'),
    ('commit readiness', 'git-commit-readiness'),
    ('push', 'git-push-readiness'),
    ('complete', 'completion-gate'),
]
VALID_STATUSES = {'pending', 'pass', 'blocked', 'skipped'}
COMPLETE_OK_BEFORE_COMPLETE = {'pass', 'skipped'}


def _as_list(value):
    return value if isinstance(value, list) else []


def validate_ledger(path: Path) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        return [f'invalid JSON ledger: {exc}']

    errors: list[str] = []
    if data.get('canonical_lifecycle') != CANONICAL_LIFECYCLE:
        errors.append('canonical_lifecycle does not match expected lifecycle')

    phases = data.get('phases')
    if not isinstance(phases, list):
        return errors + ['phases must be a list']

    expected_order = [phase for phase, _ in CANONICAL_PHASES]
    actual_order = [p.get('phase') if isinstance(p, dict) else None for p in phases]

    counts = Counter(actual_order)
    duplicates = sorted(name for name, count in counts.items() if name is not None and count > 1)
    if duplicates:
        errors.append(f'duplicate phases: {duplicates}')

    if actual_order != expected_order:
        errors.append(f'phase order must match canonical lifecycle: {expected_order}')

    seen = {}
    for item in phases:
        if not isinstance(item, dict):
            errors.append('each phase entry must be an object')
            continue
        phase_name = item.get('phase')
        if phase_name not in seen:
            seen[phase_name] = item

    blocked_before_complete: list[str] = []
    pending_before_complete: list[str] = []

    for phase, skill in CANONICAL_PHASES:
        item = seen.get(phase)
        if item is None:
            errors.append(f'missing phase {phase}')
            pending_before_complete.append(phase)
            continue

        if item.get('skill') != skill:
            errors.append(f'{phase} must use skill {skill}')

        status = item.get('status')
        evidence = _as_list(item.get('evidence'))
        blockers = _as_list(item.get('blockers'))
        accepted_risks = _as_list(item.get('accepted_risks'))

        if status not in VALID_STATUSES:
            errors.append(f'{phase} invalid status {status!r}')
            continue

        if status == 'pass' and not evidence:
            errors.append(f'{phase} pass requires at least one evidence item')
        if status == 'blocked':
            if not blockers:
                errors.append(f'{phase} blocked requires blocker text')
            if phase != 'complete':
                blocked_before_complete.append(phase)
        if status == 'skipped' and phase not in {'commit readiness', 'push'} and not (evidence or accepted_risks):
            errors.append(f'{phase} skipped requires evidence or accepted risk')
        if status == 'pending' and phase != 'complete':
            pending_before_complete.append(phase)

    complete = seen.get('complete')
    if complete:
        complete_status = complete.get('status')
        if complete_status == 'pass':
            if blocked_before_complete:
                errors.append(f'complete cannot pass while earlier phases are blocked: {blocked_before_complete}')
            if pending_before_complete:
                errors.append(f'complete cannot pass while earlier phases are pending or missing: {pending_before_complete}')
            incomplete = [
                p for p, _ in CANONICAL_PHASES[:-1]
                if seen.get(p, {}).get('status') not in COMPLETE_OK_BEFORE_COMPLETE
            ]
            if incomplete:
                errors.append(f'complete pass requires previous phases pass/skipped, got incomplete: {incomplete}')

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate structured lifecycle ledger state transitions')
    parser.add_argument('ledger')
    args = parser.parse_args()
    errors = validate_ledger(Path(args.ledger))
    if errors:
        for error in errors:
            print('ERROR:', error)
        return 1
    print('Lifecycle ledger validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
