---
type: source-summary
title: "Context Maintenance"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - context
  - workflow
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/context/how to/context_maintenance.md]]"
---

> **TL;DR**: This doc defines how stable context, live context, and durable decisions should be separated and maintained across sessions.

## Summary
The context-maintenance guide explains the division of labor between `PROJECT_CONTEXT.md`, `CURRENT_CONTEXT.md`, and the durable decision log. Its goal is to keep high-value context current without turning every file into a mixed bag of temporary notes and permanent facts.

This is a maintenance discipline document, not a product or architecture doc. It tells contributors where a new fact belongs, what kinds of updates should happen at the end of work, and what kinds of details should be avoided in each context file.

For the vault, this source is especially important because the vault is also a memory system. It shows how the PathFinder repo already distinguishes durable from transient knowledge.

## Key Points
- Context quality depends on separating stable facts from live work and durable decisions.
- `PROJECT_CONTEXT` and `CURRENT_CONTEXT` have different jobs and should not drift into each other.
- Maintenance is part of done, not optional cleanup.

## Details
### File Roles
The guide explains when to update stable context, live context, and durable decision history.

### Practical Benefit
Following this doc lowers restart cost after session compaction and reduces stale-handoff bugs.

## Related
- [[projects/pathfinder/notes/docs-project-context]]
- [[projects/pathfinder/notes/docs-current-context]]
- [[projects/pathfinder/notes/docs-dev-log-system-prompt]]
