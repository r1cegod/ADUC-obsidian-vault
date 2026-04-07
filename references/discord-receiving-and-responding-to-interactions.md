---
type: reference
title: "Receiving and Responding to Interactions"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, ai, moderation]
status: active
lang: en
url: "https://docs.discord.com/developers/interactions/receiving-and-responding"
---

> **TL;DR**: Discord's interaction response contract sets the hard transport rules for AI-backed commands: reply in 3 seconds, use followups within 15 minutes, and defer long work.

## Description
Official Discord developer reference for interaction payloads, callbacks, and followup messages.

## Notes
- Best for: request/response timing, deferred replies, followup flow
- Critical limits: initial response in 3 seconds, interaction token valid for 15 minutes

## Related
- [[wiki/synthesis/discord-receiving-and-responding-to-interactions]]
- [[wiki/synthesis/discord-ai-agent-connection-patterns]]
