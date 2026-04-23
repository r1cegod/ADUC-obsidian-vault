---
type: note
title: Raven Evaluation Domain
created: '2026-04-20'
updated: '2026-04-22'
tags:
  - project/raven
  - evaluation
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/README.md
---
> **TL;DR**: Raven evaluation docs, reports, audit logs, and production-readiness decisions are vault-canonical under `projects/raven/notes/`; repo `eval/` is only executable evidence.

## Rule

Raven follows the same evaluation-source boundary as [[projects/pathfinder/notes/docs-evaluation-domain|PathFinder Evaluation Domain]], but the rule is project-local here so agents do not have to infer it from PathFinder.

```text
Vault
  -> human-readable evaluation reports
  -> audit logs
  -> production-readiness decisions
  -> prompt/behavior rationale
  -> what changed and why it matters

Repo eval/
  -> runner scripts
  -> JSONL datasets
  -> trace folders
  -> temporary reproduction artifacts
  -> executable evidence only
```

Do not write maintained human-readable Raven evaluation reports into the repo. Repo `eval/` may contain code and raw evidence, but the report that a future agent should read belongs in the vault.

## Why

Raven is a knowledge engine. If evaluation results stay only inside repo traces or console output, the project does not compound. The vault should accumulate the judgment layer: what was tested, what failed, what changed, what is production-ready, and what remains unsafe.

## Required Domain Shape

Raven evaluation is a self-evolving domain, not just a report folder.

Required leaves:

- [[projects/raven/notes/raven-eval-how-to-use]] - official how-to/workflow leaf
- [[projects/raven/notes/raven-evaluation-insights]] - rolling compounding insight leaf

Prompt work in this domain routes through:

- [[projects/raven/notes/raven-prompt-hub]]

## Required Closeout For Raven Eval Work

When a Raven eval run happens, close it like this:

1. Run executable evidence in `/home/r1ceg/Raven/eval/`.
2. Audit traces before treating a green command as success.
3. Write or update the human-readable report in `projects/raven/notes/`.
4. Write/update [[projects/raven/notes/raven-evaluation-insights]] if the run produced durable learning.
5. Link the report from this domain note and [[projects/raven/README]].
6. Update `context/hot.md` or `context/now.md` only when continuity, next action, or production status changed.
7. Log the work in `sources/log/days/YYYY-MM-DD.md`.

## Current Reports And Leaves

- [[projects/raven/notes/raven-enricher-evaluation]] - one-node `gpt-5.4-mini` query enricher prompt/graph gate; passed 15/15 live cases across 3 rounds on 2026-04-20.
- [[projects/raven/notes/raven-eval-how-to-use]] - official evaluation workflow leaf.
- [[projects/raven/notes/raven-evaluation-insights]] - rolling compounding evaluation-insight leaf.
- [[projects/raven/notes/raven-prompt-hub]] - prompt-domain router used by evaluation work.

## Repo Evidence Boundary

Allowed in repo `eval/`:

- `eval/run_<target>_eval.py`
- `eval/<target>_cases.jsonl`
- `eval/threads/<thread_id>/traces/run_*.json`
- short pointer README only if needed

Not allowed as maintained repo docs:

- production-readiness reports
- audit narratives
- final human signoff summaries
- project evaluation strategy docs

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-enricher-evaluation]]
- [[projects/raven/notes/raven-eval-how-to-use]]
- [[projects/raven/notes/raven-evaluation-insights]]
- [[projects/raven/notes/raven-prompt-hub]]
- [[projects/raven/notes/raven-phase-1-build-plan]]
- [[projects/pathfinder/notes/docs-evaluation-domain]]
- [[projects/pathfinder/notes/docs-eval-how-to-use]]
