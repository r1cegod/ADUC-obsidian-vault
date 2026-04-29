---
type: operation
title: Context Update Operation
created: 2026-04-21T00:00:00.000Z
updated: '2026-04-29'
tags:
  - workflow
  - docs
  - context
status: active
lang: en
---
> **TL;DR**: Update the owning Duc OS page when live conversation changes what future sessions should know.

## When To Use
Use when the user reveals durable new context in conversation.

## Routing In
- [[wiki/operations-hub]]
- [[SCHEMA.md]]
- [[vault-keeping]]

## Steps
1. Decide which Duc OS page owns the new fact: [[duc-os/identity]], [[duc-os/long-arc]], [[duc-os/current]], [[duc-os/kickstart]], [[duc-os/engines]], or [[duc-os/session-protocol]].
2. Update that Duc OS page before the main task if it affects routing or judgment.
3. Leave `context/` stubs alone unless compatibility routing itself changes.
4. Log the update in the current day file.

## Routing Out
- Continue main task after context is current
- Closeout -> [[wiki/operations/self-healing-operation]]

## After Use Evolution Check
- Was the owning context file obvious?
- Did context updates happen early enough?
- Did the rule still require too much interpretation?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[duc-os]]
- [[duc-os/current]]
- [[duc-os/identity]]
- [[duc-os/long-arc]]
