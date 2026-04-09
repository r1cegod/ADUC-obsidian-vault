# Python Function Check - Output And Evaluation Seams

> **TL;DR**: Group 4 covers the cheaper stage-to-output seam around evaluation prep, compiler prompt assembly, output sanitization, queue tagging, and shared stage naming. It now passes cleanly.

Last updated: 2026-04-09

## Scope

- Files:
  - `backend/evaluation_graph.py`
  - `backend/output_graph.py`
  - `backend/data/prompts/output.py`
  - `backend/data/contracts/stages.py`
  - `main.py`

## Command

```powershell
venv\Scripts\python -m unittest test_evaluation_graph_contract.py test_output_graph_contract.py test_output_prompt_contract.py test_stage_contract.py test_main_contract.py
```

## Expected Proof

- evaluation prep seeds the right messages and stage defaults
- compiler prompt assembly stays Python-owned
- output compiler tags only the intended stage queues
- output sanitization strips unsupported characters without damaging readable text
- shared stage naming and frontend serialization stay aligned

## Latest Result

- Status: Pass
- Run date: 2026-04-09
- Result: `Ran 15 tests ... OK`

## Notes

- This group protects the cheapest visible-response seam below full replay.
- It now covers both context-compiler delegation and output sanitization in addition to the earlier queue-tagging and stage-contract checks.
