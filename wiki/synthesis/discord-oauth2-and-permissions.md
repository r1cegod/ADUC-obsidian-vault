---
type: source-summary
title: "Discord OAuth2 And Permissions"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, ai, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-oauth2-and-permissions]]"
---

> **TL;DR**: Connecting an AI moderation agent to Discord means choosing the right execution identity: bot-token actions for app-owned workflows, OAuth2 user actions only when you truly need user-scoped behavior.

## Summary
Discord separates two authentication modes: bot-token identity and OAuth2 user identity. The bot token is what most moderation automations use for Gateway connections and REST calls, while OAuth2 user tokens are needed only when the integration must act on behalf of a real person under granted scopes. For an AI moderation copilot, this distinction matters because most review, logging, and sanction tooling should run under the bot's own identity. Moderator-authenticated dashboards or appeal portals are where OAuth2 becomes relevant.

## Key Points
- Bot tokens are the default identity for Discord app automation
- OAuth2 user tokens are for acting on behalf of a real user or moderator
- Tokens should be treated like passwords and isolated accordingly

## Details
This source clarifies a common architecture mistake: trying to make the AI agent “be” the moderator through user tokens when the workflow should really belong to the bot. In most moderation designs, the bot gathers context, drafts recommendations, and executes allowed actions under its own permissions. OAuth2 belongs at the edges, such as moderator web panels, authenticated appeal forms, or explicit human approval flows.

## Related
- [[wiki/synthesis/discord-moderating-apps]]
- [[wiki/synthesis/discord-ai-agent-connection-patterns]]
