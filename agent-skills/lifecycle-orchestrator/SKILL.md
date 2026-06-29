---
name: lifecycle-orchestrator
description: Orchestrate the canonical lifecycle: init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: lifecycle-orchestrator

## Purpose

Coordinate the full reusable delivery lifecycle:

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```

Use the lightest reliable subset. Do not force every phase when the task does not need it. Use `references/skill-routing-table.md` when selecting the primary skill.

## When to Use

Use when the user asks for full workflow support, mentions init/PRD/plan/execute, requests end-to-end implementation, or wants a repeatable agent delivery process.

## Do Not Use When

Do not use for a small local fix that only needs `bug_fix` style execution, for audit-only tasks, or when the user explicitly asks to skip a lifecycle phase.

## Required Subskills

- `project-init`
- `prd-authoring`
- `implementation-planning`
- `plan-execution`
- `verification-gate`
- `code-review-primary`
- `review-fix-loop`
- `code-review-secondary`
- `multi-angle-review`
- `git-commit-readiness`
- `git-push-readiness`
- `completion-gate`
- `execution-reporting`
- `destructive-safety-gate`

Optional supporting skills:

- `repo-discovery`
- `code-search-funnel`
- `production-audit-repair`
- review and hardening skills as needed

## Procedure

1. Decide the smallest lifecycle subset needed.
2. Init: use `project-init` when setup/readiness is unknown.
3. PRD: use `prd-authoring` when product requirements or MVP scope are unclear.
4. Plan: use `implementation-planning` when implementation has multiple steps, files, risks, or verification phases.
5. Execute: use `plan-execution` to implement the approved or required plan.
6. Verify: use `verification-gate` before review and completion claims.
7. Review: use `code-review-primary` after implementation.
8. Fix review findings with `review-fix-loop` when confirmed issues exist.
9. Second review: use `code-review-secondary` to verify fixes and residual risk.
10. Multi-angle review: use `multi-angle-review` for spatial, vertical, reverse, security, data, error, test, and push-readiness lenses.
11. Push: use `git-commit-readiness` and `git-push-readiness` only when push is explicitly requested.
12. Complete: use `completion-gate` and `execution-reporting` for final evidence, divergences, skipped items, and next steps.

## Phase Selection Rules

- If there is no accessible project source, stop at Init with Blocked.
- If requirements are unclear, stop at PRD questions before planning.
- If plan assumptions fail during execution, pause and update the plan or return a decision report.
- If verification fails, do not report Done.
- If destructive action is required, invoke `destructive-safety-gate`.
- Track phase evidence with `references/lifecycle-evidence-ledger.md` before completion.

## Checklist

- [ ] Lifecycle subset chosen and justified.
- [ ] Init evidence exists or was explicitly skipped.
- [ ] PRD exists or requirements are already clear.
- [ ] Plan exists when task complexity requires it.
- [ ] Execution follows plan or explains divergence.
- [ ] Verification evidence is included.
- [ ] Primary review completed or skipped with reason.
- [ ] Secondary review completed or skipped with reason.
- [ ] Multi-angle review completed or skipped with reason.
- [ ] Push phase defaults to readiness-only unless the user explicitly requested push.
- [ ] Push completed only when explicitly requested.
- [ ] Final report avoids unverified claims.

## Output

Use `lifecycle_result` from `references/output-templates.md`, or the output template of the terminal phase when the lifecycle stops early.
