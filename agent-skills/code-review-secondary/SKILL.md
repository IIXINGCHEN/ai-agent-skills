---
name: code-review-secondary
description: Perform an independent second review after fixes or the first review. Use for second review, regression review, or final pre-push review.
metadata:
  maturity: production
  owner: local
  compatibility:
    - claude-code
    - codex
    - generic-agent-skills
---

# Skill: code-review-secondary

## Purpose

Perform an independent second-pass review to catch missed issues, verify fixes from the first review, and prevent regression before push/completion.

## When to Use

Use after `code-review-primary`, after `review-fix-loop`, or before `git-push-readiness` when the user asks for second review, second review, final review, or pre-push review.

## Do Not Use When

Do not use as a duplicate of the first review. It must change vantage point, verify previous findings, or focus on residual risk.

## Inputs

- First review findings
- Fixes applied after first review
- Current diff and file state
- Verification outputs
- Remaining risks and skipped items

## Procedure

1. Read first review findings or reconstruct them from prior report.
2. Verify each blocker/major finding was fixed or explicitly deferred.
3. Re-check the changed diff after fixes, not just the original diff.
4. Run focused regression checks or identify why they cannot run.
5. Review high-risk areas missed by first pass: boundary conditions, error paths, auth, data shape, and config.
6. Confirm no new orphan imports, dead branches, TODO/FIXME, or unverified fallbacks were introduced by fixes.
7. Decide final status: pass, pass with risks, blocked, or requires another fix loop.

## Checklist

- [ ] First review findings verified.
- [ ] Current diff rechecked after fixes.
- [ ] Regression risk checked.
- [ ] New issues introduced by fixes checked.
- [ ] Verification evidence reviewed.
- [ ] Final pre-push status is explicit.

## Rules

- Do not rubber-stamp the first review.
- Do not reopen resolved issues without new evidence.
- Do not approve push if blockers remain.
- If verification is missing, return pass-with-risk or Blocked, not Done.

## Output

Use `secondary_review_result` from `references/output-templates.md`.
