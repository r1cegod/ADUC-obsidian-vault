---
type: synthesis
title: "Discord AI Agent Connection Patterns"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, ai, moderation, synthesis]
status: active
lang: en
---

> **TL;DR**: If you already know how to create a Discord app, the connection problem reduces to four decisions: interaction vs passive intake, bot token vs OAuth2, fast acknowledgment vs deferred AI work, and classifier-first vs policy-agent-first processing.

## Overview
This page summarizes how to connect an existing Discord app to an AI moderation backend. It is intentionally about runtime wiring and architecture, not bot creation or server setup.

## Analysis
### The core connection split
There are two clean entry patterns:
- Explicit invocation: moderators or users call slash commands, buttons, or modals. This should use Discord Interactions.
- Passive intake: the system watches live messages, joins, or role/channel events. This should use Gateway plus the right intents.

### The transport pattern for explicit AI workflows
For slash-command moderation flows, the stable path is:
1. Discord sends an interaction payload
2. Your endpoint validates and acknowledges it quickly
3. The app defers the response if AI work will take more than a moment
4. Your backend calls moderation classification and/or a reasoning agent
5. The bot posts the result as a followup, a staff-only message, or both

This is the right pattern for:
- `/review-message`
- `/summarize-report`
- `/recommend-sanction`
- `/draft-appeal-response`

### The transport pattern for passive moderation
For passive AI moderation, the stable path is:
1. Gateway event arrives
2. Event is filtered by deterministic rules first
3. Relevant evidence is assembled
4. A moderation classifier and/or policy agent scores the case
5. The system logs, alerts, queues for staff review, or takes low-risk automated action

This is the right pattern for:
- spam / scam bursts
- suspicious join waves
- repeated mention abuse
- message triage queues

### Identity and authorization
- Use the bot token for almost all Discord-side moderation workflows
- Use OAuth2 user identity only when a moderator dashboard, appeal portal, or explicit user-scoped action genuinely needs it
- Treat user-scoped auth as the exception, not the center of the system

### AI-side architecture
The current best-fit stack is:
- classifier layer: `omni-moderation-latest` for harmful-content detection
- reasoning layer: GPT-5.4-class model for difficult case analysis, or cheaper GPT-5.4 mini/nano-class models for high-volume triage
- tool layer: deterministic Discord action tools, evidence retrieval tools, and logging tools

### Recommended first implementation
If the goal is AI moderation and you already know how to create the bot, start here:
1. One slash command such as `/review-message`
2. One deferred interaction flow
3. One backend endpoint that calls:
   - moderation classifier
   - policy/rules prompt
   - structured output for `violation_candidates`, `confidence`, `recommended_action`, `human_review_required`
4. One staff-only followup message

This is the smallest connection that proves the architecture without requiring privileged intents or full passive surveillance.

## Connections
- [[wiki/synthesis/discord-interactions-overview]]
- [[wiki/synthesis/discord-receiving-and-responding-to-interactions]]
- [[wiki/synthesis/discord-gateway]]
- [[wiki/synthesis/discord-oauth2-and-permissions]]
- [[wiki/synthesis/openai-practical-guide-building-agents]]
- [[wiki/synthesis/openai-models-overview]]
- [[wiki/synthesis/openai-omni-moderation-model]]

## Open Questions
- Should your first AI moderation feature be explicit command-driven review or passive live-message triage?
- Do you want the AI to recommend actions only, or execute low-risk actions automatically?
- Will the backend live as a stateless webhook service, a long-running Gateway worker, or both?

## Related
- [[wiki/synthesis/discord-moderation-domain]]
- [[wiki/synthesis/openai-practical-guide-building-agents]]
- [[wiki/synthesis/discord-interactions-overview]]
