---
name: code-search-funnel
description: Narrow the true code change surface before reading deeply or editing. Use for symbol search, route tracing, config lookup, and impact analysis.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: code-search-funnel

## Purpose

Narrow the true change surface before reading deeply or modifying code.

## When to Use

Use before modifying code, tracing a bug, auditing a call chain, or adding a feature.

## Do Not Use When

Do not use when the task has no code impact or the relevant file and exact symbol are already known from verified evidence.

## Inputs

User request, repository structure, and relevant symbols, route names, config keys, error messages, or API names.

## Procedure

1. Glob: inspect directory shape and file distribution.
2. Grep: search exact symbols, route names, config keys, error messages, and API names.
3. Read: inspect only relevant code ranges.
4. Trace: follow imports, callers, tests, types, and runtime entry points.
5. Narrow: repeat until the true change surface is identified.

## Rules

Do not assume a symbol exists. Do not read entire large files unless necessary. Find at least three similar correct implementations when the repository contains enough code. If fewer exist, state that and use the most local conservative design.

## Checklist

- [ ] Directory shape inspected.
- [ ] Exact-symbol searches run.
- [ ] Relevant code ranges read.
- [ ] Callers and callees traced.
- [ ] Tests or usage examples checked when available.
- [ ] Similar implementations identified or absence stated.
- [ ] Proposed change surface documented.

## Output

Return located files, relevant symbols, similar implementations, proposed change surface, and unknowns or blockers.
