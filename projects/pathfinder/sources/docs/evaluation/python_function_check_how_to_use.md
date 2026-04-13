# PathFinder Python Function Check

> **TL;DR**: This is the canonical low-cost backend hardening workflow for PathFinder's pure Python seams. Run it before broader replay when routing, reopen invalidation, done normalization, sub-orchestrator maintenance, or stage-to-output glue changed. The current five groups are the baseline, not a frozen limit; broader cheap seam coverage is now official policy.

Last updated: 2026-04-13

`python_function_check` is the deterministic counterpart to the replay-heavy `eval/` workflow.

Test-location rule: all Python contract/regression tests live under `backend/test/`. New tests should be added there and invoked as `backend.test.<module>` with `python -m unittest`; do not add root-level `test_*.py` files.

Use it when the target is Python-owned behavior, not model output:
- stage routing
- counter escalation
- reopen invalidation
- done normalization
- `routing_memory` prune planning
- sub-orchestrator maintenance routing
- stage-helper parity
- evaluation/output seam assembly

Do not use this workflow as a substitute for replay. It is the cheap gate that should run before broader eval.

---

## Purpose

PathFinder now has two evaluation-cost layers:

```text
python_function_check  ->  cheap deterministic seam proof
eval / replay          ->  higher-cost behavior proof
```

The goal of this workflow is to catch backend drift before replay hides the source of a failure.

Typical triggers:
- anchor-stage logic changed
- reopen invalidation changed
- `done` ownership moved deeper into Python
- output/evaluation seam assembly changed
- helper parity across stage graphs is in doubt

---

## Groups

This workflow is currently split into 5 report docs:

1. `python_function_check_shared_stage_profile_utils.md`
2. `python_function_check_orchestrator_policy.md`
3. `python_function_check_stage_helper_matrix.md`
4. `python_function_check_output_and_evaluation_seams.md`
5. `python_function_check_sub_orchestrator_and_memory_lane.md`

Each group owns one deterministic seam family and records the latest command, outcome, and findings.

The grouping is not meant to stay fixed forever. When a new cheap Python-owned seam is important enough to prove separately, broaden this workflow rather than forcing everything back into replay.

---

## Commands

Run from repo root after activating the virtual environment:

```powershell
venv\Scripts\activate
venv\Scripts\python -m unittest backend.test.test_stage_profile_utils_contract
venv\Scripts\python -m unittest backend.test.test_orchestrator_graph_contract
venv\Scripts\python -m unittest backend.test.test_stage_graph_helper_contract backend.test.test_thinking_graph_contract backend.test.test_uni_graph_contract
venv\Scripts\python -m unittest backend.test.test_evaluation_graph_contract backend.test.test_output_graph_contract backend.test.test_output_prompt_contract backend.test.test_stage_contract backend.test.test_main_contract
venv\Scripts\python -m unittest backend.test.test_message_window_contract backend.test.test_sub_orchestrator_graph_contract backend.test.test_sub_orchestrator_focus_eval_contract
```

The contract files above are all `unittest`-compatible. This matters because the original helper tests for Thinking and Uni had been written as bare pytest-style functions, which meant `python -m unittest ...` silently skipped them until they were converted.

---

## When To Use It

Use `python_function_check` first when:
- a refactor changed Python-owned behavior
- replay already passes but you still do not trust the seam
- you want the narrowest failing layer before touching prompts again

Use replay first only when the seam is already trusted and the question is about model behavior or visible response quality.

---

## Completion Rule

A Python-function-check pass is complete only when:
- all 5 group commands ran
- each report doc records the exact command and outcome
- any surfaced backend bug is either fixed or left explicitly open in the matching report
- live context and dev logs are updated if the result changes the next production move

Clean command output alone is not completion. The report docs are the durable record.
