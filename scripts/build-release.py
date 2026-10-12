#!/usr/bin/env python3
"""Build a source release from a clean commit and write its SHA-256 checksum."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    status = subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True)
    if status:
        parser.exit(1, "Commit or remove pending changes before building a release.\n")
    version = json.loads((ROOT / "plugin.json").read_text())["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        parser.exit(1, "The manifest must have a stable semantic version.\n")
    prefix = f"brand-studio-v{version}/"
    args.output.mkdir(parents=True, exist_ok=True)
    archive = args.output / f"brand-studio-v{version}.zip"
    checksum = archive.with_suffix(".zip.sha256")
    if archive.exists() or checksum.exists():
        parser.exit(1, f"Release output already exists: {archive}\n")
    content = subprocess.check_output([
        "git", "archive", "--format=zip", f"--prefix={prefix}", "HEAD",
    ], cwd=ROOT)
    archive.write_bytes(content)
    with zipfile.ZipFile(archive) as bundle:
        names = bundle.namelist()
        required = ["plugin.json", ".claude-plugin/plugin.json", ".agents/plugins/marketplace.json", "LICENSE", "README.md", "scripts/install-skills.py"]
        required += [f"skills/{name}/SKILL.md" for name in ("copywriting", "designing", "brand-building")]
        if any(prefix + name not in names for name in required):
            archive.unlink()
            parser.exit(1, "Release archive is missing required files.\n")
        if any(Path(name).name.startswith(".env") or "/.git/" in name for name in names):
            archive.unlink()
            parser.exit(1, "Release archive contains a prohibited private file.\n")
    checksum.write_text(f"{hashlib.sha256(content).hexdigest()}  {archive.name}\n")
    print(archive)
    print(checksum)


if __name__ == "__main__":
    main()
