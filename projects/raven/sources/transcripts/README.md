---
type: note
title: Raven Transcript Sources
created: '2026-04-29'
updated: '2026-04-29'
tags:
  - project/raven
  - source-summary
  - youtube
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/sources/README.md
---
> **TL;DR**: Project-local lane for Raven transcript-derived source cards: provenance, compact summaries, claims, and synthesis pointers, not full raw transcript dumps.

## Growth Contract
- Parent branch: [[projects/raven/sources/README]]
- Node role: source lane
- First parent link: [[projects/raven/sources/README]]
- Growth trigger: split only when transcript-derived artifacts accumulate separate recurring child types such as source cards, final reports, or human audit packets.
- Forbidden contents: full third-party transcripts, full video bodies, unrelated eval traces, prompt contracts, current project status, and architecture decisions.
- Source/evidence boundary: store provenance, compact transcript-derived summaries, extracted claims, build implications, warning flags, and links back to executable repo evidence; keep raw transcript text transient unless a later source-rights policy explicitly allows durable storage.

## Purpose

Raven Tier 2 needs source content, but the vault should not become raw transcript storage.

```text
kept YouTube candidate
  -> fetch transcript transiently
  -> summarize / extract claims
  -> write compact source card here
  -> high-model report may link back here
```

This lane is the evidence layer between SQLite operational state and compiled Raven project meaning.

## Artifact Shape

Generated source cards should usually contain:

```text
source metadata
original query / run id / candidate id
transcript fetch status
compact transcript summary
key claims or mechanisms
build implications
warning flags
link to YouTube source
```

They should not contain the complete transcript text.

## Related

- [[projects/raven/sources/README]]
- [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-evaluation-hub]]
