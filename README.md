# AI Agent Skills Package

A modular skill package for production-grade, evidence-driven AI coding agents.

## Contents

- `CLAUDE.md` for Claude Code.
- `AGENTS.md` for Codex / Codex-style agents.
- `agent-skills/*/SKILL.md` reusable skills.
- `references/` shared invocation, routing, evidence, output, and template contracts.
- `evals/` routing, blocked-state, adversarial, and output-contract cases.
- `manifest.json` and `agents/interface.yaml` metadata inspired by yao-meta-skill packaging patterns.

## Install

Copy the package contents into a project root.

## Canonical Lifecycle

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```

Use the smallest sufficient subset. The full lifecycle is the default only when the user requests end-to-end delivery.

## Mapped Skills

- init: `project-init`
- PRD: `prd-authoring`
- plan: `implementation-planning`
- execute: `plan-execution`
- code review: `code-review-primary`
- review fix loop: `review-fix-loop`
- second review: `code-review-secondary`
- multi-angle review: `multi-angle-review`
- commit readiness: `git-commit-readiness`
- push: `git-push-readiness`
- complete: `completion-gate`

## Recommended Invocation

```md
Use skill:
lifecycle-orchestrator

Lifecycle:
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete

Task:
[describe requested outcome]
```
