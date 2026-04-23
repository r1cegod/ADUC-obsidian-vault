---
type: note
title: Raven Vault Keeper Harness Architecture
created: '2026-04-21'
updated: '2026-04-21'
tags:
  - project/raven
  - architecture
  - vault
  - memory
  - agents
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - projects/raven/notes/raven-phase-1-build-plan.md
  - projects/raven/notes/raven-bs-detector-ingestion-architecture.md
---
> **TL;DR**: Raven should be designed as a vault keeper with three explicit layers: model, harness, and memory substrate. The model reasons, the harness decides what context/tools/state are exposed and how execution resumes, and the vault/SQLite layer preserves durable knowledge. Low-model, low-token operation only works if Raven ingests by filtering, promoting, and linking small structured artifacts rather than stuffing raw content into context.

## Core Reframe

Raven is not mainly a chatbot, search tool, or note writer.

Raven is a **vault keeper**.

```text
public information
  -> cheap triage
  -> structured candidate
  -> judgment
  -> durable memory write
  -> retrieval when needed
  -> synthesis later
```

That means the core problem is not "make the model smarter."

The core problem is:

```text
What should be seen?
What should be saved?
What should be ignored?
What should be promoted into durable knowledge?
```

## Model vs Harness vs Memory

These are different layers and should stay separate.

```text
1. Model
   - produces text, labels, structured outputs, and judgments

2. Harness
   - selects context
   - runs tools
   - checkpoints execution
   - applies retry/approval/routing rules
   - records traces and audits

3. Memory substrate
   - SQLite for operational work state
   - vault for durable meaning, links, synthesis, and long-horizon continuity
```

If these are merged into one giant prompt, Raven becomes unstable and expensive.

## What "Harness" Means For Raven

As of 2026-04-21, "agent harness" is a real but overloaded term. The useful meaning is:

```text
all the code around the model that determines
- what information is stored
- what information is retrieved
- what information is presented to the model
- how tools are invoked
- how runs are resumed and audited
```

For Raven, the harness is not the product itself. It is the **operating layer** that makes the vault keeper reliable.

Plainly:

```text
model = thinks
harness = runs the thinking correctly
memory = keeps what matters
```

If the model is the brain doing one step of reasoning, the harness is the nervous system and procedure layer that decides:

```text
what happens first
what happens next
what gets retried
what gets stored
what gets promoted
what gets discarded
what context is loaded for the next step
```

Without a harness, Raven is just isolated LLM calls. With a harness, Raven becomes a system.

## What The Harness Is Not

It is not:

```text
- a fancy prompt
- a multi-agent roleplay setup
- a vendor-specific framework name
- a substitute for data modeling
- automatic self-improvement by default
```

A lot of people use "harness" to make orchestration sound deeper than it is. The substance only appears when the system has explicit state, checkpoints, routing, and memory rules.

## Why This Matters For Low-Model / Low-Token Operation

A foundational system cannot assume frontier-model context windows forever.

So Raven should ingest in **small, lossy, structured layers**:

```text
raw source
  -> metadata slice
  -> extracted claims / observations
  -> judgment labels
  -> promoted insight note
  -> linked durable memory
```

This is the only way a cheaper model can still operate coherently.

Bad pattern:

```text
reopen giant notes
dump many pages into context
ask the model to remember everything
```

Good pattern:

```text
keep canonical notes in vault
store compact operational rows in SQLite
retrieve only the minimum linked evidence for the current step
```

## Raven Memory Architecture

```text
            ┌─────────────────────────────┐
            │        Public Source        │
            └──────────────┬──────────────┘
                           │
                           v
            ┌─────────────────────────────┐
            │   Ingest Harness / Triage   │
            │ metadata, dedupe, routing   │
            └──────────────┬──────────────┘
                           │
               ┌───────────┴───────────┐
               │                       │
               v                       v
   ┌────────────────────┐   ┌────────────────────────┐
   │ SQLite Workbench   │   │ Raven Rating / Audit   │
   │ runs queries items │   │ BS detector judgments  │
   └──────────┬─────────┘   └────────────┬───────────┘
              │                          │
              └──────────────┬───────────┘
                             v
               ┌──────────────────────────┐
               │ Vault Promotion Layer    │
               │ notes, links, synthesis, │
               │ detector evolution       │
               └────────────┬─────────────┘
                            v
               ┌──────────────────────────┐
               │ Retrieval / Reuse Layer  │
               │ minimal context packets  │
               └──────────────────────────┘
```

## Ingestion Rule

Raven should not ingest information directly into the vault by default.

It should use a promotion ladder:

```text
L0 raw reference
   source exists but is not trusted or distilled

L1 candidate
   normalized metadata + provenance + query origin

L2 judged item
   Raven score + human audit + reason codes

L3 promoted memory
   durable note or structured vault entry worth future retrieval

L4 canonical synthesis
   reusable principle, map, or project-relevant doctrine
```

Most information should die at L0-L2.

If Raven saves everything, the vault becomes a landfill and retrieval quality collapses.

## Canvas Point: Vault Ingestion Structure
This is now the next active architecture thread for the Raven canvas.

Canvas point:
vault keeper Raven uses a promotion ladder instead of writing raw source noise straight into the vault

Why it exists:
the whole system will collapse into junk retrieval if operational intake and durable memory are not separated early

What it connects to:
[[projects/raven/notes/raven-architecture-hub]], [[projects/raven/notes/raven-canvas-build-plan]], [[projects/raven/notes/raven-phase-1-ingest-rating-plan]], and the live `projects/raven/notes/raven-feature-web.canvas`

What changes if it moves:
SQLite schema, promotion rules, retrieval packets, and human-audit flow all change with it

## First Ingestion Structure To Map
The next useful Canvas expansion is not "more features." It is this memory path:

```text
public source hit
  -> SQLite candidate row
  -> judged item
  -> promotion decision
  -> vault memory note or no write
  -> later retrieval packet
```

If this path is vague, the rest of Raven will fake progress.

## Vault Interaction Contract

The vault should be treated as Raven's **brain**, but only for promoted knowledge.

```text
SQLite
  = machine-operational state
  = runs, candidates, audits, traces, checkpoints

Vault
  = meaning
  = durable synthesis
  = linked project knowledge
  = detector evolution notes
  = routing/index pages
```

So Raven interacting with the vault should follow this rule:

```text
Do not write raw noise into the brain.
Write distilled, linked, provenance-carrying knowledge.
```

## Harness Responsibilities In Raven

Minimum harness responsibilities:

```text
1. query expansion
2. source fetch + normalization
3. dedupe
4. cheap relevance / spam triage
5. rating and uncertainty
6. human audit capture
7. checkpointing and resumability
8. promotion decision: SQLite only vs vault write
9. retrieval packet assembly for later reasoning
10. detector-version traceability
```

This is more important than adding more agent personalities.

## Recommended Build Order

Do not build a grand autonomous runtime first.

Build in this order:

```text
1. SQLite ingest spine
2. rating + audit spine
3. vault promotion contract
4. retrieval packet builder
5. disagreement/evolver placeholder
6. only then consider durable long-running runtime/harness upgrades
```

## What We Can Implement In Raven From This

Map harness ideas onto the current repo instead of inventing a new architecture all at once.

```text
current repo reality
  -> one-node enricher graph
  -> YouTube metadata fetch/normalize
  -> SQLite run/query/candidate tables
```

So the next useful harness pieces are:

### 1. Step runner contract

Raven should move through named steps, not loose function calls.

```text
expand_query
  -> fetch_youtube
  -> persist_query
  -> persist_candidates
  -> readback_packet
```

Minimum effect:

```text
- each step has input/output shape
- each step can fail visibly
- each step can be rerun
```

### 2. Checkpointed run state

A Raven run should know where it is.

```text
run_id
current_step
status
error
started_at
updated_at
```

This is a harness feature, not a model feature.

### 3. Source adapter boundary

Each source should expose one normalized adapter contract.

```text
search_source(query, limit)
  -> query_record
  -> candidate_records[]
```

That lets Raven swap YouTube and Reddit without changing the rest of the graph.

### 4. Promotion gate

Before any vault write, Raven should make an explicit decision:

```text
discard
keep_in_sqlite_only
promote_to_vault
```

That single gate is the difference between a vault keeper and a hoarder.

### 5. Retrieval packet builder

When Raven needs context later, do not reopen whole notes blindly.

Build a compact packet such as:

```text
source summary
key claims
rating
reason codes
provenance
linked vault note ids
```

### 6. Audit trace

Every rating should remain inspectable.

```text
candidate
raven_label
reason_codes
human_override
detector_version
```

If a future detector change cannot be traced to disagreement evidence, it is fake evolution.

## Immediate Raven Translation

Given the current backend, the near-term harness implementation is probably:

```text
Raven_graph.py
  owns step order and state transitions

search/youtube_search.py
  stays a source adapter

db.py
  stores run/query/candidate/checkpoint state

data/search_base.py
  becomes source-agnostic adapter contract
```

That is enough harness to matter.

## Strategic Judgment

The interesting part of "harness engineering" is real.

The dangerous misunderstanding is thinking Raven needs a fancy new agent framework first.

It probably does not.

Raven's first real harness can be small and local if it already does these things well:

```text
- explicit state
- explicit checkpointable steps
- explicit promotion rules
- explicit provenance
- explicit audit trail
```

That is enough foundation for a vault keeper.

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-phase-1-build-plan]]
- [[projects/raven/notes/raven-phase-1-ingest-rating-plan]]
- [[projects/raven/notes/raven-bs-detector-ingestion-architecture]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
