---
type: concept
title: "Agent Memory Compilation"
created: 2026-04-07
updated: 2026-04-07
tags: [obsidian, memory]
status: active
lang: en
aliases: ["memory compiler", "conversation-to-knowledge pipeline"]
---

> **TL;DR**: Agent memory compilation is the pipeline that turns raw conversations, logs, or notes into durable knowledge pages that future sessions can query cheaply and consistently.

## Definition
This pattern captures volatile context before it disappears, normalizes it into a raw daily or session layer, and then promotes the durable pieces into concept and synthesis pages.

## Key Ideas
- Compaction boundaries are where valuable context gets lost, so capture has to happen before or at those seams.
- The raw layer should preserve chronology; the compiled layer should preserve concepts and decisions.
- Index-guided retrieval over compiled notes is often cheaper and more stable than repeatedly mining raw chat history.
- Linting matters because compiled memory can rot if links, contradictions, or stale claims are ignored.

## Applications
Use this for coding-agent conversations, meeting digests, personal journaling workflows, or any system where "what we learned" matters more than replaying every raw message.

## Related
- [[references/coleam00-claude-memory-compiler]]
- [[references/cole-medin-claude-memory-karpathy]]
- [[wiki/synthesis/obsidian-agent-vault-architecture]]
