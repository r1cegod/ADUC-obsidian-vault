---
type: hub
title: Raven Architecture Hub
created: '2026-04-21'
updated: '2026-04-27'
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

## Growth Contract
- Parent branch: [[projects/raven/README]]
- Node role: hub
- First parent link: [[projects/raven/README]]
- Growth trigger: create a sub-hub only when a flow or feature accumulates architecture, prompt, evaluation, and evidence children that need one route.
- Forbidden contents: prompt contracts except route links, eval reports except route links, workflow law, raw evidence, and live status dumps.
- Expected child types: architecture contracts, Canvas mirrors, feature/flow leaves, system-boundary decisions, and implementation-shape notes.

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
- Need the evaluation branch for Tier 1 and future rankers: [[projects/raven/notes/raven-evaluation-hub]]
- Need the prompt-routing layer for ranker evolution: [[projects/raven/notes/raven-prompt-hub]]
- Need the fastest walkthrough first: [[projects/raven/notes/raven-architecture-demo]]
- Need the earlier system-map canvas: [[projects/raven/notes/raven-system-map.canvas]]
- Need the current product loop and build order: [[projects/raven/notes/raven-phase-1-build-plan]]
- Need the ingest and detector boundary: [[projects/raven/notes/raven-bs-detector-ingestion-architecture]]
- Need the evaluation write boundary: [[projects/raven/notes/raven-evaluation-hub]] -> [[projects/raven/notes/raven-evaluation-domain]]
- Need the ownership rule before delegation or patching: [[projects/raven/notes/raven-workflow-hub]] -> [[projects/raven/notes/raven-ownership-delegation-protocol]]

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
- Current live skeleton: `create_run -> enricher -> youtube_search -> Send(ranker_tier1) -> ranker_tier1_final`
- Current search skeleton: medium + long YouTube `search.list`, ID dedupe, `videos.list` enrichment, `view_count >= 40000` Tier 0 filter, SQLite query/API/candidate logging.
- Current ranking skeleton: persisted candidate rows feed parallel Tier 1 scoring; `ranker_tier1_results` joins completion flags; final high-model selector writes `keep` / `throw_out` plus reason back to `raven_candidates`.
- Current model split: `LOW_LLM_KEY` runs enricher and Tier 1 on `gpt-5.4-mini`; `HIGH_LLM_KEY` runs final selection on `gpt-5.5`.
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
  -> run row
  -> query enricher
  -> YouTube duration fan-out
  -> videos.list enrichment
  -> view-count Tier 0 filter
  -> query/API/candidate logging
  -> candidate persistence
  -> parallel Tier 1 metadata scoring
  -> high-model final selector
  -> keep/throw_out writeback
  -> audit / evolve loop later
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
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-prompt-hub]]
- [[projects/raven/notes/raven-bs-detector-ingestion-architecture]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
- [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
