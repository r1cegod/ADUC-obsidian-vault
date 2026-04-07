---
type: source-summary
title: "Discord Interactions Overview"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, ai, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-interactions-overview]]"
---

> **TL;DR**: If you already have a Discord app, Interactions are the cleanest way to connect it to an AI moderation backend because Discord sends structured command/component payloads instead of forcing you to infer intent from raw chat.

## Summary
Discord's interactions layer is the main connection surface for an AI moderation assistant that users or moderators invoke explicitly. The source explains that commands, components, and modals all arrive as interaction payloads, and that apps can receive them either over Gateway or through an HTTP interactions endpoint. For connection design, this matters because it lets the AI layer start from structured user intent such as `/review-case`, `/summarize-report`, or a moderator button press. It is the cleanest entrypoint when your AI agent is acting as a copilot rather than silently watching every message.

## Key Points
- Interactions are native, structured invocations for commands, buttons, and modals
- Discord supports two mutually exclusive receive modes for interactions: Gateway or outgoing webhook
- Connection choice should match your runtime model, not library habit

## Details
This source is important because it narrows the connection problem. If the AI moderator is command-driven, you do not need to start from message-content ingestion at all. You can expose explicit moderation workflows through commands and modals, then forward the structured payload to your AI backend. That is safer, more predictable, and easier to evaluate than freeform message scraping.

## Related
- [[wiki/synthesis/discord-receiving-and-responding-to-interactions]]
- [[wiki/synthesis/discord-ai-agent-connection-patterns]]
