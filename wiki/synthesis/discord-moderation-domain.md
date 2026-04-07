---
type: synthesis
title: "Discord Moderation Domain"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, synthesis]
status: active
lang: en
---

> **TL;DR**: The domain now covers server structure, join gating, rules screening, AutoMod, anti-raid, appeals, staff operations, app permissions, filtering patterns, and the runtime connection layer for AI moderation; the remaining gaps are a defensible sanction ladder, evidence-retention standards, and deeper moderator governance.

## Overview
This page is the router for Discord moderation knowledge in the vault. It started from one practical setup tutorial, but it now includes official Discord docs, GitHub implementations, Reddit policy examples, and tactical YouTube setup guides.

## Analysis
### Current baseline
- Server structure matters because moderation quality starts with channel topology, not just bot settings
- Role hierarchy should reflect actual trust boundaries: member, bots, moderator, admin, owner
- `@everyone` should stay narrow; risky permissions and app surfaces should be opt-in, not default
- Category permissions are the main scaling mechanism because they keep future channels aligned
- Join gating is layered: verification levels, rules screening, and incident-time hardening all matter
- Staff work needs private spaces, reporting surfaces, and confidentiality boundaries
- Automation baseline: AutoMod, logging, ticket/report intake, anti-raid controls, and app-command scoping
- AI connection baseline: explicit review flows should use Interactions, while passive intake should use Gateway plus only the intents you can justify
- Appeals are a real operating requirement and usually need either a managed workflow or a self-hosted authenticated form
- Moderator scale requires structure, specialization, and documentation, not just extra moderators

### Working model extracted from the corpus
The current domain model is:
1. Lock down the default member surface
2. Add explicit join gates through verification and rules screening
3. Give moderators only the powers their workflow requires
4. Route exceptional access through role-gated categories, channels, commands, and apps
5. Capture moderation events in logs and private review spaces
6. Use automation for repeatable abuse patterns, not for ambiguous judgment calls
7. Give punished users one official appeal path instead of letting disputes spread across DMs
8. Structure the staff team so governance can scale with community size

### Known limits of current domain
This domain is much stronger than the initial configuration-only seed, but it is still not a finished production handbook. The largest remaining weak spots are offense-class sanction design, evidence retention and recusal rules for appeals, and deeper moderator lifecycle practices such as recruiting, onboarding, review, and removal.

## Connections
- [[wiki/synthesis/gehsture-discord-server-setup-2026]] is the seed source summary for the first-pass server architecture
- [[wiki/synthesis/discord-moderation-source-map]] is the route map for further source expansion
- [[wiki/synthesis/discord-ai-agent-connection-patterns]] is the runtime wiring guide for connecting an existing Discord app to an AI moderation backend
- [[wiki/synthesis/discord-auto-moderation-in-discord]] captures Discord's broader automation strategy
- [[wiki/synthesis/github-jcsumlin-discord-ban-appeal]] captures a concrete self-hosted appeal implementation

## Open Questions
- What should the warning -> timeout -> kick -> ban ladder look like for different offense classes?
- What evidence-retention window, reviewer-recusal rule, and appeal standard should exist before irreversible actions?
- Which controls should be native Discord features versus third-party bots or self-hosted tooling?
- How should moderator trust, escalation rights, onboarding, and audit review be structured as the team grows?

## Related
- [[wiki/synthesis/gehsture-discord-server-setup-2026]]
- [[wiki/synthesis/discord-moderation-source-map]]
- [[wiki/synthesis/discord-ai-agent-connection-patterns]]
- [[wiki/synthesis/discord-auto-moderation-in-discord]]
- [[references/gehsture-discord-server-setup-2026]]
