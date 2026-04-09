from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path


DEFAULT_VAULT_INDEX = Path(r"D:\ANHDUC\ADUC_vault\ADUC\log.md")
DEFAULT_VAULT_DAYS_DIR = Path(r"D:\ANHDUC\ADUC_vault\ADUC\sources\log\days")
DEFAULT_VAULT_GUIDE = Path(r"D:\ANHDUC\ADUC_vault\ADUC\sources\log\HOW_TO_WRITE.md")
DEFAULT_VAULT_DATA_HOLES = Path(r"D:\ANHDUC\ADUC_vault\ADUC\sources\log\DATA_HOLES.md")

DATE_HEADING_RE = re.compile(r"^#\s+(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
SUMMARY_RE = re.compile(r"^Summary:\s*(.+)\s*$", re.MULTILINE)
HOLE_OPEN_RE = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\] OPEN \| .+$", re.MULTILINE)


@dataclass(frozen=True)
class DailyLog:
    day: date
    summary: str
    path: Path


def read_text_normalized(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")


def read_daily_log(path: Path) -> DailyLog:
    text = read_text_normalized(path)
    date_match = DATE_HEADING_RE.search(text)
    if not date_match:
        raise ValueError(f"Missing '# YYYY-MM-DD' heading in {path}")
    summary_match = SUMMARY_RE.search(text)
    if not summary_match:
        raise ValueError(f"Missing 'Summary:' line in {path}")
    day = date.fromisoformat(date_match.group(1))
    expected_name = f"{day.isoformat()}.md"
    if path.name != expected_name:
        raise ValueError(f"Day-file name mismatch: expected {expected_name}, got {path.name}")
    return DailyLog(day=day, summary=summary_match.group(1).strip(), path=path)


def list_daily_logs(days_dir: Path) -> list[DailyLog]:
    if not days_dir.exists():
        return []
    logs = [read_daily_log(path) for path in days_dir.glob("*.md")]
    return sorted(logs, key=lambda item: item.day, reverse=True)


def build_log_index(logs: list[DailyLog]) -> str:
    lines = [
        "# Log",
        "",
        "> Navigation only. One line per day. Open the linked day file for the actual activity log.",
        "> The daily file is the log. This index is the map.",
        "",
        "- Guide | [sources/log/HOW_TO_WRITE.md](./sources/log/HOW_TO_WRITE.md)",
        "- Data holes | [sources/log/DATA_HOLES.md](./sources/log/DATA_HOLES.md)",
        "",
    ]
    for log in logs:
        lines.append(
            f"- {log.day.isoformat()} | {log.summary} | [entry](./sources/log/days/{log.path.name})"
        )
    return "\n".join(lines).rstrip() + "\n"


def build_day_template(day: date, summary: str) -> str:
    return (
        f"# {day.isoformat()}\n\n"
        f"Summary: {summary}\n\n"
        "## Activity\n"
    )


def describe(index_path: Path, days_dir: Path) -> str:
    logs = list_daily_logs(days_dir)
    index_state = "missing"
    if index_path.exists():
        index_state = f"{index_path.stat().st_size} bytes"
    day_range = "empty"
    if logs:
        day_range = f"{logs[-1].day.isoformat()}..{logs[0].day.isoformat()}"
    return (
        f"{index_path} | index={index_state}\n"
        f"{days_dir} | daily_files={len(logs)} | range={day_range}"
    )


def rebuild(index_path: Path, days_dir: Path, guide_path: Path, data_holes_path: Path) -> str:
    if not guide_path.exists():
        raise ValueError(f"Missing guide file: {guide_path}")
    if not data_holes_path.exists():
        raise ValueError(f"Missing data-holes file: {data_holes_path}")
    logs = list_daily_logs(days_dir)
    index_path.write_text(build_log_index(logs), encoding="utf-8")
    return f"rebuilt={len(logs)}"


def validate(index_path: Path, days_dir: Path, guide_path: Path, data_holes_path: Path) -> str:
    expected = build_log_index(list_daily_logs(days_dir))
    actual = read_text_normalized(index_path)
    if actual != expected:
        raise ValueError("Vault log index is stale. Run rebuild.")
    if not guide_path.exists():
        raise ValueError(f"Missing guide file: {guide_path}")
    if not data_holes_path.exists():
        raise ValueError(f"Missing data-holes file: {data_holes_path}")
    return "ok"


def ensure_day(days_dir: Path, target_day: date, summary: str) -> str:
    days_dir.mkdir(parents=True, exist_ok=True)
    day_path = days_dir / f"{target_day.isoformat()}.md"
    if day_path.exists():
        read_daily_log(day_path)
        return f"exists={day_path}"
    day_path.write_text(build_day_template(target_day, summary), encoding="utf-8")
    return f"created={day_path}"


def update_day_summary(day_path: Path, new_summary: str) -> None:
    """Replace the Summary: line in an existing day file."""
    text = read_text_normalized(day_path)
    updated, n = SUMMARY_RE.subn(f"Summary: {new_summary}", text, count=1)
    if n == 0:
        raise ValueError(f"No 'Summary:' line found in {day_path}")
    day_path.write_text(updated, encoding="utf-8")


def build_entry_block(
    entry_date: date,
    action: str,
    subject: str,
    project: str | None,
    body_lines: list[str],
) -> str:
    """Build a formatted log entry block ready to append to a day file."""
    lines = [f"\n## [{entry_date.isoformat()}] {action.upper()} | {subject}"]
    if project:
        lines.append(f"Project: {project}")
    lines.extend(body_lines)
    return "\n".join(lines) + "\n"


def append_entry(
    day_path: Path,
    entry_date: date,
    action: str,
    subject: str,
    project: str | None,
    body_lines: list[str],
) -> None:
    """Append a formatted entry block to an existing day file."""
    block = build_entry_block(entry_date, action, subject, project, body_lines)
    with day_path.open("a", encoding="utf-8") as f:
        f.write(block)


def log_entry(
    index_path: Path,
    days_dir: Path,
    guide_path: Path,
    data_holes_path: Path,
    entry_date: date,
    action: str,
    subject: str,
    project: str | None,
    body_lines: list[str],
    new_summary: str | None,
) -> str:
    """All-in-one: ensure-day → append entry → update summary → rebuild → validate."""
    day_path = days_dir / f"{entry_date.isoformat()}.md"
    ensure_day(days_dir, entry_date, new_summary or subject)
    append_entry(day_path, entry_date, action, subject, project, body_lines)
    if new_summary:
        update_day_summary(day_path, new_summary)
    rebuild(index_path, days_dir, guide_path, data_holes_path)
    validate(index_path, days_dir, guide_path, data_holes_path)
    return f"logged={entry_date.isoformat()} action={action} subject={subject!r}"


def add_hole(
    data_holes_path: Path,
    entry_date: date,
    title: str,
    description_lines: list[str],
) -> str:
    """Append a new OPEN hole entry to DATA_HOLES.md."""
    lines = [f"\n## [{entry_date.isoformat()}] OPEN | {title}"]
    lines.extend(description_lines)
    block = "\n".join(lines) + "\n"
    with data_holes_path.open("a", encoding="utf-8") as f:
        f.write(block)
    return f"added: {title!r}"


def close_hole(
    data_holes_path: Path,
    title_fragment: str,
    resolved_by: str,
    resolved_date: date,
) -> str:
    """Mark the first OPEN hole whose title contains title_fragment as RESOLVED."""
    text = read_text_normalized(data_holes_path)
    matches = list(HOLE_OPEN_RE.finditer(text))
    target = next(
        (m for m in matches if title_fragment.lower() in m.group(0).lower()),
        None,
    )
    if target is None:
        raise ValueError(f"No OPEN hole matching {title_fragment!r} in {data_holes_path}")
    old_heading = target.group(0)
    new_heading = old_heading.replace(" OPEN ", " RESOLVED ", 1)
    resolved_line = f"\nResolved: {resolved_date.isoformat()} by {resolved_by}"
    updated = text.replace(old_heading, new_heading + resolved_line, 1)
    data_holes_path.write_text(updated, encoding="utf-8")
    return f"closed: {old_heading!r}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate or rebuild the two-layer vault activity log."
    )
    parser.add_argument("--index", type=Path, default=DEFAULT_VAULT_INDEX)
    parser.add_argument("--days-dir", type=Path, default=DEFAULT_VAULT_DAYS_DIR)
    parser.add_argument("--guide", type=Path, default=DEFAULT_VAULT_GUIDE)
    parser.add_argument("--data-holes", type=Path, default=DEFAULT_VAULT_DATA_HOLES)
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("status")
    subparsers.add_parser("rebuild")
    subparsers.add_parser("validate")

    ensure_parser = subparsers.add_parser("ensure-day")
    ensure_parser.add_argument(
        "--date",
        dest="target_day",
        type=date.fromisoformat,
        default=date.today(),
        help="Day file to create in YYYY-MM-DD format. Defaults to today.",
    )
    ensure_parser.add_argument(
        "--summary",
        default="TODO",
        help="One-line summary for a new day file.",
    )

    entry_parser = subparsers.add_parser(
        "log-entry",
        help="All-in-one: ensure-day + append entry + rebuild + validate.",
    )
    entry_parser.add_argument(
        "--date",
        dest="entry_date",
        type=date.fromisoformat,
        default=date.today(),
        help="Entry date in YYYY-MM-DD format. Defaults to today.",
    )
    entry_parser.add_argument(
        "--action",
        required=True,
        help="Entry action keyword, e.g. FIX, REVIEW, UPDATE, INIT, INGEST.",
    )
    entry_parser.add_argument("--subject", required=True, help="Entry subject line.")
    entry_parser.add_argument(
        "--project",
        default=None,
        help="Optional project tag to include in the entry (e.g. pathfinder).",
    )
    entry_parser.add_argument(
        "--body",
        nargs="*",
        default=[],
        help="Body lines for the entry (one string per bullet, caller adds '- ' prefix).",
    )
    entry_parser.add_argument(
        "--update-summary",
        dest="new_summary",
        default=None,
        help="Rewrite the day-file Summary: line with this value.",
    )

    hole_parser = subparsers.add_parser("add-hole", help="Add a new OPEN gap to DATA_HOLES.md.")
    hole_parser.add_argument(
        "--date",
        dest="hole_date",
        type=date.fromisoformat,
        default=date.today(),
    )
    hole_parser.add_argument("--title", required=True, help="Short gap title.")
    hole_parser.add_argument(
        "--body",
        nargs="*",
        default=[],
        help="Description lines for the hole.",
    )

    close_parser = subparsers.add_parser(
        "close-hole",
        help="Mark a DATA_HOLES entry as RESOLVED.",
    )
    close_parser.add_argument(
        "--title",
        required=True,
        help="Fragment of the hole title to match (case-insensitive).",
    )
    close_parser.add_argument(
        "--resolved-by",
        required=True,
        help="Short reference to the resolution (log entry date, commit, etc.).",
    )
    close_parser.add_argument(
        "--date",
        dest="resolved_date",
        type=date.fromisoformat,
        default=date.today(),
        help="Resolution date in YYYY-MM-DD format. Defaults to today.",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "status":
            print(describe(args.index, args.days_dir))
            return 0
        if args.command == "rebuild":
            print(rebuild(args.index, args.days_dir, args.guide, args.data_holes))
            return 0
        if args.command == "validate":
            print(validate(args.index, args.days_dir, args.guide, args.data_holes))
            return 0
        if args.command == "ensure-day":
            print(ensure_day(args.days_dir, args.target_day, args.summary))
            return 0
        if args.command == "log-entry":
            print(
                log_entry(
                    args.index,
                    args.days_dir,
                    args.guide,
                    args.data_holes,
                    args.entry_date,
                    args.action,
                    args.subject,
                    args.project,
                    args.body,
                    args.new_summary,
                )
            )
            return 0
        if args.command == "add-hole":
            print(add_hole(args.data_holes, args.hole_date, args.title, args.body))
            return 0
        if args.command == "close-hole":
            print(
                close_hole(
                    args.data_holes,
                    args.title,
                    args.resolved_by,
                    args.resolved_date,
                )
            )
            return 0
    except ValueError as exc:
        parser.exit(status=2, message=f"error: {exc}\n")

    parser.exit(status=2, message=f"error: unknown command {args.command!r}\n")


if __name__ == "__main__":
    raise SystemExit(main())
