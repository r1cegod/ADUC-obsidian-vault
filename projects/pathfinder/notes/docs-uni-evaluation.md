---
type: source-summary
title: "University Agent Evaluation And Audit Log"
created: 2026-04-07
updated: 2026-04-07
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - university
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/uni_evaluation.md]]"
---

> **TL;DR**: The `uni` audit log now covers Round 1 Stage 4 replay through `uni_eval`, where all 4 attacks preserved populated `uni_research`, a valid trailing `PROBE:`, and a sharp final Vietnamese contradiction after one probe-field normalization fix.

## Summary
The university evaluation doc records the first dedicated hardening pass for the `university` stage. It focuses on retrieval-specific risk at the final school-choice layer: admissions checks, tuition/ROI math, prestige necessity, and international-path cost realism.

This note is useful because it captures both the architectural shift away from the legacy ToolNode loop and the evidence that the current `uni_eval` wrapper still carries a research-grounded contradiction through `context_compiler` and `output_compiler`.

If an agent is touching `backend/uni_graph.py`, this note is part of the must-read set.

## Key Points
- `uni` was refactored onto the same planner -> researcher -> synthesizer seam already used by `job`.
- Round 1 `uni_eval` now passes the current stage + compiler seam on `eval/uni_attack.jsonl`.
- One real contract bug surfaced during replay: invalid probe-field names leaked from the synthesizer and now get normalized in Python before `PROBE:` composition.
- The remaining cleanup item is still serializer-warning noise around structured outputs, not contradiction loss.

## Details
### Debugging Value
Use this note to understand why the university stage now writes a stable `uni_research` packet and why the current open risk is warning cleanup rather than school-choice contradiction loss.

### Position In The Corpus
This is both an audit history and a bridge into the broader retrieval-agent evaluation model for `job`, `major`, and `uni`.

## Related
- [[projects/pathfinder/notes/docs-data-agent-evaluation]]
- [[projects/pathfinder/notes/docs-research-sources]]
- [[projects/pathfinder/notes/docs-knowledge-agent-evaluation]]
