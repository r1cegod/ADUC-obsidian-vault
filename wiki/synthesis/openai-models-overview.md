---
type: source-summary
title: "OpenAI Models Overview"
created: 2026-04-07
updated: 2026-04-07
tags: [ai, discord, moderation, source-summary]
status: active
lang: en
source: "[[references/openai-models-overview]]"
---

> **TL;DR**: The current official model surface supports a tiered moderation architecture: stronger GPT-5.4-class reasoning for difficult case analysis, smaller GPT-5.4 mini/nano-class models for cheaper high-volume triage, and dedicated moderation models for harmful-content classification.

## Summary
OpenAI's current models page is the source of truth for selecting the LLM side of a Discord moderation system. It recommends GPT-5.4 for complex reasoning and lower-cost variants such as GPT-5.4 mini or nano for high-volume workloads. This is useful because moderation does not require one model everywhere: simple triage, ranking, or extraction can often be cheaper than full policy reasoning. The page also confirms which endpoints and tool features the current model family supports.

## Key Points
- GPT-5.4 is the current flagship recommendation for hard reasoning tasks
- GPT-5.4 mini and nano are explicitly positioned for lower-cost, high-volume workloads
- Model choice should follow workflow difficulty rather than one-model-fits-all habit

## Details
For Discord moderation, this source supports a layered architecture. A cheap model can classify or structure low-risk queue items, while a stronger model handles ambiguous reports, appeals, or sanction recommendations. That split matters because moderation often mixes huge volume with a small number of genuinely difficult cases.

## Related
- [[wiki/synthesis/openai-omni-moderation-model]]
- [[wiki/synthesis/discord-ai-agent-connection-patterns]]
