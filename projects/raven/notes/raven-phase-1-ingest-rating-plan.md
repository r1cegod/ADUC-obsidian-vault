---
type: note
title: Raven Phase 1 Ingest Rating Plan
created: '2026-04-16'
updated: '2026-04-16'
tags:
  - project/raven
  - planning
  - ingest
  - evaluation
status: active
lang: en
feeds_into:
  - projects/raven/README.md
---
> **TL;DR**: Raven Phase 1 should be a metadata-only discovery and rating loop: query enrichment -> Reddit/YouTube metadata fetch -> normalized candidates -> automatic rating -> human audit -> saved disagreement. The evolver remains a placeholder graph until audit data exists.

## User-Proposed Shape

```text
Broad ingest target
  ↓
Query enrichment
  ↓
Reddit + YouTube metadata fetch
  ↓
Rater
  ↓
Human audit
  ↓
Saved rating result
```

Second graph:

```text
Start
  ↓
Evolver placeholder
  ↓
End
```

## Phase Split

### Phase 1A - Discovery And Rating Graph

Goal: prove Raven can search public surfaces, normalize candidates, and rank likely signal before reading full raw content.

```text
IngestTarget
  ↓
QueryEnricher
  ↓
FetchYouTubeMetadata
  ↓
FetchRedditMetadata
  ↓
NormalizeCandidates
  ↓
RateCandidates
  ↓
ReviewPacket
  ↓
HumanAudit
  ↓
AuditRecord
```

Minimum candidate schema:

```text
id
source
query
title
description_or_body_preview
link
author_or_channel
published_at
source_metric
raw_metadata
```

Minimum rating schema:

```text
candidate_id
score
label
reason_codes
one_sentence_reason
uncertainty
```

Human audit records:

```text
candidate_id
raven_score
human_score
human_label
human_notes
accepted
created_at
```

## Phase 1B - Evolver Placeholder Graph

Goal: reserve the self-upgrading architecture without pretending the detector can learn before enough audits exist.

```text
AuditRecord batch
  ↓
EvolverPlaceholder
  ↓
No-op summary
```

The placeholder should only report:

- number of audited candidates
- top disagreement patterns
- missing rating criteria
- whether enough audit data exists to propose a detector change

It should not rewrite prompts, rubrics, or code yet.

## Storage Decision

The vault is Raven's primary memory and durable knowledge layer. SQLite is the agent workbench for structured operational state, not the final brain.

```text
Obsidian vault
  ↓
primary durable memory, synthesis, detector evolution notes

SQLite
  ↓
local structured work state for runs, candidates, ratings, audits, replayable disagreement

JSONL
  ↓
append-only run evidence when useful
```

Practical rule: SQLite holds the current machine-readable loop; the vault holds the meaning extracted from that loop.

## Hard Boundary

Phase 1 should not ingest transcripts, Reddit comments, full video details, crawler output, public synthesis, or broad vault memory automation. Those belong after the metadata ranker proves the first detector loop.

```text
metadata first
  ↓
ranking disagreement
  ↓
explicit detector labels
  ↓
vault synthesis
  ↓
then raw content
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
  "ratings": [],
  "review_packet": []
}
```

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
