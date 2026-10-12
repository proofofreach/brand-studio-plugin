# Packaging failure cases

Write these before implementing the installer. Verify the complete command-line flow in a temporary workspace, not isolated helper functions.

1. A fresh Codex, Claude Code, Gemini CLI, or shared installation must expose all three complete skill directories from one canonical source. Reference files must remain reachable. Paths with spaces must work.
2. Repeating installation must preserve existing links. An unrelated directory, file, or broken link at any target must block the entire installation without overwriting anything or installing a partial set.
3. Uninstall must remove only links owned by this checkout. Unrelated files and links must survive. A failure partway through installation must roll back only links created by that invocation.
4. The installer must not clone code, pull updates, write provider settings, load credentials, or contact the network. Project scope must write only inside the selected project. Unknown options and missing source skills must fail clearly.
5. The public release archive must contain the manifests, commands, skills, references, scripts, license, and installation instructions. It must exclude local campaign materials, secrets, git metadata, and runtime evidence.

Run `python3 tests/release_e2e.py --artifact /tmp/brand-studio-release-e2e.json` for repeatable installation evidence. Native host validation and behavioral scenario evidence are recorded separately in `docs/RELEASE_VERIFICATION.md`.
