# Output Templates

## implementation_result

```md
## Conclusion

[Done / Partially done / Blocked]

## Facts / Root Cause

- [confirmed fact]
- [root cause]

## Selected Solution

- [minimal solution chosen]

## Changes Made

- [file]: [change]

## Verification

| Check | Command | Result |
|---|---|---|
| Targeted test | `[command]` | [pass/fail/blocked] |

## Risks / Pending Items

- [risk or none]
```

Rules: be concise, do not claim unverified success, include actual commands and outcomes, and separate confirmed facts from assumptions.

## audit_report

```md
## Scope

## Confirmed Issues

### Issue: [short title]

- Severity:
- File:
- Symbol / route / config:
- Evidence:
- Root cause:
- Recommended fix:
- Verification:

## Risks

## Unknowns / Blockers

## Recommended Fix Order

## Verification Plan
```

Every confirmed issue must include evidence.

## blocked

```md
## Conclusion

Blocked.

## What Was Attempted

## Evidence Observed

## Blocking Reason

## Minimal Next Step
```

Rules: do not claim completion, do not fabricate unavailable data, and do not continue with speculative implementation.

## decision_report

```md
## Decision Needed

## Evidence

## Options

## Trade-offs

## Recommendation

## Minimal Next Step
```

## plan_result

```md
## Goal

## Task Type

## Current State

## Affected Areas

## Similar Implementations

## Selected Solution

## Verification Checklist

## Rollback Considerations
```

## execution_report

```md
## Completed Tasks

## Changes Made

## Tests Added

## Validation Results

## Divergences From Plan

## Skipped Items

## Ready For Commit
```

## project_init_result

```md
## Conclusion

## Detected Project

## Prerequisites

## Installation

## Environment Setup

## Start Commands

## Common Commands

## Validation

## Blockers / Missing Inputs
```

## prd_result

```md
## Conclusion

## PRD

[PRD content or file path]

## Assumptions

## Open Questions

## Recommended Next Step
```

## lifecycle_result

```md
## Conclusion

## Lifecycle Phases Used

| Phase | Skill | Result |
|---|---|---|

## Key Evidence

## Outputs Created

## Verification

## Risks / Pending Items
```

## code_review_result

```md
## Scope

## Review Summary

## Confirmed Issues

### Issue: [title]
- Severity:
- File:
- Evidence:
- Root cause:
- Suggested fix:
- Verification:

## Risks / Follow-ups

## Review Status
```

## secondary_review_result

```md
## Review Status

## First Review Findings Verified

## New Findings

## Regression Checks

## Remaining Risks

## Pre-Push Decision
```

## multi_angle_review_result

```md
## Overall Status

## Lens Results

| Lens | Result | Evidence |
|---|---|---|

## Blockers

## Major Risks

## Push Readiness
```

## review_fix_result

```md
## Fixed Issues

## Changes Made

## Tests / Verification

## Remaining Issues

## Next Review Step
```

## commit_readiness_result

```md
## Commit Readiness

## Changed Files

## Excluded Files

## Proposed Commit Message

## Blockers
```

## push_result

```md
## Push Status

## Remote / Branch

## Commands Executed

## Result

## PR Status

## Blockers / Next Step
```

## completion_result

```md
## Conclusion

## Lifecycle Status

| Phase | Result |
|---|---|

## Verification Evidence

## Review Evidence

## Push / PR Evidence

## Remaining Risks

## Final State
```
