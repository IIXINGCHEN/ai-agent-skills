---
name: test-first-repair
description: Drive bug fixes, validation changes, data contracts, and risky refactors through focused reproduction and verification.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: test-first-repair

## Purpose

Drive bug fixes, validation changes, data contract changes, and risky refactors through focused verification.

## When to Use

Use when fixing bugs, adding validation, changing API/data contracts, changing error behavior, or refactoring risky code.

## Do Not Use When

Do not create unrelated broad tests or test-only scaffolding not traceable to the task.

## Procedure

1. For a bug fix, reproduce the bug when practical.
2. For validation, test invalid input when practical.
3. For refactor, run existing tests before and after when practical.
4. Add or update the smallest focused test that protects changed behavior when the project has a test pattern.
5. If tests are absent or impractical, document why and use a smaller reliable verification.

## Checklist

- [ ] Existing test command identified or absence stated.
- [ ] Similar tests found when available.
- [ ] Failing reproduction created or impracticality stated.
- [ ] Minimal implementation changed.
- [ ] Targeted test passes.
- [ ] Related tests pass when available.

## Rules

Do not add test frameworks unless explicitly approved. Do not write tests that assert implementation details unless that is the project pattern. Do not delete existing tests to make verification pass.

## Output

Return reproduction path, test added or reason not added, verification result, and remaining risk.
