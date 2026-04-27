---
type: hub
title: Operations Hub
created: 2026-04-21T00:00:00.000Z
updated: '2026-04-25'
tags:
  - workflow
  - docs
  - meta
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
- development / technical help / code delegation -> [[development]]
- maintenance -> [[vault-keeping]]
- legacy learning references -> [[wiki/learning-protocol-hub]]
- architecture drafting -> [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]

## Start / Close
- [[wiki/operations/session-start-operation]] - load the right vault context before any task
- [[wiki/operations/self-healing-operation]] - repair pages, log durable work, and close out correctly
- [[wiki/operations/context-update-operation]] - patch context when live conversation changes what the vault should remember

## Maintenance
- [[vault-keeping]] - maintenance-family hub for drift, logging, propagation, and maintenance audits
- [[wiki/operations/branch-growth-operation]] - decide parent branch, node role, real-depth reason, Growth Contract, and propagation targets before creating durable vault nodes
- [[wiki/operations/file-creation-gate]] - create new vault files cleanly after Branch Growth selects the parent branch
- [[wiki/operations/lint-operation]] - run structural audits and flow checks
- [[wiki/operations/sort-operation]] - move pending files into the right lane

## Content
- [[wiki/operations/ingest-operation]] - turn raw sources into vault knowledge
- [[wiki/operations/query-operation]] - answer questions against compiled vault knowledge

## Draft / Architecture
- [[wiki/operations/draft-operation]] - iterative drafting loop for features, workflows, and artifacts
- [[wiki/operations/canvas-architecture-operation]] - Canvas-first workflow for system-shape decisions
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]] - architecture method note for the Canvas-first stack

## Development
- [[development]] - top-tier development domain for Detect -> Learn/Delegate routing
- [[wiki/operations/detect-operation]] - mandatory threshold operation before Learn or Delegate
- [[wiki/operations/learn-operation]] - full learning manual for technical help, docs, mechanisms, audits, Build-First, Pre-Wire, and Vibe Docing
- [[wiki/operations/delegate-operation]] - bounded code-writing operation after Duc's pattern is clear enough to copy and audit

## Learning
- [[wiki/learning-protocol-hub]] - legacy learning/help family hub, now routed through [[development]] for new technical work
- [[wiki/help-protocol]] - universal help gate retained as a Learn reference
- [[wiki/pre-wire-protocol]] - full feature ownership gate retained as a Learn reference

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
