# Agent Contract

This repository uses a small always-on contract plus reusable skills. Use this file as the entry point for Claude Code.

---

## Always Active

Priority order:

1. Safety and reversibility
2. Verifiability
3. Existing project conventions and architecture
4. Simplicity
5. Speed

Hard rules:

- Do not assume files, commands, APIs, dependencies, configuration, schemas, data sources, logs, or tools exist.
- Verify existence before using anything.
- Before first use of a shell command, verify it exists with `command -v`, `which`, or the platform equivalent.
- Do not fabricate code, data, logs, API behavior, test results, metrics, project structure, or deployment details.
- Do not invent real data sources. If a real source of truth is absent, return Blocked.
- Prefer the smallest change that solves the confirmed problem.
- Fix root causes, not symptoms.
- Match existing architecture, naming, style, tests, and build flow.
- Do not introduce new dependencies unless strictly necessary and explicitly justified.
- Do not use `--no-verify`.
- Do not perform destructive or irreversible operations without `agent-skills/destructive-safety-gate/SKILL.md`.

---

## Canonical Lifecycle

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```

Use the smallest sufficient subset. Do not force phases that the task does not need.

---

## Skill Registry

### Lifecycle
- `lifecycle-orchestrator`
- `project-init`
- `prd-authoring`
- `implementation-planning`
- `plan-execution`
- `verification-gate`
- `execution-reporting`
- `completion-gate`

### Review Chain
- `code-review-primary`
- `review-fix-loop`
- `code-review-secondary`
- `multi-angle-review`

### Review Lenses
- `spatial-review`
- `vertical-call-chain-review`
- `reverse-trace-review`
- `security-review`
- `data-integrity-hardening`
- `error-handling-hardening`

### Discovery and Repair
- `repo-discovery`
- `code-search-funnel`
- `test-first-repair`
- `production-audit-repair`

### Git and Safety
- `git-commit-readiness`
- `git-push-readiness`
- `destructive-safety-gate`
---

## Shared References

- `references/skill-routing-table.md`
- `references/lifecycle-evidence-ledger.md`
- `references/invocation-templates.md`
- `references/output-templates.md`
- `references/issue-evidence-contract.md`
- `references/commands-fusion-map.md`
- `references/strict-review-profile.md`
- `references/lifecycle-workflow.md`
- `references/review-push-lifecycle.md`
- `references/prd-template.md`

---

## Evaluation Cases

- `evals/trigger_cases.json`
- `evals/no_route_cases.json`
- `evals/blocked_cases.json`
- `evals/output_contract_cases.json`
- `evals/route_cases.json`
- `evals/adversarial_route_cases.json`

---

## Conflict Resolution

1. System, developer, and explicit user instructions
2. Always-active contract in this file
3. Loaded skill instructions
4. Shared references and output templates
5. Examples and evals

Safety, anti-fabrication, verification, and destructive-operation rules are always active and cannot be disabled.

---

## Standard Invocation

```md
Use skill:
lifecycle-orchestrator

Lifecycle:
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete

Task:
[describe requested outcome]
```
