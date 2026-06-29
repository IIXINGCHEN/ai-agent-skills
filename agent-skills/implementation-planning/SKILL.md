---
name: implementation-planning
description: Convert a user request or PRD into a concise, evidence-rich implementation plan before multi-step or risky code work.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: implementation-planning

## Purpose

Convert a user request into a concise, evidence-rich implementation plan before multi-step or risky code work.

This skill fuses the useful parts of the uploaded `workflow/plan.md` command into the skills package without forcing every task to create heavyweight documentation.

## When to Use

Use when a task has 3+ steps, touches multiple files, requires root-cause analysis, changes architecture, changes dependencies or build behavior, or needs multi-phase verification.

## Do Not Use When

Do not use for single-file trivial edits, pure conversation, or when the user explicitly asks not to create a plan and the task is safe and local.

## Inputs

- User request
- Repository discovery output
- Code-search-funnel findings
- Existing project rules such as `CLAUDE.md`, `AGENTS.md`, or local docs
- Similar implementation references when available

## Procedure

1. Clarify the actual goal, user value, and success criteria.
2. Classify task type: bug fix, feature, enhancement, refactor, audit, or production hardening.
3. Assess complexity: low, medium, or high.
4. Map affected systems, components, and entry points.
5. Gather codebase intelligence through `repo-discovery` and `code-search-funnel`.
6. Identify similar implementations, test patterns, error-handling patterns, and anti-patterns.
7. Identify required documentation or config files to read before implementation.
8. Choose the smallest safe implementation strategy.
9. Define verification commands and expected outcomes.
10. Record rollback considerations for risky changes.

## Checklist

- [ ] Goal and acceptance criteria are explicit.
- [ ] Task type and complexity are identified.
- [ ] Affected files/components are listed.
- [ ] Similar implementations are listed or absence stated.
- [ ] Tests or verification strategy is listed.
- [ ] Risks and rollback considerations are listed.
- [ ] No speculative future work is included.

## Output

Return either a concise chat plan or create/update `tasks/plan_<slug>_<YYYYMMDD>.md` when the active contract requires a plan file.

Suggested structure:

```md
# Plan: <task>

## Goal
## Task Type
## Current State
## Affected Areas
## Similar Implementations
## Selected Solution
## Verification Checklist
## Rollback Considerations
```
