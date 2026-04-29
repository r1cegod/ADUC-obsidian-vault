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
         Session-continuity file. Agent reads before Duc OS.
         Lists stable routers that don't need a repair pass.
         Hands off to duc-os.md as the root operating layer.

Wire 4  PostToolUse      scripts/check_propagation.py → settings.json
         ↓
         Enforcement layer. Fires after every Write/Edit.
         Reads file_path from tool input JSON, looks up sync matrix,
         prints downstream targets. Agent can't "forget" to propagate.
```

---

## How They Interact

```
Agent writes duc-os/current.md
        │
        ▼  [Wire 4 fires — PostToolUse hook]
        │
        ├─ script reads file_path from stdin JSON
        ├─ looks up "duc-os/current.md" in EXACT_RULES       <- Wire 1 data
        └─ prints:
           PROPAGATION REQUIRED after writing: duc-os/current.md
             -> briefing.md
                Active Projects must match between duc-os/current and briefing
             -> index.md
                Vault Status changes may require index header update

        Agent updates briefing.md
        │
        ▼  [Wire 4 fires again]
        │
        └─ prints:
           PROPAGATION REQUIRED after writing: briefing.md
             -> duc-os/current.md
                Active Projects must match between briefing and duc-os/current
           (already done - agent checks it off and stops)

Next session:
        Agent reads context/hot.md                           ← Wire 3
        Sees "briefing.md — verified 2026-04-12, stable"
        Skips briefing.md repair pass
        Saves ~200 tokens and one read
```

---

## Graph Shape

Compatibility stubs in `context/` point into Duc OS. They are not updated on every current-state change unless the redirect itself changes.

```
feeds_into: relationships on structural nodes only           ← Wire 2

duc-os.md       ──────────────────────────────►  AGENTS.md / CLAUDE.md / briefing.md

duc-os/current.md ────────────────────────────►  briefing.md / index.md

duc-os/*.md    ───────────────────────────────►  duc-os.md / index.md

context/me.md   ──────────────────────────────►  duc-os/identity.md
context/goals.md ─────────────────────────────►  duc-os/long-arc.md
context/now.md  ──────────────────────────────►  duc-os/current.md
context/hot.md  ──────────────────────────────►  duc-os.md
index.md        ──────────────────────────────►  (terminal)
log.md          ──────────────────────────────►  (terminal)

development.md  ──────────────────────────────►  briefing.md
                ──────────────────────────────►  AGENTS.md
                ──────────────────────────────►  CLAUDE.md
                ──────────────────────────────►  wiki/operations-hub.md
                ──────────────────────────────►  index.md

wiki/operations/branch-growth-operation.md ───►  vault-keeping.md
                                             ─►  wiki/operations-hub.md
                                             ─►  wiki/operations/file-creation-gate.md
                                             ─►  wiki/operations/project-init-operation.md
                                             ─►  index.md

briefing.md     ──────────────────────────────►  duc-os/current.md  (bidirectional: Active Projects)

projects/*/README.md  ────────────────────────►  briefing.md
                      ────────────────────────►  duc-os/current.md

projects/*/notes/*-hub.md  ───────────────────►  projects/*/README.md

SCHEMA.md  ───────────────────────────────────►  CLAUDE.md
           ───────────────────────────────────►  AGENTS.md

sources/log/days/*.md  ───────────────────────►  log.md
wiki/**/*.md  ────────────────────────────────►  index.md
projects/*/notes/*.md  ───────────────────────►  index.md
```

Max depth from any leaf to vault root: **4 hops**. No cycles except the
briefing <-> duc-os/current.md Active Projects bidirectional constraint.

---

## Maintenance

### Adding a New Structural Node

When you create a new project README, hub, or vault-root operational doc:

```
1. Run [[wiki/operations/branch-growth-operation]] before writing.
2. Add the Growth Contract section so the new node declares parent branch, role, first parent link, growth trigger, and forbidden contents.
3. Add exact-path row to SCHEMA.md → Propagation Sync Matrix when pattern rules are not enough.
4. Add feeds_into: to the new file's frontmatter.
5. Add the inverse — what structural nodes feed INTO the new file.
6. Update scripts/check_propagation.py EXACT_RULES dict if this node has custom downstream targets.
7. Update context/hot.md only if the new structural node changes continuity, stable-router status, flagged items, or next action.
```

### Adding a New Project

```
1. Create projects/<name>/README.md with feeds_into: [briefing.md, duc-os/current.md]
2. Include the project-root Growth Contract: parent branch, node role, first parent link, growth trigger, forbidden contents, expected child types
3. Add EXACT_RULES entry: "projects/<name>/README.md" -> [briefing.md, duc-os/current.md]
   (pattern rule already covers this - verify the pattern_rule lambda matches)
4. Update briefing.md Active Projects + duc-os/current.md Active Projects
5. PostToolUse hook will enforce downstream propagation from that point forward
```

### Updating context/hot.md

At end of a task, delta-update `context/hot.md` only when continuity, stable-router status, flagged items, or the next likely action changed.

Check these sections:
- **Current Continuity**: patch only durable project/session state that future agents need.
- **Stable Since Last Session**: add or preserve files verified stable and not edited.
- **Next Action**: update when the next likely move changed.
- **Flagged For This Session**: clear resolved items or add new blockers.

Do not rewrite the hot cache as a full session summary. The real activity record lives in `sources/log/days/YYYY-MM-DD.md`, with `log.md` as the navigation index.

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
| Hot cache | `context/hot.md` | Session-continuity cache before Duc OS |
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
At current scale, this system covers the full blast radius with zero external tooling.
