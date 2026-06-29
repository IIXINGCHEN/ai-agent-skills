# Commands Fusion Map

This file maps useful ideas from the uploaded Claude Commands package into the Skills package.

## Source Command → Target Skill

| Source command | Fused target | Notes |
|---|---|---|
| `workflow/plan.md` | `implementation-planning` | Feature understanding, codebase intelligence, plan structure, validation checklist. |
| `workflow/execute.md` | `plan-execution` | Execute plan in order, verify as you go, final report. |
| `workflow/prime.md` | `repo-discovery` | Project overview, architecture, tech stack, key files. |
| `validation/code-review-pro.md` | `production-audit-repair`, `spatial-review`, `vertical-call-chain-review`, `data-integrity-hardening`, `security-review` | Strict profile, spatial/system/reverse analysis, no mock data policy. |
| `validation/code-review.md` | `code-search-funnel`, `security-review`, `error-handling-hardening` | Verify issues are real; prioritize correctness and security. |
| `validation/validate.md` | `verification-gate` | Detect validation commands and run syntax/lint/type/test/build checks. |
| `validation/execution-report.md` | `execution-reporting` | Completed tasks, tests added, validation results, divergences. |
| `validation/system-review.md` | `execution-reporting` | Process divergence classification and improvement loop. |
| `bugfix/rca.md` | `reverse-trace-review`, `test-first-repair` | Reproduction, root cause, impact, fix strategy, testing requirements. |
| `bugfix/implement.md` | `plan-execution`, `test-first-repair`, `verification-gate` | Verify current state, implement fix, add tests, validate. |
| `project/analyze.md` | `repo-discovery`, `spatial-review` | Directory, technology, architecture, dependency analysis. |
| `utils/analyze-codebase.md` | `code-search-funnel`, `implementation-planning` | Architecture summary, pattern guide, dependency graph. |

## Fusion Rules

- Preserve command package strengths as reusable skill procedures.
- Do not import command-only assumptions such as GitHub availability unless verified.
- Do not force file output when a concise chat report is enough.
- Keep Claude command syntax as invocation examples only, not as a required runtime.
- Skills remain cross-platform for Claude Code, Codex, and generic coding agents.

## Lifecycle Additions

| Source command | Fused target | Notes |
|---|---|---|
| `project/init.md` | `project-init` | Setup, dependencies, environment, start commands, common commands, validation. |
| `docs/create-prd.md` | `prd-authoring` | PRD structure, MVP scope, user stories, success criteria, risks, phases. |
| lifecycle synthesis | `lifecycle-orchestrator` | init → PRD → plan → execute → verify → report routing. |

## Review + Push Additions

| Source command | Fused target | Notes |
|---|---|---|
| `validation/code-review.md` | `code-review-primary` | Changed-file technical review with real-issue verification. |
| `validation/code-review-pro.md` | `code-review-primary`, `multi-angle-review` | Strict profile, production readiness, no mock policy. |
| `validation/code-review-fix.md` | `review-fix-loop` | Fix review findings one by one with tests. |
| lifecycle synthesis | `code-review-secondary` | Independent second pass after fixes. |
| lifecycle synthesis | `multi-angle-review` | Spatial, vertical, reverse, security, data, error, test, push lenses. |
| `git/commit.md` | `git-commit-readiness` | Atomic commit readiness and conventional message. |
| `git/push.md` | `git-push-readiness` | Remote/branch/push safety checks. |
| `git/pr.md` | `git-push-readiness` | Optional PR readiness when GitHub CLI exists. |
| lifecycle synthesis | `completion-gate` | Final Done/Blocked decision. |
