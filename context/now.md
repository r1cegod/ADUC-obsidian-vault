---
type: context
title: Current Focus
created: '2026-04-06T00:00:00.000Z'
updated: '2026-04-26'
tags:
  - context
status: active
lang: en
feeds_into:
  - briefing.md
---
> **TL;DR**: Raven is the active next scaffold. PathFinder is reviewable unless a blocker appears. Wynncraft is a low-priority leisure assistant lane. Root context should choose the next project/domain route, not carry project-sized implementation detail.

## Active Decisions

- Technical help and code delegation route through [[development]]: run [[wiki/operations/detect-operation]] first, then [[wiki/operations/learn-operation]] for ownership/mechanism gaps or [[wiki/operations/delegate-operation]] for bounded pattern-copy execution.
- Branch creation now routes through [[wiki/operations/branch-growth-operation]] before [[wiki/operations/file-creation-gate]]. Durable nodes must have a parent branch, node role, real-depth reason, forbidden contents, first parent link, propagation targets, and an in-page Growth Contract before writeback is complete.
- Root context compression is active: `context/now.md` points to project branches; project-specific implementation detail belongs under the project context branch.
- The vault global activity log uses two layers: [[log.md]] is navigation only; daily entries live under `sources/log/days/`.
- Maintained repo mirrors should use explicit sync routines rather than manual-by-default content mirroring.

## Current Focus

```text
PathFinder
  -> reviewable / portfolio-ready unless blocker appears
  -> live detail: [[projects/pathfinder/notes/pathfinder-context-hub]] -> [[projects/pathfinder/notes/docs-current-context]]

Raven
  -> active next scaffold
  -> live detail: [[projects/raven/notes/raven-context-hub]] -> [[projects/raven/notes/raven-current-context]]

IELTS Writing
  -> active parallel training track
  -> route through [[projects/ielts-writing/README]]

Wynncraft Assistant
  -> low-priority leisure-control lane
  -> live route: [[projects/wynncraft/README]] -> [[projects/wynncraft/notes/wynncraft]]
```

Strategic direction: build reusable AI-agent infrastructure, evaluation, memory, and distribution leverage. Raven is the current project expression of that direction.

## Active Projects

- [[projects/pathfinder/README|PathFinder]] - reviewable/portfolio-ready unless a concrete blocker threatens demo or review confidence. Use [[projects/pathfinder/notes/pathfinder-context-hub]] for project-local live state and hardening context.
- [[projects/raven/README|Raven]] - active Knowledge Signal Engine scaffold. Use [[projects/raven/notes/raven-context-hub]] -> [[projects/raven/notes/raven-current-context]] for live repo state, next seams, and branch status.
- [[projects/ielts-writing/README|IELTS Writing]] - active parallel track: 20-day band 4-5 to 7-8 protocol, schema-based docs, structural gap rather than linguistic gap.
- [[projects/wynncraft/README|Wynncraft Assistant]] - low-priority leisure assistant for Wynncraft builds, source pulls, and bounded next-session strategy. Use [[projects/wynncraft/notes/wynncraft]] for the operating sheet.

## Current Raven Route

Raven's current high-level branches are:

```text
context
architecture
prompt
evaluation
workflow/rules
source/evidence
```

Next implementation direction remains:

```text
enriched query
  -> YouTube enrichment
  -> SQLite writeback
  -> Tier 1 ranker
  -> eval loop
```

## Current PathFinder Route

PathFinder-specific hardening detail was moved out of root context into:

```text
[[projects/pathfinder/notes/pathfinder-context-hub]]
  -> [[projects/pathfinder/notes/docs-current-context]]
```

Only reopen PathFinder for a named review/demo blocker, broader University comparison proof, frontend continuation proof, or cheap seam coverage worth locking.

## Vault Status

- Vault tree-growth renovation is active.
- [[wiki/synthesis/vault-target-tree-architecture]] defines the reference model for root -> trunk -> project/root -> branch hub -> leaf -> source/evidence.
- [[wiki/operations/branch-growth-operation]] is the canonical operation before creating durable vault nodes.
- Raven is the first proof branch for the new model.
- PathFinder root-context residue has been compressed into its project context branch.

## Related

- [[briefing.md]]
- [[context/hot]]
- [[context/goals]]
- [[development]]
- [[vault-keeping]]
- [[wiki/synthesis/vault-target-tree-architecture]]
- [[wiki/operations/branch-growth-operation]]
- [[projects/pathfinder/notes/pathfinder-context-hub]]
- [[projects/raven/notes/raven-context-hub]]
- [[projects/wynncraft/README]]
- [[projects/wynncraft/notes/wynncraft]]
