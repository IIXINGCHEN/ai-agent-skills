---
name: verification-gate
description: Prevent unverified completion claims by running the smallest reliable tests, lint, type checks, builds, smoke checks, or fallbacks.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: verification-gate

## Purpose

Prevent unverified completion claims.

## When to Use

Use before claiming any code audit, repair, refactor, production hardening, or behavior change is complete.

## Do Not Use When

Do not skip because commands are unavailable. Instead, report unavailable commands and use the smallest reliable fallback check.

## Procedure

Run the smallest reliable checks available in order: targeted tests, related tests, lint, type check, build, runtime smoke check, logs or user-visible acceptance check.

## Checklist

- [ ] Targeted tests run or absence stated.
- [ ] Related tests run when risk requires.
- [ ] Lint run or absence stated.
- [ ] Type check run or absence stated.
- [ ] Build run or absence stated.
- [ ] Runtime smoke check run when practical.
- [ ] Logs or user-visible checks inspected when applicable.
- [ ] Failures reported without claiming completion.

## Rules

Do not claim completion without evidence. If a command is unavailable, state it. If verification is blocked, return Blocked. Do not repeatedly run the same failing command without changing the hypothesis.

## Output

Return commands executed, results, failures, remaining risks, and blocked next step when applicable.
