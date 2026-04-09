# Context Maintenance

## File Roles
- `projects/pathfinder/sources/docs/context/docs/PROJECT_CONTEXT.md`: stable project facts that should survive session compaction.
- `projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md`: live working notes, blockers, and handoff details for the current cycle.
- `projects/pathfinder/sources/docs/DEV_LOG.md`: navigation index for the canonical project dev log.
- `projects/pathfinder/sources/docs/dev-log/days/`: the actual canonical project dev-log day files.
- `D:\ANHDUC\Path_finder\docs (archived)\`: archived repo copy, not canonical.
- `D:\ANHDUC\Path_finder\logs\DEV_LOG.md`: repo mirror index of the canonical dev log.
- `D:\ANHDUC\Path_finder\logs\dev\days\`: repo mirror day files for the project dev log.

## Update Rules
1. Put stable architecture facts in `PROJECT_CONTEXT.md`.
2. Put active tasks, blockers, and "what to do next" in `CURRENT_CONTEXT.md`.
3. When a decision should survive beyond the current work cycle, record it in the current day file under `projects/pathfinder/sources/docs/dev-log/days/`.
4. Mirror the same day-file update into `D:\ANHDUC\Path_finder\logs\dev\days\` in the same change.
5. Rebuild the paired `DEV_LOG.md` indexes after the day-file update with `python scripts\manage_dev_log.py rebuild`.
6. Link to source docs instead of copying large prompt or architecture sections.
7. Treat the vault `sources/docs/` tree as canonical and the repo `docs (archived)/` folder as archive-only, while keeping `D:\ANHDUC\Path_finder\logs\DEV_LOG.md` as the one required mirror.
8. Update dates when a stable fact changes.

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
