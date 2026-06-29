---
name: spatial-review
description: Audit project structure as a file-system, module, dependency, entry point, and configuration graph.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: spatial-review

## Purpose

Audit project structure as a file-system, module, dependency, and configuration graph.

## When to Use

Use when auditing project organization, import/export correctness, static paths, configuration paths, entry points, and module boundaries.

## Do Not Use When

Do not use as a substitute for runtime behavior tracing or data-source verification.

## Procedure

Check directory organization, module boundaries, import/export correctness, configuration file paths, static asset paths, environment references, build/runtime entry points, circular dependencies, and dead or unreachable modules.

## Checklist

- [ ] Directory layout matches detected stack conventions.
- [ ] Imports resolve to existing files or packages.
- [ ] Exports match consumers.
- [ ] Path aliases are defined and used consistently.
- [ ] Config references point to existing files.
- [ ] Static asset references point to existing assets.
- [ ] Entry points are reachable from scripts or runtime config.
- [ ] Circular dependencies checked when tooling exists.
- [ ] Dead or unreachable code reported only when evidenced.

## Evidence Required

File paths, import statements, config references, and command output.

## Output

Return confirmed structure issues and exact affected files.
