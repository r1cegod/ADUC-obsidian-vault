---
type: source-summary
title: "Output Compiler Prompt Architecture"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - prompts
  - output
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/prompt/docs/output_prompt_architecture.md]]"
---

> **TL;DR**: This doc defines the output compiler as PathFinder's only student-facing response generator and explains how its prompt is assembled by deterministic case logic plus injected signal blocks.

## Summary
The output prompt architecture doc explains how PathFinder's compiler turns internal state into the final Vietnamese response. It defines the case waterfall, the structure of each major case, and the rule that Python selects and injects the right prompt blocks before the model writes anything.

Its importance is architectural, not cosmetic. The compiler is the only student-facing generator, so this doc effectively describes the system's communication boundary with the student. It also shows how behavioral signals, escalation state, and stage reasoning are translated into one controlled response surface.

If an agent needs to understand "why does the user see this reply?", this is the canonical prompt doc to read.

## Key Points
- The output compiler is the sole student-facing response generator.
- Prompt assembly follows a deterministic case waterfall driven by Python state.
- User-facing behavior is composed from injected blocks rather than a single monolithic prompt.

## Details
### Case Model
The doc distinguishes bypass, normal stage, path debate, and escalation cases, with first-match-wins priority.

### Behavioral Control
It shows how user signals and message signals are translated into optional blocks that shape tone and content without exposing internal mechanics.

## Related
- [[projects/pathfinder/notes/docs-stage-prompt-audit]]
- [[projects/pathfinder/notes/docs-architecture]]
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]
