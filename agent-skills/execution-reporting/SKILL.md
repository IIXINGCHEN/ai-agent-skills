---
name: execution-reporting
description: Generate concise evidence-based implementation, blocked, or decision reports after execution and verification.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: execution-reporting

## Purpose

Generate a concise evidence-based implementation report after code changes or a blocked execution.

This skill fuses the useful parts of uploaded `validation/execution-report.md` and `validation/system-review.md` while avoiding unnecessary standalone documents unless requested.

## When to Use

Use after multi-step implementation, plan execution, production hardening, or when verification is blocked.

## Do Not Use When

Do not create a separate report file unless the user explicitly asks or the project contract requires it.

## Inputs

- User request
- Plan, if any
- Changes made
- Validation outputs
- Known divergences, skipped items, and blockers

## Procedure

1. Summarize intended scope.
2. Summarize actual changes.
3. List validation commands and results.
4. Identify divergences from plan and classify them as justified or problematic.
5. List skipped items and reasons.
6. Identify remaining risks and minimal next steps.
7. If repeated process issues were found, recommend updates to skills, plans, or commands.

## Checklist

- [ ] Actual changes are listed.
- [ ] Validation evidence is included.
- [ ] Divergences are classified.
- [ ] Skipped work is not hidden.
- [ ] Blockers are explicit.
- [ ] No unverified completion claim is made.

## Output

Use `implementation_result`, `blocked`, or `decision_report` from `references/output-templates.md`.
