---
type: hub
title: Raven Prompt Hub
created: '2026-04-22'
updated: '2026-04-26'
tags:
  - project/raven
  - prompts
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - projects/raven/notes/raven-evaluation-hub.md
---
> **TL;DR**: Routing page for Raven prompt work. Use this hub for prompt contracts, prompt audits, prompt evolution, and the reusable production-prompt reference inherited from PathFinder.

## Growth Contract
- Parent branch: [[projects/raven/README]]
- Node role: hub
- First parent link: [[projects/raven/README]]
- Growth trigger: split a prompt family only when multiple prompt contracts, audits, eval insights, or evolution rules need a dedicated route.
- Forbidden contents: raw eval traces, architecture decisions, current project status, and executable prompt tests.
- Expected child types: prompt contracts, prompt audits, prompt-evolution rules, and evaluation-insight links.

## Summary

Raven prompt work should be official, not implicit.

This hub exists so prompt-system work has a real home:

```text
prompt contract
  -> prompt audit
  -> evaluation insight
  -> prompt evolution
```

## Start Here

- Need the current Tier 1 prompt direction: [[projects/raven/notes/raven-source-ranker-draft]]
- Need evaluation workflow first: [[projects/raven/notes/raven-eval-how-to-use]]
- Need rolling prompt/eval lessons: [[projects/raven/notes/raven-evaluation-insights]]
- Need reusable production prompt law: [[wiki/synthesis/evaluation-production-prompt-domain]]
- Need the older source playbook from PathFinder: [[projects/pathfinder/notes/docs-production-system-prompts]]

## Why This Exists

PathFinder already has an official prompt domain. Raven should follow the same discipline instead of keeping prompt insight as chat residue.

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[wiki/synthesis/evaluation-production-prompt-domain]]
- [[projects/pathfinder/notes/pathfinder-prompt-hub]]
- [[projects/pathfinder/notes/docs-production-system-prompts]]
