---
name: repo-discovery
description: Identify repository structure, execution entry points, available commands, config, environment sources, and missing project evidence.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: repo-discovery

## Purpose

Identify repository structure, execution entry points, and missing project evidence before audit or modification.

## When to Use

Use before any code modification, audit, bug fix, refactor, or production hardening task.

## Do Not Use When

Do not use for pure conversation, non-code writing, or tasks where repository structure is already fully established in the current run.

## Inputs

Working directory, available shell tools, and project files.

## Procedure

1. Verify shell commands before first use.
2. Identify repository root.
3. Identify package manager and lock files.
4. Identify runtime and language versions.
5. Locate build, test, lint, type-check, and start commands.
6. Locate application entry points.
7. Locate configuration files.
8. Locate environment variable examples, schemas, or docs.
9. State absent items explicitly.

## Checklist

- [ ] Repository root found or absence stated.
- [ ] Git status checked when available.
- [ ] Package manager and lock files identified.
- [ ] Runtime versions identified when possible.
- [ ] Build, test, lint, type-check, and start commands identified or absence stated.
- [ ] Application entry points identified.
- [ ] Configuration files identified.
- [ ] Environment variable source identified or absence stated.

## Evidence Required

Commands executed, files found, scripts found, and missing entries.

## Stop Conditions

Stop and return Blocked if no project source code exists.

## Output

Return repository root, detected stack, available commands, missing commands, entry points, config sources, and risk notes.
