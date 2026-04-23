---
type: operation
title: "Query Operation"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
---
> **TL;DR**: Answer questions from compiled vault knowledge first, then optionally file good answers back into the vault.

## When To Use
Use when the user asks a question against vault knowledge.

## Routing In
- [[wiki/operations-hub]]
- [[SCHEMA.md]]

## Steps
1. Search index and relevant notes.
2. Prefer compiled notes over raw sources unless precision requires raw wording.
3. Synthesize the answer with citations.
4. If the answer is durable, file it back into the vault.

## Routing Out
- New durable page -> [[wiki/operations/file-creation-gate]]
- Follow-up ingest -> [[wiki/operations/ingest-operation]]

## After Use Evolution Check
- Was the answerable knowledge easy to locate?
- Did query routing overuse raw sources?
- Did filing back require too many extra hops?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[index.md]]
- [[wiki/operations/ingest-operation]]
