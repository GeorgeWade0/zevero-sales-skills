---
name: "uk-brief-for-ben"
description: "Edit or regenerate George's UK commercial brief for Ben (Zevero) as an on-brand Google Doc. Trigger on \"edit the UK brief\", \"update Ben's brief\", \"the brief for Ben\", \"add [x] to the UK brief\", \"regenerate the commercial brief\", or any request to change/refresh that document. Holds the current content, the Zevero brand styling, and the HubSpot queries needed to refresh the numbers."
---

# UK Commercial Brief for Ben (Zevero)

Maintains George Wade's (CCO) UK commercial standing-and-outlook brief, written for his co-founder Ben. Output is an on-brand **Google Doc** so George can edit and Ben can comment.

## Key constraint
The Google Drive connector can **create** files but not edit them in place. Every change means generating a NEW Google Doc from the full updated HTML (`create_file` with `contentMimeType: text/html`, title "UK Commercial Brief — Ben"). Tell George the new link and that the previous copy can be deleted. Do not attempt partial edits.

## Brand styling (Zevero presentation system, document variant)
- Font: Manrope (Arial fallback). **No bold anywhere** — hierarchy from size and colour.
- Body text `#0A1414` (near-black; George found grey `#7A7A7A` hard to read — never use grey for body).
- Section labels: ALL CAPS, 8pt, letter-spacing 2px, Accent Blue `#28A0CC`.
- Title: 24pt, Regular weight, sentence case, Dark Green `#002321`.
- Emphasis (figures, key phrases): Accent Blue `#28A0CC`. Never yellow on light backgrounds.
- Bullets: arrow `&rarr;` in Accent Blue, never `•`.
- Tables: header row fill Base Green `#265A62` with white text; body rows `#0A1414` with `1px solid #DBE5E7` bottom borders; numeric columns right-aligned.
- Callout/insight panel: background Seastone `#EDF2F3`, 9pt.
- Separators: middle dots ` · `, never em dashes. British English. No emoji.

## Current structure (keep unless George says otherwise)
1. Header label `COMMERCIAL · UK`, title "UK commercial standing and outlook", byline "Prepared for Ben · [date] · George Wade, CCO".
2. **WHERE WE ARE** — won MTD, deals about to land, H1 vs target, open pipeline vs target, recent creation.
3. **CLOSING BY END OF JULY** (rename to the current period) — named deals with amount, owner, stage age, status.
4. **PIPELINE CREATION · LAST 3 MONTHS** — table: Month / New deals / Value created / Avg deal size, plus Seastone insight panel naming the big logos.
5. **WHO SOURCED [period]'S PIPELINE** — SDR split from the `meeting_booked_by` field, with the caveat that the field only went live in July 2026 so older deals are unattributed.
6. **FORECAST · NEXT 3 MONTHS** — per month: likely, with worst/best on the near month; then total and the method line.
7. **RISKS** — 2–3 specific, honest items.

## Refreshing the numbers (HubSpot portal 20432895, USD via `amount_in_home_currency`)
- UK new-biz pipeline `740537691`. EXCLUDE stage `1077299567` (Revisit Later) and the 27 `$0` "Zevero Lite" trial records. Renewals pipeline `765893559` is CS-owned — out of scope.
- UK stages: 1077320478 Discovery, 1077320479 Demo Scheduled, 1077320480 Scoping, 1077320481 Proposal Sent, 1077320482 Negotiation, 1077299566 Trial, 1077299565 Verbal Agreement.
- People: Joe Johnson (owner 1587076576) and James Carter (335736197) are the UK AEs, George is de-facto UK lead. SDRs seen in `meeting_booked_by`: George Harper, Tom Templeman, Georgie McCarthy.
- `search_crm_objects` caps at 200 results — check `total` and paginate; digest oversized results via a subagent. `query_crm_data` SQL fails on permissions in this portal; use search.
- Forecast method: stage-weighted (VA 90%, Negotiation 70%, Trial 60%, Proposal 50%, Scoping 35%, Demo 20%, Discovery 10%), then judgement adjustments — downgrade deals quiet 30+ days or with past-due close dates, upgrade recently active ones, exclude 90-day zombies. Show best/likely/worst.

## Known gaps George may ask to add
- Win rate and median cycle length (validates the forecast — the strongest addition).
- Losses with reasons (UK lost ~$35k in the week to 29 Jul: FreshLinc, Vitaflo, Pentire, Locate Productions).
- Path to target: gap between forecast and target, and what closes it.
- Marketing-sourced share, to sit alongside the SDR split.

## Rules
- Ben is a co-founder: numbers first, no hype, flag bad news plainly.
- George's own deal context overrides HubSpot inference (e.g. he judged Riley, Foreva, Foilco and Origin as August rollovers despite July close dates).
- Read-only against HubSpot. Never send anything — George shares the doc himself.
