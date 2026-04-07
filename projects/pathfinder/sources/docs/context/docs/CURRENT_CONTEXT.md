# Current Context

Use this file as the short-lived working scratchpad for the current build cycle.
Move durable decisions to `PROJECT_CONTEXT.md` or `projects/pathfinder/sources/docs/DEV_LOG.md`.

> **TL;DR**: Thinking, Purpose, Goals, Job, Major, and Uni now pass the current Stage 4 replay seam at `stage_graph -> context_compiler -> output_compiler`. The live decision is whether to clean the cross-cutting serializer warnings next or open a broader post-seam hardening pass.

## Active Goal
- Goal: Close the current Stage 4 seam cleanly across all six stages and decide what the next hardening layer should be.
- Success condition: the repo now holds verified Stage 4 passes for `thinking_eval`, `purpose_eval`, `goals_eval`, `job_eval`, `major_eval`, and `uni_eval`, with the next action narrowed to serializer-warning cleanup or a broader post-seam replay path.
- Deadline or milestone: 2026-04-07 evaluation-graph design-to-implementation handoff.

## Current Workstream
- Area: Stage 4 visible-response audit at the seam between each stage graph and the output compiler, now closed across all six stages.
- Files in play: `D:\ANHDUC\Path_finder\backend\major_graph.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\major.py`, `D:\ANHDUC\Path_finder\backend\data\state.py`, `D:\ANHDUC\Path_finder\backend\evaluation_graph.py`, `D:\ANHDUC\Path_finder\backend\output_graph.py`, `D:\ANHDUC\Path_finder\eval\major_attack.jsonl`, `D:\ANHDUC\Path_finder\eval\run_eval.py`, `projects/pathfinder/sources/docs/evaluation/major_evaluation.md`, `projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md`, `projects/pathfinder/sources/docs/DEV_LOG.md`
- Why this matters now: `major` was the last unaudited retrieval stage still lagging behind `job`'s explicit research seam. Now that both `major` and `major_eval` preserve retrieval-stage contradiction and final Vietnamese pressure, the current Stage 4 wrapper claim is closed across all six stages and the remaining question is what to harden next.

## Open Questions
- Question: after all six stage wrappers now pass, is the higher-leverage next move serializer-warning cleanup or a broader orchestrator / full-path replay.
- Blocking component: trace-time Pydantic serializer warnings still fire around structured outputs in the retrieval-stage traces even though the runs succeed.
- Next check: decide whether to clean the warnings before opening the next hardening layer.

## Risks And Constraints
- Risk: this seam can prove stage + compiler behavior, but it cannot prove orchestrator classification quality.
- Evidence: `message_tag`, `user_tag`, counters, and routing still belong to `input_parser`, `stage_manager`, and `counter_manager`, none of which are executed in the wrapper graph.
- Mitigation: explicitly scope the claim to "production-ready at the stage + compiler seam" and keep full orchestrator replay as a separate, higher-cost follow-up when routing behavior itself is under test.

## Commands To Re-Run
- `venv\Scripts\python -c "from backend.evaluation_graph import thinking_eval_graph, purpose_eval_graph, goals_eval_graph, job_eval_graph, major_eval_graph, uni_eval_graph; print('OK')"`
- `venv\Scripts\python -c "from backend.data.state import MajorResearch; from backend.major_graph import major_graph; print('OK')"`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack_v2.jsonl --graph thinking_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/purpose_attack.jsonl --graph purpose_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/goals_attack.jsonl --graph goals_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/uni_attack.jsonl --graph uni_eval`

## Handoff
- Latest change: refactored `major_graph.py` off the legacy ToolNode path into a `job`-style planner -> researcher -> synthesizer seam with a new `major_research` packet in state, then ran both `major` and `major_eval` on `eval/major_attack.jsonl`.
- Correction after follow-up: do not call this full-system production readiness. The correct claim is stage + compiler seam readiness only, starting with Thinking.
- Verification completed:
  - `venv\Scripts\python -c "from backend.evaluation_graph import thinking_eval_graph, purpose_eval_graph, goals_eval_graph, job_eval_graph, major_eval_graph, uni_eval_graph; print('OK')"`
  - `venv\Scripts\python -c "from backend.data.state import MajorResearch; from backend.major_graph import major_graph; print('OK')"`
  - `venv\Scripts\python -m unittest test_evaluation_graph_contract.py`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack_v2.jsonl --graph thinking_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack.jsonl --graph thinking_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/purpose_attack.jsonl --graph purpose_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/goals_attack.jsonl --graph goals_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/uni_attack.jsonl --graph uni_eval`
- Result from the latest run: all 4 Major attacks passed at both the stage-local and stage + compiler seams. One real bug surfaced on the first pass: the Dreamer case skipped research on a new `field` claim, so the planner prompt now hard-requires search on new fields, including Dreamer paths. Pydantic serializer warnings still appear in trace serialization.
- Next best action: decide whether to clean the serializer warnings next or open a broader post-seam replay path now that the current Stage 4 wrapper passes across all six stages.

## Update Stamp
- Last updated: 2026-04-07
- Owner: Codex
