---
name: "cco-weekly-brief"
description: "George's Monday CCO brief for Zevero. Trigger on \"run my CCO brief\", \"weekly brief\", \"Monday brief\", \"start my week\", \"what should I focus on this week\", or when the scheduled Monday task fires. Combines 2026 OKR status from Notion, HubSpot pipeline movement, and this week's calendar into one prioritised brief."
---

# CCO Weekly Brief (Zevero)

George's start-of-week brief: OKR status → pipeline movement → week ahead → top 3 priorities. Inline visual (zevero-brand styling if available) + short chat summary. One screen, not a report.

## George's operating context
- Regional leads (report to George): JP — Kosuke Motohashi (HubSpot owner 1722826374); APAC — Mizuho Taniguchi (1211697223); UK — Joe Johnson (1587076576) + James Carter (335736197), George de-facto UK lead. Other JP reps: Shun Sasaki (983823408), Kazuki Hamada (2006020156), Yoshio Kawanishi (1208056903).
- Always flag: strategic-logo movement (Arsenal FC, Premier League, Suntory, Amazon JP, Tokyo Metropolitan Government and similar name-brands); losses ≥$25k with reason; Negotiation/Verbal Agreement deals quiet 14+ days; commercial KRs trending down WoW.
- "Revisit Later" stages (UK 1077299567, JP 1094367565, APAC 1085330743) are NOT pipeline — exclude from all totals.
- Renewals pipeline (765893559) is CS-owned — one line max, only if something needs George's attention.
- ARR-add KRs = ALL new-biz closed-won (incl. addons).

## Data sources (parallel where possible)

### 1. Notion — 2026 OKRs
- Key Results data source: `collection://32c47725-133b-806d-b0cf-000bdefe7d38`; Objectives: `collection://32c47725-133b-80f7-96a8-000b002df408`; OKR home: `32c47725-133b-801d-951d-d593b45db111`.
- Query via SQL mode: Key Result, Status, Deadline, Region, Start/Current/Target Value, Trend, Commentary. Progress formula is not queryable — compute (Current−Start)/(Target−Start), inverted for reduce-targets. George Wade's Notion ID: `08d3cfaa-a453-45f7-a087-677869373bb2` (owns Objective 1 "Scale to $7m revenue with platform as the engine").

### 2. HubSpot (portal 20432895, USD via `amount_in_home_currency`)
- Pipelines: UK `740537691`, JP `751468103`, APAC `746359176`, Renewals `765893559`.
- Stage IDs — UK: 1077320478 Discovery, 1077320479 Demo, 1077320480 Scoping, 1077320481 Proposal, 1077320482 Negotiation, 1077299566 Trial, 1077299565 Verbal Agreement. JP: 1094431809 Discovery, 1094431810 Demo, 1094431811 Scoping, 1094431812 Proposal, 1094431813 Negotiation, 1094491959 Trial, 1094491958 Verbal Agreement. APAC: 1085121090 Discovery, 1085121091 Demo, 1085121092 Scoping, 1085121093 Proposal, 1085330741 Negotiation, 1085330742 Trial, 1085121094 Verbal Agreement.
- IMPORTANT: 350+ open deals; `search_crm_objects` caps at 200 — check `total`, paginate with `offset`, digest oversized results via a subagent. Prefer `query_crm_data` SQL for aggregates if permitted (permissions error → fall back to search).
- Pull per region: open + weighted pipeline (active stages only), closing this month, won last week / MTD, notable stage moves, late-stage stalls.

### 3. Google Calendar — this week's events for george@zevero.earth; flag external/customer, board/leadership meetings, prep needed.

### 4. Optional: Gmail unread deal-critical threads (3 days); Notion "Action Items - KR Owners" page `32f47725-133b-80dd-8020-ec088f97a7bc`.

## Output
1. **Headline** — one sentence vs the $7m objective.
2. **OKR scoreboard** — commercial KRs first: progress %, trend, RAG. Call out At Risk + Declining/Flat explicitly.
3. **Pipeline movement** — per region: open, weighted, closing this month, won last week; biggest moves and stallers. Strategic logos always named.
4. **Week ahead** — key meetings + prep needed.
5. **Top 3 priorities** — highest leverage on at-risk KRs; name deals, owners, actions. Nothing a generic CCO could have written.

## Rules
- Read-only; never write to Notion/HubSpot.
- Missing connector → produce from what's available, note the gap in one line.
- Scheduled/non-interactive run → no clarifying questions, full brief.
