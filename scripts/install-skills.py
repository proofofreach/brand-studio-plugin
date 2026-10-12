#!/usr/bin/env python3
"""Link Brand Studio skills without copying them or modifying host settings."""
import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("copywriting", "designing", "brand-building")
HOST_DIRS = {"codex": ".agents", "claude": ".claude", "gemini": ".gemini", "shared": ".agents"}


def owned_link(target, source):
    return target.is_symlink() and target.resolve() == source


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("host", choices=HOST_DIRS)
    parser.add_argument("--scope", choices=("user", "project"), default="user")
    parser.add_argument("--destination", type=Path, help="Override the skills directory")
    parser.add_argument("--uninstall", action="store_true", help="Remove only links owned by this checkout")
    args = parser.parse_args()
    base = Path.home() if args.scope == "user" else Path.cwd()
    destination = (args.destination or base / HOST_DIRS[args.host] / "skills").expanduser().absolute()
    pairs = [(destination / name, ROOT / "skills" / name) for name in SKILLS]

    # Preflight the entire install, including conflicts with broken links.
    for target, source in pairs:
        if not args.uninstall and not (source / "SKILL.md").is_file():
            parser.exit(1, f"Missing source skill: {source}\n")
        if (target.exists() or target.is_symlink()) and not owned_link(target, source):
            parser.exit(1, f"Conflict: {target}. Existing content was left unchanged.\n")

    if args.uninstall:
        for target, source in pairs:
            if owned_link(target, source):
                target.unlink()
                print(f"Removed {target}")
        return

    created = []
    try:
        destination.mkdir(parents=True, exist_ok=True)
        for target, source in pairs:
            if owned_link(target, source):
                print(f"Already linked: {target}")
                continue
            target.symlink_to(source, target_is_directory=True)
            created.append((target, source))
            print(f"Linked {target} -> {source}")
    except OSError as error:
        for target, source in reversed(created):
            if owned_link(target, source):
                target.unlink()
        parser.exit(1, f"Installation failed: {error}. Newly created skill links were removed.\n")
    print("Restart or reload your agent to discover the skills. Keep this source directory in place.")


if __name__ == "__main__":
    try:
        main()
    except OSError as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
