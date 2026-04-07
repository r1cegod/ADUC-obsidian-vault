---
type: concept
title: "LLM Wiki"
created: 2026-04-07
updated: 2026-04-07
tags: [obsidian, memory]
status: active
lang: en
aliases: ["llm knowledge base", "compiled markdown wiki"]
---

> **TL;DR**: An LLM wiki is a persistent, interlinked markdown layer that sits between raw sources and future queries, so knowledge gets compiled once and maintained over time instead of re-derived from scratch on every question.

## Definition
An LLM wiki is a markdown-native knowledge base maintained by an agent. Raw sources stay immutable, while the agent creates and updates summaries, concept pages, synthesis pages, cross-links, an index, and a log.

## Key Ideas
- Separate immutable raw sources from compiled wiki pages.
- Use `index.md` and `log.md` as the navigation and history backbone.
- Let the agent do the bookkeeping: cross-references, contradiction checks, and synthesis maintenance.
- Keep the schema explicit so the agent behaves like a maintainer instead of a generic chatbot.

## Applications
Use this pattern for project docs, personal knowledge systems, research domains, conversation memory, or any topic where sources accumulate over time and should become easier to query with each ingest.

## Related
- [[references/andrej-karpathy-llm-wiki]]
- [[wiki/concepts/agent-memory-compilation]]
- [[wiki/synthesis/obsidian-agent-vault-architecture]]
