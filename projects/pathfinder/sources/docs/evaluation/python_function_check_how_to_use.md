# PathFinder Python Function Check

> **TL;DR**: This is the canonical low-cost backend hardening workflow for PathFinder's pure Python seams. Run it before broader replay when routing, reopen invalidation, done normalization, or stage-to-output glue changed.

Last updated: 2026-04-09

`python_function_check` is the deterministic counterpart to the replay-heavy `eval/` workflow.

Use it when the target is Python-owned behavior, not model output:
- stage routing
- counter escalation
- reopen invalidation
- done normalization
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

This workflow is split into 4 report docs:

1. `python_function_check_shared_stage_profile_utils.md`
2. `python_function_check_orchestrator_policy.md`
3. `python_function_check_stage_helper_matrix.md`
4. `python_function_check_output_and_evaluation_seams.md`

Each group owns one deterministic seam family and records the latest command, outcome, and findings.

---

## Commands

Run from repo root after activating the virtual environment:

```powershell
venv\Scripts\activate
venv\Scripts\python -m unittest test_stage_profile_utils_contract.py
venv\Scripts\python -m unittest test_orchestrator_graph_contract.py
venv\Scripts\python -m unittest test_stage_graph_helper_contract.py test_thinking_graph_contract.py test_uni_graph_contract.py
venv\Scripts\python -m unittest test_evaluation_graph_contract.py test_output_graph_contract.py test_output_prompt_contract.py test_stage_contract.py test_main_contract.py
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
- all 4 group commands ran
- each report doc records the exact command and outcome
- any surfaced backend bug is either fixed or left explicitly open in the matching report
- live context and dev logs are updated if the result changes the next production move

Clean command output alone is not completion. The report docs are the durable record.
