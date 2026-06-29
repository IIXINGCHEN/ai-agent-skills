---
name: security-review
description: Audit security-sensitive behavior in task scope: auth, validation, secrets, injection, paths, SSRF, deserialization, and dependencies.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: security-review

## Purpose

Audit security-sensitive behavior in the confirmed task scope.

## When to Use

Use when changes touch authentication, authorization, user input, filesystem paths, network calls, database queries, secrets, serialization, uploads, or external integrations.

## Do Not Use When

Do not expand into a full security audit unless the user asks for it. Keep scope tied to the active task.

## Procedure

Check authentication boundaries, authorization checks, input validation, output encoding, secrets handling, SQL/NoSQL/command injection risk, path traversal risk, SSRF risk, CSRF/CORS behavior, unsafe deserialization, and dependency/supply-chain impact.

## Checklist

- [ ] Authn/authz boundaries checked.
- [ ] Inputs validated or constrained.
- [ ] Outputs encoded or escaped where applicable.
- [ ] Secrets are not printed or committed.
- [ ] Queries are parameterized where applicable.
- [ ] Shell commands avoid unsanitized input.
- [ ] File paths prevent traversal where applicable.
- [ ] External URLs are constrained where applicable.
- [ ] Deserialization is safe.
- [ ] New dependency risk assessed if introduced.

## Rules

Do not print secrets. Do not weaken security to make tests pass. Prefer fail-closed behavior for security controls.

## Output

Return confirmed security issues, evidence, minimal fix, and verification.
