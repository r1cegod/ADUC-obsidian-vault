---
type: note
title: Raven Evaluation Insights
created: '2026-04-22'
updated: '2026-05-03'
tags:
  - project/raven
  - evaluation
  - prompts
  - insights
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-evaluation-hub.md
---
> **TL;DR**: Rolling compounding note for what Raven evaluation teaches over time. This page should grow with the vault: prompt insights, failure patterns, audit lessons, and domain-level evaluation strategy shifts.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-evaluation-hub]]
- Node role: rolling insight leaf
- First parent link: [[projects/raven/notes/raven-evaluation-hub]]
- Growth trigger: update when an eval cycle produces a durable cross-run lesson, prompt law, stable failure pattern, or workflow correction.
- Forbidden contents: raw run dumps, full trace summaries, temporary failures, and per-run report detail.
- Source/evidence boundary: cross-run lessons live here; executable evidence and raw traces remain in repo `eval/`, and per-run truth belongs in report leaves.

## Purpose

This is the compounding memory layer for Raven evaluation.

```text
run finishes
  -> what did Raven learn?
  -> what did Duc learn?
  -> what should change next time?
```

Reports tell you what happened.
This note tells you what now belongs to the system.

## Current Durable Insights

### Eval Operations

- `daily eval` means run the Raven full graph first and create a fresh packet; it is not a vault-only status summary.
- Focused node/dataset evals are Phase 2: they start from Duc audit lines or inspected failures, then rerun until the current dataset standard is met.
- A passing daily full graph with blank Duc audit lines creates audit evidence, not an automatic prompt/dataset patch.
- Focused datasets must track the current request-era schema. Old query-era rows without `request` are not meaningful failures; they are migration debt.
- Daily eval candidate counts are not comparable while `raven_candidates` suppresses previously seen videos globally. Eval isolation or run-local candidate identity must come before search/prompt tuning.

### YouTube Search / Candidate Evidence

- Low candidate counts can be a storage artifact, not a search artifact. On 2026-05-03, direct YouTube diagnostics found dozens of filter-passing results for the daily queries, while the packet showed only 11 candidates because global `UNIQUE(source, platform_id)` / `link UNIQUE` suppressed videos already stored by earlier runs.
- Best route: make candidates run-local first, then add a source-history layer later if needed. Do not use global candidate uniqueness as a substitute for source memory.
- Query tuning should happen after storage semantics are fixed. Initial high-volume query families for YouTube growth are `small youtube channel growth`, `youtube channel mistakes`, and `youtube growth case study`.

### Tier 1 Ranker

- Tier 1 is a metadata-only attention filter, not a truth engine.
- Tier 1 optimizes for `why Duc would click`, not generic click desirability.
- Numeric scoring is unnecessary at this layer; string-rich judgment is preferred.
- Current output shape is centered on `sexy_label`, `positive_pull[]`, `negative_push[]`, `title_pull`, `preview_pull`, and `final_verdict`.
- One markdown file per eval run is the preferred audit artifact shape.
- The human audit surface should stay minimal: title, preview, Raven output, and one plain-language Duc audit line.
- Prompt evolution should follow the evidence loop: run -> audit file -> human audit -> dataset -> prompt audit -> rerun.
- Production-grade prompt shape matters: identity, scope, task, input contract, output contract, grounding, examples, evolution path, and guardrails should be explicit before calling a prompt production-like.
- Evaluators must not let clickbait curiosity count as positive signal. For negative/hype cases, `positive_pull[]` should be empty unless there is a real useful signal being outweighed.
- Control-leak markers must be context-aware. A broad marker like `schema` can create false failures when the candidate legitimately mentions a database schema.

## How To Use This Note

Add to this page when a run produces durable insight such as:

```text
- a prompt law
- a stable failure pattern
- an audit heuristic
- a better evaluation loop rule
- a permanent boundary or anti-pattern
```

Do not dump raw run summaries here. Those belong in the report layer.

## Growth Law

```text
report
  -> per-run truth

insights note
  -> cross-run compounding truth
```

If this page stops growing, the evaluation domain is not compounding.

## Related

- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-eval-how-to-use]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-enricher-evaluation]]
- [[projects/raven/README]]
