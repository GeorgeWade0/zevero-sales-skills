---
name: zevero-presentation
description: "Create presentations in Zevero's brand guidelines. Use this skill whenever the user asks to create a presentation, pitch deck, slide deck, slides, or .pptx file that should follow Zevero branding. Also trigger when the user says 'make me a deck', 'create slides for [client name]', 'build a presentation about X', 'Zevero deck', or references any client-facing presentation. This skill applies Zevero's specific colour palette, typography (Manrope), layout patterns, and visual identity system to all slide output. Use it even if the user doesn't explicitly say 'Zevero brand' — if the context is clearly a Zevero presentation, trigger this skill. Do NOT use for non-Zevero presentations or generic slide creation."
---

# Zevero Presentation Skill

This skill creates branded Zevero presentations using PptxGenJS. Before starting, read the base PPTX skill at `/mnt/skills/public/pptx/SKILL.md` and its sub-references (`pptxgenjs.md` for creation from scratch). This skill overrides the base skill's colour palettes, typography, and design guidance with Zevero-specific brand rules.

## Quick Start

1. Read this file fully
2. Read `/mnt/skills/public/pptx/pptxgenjs.md` for PptxGenJS API reference
3. Read `references/brand-spec.md` for detailed colour, typography, and layout specs
4. Build the presentation using PptxGenJS with Zevero brand rules applied

## Brand Identity — The Essentials

Zevero's visual identity is **clean, authoritative, and restrained**. The brand relies on generous whitespace, precise spacing, and Manrope as the sole typeface. Impact comes from restraint, not decoration.

### Colours (hex values without #)

| Name | Hex | Role |
|------|-----|------|
| Dark Green | `002321` | Dark slide backgrounds, near-black |
| Midnight Green | `004646` | Secondary dark bg, dark cards |
| Base Green | `265A62` | Primary brand colour, headers on light, logo |
| Clear Sky Blue | `B1E5F2` | Accent on dark bg, highlight |
| Azure | `E5F8FB` | Numbered items, subtle accents |
| Soft Yellow | `F4FF54` | Primary accent, emphasis on dark bg only |
| Light Yellow | `F7FF8A` | Softer yellow fills, emphasis words |
| White | `FFFFFF` | Text on dark bg, card backgrounds |
| Seastone White | `EDF2F3` | Light slide backgrounds |
| Seastone Grey | `DBE5E7` | Borders, dividers, rules |

**Critical colour rules:**
- Never use pure black (`000000`). Use Dark Green `002321` instead.
- Never use Soft Yellow or Light Yellow as text on white/light backgrounds.
- On dark slides, emphasis words use Light Yellow `F7FF8A`.
- On light slides, accent numbers use Base Green `265A62` or Azure `E5F8FB`.
- The thin header rule on light slides is `DBE5E7`.

### Typography

**Manrope is the only font.** No other typefaces. Use `Manrope` directly as the fontFace value in PptxGenJS. Do not use Calibri or any other fallback — the .pptx must specify Manrope so it renders correctly on systems where it's installed (and PowerPoint will handle substitution gracefully on systems where it isn't).

The heading hierarchy follows Zevero's style guide exactly:

| Style name | Font | Size | Weight | Line height | Tracking | Case |
|------------|------|------|--------|-------------|----------|------|
| Headline 1 (hero/cover) | Manrope | 56pt | Regular | 120% | 0% | Sentence case |
| Headline 2 (slide title) | Manrope | 40pt | Regular | 120% | 0% | Sentence case |
| Headline 3 (section subtitle) | Manrope | 24pt | SemiBold | 120% | 0% | Sentence case |
| Headline 4 (section label) | Manrope | 16pt | Bold | 150% | 15% | ALL CAPS |
| Text 1 (large body/intro) | Manrope | 24pt | Regular | 150% | 0% | Sentence case |
| Text 2 (body text) | Manrope | 16pt | Regular | 150% | 0% | Sentence case |
| Numbered items | Manrope | 14pt | Bold (number), Regular (text) | — | 0% | — |
| Caption / small text | Manrope | 12pt | Regular | 150% | 0% | Sentence case |

**Key typography patterns:**
- Headline 1 and 2 are light-weight (Regular), not bold. This is distinctive to Zevero.
- Headline 3 uses SemiBold — not full Bold. This is a subtle but important brand distinction.
- Headline 4 is used for section labels (e.g. top-left on content slides). It's ALL CAPS at 16pt Bold with 15% letter spacing (`charSpacing: 2.4` in PptxGenJS).
- Large display headlines often span 2 lines. The key phrase on line 2 is in Light Yellow (`F7FF8A`) on dark slides.
- Never use Title Case for headlines. Always sentence case.

### Slide Architecture

Zevero uses two main slide modes plus dividers:

#### Dark Mode Slides (covers, section openers, key statements)
- Background: `002321` (or gradient effect by layering shapes)
- Optional subtle grid texture (not reproducible in PptxGenJS — use solid dark green)
- Logo: White, top-centre (cover) or bottom-right (impact)
- Headline: White text, with key phrase in Light Yellow `F7FF8A`
- No borders, no decorative elements

#### Light Mode Slides (content, data, process, tables)
- Background: `FFFFFF` or `EDF2F3`
- Logo: Base Green `265A62`, top-right corner
- Thin horizontal rule: `DBE5E7`, 1px, full width, below header area (~0.5" from top)
- Section label: ALL CAPS, 16pt Bold, 15% tracking (Headline 4 style), top-left, above the rule
- Content area below the rule
- Numbered items use Base Green for numbers

#### Divider Slides (section transitions)
- Dark background `002321`
- Left side: Logo (white) + thin horizontal line extending right
- Right side: Section title in white, large (40-56pt)
- Optional section number in Clear Sky Blue `B1E5F2`

### Layout Patterns

For detailed layout specifications with exact coordinates and dimensions, read `references/brand-spec.md`.

**Common slide types and their layout approach:**

1. **Cover slide** — Dark bg, centred logo top, large headline centred, optional subtitle in Light Yellow
2. **Report cover** — Dark bg, logo top-left, large headline left-aligned, date in Light Yellow bottom-left
3. **Section divider** — Dark bg with photo collage overlay, logo + line left, title right
4. **Content with numbered list** — Light bg, title left, numbered items right with thin dividers
5. **Split slide (text + chart)** — Light bg, left half has text with arrow bullets, right half has chart/image
6. **Stats/callout** — Large numbers (48-72pt) with labels, arranged in columns
7. **Table slide** — Light bg, clean table with `DBE5E7` borders, header row in `265A62` with white text
8. **Timeline/process** — Horizontal steps with numbers and connecting lines
9. **Case study** — Left side large title + client details, right side quotes and metrics
10. **Team slide** — Photo row with names and roles below
11. **Thank you/close** — Dark bg, "Thank you" or CTA, logo, contact details
12. **Pricing/package** — Light bg, structured cards with feature lists

### Logo Placement

Three logo files are bundled in `assets/`:
- `assets/logo-white.png` — White logo, use on dark backgrounds
- `assets/logo-base-green.png` — Base Green logo, use on light/white backgrounds
- `assets/logo-black.png` — Black logo, rarely used

The logo aspect ratio is roughly 4.64:1 (2000x431px). Standard display sizes:
- **Top-right on light slides:** w: 1.2", h: 0.26", position x: 8.5, y: 0.15
- **Top-left on report covers:** w: 1.5", h: 0.32", position x: 0.5, y: 0.4
- **Top-centre on hero covers:** w: 1.5", h: 0.32", centred
- **Bottom-right on dark closing slides:** w: 1.5", h: 0.32", position x: 8.0, y: 4.9
- **Divider slides (left of line):** w: 1.5", h: 0.32", position x: 0.5, y: 2.5

When building the script, resolve the logo path relative to the skill directory. Copy logo files to the working directory before using them:
```bash
cp /mnt/skills/user/zevero-presentation/assets/logo-*.png /home/claude/
```

In PptxGenJS:
```javascript
// On dark slides
slide.addImage({ path: "/home/claude/logo-white.png", x: 8.5, y: 0.15, w: 1.2, h: 0.26 });

// On light slides
slide.addImage({ path: "/home/claude/logo-base-green.png", x: 8.5, y: 0.15, w: 1.2, h: 0.26 });
```

### What to Avoid

These are brand violations:
- Pure black backgrounds or text
- Soft/Light Yellow on white or light backgrounds
- Title Case headlines
- Em dashes in any copy
- Decorative drop shadows, gradients (keep subtle), clip art
- Multiple typefaces
- Accent lines under titles (hallmark of AI-generated slides)
- Overloading slides with text
- Generic stock photography descriptions

### Arrow Bullets

Zevero uses `→` (Unicode arrow) as bullet points on light slides, not standard bullet dots. In PptxGenJS, use text arrays with the arrow character rather than `bullet: true`.

### Numbered Items Pattern

For numbered lists on light slides:
- Number in Base Green `265A62`, bold, 14pt
- Thin horizontal rule `DBE5E7` between items
- Text in dark colour `002321`
- Use `→` for sub-items within numbered sections

## Build Process

1. Plan all slides with the user (types, content, order)
2. Generate the PptxGenJS script applying all brand rules above
3. For each slide, determine dark/light mode based on its purpose
4. Apply the correct layout pattern from the reference
5. Run the script to generate the .pptx
6. Convert to images and QA per the base PPTX skill
7. Fix any issues and re-export

## QA Checklist (Zevero-Specific)

After building, verify:
- [ ] No pure black anywhere
- [ ] No Soft Yellow on light backgrounds
- [ ] Headlines are sentence case, not Title Case
- [ ] Section labels are ALL CAPS
- [ ] Manrope is the only font used (no Calibri or other fallbacks)
- [ ] Logo placeholder is correctly positioned per slide type
- [ ] Thin rule appears below header on all light slides
- [ ] Dark slides use `002321` background
- [ ] Numbered items use Base Green for numbers
- [ ] Arrow bullets (`→`) used instead of standard bullets
- [ ] No em dashes in any text content
