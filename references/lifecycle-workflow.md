# Lifecycle Workflow

The canonical lifecycle lives in `references/review-push-lifecycle.md`:

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```

This file documents the minimal delivery subset:

```text
init → PRD → plan → execute → verify → report
```

Use the smallest useful subset. The minimal subset is a routing aid, not a replacement for the canonical lifecycle and not a mandate to create unnecessary files.

## Phase Map

| Phase | Skill | Purpose | Stop Condition |
|---|---|---|---|
| init | `project-init` | Verify project setup, commands, runtime, env, and local readiness. | No source, missing runtime, missing env source, unsafe setup. |
| prd | `prd-authoring` | Define product requirements, MVP, stories, acceptance criteria, and risks. | Core goal/user/scope ambiguous. |
| plan | `implementation-planning` | Convert PRD or task into evidence-rich implementation plan. | Missing code evidence, unclear acceptance criteria, unsafe scope. |
| execute | `plan-execution` | Implement approved or required plan minimally. | Plan invalid, destructive action, non-local architecture change. |
| verify | `verification-gate` | Run tests/lint/type/build/smoke/log checks. | Commands missing and no reliable fallback. |
| report | `execution-reporting` | Report evidence, divergences, skipped work, risks, and next step. | None; report Blocked if incomplete. |

## Recommended Invocations

### Minimal Lifecycle Subset

```md
Use skill:
lifecycle-orchestrator

Lifecycle:
init → PRD → plan → execute → verify → report

Task:
[feature or project request]
```

### Init Only

```md
Use skill:
project-init

Task:
Analyze this project and produce safe setup, run, test, build, and validation steps.
```

### PRD Then Plan

```md
Use skills:
- prd-authoring
- implementation-planning

Task:
Create a PRD for [feature], then create an implementation plan after requirements are clear.
```

### Plan And Execute

```md
Use skills:
- implementation-planning
- plan-execution
- verification-gate
- execution-reporting

Task:
Plan and implement [task]. Keep changes minimal and verify with actual commands.
```

## File Creation Policy

- Create files only when requested or required by active project contract.
- Prefer concise chat output for exploratory work.
- If files are created, use project conventions when present.
- Do not create summary documents when the user explicitly asks for code-only implementation.

## Extended Review-Push Lifecycle

For delivery workflows requiring review and push, use `references/review-push-lifecycle.md`.

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```
