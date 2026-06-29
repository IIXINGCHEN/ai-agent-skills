---
name: review-fix-loop
description: Fix confirmed code review issues one by one with minimal changes, targeted tests, and validation after each fix batch.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: review-fix-loop

## Purpose

Repair confirmed code review findings one by one while preserving minimal-change discipline and verification evidence.

## When to Use

Use after `code-review-primary`, `code-review-secondary`, or `multi-angle-review` finds confirmed issues that the user wants fixed.

## Do Not Use When

Do not use for unconfirmed risks, style-only preferences, large architecture changes without approval, or issues requiring destructive operations without the safety gate.

## Inputs

- Review report or list of findings
- Current repository state
- Scope constraints
- Test and validation commands

## Procedure

1. Read the full review report before fixing.
2. Sort issues by severity: blocker, major, minor.
3. For each issue, explain root cause and minimal fix target.
4. Apply the smallest safe code change.
5. Add or update targeted tests when project patterns support it.
6. Run relevant checks after the fix or fix batch.
7. Re-run review on the changed diff when blockers or major issues were fixed.
8. Stop and return decision report if a fix requires scope expansion, new dependency, or architecture change.

## Checklist

- [ ] Review findings were read completely.
- [ ] Fix order follows severity.
- [ ] Each fix maps to a confirmed issue.
- [ ] Targeted tests run or absence stated.
- [ ] No unrelated refactor included.
- [ ] Review is rerun after significant fixes.

## Rules

- Do not fix unconfirmed risks as if they were bugs.
- Do not hide errors with silent fallbacks.
- Do not delete tests to pass validation.
- Do not proceed to push while blockers remain.

## Output

Use `review_fix_result` from `references/output-templates.md`.
