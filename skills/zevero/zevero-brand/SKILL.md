---
name: zevero-brand
description: Apply Zevero's visual brand guidelines to any design output. Use this skill whenever someone asks for anything visual for Zevero — including React components, HTML artifacts, presentations (PPTX), web designs, documents, graphics, dashboards, reports, or slides. Trigger on any request involving Zevero design, Zevero visuals, Zevero slides, Zevero website, or any UI work done in a Zevero context. Always load this skill before producing any Zevero-branded output, even if the request seems simple.
---

# Zevero Brand Guidelines

Apply these guidelines to every Zevero design output. This skill covers colour, typography, spacing, components, and slide patterns.

---

## Colour Palette

### Brand Colours (primary)

| Name | Hex | Usage |
|---|---|---|
| Base Green | `#004646` | Primary brand colour. Headers, key UI elements, logo colour on light bg |
| Midnight Green | `#002321` | Darkest background. Slide dark mode bg, hero sections |
| Dark Green | `#0A1414` | Near-black. Dark overlays, deep backgrounds |
| Clear Sky Blue | `#c6ebf0` | Accent on dark backgrounds, highlight colour |
| Azure | `#265a62` | Numbered items, subtle teal accents, secondary UI |
| Soft Yellow | `#f7ff8a` | Primary accent for emphasis. Use on dark backgrounds to highlight key words |
| White | `#FFFFFF` | Primary text on dark bg, card backgrounds |
| Seastone White | `#edf2f3` | Light slide backgrounds, subtle section fills |
| Light Sky Blue | `#e5f8fb` | Soft background panels, cards |
| Light Yellow | `#fbffc3` | Soft yellow fills |
| Pale Yellow | `#f5ffc8` | Very subtle yellow tint |
| Seastone Grey | `#dbe5e7` | Borders, dividers, muted backgrounds |

### Digital Colours (screen/web)

| Name | Hex | Usage |
|---|---|---|
| Digital Teal | `#265a62` | Interactive elements, links |
| Digital Sky Blue | `#b1e5f2` | Hover states, highlights |
| Digital Yellow | `#f4ff54` | CTA buttons, badges, interactive yellow |

### Colour Rules

- **Dark mode**: Midnight Green `#002321` background, White text, Soft Yellow `#f7ff8a` for emphasis words
- **Light mode**: White or Seastone White background, Base Green `#004646` or Dark text, Azure `#265a62` for numbered items
- Never use Soft Yellow as body text on a white background
- Soft Yellow is for key word highlights in display text only — one or two words per headline maximum
- Base Green is the primary teal for logos, icons, and interactive elements on light backgrounds
- Avoid pure black — use Midnight Green or Dark Green instead

---

## Typography

All type uses **Manrope** exclusively. Load via Google Fonts: `https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700&display=swap`

| Style | Weight | Size | Line Height | Letter Spacing | Case |
|---|---|---|---|---|---|
| Headline 1 | Regular (400) | 56pt / ~75px | 120% | 0 | Sentence |
| Headline 2 | Regular (400) | 40pt / ~53px | 120% | 0 | Sentence |
| Headline 3 | SemiBold (600) | 24pt / ~32px | 120% | 0 | Sentence |
| Headline 4 | Bold (700) | 16pt / ~21px | 150% | 15% | ALL CAPS |
| Text 1 | Regular (400) | 24pt / ~32px | 150% | 0 | Sentence |
| Text 2 | Regular (400) | 16pt / ~21px | 150% | 0 | Sentence |
| Button | Regular (400) | 16pt | 150% | 0 | Sentence |

**Typography patterns observed in slides:**
- Large display headlines often span 2 lines with the key phrase on the second line in Soft Yellow
- Example: Line 1 white "Intro to Sustainability" / Line 2 yellow "The Brewing Industry"
- Section labels use Headline 4 style (all-caps, small, spaced)
- Numbered items use Azure for the number, dark text for the label

---

## Spacing

8px base grid. Standard levels: `8 / 16 / 24 / 32 / 40 / 64 / 72 / 144px`

Use:
- `8px` — tight inner padding
- `16px` — component padding
- `24px` — section gaps
- `32–40px` — generous padding inside cards
- `64–72px` — slide margins / section padding
- `144px` — major layout spacing

---

## Components

### Buttons

```css
/* Primary CTA (yellow) */
background: #f4ff54;
color: #002321;
font-family: Manrope;
font-size: 16px;
font-weight: 400;
padding: 8px 12px;
border-radius: 8px;
border: none;

/* Secondary (teal outline) */
background: transparent;
color: #004646;
border: 1.5px solid #004646;
padding: 8px 12px;
border-radius: 8px;
```

### Logo Treatment

- On dark backgrounds: logo in white, optionally inside a pill/badge with a subtle teal border (`border: 1.5px solid #265a62; border-radius: 24px; padding: 8px 16px`)
- On light backgrounds: logo in Base Green `#004646`

### Cards (light mode)

```css
background: #FFFFFF;
border-radius: 12px;
border: 1px solid #dbe5e7;
padding: 32px;
```

### Cards (dark mode)

```css
background: #004646;
border-radius: 12px;
padding: 32px;
color: white;
```

### Numbered/Indexed Items

- Number in Azure `#265a62`, bold
- Horizontal rule `1px solid #dbe5e7` as divider between items
- Arrow `→` used as sub-item bullet on light slides

### Time/Label Badges (Soft Yellow)

```css
background: #f7ff8a;
color: #002321;
border-radius: 20px;
padding: 6px 16px;
font-size: 14px;
font-weight: 600;
```

---

## Slide Design Patterns

There are two main slide families. Choose based on context:

### Dark Mode Slides (impact / title / section)

Use for: cover slides, section openers, key statements, full-bleed impact moments.

- Background: Midnight Green `#002321` or gradient from `#002321` to Base Green `#004646`
- Optional subtle grid texture overlay (CSS grid pattern, very low opacity ~3-5%)
- Logo: white, top-center or top-left
- Main headline: White (line 1) + Soft Yellow `#f7ff8a` (key word, line 2)
- No explicit slide borders
- Optional: photo underneath with dark overlay (`rgba(0,35,33,0.75)`)
- Zevero logo bottom-right when logo is not at top

### Light Mode Slides (content / data / detail)

Use for: content slides, tables of contents, data, process flows, multi-column.

- Background: White `#FFFFFF` or Seastone White `#edf2f3`
- Logo: Base Green, top-right
- Thin horizontal rule `1px solid #dbe5e7` below the header area
- Section label: Headline 4 style (all-caps, small, spaced) in dark grey top-left
- Slide title: Headline 2–3 in very dark text (`#0A1414` or `#002321`)
- Numbered items: Azure numbers, dark body text
- Image panels: right-aligned, full-height column, rounded corners on image (`border-radius: 8px`)

### Divider / Section Label Slides

Use for: separating sections within a presentation.

- Dark photo collage background (grid of nature/sustainability images with dark overlay)
- Layout: logo + thin line (left side, ~40% width) + section title (right side, ~55% width)
- Section title in White, Headline 1 size
- Optional section number (large, muted, Light Sky Blue `#c6ebf0`) left of the rule

---

## Visual Personality

- **Clean and authoritative** — never cluttered; let whitespace breathe
- **Nature-rooted** — photography favours nature, agriculture, aerial shots, greenery
- **Precision** — thin rules, structured grids, exact spacing; Zevero is a data company
- **Impact through restraint** — Soft Yellow and Clear Sky Blue are accents only; overuse weakens them
- **No decorative flourishes** — no drop shadows, gradients kept subtle, no heavy patterns
- Typography does the heavy lifting; Manrope is the visual personality

---

## Quick Reference for Common Outputs

### React / HTML Artifact
- Import Manrope from Google Fonts
- Use CSS custom properties for the colour tokens
- Default to dark mode for impact pieces, light mode for data/content
- Use Tailwind sparingly — prefer inline styles or CSS vars for exact brand colours

### Presentations (PPTX)
- Dark slides: `#002321` background, white + yellow headlines
- Light slides: white bg, `#004646` logo, `#265a62` numbered items
- Always include logo (top-right on light; centre-top pill on dark)
- Read `/mnt/skills/public/pptx/SKILL.md` before producing PPTX files

### Documents (DOCX)
- Light mode defaults
- Headers in Base Green `#004646` with Manrope
- Read `/mnt/skills/public/docx/SKILL.md` before producing DOCX files

### Web Components / Artifacts
- Read `/mnt/skills/public/frontend-design/SKILL.md` for elevated design quality
- Apply brand tokens; do not substitute with generic Tailwind blues or greys
