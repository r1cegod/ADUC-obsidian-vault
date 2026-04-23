---
type: note
title: Raven Phase 1 Ingest Rating Plan
created: '2026-04-16'
updated: '2026-04-22'
tags:
  - project/raven
  - planning
  - ingest
  - evaluation
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - projects/raven/notes/raven-architecture-hub.md
  - projects/raven/notes/raven-evaluation-domain.md
---
> **TL;DR**: Raven Phase 1 is now a metadata-only discovery and Tier 1 filtering loop: query enrichment -> YouTube/Reddit metadata fetch -> normalized candidates -> Tier 1 ranker -> markdown audit -> human audit -> prompt evolution. The evolver remains evidence-backed and human-gated.

## Current Phase 1 Shape

```text
Broad ingest target
  -> Query enrichment
  -> Reddit + YouTube metadata fetch
  -> Tier 1 ranker
  -> Markdown audit file
  -> Human audit
  -> Saved disagreement / dataset
  -> Prompt evolution later
```

Second graph:

```text
Start
  -> Evolver placeholder
  -> End
```

## Phase 1A - Discovery And Tier 1 Filter Graph

Goal: prove Raven can search public surfaces, normalize candidates, and learn Duc's title-level attraction pattern before reading raw content.

```text
IngestTarget
  -> QueryEnricher
  -> FetchYouTubeMetadata
  -> FetchRedditMetadata
  -> NormalizeCandidates
  -> Tier1Ranker
  -> AuditMarkdown
  -> HumanAudit
  -> AuditRecord
```

Minimum candidate schema:

```text
candidate_id
source
query
title
description_or_preview
link
author_or_channel
published_at
source_metric
raw_metadata
```

Tier 1 output contract:

```text
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

Human audit surface:

```text
Title
Description_or_preview
Raven output
Human audit line
```

## Tier 1 Law

Tier 1 is not a truth engine.

```text
Tier 1
  = metadata-only AI filter
  = title + description_or_preview
  = "would Duc click this?"
  = cheap attention triage
```

Do not reintroduce score theater here.

## Phase 1B - Evolver Placeholder Graph

Goal: reserve the self-upgrading architecture without pretending the detector can learn before enough audited evidence exists.

```text
Audit file batch
  -> EvolverPlaceholder
  -> No-op summary
```

The placeholder should only report:

- number of audited candidates
- top disagreement patterns
- missing prompt criteria
- whether enough evidence exists to propose a prompt change

It should not rewrite prompts, rubrics, or code autonomously.

## Evaluation Pipeline

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

This evaluation loop follows the vault-grow rule:

```text
vault notes
  -> durable AI context

canvas
  -> human planning mirror
```

## Storage Decision

The vault is Raven's primary memory and durable knowledge layer. SQLite is the agent workbench for structured operational state, not the final brain.

```text
Obsidian vault
  -> primary durable memory
  -> workflow docs
  -> reports
  -> prompt/eval insight

SQLite
  -> local structured work state for runs, queries, candidates, Tier 1 outputs

repo eval/
  -> executable evidence only
```

Practical rule: SQLite holds the current machine-readable loop; the vault holds the meaning extracted from that loop.

## Hard Boundary

Phase 1 should not ingest transcripts, Reddit comments, full video details, crawler output, public synthesis, or broad vault-memory automation.

```text
metadata first
  -> audit disagreement
  -> prompt evolution
  -> then deeper content later
```

## First Backend Contract

Input:

```text
{"target": "how to find leads", "max_results_per_platform": 10}
```

Output:

```text
{
  "target": "how to find leads",
  "queries": ["how to find leads", "lead automation", "B2B lead generation workflow"],
  "candidates": [],
  "tier1_outputs": [],
  "audit_packet_path": ""
}
```

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-architecture-hub]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
