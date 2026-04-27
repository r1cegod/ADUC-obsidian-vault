---
type: note
title: Raven Tier 1 Ranker Evaluation
created: '2026-04-26'
updated: '2026-04-26'
tags:
  - project/raven
  - evaluation
  - prompts
  - backend
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-evaluation-hub.md
  - projects/raven/notes/raven-evaluation-insights.md
  - projects/raven/notes/raven-prompt-hub.md
---
> **TL;DR**: Raven Tier 1 now has a synthetic contract gate and a focused Duc-audited live gate. Current prompt is 875/1000 tokens, runs at temperature `0.7`, passes synthetic Tier 1 8/8, and passes the focused `how to find leads` audited dataset 4/4. The full 17-candidate drift check is improved but not production-stable because Tier 1 final still needs calibration.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-evaluation-hub]]
- Node role: report leaf
- First parent link: [[projects/raven/notes/raven-evaluation-hub]]
- Growth trigger: update when the Tier 1 ranker prompt gate, eval dataset, trace audit, or readiness decision changes.
- Forbidden contents: runner source code, raw JSON traces, full datasets, and unrelated search/writeback evidence.
- Source/evidence boundary: this page stores the human-readable report; executable evidence remains under `/home/r1ceg/Raven/eval/`.

## Evaluation Target

```text
candidate title + description_or_preview
  -> Tier 1 ranker prompt
  -> structured output
  -> click-worthiness audit
```

The ranker is metadata-only. It does not inspect transcripts, comments, article bodies, thumbnails, author history, or live web content.

## Prompt Contract Tested

Required output shape:

```text
sexy_label
reasoning
```

Required behavior:

```text
- label must be skip / maybe / click / must_click
- reasoning must be short, plain-English, and bounded
- high-signal metadata should surface mechanism, workflow, failure mode, source angle, or decision leverage
- weak metadata should still be rejected when it is pure hype, generic motivation, status bait, or missing mechanism
- acquisition/lead-generation rows must follow Duc-audited calibration: LinkedIn scraping can survive n8n penalty; lead-gen mistake diagnosis is at least maybe; exact systems / qualified leads / Facebook Ads lead generation can be click
```

## Production Formula Applied

The prompt was refactored from a flat instruction block into the production-grade shape captured in [[wiki/synthesis/evaluation-production-prompt-domain]]:

```text
identity
  -> scope
  -> task
  -> input contract
  -> output contract
  -> reasoning compression
  -> grounding rules
  -> calibration examples
  -> evolution path
  -> guardrails
```

This matters because Tier 1 is a judgment task. A list of rules can pass a toy eval, but production prompt shape is what keeps the model bounded when live metadata becomes messy.

## Executable Evidence

Repo evidence:

```text
/home/r1ceg/Raven/eval/run_ranker_tier1_eval.py
/home/r1ceg/Raven/eval/ranker_tier1_cases.jsonl
/home/r1ceg/Raven/src/backend/data/prompt/ranker_tier1.py
/home/r1ceg/Raven/src/backend/data/prompt/ranker_tier1_final.py
/home/r1ceg/Raven/eval/threads/30cfb4eb-1abe-4cd3-b5d4-d6e36868abaa/traces/
```

Passing command:

```bash
./.venv/bin/python eval/run_ranker_tier1_eval.py
```

Current result after prompt calibration, token gate, and Duc-audited focused loop:

```text
Synthetic Tier 1: 8/8
Thread: 6c3aa212-2f65-476a-9e81-691760613cb7

Focused audited Tier 1, how to find leads: 4/4
Thread: 551d7298-786a-457d-9d08-d96456eea9bc
Dataset: eval/ranker_tier1_how_to_find_leads_audited.jsonl
Prompt tokens: 875/1000

Tier 1 final synthetic: 1/1
Thread: 15b2658f-d896-4d7b-9096-e01dfd8327a4
```

Regression checks:

```text
py_compile: passed
unittest discovery: 3 tests passed
Raven graph import smoke: prompt constants and ranker structured LLM loaded
```

`pytest` was not available in the repo virtual environment, so standard-library `unittest` discovery was used.

## Iteration Log

Round 1:

```text
Passed: 7/8
Thread: 082adf68-72d6-4761-a73f-ac3e72ce6abd
```

Failure cause: evaluator brittleness. The output was behaviorally correct, but the evaluator treated `schema` as a control leak when it was a legitimate database-schema term.

Fix: narrowed the marker from `schema` to `output schema`.

Round 2:

```text
Passed: 8/8
Thread: 8699b14a-6e47-40e2-a831-9a9256f1a3d2
```

Pass was structurally valid, but the prompt was still not shaped by the full production prompt formula.

Round 3:

```text
Passed: 8/8
Thread: 67d3291b-bcd6-4471-99d6-7748cd963a7e
```

Trace audit caught a quality issue: hype/skip cases sometimes received `curiosity_gap` in `positive_pull`. That is not a Raven-positive signal when the curiosity is pure clickbait.

Fix: prompt now says curiosity is positive only when attached to a concrete mechanism, failure mode, workflow, or decision lever. Evaluator now rejects unexpected positive pulls when the expected positive set is empty.

Round 4:

```text
Passed: 8/8
Thread: da73e17f-71e3-4b94-9d46-64a777866a1f
```

Final sampled outputs show high-signal cases receiving mechanism/workflow/failure/decision codes and weak hype/motivation cases receiving empty positive pulls plus negative reason codes.

## Token-Cost Architecture Update

Duc raised the token-burn risk after the synthetic prompt gate, then rejected hidden code-side compacting. The runtime graph now uses a two-stage delegation shape:

```text
cheap Tier 1 per candidate
  -> normal title + preview prompt
  -> strict structured output
  -> SQLite row

high-model final selector once per run
  -> appended readable PACKET blocks
  -> keep / throw_out + short reason
```

Delegation input shape:

```text
<candidate>
candidate_id: ...
tier1_label: ...
title: ...
positive_pull: ...
negative_push: ...
tier1_verdict: ...
</candidate>
```

This keeps the expensive model from scaling linearly with every candidate while keeping the delegation input inspectable. The final selector is now named `ranker_tier1_final`. Runtime uses LangGraph `Send` fan-out from `youtube_search` for parallel Tier 1 candidate scoring, then runs one Tier 1 final selector pass over appended readable `PACKET` blocks. The renamed final-selector eval passed 1/1 with trace `afab31a7-0a65-449f-9dc9-36995c90e9e8`; live-candidate production audit is still not complete.

## Decision

```text
Production ready: NO for full Tier 1 ranking.
Ready for next step: YES for continued focused live-audit calibration.
Tier 1 status: synthetic 8/8 and Duc-audited focused lead-gen 4/4 passed.
Tier 1 final selector status: synthetic 1/1 passed, but live drift check shows it still needs calibration.
```

What is proven:

```text
- structured ranker output works with `gpt-5.4-mini`
- labels and reason codes separate useful mechanism/workflow metadata from hype/generic metadata
- evaluator catches label/code/prose/control-leak regressions
- evaluator now catches fake positive pulls on negative cases
```

What is not proven:

```text
- prompt is stable across broader real YouTube/Reddit metadata distributions
- SQLite writeback quality after all future live graph runs
- high-model final selector behavior on live candidate packets beyond synthetic 1/1
- final selector alignment with Duc's audited live lead-gen taste
- whether the unaudited promoted rows from the full drift check are acceptable
```

## Next Gate

```text
same live candidate rows
  -> current Tier 1 rerank / final selector drift check
  -> inspect promoted rows and final keep/throw_out choices
  -> update final-selector dataset from Duc audit lines
  -> focused final-selector eval rerun
```

Do not run a fresh full graph unless fresh candidates are needed. Do not call Tier 1 production-ready until final selector alignment survives the live focused loop.

## Related

- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-eval-how-to-use]]
- [[projects/raven/notes/raven-evaluation-insights]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-prompt-hub]]
- [[wiki/synthesis/evaluation-production-prompt-domain]]
