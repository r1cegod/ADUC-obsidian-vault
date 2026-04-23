---
type: note
title: Raven Source Ranker Draft
created: '2026-04-21'
updated: '2026-04-22'
tags:
  - project/raven
  - draft
  - ranking
  - metadata
  - architecture
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - projects/raven/notes/raven-phase-1-ingest-rating-plan.md
  - projects/raven/notes/raven-bs-detector-ingestion-architecture.md
  - projects/raven/notes/raven-prompt-hub.md
  - projects/raven/notes/raven-evaluation-domain.md
---
> **TL;DR**: Raven Tier 1 is a metadata-only source filter. It reads title + description_or_preview and answers one question: `would Duc click this?` The point is cheap, auditable taste-ingestion, not truth judgment.

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
6. prefer richer string outputs over precision theater
7. keep the human audit surface minimal
8. evolve through evaluation runs, not ad hoc rewrites
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

Current output is string-first:

```text
Tier1Rating
  candidate_id
  sexy_label
  positive_pull[]
  negative_push[]
  title_pull
  preview_pull
  final_verdict
  tier_version
  created_at
```

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
```

Starter negative directions:

```text
guru_fluff
generic_topic
status_bait
fake_specificity
empty_preview
overclaimed_result
```

## Prompt Contract

Lock this as one thing:

```text
1. prompt speaks in direct taste language
2. prompt judges why Duc would click
3. prompt explains title pull in natural language
4. prompt explains preview pull in natural language
5. prompt emits final sexy_label
6. prompt emits positive_pull[] and negative_push[]
7. prompt emits final_verdict
8. prompt stays metadata-only
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

Use one evaluation pipeline only:

```text
ranker runs
  -> trace + markdown audit file
  -> Duc audit
  -> Codex reads the audit file
  -> Codex creates dataset from the audit
  -> prompt audit / prompt upgrade
  -> rerun until the filter is good enough
```

That means Tier 1 evolves through evaluation runs, not ad hoc vibes.

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
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-eval-how-to-use]]
- [[projects/raven/notes/raven-evaluation-insights]]
- [[projects/raven/notes/raven-phase-1-ingest-rating-plan]]
- [[projects/raven/notes/raven-bs-detector-ingestion-architecture]]
- [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
- [[projects/raven/README]]
