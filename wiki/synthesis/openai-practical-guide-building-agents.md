---
type: source-summary
title: "OpenAI Practical Guide To Building Agents"
created: 2026-04-07
updated: 2026-04-07
tags: [ai, discord, moderation, source-summary]
status: active
lang: en
source: "[[references/openai-practical-guide-building-agents]]"
---

> **TL;DR**: For Discord moderation, OpenAI's current guidance points toward a single agent with tools and guardrails first, not an overbuilt multi-agent stack.

## Summary
OpenAI's agent guide defines an agent as a model plus tools plus instructions, then recommends using agents where rule systems become unwieldy and judgment depends on context and unstructured data. That maps well to moderation triage, evidence synthesis, and sanction recommendation. The guide also recommends establishing a baseline with the strongest model, adding evals early, and maximizing a single agent before splitting into multiple agents. For a Discord moderation copilot, this is the clearest official argument against premature orchestration complexity.

## Key Points
- Moderation fits the kinds of workflows agents handle well: contextual judgment and messy text
- Tools should be explicit and reusable, especially action tools and data-retrieval tools
- Single-agent systems are the recommended starting point until tool overload or logic complexity forces a split

## Details
The source helps connect the moderation problem to agent design rather than chatbot design. A moderation analyst agent can ingest case data, call deterministic tools, summarize evidence, and propose actions without becoming a fully autonomous moderator. The guide also reinforces that policy documents should be turned into explicit instructions and evaluated, which is exactly what a sanction ladder and appeal policy need.

## Related
- [[wiki/synthesis/openai-models-overview]]
- [[wiki/synthesis/discord-ai-agent-connection-patterns]]
