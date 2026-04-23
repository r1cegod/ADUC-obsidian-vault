---
type: operation
title: "Project Init Operation"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
---
> **TL;DR**: Create a new project workspace with the right README router, source lane, notes lane, and top-level registration.

## When To Use
Use when starting a new project in the vault.

## Routing In
- [[wiki/operations-hub]]
- [[SCHEMA.md]]

## Steps
1. Create the project directory shape.
2. Create the project README as a router, not a status dump.
3. Register the project in index, briefing, and context if active.
4. Log the project creation the same session.

## Routing Out
- Project work -> `projects/<name>/README.md`
- Maintenance closeout -> [[wiki/operations/self-healing-operation]]

## After Use Evolution Check
- Was project creation fully routable from the README?
- Did registration across top-level files feel duplicated?
- Did any project-init step still depend on memory?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[briefing.md]]
- [[context/now]]
