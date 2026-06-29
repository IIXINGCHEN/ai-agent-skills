---
name: git-push-readiness
description: Verify branch, remote, upstream, review, validation, and push readiness. Execute push only when explicitly requested.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: git-push-readiness

## Purpose

Prepare for safe push after implementation, verification, primary review, secondary review, and multi-angle review.

## When to Use

Use when the user says push, create PR, publish branch, or finish by pushing changes.

## Do Not Use When

Do not push if the user did not ask for push, if branch/remote are ambiguous, if blockers remain, or if verification/reviews are missing.

## Modes

- `readiness-only`: verify branch, remote, reviews, validation, permissions, and exact push command without pushing.
- `execute-push`: perform the push after readiness passes.

Default mode is `readiness-only` unless the user explicitly asks to push.

## Inputs

- Git status
- Current branch
- Remote configuration
- Commit state
- Verification and review outputs
- User-approved target remote/branch when needed

## Procedure

1. Verify `git` exists and repository is valid.
2. Check current branch with `git branch --show-current`.
3. Check remote configuration with `git remote -v`.
4. Check working tree status.
5. Confirm commits exist to push.
6. Confirm target remote and branch.
7. Block force push unless explicitly approved and not on protected branches.
8. Confirm verification, primary review, secondary review, and multi-angle review are pass/pass-with-accepted-risk.
9. In `readiness-only` mode, report the exact safe push command without running it.
10. In `execute-push` mode, push only the intended branch after explicit user request.
11. If PR creation is requested, verify `gh` exists and authentication is available before creating PR.

## Checklist

- [ ] Git repository verified.
- [ ] Branch identified.
- [ ] Remote identified.
- [ ] Working tree status checked.
- [ ] Commit state checked.
- [ ] Target branch confirmed.
- [ ] No blockers remain.
- [ ] Verification passed.
- [ ] Reviews passed or accepted risk is explicit.
- [ ] Mode is `readiness-only` or `execute-push`.
- [ ] Explicit push request exists before `execute-push`.
- [ ] Push command is non-force unless explicitly approved.

## Rules

- Never force push to `main`, `master`, or protected branches.
- Do not push unresolved review blockers.
- Do not create PR without verifying GitHub CLI availability and authentication.
- If authentication or permission fails, return Blocked with minimal next step.

## Output

Use `push_result` from `references/output-templates.md`.
