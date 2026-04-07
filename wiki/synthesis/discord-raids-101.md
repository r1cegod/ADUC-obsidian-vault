---
type: source-summary
title: "Discord Raids 101"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-raids-101]]"
---

> **TL;DR**: Discord's raid guide treats anti-raid as incident response: reduce mention damage, increase moderation automation, harden verification immediately, then report the event to Discord.

## Summary
Discord defines a raid as a wave of users or bots joining for malicious or disruptive purposes, then recommends a small set of concrete moves. The most important are enabling or tightening `Block Mention Spam`, raising verification to `High` or `Highest`, strengthening AutoMod responses, and using the built-in `Report Raid` flow for Community servers. The article is operationally useful because it treats anti-raid posture as something you can escalate during an incident rather than something fixed forever. It is one of the clearest official sources on “what to change right now.”

## Key Points
- Mention-spam limits are one of the fastest ways to blunt raid damage
- Verification levels can be raised temporarily to slow attacker access
- AutoMod rules should be made more restrictive during active disruption

## Details
The guide's core lesson is speed. During a raid, moderation needs controls that change attacker economics immediately, not perfect long-term policy. Raising verification buys time, mention filtering reduces blast radius, and stronger AutoMod settings reduce staff load. The article also reinforces that large or exposed communities should plan for raids ahead of time rather than improvising from a fully open default configuration.

## Related
- [[wiki/synthesis/discord-verification-levels]]
- [[wiki/synthesis/discord-moderation-domain]]
