---
type: project
title: Raven
created: '2026-04-15'
updated: '2026-04-22'
tags:
  - project/raven
  - ai
  - knowledge
  - evaluation
  - distribution
status: incubating
priority: high
lang: en
feeds_into:
  - context/now.md
  - context/goals.md
---
> **TL;DR**: Raven is the candidate next scaffold after PathFinder: a Knowledge Signal Engine that formalizes Duc's internal bullshit detector into source scoring, claim extraction, insight filtering, vault memory, and public synthesis.

## Core Thesis

Raven is not a passive knowledge absorber. It is a judgment engine.

```text
public source
   ↓
claim extraction
   ↓
bullshit detection
   ↓
insight scoring
   ↓
vault memory
   ↓
public synthesis
```

The main asset to formalize is Duc's internal bullshit detector: currently fast, intuitive, and brain-native, but not inspectable, repeatable, or delegable to agents.

## Bullshit Detector Problem

Duc can often sense when a source is fake, vague, guru-fluff, derivative, or non-actionable. The problem is that the detector is tacit.

```text
inside brain
   ↓
fast judgment
   ↓
no explicit labels
   ↓
agent cannot reproduce it
```

Raven's first job is to turn that tacit detector into explicit criteria.

## First Detector Axes

Reject or penalize sources/claims with:

- vague abstractions without concrete mechanism
- no lived experience or operational detail
- no cost, pain, risk, time, money, status, or tradeoff
- advice that survives because it sounds good, not because it predicts reality
- recycled consensus with no new angle
- emotional certainty without evidence trail
- claims that cannot change a build decision

Reward sources/claims with:

- specific failure modes
- concrete workflow details
- named tools, constraints, numbers, or examples
- repeated pain across independent sources
- falsifiable claims
- buildable implications within 7-14 days
- public artifact potential

## Product Shape

Minimum useful loop:

```text
source URL
   ↓
extract claims
   ↓
score each claim
   ↓
label bullshit / weak / useful / high-signal
   ↓
write vault note
   ↓
generate public artifact draft
```

## Distribution Angle

Raven should produce publishable artifacts from its own work:

- signal briefs
- failure analyses
- build logs
- pain maps
- "what the internet is wrong about" posts

The distribution proof is not that Duc consumes more content. The proof is that Raven makes Duc's taste visible.

## Implementation Status

- Local repo: `/home/r1ceg/Raven`
- Remote repo: `git@github.com:r1cegod/Raven.git`
- Current remote status: `main` was force-pushed from old CLI/rubric commit `94632ee` to clean scaffold commit `128ff88 Project initialized`.
- Current repo shape: root `AGENTS.md`, root `README.md`, `logs/DEV_LOG.md`, `requirements.txt`, `docs/reference/`, and active backend files under `src/backend/`.
- Active backend status 2026-04-20: SQLite foundation exists in `src/backend/db.py`; active YouTube `search.list` + first normalization pass exists in `src/backend/search/youtube_search.py`; production-ready one-node `gpt-5.4-mini` query enricher prompt/graph and eval gate exist in `src/backend/Raven_graph.py`, `src/backend/data/prompt/enricher.py`, and `eval/`.
- Reference-only code: generated full-pipeline/API examples are parked under `docs/reference/` and must not be treated as production implementation.
- Removed from active scaffold: old CLI, rubric, models, examples, uv project files, and generated smoke data.
- Local ignored files: `.env`, `.venv/`, SQLite runtime files, and scratch/editor files remain untracked.

## Next Action

Phase 1 build order is now defined in [[projects/raven/notes/raven-phase-1-build-plan]], grounded in [[projects/raven/notes/raven-phase-1-ingest-rating-plan]]. Current immediate seam:

```text
enriched query
   -> YouTube search result
   -> query log row
   -> candidate row(s)
   -> joined DB readback
```

After that, continue to Reddit search, rater, then evolver placeholder. Keep the vault as primary memory and SQLite as the agent workbench. Let schema/persistence grow from the working loop instead of designing a large database upfront.

## Architecture Router

Visual planning and architecture work now route through [[projects/raven/notes/raven-architecture-hub]], using the vault-wide [[wiki/synthesis/obsidian-d2-canvas-architecture-method]] as the operating method.

Rule in this scope:

```text
system-level Raven architecture decisions
  -> go through Canvas first

function-local code planning
  -> stays out of Canvas unless it changes architecture shape
```

Official structuring rule:

```text
architecture change stabilizes
  -> reflect it in Raven project routing
  -> give it an official home
  -> do not leave it only in chat or only on Canvas
```

Current active architecture threads:
- [[projects/raven/notes/raven-vault-keeper-harness-architecture]] for how Raven as vault keeper uses the vault through ingestion, promotion, and retrieval
- [[projects/raven/notes/raven-source-ranker-draft]] for the Tier 1 metadata-only filter, prompt contract, and evaluation loop that ingest Duc's taste through audit evidence

## Evaluation Domain Rule

Raven evaluation reports, audit logs, and production-readiness decisions are vault-canonical. Repo `eval/` is only for executable evidence: runner scripts, JSONL datasets, traces, and temporary reproduction artifacts.

Router: [[projects/raven/notes/raven-evaluation-domain]]

## Build Ownership Rule

Raven uses an ownership-first delegation rule: Duc may delegate only work he can already write, explain, test, and repair. Anything below that threshold goes through learning/pre-wire first.

Router: [[projects/raven/notes/raven-ownership-delegation-protocol]]

## Related

- [[projects/raven/notes/raven-architecture-hub]]
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]
- [[projects/raven/notes/raven-phase-1-build-plan]]
- [[projects/raven/notes/raven-phase-1-ingest-rating-plan]]
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-eval-how-to-use]]
- [[projects/raven/notes/raven-evaluation-insights]]
- [[projects/raven/notes/raven-prompt-hub]]
- [[projects/raven/notes/raven-enricher-evaluation]]
- [[projects/raven/notes/raven-bs-detector-ingestion-architecture]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
- [[context/goals]]
- [[context/now]]
