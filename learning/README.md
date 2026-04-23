---
type: hub
title: Learning Sessions
created: '2026-04-08'
updated: '2026-04-20'
tags:
  - learning
  - hub
status: active
lang: en
feeds_into:
  - wiki/learning-protocol-hub.md
---
> **TL;DR**: Index of feature-ownership learning sessions. Start from [[wiki/learning-protocol-hub]], use [[wiki/help-protocol]] for lightweight help, and create a session note for serious [[wiki/pre-wire-protocol]] runs.

## Protocol Router

Start here:

```text
[[wiki/learning-protocol-hub]]
```

Main protocols:

- [[wiki/help-protocol]] - mandatory first gate for technical help/docs/debugging
- [[wiki/build-first-learning]] - primary technical-learning method: usable artifacts, maturity levels, agent audit, plus BUILD/AUDIT/PATCH/STEAL/ABSORPTION modes
- [[wiki/vibe-docing]] - official-doc-shaped mechanism slices with neutral placeholders and strict live-value isolation
- [[wiki/pre-wire-protocol]] - full feature-ownership learning path
- [[projects/raven/notes/raven-ownership-delegation-protocol]] - stricter Raven overlay

## How To Start A New Pre-Wire Session

1. Copy [[templates/learning-session]] into `learning/sessions/[feature]-[YYYY-MM-DD].md`.
2. Fill in feature name, date, and project tag.
3. Duc writes the blueprint without agent help.
4. Duc ends the draft with `READY FOR AUDIT`.
5. Agent audits with semantic labels: OWNABLE, MECHANISM_GAP, SYSTEM_GAP, or ONE_TIME_UTILITY.
6. If MECHANISM_GAP, run dependency-ordered artifact challenges using [[wiki/build-first-learning]].
7. Use [[wiki/vibe-docing]] for one missing mechanism at a time; do not hand the artifact answer.
8. Duc builds the final feature himself unless the task becomes OWNABLE/L3 delegation.

## Sessions

<!-- Add new sessions here as they are created -->

| Date | Feature | Gap count | Status |
|------|---------|-----------|--------|
| 2026-04-16 | [[learning/sessions/raven-api-sqlite-ingest-wire-2026-04-16|Raven API + SQLite Ingest Wire]] | pending audit | active |
| - | - | - | - |

## Related

- [[wiki/learning-protocol-hub]]
- [[wiki/help-protocol]]
- [[wiki/build-first-learning]]
- [[wiki/vibe-docing]]
- [[wiki/pre-wire-protocol]]
- [[templates/learning-session]]
- [[context/me]]
