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

## Procedure

1. List exact target paths, objects, or data.
2. Explain irreversible impact.
3. Ask for confirmation with exact token `DELETE`.
4. After receiving `DELETE`, warn again.
5. Ask for a second `DELETE`.
6. Execute only after two consecutive `DELETE` confirmations.

## Rules

No shortcut. No inferred approval. No destructive operation before two confirmations. Do not batch unrelated destructive operations under one vague approval.

## Output

Either Blocked pending `DELETE` confirmation or executed with evidence after confirmation.
