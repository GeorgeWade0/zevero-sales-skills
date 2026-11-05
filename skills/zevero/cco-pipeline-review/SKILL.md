---
name: "cco-pipeline-review"
description: "Weekly Zevero pipeline & deal review prep for George (CCO). Trigger on \"pipeline review\", \"prep my pipeline call\", \"deal review\", \"pipeline health\", \"stale deals\", or \"what's stuck in the pipeline\". Produces per-region prep (UK/Japan/APAC run as separate calls) from HubSpot with a ready-to-run agenda per regional lead."
---

# CCO Pipeline & Deal Review Prep (Zevero)

Prepare George for his regional pipeline calls. Calls run PER REGION — default to prepping all three as separate sections (UK / Japan / APAC), or just the one George names. Read-only against HubSpot.

## George's operating context
- Regional leads (report to George): JP — Kosuke Motohashi (owner 1722826374); APAC — Mizuho Taniguchi (1211697223); UK — Joe Johnson (1587076576) + James Carter (335736197) jointly, George de-facto UK lead. Other JP reps: Shun Sasaki (983823408), Kazuki Hamada (2006020156), Yoshio Kawanishi (1208056903). APAC also: Kevin Milla (1554898936). Address agenda questions to the deal owner; frame escalations for the regional lead.
- George engages personally on strategic logos regardless of size (e.g. Arsenal FC, Premier League, Suntory, Amazon JP, Tokyo Metropolitan Government) and anything stuck/slipping. No $ threshold.
- "Revisit Later" stages (UK 1077299567, JP 1094367565, APAC 1085330743) are NOT pipeline — exclude from all totals and coverage; mention only as a quarterly cleanup audit (JP holds ~$1.7m parked; keep an eye on it growing).
- Renewals pipeline (765893559) is owned by Customer Success, not the reps — EXCLUDE from regional call agendas. If renewals hygiene is bad (unvalued deals, no close dates), note it once as a message for CS, separately.
- Always flag: strategic-logo movement; losses ≥$25k with reason; Negotiation/Verbal Agreement deals quiet 14+ days; anything that moves a commercial KR the wrong way.

## HubSpot config (portal 20432895, amounts = `amount_in_home_currency`, USD)
- Pipelines: UK `740537691`, JP `751468103`, APAC `746359176`, Renewals `765893559`.
- Stage IDs — UK: 1077320478 Discovery, 1077320479 Demo Scheduled, 1077320480 Scoping, 1077320481 Proposal Sent, 1077320482 Negotiation, 1077299566 Trial, 1077299565 Verbal Agreement. JP: 1094431809 Discovery, 1094431810 Demo, 1094431811 Scoping, 1094431812 Proposal, 1094431813 Negotiation, 1094491959 Trial, 1094491958 Verbal Agreement. APAC: 1085121090 Discovery, 1085121091 Demo, 1085121092 Scoping, 1085121093 Proposal, 1085330741 Negotiation, 1085330742 Trial, 1085121094 Verbal Agreement.

## Data handling (learned the hard way)
- 350+ open deals: `search_crm_objects` caps at 200/page — ALWAYS check `total` and paginate with `offset`. Digest oversized tool results via a subagent (general-purpose) rather than reading them into main context.
- Prefer `query_crm_data` SQL (GROUP BY pipeline, dealstage) for funnel totals if permitted; if it errors on permissions, fall back to search + subagent digestion (reconnecting HubSpot with expanded scopes fixes this).
- Useful properties: dealname, pipeline, dealstage, amount_in_home_currency, closedate, createdate, hubspot_owner_id, hs_v2_date_entered_current_stage, notes_last_updated, hs_next_step.

## Analysis per region (active stages only)
1. Funnel: count + $ by stage; weighted total.
2. Movement (7d): advanced / created / won / lost with $.
3. Stallers: no stage change 21+ days (30+ for Discovery), ranked by $.
4. Hygiene: past close dates, missing amounts, missing next steps.
5. Closing this month with RAG: green = Negotiation+ and recent activity; amber = late-stage but quiet 14+ days; red = early-stage or previously slipped.
6. Coverage vs KR targets: UK $400k / APAC $300k / JP $3m pipeline maintenance, plus pace vs ARR-add KRs (ARR-add = ALL new-biz closed-won incl. addons).

## Output
Per region: compact health table + one-line verdict, then agenda ordered by $ at stake (5–8 deals: owner, stage, days in stage, the specific question to ask). End each region with hygiene asks and any coverage gap needing prospecting focus. Strategic logos get flagged even when small. If a region has nothing notable, one line.

Offer to save as a doc or draft per-region Slack messages (draft only — George sends). Read-only; never modify deals.
