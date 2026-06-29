---
name: error-handling-hardening
description: Audit and improve realistic failure handling for API, file, database, network, config, input, and user-visible error states.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: error-handling-hardening

## Purpose

Audit and improve realistic failure handling for production behavior.

## When to Use

Use when auditing API calls, file operations, database operations, network calls, runtime failures, configuration failures, or user-visible error states.

## Do Not Use When

Do not add broad defensive code for impossible states unsupported by actual execution paths.

## Procedure

Check API call failures, file operation failures, database connection/query failures, network timeout, invalid configuration, invalid input, partial failure, logging/observability, and user-visible error states.

## Checklist

- [ ] API, file, database, and network errors handled.
- [ ] Invalid configuration handled.
- [ ] Invalid input handled.
- [ ] Partial failure behavior defined.
- [ ] Logs preserve diagnostic context.
- [ ] Secrets are not leaked.
- [ ] User-visible error state exists where applicable.

## Rules

Do not swallow errors silently. Preserve diagnostic context. Do not leak secrets. Handle realistic failure modes only. Keep behavior consistent with existing project patterns.

## Output

Return missing error handling and minimal correction.
