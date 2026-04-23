---
type: operation
title: "Sort Operation"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
---
> **TL;DR**: Move unsorted files into the correct vault lane so later ingest and retrieval operate on a clean structure.

## When To Use
Use when `pending/` or another unsorted lane needs cleanup.

## Routing In
- [[wiki/operations-hub]]
- [[vault-keeping]]
- [[SCHEMA.md]]

## Steps
1. Scan the unsorted files.
2. Choose the correct destination lane.
3. Move the files.
4. Ask only when the destination is materially ambiguous.
5. Offer or trigger ingest if the files should become knowledge immediately.

## Routing Out
- Ingest after sorting -> [[wiki/operations/ingest-operation]]
- Maintenance closeout -> [[wiki/operations/self-healing-operation]]

## After Use Evolution Check
- Were the destination lanes obvious?
- Did sorting require too much schema recall?
- Are there repeated ambiguous destinations that need clearer docs?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[vault-keeping]]
- [[wiki/operations/ingest-operation]]
