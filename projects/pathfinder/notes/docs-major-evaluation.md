---
type: source-summary
title: "Major Agent Evaluation And Audit Log"
created: 2026-04-07
updated: 2026-04-07
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - major
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/major_evaluation.md]]"
---

> **TL;DR**: This audit log records the first dedicated `major` hardening pass, where the stage was refactored off the legacy ToolNode into a `job`-style research seam and then passed both `major` and `major_eval` replay on 2026-04-07.

## Summary
The major evaluation doc captures two linked outcomes: the architectural refactor from a prompt-bound tool loop into a planner / researcher / synthesizer seam, and the first replay proof that this new seam preserves contradiction through both the stage graph and the `major_eval` wrapper.

The most important finding was not a crash but a retrieval-policy bug. The first draft let a Dreamer case skip research even though a new major field had been introduced. The fix made the contract explicit: a new major `field` always triggers search, and Dreamer paths still search for the execution barrier rather than bypassing retrieval.

If an agent is touching `backend/major_graph.py`, this note is now part of the must-read set.

## Key Points
- `major` no longer uses the legacy ToolNode loop; it now mirrors `job`'s explicit research seam.
- The first Dreamer replay exposed a real trigger bug, and the planner prompt now hard-requires search on new field claims.
- `major` and `major_eval` both passed the Round 1 attack set on 2026-04-07.
- The next open decision is `uni_eval` versus cleanup of the shared serializer warnings.

## Details
### Debugging Value
Use this note to understand why `major_graph.py` was moved off ToolNode and where the main residual risk still lives: warning cleanup, not contradiction loss.

### Position In The Corpus
This note is both the audit history for Stage 4 `major` work and the routing bridge into the remaining retrieval-stage audit queue.

## Related
- [[projects/pathfinder/notes/docs-data-agent-evaluation]]
- [[projects/pathfinder/notes/docs-job-evaluation]]
- [[projects/pathfinder/notes/docs-eval-how-to-use]]
