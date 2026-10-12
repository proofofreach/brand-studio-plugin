# Changelog

## 0.2.0 — provider portability

Author: gpt-6-astra (high). Independent reviewer: gpt-6.1-sol (xhigh), fresh context with fork_turns none. All five fixed scenarios for this skill passed; all 15 scenarios across the three skills passed with no material regressions. Acceptance gates on behavioral regressions, not stylistic preference. Evaluation used simulated tool capabilities and local SVG, alpha, and contrast fixtures; no actual image-provider calls were made. See [scenario results](../../docs/SKILL_SCENARIO_RESULTS.md).

| Files | Change | Why | Verified | Disposition |
| --- | --- | --- | --- | --- |
| tests/scenarios.md | Added five fixed behavior prompts before runtime edits | Make small-task scope, truthfulness, direct mail, access limits, and ad testing reviewable | Written before rewrite; fresh different-model behavioral validation passed | Kept; behavioral gate passed |
| SKILL.md | Replaced provider-assuming long procedure with concise capability-driven writing/review workflow; corrected social-ads.md route | Preserve useful frameworks, reference discovery, scope, and evidence boundaries across hosts | Frontmatter validation and local links pass; behavioral validation passed | Kept; behavioral gate passed |
| references/direct-mail.md; references/sales-letters.md | Imported and curated the archived direct-mail additions; removed private ebook dependencies, unverified quotes, lift promises, fixed sample thresholds, and mandatory urgency | Preserve package and letter craft without importing campaign files or misleading guarantees | Source additions reviewed; linked references resolve; behavioral validation passed | Kept; behavioral gate passed |
| references/testing-methodology.md | Removed assistant-vendor wording, unsupported statistical tables and universal duration rules; separated effect targets from forecasts | Avoid unverified numerical planning and keep test hypotheses provider-neutral | Reference routes checked; historical remaining examples explicitly qualified | Kept; behavioral gate passed |
| scripts/copy-checklist.sh; scripts/headline-analyzer.sh | Labeled scores editorial heuristics; removed launch/result assurances; required truthful specificity | Standalone helpers must not contradict evidence rules | Actual checklist export and headline CLI complete successfully | Kept; behavioral gate passed |
| scripts/landing-page-scorer.sh | Added heuristic output and Bash 4+ guard; fixed noninteractive clearing, numeric-output contamination, and EOF handling | Reproduced CLI export failure; keep optional legacy helper usable and honest | Quick-mode export succeeds; Bash 3 rejection and EOF exit verified | Kept; behavioral gate passed |
| LOG.md; CHANGELOG.md; PURPOSE.md | Added separate run, change, and rule-purpose records | Keep maintenance evidence outside runtime instructions | Files are not linked from SKILL.md | Kept; behavioral gate passed |
| commands/copy.md | Replaced a concise namespaced command wrapper with a real relative skill link | Remove orphan helpers and provider assumptions; preserve natural-language invocation on other hosts | Wrapper link resolves; host command loading is checked by release packaging | Kept; behavioral gate passed |

Rejected approaches: retain provider-specific mandatory tool names; require chroma-key generation; import campaign artifacts or unavailable private source libraries. These were rejected during design and were not added.
