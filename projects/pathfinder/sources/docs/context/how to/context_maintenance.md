# Context Maintenance

## File Roles
- `projects/pathfinder/sources/docs/context/docs/PROJECT_CONTEXT.md`: stable project facts that should survive session compaction.
- `projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md`: live working notes, blockers, and handoff details for the current cycle.
- `projects/pathfinder/sources/docs/DEV_LOG.md`: append-only engineering decision history.
- `D:\ANHDUC\Path_finder\docs\`: archived repo copy, not canonical.

## Update Rules
1. Put stable architecture facts in `PROJECT_CONTEXT.md`.
2. Put active tasks, blockers, and "what to do next" in `CURRENT_CONTEXT.md`.
3. When a decision should survive beyond the current work cycle, also record it in `projects/pathfinder/sources/docs/DEV_LOG.md`.
4. Link to source docs instead of copying large prompt or architecture sections.
5. Treat the vault `sources/docs/` tree as canonical and the repo `docs/` folder as archive-only.
6. Update dates when a stable fact changes.

## Good Candidates For PROJECT_CONTEXT.md
- Stage order
- Core architecture shape
- Stable code conventions
- Canonical doc locations
- Repeated verification commands

## Good Candidates For CURRENT_CONTEXT.md
- Current objective
- Files being edited
- Open risks
- Test commands for this work
- Best next step for the next session

## Avoid
- Long copied prompt text
- Per-turn troubleshooting logs
- Facts that are already obsolete or under active debate
- Reviving repo `docs/` as a parallel live documentation tree
