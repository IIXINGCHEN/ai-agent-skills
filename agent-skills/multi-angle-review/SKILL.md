---
name: multi-angle-review
description: "Review code from multiple lenses: spatial, vertical, reverse, security, data integrity, error handling, tests, and push readiness."
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: multi-angle-review

## Purpose

Perform a structured multi-angle review that combines independent review lenses instead of a single generic code review.

## When to Use

Use when the user asks for multi-angle review, multi-angle review, multidimensional review, strict review, production readiness review, or final confidence review before push.

## Do Not Use When

Do not use for trivial single-line changes unless the user explicitly requests strict review.

## Inputs

- Current diff and changed files
- PRD and plan when available
- First/second review outputs when available
- Verification results
- Project configuration and deployment context

## Required Lenses

- Spatial review: file structure, imports, paths, config, architecture boundaries.
- Vertical call-chain review: UI/CLI → API → service → data/log/API → response → rendering.
- Reverse trace review: outcomes/errors/tests/logs back to root cause.
- Security review: auth, input, secrets, injection, path traversal, SSRF, unsafe deserialization.
- Data integrity review: source of truth, schema, serialization, fake data, migrations.
- Error handling review: API/file/db/network/config/input failures.
- Test and verification review: targeted tests, related tests, lint, type, build, smoke.
- Push readiness review: branch, status, remote, commit boundaries, protected branch risk.

## Procedure

1. Select only lenses relevant to the changed scope unless strict/full lifecycle requires all lenses.
2. For each selected lens, identify concrete evidence and confirmed issues.
3. Classify findings as blocker, major, minor, or follow-up.
4. Cross-check whether one lens contradicts another.
5. Convert blockers/major findings into a fix loop before push.
6. Confirm all required verification evidence exists or mark Blocked.

## Checklist

- [ ] Spatial lens completed or skipped with reason.
- [ ] Vertical lens completed or skipped with reason.
- [ ] Reverse lens completed or skipped with reason.
- [ ] Security lens completed or skipped with reason.
- [ ] Data integrity lens completed or skipped with reason.
- [ ] Error handling lens completed or skipped with reason.
- [ ] Test/verification lens completed or skipped with reason.
- [ ] Push readiness lens completed or skipped with reason.
- [ ] Blockers are fixed before push.

## Rules

- Do not turn every lens into generic advice.
- Each confirmed finding must include evidence.
- If a lens is not applicable, state why.
- If strict profile is active, production mock/stub/placeholder data is a blocker.

## Output

Use `multi_angle_review_result` from `references/output-templates.md`.
