---
type: source-summary
title: "YouTube Sapphire Appeals 2026"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/youtube-sapphire-appeals-2026]]"
---

> **TL;DR**: This tutorial shows a lightweight appeals stack: Sapphire sends punished users a DM button, appeal.gg hosts the form, and staff review submissions in a private channel.

## Summary
This video is the most practical off-the-shelf appeals setup in the current corpus. It starts by enabling Sapphire's user notifications on punish and unpunish, then moves the workflow into appeal.gg where forms, questions, links, and retention windows are configured. It recommends keeping appeal data retention short, using clear form names, and optionally separating forms by punishment type. For this domain, it fills the “managed-bot appeals workflow” slot that sits between pure policy and self-hosted custom apps.

## Key Points
- Punishment notifications matter because they carry users into the appeal path immediately
- Appeal forms should be explicit about scope, questions, and storage duration
- Private staff channels remain essential even when the form itself is external

## Details
The tutorial is useful because it shows how to stand up appeals without building a custom web app. That makes it relevant for smaller communities or teams that want fast deployment. The tradeoff is dependence on external services and their retention, interface, and permissions model. It should therefore be paired with a clear internal appeal policy, not used as policy by itself.

## Related
- [[wiki/synthesis/github-jcsumlin-discord-ban-appeal]]
- [[wiki/synthesis/discord-moderation-domain]]
