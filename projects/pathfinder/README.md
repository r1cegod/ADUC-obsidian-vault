---
type: project
title: "PathFinder"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - ai
  - engineering
status: active
priority: high
lang: en
---

> **TL;DR**: PathFinder is a Vietnamese multi-agent career counselor project now mirrored into the vault with local raw docs plus derived summary notes.

## Start Here
For any PathFinder task, read in this order:
1. [[projects/pathfinder/notes/docs-project-context|PathFinder Project Context]]
2. [[projects/pathfinder/notes/docs-current-context|Current Context]]
3. Follow the task routes below

If exact wording or contract precision matters, drill into `projects/pathfinder/sources/docs/` only after reading the relevant note page.

## Goal
Build a durable project workspace that lets any agent start from a compressed, structured knowledge layer before drilling into the canonical PathFinder docs inside this vault.

## Current Status
Core `docs/` content has been ingested into project-local sources and summarized into note pages. This vault now holds the canonical operational contract, while the repo `docs/` folder is archived.

## Task Routes
- Architecture and graph shape: [[projects/pathfinder/notes/pathfinder-architecture-hub|PathFinder Architecture Hub]]
- Live implementation handoff: [[projects/pathfinder/notes/pathfinder-context-hub|PathFinder Context Hub]]
- Prompt work: [[projects/pathfinder/notes/pathfinder-prompt-hub|PathFinder Prompt Hub]]
- Evaluation work: [[projects/pathfinder/notes/pathfinder-evaluation-hub|PathFinder Evaluation Hub]]
- Workflow and handoff docs: [[projects/pathfinder/notes/pathfinder-workflow-hub|PathFinder Workflow Hub]]

## Core Links
- [[projects/pathfinder/notes/pathfinder-docs-ingest|PathFinder Docs Ingest]]
- [[projects/pathfinder/notes/docs-project-context|PathFinder Project Context]]
- [[projects/pathfinder/notes/docs-architecture|PathFinder Architecture]]
- [[projects/pathfinder/notes/docs-stage-prompt-audit|Stage Prompt Audit Guide]]
- [[projects/pathfinder/notes/pathfinder-architecture-hub|PathFinder Architecture Hub]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub|PathFinder Evaluation Hub]]

## Raw Sources
- Project-local mirror: `projects/pathfinder/sources/docs/`
- Canonical live docs: `projects/pathfinder/sources/docs/`
- Archived repo copy: `D:\ANHDUC\Path_finder\docs\`
- Rule: this vault now holds the live PathFinder documentation set; the repo `docs/` folder is archive-only

## Tasks
- [x] Mirror `docs/` into project-local sources, excluding `DEV_LOG.md`
- [x] Create one derived summary page per ingested doc
- [x] Add project routing to the vault index and context layer
- [ ] Decide whether future repo doc updates should be mirrored manually or through a sync routine

## Notes
This project workspace is now both the routing layer and the live documentation home for PathFinder. The repo `docs/` folder is kept only as archived reference material.

The strongest value of this workspace is onboarding efficiency. Agents can begin with the README, the ingest synthesis page, and a few key summaries, then open the raw source only when precision requires it.

Project hubs are now the default navigation layer beneath this README. When a task falls into one domain, open the matching hub first instead of scanning the full note set.

## Related
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]
- [[context/now]]
- [[briefing.md]]
