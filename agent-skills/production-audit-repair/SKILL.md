---
name: production-audit-repair
description: Perform evidence-based production-grade multidimensional audit and minimal repair for real project code.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: production-audit-repair

## Purpose

Perform evidence-based production-grade multidimensional audit and minimal repair for real project code. This is an orchestrator skill that coordinates focused subskills.

## When to Use

Use when the user asks for production-grade code audit and repair, multidimensional review, full project consistency check, mock/fake/demo/random/placeholder data removal, real data source verification, or cross-file API/config/data-flow/error-handling repair.

## Do Not Use When

Do not use for simple text edits, documentation-only tasks, isolated styling changes, speculative architecture redesign, tasks without accessible source code, or tasks where the user explicitly asks for audit only.

## Required Subskills

- `repo-discovery`
- `code-search-funnel`
- `implementation-planning` when planning is required
- `spatial-review`
- `vertical-call-chain-review`
- `reverse-trace-review`
- `data-integrity-hardening`
- `error-handling-hardening`
- `security-review`
- `test-first-repair`
- `verification-gate`
- `execution-reporting`
- `destructive-safety-gate`

## Inputs

- User task and constraints
- Accessible project source code
- Existing tests, build scripts, runtime scripts, configuration, logs, or data source definitions when available
- User-provided real data sources when the project does not define one

## Procedure

1. Run `repo-discovery`.
2. Identify build, test, runtime, config, and data-source entry points.
3. Use `code-search-funnel` to narrow the change surface.
4. Apply `spatial-review` for file-system, module, import, and path correctness.
5. Apply `vertical-call-chain-review` for frontend-backend-database/API flow completeness.
6. Apply `reverse-trace-review` from behavior, errors, logs, failed tests, and API responses.
7. Apply `data-integrity-hardening` to identify fake data and verify real sources of truth.
8. Apply `error-handling-hardening` and `security-review` to confirmed affected flows.
9. Repair confirmed issues only, using minimal root-cause changes.
10. Use `test-first-repair` for bugs, validation, data contracts, or risky behavior.
11. Run `verification-gate` before claiming completion.
12. Use `execution-reporting` after multi-step changes, blocked verification, or plan divergence.
13. Return `implementation_result` or `blocked` from `references/output-templates.md`.

## Evidence Required

Every confirmed issue must include file path, symbol/route/config key/command/data source, observed evidence, root cause, minimal fix, and verification method.

## Stop Conditions

Stop and return Blocked if no project source code is available, required real data source is absent, verification cannot be performed or replaced by a reliable smaller check, destructive operation lacks approval, scope is ambiguous, repair requires non-local architecture redesign, or repair requires a high-impact dependency without approval.

## Output

Use `implementation_result`, `audit_report`, `blocked`, or `decision_report` from `references/output-templates.md`.
