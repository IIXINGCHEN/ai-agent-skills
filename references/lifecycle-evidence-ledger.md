# Lifecycle Evidence Ledger

Use this ledger before `completion-gate`. Every required phase must have a status and evidence.

Canonical lifecycle:

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```

| Phase | Skill | Status | Evidence | Blockers | Accepted Risks |
|---|---|---|---|---|---|
| init | `project-init` | pending/pass/blocked/skipped |  |  |  |
| PRD | `prd-authoring` | pending/pass/blocked/skipped |  |  |  |
| plan | `implementation-planning` | pending/pass/blocked/skipped |  |  |  |
| execute | `plan-execution` | pending/pass/blocked/skipped |  |  |  |
| code review | `code-review-primary` | pending/pass/blocked/skipped |  |  |  |
| review fix loop | `review-fix-loop` | pending/pass/blocked/skipped |  |  |  |
| second review | `code-review-secondary` | pending/pass/blocked/skipped |  |  |  |
| multi-angle review | `multi-angle-review` | pending/pass/blocked/skipped |  |  |  |
| commit readiness | `git-commit-readiness` | pending/pass/blocked/skipped |  |  |  |
| push | `git-push-readiness` | pending/pass/blocked/skipped |  |  |  |
| complete | `completion-gate` | pending/pass/blocked |  |  |  |

Status rules:

- `pass`: completed with evidence.
- `blocked`: cannot proceed; include blocker and minimal next step.
- `skipped`: intentionally skipped with reason.
- `pending`: not yet executed.
