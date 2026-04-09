# Python Function Check - Stage Helper Matrix

> **TL;DR**: Group 3 covers helper parity across all six stage graphs. It now passes after exposing and closing a real Thinking bug where single-turn confidence caps could leave `done=True`.

Last updated: 2026-04-09

## Scope

- Files:
  - `backend/thinking_graph.py`
  - `backend/purpose_graph.py`
  - `backend/goals_graph.py`
  - `backend/job_graph.py`
  - `backend/major_graph.py`
  - `backend/uni_graph.py`
- Ownership:
  - `get_current_stage`
  - `reopen_invalidator_node`
  - retrieval `route_after_planner`

## Command

```powershell
venv\Scripts\python -m unittest test_stage_graph_helper_contract.py test_thinking_graph_contract.py test_uni_graph_contract.py
```

## Expected Proof

- all stage graphs honor `anchor_stage` before `current_stage`
- reopen invalidation follows the same targeted-field logic across all six stages
- retrieval stages branch to research only when both `need_research` and `search_query` are present
- Thinking and Uni helper contracts still pass under the broader matrix

## Latest Result

- Status: Pass
- Run date: 2026-04-09
- Result: `Ran 9 tests ... OK`

## Findings

First pass exposed two issues:
- the documented `unittest` command was silently skipping pytest-style bare-function files
- `backend/thinking_graph.py::_apply_verification_caps()` could cap confidences below threshold while leaving `done=True`

## Fix Applied

- converted the legacy Thinking and Uni helper contract files onto `unittest`
- normalized Thinking after verification caps so the helper itself, not just its caller, keeps `done` aligned with the current confidence state

## Notes

- This was the only group that surfaced a real backend inconsistency during the first grouped pass.
- The stale Thinking `done` bug is now closed and recorded here as part of the deterministic seam history.
