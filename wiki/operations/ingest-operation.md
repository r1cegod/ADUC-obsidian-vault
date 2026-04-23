---
type: operation
title: "Ingest Operation"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
---
> **TL;DR**: Turn raw source material into linked vault knowledge through read, summarize, cross-reference, register, and log.

## When To Use
Use when the user wants sources processed into the vault.

## Routing In
- [[wiki/operations-hub]]
- [[SCHEMA.md]]

## Steps
1. Deduplicate against existing index and notes.
2. Read and analyze the source.
3. Create or update the primary summary page.
4. Update related entity, concept, or project notes if needed.
5. Cross-link, update index/context, and log the ingest.

## Routing Out
- More source work -> [[wiki/operations/sort-operation]]
- Query against new knowledge -> [[wiki/operations/query-operation]]
- Closeout -> [[wiki/operations/self-healing-operation]]

## After Use Evolution Check
- Was the ingest route obvious?
- Did deduplication or indexing feel scattered?
- Did any repeated ingest step belong in a tighter leaf?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[index.md]]
- [[wiki/operations/query-operation]]
