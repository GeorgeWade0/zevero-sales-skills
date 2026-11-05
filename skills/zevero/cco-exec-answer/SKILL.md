---
name: "cco-exec-answer"
description: "Answer exec/co-founder commercial questions for George (CCO, Zevero) with live data, fast. Trigger on \"my co-founder asked...\", \"what's our UK/Japan/APAC standing\", \"commercial forecast for the next few months\", \"quick report on [region/metric]\", \"where are we against goals\", or any ad-hoc leadership question about commercial performance. Produces a Slack-ready answer."
---

# CCO Exec Answer (Zevero)

Answer ad-hoc commercial questions from George's co-founder/leadership (e.g. "Commercial UK standing and plan/forecast over next few months") in minutes, grounded in live data. Output: a **Slack-ready message** George can paste — tight, numbers-first, honest about risk. No preamble, no fluff.

## Context
- Company objectives: #1 "Scale to $7m revenue with platform as the engine" (George's), #2 renewal/expansion, #3 profitable delivery. KR targets: UK $400k ARR-add H1 + $400k pipeline; APAC $300k ARR-add H1 + $300k pipeline; Japan $2m EPD Q2 + $3m pipeline. ARR-add = ALL new-biz closed-won incl. addons. (H1 KRs may have rolled to Q3 versions — check Notion for current-quarter KRs.)
- Regional leads: JP — Kosuke Motohashi (1722826374); APAC — Mizuho Taniguchi (1211697223); UK — Joe Johnson (1587076576) + James Carter (335736197), George de-facto lead. Renewals = Customer Success, not sales.

## Data (pull only what the question needs)
- **Notion KRs**: `collection://32c47725-133b-806d-b0cf-000bdefe7d38` (SQL query; compute progress from Start/Current/Target).
- **HubSpot** portal 20432895, USD via `amount_in_home_currency`. Pipelines: UK `740537691`, JP `751468103`, APAC `746359176`, Renewals `765893559`. Stage IDs — UK: 1077320478 Discovery, 1077320479 Demo, 1077320480 Scoping, 1077320481 Proposal, 1077320482 Negotiation, 1077299566 Trial, 1077299565 Verbal Agreement (JP: 1094431809/10/11/12/13, 1094491959 Trial, 1094491958 VA; APAC: 1085121090/91/92/93, 1085330741 Neg, 1085330742 Trial, 1085121094 VA). EXCLUDE "Revisit Later" (UK 1077299567, JP 1094367565, APAC 1085330743) from all pipeline numbers.
- 350+ open deals: check `total`, paginate (offset), digest large results via subagent. `query_crm_data` SQL preferred if permitted; fall back to `search_crm_objects` on permissions errors.

## Forecast method (George's preference: weighted + judgement)
1. Base: stage-weighted open pipeline by expected close month. Default weights: Discovery 10%, Demo 20%, Scoping 35%, Proposal 50%, Negotiation 70%, Trial 60%, Verbal Agreement 90%.
2. Judgement adjustments (state them explicitly): downgrade deals quiet 30+ days or with past-due close dates; upgrade deals with recent activity; exclude obvious zombies (Revisit-Later-adjacent, 90+ days stalled).
3. Present best / likely / worst per month for the asked horizon, plus won-to-date for the period.

## Output template (Slack-ready)
**[Region] commercial standing — [date]**
- Where we are: won QTD/YTD $, vs KR target, open + weighted pipeline.
- Forecast (next N months): best / likely / worst with one line on what swings it.
- What's driving it: 2–3 named deals or dynamics.
- Risks: honest, specific.
- Plan: 2–3 actions with owners.

Keep under ~200 words unless George asks for depth. Show working (weights, adjustments) in chat below the Slack message so George can sanity-check, but keep the message itself clean. Never send anything — George pastes/forwards it himself.
