# Issue Evidence Contract

Every confirmed issue must be evidence-backed.

## Required Fields

```md
### Issue: [short title]

- Severity: [critical/high/medium/low]
- Category: [spatial/vertical/reverse/data/error/security/test/config]
- File: [path]
- Symbol / route / config key: [name]
- Evidence: [actual code, command output, log, response, or test failure]
- Root cause: [why this happens]
- Minimal fix: [smallest safe correction]
- Verification: [specific check]
- Risk: [remaining risk]
```

## Severity Guide

- Critical: security, data loss, or production outage risk with confirmed path.
- High: broken user-visible behavior or invalid production data path.
- Medium: confirmed correctness, reliability, or maintainability issue in active code.
- Low: localized issue with limited impact.

## Anti-Patterns

Do not report guessed bugs, generic best-practice comments, risks not tied to reachable code, unrequested missing features, or fake-data concerns when no real replacement source exists. Use Blocked for missing real sources.
