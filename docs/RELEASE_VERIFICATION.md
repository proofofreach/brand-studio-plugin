# Brand Studio 0.2.0 verification

This release separates portable skill behavior from host installation support. A passing packaging check does not prove a particular model's creative quality or a third-party image service's reliability.

## Local gates

| Gate | Result | Repeatable evidence |
| --- | --- | --- |
| Skill frontmatter | All three pass the skill-creator validator | Run `quick_validate.py` from the skill-creator skill with PyYAML installed |
| Relative runtime links | Core skills and command links resolve | Inspect links relative to each Markdown file |
| Portable plugin manifest | Passes the Agent Plugins 1.0.0 JSON schema | Validate `plugin.json` against its declared `$schema` |
| Claude manifests | Strict validation passes | `claude plugin validate .claude-plugin/plugin.json --strict` and the marketplace equivalent |
| Installer | Fresh installation, repeat installation, removal, path spaces, conflicting files/directories/broken links, project scope, unknown hosts, and missing sources pass | `python3 tests/release_e2e.py --artifact /tmp/brand-studio-release-e2e.json` |
| Native Codex installation | Local marketplace registration, installation, and discovery pass on Codex CLI 0.162.1 | Use a temporary `CODEX_HOME`, register the repository, install `brand-studio@brand-studio`, then list plugins |
| Native Claude installation | Local marketplace registration and installation pass on Claude Code 2.1.296 | Use a temporary `CLAUDE_CONFIG_DIR`, register the repository, then install `brand-studio@brand-studio-local` |
| Gemini installation layout | Skill links and resources pass installer checks | Native Gemini CLI/model execution was not performed |
| Behavioral regressions | All 15 fixed scenarios pass fresh-context review by gpt-6.1-sol after gpt-6-astra authored the rewrite | Fixed cases live in each skill's `tests/scenarios.md`; see [scenario results](SKILL_SCENARIO_RESULTS.md) |

Native installation tests use isolated configuration directories. They do not modify the maintainer's normal plugin settings. No paid GitHub runner or workflow is required by these gates.

## Release boundary

- The core workflows use Markdown; image, search, inspection, and file capabilities come from the host.
- Behavioral evaluation simulates declared tool capabilities. It does not certify every image or search provider.
- Optional copy helpers require a Unix shell. The landing-page scorer requires Bash 4+ and identifies older Bash explicitly; core skills do not require these helpers.
- The installer uses symlinks to one canonical source and refuses unrelated collisions. Keep the source directory in place. Symlink support on Windows depends on local permissions.
- No credentials, MCP servers, campaign files, books, or generated customer assets are included in the release package.
- This is a GitHub source release. It is not a submission to OpenAI's public plugin directory or a certification by an agent provider.

## Build and verify an archive

From a clean Git checkout at the release commit:

```sh
python3 scripts/build-release.py --output /tmp/brand-studio-release
```

The builder uses tracked files from `HEAD`, verifies required package files, excludes Git metadata and environment files, and writes a SHA-256 checksum. Unpack the resulting ZIP into a temporary directory and rerun `tests/release_e2e.py` there before publishing.
