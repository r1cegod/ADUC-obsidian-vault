---
type: synthesis
title: PathFinder Docs Ingest
created: 2026-04-06
updated: 2026-04-07
tags:
  - project/pathfinder
  - pathfinder
  - docs
  - synthesis
status: active
lang: en
feeds_into:
  - projects/pathfinder/README.md
---

> **TL;DR**: The PathFinder docs corpus now exists in the vault as a project-local source mirror plus a compressed note layer covering architecture, state, prompts, context, evaluation, and workflow docs.

## Summary
This ingest establishes the first structured knowledge layer for PathFinder inside the vault. Twenty-one repo docs are now mirrored into `projects/pathfinder/sources/docs/`, excluding `docs/DEV_LOG.md`, and each source now has a derived note page in `projects/pathfinder/notes/`.

The corpus divides cleanly into five knowledge bands: architecture contracts, context and maintenance rules, prompt architecture, evaluation workflow, and contributor workflow docs. Together they describe how the system is built, how it is operated, and how behavior changes are hardened before being treated as production direction.

One important distinction inside that workflow band: files under `delegated/` are human-consumption implementation walkthroughs, while `workflows/delegated_feature_how_to.md` is the protocol that teaches the LLM how to write those walkthroughs.

The main practical value is routing. Future agents can start here, then jump into the specific note or raw source they need instead of scanning the entire repo docs tree from zero.

## Key Clusters
- Architecture: [[projects/pathfinder/notes/pathfinder-architecture-hub|PathFinder Architecture Hub]]
- Context: [[projects/pathfinder/notes/pathfinder-context-hub|PathFinder Context Hub]]
- Prompts: [[projects/pathfinder/notes/pathfinder-prompt-hub|PathFinder Prompt Hub]]
- Evaluation: [[projects/pathfinder/notes/pathfinder-evaluation-hub|PathFinder Evaluation Hub]]
- Workflows: [[projects/pathfinder/notes/pathfinder-workflow-hub|PathFinder Workflow Hub]]

## Recommended First-Read Path
1. [[projects/pathfinder/README|Project README]]
2. [[projects/pathfinder/notes/docs-project-context|PathFinder Project Context]]
3. [[projects/pathfinder/notes/docs-current-context|Current Context]]
4. [[projects/pathfinder/notes/pathfinder-architecture-hub|PathFinder Architecture Hub]]
5. The relevant domain hub for the current task

## Why This Matters
The vault is now the live documentation home for PathFinder as well as the lower-token routing layer. Agents can read a short synthesis page, open the two or three summaries relevant to the current task, and only then drill into the canonical raw markdown under `projects/pathfinder/sources/docs/`. The repo `docs/` folder remains only as archived reference material.

## Related
- [[projects/pathfinder/README]]
- [[projects/pathfinder/notes/pathfinder-architecture-hub]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub]]
- [[projects/pathfinder/notes/docs-project-context]]
- [[projects/pathfinder/notes/docs-architecture]]
- [[projects/pathfinder/notes/docs-stage-prompt-audit]]
