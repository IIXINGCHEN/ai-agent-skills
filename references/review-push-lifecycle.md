# Review + Push Lifecycle

## Canonical Lifecycle

Use this exact lifecycle label everywhere:

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```

## Phase Map

| Phase | Skill | Purpose | Gate |
|---|---|---|---|
| init | `project-init` | Setup and readiness evidence. | Project source and setup commands verified. |
| PRD | `prd-authoring` | Requirements and acceptance criteria. | MVP scope and open questions clear. |
| plan | `implementation-planning` | Evidence-rich implementation plan. | Change surface and validation plan clear. |
| execute | `plan-execution` | Minimal implementation. | Tasks complete or divergence explained. |
| code review | `code-review-primary` | First code review. | Blockers fixed or accepted as blocked. |
| review fix loop | `review-fix-loop` | Fix confirmed review findings. | Fixes verified with targeted checks. |
| second review | `code-review-secondary` | Independent second pass. | Fixes verified, no new blockers. |
| multi-angle review | `multi-angle-review` | Spatial, vertical, reverse, security, data, error, test, and push-readiness lenses. | All applicable lenses pass or risks explicit. |
| commit readiness | `git-commit-readiness` | Atomic commit readiness and message. | Intended files only, no blockers. |
| push | `git-push-readiness` | Push readiness or explicitly requested push. | Remote/branch verified, no blockers. |
| complete | `completion-gate` | Final status. | Done, Done with accepted risks, or Blocked. |

## Push Policy

- Default to `readiness-only` mode.
- Execute push only when explicitly requested.
- Commit only when explicitly requested or required by workflow.
- Never use `--no-verify`.
- Never force push to `main`, `master`, or protected branches.
- Block push if verification or review blockers remain.

## Review Policy

- `code-review-primary` finds confirmed issues.
- `review-fix-loop` repairs confirmed issues only.
- `code-review-secondary` verifies fixes and residual risk.
- `multi-angle-review` checks independent lenses and final readiness.
- `completion-gate` cannot return Done while blockers remain.
