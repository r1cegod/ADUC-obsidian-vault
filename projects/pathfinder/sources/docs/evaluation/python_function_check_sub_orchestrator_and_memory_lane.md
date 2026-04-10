# Python Function Check - Sub-Orchestrator And Memory Lane

> **TL;DR**: Group 5 covers the cheap deterministic checks for `routing_memory` pruning, sub-orchestrator routing, focused eval entrypoints, and the current periodic-refresh policy for the sub-orchestrator worker lane.

Last updated: 2026-04-10

## Scope

- Files:
  - `backend/message_window.py`
  - `backend/sub_orchestrator_graph.py`
  - `backend/sub_orchestrator_focus_eval.py`

## Command

```powershell
venv\Scripts\python -m unittest test_message_window_contract.py test_sub_orchestrator_graph_contract.py test_sub_orchestrator_focus_eval_contract.py
```

## Expected Proof

- `routing_memory` prune planning returns the right retired slice, kept slice, and `RemoveMessage(...)` updates
- the sub-orchestrator router refreshes core bool fields every 5 turns without waking low-signal pattern workers by default
- `compliance` stays on the intended every-5-turn worker refresh in addition to current-message and counter triggers
- focused `summarizer` and `worker` entrypoints stay callable without the main orchestrator

## Latest Result

- Status: Pass
- Run date: 2026-04-10
- Result: `Ran 16 tests ... OK`

## Notes

- This group is the new cheap seam bucket added after the sub-orchestrator focus-eval lane became production-ready at its own seam.
- It complements, but does not replace, the focused eval runner in `eval/run_sub_orchestrator_focus_eval.py`.
