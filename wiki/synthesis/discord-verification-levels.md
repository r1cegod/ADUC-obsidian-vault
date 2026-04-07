---
type: source-summary
title: "Discord Verification Levels"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-verification-levels]]"
---

> **TL;DR**: Verification levels are Discord's simplest built-in anti-raid gate: stronger levels reduce spam and drive-by abuse, but they also add onboarding friction that can hurt legitimate joiners.

## Summary
Discord documents five verification levels that determine when a new member is allowed to talk or join voice channels. The levels progress from no friction at `None` to verified phone-number gating at `Highest`, with intermediate steps layering verified email, account-age, and time-in-server requirements. The operational lesson is straightforward: verification is a throttle, not a full moderation system. It buys time during raids and slows throwaway accounts, but it should be combined with AutoMod, rules screening, and staff response.

## Key Points
- `Low` requires verified email; `Medium` adds 5 minutes since email verification
- `High` adds both prior requirements plus 5 minutes account age and 10 minutes in-server
- `Highest` adds verified phone number and is the strongest join gate

## Details
This source is useful because it makes the friction ladder explicit. `High` and `Highest` are especially important during raids because they delay immediate channel access and force more cost onto attacker accounts. The tradeoff is legitimate-user drop-off, so the right setting depends on whether the server is private, public, or actively under attack. In practice, verification should be treated as a tunable incident-response control.

## Related
- [[wiki/synthesis/discord-raids-101]]
- [[wiki/synthesis/discord-moderation-domain]]
