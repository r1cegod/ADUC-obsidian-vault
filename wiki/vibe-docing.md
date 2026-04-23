---
type: protocol
title: Vibe Docing
created: '2026-04-17'
updated: '2026-04-20'
tags:
  - learning
  - protocol
  - meta
status: active
lang: en
feeds_into:
  - wiki/help-protocol.md
  - wiki/pre-wire-protocol.md
  - wiki/learning-protocol-hub.md
---
> **TL;DR**: VIBE_DOCING is a scoped mechanism-help operation: the agent mimics an official doc slice with neutral placeholders so Duc gets the missing mechanism without receiving the artifact answer.

## Definition

```text
VIBE_DOCING
  = official-doc-shaped mechanism slice
  + scoped to one operation
  + uses neutral placeholder values
  + avoids the challenge's exact answer
```

Use it when Duc has a visible artifact challenge but lacks one concrete mechanism, and a full official doc page would be too broad or momentum-killing. It is the mechanism-help operation inside [[wiki/build-first-learning]].

## When To Use

Use VIBE_DOCING for a `DOC_GAP` or narrow `MECHANISM_GAP` after the system seam is visible.

Good triggers:

- `vibe doc sqlite3.connect`
- `vibe doc CREATE TABLE`
- `vibe doc INSERT placeholders`
- `vibe doc SELECT fetchall`
- `vibe doc commit`
- `vibe doc API request headers`

Do not use it to bypass the blueprint or artifact attempt. If Duc has not made the seam visible, return to [[wiki/help-protocol]] or [[wiki/pre-wire-protocol]].

## Required Shape

Every vibe-doc section should look like a small official doc page:

```text
Operation:
What it does:
Pattern:
Parameters / inputs:
Returns / output:
Common traps:
Official source:
```

Keep it short. One operation per response.

## Allowed

```text
- mimic official documentation structure
- explain one operation or mechanism
- use neutral placeholder names and values
- show small non-product examples
- list common error modes
- cite or name the official doc section when useful
```

## Forbidden

```text
- use the challenge's exact target value
- reuse Duc's current live query, table values, API values, filenames-under-construction, or candidate data as example values
- use Raven's exact table/column set when that is the artifact Duc must design
- provide a complete runnable product solution before Duc attempts
- hide architecture decisions inside an example
- broaden into a full tutorial when one operation was requested
```

## Example

```text
Operation: sqlite3.connect(path)

What it does:
Opens a connection to a SQLite database file. If the file does not exist, SQLite may create it.

Pattern:
connection = sqlite3.connect("path/to/example.sqlite")

Parameters / inputs:
- path: string path to the database file

Returns / output:
- a Connection object used to execute SQL

Common traps:
- Opening a database is not the same as saving writes.
- INSERT, UPDATE, and DELETE need commit.

Official source:
- Python sqlite3 tutorial / connect reference
```

This example teaches the mechanism without solving a Raven-specific artifact.

## Value Isolation Rule

VIBE_DOCING must not reuse live values from the current build. This includes current query strings, API keys, table rows, active filenames under construction, candidate data, or exact Raven challenge values.

Use neutral placeholders instead:

```text
Allowed:
  "example topic"
  "example_id_123"
  "path/to/example.sqlite"
  "Example title"

Forbidden:
  Duc's current search query
  current API response values
  current DB row values
  active artifact answers
```

If a previous answer leaked live values into a doc slice, correct the protocol and switch back to neutral examples immediately.

## Relationship To Other Protocols

```text
[[wiki/help-protocol]]
  -> decides whether help/docs are allowed

[[wiki/build-first-learning]]
  -> keeps the learning motion artifact-first and usable

[[wiki/vibe-docing]]
  -> delivers the smallest official-doc-shaped mechanism slice

[[wiki/pre-wire-protocol]]
  -> uses build-first artifact levels and vibe docing inside feature ownership challenges
```

## Related

- [[wiki/help-protocol]]
- [[wiki/build-first-learning]]
- [[wiki/pre-wire-protocol]]
- [[wiki/learning-protocol-hub]]
- [[learning/README]]
