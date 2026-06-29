# AI Agent Skills

Languages: [English](README.md) | [中文](README.zh-CN.md)

Reusable, evidence-driven skills for AI coding agents.

This repository provides a production-oriented skill system for Claude Code, Codex-style agents, and generic agent-skill runtimes. It defines a complete software delivery lifecycle from project initialization to PRD, planning, execution, code review, review fixes, second review, multi-angle review, commit readiness, push readiness, and completion gating.

## Canonical Lifecycle

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```

Use the smallest sufficient subset. Do not force every phase when the task does not need it.

## What This Repository Provides

- `CLAUDE.md` entrypoint for Claude Code.
- `AGENTS.md` entrypoint for Codex and Codex-style agents.
- Reusable skills under `agent-skills/`.
- Shared references under `references/`.
- Routing and output evals under `evals/`.
- Metadata in `manifest.json`.
- Cross-agent interface metadata in `agents/interface.yaml`.

## Repository Structure

```text
.
├── CLAUDE.md
├── AGENTS.md
├── README.md
├── manifest.json
├── agents/
│   └── interface.yaml
├── agent-skills/
│   ├── lifecycle-orchestrator/
│   ├── project-init/
│   ├── prd-authoring/
│   ├── implementation-planning/
│   ├── plan-execution/
│   ├── verification-gate/
│   ├── code-review-primary/
│   ├── review-fix-loop/
│   ├── code-review-secondary/
│   ├── multi-angle-review/
│   ├── git-commit-readiness/
│   ├── git-push-readiness/
│   ├── completion-gate/
│   └── ...
├── references/
│   ├── skill-routing-table.md
│   ├── lifecycle-evidence-ledger.md
│   ├── review-push-lifecycle.md
│   ├── lifecycle-workflow.md
│   ├── output-templates.md
│   ├── issue-evidence-contract.md
│   ├── strict-review-profile.md
│   ├── prd-template.md
│   └── commands-fusion-map.md
└── evals/
    ├── trigger_cases.json
    ├── route_cases.json
    ├── adversarial_route_cases.json
    ├── blocked_cases.json
    ├── no_route_cases.json
    └── output_contract_cases.json
```

## Skills

### Lifecycle Skills

| Skill | Purpose |
|---|---|
| `lifecycle-orchestrator` | Orchestrates the full lifecycle. |
| `project-init` | Analyzes project setup, dependencies, runtime, environment, and commands. |
| `prd-authoring` | Creates or refines a Product Requirements Document. |
| `implementation-planning` | Converts a task or PRD into an implementation plan. |
| `plan-execution` | Executes an approved plan in small verified steps. |
| `verification-gate` | Prevents unverified completion claims. |
| `execution-reporting` | Produces evidence-based execution reports. |
| `completion-gate` | Decides Done, Done with accepted risks, or Blocked. |

### Review Chain Skills

| Skill | Purpose |
|---|---|
| `code-review-primary` | First evidence-based review after implementation. |
| `review-fix-loop` | Fixes confirmed review issues one by one. |
| `code-review-secondary` | Independent second review after fixes. |
| `multi-angle-review` | Multi-lens review: spatial, vertical, reverse, security, data, error, test, and push readiness. |

### Review Lens Skills

| Skill | Purpose |
|---|---|
| `spatial-review` | Reviews file structure, imports, paths, config, and architecture boundaries. |
| `vertical-call-chain-review` | Reviews UI/API/service/data flow. |
| `reverse-trace-review` | Traces failures or outcomes back to root cause. |
| `security-review` | Reviews auth, input, secrets, injection, paths, SSRF, and dependencies. |
| `data-integrity-hardening` | Ensures real data sources and schema consistency. |
| `error-handling-hardening` | Reviews realistic API/file/db/network/config/input failures. |

### Discovery, Repair, Git, and Safety Skills

| Skill | Purpose |
|---|---|
| `repo-discovery` | Finds repository structure, commands, config, and missing evidence. |
| `code-search-funnel` | Narrows the true change surface before editing. |
| `test-first-repair` | Uses focused reproduction and verification for risky fixes. |
| `production-audit-repair` | Performs production-grade multidimensional audit and repair. |
| `git-commit-readiness` | Checks atomic commit readiness and commit message. |
| `git-push-readiness` | Checks push readiness and only pushes when explicitly requested. |
| `destructive-safety-gate` | Requires two `DELETE` confirmations before destructive operations. |

## Quick Start

Use the full lifecycle:

```md
Use skill:
lifecycle-orchestrator

Lifecycle:
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete

Task:
[describe requested outcome]
```

Use production audit and repair:

```md
Use skill:
production-audit-repair

Task:
Perform a production-grade multidimensional audit and repair of this project.

Constraints:
- Remove mock, fake, demo, random, placeholder, and guessed data.
- Use only real APIs, logs, system metrics, database records, configured services, or user-provided files.
- Modify only necessary code.
```

Use review only:

```md
Use skills:
- code-review-primary
- code-review-secondary
- multi-angle-review

Task:
Review the implemented changes and report confirmed issues only.
```

## Safety Model

Always-active rules:

- Do not fabricate files, commands, APIs, logs, data, metrics, test results, or project structure.
- Verify before using commands, paths, dependencies, APIs, or data sources.
- Do not invent real data sources.
- Prefer the smallest safe change.
- Do not use `--no-verify`.
- Do not push unless explicitly requested.
- Default push mode is `readiness-only`.
- Do not perform destructive operations without the destructive safety gate.

## Push Policy

`git-push-readiness` supports two modes:

```text
readiness-only
execute-push
```

Default:

```text
readiness-only
```

Use `execute-push` only when the user explicitly asks to push.

Never force push to:

```text
main
master
protected branches
```

## Routing and Evidence

Use:

```text
references/skill-routing-table.md
```

to select the correct skill.

Use:

```text
references/lifecycle-evidence-ledger.md
```

before `completion-gate`.

Every confirmed issue should include:

```text
file
symbol / route / config
evidence
root cause
minimal fix
verification
risk
```

## Evals

This package includes:

```text
evals/trigger_cases.json
evals/route_cases.json
evals/adversarial_route_cases.json
evals/blocked_cases.json
evals/no_route_cases.json
evals/output_contract_cases.json
```

These evals help check:

- correct skill routing
- no-route behavior
- blocked states
- adversarial cases
- output contract completeness

## Compatibility

Designed for:

```text
Claude Code
Codex-style agents
Generic agent-skills runtimes
```

## Version

Current package version:

```text
1.2.0
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
