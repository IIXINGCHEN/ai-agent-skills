---
name: destructive-safety-gate
description: Require explicit two-step confirmation before destructive or irreversible operations.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: destructive-safety-gate

## Purpose

Prevent destructive or irreversible operations without explicit two-step confirmation.

## When to Use

Use before destructive or irreversible operations such as `rm`, `del`, `rmdir`, `git reset --hard`, `git clean -fd`, dropping tables, deleting records, force pushing, or overwriting user data.

## Do Not Use When

Do not use as a substitute for ordinary file edits. Use it only for destructive or irreversible operations.

## Destructive Operation Classes

Treat these as destructive unless proven otherwise:

- File deletion or overwrite: `rm`, `del`, `rmdir`, truncation, recursive copy over user files, archive replacement.
- Git history or workspace destruction: `git reset --hard`, `git clean`, force push, branch deletion, tag deletion, rebase of shared branches.
- Data destruction: dropping tables, deleting records, destructive migrations, queue purges, cache flushes that remove source-of-truth data.
- Permission or publication changes: making private data public, revoking access, rotating or deleting credentials.
- Infrastructure destruction: deleting buckets, volumes, deployments, databases, environments, or production resources.

## Procedure

1. Classify the operation using the destructive operation classes above.
2. List exact target paths, objects, data, branches, resources, or permissions.
3. Explain irreversible impact and blast radius.
4. Create or identify a recoverable backup, snapshot, export, branch, or rollback plan. If no recovery path exists, state that explicitly and return Blocked unless the user accepts the risk.
5. Record the approval shape using `schemas/destructive-action.schema.json` when a structured record is practical.
6. Ask for confirmation with exact token `DELETE`.
7. After receiving `DELETE`, warn again with exact targets and recovery status.
8. Ask for a second `DELETE`.
9. Execute only after two consecutive `DELETE` confirmations.
10. Report the command/action executed, backup or rollback reference, and verification evidence.

## Rules

No shortcut. No inferred approval. No destructive operation before two confirmations. Do not batch unrelated destructive operations under one vague approval. Do not proceed if the target list, blast radius, or recovery plan is ambiguous.

## Output

Either Blocked pending `DELETE` confirmation or executed with evidence after confirmation.
