#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"ERROR: PyYAML is required: {exc}")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['# Skill:', '## Purpose', '## When to Use', '## Do Not Use When', '## Procedure', '## Output']
REQUIRED_CONTRACT_KEYS = ['name', 'description', 'preconditions', 'postconditions', 'verification']


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{path.relative_to(ROOT)} invalid JSON: {exc}')
        return None


def parse_frontmatter(text: str, errors: list[str]):
    match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not match:
        errors.append('missing YAML frontmatter')
        return None
    try:
        data = yaml.safe_load(match.group(1))
    except Exception as exc:
        errors.append(f'invalid YAML frontmatter: {exc}')
        return None
    if not isinstance(data, dict):
        errors.append('frontmatter must be a mapping')
        return None
    return data


def referenced_by_eval(skill: str) -> bool:
    for path in (ROOT / 'evals').glob('*.json'):
        try:
            cases = json.loads(path.read_text(encoding='utf-8'))
        except Exception:
            continue
        for case in cases:
            if not isinstance(case, dict):
                continue
            if case.get('expected_route') == skill:
                return True
            if skill in case.get('expected_skills', []):
                return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description='Verify one skill package directory')
    parser.add_argument('skill')
    args = parser.parse_args()
    skill = args.skill
    skill_dir = ROOT / 'agent-skills' / skill
    skill_file = skill_dir / 'SKILL.md'
    errors: list[str] = []

    manifest = load_json(ROOT / 'manifest.json', errors)
    manifest_skills = set(manifest.get('skills', [])) if isinstance(manifest, dict) else set()
    if skill not in manifest_skills:
        errors.append(f'{skill} is not listed in manifest.skills')

    if not skill_dir.exists():
        errors.append(f'missing {skill_dir.relative_to(ROOT)}')
    if not skill_file.exists():
        errors.append(f'missing {skill_file.relative_to(ROOT)}')
    else:
        text = skill_file.read_text(encoding='utf-8')
        frontmatter = parse_frontmatter(text, errors)
        if frontmatter:
            if frontmatter.get('name') != skill:
                errors.append(f'frontmatter name must be {skill!r}')
            if not frontmatter.get('description'):
                errors.append('frontmatter missing description')
            metadata = frontmatter.get('metadata')
            if not isinstance(metadata, dict):
                errors.append('frontmatter metadata must be a mapping')
            elif not metadata.get('compatibility'):
                errors.append('frontmatter metadata.compatibility must be non-empty')
        for marker in REQUIRED:
            if marker not in text:
                errors.append(f'missing {marker}')

    verify_path = skill_dir / 'verify.sh'
    if not verify_path.exists():
        errors.append('missing verify.sh')
    elif f"verify-skill.py '{skill}'" not in verify_path.read_text(encoding='utf-8'):
        errors.append('verify.sh must call verify-skill.py for this skill')

    contract_path = skill_dir / 'contract.json'
    contract = None
    if not contract_path.exists():
        errors.append('missing contract.json')
    else:
        contract = load_json(contract_path, errors)
        if isinstance(contract, dict):
            for key in REQUIRED_CONTRACT_KEYS:
                if key not in contract:
                    errors.append(f'contract.json missing {key}')
            if contract.get('name') != skill:
                errors.append('contract.name must match skill')
            for key in ['preconditions', 'postconditions', 'verification']:
                if not isinstance(contract.get(key), list) or not contract.get(key):
                    errors.append(f'contract.{key} must be a non-empty list')
            for command in contract.get('verification', []) if isinstance(contract.get('verification'), list) else []:
                if isinstance(command, str) and command.startswith('agent-skills/') and not (ROOT / command).exists():
                    errors.append(f'contract verification path missing: {command}')

    manifest_contracts = manifest.get('skill_contracts', {}) if isinstance(manifest, dict) else {}
    entry = manifest_contracts.get(skill) if isinstance(manifest_contracts, dict) else None
    if not isinstance(entry, dict):
        errors.append(f'manifest.skill_contracts missing {skill}')
    else:
        if entry.get('contract') != f'agent-skills/{skill}/contract.json':
            errors.append('manifest skill contract path mismatch')
        if entry.get('verify') != f'agent-skills/{skill}/verify.sh':
            errors.append('manifest skill verify path mismatch')

    if not referenced_by_eval(skill):
        errors.append(f'{skill} is not covered by any eval expected_route or expected_skills')

    if errors:
        for error in errors:
            print('ERROR:', error)
        return 1
    print(f'Skill verification passed: {skill}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
