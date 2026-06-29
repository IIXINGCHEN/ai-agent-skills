---
name: git-commit-readiness
description: Check whether changes are ready for a safe atomic commit and produce a conventional commit message.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: git-commit-readiness

## Purpose

Check whether the working tree is ready for a safe, atomic commit and prepare a conventional commit message.

## When to Use

Use after implementation, verification, and reviews pass, before push or completion, when the repository uses Git.

## Do Not Use When

Do not create commits unless the user asked for commits or the active project workflow requires it. Do not use when Git is unavailable.

## Inputs

- Current Git status
- Diff and changed files
- Verification and review results
- Project commit conventions

## Procedure

1. Verify `git` exists.
2. Verify current directory is inside a Git repository.
3. Run `git status --porcelain` and `git diff --stat`.
4. Confirm changes are cohesive and atomic.
5. Confirm no secrets, generated junk, or unrelated files are included.
6. Confirm verification and reviews passed or risks are explicit.
7. Prepare conventional commit message focused on why.
8. If commit is requested, stage only intended files and commit without `--no-verify`.

## Checklist

- [ ] Git repository verified.
- [ ] Changed files reviewed.
- [ ] No unrelated files included.
- [ ] No secrets included.
- [ ] Verification passed or risk stated.
- [ ] Reviews passed or risk stated.
- [ ] Commit message is conventional and explains why.

## Rules

- Do not use `--no-verify`.
- Do not auto-add all files if unrelated changes exist.
- Do not add fixed co-author lines unless project/user requires them.
- Do not commit if blockers remain.

## Output

Use `commit_readiness_result` from `references/output-templates.md`.
