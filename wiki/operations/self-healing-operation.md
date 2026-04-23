---
type: operation
title: "Self-Healing Operation"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
---
> **TL;DR**: Final closeout workflow for vault edits: repair structure, log durable work, and finish propagation before ending the response.

## When To Use
Use at the end of any task that created or edited durable vault state.

## Routing In
- [[wiki/operations-hub]]
- [[vault-keeping]]
- [[SCHEMA.md]]

## Steps
1. Repair edited or created pages if needed.
2. Append the day-log entry.
3. Sync `log.md` only when the daily summary changed or a new day was created.
4. Patch downstream routers or context if the propagation rules require it.

## Routing Out
- End the task only after the vault closeout is complete

## After Use Evolution Check
- Did closeout happen before the response, not after?
- Did any propagation target get missed?
- Did the logging rule remain compact enough?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[vault-keeping]]
- [[log.md]]
- [[sources/log/HOW_TO_WRITE.md]]
