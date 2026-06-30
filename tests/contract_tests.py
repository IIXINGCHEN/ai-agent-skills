#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, check=True, text=True, capture_output=True)


def run_allow_fail(*args: str, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, input=input_text, capture_output=True)


def route(text: str) -> dict:
    result = run(sys.executable, 'scripts/route-validate.py', text)
    return json.loads(result.stdout)


def test_package_validation() -> None:
    run(sys.executable, 'scripts/validate-package.py')


def test_route_evals() -> None:
    run(sys.executable, 'scripts/route-validate.py', '--evals')


def test_route_review_do_not_push_is_not_push_readiness() -> None:
    result = route('Please review these files; do not push anything.')
    if result['route'] != 'code-review-primary' or 'git-push-readiness' in result.get('supporting_skills', []):
        raise AssertionError(result)


def test_route_completion_common_phrase() -> None:
    result = route('Complete the lifecycle with evidence')
    if result['route'] != 'completion-gate':
        raise AssertionError(result)


def test_lifecycle_state_machine_blocks_missing_evidence() -> None:
    ledger = json.loads((ROOT / 'references/lifecycle-evidence-ledger.template.json').read_text(encoding='utf-8'))
    ledger['phases'][0]['status'] = 'pass'
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(ledger, f)
        temp = f.name
    result = run_allow_fail(sys.executable, 'scripts/lifecycle-state-machine.py', temp)
    if result.returncode == 0:
        raise AssertionError('state machine accepted pass without evidence')


def test_lifecycle_blocks_completion_after_blocker() -> None:
    ledger = json.loads((ROOT / 'references/lifecycle-evidence-ledger.template.json').read_text(encoding='utf-8'))
    for phase in ledger['phases']:
        phase['status'] = 'skipped'
        phase['evidence'] = ['intentional skip']
    ledger['phases'][0]['status'] = 'blocked'
    ledger['phases'][0]['blockers'] = ['no source']
    ledger['phases'][-1]['status'] = 'pass'
    ledger['phases'][-1]['evidence'] = ['claimed complete after blocker']
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(ledger, f)
        temp = f.name
    result = run_allow_fail(sys.executable, 'scripts/lifecycle-state-machine.py', temp)
    if result.returncode == 0:
        raise AssertionError('state machine accepted complete pass after blocker')


def test_lifecycle_rejects_duplicate_phases() -> None:
    ledger = json.loads((ROOT / 'references/lifecycle-evidence-ledger.template.json').read_text(encoding='utf-8'))
    for phase in ledger['phases']:
        phase['status'] = 'skipped'
        phase['evidence'] = ['intentional skip']
    ledger['phases'].append({'phase': 'init', 'skill': 'project-init', 'status': 'pass', 'evidence': ['duplicate'], 'blockers': [], 'accepted_risks': []})
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(ledger, f)
        temp = f.name
    result = run_allow_fail(sys.executable, 'scripts/lifecycle-state-machine.py', temp)
    if result.returncode == 0:
        raise AssertionError('state machine accepted duplicate phases')


def test_output_guard_rejects_missing_issue_file() -> None:
    report = '''### Issue: bad
- Severity: high
- Category: config
- File: missing.py
- Symbol / route / config: x
- Evidence: concrete command output
- Root cause: y
- Minimal fix: z
- Verification: run test
- Risk: r
'''
    result = run_allow_fail(sys.executable, 'scripts/output-guard.py', input_text=report)
    if result.returncode == 0:
        raise AssertionError('output guard accepted nonexistent File field')


def test_verify_skill_rejects_invalid_frontmatter_yaml() -> None:
    skill = ROOT / 'agent-skills' / 'project-init' / 'SKILL.md'
    original = skill.read_text(encoding='utf-8')
    try:
        skill.write_text(original.replace(
            'description: Analyze a project and produce safe evidence-based initialization steps for dependencies, environment, startup, validation, and common commands.',
            'description: Broken: yaml: scalar',
            1,
        ), encoding='utf-8')
        result = run_allow_fail(sys.executable, 'scripts/verify-skill.py', 'project-init')
        if result.returncode == 0:
            raise AssertionError('verify-skill accepted invalid YAML frontmatter')
    finally:
        skill.write_text(original, encoding='utf-8')


def test_validate_package_rejects_empty_schema_enum() -> None:
    schema_path = ROOT / 'schemas' / 'confirmed-issue.schema.json'
    original = schema_path.read_text(encoding='utf-8')
    try:
        schema = json.loads(original)
        schema['properties']['severity']['enum'] = []
        schema_path.write_text(json.dumps(schema), encoding='utf-8')
        result = run_allow_fail(sys.executable, 'scripts/validate-package.py')
        if result.returncode == 0:
            raise AssertionError('validate-package accepted empty enum')
    finally:
        schema_path.write_text(original, encoding='utf-8')


def test_all_skill_verify_scripts() -> None:
    for verify in sorted((ROOT / 'agent-skills').glob('*/verify.sh')):
        run('bash', str(verify.relative_to(ROOT)))


def main() -> int:
    tests = [
        test_package_validation,
        test_route_evals,
        test_route_review_do_not_push_is_not_push_readiness,
        test_route_completion_common_phrase,
        test_lifecycle_state_machine_blocks_missing_evidence,
        test_lifecycle_blocks_completion_after_blocker,
        test_lifecycle_rejects_duplicate_phases,
        test_output_guard_rejects_missing_issue_file,
        test_verify_skill_rejects_invalid_frontmatter_yaml,
        test_validate_package_rejects_empty_schema_enum,
        test_all_skill_verify_scripts,
    ]
    for test in tests:
        test()
        print(f'PASS {test.__name__}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
