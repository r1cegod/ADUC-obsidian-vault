# How To Write The Vault Activity Log

> **TL;DR**: Write the real log entry in `sources/log/days/YYYY-MM-DD.md`, then keep `log.md` as the one-line-per-day navigation index.

Last updated: 2026-04-09

Rules:

- `log.md` is navigation only
- write the real activity log in `sources/log/days/YYYY-MM-DD.md`
- keep data-gap-only notes in `sources/log/DATA_HOLES.md`
- keep one day per file
- if the same day changes again, update that same day file
- keep the block format inside the day file: `## [YYYY-MM-DD] ACTION | Subject`
- add `Project: <tag>` on the line after the heading when the entry belongs to a specific project (e.g. `Project: pathfinder`); omit the line for vault-global work
- after updating a day file, sync `log.md` directly using the Edit tool (no script needed)

## Syncing log.md after a day-file change

`log.md` is one line per day. After touching a day file:

| What changed | Action on log.md |
|---|---|
| New day file created | Insert new line at top of the entries block (newest-first) |
| `Summary:` line updated | Edit the matching line in log.md |
| Entry added, summary unchanged | No log.md update needed |

Line format:
```
- YYYY-MM-DD | {Summary line} | [entry](./sources/log/days/YYYY-MM-DD.md)
```

Insert position for new days: after the `- Data holes | ...` header line, before the previous most-recent entry.

## DATA_HOLES.md — gap tracking

Gaps use heading-based entries so they can be opened and closed programmatically:

```md
## [YYYY-MM-DD] OPEN | Gap title
- description
- resolution criteria

## [YYYY-MM-DD] RESOLVED | Gap title
Resolved: YYYY-MM-DD by <log entry or commit reference>
- original description
```

Add a new gap:
```
python scripts\manage_vault_log.py add-hole \
  --title "Gap name" \
  --body "- description" "- resolution criteria"
```

Close a gap (case-insensitive title fragment match):
```
python scripts\manage_vault_log.py close-hole \
  --title "gap name fragment" \
  --resolved-by "2026-04-08 vault log"
```

## Day-file shape

```md
# 2026-04-08

Summary: Short one-line day summary

## Activity

## [2026-04-08] FIX | Subject
Project: pathfinder
- what changed
```
