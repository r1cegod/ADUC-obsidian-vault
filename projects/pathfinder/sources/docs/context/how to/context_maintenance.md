# Context Maintenance

## File Roles
- `projects/pathfinder/sources/docs/context/docs/PROJECT_CONTEXT.md`: stable project facts that should survive session compaction.
- `projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md`: live working notes, blockers, and handoff details for the current cycle.
- `projects/pathfinder/sources/docs/DEV_LOG.md`: append-only engineering decision history.
- `D:\ANHDUC\Path_finder\docs (archived)\`: archived repo copy, not canonical.
- `D:\ANHDUC\Path_finder\logs\DEV_LOG.md`: repo mirror of the canonical dev log; update it in the same change whenever a new dev-log entry is added.

## Update Rules
1. Put stable architecture facts in `PROJECT_CONTEXT.md`.
2. Put active tasks, blockers, and "what to do next" in `CURRENT_CONTEXT.md`.
3. When a decision should survive beyond the current work cycle, also record it in `projects/pathfinder/sources/docs/DEV_LOG.md`.
4. Mirror the same dev-log entry into `D:\ANHDUC\Path_finder\logs\DEV_LOG.md` in the same update.
5. Link to source docs instead of copying large prompt or architecture sections.
6. Treat the vault `sources/docs/` tree as canonical and the repo `docs (archived)/` folder as archive-only, while keeping `D:\ANHDUC\Path_finder\logs\DEV_LOG.md` as the one required mirror.
7. Update dates when a stable fact changes.

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
- Reviving repo `docs (archived)/` as a parallel live documentation tree
