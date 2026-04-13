# Current Context

Use this file as the short-lived working scratchpad for the current build cycle.
Move durable decisions to `PROJECT_CONTEXT.md` or `projects/pathfinder/sources/docs/DEV_LOG.md`.

> **TL;DR**: The 2026-04-13 university-finding frontend eval fixed the Major soft lock, and the focused University comparison replay now carries the R7 insight into a passing stage + compiler seam: UEH stays conditional, weak FPT evidence does not outrank UEH, and the response moves to RMIT instead of asking another meta-threshold/source-choice question.

## Active Goal
- Goal: Broaden the University comparison/ranking pass beyond the first UEH -> FPT -> RMIT seam.
- Success condition: with the seeded Product BA/UX student, University can compare UEH/FPT/RMIT/UEL on artifact strength, internship/network, international exposure, and ROI without re-asking meta column/page-type questions once the student has provided the priority order.
- Deadline or milestone: next PathFinder eval session.

## Current Workstream
- Area: Full-path/frontend evaluation hardening after the university-finding run.
- Files in play: `D:\ANHDUC\Path_finder\backend\data\prompts\uni.py`, `D:\ANHDUC\Path_finder\backend\uni_graph.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\output.py`, `D:\ANHDUC\Path_finder\eval\uni_comparison_frontend_2026-04-13.jsonl`, `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\uni_evaluation.md`
- Why this matters now: the first restored-trace comparison seam passes, but a broader proof still needs RMIT/UEL coverage and/or a full frontend continuation.

## Open Questions
- Resolved call: once the full eval sweep lands, then decide whether the higher-leverage next move is `orchestrator replay` or a broader `full-path production audit`.
- Resolved call: treat token optimization as active message-lane and sub-orchestrator work now, not as a separate undecided bucket after full eval.
- Resolved call: broaden `python_function_check` seam coverage beyond the current four groups where cheap deterministic proof is still missing.
- Resolved call: move maintained repo mirrors toward explicit sync routines rather than manual-by-default mirroring.
- New result: Round 3 is complete for both sub-orchestrator families on the dedicated focus-eval lane; the lane is now production ready at that seam, with the scope kept explicit and separate from full-system proof.
- Blocking component: no live blocking runtime debt is currently open at the output compiler seam after the frontend trace output regression pass.
- Next check: add or run the next University comparison cases for RMIT and UEL, then decide whether the higher-leverage follow-up is restored-trace replay or full frontend continuation.

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
- `venv\Scripts\python -m unittest backend.test.test_text_safety_contract backend.test.test_output_graph_contract backend.test.test_main_contract backend.test.test_debug_trace_contract`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/live_trace_goals_rounds.jsonl --graph goals_eval --workers 1`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/live_trace_job_rounds.jsonl --graph job_eval --workers 1`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/live_trace_major_rounds.jsonl --graph major_eval --workers 1`
- `venv\Scripts\python eval\run_eval.py --mode multi --file eval\live_frontend_output_regression_2026-04-12.jsonl --graph output --workers 1`

## Handoff
- Latest change: `eval/uni_comparison_frontend_2026-04-13.jsonl` now captures the R7 UEH/FPT/RMIT comparison loop. University research narrows school-specific official-domain searches, uses an `official_program` bucket, and the output compiler keeps named-school comparison probes from becoming another source-choice question.
- Correction after follow-up: do not call this full-system production readiness. The correct claim is stage + compiler seam readiness only, starting with Thinking.
- Verification completed:
- `venv\Scripts\python -m unittest backend.test.test_stage_profile_utils_contract`
- `venv\Scripts\python -m unittest backend.test.test_orchestrator_graph_contract`
- `venv\Scripts\python -m unittest backend.test.test_stage_graph_helper_contract backend.test.test_thinking_graph_contract backend.test.test_uni_graph_contract`
- `venv\Scripts\python -m unittest backend.test.test_evaluation_graph_contract backend.test.test_output_graph_contract backend.test.test_output_prompt_contract backend.test.test_stage_contract backend.test.test_main_contract`
- `venv\Scripts\python -m unittest backend.test.test_message_window_contract backend.test.test_sub_orchestrator_graph_contract backend.test.test_sub_orchestrator_focus_eval_contract`
- `venv\Scripts\python eval/run_sub_orchestrator_focus_eval.py --target worker --file eval/sub_orchestrator_worker_focus.jsonl --mode single`
  - `venv\Scripts\python -c "from backend.evaluation_graph import thinking_eval_graph, purpose_eval_graph, goals_eval_graph, job_eval_graph, major_eval_graph, uni_eval_graph; print('OK')"`
  - `venv\Scripts\python -c "from backend.data.state import MajorResearch; from backend.major_graph import major_graph; print('OK')"`
  - `venv\Scripts\python -m unittest backend.test.test_evaluation_graph_contract`
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
  - `venv\Scripts\python eval\run_eval.py --mode multi --file eval\uni_comparison_frontend_2026-04-13.jsonl --graph uni --workers 1`
  - `venv\Scripts\python eval\run_eval.py --mode multi --file eval\uni_comparison_frontend_2026-04-13.jsonl --graph uni_eval --workers 1`
  - `venv\Scripts\python -m unittest backend.test.test_uni_graph_contract backend.test.test_output_prompt_contract`
  - `venv\Scripts\python -m py_compile backend\uni_graph.py backend\data\prompts\uni.py backend\data\prompts\output.py`
  - `venv\Scripts\python eval\run_eval.py --mode multi --file eval\live_frontend_output_regression_2026-04-12.jsonl --graph output --workers 1`
  - `venv\Scripts\python -m unittest backend.test.test_output_prompt_contract backend.test.test_output_graph_contract backend.test.test_orchestrator_graph_contract backend.test.test_purpose_prompt_contract backend.test.test_sub_orchestrator_graph_contract backend.test.test_stage_profile_utils_contract backend.test.test_message_window_contract backend.test.test_main_contract backend.test.test_debug_trace_contract`
- Next best action for eval session: broaden University comparison/ranking replay to RMIT and UEL, or run a full frontend continuation if browser-level proof is needed.
- Next best action for frontend session: only reopen frontend testing for new UI changes or mobile polish; baseline reports live in `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\`, with repo screenshots/traces kept as reproduction evidence.

## Update Stamp
- Last updated: 2026-04-13
- Owner: Codex
