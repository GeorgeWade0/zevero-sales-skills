# Discovery brief widget template

Render the brief via `mcp__visualize__show_widget`. Use `title` like `<company_slug>_discovery_brief` (snake_case, e.g. `north_south_wines_discovery_brief`).

Pass three short, slightly playful `loading_messages` — examples: `["Styling the brief", "Laying out the one-pager", "Polishing the panel"]`. Keep them generic enough to suit any company.

## Template

Copy the block below, fill in the placeholders, and pass as `widget_code`. Keep section structure exactly as shown — the design depends on it.

```html
<style>
  .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }
  .brief { padding: 1rem 0; font-family: var(--font-sans); color: var(--color-text-primary); }
  .brief .h1 { font-size: 22px; font-weight: 500; margin: 0 0 4px; letter-spacing: -0.01em; }
  .brief .sub { font-size: 14px; color: var(--color-text-secondary); margin: 0 0 1.25rem; }
  .brief .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; margin: 0 0 1.5rem; }
  .brief .stat { background: var(--color-background-secondary); border-radius: var(--border-radius-md); padding: 12px 14px; }
  .brief .stat-l { font-size: 12px; color: var(--color-text-secondary); margin: 0 0 4px; }
  .brief .stat-v { font-size: 15px; font-weight: 500; margin: 0; line-height: 1.3; }
  .brief .row { display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin: 0 0 1.25rem; }
  .brief .sec-label { font-size: 12px; font-weight: 500; color: var(--color-text-secondary); margin: 0 0 6px; letter-spacing: 0.02em; }
  .brief p { font-size: 14px; line-height: 1.55; margin: 0 0 0.5rem; color: var(--color-text-primary); }
  .brief a { color: var(--color-text-info); text-decoration: none; }
  .brief a:hover { text-decoration: underline; }
  .brief .hubspot { display: flex; align-items: center; gap: 10px; background: var(--color-background-secondary); border-radius: var(--border-radius-md); padding: 10px 14px; margin: 0 0 1.25rem; font-size: 13px; color: var(--color-text-primary); }
  .brief .hubspot .pill { display: inline-block; padding: 2px 10px; border-radius: var(--border-radius-md); font-weight: 500; font-size: 12px; }
  .brief .hubspot .pill-yes { background: #EAF3DE; color: #27500A; }
  .brief .hubspot .pill-no { background: var(--color-background-primary); color: var(--color-text-secondary); border: 0.5px solid var(--color-border-tertiary); }
  .brief .hubspot .pill-skip { background: #FAEEDA; color: #633806; }
  .brief .panel { background: #E1F5EE; border-radius: var(--border-radius-lg); padding: 1.1rem 1.25rem 1rem; margin: 0 0 1.25rem; }
  .brief .panel .sec-label { color: #085041; }
  .brief .panel .links-row { font-size: 13px; line-height: 1.6; color: #04342C; margin: 0 0 12px; }
  .brief .panel .links-row a { color: #0F6E56; }
  .brief .features { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; }
  .brief .feature { background: rgba(255,255,255,0.55); border-radius: var(--border-radius-md); padding: 12px 12px 10px; }
  .brief .feature .ico { font-size: 22px; color: #0F6E56; margin-bottom: 4px; display: block; }
  .brief .feature .ftitle { font-size: 13px; font-weight: 500; margin: 0 0 6px; color: #085041; }
  .brief .feature p { font-size: 12.5px; line-height: 1.45; color: #04342C; margin: 0 0 4px; }
  .brief .feature ul { margin: 0; padding-left: 14px; }
  .brief .feature li { font-size: 12.5px; line-height: 1.45; color: #04342C; margin-bottom: 3px; }
  .brief .fit { display: grid; grid-template-columns: 38% 1fr; gap: 0; border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-md); overflow: hidden; margin: 0 0 1.25rem; }
  .brief .fit .fhead { font-size: 12px; font-weight: 500; color: var(--color-text-secondary); padding: 8px 12px; background: var(--color-background-secondary); }
  .brief .fit .fcell { font-size: 13px; line-height: 1.45; padding: 10px 12px; border-top: 0.5px solid var(--color-border-tertiary); }
  .brief .fit .fcell.need { color: var(--color-text-primary); font-weight: 500; }
  .brief .fit .fcell.angle { color: var(--color-text-primary); }
  .brief .questions { list-style: none; padding: 0; margin: 0; }
  .brief .questions li { display: flex; align-items: flex-start; gap: 10px; font-size: 14px; line-height: 1.5; margin-bottom: 8px; color: var(--color-text-primary); }
  .brief .questions .qi { color: #1D9E75; font-size: 16px; margin-top: 2px; flex-shrink: 0; }
</style>
<h2 class="sr-only">Pre-meeting discovery brief for {{COMPANY_NAME}} with {{LEAD_NAME}}, {{LEAD_TITLE}}</h2>
<div class="brief">
  <p class="h1">{{COMPANY_NAME}}</p>
  <p class="sub">Discovery brief · meeting with {{LEAD_NAME}}, {{LEAD_TITLE}}</p>

  <div class="stats">
    <div class="stat"><p class="stat-l">{{STAT_1_LABEL}}</p><p class="stat-v">{{STAT_1_VALUE}}</p></div>
    <div class="stat"><p class="stat-l">{{STAT_2_LABEL}}</p><p class="stat-v">{{STAT_2_VALUE}}</p></div>
    <div class="stat"><p class="stat-l">{{STAT_3_LABEL}}</p><p class="stat-v">{{STAT_3_VALUE}}</p></div>
    <div class="stat"><p class="stat-l">{{STAT_4_LABEL}}</p><p class="stat-v">{{STAT_4_VALUE}}</p></div>
  </div>

  <div class="row">
    <div>
      <p class="sec-label">Company</p>
      <p>{{COMPANY_PARAGRAPH_WITH_INLINE_LINKS}}</p>
    </div>
    <div>
      <p class="sec-label">Lead</p>
      <p>{{LEAD_PARAGRAPH_WITH_INLINE_LINKS}}</p>
    </div>
  </div>

  <div class="hubspot">
    <i class="ti ti-message-circle" style="font-size:16px; color: var(--color-text-secondary);" aria-hidden="true"></i>
    <span style="flex:1;">Previous communications</span>
    {{HUBSPOT_PILL}}
  </div>

  <div class="panel">
    <p class="sec-label">Sustainability situation</p>
    <p class="links-row">Public reporting · {{REPORTING_LINKS_SEPARATED_BY_MIDDLE_DOT}}</p>

    <div class="features">
      <div class="feature">
        <i class="ti ti-leaf ico" aria-hidden="true"></i>
        <p class="ftitle">Environmental commitments</p>
        <ul>
          {{COMMITMENTS_BULLETS_AS_LI}}
        </ul>
      </div>
      <div class="feature">
        <i class="ti ti-chart-bar ico" aria-hidden="true"></i>
        <p class="ftitle">Scope 1, 2 &amp; 3</p>
        {{SCOPE_PARAGRAPHS_AS_P}}
      </div>
      <div class="feature">
        <i class="ti ti-bulb ico" aria-hidden="true"></i>
        <p class="ftitle">Likely challenges</p>
        <ul>
          {{CHALLENGES_BULLETS_AS_LI}}
        </ul>
      </div>
    </div>
  </div>

  <p class="sec-label">Where Zevero fits</p>
  <div class="fit">
    <div class="fhead">Their need</div>
    <div class="fhead">Zevero angle</div>
    {{FIT_ROWS_AS_PAIRED_DIVS}}
  </div>

  <p class="sec-label">Discovery questions for {{LEAD_FIRST_NAME}}</p>
  <ul class="questions">
    {{QUESTIONS_AS_LI_WITH_CHECK_ICON}}
  </ul>
</div>
```

## How to fill the placeholders

### Stats row

Pick the four most striking facts. Each value must be ≤4 words.

Good choices: industry, B Corp score + year, ISO certifications, headline emissions target, headcount, revenue band, recent funding, named customer count.

Example: `Industry` / `Wine distribution` · `B Corp` / `88.5 · since 2023` · `ISO 14001` / `Certified Nov 2025` · `2030 target` / `−25% intensity`.

### Company paragraph

Two to three sentences. Always end with the website link, and the Companies House / equivalent registry link if findable. Inline links — never plain URLs.

### Lead paragraph

Two to three sentences. Confirm title, who they report to (if known), tenure or background, then end with the LinkedIn link. If tenure isn't confirmable, write something like "Tenure not confirmable publicly — worth asking on the call."

### HubSpot pill

Pick one based on your HubSpot search result:

- **Yes (prior engagement):** `<a href="{{HUBSPOT_COMPANY_URL}}" class="pill pill-yes">Yes — view in HubSpot</a>`
- **No (no prior engagement):** `<span class="pill pill-no">No prior engagement</span>`
- **Not checked (e.g. HubSpot unavailable):** `<span class="pill pill-skip">Not checked</span>`

### Sustainability panel — reporting links

Three to six anchor tags separated by ` · ` (space-middledot-space). Use the panel link colour (`#0F6E56`) — set inline if needed:

```html
<a href="..." style="color:#0F6E56;">Our Impact</a> · <a href="..." style="color:#0F6E56;">Impact Report 2025</a>
```

### Environmental commitments

Four to six short `<li>` items. Each bullet is one fact: certification, target, signatory status, programme. Keep them telegraphic — no full sentences.

### Scope 1, 2 & 3

Two short `<p>` paragraphs. The first describes their measurement status. The second states whether a software provider is named — and if not, explicitly says "Software / provider not disclosed publicly. Highest-value question for the call." Do not bold mid-sentence.

### Likely challenges

Four to six short `<li>` items. Pull directly from what you found. If they're tackling something specific (CSRD, B Corp recert, bottle weight), name it.

### Where Zevero fits — rows

Five to eight paired divs. Format each row as:

```html
<div class="fcell need">{{their_need}}</div><div class="fcell angle">{{zevero_angle}}</div>
```

Pull rows from `zevero_fit_angles.md` but only the ones that genuinely apply.

### Discovery questions

Four to six `<li>` items. Always include this format:

```html
<li><i class="ti ti-circle-check qi" aria-hidden="true"></i>{{question}}</li>
```

Tailor to what you found. If the software provider wasn't disclosed, that's question 1. Examples of good questions: "How are you measuring Scope 1–3 today?", "Spend-based or supplier-specific Scope 3?", "Is SBTi on the roadmap?", "Who else in the business needs this data?".

## Constraints — don't break these

- Sentence case throughout. No Title Case, no ALL CAPS.
- No emoji. Icons only via Tabler outline classes (`ti ti-…`).
- No mid-sentence bolding.
- Hardcoded teal hex values inside the panel are intentional — they keep the mint look across light/dark mode. Don't swap them for CSS variables.
- Don't add a sources list at the bottom. All links inline.
- Don't include filler sections if there's nothing to say. Better to drop a row than pad.
