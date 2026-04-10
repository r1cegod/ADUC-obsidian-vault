# PathFinder Sub-Orchestrator Focus Eval

Last updated: 2026-04-10

> **TL;DR**: This is the dedicated evaluation workflow for the sub-orchestrator lane only. It runs the `summarizer` and `worker` families directly, never touches the main orchestrator, and follows the same 3-round production gate used elsewhere in PathFinder.

Use this file for:
- sub-orchestrator-only evaluation workflow
- the dedicated focus-eval runner and datasets
- trace locations for `summarizer` and `worker`
- the per-family 3-round production gate

Companion evaluation docs:
- `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\eval_how_to_use.md`
- `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\sub_orchestrator_evaluation.md`

---

## Purpose

This workflow exists for one narrow question:

```text
Did the sub-orchestrator's own prompt and memory-maintenance lane behave correctly,
without replay noise from input_parser, stage routing, counters, or output compilation?
```

Use it when:
- `backend/data/prompts/sub_orchestrator.py` changed
- `backend/sub_orchestrator_graph.py` changed
- `routing_memory` summarization or worker refresh behavior changed
- you want to harden prompt behavior without touching `input_orchestrator`

Do not use it as a substitute for full replay. It is a focused seam audit.

---

## Targets

There are 2 target families:

- `summarizer`
  - owns compression of retired `routing_memory` into `user_tag_summaries`
  - proves what survives after the memory lane crosses the budget

- `worker`
  - owns refresh of persistent `user_tag` fields from current `routing_memory` plus carried summaries
  - proves bool/text updates without replaying the main orchestrator

Each family has its own 3-round production gate.

---

## Round Gate

Production-ready is per family, not for the whole lane at once.

Rules:
- `summarizer` gets at most 3 rounds
- `worker` gets at most 3 rounds
- after each round, stop and hand over the updated audit log
- do not silently continue to Round 2 or Round 3 without a user review step

Minimum shape:
- Round 1: first hardening pass
- Round 2: follow-up after observed drift and user review
- Round 3: final confirmation pass

If a family is still unstable after Round 3, it is not production ready.

---

## Runner

Run from repo root after activating the venv:

```powershell
venv\Scripts\activate
venv\Scripts\python eval/run_sub_orchestrator_focus_eval.py --target summarizer --file eval/sub_orchestrator_summarizer_focus.jsonl --mode single
venv\Scripts\python eval/run_sub_orchestrator_focus_eval.py --target worker --file eval/sub_orchestrator_worker_focus.jsonl --mode single
```

Optional flags:
- `--mode single|multi`
- `--workers <int>` for `multi`

This runner calls the sub-orchestrator focus graphs directly:
- `summarizer` -> limit check + summary chain only
- `worker` -> router + worker chain only

It does not call:
- `backend/orchestrator_graph.py`
- `input_parser`
- `stage_manager`
- `counter_manager`

---

## Dataset Contract

Each JSONL row overlays `backend.data.state.DEFAULT_STATE`.

Supported top-level eval metadata keys:
- `eval_case`
- `expected_checks`
- `notes`

Supported message queues:
- `routing_memory`
- `messages`

If `routing_memory` is missing and `messages` exists, `messages` is mirrored into `routing_memory`.

Compact dataset helper:
- each message object may include `repeat: <int>`
- the runner expands that message content by newline repetition before invocation
- this is mainly for forcing realistic over-budget summarizer cases without giant inline literals

---

## Trace Output

Trace files land in the standard folder:

```text
eval/threads/<thread_id>/traces/run_0001.json
```

Each trace includes:
- `focus_target`
- `eval_metadata`
- `normalized_input`
- `output`
- `status`

Audit the trace content, not just exit code `0`.

For `summarizer`, check:
- `routing_memory_over_limit`
- `user_tag_summaries`
- whether the right signal survived compression

For `worker`, check:
- `selected_agents`
- `user_tag`
- whether the right fields changed and weak fields stayed conservative

---

## Completion Rule

A sub-orchestrator focus-eval task is complete only when:
- the target family and round are written into `sub_orchestrator_evaluation.md`
- the target dataset ran cleanly
- traces were manually audited
- residual risks were recorded
- current context and dev-log mirrors were updated

Exit code alone is not completion.
