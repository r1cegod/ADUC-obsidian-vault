---
type: source-summary
title: "University Agent Evaluation And Audit Log"
created: 2026-04-07
updated: 2026-04-13
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - university
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/uni_evaluation.md]]"
---

> **TL;DR**: The `uni` audit log covers Round 1 `uni_eval`, the 2026-04-09 confidence-lock audit, and the 2026-04-13 Round 2 frontend comparison replay where UEH stays conditional, weak FPT does not outrank UEH, and the response moves to RMIT instead of asking another meta-threshold/source-choice question.

## Summary
The university evaluation doc records the dedicated hardening passes for the `university` stage. It focuses on retrieval-specific risk at the final school-choice layer: admissions checks, tuition/ROI math, prestige necessity, international-path cost realism, and named-school comparison behavior.

This note is useful because it captures both the architectural shift away from the legacy ToolNode loop and the evidence that the current `uni_eval` wrapper can carry a research-grounded contradiction through `context_compiler` and `output_compiler`. The newest replay adds the frontend R7 comparison failure as executable evidence: after UEH evidence is weak and FPT evidence remains generic, the system keeps both conditional and moves the comparison to RMIT rather than asking the student for another threshold.

If an agent is touching `backend/uni_graph.py`, this note is part of the must-read set.

## Key Points
- `uni` was refactored onto the same planner -> researcher -> synthesizer seam already used by `job`.
- Round 1 `uni_eval` now passes the current stage + compiler seam on `eval/uni_attack.jsonl`.
- One real contract bug surfaced during replay: invalid probe-field names leaked from the synthesizer and now get normalized in Python before `PROBE:` composition.
- The 2026-04-13 comparison replay added `eval/uni_comparison_frontend_2026-04-13.jsonl`, `official_program` query routing, named-school domain narrowing, and an output-compiler guard for next-school probes.
- Remaining proof: broader RMIT/UEL comparison coverage or a full frontend continuation.

## Details
### Debugging Value
Use this note to understand why the university stage now writes a stable `uni_research` packet and why the current open risk is warning cleanup rather than school-choice contradiction loss.

### Position In The Corpus
This is both an audit history and a bridge into the broader retrieval-agent evaluation model for `job`, `major`, and `uni`.

## Related
- [[projects/pathfinder/notes/docs-data-agent-evaluation]]
- [[projects/pathfinder/notes/docs-research-sources]]
- [[projects/pathfinder/notes/docs-knowledge-agent-evaluation]]
