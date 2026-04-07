---
type: source-summary
title: "jcsumlin Discord Ban Appeal"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/github-jcsumlin-discord-ban-appeal]]"
---

> **TL;DR**: This repo turns Discord appeals into an authenticated workflow: users log in with Discord, submit appeals through a web form, and moderators review them through webhook-driven staff handling.

## Summary
`jcsumlin/discord-ban-appeal` is the most implementation-rich appeals source in the current batch. It builds a React-based appeal portal around Discord OAuth2 so users cannot easily forge identity, then routes new appeals into Discord through webhooks where moderators can review or approve them. The repository is explicitly positioned for easy deployment, including Netlify, and documents the environment variables needed to connect a bot, guild, and appeal channel. For this moderation domain, it fills the gap between “you should have an appeal system” and “here is how to run one.”

## Key Points
- OAuth2 binds appeals to actual Discord identities rather than anonymous form responses
- Webhooks make appeals visible inside Discord's staff workflow instead of forcing moderators into email or external dashboards
- The repo is deployment-oriented, which makes it useful as an implementation template rather than just a concept demo

## Details
The strongest lesson here is that a credible appeal system needs both identity integrity and staff ergonomics. The repo solves the first through OAuth2 and the second through webhook delivery into staff channels. It also shows the operational burden that appeals systems create: credentials, channel isolation, secrets, anti-spam controls, and moderator review logic all have to exist before the form is genuinely trustworthy.

## Related
- [[wiki/synthesis/github-sylveon-discord-ban-appeals]]
- [[wiki/synthesis/discord-moderation-domain]]
