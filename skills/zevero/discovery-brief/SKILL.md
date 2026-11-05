---
name: discovery-brief
description: >
  Build a pre-meeting intelligence brief for a Zevero discovery call. Triggers include
  "build a discovery brief", "brief for [company]", "pre-meeting brief", "prep me for
  [company]", "research [company] before my call", "I have a call with [company]",
  "discovery brief: [company]", "intel on [company]", "cheat sheet for [meeting]", "prep
  for my meeting with [name] at [company]", "background on [company]" — or any phrase
  about preparing for a sales call or external meeting. Takes a company name and a lead
  name, checks HubSpot for prior engagement, researches the company and the lead,
  deep-dives their sustainability situation (commitments, scope 1/2/3 measurement,
  software provider, challenges), maps it to where Zevero fits, and renders a one-page
  visual brief inline. Trigger even if the user only says "brief for [company]" — sales
  reps use this before every discovery call.
---

# Discovery brief

You are preparing a pre-meeting intelligence brief for a Zevero salesperson going into a discovery call. The deliverable is a one-page visual brief rendered inline via `mcp__visualize__show_widget`, in the Zevero cheat-sheet style.

## What you need from the user

- **Company name** — the prospect.
- **Lead name** — the person they're meeting with. Title is helpful but optional.

If either is missing, use AskUserQuestion to gather them. Don't proceed without both. If the user has provided a meeting time or any additional context (e.g. "they're a wholesale distributor"), use it but don't ask for more.

## Workflow

Run independent phases in parallel where possible — phases 1 through 4 can all kick off together.

### 1. Check HubSpot

Search HubSpot for the company using `mcp__1c001c12-08ac-42b6-9021-e8066bcbb1de__search_crm_objects` against the `companies` object type. You only need to know whether the company exists in the CRM — not a full history dump.

- If a company record is found → record the HubSpot URL for the company.
- If nothing matches → "No prior engagement".

The salesperson will click through to HubSpot for the full picture; the brief just surfaces the yes/no signal.

### 2. Research the company

Use WebSearch and web_fetch to find:

- Industry / sector and a 1–2 sentence description
- Website URL and HQ location
- Approximate size (employees / revenue if findable)
- Notable accolades or recent press (B Corp, ISO, awards, funding, recent news)

Two or three sentences is plenty. The brief is not a Wikipedia article.

### 3. Research the lead

Use WebSearch to find:

- Job title (confirm the user's claim)
- Who they report to, if findable
- Tenure or background highlights
- LinkedIn URL

If tenure isn't confirmable from public sources, say so explicitly — it becomes a useful question for the call. Don't fabricate.

### 4. Sustainability deep-dive — the most important section

Find:

- **Their sustainability / impact / ESG content** — a website page, an impact report PDF, a B Corp profile, a CDP submission. Always link it. If a company has multiple reporting surfaces, link the most authoritative one and one or two supplements.
- **Environmental commitments** — net zero dates, intensity targets, SBTi commitment, B Corp, ISO 14001, signatory of charters (Sustainable Wine Roundtable, Race to Zero, SME Climate Hub, Better Cotton, etc.), reduction roadmaps.
- **Scope 1, 2 & 3 measurement status.** Have they measured? How? **Do they name a software or solution provider?** (Greenly, Watershed, Planet Mark, Compare Your Footprint, Sweep, Persefoni, Plan A, Normative, Sphera, Salesforce Net Zero Cloud, internal team, consultancy.) If they don't disclose a provider, **say so explicitly and flag it as the highest-value discovery question**. Companies usually proudly name their provider, so silence is a real signal.
- **Specific challenges or goals.** Common signals: struggling with scope 3, want B Corp, want SBTi, want to move from spend-based to supplier-specific data, prepping for CSRD/SECR/Streamlined Energy and Carbon Reporting, building a reduction roadmap, customer ESG questionnaires (CDP, EcoVadis), bottle weight / packaging programmes.

Where to look: the company's `/sustainability`, `/impact`, `/our-impact` and `/esg` pages; their B Corp profile if they're certified; trade press; LinkedIn posts from the lead and the head of sustainability; recent interviews.

### 5. Synthesize Zevero fit

Map what you found to the angles in `references/zevero_fit_angles.md`. Be specific — if the company doesn't have ISO 14001, don't mention the ISO angle. If they're already on Watershed, the angle is re-platforming and depth, not "first footprint". Pick 5–8 rows that genuinely apply.

End with 4–6 discovery questions tailored to the gaps you actually found, not generic ones. If they didn't disclose their software, the first question is always "what are you using to measure today?"

### 6. Render the brief

Read `references/widget_template.md` for the full HTML template and the design rules. Fill in the placeholders and call `mcp__visualize__show_widget`.

Before calling `show_widget`, call `mcp__visualize__read_me` with `modules: ["mockup"]` silently — this loads the design system context the widget renderer needs. Don't narrate this call to the user.

## Tone

The salesperson reading this is busy. Write in clipped, specific prose. Numbers and links beat adjectives. Use sentence case. No emoji. No corporate fluff. When something is unknown, say "not disclosed publicly" and turn it into a discovery question rather than guessing.

## After rendering

Write a short (1–3 sentences) post-amble in chat that calls out any open questions or red flags the salesperson should clock before the call. Don't restate the brief — they can read it. Examples of useful post-amble:

- "Worth confirming Erin's tenure on the call — public sources still show Rebecca Murphy in the role as recently as Feb 2024."
- "They don't name a measurement provider anywhere public. Lead with that question."
- "Heads-up: there's an active deal in HubSpot from Tom — check the deal notes before the call."

That's it. Keep the loop tight: research, render, flag.
