# Invocation Templates

## Production Multidimensional Audit and Repair

```md
Use skill:
production-audit-repair

Task:
Perform a production-grade multidimensional audit and repair of this project.

Constraints:
- Remove mock, fake, demo, random, placeholder, and guessed data.
- Use only real APIs, logs, system metrics, database records, configured services, or user-provided files.
- Do not generate summary documents unless explicitly requested.
- Modify only necessary code.
```

## Audit Only

```md
Use skills:
- repo-discovery
- code-search-funnel
- spatial-review
- vertical-call-chain-review
- reverse-trace-review
- data-integrity-hardening
- error-handling-hardening
- security-review

Task:
Audit the project and list confirmed issues only. Do not modify files.
```

## Focused Bug Fix

```md
Use skills:
- repo-discovery
- code-search-funnel
- test-first-repair
- verification-gate
- destructive-safety-gate

Bug:
[observed behavior]

Expected:
[expected behavior]
```

## Real Data Replacement

```md
Use skills:
- repo-discovery
- code-search-funnel
- data-integrity-hardening
- vertical-call-chain-review
- verification-gate

Task:
Replace fake metrics/data with real configured data sources only if a real source exists.

Stop condition:
If no real source of truth exists, return Blocked and specify the missing source.
```

## Plan Then Execute

```md
Use skills:
- repo-discovery
- code-search-funnel
- implementation-planning
- plan-execution
- verification-gate
- execution-reporting

Task:
Plan and implement [task]. Keep changes minimal and verify with actual commands.
```

## Strict Code Review Profile

```md
Use skills:
- repo-discovery
- code-search-funnel
- spatial-review
- vertical-call-chain-review
- reverse-trace-review
- data-integrity-hardening
- error-handling-hardening
- security-review
- verification-gate

Profile:
strict

Reference:
references/strict-review-profile.md
```

## Full Lifecycle: Init → PRD → Plan → Exec

```md
Use skill:
lifecycle-orchestrator

Lifecycle:
init → PRD → plan → execute → verify → report

Task:
[describe feature or project outcome]
```

## Init

```md
Use skill:
project-init

Task:
Analyze this project and produce safe setup, run, test, build, and validation steps.
```

## PRD

```md
Use skill:
prd-authoring

Task:
Create a PRD for [feature/product]. Separate facts, assumptions, and open questions.
```

## Complete Review-Push Lifecycle

```md
Use skill:
lifecycle-orchestrator

Lifecycle:
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete

Task:
[describe requested outcome]
```

## Review Chain Only

```md
Use skills:
- code-review-primary
- review-fix-loop
- code-review-secondary
- multi-angle-review
- verification-gate
- completion-gate

Task:
Review the implemented changes, fix confirmed issues, run a second review, then perform multi-angle review.
```

## Push After Reviews

```md
Use skills:
- verification-gate
- code-review-primary
- code-review-secondary
- multi-angle-review
- git-commit-readiness
- git-push-readiness
- completion-gate

Task:
Verify, review, prepare commit, push, and report final status.
```
