---
type: source-summary
title: "Cole Medin Claude Memory Compiler"
created: 2026-04-07
updated: 2026-04-07
tags: [obsidian, memory, source-summary]
status: active
lang: en
source: "[[sources/transcripts/cole-medin-claude-memory-karpathy]]"
---

> **TL;DR**: Cole Medin adapts the LLM wiki pattern into a conversation-memory system: hooks capture Claude Code sessions into daily logs, a compile step extracts durable knowledge, and future sessions start with the rules plus the index already loaded.

## Summary
This source is the most automation-heavy implementation in the batch. It treats raw conversations as the important source material, captures them through hooks at session-end and pre-compaction boundaries, stores them in daily logs, and then compiles those logs into more durable knowledge articles. The video matters because it shows a real answer to context loss: do not trust chat history to remain available, capture it before it disappears. It is strongest for coding-agent memory systems and weaker for broader personal knowledge practice.

## Key Points
- Session-start should preload the agent rules plus the index.
- Pre-compact and session-end hooks should both protect against context loss.
- Daily logs are the raw chronological lane; compiled knowledge is the query lane.
- Query and lint scripts are part of the system, not optional cleanup.
- The main benefit is speed: future answers can come from compiled takeaways instead of replaying old work.

## Details
### What the source teaches well
The video provides a clear data-flow model: conversation -> capture hook -> daily log -> compile -> knowledge article -> next-session injection. That makes memory maintenance feel like an engineering pipeline rather than a vague note-taking habit.

### Limits
The source assumes a coding-agent environment and does not spend much time on human authorship, reflection quality, or the difference between genuine self-knowledge and agent-generated patterning.

## Related
- [[references/cole-medin-claude-memory-karpathy]]
- [[wiki/concepts/agent-memory-compilation]]
- [[wiki/synthesis/obsidian-agent-vault-architecture]]
