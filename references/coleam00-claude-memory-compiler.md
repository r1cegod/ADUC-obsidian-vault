---
type: reference
title: "claude-memory-compiler"
created: 2026-04-07
updated: 2026-04-07
tags: [obsidian, memory]
status: active
lang: en
url: "https://github.com/coleam00/claude-memory-compiler"
---

> **TL;DR**: Cole Medin's repo operationalizes the Karpathy pattern for Claude Code with hooks, daily logs, compilation scripts, query scripts, and lint checks.

## Description
This repo is the most implementation-ready related source in the batch. It shows how session transcripts can be captured, normalized into a daily raw layer, compiled into concept pages, and injected back into future sessions.

## Notes
- Repository owner: `coleam00`
- Public repo state observed: 2026-04-07
- Pipeline: conversation -> hooks -> daily logs -> compile -> knowledge articles -> session-start injection
- Utility scripts mentioned in README: `compile.py`, `query.py`, `lint.py`
- Scope note: coding-agent memory system, not a full personal-knowledge methodology

## Related
- [[references/cole-medin-claude-memory-karpathy]]
- [[wiki/concepts/agent-memory-compilation]]
- [[wiki/synthesis/obsidian-agent-vault-architecture]]
