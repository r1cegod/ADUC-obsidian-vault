---
type: note
title: Raven Source Ranker Draft
created: '2026-04-21'
updated: '2026-04-26'
tags:
  - project/raven
  - draft
  - ranking
  - metadata
  - architecture
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-prompt-hub.md
  - projects/raven/notes/raven-evaluation-hub.md
  - projects/raven/notes/raven-phase-1-ingest-rating-plan.md
  - projects/raven/notes/raven-bs-detector-ingestion-architecture.md
---
> **TL;DR**: Raven Tier 1 is a metadata-only source filter. It reads title + description_or_preview and answers one question: `would Duc click this?` The point is cheap, auditable taste-ingestion, not truth judgment.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-prompt-hub]] and [[projects/raven/notes/raven-evaluation-hub]]
- Node role: prompt/evaluation draft leaf
- First parent link: [[projects/raven/notes/raven-prompt-hub]]
- Growth trigger: update when Tier 1 prompt contract, output shape, audit loop, or metadata-only boundary changes.
- Forbidden contents: raw transcripts, full articles, Reddit comments, runner scripts, per-run traces, and score-heavy contracts.
- Source/evidence boundary: this page owns the durable Tier 1 contract; executable evidence and raw audit artifacts stay in repo `eval/` or the active backend workspace.

## Scope

```text
Tier 1 source ranker
  = metadata-only AI filter
  = title + description_or_preview
  = early attention triage
  = first taste-ingestion layer
```

Allowed inputs:

```text
source
query
platform_id
title
description_or_preview
link
author_or_channel
published_at
source_metric
query_origin
```

Forbidden inputs in this phase:

```text
full transcript
full article body
Reddit comments
YouTube comments
full video details dump
broad crawler output
```

## Why No Raws

```text
metadata filter first
  -> disagreement audit
  -> prompt evolution
  -> detector clarity
  -> only then deeper ingest later
```

If raws enter too early, Raven can fake intelligence by leaning on content volume instead of learning judgment.

## Tier 1 Job

Tier 1 does not answer whether a source is true.

It answers:

```text
would Duc click this?
```

So this is not a truth engine.
It is not deep evaluation.
It is cheap attention triage.

## Current Contract Direction

Current stacked decisions:

```text
1. Tier 1 is metadata-only attention triage
2. optimize for why Duc would click
3. use title + preview, not title alone
4. split title judgment from preview judgment
5. avoid numeric scoring in Tier 1
6. prefer readable structured strings over clever builders
7. keep input budget pressure in the prompt/eval contract, not hidden code truncation
8. call the high model once on appended delegation blocks, not once per candidate
9. name the join node `ranker_tier1_final`, because it is the final selector for Tier 1 triage, not Raven's final truth ranker
10. use LangGraph `Send` fan-out for cheap parallel Tier 1 candidate scoring
11. keep the production Tier 1 prompt under 1000 tokens
12. keep the evolution loop outside the prompt, in the trace-to-markdown eval script and Duc audit artifact
13. keep the human audit surface minimal
14. evolve through evaluation runs, not ad hoc rewrites
```

## Input Contract

```text
Tier1Candidate
  candidate_id
  run_id
  query_id
  source
  query
  platform_id
  title
  description_or_preview
  link
  author_or_channel
  published_at
  source_metric
  raw_metadata
```

`raw_metadata` here means API response fragments needed for replay or debugging, not raw third-party content.

## Output Contract

Current output is compact and string-first:

```text
Tier1Rating
  candidate_id
  sexy_label
  reasoning
  tier_version
  created_at
```

Runtime currently stores `reasoning` in the existing `final_verdict` DB field to avoid schema churn during the draft loop. The old positive/negative pull fields remain in the table for now but are not part of the active prompt output.

Starter label set:

```text
skip
maybe
click
must_click
```

Why this split exists:

```text
title_pull
  = what in the title creates attraction or repulsion

preview_pull
  = how the preview reinforces or weakens the click impulse

final_verdict
  = combined natural-language click judgment
```

## Reason-Code Shape

Current agreed reason-code shape:

```text
positive_pull[]
negative_push[]
```

Meaning:

```text
positive_pull
  = attraction mechanisms

negative_push
  = repulsion mechanisms
```

Starter positive directions:

```text
novel_angle
concrete_outcome
specific_mechanism
operator_energy
clear_pain
curiosity_gap
failure_mode
buildable_workflow
decision_leverage
```

Starter negative directions:

```text
guru_fluff
generic_topic
status_bait
fake_specificity
empty_preview
overclaimed_result
no_mechanism
entertainment_only
generic_motivation
```

## Prompt Contract

Lock this as a production-shaped prompt contract, not a loose instruction list:

```text
1. named ranker identity
2. in-scope / out-of-scope boundary
3. single task: would Duc click from metadata only?
4. input contract: title + description_or_preview only
5. output contract: sexy_label, positive_pull[], negative_push[], title_pull, preview_pull, final_verdict
6. grounding rules: no raws, no outside knowledge, no popularity shortcut
7. calibration examples for high-signal, hype, and thin relevance
8. eval/evolution path: run -> trace -> human audit -> dataset -> rerun
9. guardrails against metadata prompt injection
```

Prompt posture:

```text
would Duc click this?
```

Not:

```text
estimate generic click desirability
```

## Audit Artifact

Current audit packet direction:

```text
one markdown file per eval run
```

Current audit markdown schema:

```text
Title
Description_or_preview
Raven output
Human audit line
```

Meaning:

```text
show the candidate
show the full ranker output
then let Duc answer in plain language
```

No extra explanation layer is required.

## Evolution Loop

Use one evaluation pipeline only. Keep this loop outside the production prompt:

```text
ranker runs
  -> trace JSON
  -> eval script renders markdown audit file
  -> Duc audit lines
  -> Codex reads the audit file
  -> dataset update
  -> prompt audit / prompt upgrade
  -> rerun until the filter is good enough
```

That means Tier 1 evolves through the script + audit artifact, not by teaching the ranker about its own evolution process.

Current evaluation state: [[projects/raven/notes/raven-tier-1-ranker-evaluation]] records synthetic Tier 1 8/8, focused Duc-audited `how to find leads` Tier 1 4/4, and Tier 1 final synthetic 1/1. The full 17-candidate drift check improved Tier 1 from all-skip to 5 promoted rows, but final selector still needs live calibration.

Automation boundary:

```text
automatic
- run Tier 1
- render audit markdown
- create/update dataset from the audit
- audit prompt against the dataset

human gate
- audit labels
- approve the next tier version
```

## Token Budget Shape

The runtime architecture should avoid high-model fanout:

```text
candidate metadata
  -> LangGraph Send fan-out
  -> title + preview prompt under 1000-token system prompt
  -> cheap Tier 1 model per candidate
  -> reducer-backed done results
  -> append readable PACKET blocks
  -> one high-model ranker_tier1_final selector per run
```

Current runtime shape:

```text
PACKET = """<candidate>
candidate_id: {candidate_id}
tier1_query: {query}
tier1_label: {sexy_label}
title: {title}
tier1_reasoning: {final_verdict}
</candidate>"""

packet += PACKET.format(...)
```

Enricher, Tier 1, and Tier 1 final currently run at temperature `0.7` during the live calibration loop.

No hidden code-side truncation or compact builder should sit between the row and the selector. Token-budget pressure belongs in the prompt/eval contract unless Duc explicitly approves code-side trimming.

The high model decides only:

```text
keep
throw_out
short reason
```

No `maybe`, no rank. If the final selector is uncertain, it throws out; the next search run can rediscover similar material.

This preserves the cheap taste-ingestion layer while preventing expensive final ranking from scaling with every candidate.

## Promotion Boundary

Tier 1 itself should not write straight into the vault.

```text
ranker output
  -> SQLite rating row
  -> human audit
  -> promotion decision later
```

This prevents the vault from filling with unverified first-pass impressions.

## Vault-Grow Rule

This draft follows the vault-grow rule:

```text
vault notes
  -> AI context
  -> durable memory of the draft and eval loop

canvas
  -> human context
  -> live planning mirror for the session
```

One session should usually update both.

## Canvas Status

As of 2026-04-24, `projects/raven/notes/raven-feature-web.canvas` has a Tier 1 ranker draft node in the live ranking area.

```text
persisted candidate rows
  -> Tier 1 ranker draft node
  -> Tier1Rating row
```

The node remains draft/unfinished: it represents the next architecture seam after the verified YouTube-to-SQLite bridge, not completed runtime code.

## Draft Verdict

Phase 1 Raven needs a Tier 1 source ranker, not a truth engine.

```text
goal
  = rank what deserves attention
not
  = decide the final truth of the internet
```

## Related

- [[projects/raven/notes/raven-prompt-hub]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-eval-how-to-use]]
- [[projects/raven/notes/raven-evaluation-insights]]
- [[projects/raven/notes/raven-phase-1-ingest-rating-plan]]
- [[projects/raven/notes/raven-bs-detector-ingestion-architecture]]
- [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
- [[projects/raven/README]]
