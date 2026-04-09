---
type: synthesis
title: "PathFinder Evaluation Hub"
created: 2026-04-06
updated: 2026-04-09
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - synthesis
status: active
lang: en
---

> **TL;DR**: This hub is the default entrypoint for PathFinder evaluation work, routing across both replay eval and the newer grouped Python-function-check workflow.

## Summary
Use this hub when the task is about attack datasets, replay execution, deterministic backend seam checks, evaluation policy, or stage hardening status. It connects the top-level evaluation router to both the replay guide and the newer Python-function-check workflow, plus the stage-specific audit logs.

This domain is already large enough that hub-based navigation is better than opening individual eval notes one by one from the README.

## Suggested Entry Points
- Need the official evaluation workflow and signoff rules: [[projects/pathfinder/notes/docs-eval-how-to-use|PathFinder Evaluation Pipeline]]
- Need the cheap deterministic backend gate before replay: [[projects/pathfinder/notes/docs-python-function-check-how-to-use|PathFinder Python Function Check]]
- Need the general knowledge-agent evaluation model: [[projects/pathfinder/notes/docs-knowledge-agent-evaluation|Knowledge Agent Evaluation Guide]]
- Need runner mechanics or graph registration: [[projects/pathfinder/notes/docs-eval-run-eval|eval/run_eval.py - How To Use]]
- Need the cheaper stage-to-compiler replay seam: [[projects/pathfinder/notes/docs-evaluation-graph|Evaluation Graph]]
- Need knowledge-agent audit status: [[projects/pathfinder/notes/docs-thinking-evaluation|Thinking Agent Evaluation And Audit Log]], [[projects/pathfinder/notes/docs-purpose-evaluation|Purpose Agent Evaluation And Audit Log]], [[projects/pathfinder/notes/docs-goals-evaluation|Goals Agent Evaluation And Audit Log]]
- Need retrieval-stage rules or data-agent eval shape: [[projects/pathfinder/notes/docs-data-agent-evaluation|Data Agent Evaluation Guide]], [[projects/pathfinder/notes/docs-job-evaluation|Job Agent Evaluation And Audit Log]], [[projects/pathfinder/notes/docs-uni-evaluation|University Agent Evaluation And Audit Log]], [[projects/pathfinder/notes/docs-research-sources|Retrieval Research Sources]]

## Use This Hub For
- planning or replaying evaluation work
- proving deterministic backend seams before replay
- checking stage hardening status
- understanding retrieval-stage evaluation rules
- locating the right stage-local audit history

## Related
- [[projects/pathfinder/README]]
- [[projects/pathfinder/notes/docs-eval-how-to-use]]
- [[projects/pathfinder/notes/docs-python-function-check-how-to-use]]
- [[projects/pathfinder/notes/docs-knowledge-agent-evaluation]]
- [[projects/pathfinder/notes/docs-evaluation-graph]]
- [[projects/pathfinder/notes/pathfinder-prompt-hub]]
- [[projects/pathfinder/notes/pathfinder-workflow-hub]]
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]
