---
type: synthesis
title: "Vault Routing Renovation Report"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
feeds_into:
  - briefing.md
  - wiki/operations-hub.md
  - vault-keeping.md
---
> **TL;DR**: The vault routing renovation replaced hidden operation paths with hub-based routing, promoted `vault-keeping` into a true maintenance family hub, slimmed `SCHEMA.md` into a constitution, established an explicit official branching rule, and finished with compressed wrappers plus a continuity-only `context/hot.md`.

## What Changed

The renovation introduced a real routing stack:

```text
briefing
  -> operations-hub / vault-keeping / learning-protocol-hub / project README
  -> domain hub if needed
  -> canonical leaf
```

Major changes:
- created [[wiki/operations-hub]] as the global registry for official operations
- created canonical operation leaves under `wiki/operations/`
- promoted [[vault-keeping]] into the top-tier maintenance-family hub
- officialized Canvas-first architecture work for Raven
- converted [[SCHEMA.md]] from execution-manual mode into constitution mode
- added the hard operation-evolution law
- added the hard official branching rule

## Current Branch Architecture

### Top Routers
- [[briefing.md]] — global entry for active work and operation selection
- [[wiki/operations-hub]] — registry for official operation families and leaves
- [[vault-keeping]] — maintenance-family hub
- [[wiki/learning-protocol-hub]] — learning/help family hub
- project `README.md` pages — root branch nodes for project-local routing

### Project Branch Pattern

Preferred shape:

```text
project README
  -> project hub(s) when a domain grows
  -> direct artifact only when the branch is still small
```

Current state:
- PathFinder is the mature example: project README -> named domain hubs -> leaf notes
- Raven is mid-transition: project README -> architecture hub -> active Canvas and direct architecture notes
- IELTS Writing was patched into a minimal router so its README behaves like a project branch node rather than a flat content page

### Constitutional Layer
- [[SCHEMA.md]] now owns law, schema, propagation, and governance
- execution detail lives in operation leaves
- routing detail lives in hubs and project READMEs

## Branch Audit Findings

### What Is Working
- Official operations are now discoverable without scanning `SCHEMA.md`
- Maintenance has a real family hub instead of being buried in constitutional text
- PathFinder shows the cleanest branch pattern in the vault
- Raven architecture work now has a visible hub and a live board route

### What Was Still Wrong
- some older routers still described the pre-hub topology
- branch law existed implicitly, not explicitly
- project README quality was uneven across domains
- `SCHEMA.md` still carried too much execution detail after the leaf layer existed

### Fixes Landed In This Pass
- added the official branching rule to [[vault-keeping]]
- updated the vault root [[README.md]] so it reflects the new routing stack
- upgraded [[projects/ielts-writing/README]] into a minimal project router
- compiled the renovation into this report

### Final Cleanup Pass
- compressed [[AGENTS.md]] into a thinner Codex wrapper that points to hubs instead of repeating deep workflow bodies
- compressed [[CLAUDE.md]] into a thinner Claude wrapper with the same routing spine
- rebuilt [[context/hot]] into a real continuity cache and removed stale historical session dumps

## Official Branching Rule

The branch law now enforced by [[vault-keeping]]:

```text
top router
  -> family hub or project README
  -> domain hub if needed
  -> canonical leaf
```

Meaning:
- top routers should not dump mixed-family leaves
- family hubs should route inside one family
- project READMEs should act as project root routers
- hubs should appear once a branch has 3+ related notes or obvious growth pressure
- branch depth should usually stay within one or two hops before a leaf

## Remaining Debt

- Raven still has only one mature project hub; more domain hubs should appear only when the branches become real, not pre-emptively
- wrapper routing is now lean; future changes should resist re-bloating them
- the vault root README is now less stale, but it remains partly human-facing and not a full agent router by design

## Related
- [[briefing.md]]
- [[wiki/operations-hub]]
- [[vault-keeping]]
- [[SCHEMA.md]]
- [[wiki/learning-protocol-hub]]
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]
