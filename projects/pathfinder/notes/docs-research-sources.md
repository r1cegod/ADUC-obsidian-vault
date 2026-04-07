---
type: source-summary
title: "Retrieval Research Sources"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - retrieval
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/research_sources.md]]"
---

> **TL;DR**: This doc defines the source-priority and query-shaping policy for retrieval stages, including how to treat narrow factual searches and supplementary Reddit evidence.

## Summary
The retrieval research sources doc explains where data agents should look for evidence and how search queries should be shaped. It prioritizes domain quality, query decomposition, and narrow contradiction-focused retrieval over broad "research everything" searches.

One of its most important contributions is source discipline. It makes clear that Reddit may be useful as supplementary evidence but should not be treated as the primary foundation for a factual claim when stronger sources exist.

This note matters because retrieval quality is partly a prompt issue and partly a source-selection policy issue. The doc addresses the latter.

## Key Points
- Good retrieval starts with source priorities and query discipline, not only a search tool.
- Broad blended searches perform worse than narrow contradiction-focused queries.
- Reddit is supplementary context, not primary evidence.

## Details
### Role In Evaluation
This source complements the data-agent evaluation guide by defining the raw material quality standard that retrieval stages should aim for.

### Engineering Use
Use it when building or revising research planner logic, source allowlists, or retrieval prompts.

## Related
- [[projects/pathfinder/notes/docs-data-agent-evaluation]]
- [[projects/pathfinder/notes/docs-job-evaluation]]
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]
