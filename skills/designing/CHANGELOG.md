# Changelog

## 0.2.0 — provider portability

Author: gpt-6-astra (high). Independent reviewer: gpt-6.1-sol (xhigh), fresh context with fork_turns none. All five fixed scenarios for this skill passed; all 15 scenarios across the three skills passed with no material regressions. Acceptance gates on behavioral regressions, not stylistic preference. Evaluation used simulated tool capabilities and local SVG, alpha, and contrast fixtures; no actual image-provider calls were made. See [scenario results](../../docs/SKILL_SCENARIO_RESULTS.md).

| Files | Change | Why | Verified | Disposition |
| --- | --- | --- | --- | --- |
| tests/scenarios.md | Added five fixed behavior prompts before runtime edits | Exercise vector-only production, native alpha, missing export tools, bounded contrast correction, and audit evidence | Written before rewrite; fresh different-model behavioral validation passed | Kept; behavioral gate passed |
| SKILL.md | Replaced hardcoded image provider/tool list with capability-driven production and honest fallback; added vector, alpha, lettering, and verification distinctions | Support compatible hosts while preserving brand design principles and existing identity | Frontmatter validation and all four reference links pass; behavioral validation passed | Kept; behavioral gate passed |
| LOG.md; CHANGELOG.md; PURPOSE.md | Added separate run, change, and rule-purpose records | Keep maintenance evidence outside runtime instructions | Files are not linked from SKILL.md | Kept; behavioral gate passed |
| commands/design.md | Replaced a concise namespaced command wrapper with a real relative skill link | Remove orphan helpers and provider assumptions; preserve natural-language invocation on other hosts | Wrapper link resolves; host command loading is checked by release packaging | Kept; behavioral gate passed |

Rejected approaches: retain provider-specific mandatory tool names; require chroma-key generation; import campaign artifacts or unavailable private source libraries. These were rejected during design and were not added.
