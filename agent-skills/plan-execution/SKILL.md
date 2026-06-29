---
name: plan-execution
description: Execute an approved or required implementation plan in small, verified, traceable steps.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: plan-execution

## Purpose

Execute an approved or required implementation plan in small, verified steps.

This skill fuses the useful parts of the uploaded `workflow/execute.md` command into the skills package.

## When to Use

Use when a plan file exists, a prior planning step produced tasks, or the user asks to implement an approved plan.

## Do Not Use When

Do not use to skip discovery, bypass verification, or execute a plan that conflicts with current evidence.

## Inputs

- Plan file or plan summary
- Repository state
- Relevant code and tests
- Verification commands from the plan

## Procedure

1. Read the full plan and confirm scope.
2. Verify the current repository state still matches plan assumptions.
3. Execute tasks in order unless evidence shows a safer order.
4. For each task, change the smallest necessary code.
5. Verify as you go with the smallest reliable check.
6. Add or update focused tests when project patterns support it.
7. Run final verification through `verification-gate`.
8. Report completed tasks, changed files, tests, validation results, divergences, and remaining risks.

## Checklist

- [ ] Plan read before edits.
- [ ] Plan assumptions verified against current files.
- [ ] Tasks executed in traceable order.
- [ ] Each change maps to a plan item or required fix.
- [ ] Tests added or reason not added.
- [ ] Validation commands run or absence stated.
- [ ] Divergences from plan explained.

## Output

Use `implementation_result` from `references/output-templates.md`. Include any justified divergence from the plan.
