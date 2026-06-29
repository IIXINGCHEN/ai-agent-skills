---
name: prd-authoring
description: Create or refine a Product Requirements Document from goals, constraints, evidence, MVP scope, user stories, and acceptance criteria.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: prd-authoring

## Purpose

Create a clear, actionable Product Requirements Document that can feed `implementation-planning` without smuggling in unverified implementation assumptions.

## When to Use

Use when the user asks for a PRD, product requirements, MVP scope, user stories, feature specification, requirements clarification, or a product/design document before planning.

## Do Not Use When

Do not use for direct code implementation, bug fixes with already clear acceptance criteria, or speculative product strategy unrelated to the current task.

## Inputs

- Conversation context
- User goals and constraints
- Existing project context when available
- Product, user, technical, compliance, and integration requirements
- Open questions and assumptions

## Procedure

1. Extract explicit requirements from the user request and conversation.
2. Identify implicit needs, constraints, non-goals, and success criteria.
3. Ask only the smallest number of clarifying questions when critical information is missing.
4. Separate facts, assumptions, and open questions.
5. Define MVP scope and out-of-scope items.
6. Write user stories with concrete benefits.
7. Define functional and non-functional requirements.
8. Include architecture, API, integration, security, and configuration sections only when applicable.
9. Define measurable acceptance criteria.
10. Define implementation phases that can feed `implementation-planning`.
11. Run quality checks before final output.

## PRD Template

Use `references/prd-template.md` for the full PRD template. Keep short PRDs short and omit sections that are not applicable.

## Checklist

- [ ] Executive summary is concise.
- [ ] MVP scope is explicit.
- [ ] Out-of-scope items are explicit.
- [ ] User stories include benefit.
- [ ] Requirements are testable.
- [ ] Success criteria are measurable.
- [ ] Risks have mitigations.
- [ ] Assumptions are labeled.
- [ ] Open questions are not hidden.
- [ ] Implementation phases are actionable.

## Rules

- Do not fabricate business facts, user research, metrics, or technical constraints.
- Do not treat assumptions as confirmed requirements.
- Do not over-spec architecture when the user asked only for product requirements.
- Do not create a PRD file unless the user asks for a file or project convention requires it.

## Stop Conditions

Stop and ask clarifying questions if the core product goal, target user, or MVP boundary is ambiguous and cannot be safely assumed.

Return Blocked if required external facts are unavailable and the user asks for evidence-backed PRD content.

## Output

Use `prd_result` from `references/output-templates.md`.

If writing a file is requested or required, create `PRD.md`, `docs/PRD.md`, or `tasks/prd_<slug>_<YYYYMMDD>.md` according to project convention.
