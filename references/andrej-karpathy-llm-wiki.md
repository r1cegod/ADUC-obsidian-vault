---
type: reference
title: "LLM Wiki"
created: 2026-04-07
updated: 2026-04-07
tags: [obsidian, memory]
status: active
lang: en
url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
---

> **TL;DR**: Karpathy's gist defines the core pattern: immutable raw sources, an LLM-maintained wiki, a schema file, and `index.md` plus `log.md` as the lightweight navigation backbone.

## Description
This is the original architecture note behind the current wave of Obsidian-plus-agent memory systems. It is intentionally abstract and leaves the exact directory structure, tooling, and rituals to the user and their agent.

## Notes
- Author: Andrej Karpathy
- Created: 2026-04-04
- Core layers: raw sources, compiled wiki, schema/instruction file
- Key operational moves: ingest, query, lint, index maintenance, log maintenance
- Important caveat: the gist describes the pattern, not a production-ready implementation

## Related
- [[wiki/concepts/llm-wiki]]
- [[wiki/synthesis/obsidian-agent-vault-architecture]]
- [[references/nate-herk-karpathy-claude-code-obsidian]]
