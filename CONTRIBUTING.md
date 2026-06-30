# Contributing

Thank you for helping improve AI Agent Skills.

This repository is a governed skill package for AI coding agents. Contributions should preserve safety, evidence, routing clarity, and reusable structure.

## Contribution Principles

- Keep `SKILL.md` files lean and action-oriented.
- Put long templates, policy details, and examples in `references/`.
- Add or update `evals/` when changing routing behavior or output contracts.
- Do not add mock, fake, guessed, or unverifiable evidence as if it were real.
- Do not weaken safety gates, destructive-operation rules, verification gates, or push readiness rules.
- Prefer small, focused changes.

## Required Checks

Before submitting changes, run:

```bash
python3 scripts/validate-package.py
```

This command verifies the package contract. At minimum, confirm:

- [ ] `manifest.json` is valid JSON.
- [ ] Every `evals/*.json` file is valid JSON.
- [ ] Deterministic routing evals pass with `python3 scripts/route-validate.py --evals`.
- [ ] Contract tests pass with `python3 tests/contract_tests.py`.
- [ ] Every skill directory has exactly one `SKILL.md`.
- [ ] Every `SKILL.md` has frontmatter with `name`, `description`, and `metadata`.
- [ ] Every `agent-skills/*` directory has `verify.sh` and `contract.json`.
- [ ] Every `SKILL.md` contains the required sections:
  - `# Skill:`
  - `## Purpose`
  - `## When to Use`
  - `## Do Not Use When`
  - `## Procedure`
  - `## Output`
- [ ] `manifest.skills` matches `agent-skills/*/SKILL.md`.
- [ ] `CLAUDE.md` and `AGENTS.md` list each skill once.
- [ ] The canonical lifecycle remains consistent:

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```

- [ ] Minimal lifecycle subset references are explicitly labeled as subsets, not as replacements for the canonical lifecycle.
- [ ] Confirmed issue output templates include `Severity`, `Category`, `File`, `Symbol / route / config`, `Evidence`, `Root cause`, `Minimal fix`, `Verification`, and `Risk`.

## Pull Request Expectations

A pull request should include:

- Summary of the change.
- Reason for the change.
- Files changed.
- Validation performed.
- Any accepted risks or blocked checks.

## Safety Requirements

Do not submit changes that:

- Encourage unverified completion claims.
- Encourage `git push --force` or `--no-verify`.
- Remove explicit push confirmation requirements.
- Remove destructive-operation confirmation gates.
- Invent APIs, data sources, logs, metrics, tests, or repository state.
