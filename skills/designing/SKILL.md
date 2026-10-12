---
name: designing
description: Create and critique brand identity assets, logos, color palettes, typography, and visual guidelines. Use for visual branding and focused identity audits, with outputs matched to available image, vector, file, and inspection capabilities.
---

# Designing

Produce a distinctive visual identity or focused asset that fits the audience, brand, and intended use. Preserve accepted identity choices unless the user requests a change. Scale the process to the task; a palette fix does not need a full discovery workshop.

## Establish direction

Read the brief and available brand documents. Identify audience, positioning, personality, required applications, and output constraints. Use existing decisions first. Ask only when a missing choice materially blocks useful work; otherwise proceed with explicit assumptions.

For a new identity, explore a small set of genuinely different ideas when useful, explain the tradeoffs, and recommend a direction. For a selected concept or narrow edit, refine it directly. Do not require an approval checkpoint for every phase. Use any available competitive research as evidence, not as permission to imitate; label unresearched differentiation as a design judgment. Visual similarity checks do not establish trademark clearance.

## Choose an available production path

Inspect the capabilities and documented tool schemas exposed by the current host. Tool names and parameter names differ; do not assume a particular model, provider, MCP server, image generator, or browser exists.

- **Vector work:** Prefer editable SVG or another supported vector format for geometric marks, simple icons, diagrams, and precise wordmark construction when suitable. Use available drawing/file tools, or deliver SVG source in the response if file writing is unavailable. An SVG containing an embedded bitmap is not an editable vector logo. Identify live-font dependencies; do not claim text was outlined unless it was.
- **Raster work:** Use an available image-generation/editing capability for illustrative marks, mascots, textures, concept exploration, and mockups. Follow its native instructions, supply relevant references, and inspect the result when possible. A prompt requesting “vector style” still produces raster output unless the actual file is vector.
- **No image generator:** Complete suitable vector assets and written specifications with available tools. For work needing raster generation, provide a precise art direction or generation prompt and state that the image has not been produced. Do not imply a concept description is a finished visual or demand an unrelated installation.
- **Search and files:** Use available search for requested/current references, source verification, or licensing checks. Without it, use supplied evidence and label gaps. If an audit depends on inaccessible assets or URLs, request those materials rather than inventing findings. Save or export only formats the host can actually produce; distinguish source, preview, and final exports.

Image prompts should specify subject, visual idea, composition, palette, intended scale, output needs, and exclusions. Include exact lettering only for a wordmark or lockup that calls for it. Symbol-only marks, favicons, and icons need not contain the brand name.

## Transparency and asset integrity

When transparency is required, use a tool's documented native transparent-background option first. Preserve alpha when editing an existing transparent asset unless the user requests otherwise.

Verify the actual file when inspection is available: format, dimensions, alpha channel and transparent pixels, and edge quality on light and dark backgrounds. An alpha channel with every pixel opaque is not a transparent result. A white background or painted checkerboard is not transparency. If inspection is unavailable, say transparency is requested but unverified; do not claim a verified transparent export.

If native transparency is unsupported or fails, use an available background-removal workflow only if it suits the asset. Any provider-specific workaround must be labeled as such, applied only to that provider's demonstrated limitation, and followed by an alpha/edge check. Chroma-key backgrounds are not a universal generation requirement; they can damage fine edges and matching foreground colors. If a reliable export cannot be produced, retain the usable source and clearly identify the missing deliverable.

## Develop and verify the system

- **Logo:** Favor a clear, distinctive silhouette. Check the intended smallest use, monochrome and reversed versions when relevant, optical balance, spacing, and consistency across requested lockups. Use actual renders when available and label unrendered source. Do not claim uniqueness or production readiness solely from a generated preview.
- **Color:** Define functional roles and usable combinations, not just swatches. Calculate contrast for specified text/background pairs where possible; scope any accessibility conclusion to the checks performed. Provide HEX/RGB for digital use. Print CMYK values depend on a color profile; label approximations and do not invent exact Pantone matches or print proofs.
- **Typography:** Select for voice, language coverage, legibility, and real applications. Specify hierarchy and fallbacks. Verify font licensing/source availability when possible; otherwise mark them unverified rather than claiming a font is free or redistributable.
- **Supporting elements:** Add patterns, icons, imagery direction, or layouts only when they help the requested identity. Check that they reinforce the same visual logic.

For an audit, separate observed defects, reasoned recommendations, and checks that could not be completed. Avoid pseudo-precise scores unless a rubric is requested; a score does not certify accessibility, originality, or performance.

## References on demand

Read only the relevant sections. These are design frameworks and illustrative examples, not researched facts about the user's brand or substitutes for current standards, measured checks, font licenses, or legal clearance.

- Logo construction, types, and evaluation: [logo-design-principles.md](references/logo-design-principles.md).
- Color relationships and palette development: [color-theory-principles.md](references/color-theory-principles.md).
- Type selection, pairing, and hierarchy: [typography-principles.md](references/typography-principles.md).
- Positioning and visual differentiation: [brand-strategy-principles.md](references/brand-strategy-principles.md).

## Deliver

Provide the requested assets or specifications with concise rationale and usage guidance. For file sets, include a small inventory identifying each actual file, format, purpose, dependencies, and verification status. Distinguish generated assets from proposed concepts and unavailable exports. Mention material limits without expanding a small assignment into an unsolicited brand book.
