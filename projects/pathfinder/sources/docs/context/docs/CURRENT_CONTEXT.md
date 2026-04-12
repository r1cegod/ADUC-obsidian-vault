# Current Context

Use this file as the short-lived working scratchpad for the current build cycle.
Move durable decisions to `PROJECT_CONTEXT.md` or `projects/pathfinder/sources/docs/DEV_LOG.md`.

> **TL;DR**: The 2026-04-12 frontend trace output regression now passes: incomplete current stages stay anchored to raw backend `done` state, the output lock no longer conflicts with same-turn stage intro, Purpose now has handoff sufficiency, same-turn stage completion can advance before output, and sub-orchestrator workers read a capped 2.5k recent tail while the 5k summarizer lane remains intact.

## Active Goal
- Goal: Continue the full-eval track from the captured live trace: verify the prompt-only Goals handoff contract beyond the stage-wrapper eval seam. Frontend fixture testing now has a baseline report and how-to.
- Success condition: the repo now holds verified Stage 4 passes for `thinking_eval`, `purpose_eval`, `goals_eval`, `job_eval`, `major_eval`, and `uni_eval`, the confidence prompts are aligned to Python's `> 0.8` gate, the structured-output serializer warnings are gone from the active graph boundary, the current `python_function_check` groups pass on the cleaned backend across all five buckets, the main `messages` lane prunes before orchestrator prompting, and the sub-orchestrator focus-eval lane has all 3 rounds complete with stable drift control and cleaned output hygiene.
- Deadline or milestone: 2026-04-07 evaluation-graph design-to-implementation handoff.

## Current Workstream
- Area: Full-path evaluation hardening after the frontend trace output regression, same-turn stage transition patch, Purpose prompt audit, and test-path bug fixes.
- Files in play: `D:\ANHDUC\Path_finder\backend\data\prompts\output.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\purpose.py`, `D:\ANHDUC\Path_finder\backend\output_graph.py`, `D:\ANHDUC\Path_finder\backend\sub_orchestrator_graph.py`, `D:\ANHDUC\Path_finder\eval\live_frontend_output_regression_2026-04-12.jsonl`, `D:\ANHDUC\Path_finder\eval\FRONTEND_EVALUATION_REPORT.md`
- Why this matters now: the real frontend trace showed assistant wording could run ahead of raw state; the output compiler now has a raw-state lock, so the next proof should move back to a fresh live uncertainty chat or broader orchestrator/full-path eval rather than another output-only patch.

## Open Questions
- Resolved call: once the full eval sweep lands, then decide whether the higher-leverage next move is `orchestrator replay` or a broader `full-path production audit`.
- Resolved call: treat token optimization as active message-lane and sub-orchestrator work now, not as a separate undecided bucket after full eval.
- Resolved call: broaden `python_function_check` seam coverage beyond the current four groups where cheap deterministic proof is still missing.
- Resolved call: move maintained repo mirrors toward explicit sync routines rather than manual-by-default mirroring.
- New result: Round 3 is complete for both sub-orchestrator families on the dedicated focus-eval lane; the lane is now production ready at that seam, with the scope kept explicit and separate from full-system proof.
- Blocking component: no live blocking runtime debt is currently open at the output compiler seam after the frontend trace output regression pass.
- Next check: run a fresh uncertainty chat or broader orchestrator/full-path eval using `eval/FRONTEND_EVALUATION_REPORT.md` and `eval/live_frontend_output_regression_2026-04-12.jsonl` as the baseline evidence.

## Risks And Constraints
- Risk: this seam can prove stage + compiler behavior, but it cannot prove orchestrator classification quality.
- Evidence: `message_tag`, `user_tag`, counters, and routing still belong to `input_parser`, `stage_manager`, and `counter_manager`, none of which are executed in the wrapper graph.
- Mitigation: explicitly scope the claim to "production-ready at the stage + compiler seam", run full eval next, and only choose the replay-vs-full-path follow-up once that broader failure surface is visible.

## Commands To Re-Run
- `venv\Scripts\python -c "from backend.evaluation_graph import thinking_eval_graph, purpose_eval_graph, goals_eval_graph, job_eval_graph, major_eval_graph, uni_eval_graph; print('OK')"`
- `venv\Scripts\python -c "from backend.data.state import MajorResearch; from backend.major_graph import major_graph; print('OK')"`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack_v2.jsonl --graph thinking_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/purpose_attack.jsonl --graph purpose_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/goals_attack.jsonl --graph goals_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/uni_attack.jsonl --graph uni`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/uni_attack.jsonl --graph uni_eval`
- `venv\Scripts\python -m unittest test_text_safety_contract.py test_output_graph_contract.py test_main_contract.py test_debug_trace_contract.py`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/live_trace_goals_rounds.jsonl --graph goals_eval --workers 1`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/live_trace_job_rounds.jsonl --graph job_eval --workers 1`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/live_trace_major_rounds.jsonl --graph major_eval --workers 1`
- `venv\Scripts\python eval\run_eval.py --mode multi --file eval\live_frontend_output_regression_2026-04-12.jsonl --graph output --workers 1`

## Handoff
- Latest change: `output.py` and `output_graph.py` now lock output compilation to raw current-stage completion state without conflicting with transition intro; `purpose.py` adds handoff sufficiency for Purpose; `orchestrator_graph.py` adds a post-stage manager for same-turn completion; `sub_orchestrator_graph.py` caps worker read windows to reduce every-fifth-turn token fanout.
- Correction after follow-up: do not call this full-system production readiness. The correct claim is stage + compiler seam readiness only, starting with Thinking.
- Verification completed:
- `venv\Scripts\python -m unittest test_stage_profile_utils_contract.py`
- `venv\Scripts\python -m unittest test_orchestrator_graph_contract.py`
- `venv\Scripts\python -m unittest test_stage_graph_helper_contract.py test_thinking_graph_contract.py test_uni_graph_contract.py`
- `venv\Scripts\python -m unittest test_evaluation_graph_contract.py test_output_graph_contract.py test_output_prompt_contract.py test_stage_contract.py test_main_contract.py`
- `venv\Scripts\python -m unittest test_message_window_contract.py test_sub_orchestrator_graph_contract.py test_sub_orchestrator_focus_eval_contract.py`
- `venv\Scripts\python eval/run_sub_orchestrator_focus_eval.py --target worker --file eval/sub_orchestrator_worker_focus.jsonl --mode single`
  - `venv\Scripts\python -c "from backend.evaluation_graph import thinking_eval_graph, purpose_eval_graph, goals_eval_graph, job_eval_graph, major_eval_graph, uni_eval_graph; print('OK')"`
  - `venv\Scripts\python -c "from backend.data.state import MajorResearch; from backend.major_graph import major_graph; print('OK')"`
  - `venv\Scripts\python -m unittest test_evaluation_graph_contract.py`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack_v2.jsonl --graph thinking_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack.jsonl --graph thinking_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/purpose_attack.jsonl --graph purpose_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/goals_attack.jsonl --graph goals_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major_eval`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/uni_attack.jsonl --graph uni`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/uni_attack.jsonl --graph uni_eval`
- Result from the latest run: trace `live_0001.json` starts at Thinking turn 1; trace `live_0051.json` ends at Goals turn 51 with `thinking` and `purpose` completed; the session was stopped at `2026-04-11T15:38:47+07:00`.
- Result from the audit: final `output.messages` was already sanitized, but streamed live text and `assistant_text` could capture raw non-Latin chunks; that gap is patched. Goals now has a prompt-only planning-ready handoff contract, so the remaining proof is full orchestrator behavior rather than the stage-wrapper seam.
- Latest verification:
  - `venv\Scripts\python eval\run_eval.py --mode multi --file eval\live_frontend_output_regression_2026-04-12.jsonl --graph output --workers 1`
  - `venv\Scripts\python -m unittest test_output_prompt_contract.py test_output_graph_contract.py test_orchestrator_graph_contract.py test_purpose_prompt_contract.py test_sub_orchestrator_graph_contract.py test_stage_profile_utils_contract.py test_message_window_contract.py test_main_contract.py test_debug_trace_contract.py`
- Next best action for eval session: run the fresh uncertainty chat or a broader orchestrator/full-path audit without editing the raw live traces.
- Next best action for frontend session: only reopen frontend testing for new UI changes or mobile polish; baseline is `eval/FRONTEND_EVALUATION_REPORT.md`, with screenshots under `eval/frontend-eval/2026-04-11/` and workflow in the vault frontend evaluation how-to.

## Update Stamp
- Last updated: 2026-04-12
- Owner: Codex
