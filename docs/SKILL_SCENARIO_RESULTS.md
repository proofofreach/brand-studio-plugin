# Skill scenario results

Release candidate: 0.2.0. Date: 2026-10-12.

Gate: **PASS — 15/15 scenarios; no material behavioral regressions.** Reviewer: `gpt-6.1-sol` at `xhigh`, fresh agent (`fork_turns: none`). Author: `gpt-6-astra` at `high`. Each case produced an actual response, which the reviewer inspected against the fixed expected behavior in the corresponding `tests/scenarios.md`.

This is bounded behavioral simulation using only each scenario's declared capabilities and fixtures. Native raster transparency used a deterministic local tool stub; its PNG alpha and light/dark edges were inspected. The geometric SVG was rendered at 24 px and in reverse. Gray text contrast was calculated from sRGB values. No external search, image service, publication, or spend occurred. This gate does not establish native execution across Claude, Gemini, or every provider model/runtime.

| Skill / case | Result | Observation |
| --- | --- | --- |
| copywriting-1 | PASS | Exactly three calm headlines; no discovery questions, invented trial terms, research, or metrics. |
| copywriting-2 | PASS | Ranking, results, customer count, and cancellation promise removed; verified SMS/$12 offer retained. |
| copywriting-3 | PASS | Letter, plain identified envelope, PS, and reply card agree; direct-mail and sales-letter references used; missing address is explicit. |
| copywriting-4 | PASS | Requests page text/attachment and claims no inspection. |
| copywriting-5 | PASS | Two angles with distinct hypotheses; social-ads and testing references used; primary business metric, guardrails, and conditional stopping rule; no count threshold or launch. |
| designing-1 | PASS | Editable icon-only paths, exact green, no bitmap/fonts; actual 24 px and reversed renders inspected; no clearance claim. |
| designing-2 | PASS | Native transparency option used in stub; actual fixture alpha and light/dark edge previews inspected; raster/fixture limits explicit. |
| designing-3 | PASS | Fixture opaque RGB result reported; no undocumented parameter invented; transparent deliverable remains incomplete with useful handoff. |
| designing-4 | PASS | Only text color changes; actual sRGB calculations 4.478:1 to 4.542:1; scope limited to this normal-text pair. |
| designing-5 | PASS | Requests inaccessible inputs; does not invent inspection, uniqueness, licensing, or legal clearance. |
| brand-building-1 | PASS | Complete concise strategy, visual specifications, voice examples, and applications; concepts are not generated assets; no phases/providers/research claims. |
| brand-building-2 | PASS | Approved icon-only mark, palette, name, and tone preserved; one guide/two captions; missing specifications remain placeholders. |
| brand-building-3 | PASS | Useful core kit and actual unrendered SVG despite absent siblings; no price, count, image output, or rights claim invented. |
| brand-building-4 | PASS | Supplied uninspected sources, proposed cream, actual Markdown, and missing PNG/PDF exports distinguished; useful source and precise handoff provided. |
| brand-building-5 | PASS | Exactly three candidates, provisional choice, coherent starter kit; availability unverified; no approvals or registrations. |

Evidence is retained in `/tmp/brand-studio-forward-tests`: `results.json` contains prompts, expected behavior, per-case assessments, and source/response SHA-256 values. The 15 Markdown responses, SVG sources, render/edge previews, fixture tool trace, contrast calculation, and `packaging-e2e.json` are retained alongside it. Text-only cases' response files are evaluator records, not file capabilities claimed by those simulated hosts. Release publication may attach this evidence bundle.

The installer CLI E2E passed its 11 recorded checks. Command routing and manifests were reviewed with no release blocker found. Native host installation/discovery and the exact final source archive are separate release checks owned by the release operator. No font/trademark clearance or real image-provider output was certified by these tests.
