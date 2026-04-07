---
type: source-summary
title: "PathFinder Project Context"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - context
  - docs
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/context/docs/PROJECT_CONTEXT.md]]"
---

> **TL;DR**: This doc is the compact stable briefing for PathFinder: purpose, stack, system shape, source-of-truth files, code entry points, and repo-wide conventions.

## Summary
`PROJECT_CONTEXT.md` is the first-stop context doc for PathFinder. It compresses the stable facts of the repo into one short briefing: what the system does, what it is built with, how the graph is shaped, where the canonical docs live, and which code files anchor the implementation.

It is intentionally stable. If a fact changes often, it does not belong here. That makes the document ideal for low-token onboarding because it gives agents enough orientation to act without immediately reading the full architecture corpus.

Inside the vault, this summary is one of the most important routing notes because it mirrors the repo's own "start here" contract.

## Key Points
- This is the stable briefing doc, not a live scratchpad.
- It points to all canonical repo docs and code entry points.
- It locks the highest-level conventions that agents should respect before changing code.

## Details
### Role In The Repo
The file bridges between generic repository instructions and deeper architecture docs.

### Best Use
Use it as the first project-specific read for any future agent session, then branch into live context or deeper technical docs as needed.

## Related
- [[projects/pathfinder/notes/docs-current-context]]
- [[projects/pathfinder/notes/docs-architecture]]
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]
