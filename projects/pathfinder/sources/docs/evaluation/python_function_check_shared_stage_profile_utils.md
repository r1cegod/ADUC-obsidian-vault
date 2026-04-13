# Python Function Check - Shared Stage Profile Utils

> **TL;DR**: Group 1 covers the shared reopen and done-normalization layer in `backend/stage_profile_utils.py`. It now passes and locks the common behavior every stage relies on.

Last updated: 2026-04-09

## Scope

- File: `backend/stage_profile_utils.py`
- Ownership:
  - reentry mode detection
  - probe-target invalidation
  - done-field counting
  - normalized `done` recomputation

## Command

```powershell
venv\Scripts\python -m unittest backend.test.test_stage_profile_utils_contract
```

## Expected Proof

- reentry mode only activates on real anchor detours
- reopen invalidation clamps only the targeted field when a `PROBE:` field exists
- reopen invalidation falls back to all done-fields when probe targeting is absent
- nested Goals `done` flags are recomputed from shared confidence rules

## Latest Result

- Status: Pass
- Run date: 2026-04-09
- Result: `Ran 5 tests ... OK`

## Notes

- This group is the best leverage point because one bug here can corrupt every stage.
- The current suite now covers both targeted-field invalidation and nested Goals normalization, which were previously unguarded.
