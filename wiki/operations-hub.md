---
type: hub
title: "Operations Hub"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
feeds_into:
  - briefing.md
  - AGENTS.md
  - CLAUDE.md
  - index.md
  - vault-keeping.md
---
> **TL;DR**: Global registry for all official vault operations. Start here when the task is about choosing the right operation family or finding the canonical operation leaf.

## How To Use
Use this hub when the question is:

- what official operations exist?
- which operation should handle this task?
- where is the canonical leaf for a workflow?

Use family hubs when the family is already obvious:
- maintenance -> [[vault-keeping]]
- learning/help -> [[wiki/learning-protocol-hub]]
- architecture drafting -> [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]

## Start / Close
- [[wiki/operations/session-start-operation]] - load the right vault context before any task
- [[wiki/operations/self-healing-operation]] - repair pages, log durable work, and close out correctly
- [[wiki/operations/context-update-operation]] - patch context when live conversation changes what the vault should remember

## Maintenance
- [[vault-keeping]] - maintenance-family hub for drift, logging, propagation, and maintenance audits
- [[wiki/operations/file-creation-gate]] - create new vault files cleanly
- [[wiki/operations/lint-operation]] - run structural audits and flow checks
- [[wiki/operations/sort-operation]] - move pending files into the right lane

## Content
- [[wiki/operations/ingest-operation]] - turn raw sources into vault knowledge
- [[wiki/operations/query-operation]] - answer questions against compiled vault knowledge

## Draft / Architecture
- [[wiki/operations/draft-operation]] - iterative drafting loop for features, workflows, and artifacts
- [[wiki/operations/canvas-architecture-operation]] - Canvas-first workflow for system-shape decisions
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]] - architecture method note for the Canvas-first stack

## Learning
- [[wiki/learning-protocol-hub]] - learning/help family hub
- [[wiki/help-protocol]] - universal help gate
- [[wiki/pre-wire-protocol]] - full feature ownership gate

## Project Lifecycle
- [[wiki/operations/project-init-operation]] - start a new project workspace correctly
- [[wiki/operations/archive-operation]] - archive pages or projects without breaking routing

## Routing Rule
Official operations should be found by routing, not by scanning `SCHEMA.md`.

```text
question about operations
  -> operations hub
  -> family hub if needed
  -> canonical operation leaf
```

## Related
- [[SCHEMA.md]]
- [[vault-keeping]]
- [[wiki/learning-protocol-hub]]
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]
- [[index.md]]
