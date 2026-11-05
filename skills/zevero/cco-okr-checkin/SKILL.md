---
name: "cco-okr-checkin"
description: "Zevero 2026 OKR check-in and update for George (CCO). Trigger on \"OKR check-in\", \"update the OKRs\", \"how are we tracking on OKRs\", \"refresh KR numbers\", \"OKR review\", or \"draft OKR commentary\". Pulls latest commercial numbers from HubSpot, flags at-risk KRs, drafts Current Value/Trend/Commentary updates, and writes to Notion only after George approves."
---

# CCO OKR Check-in & Update (Zevero)

Refresh the 2026 OKR picture with live data, then draft Notion updates for George's approval. NEVER write to Notion before explicit approval in this conversation.

## George's operating context
- ARR-add KRs (UK $400k, APAC $300k H1) count ALL new-biz closed-won incl. addons/upsells in the regional pipelines.
- Pipeline-maintenance KRs: measure ACTIVE stages only — exclude "Revisit Later" (UK 1077299567, JP 1094367565, APAC 1085330743). Note: the APAC Notion value has historically included Revisit Later deals — call out the discrepancy rather than silently matching it.
- Renewals pipeline (765893559) is CS-owned; relevant to the NRR KR, not the regional ARR KRs.
- Flag immediately: any KR whose live number trends down WoW.
- Regional leads: JP Kosuke Motohashi, APAC Mizuho Taniguchi, UK Joe Johnson + James Carter (George de-facto lead) — name the accountable lead in commentary for at-risk KRs.
- George Wade = Notion user `08d3cfaa-a453-45f7-a087-677869373bb2` (owns Objective 1 "Scale to $7m revenue with platform as the engine").

## Step 1 — Read current OKR state from Notion
- Key Results: `collection://32c47725-133b-806d-b0cf-000bdefe7d38`; Objectives: `collection://32c47725-133b-80f7-96a8-000b002df408`; Initiatives: `collection://3ab47725-133b-8090-8cd3-000b8cf7d357`.
- Query all KRs (title, Status, Deadline, Region, Start/Current/Target Value, Trend, Commentary, Owner, Objective, Last edited time). Progress formula not SQL-queryable — compute (Current−Start)/(Target−Start), inverted for reduce-targets. Note staleness via Last edited time. H1 KRs past deadline → flag for close-out/rollover (Q3 planning pages exist under the OKR home `32c47725-133b-801d-951d-d593b45db111`).

## Step 2 — Pull fresh evidence (HubSpot portal 20432895, USD via amount_in_home_currency)
- Pipelines: UK `740537691`, JP `751468103`, APAC `746359176`, Renewals `765893559`.
- ARR KRs: sum closed-won since period start per region. Pipeline KRs: current open pipeline per region, ACTIVE stages only.
- 350+ open deals: check `total`, paginate with offset, digest big results via subagent. `query_crm_data` SQL preferred; on permissions error fall back to `search_crm_objects`.
- Marketing KRs: HubSpot campaign/attribution reports where available, else mark "needs marketing input". Non-commercial KRs (engineering, NPS, engagement): keep Notion's value, mark "no live source".

## Step 3 — Draft the check-in
Table: KR | Notion value | Live value | Δ | Progress % | proposed Status | proposed Trend | proposed Commentary (1–2 factual sentences naming the driver — specific deals won/slipped and the accountable lead). Then a "what's driving risk" paragraph for At Risk items. Show arithmetic where live differs materially from Notion.

## Step 4 — Approval gate, then write
Ask which updates to apply (all/subset/none). On approval, update approved KR pages (Current Value, Trend, Status, Commentary) via Notion page-update; confirm with links. If asked, add a dated entry under Monthly Reports (`32d47725-133b-80d4-887d-d1f0ac0383a1`).
