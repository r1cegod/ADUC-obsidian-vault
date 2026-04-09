# Python Function Check - Orchestrator Policy

> **TL;DR**: Group 2 covers the Python-owned orchestrator policy in `backend/orchestrator_graph.py`. It now passes on stage advancement, anchor handling, counter windows, and route selection.

Last updated: 2026-04-09

## Scope

- File: `backend/orchestrator_graph.py`
- Ownership:
  - stage advancement
  - anchor-stage routing
  - contradiction bookkeeping
  - counter escalation
  - route selection

## Command

```powershell
venv\Scripts\python -m unittest test_orchestrator_graph_contract.py
```

## Expected Proof

- stage progression moves to the next unfinished stage
- requested anchors split cleanly into `forced` vs `revisit`
- path-debate readiness only flips under the intended Python gate
- the 10-turn escalation window emits normalized family text and resets correctly
- bypass or escalation traffic routes directly to `context_compiler`

## Latest Result

- Status: Pass
- Run date: 2026-04-09
- Result: `Ran 8 tests ... OK`

## Notes

- This group is the highest-risk deterministic seam above the current Stage 4 wrapper pass.
- It now has direct coverage for stage-manager and counter-manager policy instead of only the escalation-family formatter helpers.
