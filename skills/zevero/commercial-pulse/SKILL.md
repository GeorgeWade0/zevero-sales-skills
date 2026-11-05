---
name: commercial-pulse
description: Install or refresh the Zevero Commercial Pulse dashboard in Cowork. Use when the user asks to "show me Commercial Pulse", "open the commercial dashboard", "where are we on pipeline", "pipeline pulse", "team pipeline view", "Zevero pipeline dashboard", "install commercial pulse", or any similar request to see the team-wide commercial pipeline. Also trigger if the user mentions Zevero pipeline metrics, closing this month, won MTD, or wants the same Commercial Pulse dashboard George (CCO) uses.
---

# Commercial Pulse

Installs the Commercial Pulse artifact in the user's Cowork sidebar. The artifact renders a live dashboard against the Zevero HubSpot portal: new-biz funnel (UK / JP / APAC), renewal funnel, hero tiles for open pipeline / weighted / closing this month / won MTD, closing-this-month deal list with RAG, top stallers, and overdue close-date hygiene. Auto-refreshes every 10 minutes.

## What to do

1. Verify HubSpot is connected. If `mcp__1c001c12-08ac-42b6-9021-e8066bcbb1de__search_crm_objects` is not available, stop and tell the user: "Commercial Pulse needs the HubSpot connector. Connect it in Cowork settings, then run this again." Don't try to install the artifact without HubSpot.

2. Copy the artifact HTML from this skill's references folder into the user's outputs directory so Cowork can install it. The artifact source lives at `references/artifact.html` inside this skill. Use the Read tool to load it, then Write it to the user's outputs directory at a path you'll pass to `create_artifact`.

3. Check whether the artifact already exists by calling `mcp__cowork__list_artifacts`. Look for `id: "commercial-pulse"`.

4. **If it does NOT exist:** call `mcp__cowork__create_artifact` with:
   - `id`: `commercial-pulse`
   - `html_path`: the absolute path you just wrote the HTML to
   - `description`: `Live Zevero commercial pipeline — new-biz and renewal funnels, closing this month with RAG, stallers, and hygiene. Pulls from HubSpot. Refreshes every 10 min.`
   - `mcp_tools`: `["mcp__1c001c12-08ac-42b6-9021-e8066bcbb1de__search_crm_objects"]`

5. **If it already exists:** call `mcp__cowork__update_artifact` with:
   - `id`: `commercial-pulse`
   - `html_path`: same path
   - `update_summary`: `Refresh Commercial Pulse to the latest plugin version.`

6. Confirm to the user: "Commercial Pulse is now in your Cowork sidebar. Open it to see live pipeline against the Zevero HubSpot portal. Refreshes every 10 minutes." Include a brief one-line summary if you want, but don't reproduce the dashboard data in chat — the artifact is where they should look.

## Configuration baked in

- HubSpot portal: `20432895`
- New-biz pipelines: UK `740537691`, JP `751468103`, APAC `746359176`
- Renewal pipeline: `765893559`
- Stage IDs and ordering normalised across UK / JP / APAC into: Discovery → Demo Scheduled → Scoping → Proposal Sent → Negotiation → Trial → Verbal Agreement
- Renewal funnel: Identified → Meeting Scheduled → Contracting → Verbal Agreement
- Currency: USD across the board (uses `amount_in_home_currency` from HubSpot — JPY, GBP and other native deal currencies are auto-converted by HubSpot's exchange rate)

## Notes for the installing user

- This artifact reads pipeline data from the Zevero HubSpot portal (`20432895`). You need to be connected to HubSpot in Cowork settings and have at least view access to that portal.
- Data is org-wide pipeline, not personal. Every Zevero teammate who installs this sees the same figures.
- Deal rows are clickable and deep-link into HubSpot.
- The artifact will not work if opened outside Cowork (e.g. dragged into a browser) — it depends on Cowork's MCP runtime.
