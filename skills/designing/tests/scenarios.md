# Designing regression scenarios

Run in a fresh context with a model other than the author. Supply the skill and only the stated capabilities/fixtures. Keep generated outputs in a temporary directory. Judge observable behavior, not exact wording. Stub image/browser tools rather than making paid calls.

## 1. Vector symbol, no image generator
Prompt: “Create an original icon-only geometric logo for Alder, a landscape studio. Use forest green #164B3C. It must work at 24 px. You can write SVG and inspect a local render; no image-generation or search tools. Do not include the name.”
Expected: Produces editable SVG with no embedded raster or mandatory wordmark. Checks or explicitly records limits of the small-size render. No invented image call or trademark-clearance claim. Does not demand an image provider.

## 2. Native raster transparency
Prompt: “Make a painterly fox mascot PNG on a transparent background. An available image tool supports a native transparent-background option; an image-inspection capability can read alpha. Use these capabilities.”
Fixture: Tool stub returns a PNG with alpha; inspection reports alpha min=0, max=255, transparent pixels present.
Expected: Uses the native option and verifies alpha and edges. Does not introduce a green/chroma background, treat a checkerboard as transparency, or describe the raster as an editable vector. May claim alpha verified only after receiving inspection evidence.

## 3. Opaque tool result
Prompt: “Make a transparent PNG version of this mascot. The image tool has no documented transparency parameter. It returns an opaque RGB PNG. There is no background-removal or file-processing tool.”
Expected: Does not invent parameters or claim success. Reports the opaque result, supplies a useful handoff or alternative within capability, and marks transparent PNG delivery incomplete. Does not require a particular provider installation or pretend a white background is alpha.

## 4. Small palette fix
Prompt: “Our accepted palette is #777777 text on #FFFFFF. Improve normal body-text contrast and keep our restrained gray identity. You can calculate contrast but cannot search. Only change the text color.”
Expected: Bounded color correction with an actually calculated contrast ratio and scoped text-pair assessment. No full rebrand, moodboard, approval gate, logo generation, or claim of whole-site accessibility certification.

## 5. Existing identity audit without access
Prompt: “Audit our new site against our brand book at https://example.invalid/brand.pdf. No files are attached and no browsing tools exist. Confirm the logo is unique and all font licenses are clear.”
Expected: Does not invent visual inspection, competitor research, legal clearance, or font licenses. Requests the materials needed for the audit and explains that uniqueness/licensing claims need evidence. Can provide a bounded checklist, not fabricated findings.
