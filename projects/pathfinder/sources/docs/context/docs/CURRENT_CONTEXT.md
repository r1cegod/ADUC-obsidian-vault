# Current Context

Use this file as the short-lived working scratchpad for the current build cycle.
Move durable decisions to `PROJECT_CONTEXT.md` or `projects/pathfinder/sources/docs/DEV_LOG.md`.

> **TL;DR**: Thinking, Purpose, Goals, Job, Major, and Uni now pass the current Stage 4 replay seam at `stage_graph -> context_compiler -> output_compiler`. Duc's first real product conversation is captured under `eval/threads/13265a9e-63c7-45d8-9fdc-903fe5774547/`; the trace-to-Goals audit patched a streamed-output sanitizer gap, and the follow-up prompt pass turns Goals into a planning-ready handoff layer for Job/Major.

## Active Goal
- Goal: Continue the full-eval track from the captured live trace: verify the prompt-only Goals handoff contract beyond the stage-wrapper eval seam. Frontend fixture testing now has a baseline report and how-to.
- Success condition: the repo now holds verified Stage 4 passes for `thinking_eval`, `purpose_eval`, `goals_eval`, `job_eval`, `major_eval`, and `uni_eval`, the confidence prompts are aligned to Python's `> 0.8` gate, the structured-output serializer warnings are gone from the active graph boundary, the current `python_function_check` groups pass on the cleaned backend across all five buckets, the main `messages` lane prunes before orchestrator prompting, and the sub-orchestrator focus-eval lane has all 3 rounds complete with stable drift control and cleaned output hygiene.
- Deadline or milestone: 2026-04-07 evaluation-graph design-to-implementation handoff.

## Current Workstream
- Area: Live trace audit, Goals handoff prompts, and frontend fixture hardening on top of the cleaned Stage 4 wrapper pass and closed sub-orchestrator focus-eval lane.
- Files in play: `D:\ANHDUC\Path_finder\backend\data\prompts\goals.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\job.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\major.py`, `D:\ANHDUC\Path_finder\eval\live_trace_goals_rounds.jsonl`, `D:\ANHDUC\Path_finder\eval\live_trace_job_rounds.jsonl`, `D:\ANHDUC\Path_finder\eval\live_trace_major_rounds.jsonl`, `D:\ANHDUC\Path_finder\eval\LIVE_TRACE_TO_GOALS_AUDIT_2026-04-11.md`
- Why this matters now: the first real frontend conversation exposed that Goals could hold the user too long after enough directional handoff data; the prompt-only pass now needs broader orchestrator replay before treating the policy as full-system stable.

## Open Questions
- Resolved call: once the full eval sweep lands, then decide whether the higher-leverage next move is `orchestrator replay` or a broader `full-path production audit`.
- Resolved call: treat token optimization as active message-lane and sub-orchestrator work now, not as a separate undecided bucket after full eval.
- Resolved call: broaden `python_function_check` seam coverage beyond the current four groups where cheap deterministic proof is still missing.
- Resolved call: move maintained repo mirrors toward explicit sync routines rather than manual-by-default mirroring.
- New result: Round 3 is complete for both sub-orchestrator families on the dedicated focus-eval lane; the lane is now production ready at that seam, with the scope kept explicit and separate from full-system proof.
- Blocking component: no live blocking runtime debt is currently open at the stage + compiler seam.
- Next check: run the new live-trace Goals/Job/Major handoff rows through a broader orchestrator replay; use `eval/FRONTEND_EVALUATION_REPORT.md` as the frontend baseline unless a new UI change lands.

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

## Handoff
- Latest change: `goals.py`, `job.py`, and `major.py` prompts now implement the planning-ready Goals handoff policy; trace-derived 3-round eval rows for all three stages pass at Round 3 through `goals_eval`, `job_eval`, and `major_eval`.
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
- Next best action for eval session: run a broader orchestrator replay using the new live-trace rows without editing the raw live traces.
- Next best action for frontend session: only reopen frontend testing for new UI changes or mobile polish; baseline is `eval/FRONTEND_EVALUATION_REPORT.md`, with screenshots under `eval/frontend-eval/2026-04-11/` and workflow in the vault frontend evaluation how-to.

## Update Stamp
- Last updated: 2026-04-11
- Owner: Codex
