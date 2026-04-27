#!/usr/bin/env python3
"""
check_propagation.py — PostToolUse vault propagation checker.

Fires after every Write/Edit tool call via Claude Code PostToolUse hook.
Reads tool input from stdin (JSON), extracts file_path,
looks up propagation targets from EXACT_RULES and PATTERN_RULES,
and prints what still needs updating.

Never raises — agent must never be blocked by this script.

Maintenance: when you add a new structural node to the vault,
add an entry to EXACT_RULES and update the inverse relationships.
See SCHEMA.md -> Propagation Sync Matrix for the full table.
"""

import json
import sys
from pathlib import Path

VAULT_ROOT = "D:/ANHDUC/ADUC_vault/ADUC"
VAULT_ROOT_CANDIDATES = [
    Path(VAULT_ROOT),
    Path("/mnt/d/ANHDUC/ADUC_vault/ADUC"),
]

# Exact-path rules
# Key: vault-relative path (forward slashes, no leading slash)
# Value: list of (target, reason) tuples. Empty list = terminal node.
EXACT_RULES = {
    "briefing.md": [
        ("context/now.md", "Active Projects must match between briefing and context/now"),
    ],
    "context/now.md": [
        ("briefing.md",  "Active Projects must match between context/now and briefing"),
        ("index.md",     "Vault Status changes may require index header update"),
    ],
    "SCHEMA.md": [
        ("CLAUDE.md",  "Rule changes in SCHEMA must be reflected in CLAUDE.md wrapper"),
        ("AGENTS.md",  "Rule changes in SCHEMA must be reflected in AGENTS.md wrapper"),
    ],
    "CLAUDE.md": [
        ("AGENTS.md",  "Behavioral rules must be consistent across agent entry points"),
    ],
    "AGENTS.md": [
        ("CLAUDE.md",  "Behavioral rules must be consistent across agent entry points"),
    ],
    "development.md": [
        ("briefing.md", "Development-domain routing should stay visible from the vault entrypoint"),
        ("AGENTS.md", "Codex wrapper must route technical help and delegation through Development"),
        ("CLAUDE.md", "Claude wrapper must route technical help and delegation through Development"),
        ("wiki/operations-hub.md", "Operation registry must expose the Development domain and leaves"),
        ("index.md", "Index must list the Development domain and operation leaves"),
    ],
    "wiki/operations/branch-growth-operation.md": [
        ("vault-keeping.md", "Maintenance router must expose Branch Growth before File Creation Gate"),
        ("wiki/operations-hub.md", "Operation registry must expose Branch Growth"),
        ("wiki/operations/file-creation-gate.md", "File Creation Gate must start after parent-branch selection"),
        ("wiki/operations/project-init-operation.md", "Project Init must use Branch Growth for project roots and initial hubs"),
        ("index.md", "Index must list the Branch Growth operation"),
    ],
    # Terminal nodes — nothing downstream, listed explicitly so agents know they're done
    "context/hot.md":  [],
    "context/me.md":   [],
    "context/goals.md": [],
    "index.md":        [],
    "log.md":          [],
}

# Pattern rules — checked in order, ALL matching rules fire (not first-match-only)
PATTERN_RULES = [
    {
        # projects/*/README.md  →  briefing + context/now
        "match": lambda p: (
            p.startswith("projects/")
            and p.endswith("/README.md")
            and p.count("/") == 2
        ),
        "targets": [
            ("briefing.md",    "Project status changes propagate to Active Projects list"),
            ("context/now.md", "Project status changes propagate to Active Projects list"),
        ],
    },
    {
        # Hub notes  →  parent project README
        "match": lambda p: (
            p.startswith("projects/")
            and "/notes/" in p
            and p.endswith("-hub.md")
        ),
        "targets_fn": lambda p: [
            (
                p.split("/notes/")[0] + "/README.md",
                "Hub routing changes may require README task-router update",
            )
        ],
    },
    {
        # Canvas boards  →  project architecture hub + parent project README
        "match": lambda p: (
            p.startswith("projects/")
            and "/notes/" in p
            and p.endswith(".canvas")
        ),
        "targets_fn": lambda p: [
            (
                p.split("/notes/")[0] + "/notes/" + p.split("/")[1] + "-architecture-hub.md",
                "Canvas routing changes should stay explicit through the project architecture hub",
            ),
            (
                p.split("/notes/")[0] + "/README.md",
                "Canvas work should remain discoverable from the project README router",
            ),
        ],
    },
    {
        # Day log files  →  log.md nav index
        "match": lambda p: p.startswith("sources/log/days/"),
        "targets": [
            ("log.md", "Day file write requires navigation line sync in log.md"),
        ],
    },
    {
        # Wiki pages  →  index.md
        "match": lambda p: p.startswith("wiki/") and p.endswith(".md"),
        "targets": [
            ("index.md", "Verify index.md entry exists and is current"),
        ],
    },
    {
        # Project leaf notes  →  index.md
        "match": lambda p: (
            p.startswith("projects/")
            and "/notes/" in p
            and p.endswith(".md")
        ),
        "targets": [
            ("index.md", "Verify index.md entry exists and parent hub TL;DR is current"),
        ],
    },
    {
        # References  →  index.md
        "match": lambda p: p.startswith("references/") and p.endswith(".md"),
        "targets": [
            ("index.md", "Verify index.md entry exists and is current"),
        ],
    },
]


def is_durable_entry(rel_path: str) -> bool:
    """Return whether a path is a durable navigable vault entry."""
    if not rel_path.endswith(".md"):
        return False
    if rel_path.startswith("sources/log/days/"):
        return False
    if rel_path.startswith("journal/daily/"):
        return False
    return rel_path.startswith(("wiki/", "projects/", "references/", "learning/"))


def vault_path(rel_path: str) -> Path | None:
    """Resolve a vault-relative path on Windows or WSL."""
    for root in VAULT_ROOT_CANDIDATES:
        candidate = root / rel_path
        if candidate.exists():
            return candidate
    return None


def has_growth_contract(rel_path: str) -> bool | None:
    """Return whether the file contains a Growth Contract, if readable."""
    path = vault_path(rel_path)
    if path is None or not path.is_file():
        return None
    try:
        in_fence = False
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            stripped = line.strip()
            if stripped.startswith("```"):
                in_fence = not in_fence
                continue
            if not in_fence and stripped == "## Growth Contract":
                return True
        return False
    except Exception:
        return None


def print_growth_contract_reminder(rel_path: str) -> None:
    """Remind agents that new durable entries must be branch-aware."""
    if not is_durable_entry(rel_path):
        return

    print("\nENTRY GROWTH CONTRACT")
    growth_contract = has_growth_contract(rel_path)
    if growth_contract is False:
        print("  BLOCKER: no actual ## Growth Contract heading found in this file.")
        print("  Add it before considering the write complete.")
    elif growth_contract is None:
        print("  CHECK: file could not be read; confirm the contract manually.")
    else:
        print("  OK: actual ## Growth Contract heading found.")
    print("  Durable entries must carry:")
    print("  → parent branch")
    print("  → node role")
    print("  → first parent link")
    print("  → growth trigger")
    print("  → forbidden contents")
    print("  → expected child types or source/evidence boundary when relevant")


def normalize(path_str: str) -> str:
    """Convert absolute or mixed-slash path to vault-relative forward-slash path."""
    p = path_str.replace("\\", "/")
    for root in VAULT_ROOT_CANDIDATES:
        vault = str(root).replace("\\", "/").rstrip("/")
        if p.startswith(vault):
            return p[len(vault):].lstrip("/")
    # Already relative or unknown root — return as-is
    return p


def check(rel_path: str) -> None:
    targets: list[tuple[str, str]] = []

    if rel_path in EXACT_RULES:
        targets = list(EXACT_RULES[rel_path])
    else:
        for rule in PATTERN_RULES:
            if rule["match"](rel_path):
                if "targets_fn" in rule:
                    targets.extend(rule["targets_fn"](rel_path))
                else:
                    targets.extend(rule["targets"])

    if not targets:
        if rel_path in EXACT_RULES:
            print(f"\n✓ {rel_path} — terminal node. No propagation required.")
        else:
            print(f"\n✓ {rel_path} — leaf note. Confirm index.md entry exists.")
        print_growth_contract_reminder(rel_path)
        return

    print(f"\n⚡ PROPAGATION REQUIRED after writing: {rel_path}")
    for target, reason in targets:
        print(f"  → {target}")
        print(f"     {reason}")
    print_growth_contract_reminder(rel_path)


def main() -> None:
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return
        data = json.loads(raw)
        tool_input = data.get("tool_input") or {}
        file_path = tool_input.get("file_path", "")
        if file_path:
            check(normalize(file_path))
    except Exception:
        pass  # Never block the agent


if __name__ == "__main__":
    main()
