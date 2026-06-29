# Strict Review Profile

Use this profile when the user asks for production-grade, strict, or full-repository review.

Derived from the uploaded `validation/code-review-pro.md` command and adapted for reusable skills.

## Review Priority

1. Correctness
2. Security
3. Reliability
4. Data integrity
5. Error handling
6. Tests and verification
7. Maintainability
8. Performance when relevant

## Strict Requirements

### Spatial Analysis

- Validate module dependency graph.
- Verify imports resolve to real accessible modules.
- Check API/business/data layering boundaries.
- Check cross-cutting concerns such as config, logging, errors, and auth.

### Vertical Integration

- Trace UI/CLI to API/service/data store.
- Validate request validation, response schema, status codes, and error shape.
- Validate CRUD, transactions, and rollback behavior when applicable.
- Validate third-party integrations for auth, timeout, retry, and observability.

### Reverse Analysis

- Infer intended behavior from contracts and verify implementation matches.
- Backtrack from user workflows and failures.
- Verify realistic exception handling.
- Review attack surface for fail-closed behavior.

### No Mock Data Policy

Blocker by default in production paths:

- mock data shown to real users
- fake records written to real stores
- random/generated metrics represented as real monitoring data
- placeholder integrations in production flow

Allowed:

- tests
- docs examples
- explicitly gated local/dev paths

If no real source of truth exists, return Blocked instead of inventing one.

### Production Readiness Gate

- No placeholder/example-only production code.
- No silent fallback that hides production failures.
- No unverified completion claim.
- Every confirmed issue has evidence.
