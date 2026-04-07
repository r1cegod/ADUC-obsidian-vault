---
type: source-summary
title: "Stage Prompt Audit Guide"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - prompts
  - stages
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/prompt/docs/stage_prompt.md]]"
---

> **TL;DR**: This guide defines how every stage analyst and extractor prompt should reason, verify claims, and hand the output compiler one concrete `PROBE:` anchor.

## Summary
The stage prompt audit guide is the central prompt-contract doc for PathFinder's stage agents. It defines what a stage agent actually does, how the analyst prompt should be structured, what the reasoning output contract looks like, and how the extractor and analyst form an adversarial verification loop.

The doc is strict about role separation. Stage prompts must focus on domain reasoning, not student-facing wording, because the output compiler is the only node allowed to speak to the student. It also codifies the self-report ceiling and the requirement that analysts design real trade-offs rather than ask weak follow-up questions.

This is one of the highest-value docs in the whole corpus because it directly governs stage-agent behavior quality.

## Key Points
- Stage agents are internal reasoning lobes, not chatbots.
- `PROBE:` ownership belongs to the active stage, and it is the core handoff artifact.
- The extractor and analyst form a tight verification loop that resists shallow self-report.

## Details
### Prompt Structure
The guide standardizes block order and clarifies what belongs in identity, instructions, guardrails, and output format.

### Behavioral Contract
It sets the confidence and verification philosophy that later stage audits enforce through attack datasets and code-level clamps.

## Related
- [[projects/pathfinder/notes/docs-output-prompt-architecture]]
- [[projects/pathfinder/notes/docs-thinking-evaluation]]
- [[projects/pathfinder/notes/docs-purpose-evaluation]]
