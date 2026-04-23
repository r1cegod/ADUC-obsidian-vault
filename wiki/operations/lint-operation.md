---
type: operation
title: "Lint Operation"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
---
> **TL;DR**: Structural audit workflow for finding and fixing drift in routing, indexing, links, freshness, and vault health.

## When To Use
Use for vault maintenance audits, flow checks, and drift cleanup.

## Routing In
- [[wiki/operations-hub]]
- [[vault-keeping]]
- [[SCHEMA.md]]

## Steps
1. Run the structural checks.
2. Run the content-quality and gap checks.
3. Check pending files and context freshness.
4. Fix what is cheap and safe.
5. Log the rest explicitly.

## Routing Out
- Sorting -> [[wiki/operations/sort-operation]]
- Closeout -> [[wiki/operations/self-healing-operation]]

## After Use Evolution Check
- Did the lint scope fit the task size?
- Were the cheap fixes obvious?
- Did the audit still over-rely on `SCHEMA` scanning?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[vault-keeping]]
- [[wiki/operations/self-healing-operation]]
