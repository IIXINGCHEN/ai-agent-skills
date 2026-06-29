---
name: reverse-trace-review
description: Trace backward from observed behavior, errors, logs, failed tests, responses, or database state to root cause.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: reverse-trace-review

## Purpose

Trace backward from observed outcomes to root cause.

## When to Use

Use when starting from user-visible behavior, errors, logs, failed tests, API responses, database state, or monitoring output.

## Do Not Use When

Do not use when there is no observed outcome and the task is purely forward design.

## Procedure

Start from observed outcome, then trace error/failed assertion, logs/metrics/API response, handler, business logic, data source, and configuration.

## Checklist

- [ ] Observed result captured exactly.
- [ ] Error or failed assertion captured exactly.
- [ ] Logs or responses checked when available.
- [ ] Responsible handler identified.
- [ ] Business rule identified.
- [ ] Data source or missing source identified.
- [ ] Config impact checked.
- [ ] Fallback behavior checked.
- [ ] Security behavior fails closed when applicable.

## Output

Return root-cause trace, minimal repair target, remaining unknowns, and verification method.
