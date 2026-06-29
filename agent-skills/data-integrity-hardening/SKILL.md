---
name: data-integrity-hardening
description: Ensure data comes from real sources of truth and remains consistent across storage, APIs, services, and UI.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: data-integrity-hardening

## Purpose

Ensure data comes from real sources of truth and remains consistent across storage, APIs, services, and UI.

## When to Use

Use when the task requires real data, mock removal, schema consistency, API/data validation, monitoring metrics, logs, or production hardening.

## Do Not Use When

Do not use to invent a source of truth or create fake data fallbacks.

## Procedure

Check source of truth, mock/demo/fake/random/generated/placeholder data, schema consistency, type conversion safety, serialization/deserialization correctness, database constraints and migrations, API response shape consistency, and real-data provenance.

## Checklist

- [ ] Source of truth identified.
- [ ] Mock/demo/sample/random/generated placeholder data locations identified.
- [ ] API response schemas checked.
- [ ] Database schema or query shape checked when applicable.
- [ ] Type conversions checked.
- [ ] Serialization/deserialization checked.
- [ ] Frontend data expectations checked when applicable.

## Rules

Real data must come from configured APIs, logs, databases, system metrics, or user-provided files. Do not invent real data sources. If no source of truth exists, return Blocked. Do not replace fake data with another fake fallback.

## Output

Return fake/mock data locations, real source availability, required fix, and blocked items if real source is missing.
