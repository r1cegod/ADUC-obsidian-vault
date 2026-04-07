---
type: synthesis
title: "Obsidian Agent Vault Architecture"
created: 2026-04-07
updated: 2026-04-07
tags: [obsidian, memory, second-brain, synthesis]
status: active
lang: en
---

> **TL;DR**: The batch converges on one durable pattern: keep raw sources immutable, compile them into interlinked markdown pages, navigate through `index.md` and `log.md`, treat daily notes as raw capture to be graduated later, and protect trust with a strict human-vs-agent write boundary.

## Overview
This page is the human-readable topic digest for the current Obsidian/agent-memory ingest. Its job is to let the owner understand the topic without rereading every video, gist, repo, or landing page.

## Analysis
### What the sources agree on
- Markdown files are the memory substrate; Obsidian is mainly the browsing and linking surface.
- A root instruction file or schema is load-bearing because it tells the agent how to navigate and maintain the vault.
- `index.md` and `log.md` are the simplest reliable navigation primitives at current scale.
- The best systems separate raw capture from compiled knowledge.

### Where the sources differ
- Karpathy and Nate focus on the wiki architecture itself.
- Cole focuses on automating conversation capture into a daily raw layer and then compiling it.
- Ben focuses on broad vault roles: context, projects, resources, skills, tasks, and teams.
- Greg/Vin focus on human workflow: commands, reflection, daily notes, and write ownership.

### What changed in this vault
- Added `sources/transcripts/` as a first-class raw lane for YouTube/video ingest.
- Strengthened the daily-note template around raw capture, signals worth keeping, and promotion targets.
- Made the human-vs-agent write boundary explicit in the schema and entry docs.
- Formalized a new batch-ingest rule: if multiple sources form one topic, create a human-readable synthesis page instead of leaving only source-by-source notes.

### Practical reading of the topic
The strongest pattern is not "let the agent write everything." It is "let the agent maintain compiled knowledge while the human continues to own raw reflection and source curation." In practice that means the vault should have:
- immutable or near-immutable source material
- an agent-maintained compiled layer
- a daily/raw lane where chronology and voice are preserved
- a promotion path from daily/raw into durable concepts and syntheses

## Connections
- [[wiki/concepts/llm-wiki]] is the abstract architecture
- [[wiki/concepts/agent-memory-compilation]] is the capture-and-promotion pipeline
- [[wiki/concepts/human-agent-write-boundary]] is the trust rule that keeps the system honest
- [[wiki/concepts/daily-note-graduation]] is the compounding mechanism for raw reflection

## Open Questions
- Should session-end and pre-compact capture stay manual in this vault or become automated later?
- How much of the command layer should stay as documentation versus real executable tooling?
- When GitHub and Reddit ingest become common, what deserves a dedicated topic digest versus only source-level summaries?

## Related
- [[references/andrej-karpathy-llm-wiki]]
- [[references/coleam00-claude-memory-compiler]]
- [[references/greg-isenberg-vin-obsidian-claude-code]]
