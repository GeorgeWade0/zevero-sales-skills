# Zevero Brand Specification — Detailed Reference

This file contains exact dimensions, coordinates, and code patterns for building Zevero-branded slides in PptxGenJS. All measurements are in inches for a 16:9 layout (10" x 5.625").

## Table of Contents

1. [Colour Constants](#colour-constants)
2. [Slide Masters](#slide-masters)
3. [Cover Slides](#cover-slides)
4. [Section Divider Slides](#section-divider-slides)
5. [Light Content Slides](#light-content-slides)
6. [Split Layout Slides](#split-layout-slides)
7. [Stats and Callout Slides](#stats-and-callout-slides)
8. [Table Slides](#table-slides)
9. [Timeline Slides](#timeline-slides)
10. [Case Study Slides](#case-study-slides)
11. [Team Slides](#team-slides)
12. [End/Thank You Slides](#end-slides)
13. [Reusable Code Patterns](#reusable-code-patterns)

---

## Colour Constants

Define these at the top of every script:

```javascript
const COLORS = {
  darkGreen:    "002321",   // Primary dark background
  midnightGreen:"004646",   // Secondary dark bg, dark cards
  baseGreen:    "265A62",   // Primary brand, headers on light
  clearSkyBlue: "B1E5F2",   // Accent on dark bg
  azure:        "E5F8FB",   // Numbered items, subtle accents
  softYellow:   "F4FF54",   // Primary accent (dark bg only)
  lightYellow:  "F7FF8A",   // Emphasis words on dark bg
  white:        "FFFFFF",   // Text on dark bg, card bg
  seastoneWhite:"EDF2F3",   // Light slide bg
  seastoneGrey: "DBE5E7",   // Borders, dividers, rules
  lightSkyBlue: "C6EBF0",   // Soft background panels
  paleYellow:   "FBFFC3",   // Very subtle yellow tint
};

const FONT = "Manrope";  // Zevero's sole typeface
```

---

## Logo Files

Copy logos to working directory before running any script:
```bash
cp /mnt/skills/user/zevero-presentation/assets/logo-*.png /home/claude/
```

Logo paths for PptxGenJS:
```javascript
const LOGO_WHITE = "/home/claude/logo-white.png";       // dark backgrounds
const LOGO_GREEN = "/home/claude/logo-base-green.png";   // light backgrounds
const LOGO_BLACK = "/home/claude/logo-black.png";        // rarely used
const LOGO_W = 1.2;  // display width in inches
const LOGO_H = 0.26; // display height in inches
```

---

## Slide Masters

Define these for consistency:

```javascript
// Dark slide master
pres.defineSlideMaster({
  title: "DARK_SLIDE",
  background: { color: COLORS.darkGreen },
  objects: []
});

// Light slide master with header rule and logo
pres.defineSlideMaster({
  title: "LIGHT_SLIDE",
  background: { color: COLORS.white },
  objects: [
    // Thin header rule
    { shape: pres.shapes.LINE, options: {
      x: 0, y: 0.55, w: 10, h: 0,
      line: { color: COLORS.seastoneGrey, width: 0.75 }
    }},
    // Logo (top-right)
    { image: { path: LOGO_GREEN, x: 8.5, y: 0.15, w: LOGO_W, h: LOGO_H } }
  ]
});

// Seastone white slide
pres.defineSlideMaster({
  title: "SEASTONE_SLIDE",
  background: { color: COLORS.seastoneWhite },
  objects: [
    { shape: pres.shapes.LINE, options: {
      x: 0, y: 0.55, w: 10, h: 0,
      line: { color: COLORS.seastoneGrey, width: 0.75 }
    }},
    { image: { path: LOGO_GREEN, x: 8.5, y: 0.15, w: LOGO_W, h: LOGO_H } }
  ]
});
```

---

## Cover Slides

### Type A: Centred hero cover (presentation title)

```
Layout:
- Background: darkGreen
- Logo "zevero" centred, top area (y: 0.6)
- Large headline centred (56pt, Regular weight)
  - Line 1: white
  - Line 2: lightYellow (emphasis phrase)
```

```javascript
function addCoverSlide(pres, { title, subtitle, emphasisLine }) {
  let slide = pres.addSlide({ masterName: "DARK_SLIDE" });

  // Logo (centred)
  slide.addImage({ path: LOGO_WHITE, x: 4.25, y: 0.5, w: 1.5, h: 0.32 });

  // Main title
  let titleParts = [
    { text: title, options: { fontSize: 56, fontFace: FONT, color: COLORS.white, breakLine: true } }
  ];
  if (emphasisLine) {
    titleParts.push({
      text: emphasisLine,
      options: { fontSize: 56, fontFace: FONT, color: COLORS.lightYellow }
    });
  }
  slide.addText(titleParts, {
    x: 0.5, y: 1.5, w: 9, h: 3,
    align: "center", valign: "middle", margin: 0
  });

  // Subtitle if provided
  if (subtitle) {
    slide.addText(subtitle, {
      x: 1, y: 4.5, w: 8, h: 0.5,
      fontFace: FONT, fontSize: 16, color: COLORS.lightYellow,
      align: "center", margin: 0
    });
  }
  return slide;
}
```

### Type B: Report cover (left-aligned with date)

```
Layout:
- Background: darkGreen
- Logo "zevero" top-left (x: 0.5, y: 0.4)
- Large headline left-aligned (56pt)
- Date in lightYellow, bottom-left
```

```javascript
function addReportCover(pres, { title, date }) {
  let slide = pres.addSlide({ masterName: "DARK_SLIDE" });

  slide.addImage({ path: LOGO_WHITE, x: 0.5, y: 0.4, w: 1.5, h: 0.32 });

  slide.addText(title, {
    x: 0.5, y: 1.5, w: 8, h: 2.5,
    fontFace: FONT, fontSize: 56, color: COLORS.white,
    align: "left", valign: "top", margin: 0
  });

  if (date) {
    slide.addText(date, {
      x: 0.5, y: 4.6, w: 4, h: 0.4,
      fontFace: FONT, fontSize: 16, color: COLORS.lightYellow,
      align: "left", margin: 0
    });
  }
  return slide;
}
```

---

## Section Divider Slides

```
Layout:
- Background: darkGreen
- Left area: Logo "zevero" + thin white horizontal line
- Right area: Section title (40-56pt white)
- Optional: section number in clearSkyBlue, left of line
```

```javascript
function addDividerSlide(pres, { title, sectionNumber }) {
  let slide = pres.addSlide({ masterName: "DARK_SLIDE" });

  // Logo
  slide.addImage({ path: LOGO_WHITE, x: 0.5, y: 2.5, w: 1.5, h: 0.32 });

  // Thin white line from logo to centre
  slide.addShape(pres.shapes.LINE, {
    x: 2.1, y: 2.7, w: 3, h: 0,
    line: { color: COLORS.white, width: 0.5 }
  });

  // Section number (optional)
  if (sectionNumber) {
    slide.addText(String(sectionNumber).padStart(2, "0"), {
      x: 0.5, y: 2.0, w: 1.5, h: 0.5,
      fontFace: FONT, fontSize: 24, color: COLORS.clearSkyBlue,
      align: "left", margin: 0
    });
  }

  // Section title
  slide.addText(title, {
    x: 5.3, y: 1.8, w: 4.2, h: 2,
    fontFace: FONT, fontSize: 44, color: COLORS.white,
    align: "left", valign: "middle", margin: 0
  });

  return slide;
}
```

---

## Light Content Slides

### Standard content layout (title left, content right)

```
Layout:
- Master: LIGHT_SLIDE (has rule + logo)
- Section label: ALL CAPS, 16pt Bold, 15% tracking, top-left above rule
- Title: left column (x: 0.5, y: 0.8, w: 4)
- Content: right column with numbered items or text blocks
```

```javascript
function addContentSlide(pres, { sectionLabel, title, subtitle, items }) {
  let slide = pres.addSlide({ masterName: "LIGHT_SLIDE" });

  // Section label (ALL CAPS)
  if (sectionLabel) {
    slide.addText(sectionLabel.toUpperCase(), {
      x: 0.5, y: 0.15, w: 4, h: 0.3,
      fontFace: FONT, fontSize: 16, bold: true,
      color: COLORS.seastoneGrey, align: "left",
      charSpacing: 2.4, margin: 0
    });
  }

  // Title
  slide.addText(title, {
    x: 0.5, y: 0.8, w: 4, h: 1.5,
    fontFace: FONT, fontSize: 40, color: COLORS.darkGreen,
    align: "left", valign: "top", margin: 0
  });

  // Subtitle
  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.5, y: 2.3, w: 4, h: 0.8,
      fontFace: FONT, fontSize: 14, color: COLORS.baseGreen,
      align: "left", margin: 0
    });
  }

  // Numbered items on the right
  if (items && items.length > 0) {
    // Vertical divider
    slide.addShape(pres.shapes.LINE, {
      x: 4.8, y: 0.8, w: 0, h: 4.2,
      line: { color: COLORS.seastoneGrey, width: 0.5 }
    });

    const startY = 0.8;
    const itemHeight = 4.2 / items.length;

    items.forEach((item, i) => {
      const y = startY + (i * itemHeight);

      // Number
      slide.addText(String(i + 1).padStart(2, "0"), {
        x: 5.0, y: y, w: 0.5, h: 0.3,
        fontFace: FONT, fontSize: 14, bold: true,
        color: COLORS.baseGreen, margin: 0
      });

      // Item text
      slide.addText(item.title || item, {
        x: 5.6, y: y, w: 3.9, h: 0.3,
        fontFace: FONT, fontSize: 14, bold: true,
        color: COLORS.darkGreen, margin: 0
      });

      // Item description
      if (item.description) {
        slide.addText(item.description, {
          x: 5.6, y: y + 0.3, w: 3.9, h: 0.4,
          fontFace: FONT, fontSize: 12, color: COLORS.baseGreen,
          margin: 0
        });
      }

      // Horizontal rule between items
      if (i < items.length - 1) {
        slide.addShape(pres.shapes.LINE, {
          x: 5.0, y: y + itemHeight - 0.05, w: 4.5, h: 0,
          line: { color: COLORS.seastoneGrey, width: 0.5 }
        });
      }
    });
  }

  return slide;
}
```

### Arrow bullet content

For content slides with arrow (`→`) bullets:

```javascript
function makeArrowBullets(items) {
  let parts = [];
  items.forEach((item, i) => {
    parts.push({ text: "→   ", options: {
      fontFace: FONT, fontSize: 14, color: COLORS.baseGreen,
      breakLine: false
    }});
    parts.push({ text: item, options: {
      fontFace: FONT, fontSize: 14, color: COLORS.darkGreen,
      breakLine: true, paraSpaceAfter: 8
    }});
  });
  return parts;
}
```

---

## Split Layout Slides

### Text left, visual right (50/50 split)

The right half is often a chart, image, or platform screenshot.

```javascript
function addSplitSlide(pres, { sectionLabel, title, bullets, rightContent }) {
  let slide = pres.addSlide({ masterName: "LIGHT_SLIDE" });

  if (sectionLabel) {
    slide.addText(sectionLabel.toUpperCase(), {
      x: 0.5, y: 0.15, w: 4, h: 0.3,
      fontFace: FONT, fontSize: 16, bold: true,
      color: COLORS.seastoneGrey, charSpacing: 2.4, margin: 0
    });
  }

  // Left half background (light blue tint)
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0.55, w: 5, h: 5.075,
    fill: { color: COLORS.azure }
  });

  // Title
  slide.addText(title, {
    x: 0.5, y: 0.8, w: 4, h: 1,
    fontFace: FONT, fontSize: 32, color: COLORS.darkGreen,
    margin: 0
  });

  // Arrow bullets
  if (bullets) {
    slide.addText(makeArrowBullets(bullets), {
      x: 0.5, y: 2.0, w: 4, h: 3,
      valign: "top", margin: 0
    });
  }

  // Right side: placeholder for chart/image
  // The caller should add their own content here at x: 5.2, y: 0.8, w: 4.3, h: 4.2

  return slide;
}
```

---

## Stats and Callout Slides

Large numbers with labels, used for KPIs and impact data.

```javascript
function addStatsSlide(pres, { title, stats }) {
  // stats = [{ value: "100k+", label: "Emission factors" }, ...]
  let slide = pres.addSlide({ masterName: "LIGHT_SLIDE" });

  slide.addText(title, {
    x: 0.5, y: 0.8, w: 9, h: 0.8,
    fontFace: FONT, fontSize: 32, color: COLORS.darkGreen,
    align: "center", margin: 0
  });

  const colW = 8 / stats.length;
  const startX = 1;
  stats.forEach((stat, i) => {
    const x = startX + (i * colW);

    slide.addText(stat.value, {
      x: x, y: 2.0, w: colW - 0.3, h: 1,
      fontFace: FONT, fontSize: 48, bold: true,
      color: COLORS.baseGreen, align: "center", margin: 0
    });

    slide.addText(stat.label, {
      x: x, y: 3.0, w: colW - 0.3, h: 1,
      fontFace: FONT, fontSize: 14, color: COLORS.darkGreen,
      align: "center", margin: 0
    });
  });

  return slide;
}
```

---

## Table Slides

```javascript
function addTableSlide(pres, { sectionLabel, title, headers, rows }) {
  let slide = pres.addSlide({ masterName: "LIGHT_SLIDE" });

  if (sectionLabel) {
    slide.addText(sectionLabel.toUpperCase(), {
      x: 0.5, y: 0.15, w: 4, h: 0.3,
      fontFace: FONT, fontSize: 16, bold: true,
      color: COLORS.seastoneGrey, charSpacing: 2.4, margin: 0
    });
  }

  if (title) {
    slide.addText(title, {
      x: 0.5, y: 0.7, w: 9, h: 0.6,
      fontFace: FONT, fontSize: 24, bold: true,
      color: COLORS.darkGreen, margin: 0
    });
  }

  // Build table data
  let headerRow = headers.map(h => ({
    text: h,
    options: {
      fontFace: FONT, fontSize: 12, bold: true,
      color: COLORS.white, fill: { color: COLORS.baseGreen },
      align: "left", valign: "middle"
    }
  }));

  let dataRows = rows.map(row =>
    row.map(cell => ({
      text: String(cell),
      options: {
        fontFace: FONT, fontSize: 11,
        color: COLORS.darkGreen, fill: { color: COLORS.white },
        align: "left", valign: "middle",
        border: [
          { pt: 0, color: COLORS.white },           // top
          { pt: 0, color: COLORS.white },           // right
          { pt: 0.5, color: COLORS.seastoneGrey },  // bottom
          { pt: 0, color: COLORS.white }             // left
        ]
      }
    }))
  );

  slide.addTable([headerRow, ...dataRows], {
    x: 0.5, y: 1.4, w: 9, h: 3.5,
    border: { pt: 0.5, color: COLORS.seastoneGrey },
    rowH: [0.35],
    autoPage: false
  });

  return slide;
}
```

---

## Timeline Slides

Horizontal process flow with numbered steps.

```javascript
function addTimelineSlide(pres, { sectionLabel, title, subtitle, steps }) {
  let slide = pres.addSlide({ masterName: "LIGHT_SLIDE" });

  if (sectionLabel) {
    slide.addText(sectionLabel.toUpperCase(), {
      x: 0.5, y: 0.15, w: 4, h: 0.3,
      fontFace: FONT, fontSize: 16, bold: true,
      color: COLORS.seastoneGrey, charSpacing: 2.4, margin: 0
    });
  }

  slide.addText(title, {
    x: 0.5, y: 0.7, w: 9, h: 0.6,
    fontFace: FONT, fontSize: 24, bold: true,
    color: COLORS.darkGreen, margin: 0
  });

  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.5, y: 1.3, w: 9, h: 0.5,
      fontFace: FONT, fontSize: 14, color: COLORS.baseGreen, margin: 0
    });
  }

  // Connecting line
  const lineY = 2.6;
  slide.addShape(pres.shapes.LINE, {
    x: 0.8, y: lineY, w: 8.4, h: 0,
    line: { color: COLORS.seastoneGrey, width: 1.5 }
  });

  const stepW = 8.4 / steps.length;
  steps.forEach((step, i) => {
    const cx = 0.8 + (i * stepW) + (stepW / 2);

    // Step number circle
    slide.addShape(pres.shapes.OVAL, {
      x: cx - 0.2, y: lineY - 0.2, w: 0.4, h: 0.4,
      fill: { color: COLORS.baseGreen }
    });
    slide.addText(String(i + 1), {
      x: cx - 0.2, y: lineY - 0.2, w: 0.4, h: 0.4,
      fontFace: FONT, fontSize: 12, bold: true,
      color: COLORS.white, align: "center", valign: "middle", margin: 0
    });

    // Step title
    slide.addText(step.title, {
      x: cx - (stepW / 2) + 0.1, y: lineY + 0.4, w: stepW - 0.2, h: 0.4,
      fontFace: FONT, fontSize: 12, bold: true,
      color: COLORS.darkGreen, align: "center", margin: 0
    });

    // Step description
    if (step.description) {
      slide.addText(step.description, {
        x: cx - (stepW / 2) + 0.1, y: lineY + 0.8, w: stepW - 0.2, h: 1,
        fontFace: FONT, fontSize: 10, color: COLORS.baseGreen,
        align: "center", margin: 0
      });
    }
  });

  return slide;
}
```

---

## Case Study Slides

```javascript
function addCaseStudySlide(pres, { sectionLabel, title, subtitle, quote, quoteName, quoteRole, metrics }) {
  let slide = pres.addSlide({ masterName: "LIGHT_SLIDE" });

  slide.addText("CASE STUDY", {
    x: 0.5, y: 0.15, w: 4, h: 0.3,
    fontFace: FONT, fontSize: 16, bold: true,
    color: COLORS.seastoneGrey, charSpacing: 2.4, margin: 0
  });

  // Left column: title and metrics
  slide.addText(title, {
    x: 0.5, y: 0.8, w: 4, h: 1.5,
    fontFace: FONT, fontSize: 32, color: COLORS.darkGreen, margin: 0
  });

  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.5, y: 2.3, w: 4, h: 1,
      fontFace: FONT, fontSize: 14, color: COLORS.baseGreen, margin: 0
    });
  }

  // Metrics as numbered items
  if (metrics) {
    metrics.forEach((m, i) => {
      slide.addText(String(i + 1).padStart(2, "0"), {
        x: 0.5, y: 3.4 + (i * 0.45), w: 0.4, h: 0.35,
        fontFace: FONT, fontSize: 12, bold: true,
        color: COLORS.baseGreen, margin: 0
      });
      slide.addText(m, {
        x: 1.0, y: 3.4 + (i * 0.45), w: 3.5, h: 0.35,
        fontFace: FONT, fontSize: 12, color: COLORS.darkGreen, margin: 0
      });
    });
  }

  // Right column: quote
  if (quote) {
    // Quote background
    slide.addShape(pres.shapes.RECTANGLE, {
      x: 5.2, y: 0.8, w: 4.3, h: 4.2,
      fill: { color: COLORS.seastoneWhite }
    });

    slide.addText(`"${quote}"`, {
      x: 5.5, y: 1.2, w: 3.7, h: 2.5,
      fontFace: FONT, fontSize: 16, italic: true,
      color: COLORS.darkGreen, margin: 0
    });

    if (quoteName) {
      slide.addText(quoteName, {
        x: 5.5, y: 4.0, w: 3.7, h: 0.3,
        fontFace: FONT, fontSize: 12, bold: true,
        color: COLORS.darkGreen, margin: 0
      });
    }
    if (quoteRole) {
      slide.addText(quoteRole, {
        x: 5.5, y: 4.3, w: 3.7, h: 0.3,
        fontFace: FONT, fontSize: 11, color: COLORS.baseGreen, margin: 0
      });
    }
  }

  return slide;
}
```

---

## Team Slides

Photos with names in a horizontal row. Since we cannot embed actual photos programmatically without files, create placeholder boxes.

```javascript
function addTeamSlide(pres, { title, members }) {
  let slide = pres.addSlide({ masterName: "LIGHT_SLIDE" });

  slide.addText("OUR TEAM", {
    x: 0.5, y: 0.15, w: 4, h: 0.3,
    fontFace: FONT, fontSize: 16, bold: true,
    color: COLORS.seastoneGrey, charSpacing: 2.4, margin: 0
  });

  slide.addText(title, {
    x: 0.5, y: 0.7, w: 9, h: 0.6,
    fontFace: FONT, fontSize: 20, color: COLORS.darkGreen,
    align: "center", margin: 0
  });

  const colW = 8 / members.length;
  members.forEach((m, i) => {
    const x = 1 + (i * colW);

    // Photo placeholder
    slide.addShape(pres.shapes.RECTANGLE, {
      x: x, y: 1.5, w: colW - 0.3, h: 1.8,
      fill: { color: COLORS.lightSkyBlue }
    });
    slide.addText("[Photo]", {
      x: x, y: 1.5, w: colW - 0.3, h: 1.8,
      fontFace: FONT, fontSize: 12, color: COLORS.baseGreen,
      align: "center", valign: "middle", margin: 0
    });

    // Name
    slide.addText(m.name, {
      x: x, y: 3.5, w: colW - 0.3, h: 0.35,
      fontFace: FONT, fontSize: 14, bold: true,
      color: COLORS.darkGreen, margin: 0
    });

    // Role
    slide.addText(m.role, {
      x: x, y: 3.85, w: colW - 0.3, h: 0.35,
      fontFace: FONT, fontSize: 12, color: COLORS.baseGreen, margin: 0
    });

    // Bio
    if (m.bio) {
      slide.addText(m.bio, {
        x: x, y: 4.2, w: colW - 0.3, h: 0.8,
        fontFace: FONT, fontSize: 10, color: COLORS.baseGreen, margin: 0
      });
    }
  });

  return slide;
}
```

---

## End Slides

### Thank you slide

```javascript
function addThankYouSlide(pres, { message, website, contactName, contactRole, contactEmail }) {
  let slide = pres.addSlide({ masterName: "DARK_SLIDE" });

  slide.addText(message || "Thank you", {
    x: 0.5, y: 1.5, w: 9, h: 1.5,
    fontFace: FONT, fontSize: 56, color: COLORS.white,
    align: "center", margin: 0
  });

  if (website) {
    slide.addText(website, {
      x: 3, y: 3.2, w: 4, h: 0.4,
      fontFace: FONT, fontSize: 16, color: COLORS.lightYellow,
      align: "center", margin: 0
    });
  }

  // Logo bottom-right
  slide.addImage({ path: LOGO_WHITE, x: 8.0, y: 4.9, w: 1.5, h: 0.32 });

  return slide;
}
```

### CTA closing slide (personalised)

```javascript
function addCTASlide(pres, { companyName, contactName, contactRole, contactEmail }) {
  let slide = pres.addSlide({ masterName: "DARK_SLIDE" });

  let titleParts = [
    { text: "Let's see how\nZevero can help\n", options: {
      fontFace: FONT, fontSize: 40, color: COLORS.white, breakLine: true
    }},
    { text: companyName + "\n", options: {
      fontFace: FONT, fontSize: 40, color: COLORS.white, breakLine: true
    }},
    { text: "decarbonise", options: {
      fontFace: FONT, fontSize: 40, color: COLORS.lightYellow
    }}
  ];

  slide.addText(titleParts, {
    x: 0.5, y: 0.8, w: 5, h: 3,
    valign: "top", margin: 0
  });

  // Website
  slide.addText("zevero.earth", {
    x: 0.5, y: 4.0, w: 4, h: 0.3,
    fontFace: FONT, fontSize: 14, color: COLORS.lightYellow, margin: 0
  });

  // Contact details (right side)
  if (contactName) {
    slide.addText([
      { text: contactName, options: { fontFace: FONT, fontSize: 14, bold: true, color: COLORS.white, breakLine: true }},
      { text: contactRole || "", options: { fontFace: FONT, fontSize: 12, color: COLORS.clearSkyBlue, breakLine: true }},
      { text: contactEmail || "", options: { fontFace: FONT, fontSize: 12, color: COLORS.clearSkyBlue }}
    ], {
      x: 6.5, y: 4.0, w: 3, h: 1,
      margin: 0
    });
  }

  // Logo
  slide.addImage({ path: LOGO_WHITE, x: 8.0, y: 4.9, w: 1.5, h: 0.32 });

  return slide;
}
```

---

## Reusable Code Patterns

### Full script skeleton

Every Zevero presentation script should follow this structure:

```javascript
const pptxgen = require("pptxgenjs");

// ── Colour constants ──
const COLORS = { /* ... as above ... */ };
const FONT = "Manrope";

// ── Logo paths (copy from skill assets first) ──
const LOGO_WHITE = "/home/claude/logo-white.png";
const LOGO_GREEN = "/home/claude/logo-base-green.png";
const LOGO_W = 1.2;
const LOGO_H = 0.26;

// ── Create presentation ──
let pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "Zevero";
pres.title = "PRESENTATION TITLE";

// ── Define slide masters ──
// ... (as above)

// ── Helper functions ──
// ... (as needed from patterns above)

// ── Build slides ──
// 1. Cover
// 2. Contents / agenda
// 3. Section dividers + content
// 4. Data / charts
// 5. Case studies
// 6. Team
// 7. Close / CTA

// ── Export ──
pres.writeFile({ fileName: "/home/claude/output.pptx" })
  .then(() => console.log("Done"))
  .catch(err => console.error(err));
```

### Chart styling for Zevero

When adding charts, apply these brand colours:

```javascript
const chartOptions = {
  chartColors: [COLORS.baseGreen, COLORS.midnightGreen, COLORS.clearSkyBlue, COLORS.lightYellow],
  chartArea: { fill: { color: COLORS.white }, roundedCorners: true },
  catAxisLabelColor: COLORS.baseGreen,
  valAxisLabelColor: COLORS.baseGreen,
  catAxisLabelFontFace: FONT,
  valAxisLabelFontFace: FONT,
  valGridLine: { color: COLORS.seastoneGrey, size: 0.5 },
  catGridLine: { style: "none" },
  showLegend: true,
  legendPos: "b",
  legendFontFace: FONT,
  legendColor: COLORS.darkGreen
};
```
