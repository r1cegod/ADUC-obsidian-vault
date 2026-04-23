---
type: hub
title: Raven Architecture Hub
created: '2026-04-21'
updated: '2026-04-22'
tags:
  - project/raven
  - architecture
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - context/now.md
---
> **TL;DR**: This hub is the default entrypoint for Raven architecture work, with Canvas-first policy for system-level decisions and markdown mirrors for stable structure.

## Summary
Raven has crossed the threshold where repo code alone is no longer enough to hold the architecture in working memory. This domain exists to externalize the system into a visual planning surface that lives inside the vault.

Official planning stack:

```text
Obsidian Canvas
  -> first stop for architecture decisions in this scope

Markdown notes
  -> durable mirrors, contracts, and routing

Optional D2
  -> formal rendered map only when a project actually benefits from it
```

Primary artifacts:
- `projects/raven/notes/raven-feature-web.canvas`
- `[[projects/raven/notes/raven-system-map.canvas]]`
- `[[projects/raven/notes/raven-vault-keeper-harness-architecture]]`

## Start Here
- Need the Canvas-first plan: [[projects/raven/notes/raven-canvas-build-plan]]
- Need the official DRAFT operation first: [[wiki/operations/draft-operation]]
- Need the current live canvas first: `projects/raven/notes/raven-feature-web.canvas`
- Need the next vault-ingestion thread: [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
- Need the current Tier 1 ranking draft: [[projects/raven/notes/raven-source-ranker-draft]]
- Need the evaluation workflow for Tier 1 and future rankers: [[projects/raven/notes/raven-eval-how-to-use]]
- Need the prompt-routing layer for ranker evolution: [[projects/raven/notes/raven-prompt-hub]]
- Need the fastest walkthrough first: [[projects/raven/notes/raven-architecture-demo]]
- Need the earlier system-map canvas: [[projects/raven/notes/raven-system-map.canvas]]
- Need the current product loop and build order: [[projects/raven/notes/raven-phase-1-build-plan]]
- Need the ingest and detector boundary: [[projects/raven/notes/raven-bs-detector-ingestion-architecture]]
- Need the evaluation write boundary: [[projects/raven/notes/raven-evaluation-domain]]
- Need the ownership rule before delegation or patching: [[projects/raven/notes/raven-ownership-delegation-protocol]]

## What This Domain Owns
- the live Raven skeleton as it actually exists in code
- the split between current code reality and future intended features
- the memory boundary between SQLite workbench state and vault-canonical synthesis
- the visual planning workflow used before major implementation changes

## Planning Rules
- Put Raven architecture decisions on Canvas first when they change system shape, storage boundaries, routing, or ingestion structure.
- Do not force Canvas into function-local code planning.
- Use the active Raven canvas for exploratory mapping, TODO clustering, open questions, and skeleton updates.
- Keep the canvas human-facing: text, groups, arrows, tensions, and questions, not note/file cards as the main board.
- Use much lighter versions of the domain colors only for actual unfinished function or feature cards.
- Promote stable decisions from the canvas back into markdown notes first, then D2 only if a formal render is worth the cost.
- Reflect stabilized architecture changes back into the Raven project routing layer in the same task: README, the right hub/leaf, and any affected domain router.
- Do not let the canvas become the only source of truth.

## Current Active Board
- Live board: `projects/raven/notes/raven-feature-web.canvas`
- Current live skeleton: `enricher -> youtube_search`
- Detached growth zone: open questions plus intended / not discussed features
- Next expansion threads: how Raven as vault keeper uses the vault for ingestion/promotion, and how Tier 1 ranking evolves through audit-backed prompt work

## Operating Commands

```text
Render the current Raven overview diagram:
~/.local/bin/d2 --layout elk --theme 201 --pad 40 \
  /mnt/d/ANHDUC/ADUC_vault/ADUC/projects/raven/notes/raven-system-map.d2 \
  /mnt/d/ANHDUC/ADUC_vault/ADUC/projects/raven/notes/raven-system-map.svg

Audit the structure in text before closing:
~/.local/bin/d2 --layout elk \
  /mnt/d/ANHDUC/ADUC_vault/ADUC/projects/raven/notes/raven-system-map.d2 \
  /mnt/d/ANHDUC/ADUC_vault/ADUC/projects/raven/notes/raven-system-map.txt

The D2 source sets root `style.fill` so the SVG stays genuinely dark rather than rendering on a white background.
```

Open these in Obsidian:
- `[[projects/raven/notes/raven-system-map.canvas]]`
- `[[projects/raven/notes/raven-system-map.d2]]`
- `![[projects/raven/notes/raven-system-map.svg]]`

## Current System Shape

```text
target
  -> query enricher
  -> source discovery
  -> candidate persistence
  -> video gate
  -> judgment layer
  -> channel memory
  -> channel rank
  -> report packet
  -> evolve loop
```

The architecture law is:

```text
search is recall
video gate is noise reduction
judgment is content evaluation
channel rank is accumulated source trust
evolve loop changes rules only after enough audit evidence
```

## Next Question In Scope

```text
vault keeper Raven
  -> what enters SQLite first
  -> what gets judged there
  -> what gets promoted into the vault
  -> what comes back out as retrieval packets
```

## Related
- [[projects/raven/notes/raven-canvas-build-plan]]
- [[projects/raven/notes/raven-architecture-demo]]
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]
- [[projects/raven/README]]
- [[projects/raven/notes/raven-phase-1-build-plan]]
- [[projects/raven/notes/raven-phase-1-ingest-rating-plan]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-eval-how-to-use]]
- [[projects/raven/notes/raven-prompt-hub]]
- [[projects/raven/notes/raven-bs-detector-ingestion-architecture]]
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
- [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
