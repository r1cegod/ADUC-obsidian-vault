---
type: note
title: Raven Sources And Evidence
created: '2026-04-25'
updated: '2026-04-25'
tags:
  - project/raven
  - docs
  - workflow
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - projects/raven/notes/raven-workflow-hub.md
---
> **TL;DR**: Raven source/evidence lane. Use this as the project-local landing zone for raw evidence pointers, eval artifacts, references, and future source material that should not be mixed into compiled project notes.

## Growth Contract
- Parent branch: [[projects/raven/README]] and [[projects/raven/notes/raven-workflow-hub]]
- Node role: source lane
- First parent link: [[projects/raven/README]]
- Growth trigger: create child lanes only when real source/evidence accumulation appears, such as recurring eval evidence, external references, or raw material awaiting promotion.
- Forbidden contents: Raven project status, architecture decisions, prompt contracts, human-readable eval reports, and large third-party dumps.
- Source/evidence boundary: this lane stores raw pointers, inventories, small exact snippets, and evidence references; compiled meaning stays in `projects/raven/notes/`.

## Purpose

This folder separates raw/evidence material from compiled Raven knowledge.

```text
projects/raven/notes/
  -> compiled meaning, reports, workflow, architecture, decisions

projects/raven/sources/
  -> raw source pointers, evidence references, datasets, trace pointers, exact material when needed
```

Do not make raw evidence the first read. Compiled notes should point here only when exact reproduction or source inspection is needed.

## Suggested Lanes

Create subfolders only when real evidence pressure appears:

```text
eval/        pointers or curated evidence related to evaluation runs
references/  project-local external references
raw/         raw material that belongs to Raven but is not yet compiled
```

Do not create empty decorative folders.

## Repo Boundary

Raven repo `eval/` remains the executable evidence workspace:

```text
/home/r1ceg/Raven/eval/
  -> runner scripts
  -> JSONL datasets
  -> trace folders
  -> temporary reproduction artifacts
```

Vault reports and production-readiness decisions belong in:

```text
projects/raven/notes/
```

This source lane may point to repo evidence, but it should not duplicate large runnable artifacts unless there is a clear preservation reason.

## What Belongs Here

```text
external reference pointers
raw source summaries awaiting promotion
eval evidence pointers
small curated exact evidence snippets when needed
source inventories
```

## What Does Not Belong Here

```text
Raven project status
architecture decisions
prompt contracts
human-readable eval reports
large third-party content dumps
```

Route those through the project notes branch.

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-workflow-hub]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-context-hub]]
- [[wiki/synthesis/vault-target-tree-architecture]]
