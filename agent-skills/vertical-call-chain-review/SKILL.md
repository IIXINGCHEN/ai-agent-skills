---
name: vertical-call-chain-review
description: Audit complete vertical behavior chains across UI, API, backend, services, databases, logs, and external systems.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: vertical-call-chain-review

## Purpose

Audit complete vertical behavior chains across UI, API, backend, services, databases, logs, and external systems.

## When to Use

Use when checking frontend-backend-database/API completeness, API contract consistency, or user-visible behavior driven by multiple layers.

## Do Not Use When

Do not use for isolated single-file syntax fixes unless the fix affects a cross-layer contract.

## Procedure

Trace user action, frontend component/client entry, client API call, backend route/controller, service/business logic, database/query/log/API source, response serialization, frontend rendering, and loading/empty/error states.

## Checklist

- [ ] User operation identified.
- [ ] Frontend caller identified when applicable.
- [ ] Client request shape identified.
- [ ] Backend route/controller identified.
- [ ] Service/business logic identified.
- [ ] Data source identified.
- [ ] Response shape identified.
- [ ] Frontend rendering state identified.
- [ ] Loading, empty, and error states checked.
- [ ] Auth/authz propagation checked when applicable.

## Contract Checks

Request schema, response schema, status code, error shape, data type, and auth propagation consistency.

## Output

Return broken or incomplete chains with evidence.
