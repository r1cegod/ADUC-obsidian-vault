# Current Context

Use this file as the short-lived working scratchpad for the current build cycle.
Move durable decisions to `PROJECT_CONTEXT.md` or `projects/pathfinder/sources/docs/DEV_LOG.md`.

> **TL;DR**: Thinking, Purpose, Goals, Job, Major, and Uni now pass the current Stage 4 replay seam at `stage_graph -> context_compiler -> output_compiler`. Follow-up confidence audits aligned both the knowledge-agent and retrieval-agent extractor prompts to Python's `> 0.8` done threshold, the cross-cutting structured-output serializer warning debt is now paid by forcing LangChain structured output onto `method="function_calling"`, and the new four-group `python_function_check` workflow now passes after fixing Thinking's stale post-cap `done` flag. The live next move is the broader full eval pass.

## Active Goal
- Goal: Close the current Stage 4 seam cleanly across all six stages, lock the cheap Python-owned backend seams, and move up to the broader full eval layer.
- Success condition: the repo now holds verified Stage 4 passes for `thinking_eval`, `purpose_eval`, `goals_eval`, `job_eval`, `major_eval`, and `uni_eval`, the confidence prompts are aligned to Python's `> 0.8` gate, the structured-output serializer warnings are gone from the active graph boundary, and all four `python_function_check` groups pass on the cleaned backend.
- Deadline or milestone: 2026-04-07 evaluation-graph design-to-implementation handoff.

## Current Workstream
- Area: Post-seam hardening follow-up on the closed Stage 4 wrapper pass, now centered on cheap deterministic backend proofs before the next replay layer.
- Files in play: `D:\ANHDUC\Path_finder\backend\data\prompts\thinking.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\purpose.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\goals.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\job.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\major.py`, `D:\ANHDUC\Path_finder\backend\data\prompts\uni.py`, `D:\ANHDUC\Path_finder\backend\thinking_graph.py`, `D:\ANHDUC\Path_finder\backend\purpose_graph.py`, `D:\ANHDUC\Path_finder\backend\goals_graph.py`, `D:\ANHDUC\Path_finder\backend\job_graph.py`, `D:\ANHDUC\Path_finder\backend\major_graph.py`, `D:\ANHDUC\Path_finder\backend\uni_graph.py`, `D:\ANHDUC\Path_finder\backend\orchestrator_graph.py`, `D:\ANHDUC\Path_finder\backend\evaluation_graph.py`, `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\python_function_check_how_to_use.md`, `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\python_function_check_shared_stage_profile_utils.md`, `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\python_function_check_orchestrator_policy.md`, `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\python_function_check_stage_helper_matrix.md`, `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\python_function_check_output_and_evaluation_seams.md`, `projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md`, `projects/pathfinder/sources/docs/dev-log/days/2026-04-09.md`
- Why this matters now: the cheapest remaining production risk above the Stage 4 seam was stale or missing Python-owned contracts. The new grouped `python_function_check` workflow makes that layer explicit, and it already surfaced one real backend inconsistency: Thinking could cap single-turn confidence below threshold while leaving `done=True`. That mismatch is now fixed in Python.

## Open Questions
- Question: once the full eval sweep lands, is the higher-leverage next move orchestrator replay or a broader full-path production audit.
- Blocking component: no live blocking runtime debt is currently open at the stage + compiler seam.
- Next check: run the full eval layer on top of the cleaned Stage 4 seam and grouped Python-function checks.

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
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major_eval`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/uni_attack.jsonl --graph uni`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/uni_attack.jsonl --graph uni_eval`

## Handoff
- Latest change: added the repo-local `python_function_check/` workflow with four grouped reports, converted the two legacy helper contract files onto `unittest`, and fixed Thinking's stale post-cap `done` bug by normalizing after verification caps.
- Correction after follow-up: do not call this full-system production readiness. The correct claim is stage + compiler seam readiness only, starting with Thinking.
- Verification completed:
  - `venv\Scripts\python -m unittest test_stage_profile_utils_contract.py`
  - `venv\Scripts\python -m unittest test_orchestrator_graph_contract.py`
  - `venv\Scripts\python -m unittest test_stage_graph_helper_contract.py test_thinking_graph_contract.py test_uni_graph_contract.py`
  - `venv\Scripts\python -m unittest test_evaluation_graph_contract.py test_output_graph_contract.py test_output_prompt_contract.py test_stage_contract.py test_main_contract.py`
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
- Result from the latest run: the confidence contract is now aligned to `> 0.8` lock-safe counting across all six stages, the structured-output warning debt is paid, the grouped `python_function_check` workflow passes across all four buckets, and Thinking no longer preserves `done=True` after single-turn confidence caps pull the profile below threshold.
- Next best action: run the full eval pass on the cleaned backend and treat the resulting failures as the next hardening queue.

## Update Stamp
- Last updated: 2026-04-09
- Owner: Codex
