# Current Context

Use this file as the short-lived working scratchpad for the current build cycle.
Move durable decisions to `PROJECT_CONTEXT.md` or `projects/pathfinder/sources/docs/DEV_LOG.md`.

> **TL;DR**: Thinking, Purpose, Goals, Job, Major, and Uni now pass the current Stage 4 replay seam at `stage_graph -> context_compiler -> output_compiler`. Follow-up confidence audits aligned both the knowledge-agent and retrieval-agent extractor prompts to Python's `> 0.8` done threshold, the cross-cutting structured-output serializer warning debt is now paid by forcing LangChain structured output onto `method="function_calling"`, the grouped `python_function_check` workflow now passes across five buckets including the sub-orchestrator memory lane, and the sub-orchestrator focus-eval lane now has Round 3 complete for both `summarizer` and `worker` without touching the main orchestrator. The lane is now production ready at its own seam; the official live stack is now: run full eval, keep token optimization inside the sub-orchestrator lane, and move maintained repo mirrors onto explicit sync routines.

## Active Goal
- Goal: Keep the full-eval gate as the top production priority now that the sub-orchestrator focus-eval lane is closed cleanly at its own seam.
- Success condition: the repo now holds verified Stage 4 passes for `thinking_eval`, `purpose_eval`, `goals_eval`, `job_eval`, `major_eval`, and `uni_eval`, the confidence prompts are aligned to Python's `> 0.8` gate, the structured-output serializer warnings are gone from the active graph boundary, the current `python_function_check` groups pass on the cleaned backend across all five buckets, and the sub-orchestrator focus-eval lane has all 3 rounds complete with stable drift control and cleaned output hygiene.
- Deadline or milestone: 2026-04-07 evaluation-graph design-to-implementation handoff.

## Current Workstream
- Area: Post-seam hardening follow-up on the closed Stage 4 wrapper pass, now split across full-eval preparation, active sub-orchestrator token work, the new sub-orchestrator focus-eval lane, and expansion of the cheap deterministic seam gate.
- Files in play: `D:\ANHDUC\Path_finder\backend\sub_orchestrator_graph.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\sub_orchestrator.py`, `D:\ANHDUC\Path_finder\backend\sub_orchestrator_focus_eval.py`, `D:\ANHDUC\Path_finder\eval\run_sub_orchestrator_focus_eval.py`, `D:\ANHDUC\Path_finder\eval\sub_orchestrator_summarizer_focus.jsonl`, `D:\ANHDUC\Path_finder\eval\sub_orchestrator_worker_focus.jsonl`, `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\sub_orchestrator_focus_eval_how_to_use.md`, `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\sub_orchestrator_evaluation.md`, `projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md`, `projects/pathfinder/sources/docs/dev-log/days/2026-04-10.md`
- Why this matters now: the sub-orchestrator lane now has real bespoke prompts plus a direct evaluation seam, which makes token-work and prompt drift auditable without waiting for broader replay, while full eval still stays the main production gate.

## Open Questions
- Resolved call: once the full eval sweep lands, then decide whether the higher-leverage next move is `orchestrator replay` or a broader `full-path production audit`.
- Resolved call: treat token optimization as active sub-orchestrator work now, not as a separate undecided bucket after full eval.
- Resolved call: broaden `python_function_check` seam coverage beyond the current four groups where cheap deterministic proof is still missing.
- Resolved call: move maintained repo mirrors toward explicit sync routines rather than manual-by-default mirroring.
- New result: Round 3 is complete for both sub-orchestrator families on the dedicated focus-eval lane; the lane is now production ready at that seam, with the scope kept explicit and separate from full-system proof.
- Blocking component: no live blocking runtime debt is currently open at the stage + compiler seam.
- Next check: run the full eval layer on top of the cleaned Stage 4 seam and grouped Python-function checks, then decide the next higher-cost audit from that broader failure surface.

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

## Handoff
- Latest change: broadened the canonical `python_function_check` workflow to five grouped reports by adding the sub-orchestrator + `routing_memory` seam, kept the helper contract files on `unittest`, and preserved the cleaned Thinking post-cap `done` normalization behavior.
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
- Result from the latest run: the confidence contract is now aligned to `> 0.8` lock-safe counting across all six stages, the structured-output warning debt is paid, the grouped `python_function_check` workflow passes across all five buckets, and Thinking no longer preserves `done=True` after single-turn confidence caps pull the profile below threshold.
- Next best action: run the full eval pass on the cleaned backend, keep sub-orchestrator token optimization moving in parallel, and only reopen this lane if broader eval surfaces a seam mismatch the focused rounds did not cover.

## Update Stamp
- Last updated: 2026-04-10
- Owner: Codex
