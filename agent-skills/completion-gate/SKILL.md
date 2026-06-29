---
name: completion-gate
description: Make the final Done, Done with accepted risks, or Blocked decision from lifecycle, verification, review, and push evidence.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: completion-gate

## Purpose

Make the final completion decision based on evidence, not optimism.

## When to Use

Use at the end of the lifecycle after implementation, verification, reviews, and optional push.

## Do Not Use When

Do not use to bypass missing verification, unresolved blockers, or unapproved destructive/push actions.

## Inputs

- `references/lifecycle-evidence-ledger.md` when available

- Lifecycle phase results
- Verification outputs
- Review outputs
- Push or PR result if applicable
- Remaining risks and accepted deferrals

## Procedure

1. Collect phase results using `references/lifecycle-evidence-ledger.md` when available for init, PRD, plan, execute, code review, secondary review, multi-angle review, push, and report.
2. Confirm required phases were completed or intentionally skipped with reason.
3. Confirm no blockers remain.
4. Confirm verification evidence exists.
5. Confirm push/PR status if requested.
6. Classify final state: Done, Done with accepted risks, or Blocked.
7. Provide concise final report with evidence and next step.

## Checklist

- [ ] Lifecycle evidence ledger checked.
- [ ] Required phases completed or skipped with reason.
- [ ] Verification evidence included.
- [ ] Primary review status included.
- [ ] Secondary review status included.
- [ ] Multi-angle review status included.
- [ ] Push/PR status included if requested.
- [ ] Remaining risks explicit.
- [ ] Final state is not overstated.

## Rules

- Do not say Done if verification failed or was not run without explanation.
- Do not say pushed if push did not succeed.
- Do not hide skipped phases.
- Do not add new offers after final completion unless user asks.

## Output

Use `completion_result` from `references/output-templates.md`.
