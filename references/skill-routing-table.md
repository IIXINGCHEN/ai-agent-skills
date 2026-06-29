# Skill Routing Table

Use this table to select exactly one primary skill unless the user asks for a lifecycle chain.

| User intent | Primary skill | Supporting skills | Do not use |
|---|---|---|---|
| Initialize or run a project locally | `project-init` | `repo-discovery` | `lifecycle-orchestrator` unless full lifecycle is requested |
| Create or refine requirements | `prd-authoring` | `project-init` when project context is needed | `plan-execution` |
| Create an implementation plan | `implementation-planning` | `repo-discovery`, `code-search-funnel` | `plan-execution` before plan approval when approval is required |
| Execute an approved plan | `plan-execution` | `verification-gate` | `git-push-readiness` |
| Review changed files | `code-review-primary` | `review-fix-loop` | `production-audit-repair` unless full production audit is requested |
| Fix review findings | `review-fix-loop` | `test-first-repair`, `verification-gate` | Fixing unconfirmed risks |
| Run independent second review | `code-review-secondary` | `verification-gate` | Repeating first review without new evidence |
| Run strict multidimensional review | `multi-angle-review` | Review lens skills | Single-lens review only |
| Full production audit and repair | `production-audit-repair` | `multi-angle-review`, review lenses | `code-review-primary` only |
| Security-only review | `security-review` | `code-search-funnel` | Full lifecycle unless requested |
| Real-data or mock-data hardening | `data-integrity-hardening` | `vertical-call-chain-review` | Inventing data sources |
| Push readiness | `git-push-readiness` | `git-commit-readiness`, `completion-gate` | `execute-push` unless explicitly requested |
| Final lifecycle decision | `completion-gate` | `execution-reporting` | Done without evidence |

Canonical lifecycle:

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```
