---
type: source-summary
title: "OpenAI Omni Moderation Model"
created: 2026-04-07
updated: 2026-04-07
tags: [ai, discord, moderation, source-summary]
status: active
lang: en
source: "[[references/openai-omni-moderation-model]]"
---

> **TL;DR**: `omni-moderation-latest` is best treated as the first-pass safety classifier in a Discord moderation stack, not the final decision-maker for sanctions or appeals.

## Summary
The official `omni-moderation-latest` page describes OpenAI's current dedicated moderation model for harmful content in text and images. In a Discord moderation architecture, this model is best used as a fast safety gate: detect whether content falls into known harmful categories, then pass the result and the original evidence to a broader policy agent or human review layer. The page is useful mainly because it clarifies that a moderation-specific classifier exists and can be separated from general reasoning models. That separation is healthy for moderation design.

## Key Points
- The moderation model is specialized for harmful-content detection
- It accepts text and images, which is useful for Discord screenshots or image evidence
- It should support policy decisions, not replace policy decisions

## Details
This source sharpens the architecture boundary. Harm categories are not the same thing as server rules, local norms, or sanction thresholds. A Discord server may ban content that is not globally unsafe, or allow edge cases that require moderator context. The moderation model should therefore feed the agent, not become the agent.

## Related
- [[wiki/synthesis/openai-models-overview]]
- [[wiki/synthesis/discord-ai-agent-connection-patterns]]
