# Evals Schema

Evaluation files are lightweight JSON case lists used to check skill routing, blocked behavior, no-route behavior, adversarial prompts, and output-contract completeness.

Each `*.json` file must contain a top-level array of case objects.

## Common Fields

| Field | Type | Meaning |
|---|---:|---|
| `input` | string | User request or prompt to evaluate. |
| `expected` | string | Generic expected result, currently used for `no_route` cases. |
| `expected_route` | string | Expected primary skill route, or `no_route`. |
| `expected_skills` | string[] | Expected triggered skills for trigger-focused cases. |
| `expected_output` | string | Expected output class such as `blocked`. |
| `expected_mode` | string | Expected mode for mode-sensitive skills, such as `readiness-only`. |
| `must_not_route` | string[] | Routes that must not be selected. |
| `required_reason` | string | Reason text or concept that must appear in blocked output. |
| `reason` | string | Human-readable rationale for the expected result. |
| `case` | string | Output contract case name. |
| `must_include` | string[] | Required fields or sections for an output contract case. |

## File Contracts

- `route_cases.json`: use `input` and `expected_route`.
- `trigger_cases.json`: use `input` and `expected_skills`.
- `no_route_cases.json`: use `input` and `expected`.
- `blocked_cases.json`: use `input`, `expected_output`, and `required_reason`.
- `adversarial_route_cases.json`: use route fields plus `reason`, `expected_mode`, `expected_output`, or `must_not_route` when needed.
- `output_contract_cases.json`: use `case` and `must_include`.

## Rules

- Do not reference skills that are absent from `manifest.skills`.
- Use `no_route` for prompts that should not activate a coding-agent skill.
- Use `blocked` when the safe result is to stop rather than invent missing evidence, data, permissions, or runtime state.
- Add new fields only after documenting them here and updating `scripts/validate-package.py`.
