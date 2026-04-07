---
type: source-summary
title: "PathFinder State Architecture"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - state
  - docs
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/architecture/docs/state_architecture.md]]"
---

> **TL;DR**: This doc is the field-by-field contract for `PathFinderState`, including who writes each field, who reads it, and what exit condition makes it meaningful.

## Summary
The state architecture doc is the precise contract beneath the higher-level architecture overview. It explains how signals move through the system, what every field means, and how each state element participates in routing, analysis, or output compilation.

Its most important rule is operational: every new state field needs a writer, a reader, and an exit condition. That keeps the graph from accumulating dead or ambiguous state and turns the state schema into an auditable interface rather than a dumping ground.

For agents working on PathFinder, this is the authoritative place to answer "where should this data live?" and "who is responsible for maintaining it?".

## Key Points
- `PathFinderState` is treated as a contract, not a convenience structure.
- Fields are documented with lifecycle responsibilities, not only names and types.
- The doc highlights counter behavior, signal relationships, and state-extension rules.

## Details
### Signal Flow
The document explains how conversation data, extracted profiles, behavioral signals, and system counters interact over a turn.

### Contract Discipline
It makes clear that adding state is not free. New fields require end-to-end ownership and documentation updates.

### Debugging Value
Because it names writers and readers explicitly, this doc is also a debugging map for tracing stale or misused state.

## Related
- [[projects/pathfinder/notes/docs-architecture]]
- [[projects/pathfinder/notes/docs-project-context]]
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]
