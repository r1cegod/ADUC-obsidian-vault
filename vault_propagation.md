# Vault Propagation System

> Official documentation for the four-wire agent blast-radius solution.
> Implemented 2026-04-12. Companion to `vault_architecture.md`.

---

## Problem

A single vault write can touch 3-5 downstream files.
Without a lookup system, agents either:
- re-read every structural node after every write (slow, wastes tokens), or
- forget to propagate and leave the vault in a drifted state (broken navigation)

The propagation system solves this with four complementary layers.
No single layer is sufficient. All four are required for the guarantee.

---

## The Four Wires

```
Wire 1  Sync Matrix      SCHEMA.md → Propagation Sync Matrix
         ↓
         Lookup table: "if I write X, check Y."
         Agent consults after every write. Static, zero tooling.

Wire 2  feeds_into:      Frontmatter on structural nodes
         ↓
         Machine-readable graph. Agent reads field during normal
         file processing — no CLI, no traversal algorithm.
         Covers structural nodes only (not leaf notes).

Wire 3  Hot Cache        context/hot.md
         ↓
         Session-continuity file. Agent reads first, every session.
         Lists stable routers that don't need a repair pass.
         Compresses the 5-file tier load → 1 read in repeat sessions.

Wire 4  PostToolUse      scripts/check_propagation.py → settings.json
         ↓
         Enforcement layer. Fires after every Write/Edit.
         Reads file_path from tool input JSON, looks up sync matrix,
         prints downstream targets. Agent can't "forget" to propagate.
```

---

## How They Interact

```
Agent writes context/now.md
        │
        ▼  [Wire 4 fires — PostToolUse hook]
        │
        ├─ script reads file_path from stdin JSON
        ├─ looks up "context/now.md" in EXACT_RULES          ← Wire 1 data
        └─ prints:
           ⚡ PROPAGATION REQUIRED after writing: context/now.md
             → briefing.md
                Active Projects must match between context/now and briefing
             → index.md
                Vault Status changes may require index header update

        Agent updates briefing.md
        │
        ▼  [Wire 4 fires again]
        │
        └─ prints:
           ⚡ PROPAGATION REQUIRED after writing: briefing.md
             → context/now.md
                Active Projects must match between briefing and context/now
           (already done — agent checks it off and stops)

Next session:
        Agent reads context/hot.md                           ← Wire 3
        Sees "briefing.md — verified 2026-04-12, stable"
        Skips briefing.md repair pass
        Saves ~200 tokens and one read
```

---

## Graph Shape

```
feeds_into: relationships on structural nodes only           ← Wire 2

context/me.md   ──────────────────────────────►  (terminal)
context/goals.md ─────────────────────────────►  (terminal)
context/hot.md  ──────────────────────────────►  (terminal)
index.md        ──────────────────────────────►  (terminal)
log.md          ──────────────────────────────►  (terminal)

context/now.md  ──────────────────────────────►  briefing.md
briefing.md     ──────────────────────────────►  context/now.md  (bidirectional: Active Projects)

projects/*/README.md  ────────────────────────►  briefing.md
                      ────────────────────────►  context/now.md

projects/*/notes/*-hub.md  ───────────────────►  projects/*/README.md

SCHEMA.md  ───────────────────────────────────►  CLAUDE.md
           ───────────────────────────────────►  AGENTS.md

sources/log/days/*.md  ───────────────────────►  log.md
wiki/**/*.md  ────────────────────────────────►  index.md
projects/*/notes/docs-*.md  ──────────────────►  index.md
```

Max depth from any leaf to vault root: **4 hops**. No cycles except the
briefing ↔ context/now.md Active Projects bidirectional constraint.

---

## Maintenance

### Adding a New Structural Node

When you create a new project README, hub, or vault-root operational doc:

```
1. Add exact-path row to SCHEMA.md → Propagation Sync Matrix
2. Add feeds_into: to the new file's frontmatter
3. Add the inverse — what structural nodes feed INTO the new file
4. Update scripts/check_propagation.py EXACT_RULES dict
5. Update context/hot.md → Last Session Summary (file changed)
```

### Adding a New Project

```
1. Create projects/<name>/README.md with feeds_into: [briefing.md, context/now.md]
2. Add EXACT_RULES entry: "projects/<name>/README.md" → [briefing.md, context/now.md]
   (pattern rule already covers this — verify the pattern_rule lambda matches)
3. Update briefing.md Active Projects + context/now.md Active Projects
4. PostToolUse hook will enforce downstream propagation from that point forward
```

### Updating context/hot.md

At end of every task, update three sections:
- **Stable Since Last Session**: add files you verified clean and did not edit
- **Last Session Summary**: files changed, open threads, next action
- **Flagged For This Session**: clear resolved items, add new ones

### Growing Structural Node Count

Current structural nodes: ~20. Trigger for review: when EXACT_RULES in
`scripts/check_propagation.py` exceeds 30 entries, audit for redundancy.
Pattern rules reduce the need for exact entries — prefer patterns for file families.

---

## File Inventory

| Component | Location | Role |
|-----------|----------|------|
| Sync matrix | `SCHEMA.md → Propagation Sync Matrix` | Source of truth for propagation rules |
| Hook script | `scripts/check_propagation.py` | PostToolUse enforcement |
| Hook config | `C:/Users/r1ceg/.claude/settings.json` | Wires script to Claude Code PostToolUse |
| Hot cache | `context/hot.md` | Session-continuity, stable router skip |
| feeds_into: | Frontmatter on structural nodes | Machine-readable graph |

---

## Why Not BFS / Full Dependency Graph

The vault's dependency structure is a **shallow tree** (max 4 hops), not a general graph.
BFS is designed for graphs with cycles, cross-links, and non-obvious paths.

| Full BFS approach | This system |
|------------------|-------------|
| Bidirectional relationship types (depends-on, extends, implements, consumes) | One type: feeds_into: |
| CLI commands for traversal | PostToolUse hook reads a Python dict |
| Works across 35 agent platforms | Targets Claude Code only |
| Obsidian CLI dependency | Zero external dependencies |
| Useful when depth > 5 and cycles exist | Vault max depth: 4, no cycles |

At 500+ structural nodes with cross-project dependencies, revisit BFS.
At current scale (20 structural nodes, 2 projects, max 4 hops), this system
covers the full blast radius with zero external tooling.
