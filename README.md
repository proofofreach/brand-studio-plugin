# Brand Studio

Portable agent skills for marketing copy, visual identity, and cohesive brand systems. Built by [Codeface Media](https://codefacemedia.com).

Brand Studio supplies the working methods and reference library. Your agent supplies the model and available tools. No particular model, image service, MCP server, or API key is required by the package.

| Skill | Use it for |
| --- | --- |
| `copywriting` | Headlines, landing pages, emails, ads, direct mail, offers, and copy reviews |
| `designing` | Logos, palettes, typography, visual identity, and asset specifications |
| `brand-building` | Coordinate strategy, design, and voice into a consistent brand kit |

## Install

Choose one installation route per host to avoid duplicate skill registrations.

### Claude Code plugin

```sh
claude plugin marketplace add https://github.com/ProofOfReach/brand-studio-plugin.git
claude plugin install brand-studio@brand-studio-local
```

The existing `brand-studio-local` marketplace name is preserved for current users. Restart Claude Code after installation. Invoke `/brand-studio:copy`, `/brand-studio:design`, or `/brand-studio:brand-kit`, or ask for a task matching a core skill.

### Codex plugin

```sh
codex plugin marketplace add https://github.com/ProofOfReach/brand-studio-plugin.git
codex plugin add brand-studio@brand-studio
```

Restart Codex, select a Brand Studio skill, or ask for a matching task. This route uses the portable root `plugin.json` and the Codex repository marketplace. It does not submit the package to OpenAI's public directory.

### Local skills: Codex, Claude Code, or Gemini CLI

Keep one checkout as the canonical source:

```sh
git clone https://github.com/ProofOfReach/brand-studio-plugin.git
cd brand-studio-plugin
python3 scripts/install-skills.py codex
# Or: python3 scripts/install-skills.py claude
# Or: python3 scripts/install-skills.py gemini
```

The installer requires Python 3.9+ and permission to create directory symlinks. It links the three complete skill folders; it does not copy them, edit agent settings, install tools, or read credentials. Windows users may need Developer Mode or an elevated shell for symlink creation.

| Target | User location | Project location |
| --- | --- | --- |
| `codex` or `shared` | `~/.agents/skills/` | `.agents/skills/` |
| `claude` | `~/.claude/skills/` | `.claude/skills/` |
| `gemini` | `~/.gemini/skills/` | `.gemini/skills/` |

For project scope, run the installer from the project directory:

```sh
python3 /path/to/brand-studio-plugin/scripts/install-skills.py codex --scope project
```

Use `--destination /path/to/skills` for another Agent Skills-compatible host. Existing unrelated files, directories, or links block installation; the installer never overwrites them. Keep the checkout in place and reload your host's skills. For Gemini CLI, use `/skills reload` and `/skills list`.

Remove only this checkout's links with the same target and scope:

```sh
python3 scripts/install-skills.py codex --uninstall
```

Use the host's plugin uninstall command if you chose a plugin installation. Updating the checkout updates linked skills; plugin users should refresh the marketplace and update through their host.

Installation locations follow [Codex's skill documentation](https://learn.chatgpt.com/docs/build-skills), [Claude Code's plugin documentation](https://code.claude.com/docs/en/plugins-reference), and [Gemini CLI's skills documentation](https://geminicli.com/docs/cli/skills/).

## Use

Examples work as ordinary requests after installation; slash-command syntax is host-specific.

- “Use copywriting to improve this landing page. Preserve the facts and do not invent results.”
- “Use designing to create an icon-only SVG mark and an accessible color palette for this brand.”
- “Use brand-building to produce a concise brand kit from this audience, positioning, and product brief.”
- “Write a postcard and sales letter for this offer using the supplied customer research.”

The skills use supplied context first and load references only when relevant. If browsing is available, research can use it. Without browsing, the agent works from supplied material and labels unanswered research questions. If image generation is available, the design skill can use it. Without it, the agent can create suitable vector assets or provide concepts and production specifications, without claiming to have rendered images.

For raster assets needing transparency, the agent checks the tool's actual output rather than assuming that every image provider has the same capabilities. Provider-specific workarounds are conditional. Print color conversions and editorial scores are estimates, not press proofs or conversion forecasts.

## Compatibility and verification

| Surface | Release verification |
| --- | --- |
| Codex CLI | Native marketplace installation and discovery; local skill installation |
| Claude Code | Native manifest validation and marketplace installation; local skill installation |
| Gemini CLI | Documented discovery layout and local installation; native Gemini execution not tested |
| Other Agent Skills hosts | Portable `SKILL.md` files and complete relative resources; host-specific behavior not certified |
| Image/search providers | Capability-based instructions; no image or search service bundled |

The core workflows are Markdown and need no shell. Optional copy-audit helpers require Bash and standard Unix tools; the landing-page scorer requires Bash 4+. Their scores are editorial heuristics; they do not establish commercial results or release readiness.

Run the local packaging checks:

```sh
python3 tests/release_e2e.py --artifact /tmp/brand-studio-release-e2e.json
claude plugin validate .claude-plugin/plugin.json --strict
claude plugin validate .claude-plugin/marketplace.json --strict
```

See [release verification](docs/RELEASE_VERIFICATION.md) for behavioral scenarios, native host versions, and remaining limits. Per-skill `tests/scenarios.md` files define repeatable behavioral checks. `LOG.md`, `CHANGELOG.md`, and `PURPOSE.md` are maintenance records, not runtime instructions.

## License

[MIT](LICENSE) covers this package. Named frameworks and authors are attributed in the reference material; their original works, fonts, trademarks, and generated assets retain their own applicable rights.
