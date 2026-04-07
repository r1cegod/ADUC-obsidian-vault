---
type: source-summary
title: "Nate Herk Karpathy Obsidian Setup"
created: 2026-04-07
updated: 2026-04-07
tags: [obsidian, memory, source-summary]
status: active
lang: en
source: "[[sources/transcripts/nate-herk-karpathy-claude-code-obsidian]]"
---

> **TL;DR**: Nate Herk shows the quickest practical version of the Karpathy pattern: keep a raw folder, compile into a wiki folder, maintain `index.md` and `log.md`, and optionally add hot-cache plus recurring lint once the vault grows.

## Summary
This video is a fast implementation guide for the LLM wiki idea. Its strongest contribution is concrete structure: `raw`, `wiki`, `index`, and `log`, with domain subindexes when a vault starts to split into distinct areas. Nate also adds two pragmatic ideas not emphasized in the original gist: a hot cache for very recent, high-frequency context and recurring lint passes that check for inconsistencies and missing structure. The video is strongest as setup guidance, not as a full theory of memory capture.

## Key Points
- Obsidian is just the markdown IDE; the real asset is the structured file system.
- `index.md` and `log.md` are enough for retrieval at moderate scale without vector search.
- Domain subindexes help prevent one global index from becoming unreadable.
- A hot cache can reduce expensive wiki traversal for high-frequency assistant workflows.
- Linting is what keeps the vault coherent as more sources arrive.

## Details
### What the source teaches well
It translates abstract architecture into a folder layout a user can build quickly. The biggest value is operational clarity: where new raw material goes, where compiled pages live, how retrieval starts, and why indexes matter more than embeddings at small-to-medium scale.

### Limits
This source does not say much about how to capture conversations before context compaction or how to protect human-authored notes from agent overwrite. Those questions are handled better by the Cole and Greg/Vin sources.

## Related
- [[references/nate-herk-karpathy-claude-code-obsidian]]
- [[wiki/synthesis/obsidian-agent-vault-architecture]]
- [[wiki/concepts/llm-wiki]]
