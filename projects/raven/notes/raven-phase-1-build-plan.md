---
type: note
title: Raven Phase 1 Build Plan
created: '2026-04-16'
updated: '2026-04-16'
tags:
  - project/raven
  - planning
  - backend
  - sqlite
  - evaluation
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - projects/raven/notes/raven-phase-1-ingest-rating-plan.md
---
> **TL;DR**: Build Raven Phase 1 as four connected working slices: Reddit/YouTube search -> query enricher -> rater -> evolver placeholder. Let persistence/schema details grow from the working loop, but keep each slice's input/output contract explicit.

## Build Shape

```text
User target
  ↓
1. Reddit + YouTube search function
  ↓
2. Query enricher
  ↓
3. Rater
  ↓
4. Evolver placeholder
  ↓
Vault synthesis later
```

Phase 1 is not a full research agent. It is a source discovery and judgment loop.

## Storage Boundary

```text
Vault
  ↓
primary memory, final synthesis, detector evolution notes

SQLite
  ↓
agent workbench for runs, candidates, ratings, audits
```

Do not over-design the database first. Add tables when a working slice needs persistence.

## Phase 1 - Reddit And YouTube Search Function

Goal: one callable function that accepts a query and returns normalized metadata candidates from both platforms.

```text
search_sources(query, limit)
  -> list[SourceCandidate]
```

Candidate should contain at minimum:

```text
source
platform_id
title
description_or_preview
link
author_or_channel
published_at
source_metric
raw_metadata
```

Build order:

```text
fake searcher
  ↓
normalizer
  ↓
real YouTube search
  ↓
real Reddit search
```

Acceptance:

- fake search works without API keys
- Reddit and YouTube return the same internal shape
- source links are usable
- no transcripts, comments, or raw full-content ingestion yet

## Phase 2 - Query Enricher

Goal: turn broad target text into multiple search queries.

```text
expand_query("how to find leads")
  -> [
    "how to find leads",
    "lead automation",
    "B2B lead generation workflow",
    "cold outreach lead sourcing",
    "founder lead generation system"
  ]
```

Then wire it:

```text
target
  ↓
expand_query
  ↓
search_sources for each query
  ↓
deduped candidates
```

Acceptance:

- broad targets produce specific variants
- exact user target is always preserved
- duplicate links collapse
- output still fits the same candidate schema

## Phase 3 - Rater

Goal: score metadata candidates before reading full content.

```text
rate_candidate(candidate)
  -> CandidateRating
```

Rating output:

```text
candidate_id
score
label
reason_codes
one_sentence_reason
uncertainty
```

Initial labels:

```text
bullshit
weak
useful
high_signal
```

Initial reason codes:

```text
specific_mechanism
operational_detail
named_tools_or_numbers
clear_failure_mode
vague_abstraction
guru_fluff
recycled_consensus
low_build_relevance
```

Acceptance:

- every candidate gets a rating
- ratings sort into a review packet
- reasons are inspectable by Duc
- human audit can disagree with Raven

## Phase 4 - Evolver Placeholder

Goal: connect the self-upgrade graph without pretending Raven can improve itself yet.

```text
ratings + human audits
  ↓
evolver_placeholder
  ↓
disagreement summary
```

Allowed output:

```text
audited_count
disagreement_patterns
missing_criteria
enough_data_to_evolve
```

Forbidden in Phase 1:

```text
automatic prompt rewrite
automatic rubric rewrite
automatic code rewrite
```

Acceptance:

- evolver consumes real audit data
- evolver summarizes disagreement
- evolver makes no autonomous changes

## First Usable End-To-End Demo

```text
Input:
  "how to find leads"

Output:
  expanded queries
  Reddit + YouTube candidates
  Raven ratings
  sorted review packet
  placeholder evolver summary
```

This is the first working Raven loop.

## Non-Goals

- no frontend-first build
- no full crawler
- no transcripts
- no Reddit comments
- no public synthesis yet
- no autonomous self-upgrade
- no Postgres
- no durable storage of full third-party content

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-phase-1-ingest-rating-plan]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
