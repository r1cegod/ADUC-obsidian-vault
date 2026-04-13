---
type: source-summary
title: "PathFinder Frontend Evaluation Workflow"
created: 2026-04-12
updated: 2026-04-13
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - workflow
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/frontend_evaluation_how_to_use.md]]"
---

> **TL;DR**: Use fixtures first for UI states, then the optimized live-user or identity-continuation workflow for traced product conversations; write reports in the vault and verify stage completion from raw backend state, not assistant wording.

## Summary
The frontend evaluation workflow is the third evaluation layer, sitting after the Python-function-check deterministic gate and replay eval. It tests the UI/product surface that replay cannot reach: fixture sweeps across 13 states, forced-stage transitions, overflow/overlay safety, and real student-like traced conversations.

Its strongest runtime rule: do not count assistant wording as stage completion. The workflow requires verifying stage completion from raw `getBackendState()` before calling any stage done. The 2026-04-13 update also made report ownership explicit: frontend evaluation reports live in the vault evaluation directory, while repo `eval/` keeps raw traces, datasets, manifests, and scratch inputs needed to reproduce findings.

## Key Points
- Fixture sweep and forced-stage sweep come before any live chat turns.
- A live user-like run requires a coherent student profile kept consistent throughout.
- Stage completion requires raw backend state agreement: `payload.rawState.goals?.done === true`, not assistant text.
- The uncertainty attack run is a distinct eval mode (added 2026-04-12): cooperative student with mixed preferences, family pressure, and shallow direction — tests that PathFinder separates genuine uncertainty from avoidance without soft-locking or false escalation.
- The identity-continuation run is a distinct eval mode (added 2026-04-12): restore trace `output` into a fresh debug session, continue as the same human, and use `eval/live_session_probe.py send --message-file` for UTF-8-safe turns with compact state checks.
- Reports live in `projects/pathfinder/sources/docs/evaluation/`; repo `eval/` is evidence only.

## Details

### Layers In Order
1. Static checks: `npm run lint`, `npm run build`
2. Browser load check + error overlay assertion
3. Debug helper availability: `window.__PF_DEBUG__`
4. Fixture sweep (13 fixtures via `applyFixture`)
5. Forced-stage sweep (all 6 stages, start + finish)
6. Live trace smoke (only when explicitly needed)
7. Live user-like run (student profile, batch quiz click, stage completion from raw state)
8. Uncertainty attack run (separate report, own evidence file)
9. Identity-continuation debug run (restore raw trace output, continue from compact state)

### Not A Substitute For Replay
The frontend eval cannot prove orchestrator routing, counter windows, or message-tag classification. It proves UI state transitions and visible response quality only.

### Startup Requirement
Backend must start in debug mode (`PATHFINDER_DEBUG=1`) for `window.__PF_DEBUG__` to be available. Do not run fixture sweeps against a non-debug backend.

## Related
- [[projects/pathfinder/notes/docs-eval-how-to-use]]
- [[projects/pathfinder/notes/docs-evaluation-domain]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub]]
- [[projects/pathfinder/notes/docs-python-function-check-how-to-use]]
- [[projects/pathfinder/notes/docs-goals-evaluation]]
- [[projects/pathfinder/notes/docs-thinking-evaluation]]
