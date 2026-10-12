#!/usr/bin/env python3
"""Exercise complete installer commands against temporary skill registries."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import shutil

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("copywriting", "designing", "brand-building")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, required=True)
    args = parser.parse_args()
    checks = []

    def run(*arguments, expected=0, cwd=None):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/install-skills.py"), *arguments],
            cwd=cwd, capture_output=True, text=True,
        )
        assert result.returncode == expected, result.stdout + result.stderr
        return result

    with tempfile.TemporaryDirectory(prefix="brand studio e2e ") as workspace:
        workspace = Path(workspace)
        for host in ("codex", "claude", "gemini", "shared"):
            destination = workspace / host / "skill registry"
            run(host, "--destination", str(destination))
            for name in SKILLS:
                target = destination / name
                assert target.is_symlink()
                assert target.resolve() == ROOT / "skills" / name
                assert (target / "SKILL.md").is_file()
            before = {name: os.readlink(destination / name) for name in SKILLS}
            run(host, "--destination", str(destination))
            assert before == {name: os.readlink(destination / name) for name in SKILLS}
            run(host, "--destination", str(destination), "--uninstall")
            assert not any((destination / name).is_symlink() for name in SKILLS)
            checks.append({"case": f"{host}: install, repeat, uninstall", "passed": True})

        for collision in ("directory", "file", "broken-link"):
            destination = workspace / collision
            destination.mkdir()
            target = destination / "designing"
            if collision == "directory":
                target.mkdir()
                (target / "mine.txt").write_text("keep")
            elif collision == "file":
                target.write_text("keep")
            else:
                target.symlink_to(workspace / "missing")
            run("codex", "--destination", str(destination), expected=1)
            assert not (destination / "copywriting").exists()
            assert not (destination / "brand-building").exists()
            run("codex", "--destination", str(destination), "--uninstall", expected=1)
            assert target.exists() or target.is_symlink()
            checks.append({"case": f"preserve conflicting {collision}", "passed": True})

        project = workspace / "project"
        project.mkdir()
        for host, folder in (("codex", ".agents"), ("claude", ".claude"), ("gemini", ".gemini")):
            run(host, "--scope", "project", cwd=project)
            assert all((project / folder / "skills" / name).is_symlink() for name in SKILLS)
            run(host, "--scope", "project", "--uninstall", cwd=project)
        checks.append({"case": "project scope for each host", "passed": True})
        run("unknown-host", expected=2)
        checks.append({"case": "unknown target rejected", "passed": True})

        damaged = workspace / "damaged source"
        (damaged / "scripts").mkdir(parents=True)
        shutil.copy2(ROOT / "scripts/install-skills.py", damaged / "scripts/install-skills.py")
        shutil.copytree(ROOT / "skills", damaged / "skills")
        (damaged / "skills/designing/SKILL.md").unlink()
        destination = workspace / "missing-source-target"
        result = subprocess.run([
            sys.executable, str(damaged / "scripts/install-skills.py"), "shared", "--destination", str(destination),
        ], capture_output=True, text=True)
        assert result.returncode == 1 and "Missing source skill" in result.stderr
        assert not destination.exists()
        checks.append({"case": "missing source rejected before any writes", "passed": True})

    manifests = [ROOT / "plugin.json", ROOT / ".claude-plugin/plugin.json"]
    for manifest in manifests:
        data = json.loads(manifest.read_text())
        assert data["name"] == "brand-studio" and data["version"] == "0.2.0"
        assert data["license"] == "MIT"
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    assert marketplace["plugins"][0]["version"] == "0.2.0"
    assert marketplace["plugins"][0]["source"] == "./"
    assert (ROOT / "LICENSE").is_file()
    checks.append({"case": "consistent version and license metadata", "passed": True})
    report = {"passed": True, "checks": checks}
    args.artifact.parent.mkdir(parents=True, exist_ok=True)
    args.artifact.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
