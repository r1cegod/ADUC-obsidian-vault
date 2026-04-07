---
type: source-summary
title: "Dev Log Generator - System Prompt"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - docs
  - workflow
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/DEV_LOG_SYSTEM_PROMPT.md]]"
---

> **TL;DR**: This doc specifies how a dev-log writer should turn completed work into durable architecture and decision entries instead of loose session notes.

## Summary
The document defines a system prompt for generating high-signal development log entries. Its purpose is to capture what changed, why it changed, what broke before the fix, and what was learned, so the repo accumulates durable reasoning instead of shallow summaries.

The workflow is opinionated. It expects the writer to inspect actual diffs and behavior, reject vague language, and record concrete architectural implications. The result is a decision-history artifact rather than a diary.

For the vault, this doc matters because it explains the quality bar behind PathFinder's durable memory. It is the meta-rule behind what belongs in long-lived decision history and what should stay in transient context files.

## Key Points
- Dev-log entries are meant to preserve reasoning, not just chronology.
- Every entry should explain the failure mode that existed before the change.
- The document pushes writers toward architectural consequences and next-step implications.

## Details
### Operational Use
Use this source when an agent needs to convert a completed implementation or evaluation pass into a durable decision record. It is not a runtime system contract; it is a maintenance-quality contract.

### Relationship To Other Docs
This prompt complements the repo's context-maintenance rules. `CURRENT_CONTEXT` captures live work, while this prompt helps move important results into durable memory.

## Related
- [[projects/pathfinder/notes/docs-context-maintenance]]
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]
- [[projects/pathfinder/README]]
