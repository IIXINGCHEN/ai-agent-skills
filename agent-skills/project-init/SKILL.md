---
name: project-init
description: Analyze a project and produce safe evidence-based initialization steps for dependencies, environment, startup, validation, and common commands.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: project-init

## Purpose

Initialize project understanding and produce safe setup guidance without guessing commands, tools, runtimes, or environment variables.

This skill complements `repo-discovery`: `repo-discovery` identifies what exists; `project-init` turns verified evidence into executable setup guidance.

## When to Use

Use when the user asks to initialize, set up, onboard, bootstrap, run locally, install dependencies, start a dev server, document common commands, or verify project readiness.

## Do Not Use When

Do not use for production deployment, destructive environment reset, dependency upgrades, or installing new tooling without explicit approval.

## Inputs

- Project path or current directory
- Repository files
- Build/package manager files
- Existing docs such as README, CONTRIBUTING, `.env.example`, or project-specific agent files
- Available shell tools verified by `command -v`, `which`, or platform equivalent

## Procedure

1. Run `repo-discovery` first.
2. Identify build system files such as `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `Makefile`, `pom.xml`, `build.gradle`, `next.config.*`, `vite.config.*`, or framework config files.
3. Identify package manager from lockfiles and project config, not preference.
4. Identify runtime requirements from version files, engines, toolchain files, or docs.
5. Identify framework and dev tools.
6. Identify environment configuration sources such as `.env.example`, config schemas, README sections, or deployment docs.
7. Produce setup steps using only verified commands and files.
8. For each command, state whether it was executed, only recommended, or blocked.
9. Provide validation commands from existing scripts or project docs.
10. Return Blocked if required runtime, package manager, env source, or project source is missing.

## Checklist

- [ ] Project source exists.
- [ ] Repository root or project path is verified.
- [ ] Package manager is derived from lockfile/config evidence.
- [ ] Runtime version source is identified or absence stated.
- [ ] Install command is verified or absence stated.
- [ ] Environment setup source is identified or absence stated.
- [ ] Start command is identified or absence stated.
- [ ] Test/build/lint/type-check commands are identified or absence stated.
- [ ] Commands are non-destructive and reversible.
- [ ] Platform caveats are stated when relevant.

## Evidence Required

- File paths that define setup behavior
- Detected scripts or commands
- Tool availability checks
- Missing setup requirements

## Stop Conditions

Stop and return Blocked if:

- no project source code exists
- package manager cannot be determined and multiple conflicting choices exist
- required runtime/tool is missing and cannot be installed safely
- environment variables are required but no source or user-provided values exist
- setup requires destructive cleanup or overwriting user files without confirmation

## Output

Use `project_init_result` from `references/output-templates.md`.

If writing a file is requested or required, create `tasks/init_<project-slug>_<YYYYMMDD>.md` or `.agents/init/<project-slug>.md` according to project convention.
