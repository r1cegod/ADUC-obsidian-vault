---
type: operation
title: "Archive Operation"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
---
> **TL;DR**: Retire pages or projects without deleting them, preserving routing and link integrity while marking them as archived.

## When To Use
Use when a page, project, or source is no longer active but should remain referenceable.

## Routing In
- [[wiki/operations-hub]]
- [[SCHEMA.md]]

## Steps
1. Mark the item archived in frontmatter.
2. Update the relevant index/router locations.
3. Remove it from active-project surfaces if needed.
4. Log the archival.

## Routing Out
- Maintenance closeout -> [[wiki/operations/self-healing-operation]]

## After Use Evolution Check
- Was archival visible enough in the router layer?
- Did the route preserve link integrity cleanly?
- Did active-project cleanup require too many hops?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[index.md]]
- [[briefing.md]]
