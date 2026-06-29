---
name: code-review-primary
description: Perform the first evidence-based code review after implementation. Use for code review, pre-commit review, or changed-file review before second review or push.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: code-review-primary

## Purpose

Perform the first technical code review after implementation, focused on confirmed issues in changed files and impacted flows.

## When to Use

Use after `plan-execution` and before secondary review, push, or completion. Use when the user says code review, pre-commit review, or review changed files.

## Do Not Use When

Do not use for product requirements review, PRD review, or broad repository audit unless the user explicitly requests full-repo scope.

## Inputs

- Current repository state
- Changed files and untracked files
- Implementation plan or task summary
- Test and validation outputs
- Project rules and existing patterns

## Procedure

1. Verify Git and shell commands before first use.
2. Determine review scope: diff, staged, changed files, or full repo if requested.
3. Collect context with `git status`, `git diff --stat`, and relevant file lists when Git exists.
4. Read relevant changed files in enough context to verify issues are real.
5. Review by priority: correctness, security, reliability, data integrity, error handling, tests, maintainability.
6. Verify each issue with code evidence, command output, failing test, or reachable path.
7. Separate confirmed issues from risks and follow-ups.
8. Recommend minimal fixes and verification commands.
9. If safe fixes are requested, route to `review-fix-loop`; otherwise report findings.

## Checklist

- [ ] Review scope is explicit.
- [ ] Changed files are identified.
- [ ] Project rules and patterns are considered.
- [ ] Correctness issues checked.
- [ ] Security issues checked.
- [ ] Reliability and resource cleanup checked.
- [ ] Error handling checked.
- [ ] Data integrity checked.
- [ ] Tests and determinism checked.
- [ ] Every confirmed issue has evidence.

## Rules

- Focus on real bugs, not style-only preference.
- Be specific: file, symbol, line or nearby context.
- Do not claim an issue without evidence.
- Under strict profile, mock/stub/placeholder production paths are blockers.
- Do not silently fix large issues without user approval when scope expands.

## Output

Use `code_review_result` from `references/output-templates.md`.
