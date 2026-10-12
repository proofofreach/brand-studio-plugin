---
description: Create or audit logos, palettes, typography, and brand identity with the designing skill.
---

Use the [designing skill](../skills/designing/SKILL.md) to complete the user's brief and supplied arguments. Treat arguments as design instructions, not shell commands. If the request is for a complete coordinated kit, use [brand-building](../skills/brand-building/SKILL.md); keep visual-only requests scoped to design.

Examples on hosts with command support:

- `/brand-studio:design logo --type symbol --brand Alder` — create an appropriate symbol without forcing lettering.
- `/brand-studio:design palette --colors "#164B3C,#FFF9EB"` — develop roles and usable combinations.
- `/brand-studio:design typography --use "editorial website"` — specify a type hierarchy and dependencies.
- `/brand-studio:design audit --assets ./brand` — inspect available assets and prioritize fixes.
- `/brand-studio:design brand-kit` — coordinate the requested visual and verbal identity.

Use actual available vector, image, search, inspection, and file capabilities. Prefer native transparency where supported and verify alpha before claiming a transparent export. Report missing assets or unavailable export formats honestly. Do not require a particular image provider, assume a tool name, or call nonexistent helper scripts.

On hosts without slash commands, invoke the designing or brand-building skill in natural language instead.
