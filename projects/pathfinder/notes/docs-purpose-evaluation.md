---
type: source-summary
title: "Purpose Agent Evaluation And Audit Log"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - purpose
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/purpose_evaluation.md]]"
---

> **TL;DR**: This audit log tracks how the purpose stage was hardened around contradiction handling and a deterministic `PROBE:` handoff.

## Summary
The purpose evaluation doc captures the audit and patch cycle for the `purpose` stage. It records the discovered vulnerabilities, the attack plan, the patch set, and the execution results after replaying the attacks.

A key theme is contract reliability. The doc shows that prompt quality alone was not enough, because the analyst could still fail to emit the required `PROBE:` anchor consistently. That led to stronger Python composition of the final handoff.

This makes the note useful both for understanding Stage 1 specifically and for seeing when PathFinder moves a rule from prompt-only enforcement into deterministic code.

## Key Points
- The purpose stage needed both prompt hardening and graph-level safety rails.
- The required `PROBE:` anchor became a reliability issue, not just a formatting preference.
- Contradiction-rich handoff is a major theme of this stage's hardening work.

## Details
### Engineering Lesson
When a field or anchor is required every turn, PathFinder often ends up enforcing it in Python rather than trusting prompt obedience alone.

### Best Use
Read this before changing `purpose` prompt logic or its graph-level analyst output contract.

## Related
- [[projects/pathfinder/notes/docs-stage-prompt-audit]]
- [[projects/pathfinder/notes/docs-stage-evaluation]]
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]
