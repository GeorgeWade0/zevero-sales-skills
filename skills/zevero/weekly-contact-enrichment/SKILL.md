---
name: weekly-contact-enrichment
description: Weekly three-part CRM hygiene sweep for Zevero HubSpot — (1) fill missing names on deal-associated contacts, (2) detect contacts whose Apollo employment no longer matches the CRM company (leavers), (3) surface likely replacement contacts for review.
---

Run a weekly CRM hygiene sweep for the Zevero HubSpot CRM. The sweep has three parts that all run in a single weekly execution.

**Apollo budget:** up to **50 `people_match` enrich calls per week** — 10 for Part 1, 40 for Part 2. Part 3 uses `apollo_mixed_people_api_search` which *may* consume additional credits depending on plan; the skill must cap Part 3 at 1 search per leaver and track actual credit consumption by reading Apollo usage headers if available, otherwise assume worst case and include the count in the Slack summary so the budget stays visible.

**Review surface:** two-layer — a Slack summary to George Wade (U01SRM118T1) AND custom HubSpot properties written to each touched contact so the state lives on the record and persists week-to-week.

**Conservative bar throughout:** it is always better to skip an ambiguous case than to write wrong data. Scheduled task runs unattended, so use `CONFIRMATION_WAIVED_FOR_SESSION` on `manage_crm_objects` calls.

---

## Step 0 — Verify prerequisites (run first, every time)

Before any work, call `search_properties` on the `contacts` object to confirm these 6 custom properties exist:

- `enrichment_name_status` — enum: `enriched`, `unparseable`, `not_checked`
- `enrichment_name_checked_at` — datetime (last time Part 1 looked at this contact)
- `enrichment_employment_status` — enum: `match`, `leaver_flagged`, `no_apollo_data`, `not_checked`
- `enrichment_employment_checked_at` — datetime (last time Part 2 looked at this contact)
- `enrichment_notes` — multi-line text (human-readable detail from whichever part last touched the record)
- `enrichment_replacement_candidate` — single-line text (name — title — email, set by Part 3)

If any property is missing: log which ones are missing, include the list in the Slack summary, and for every subsequent write omit just the missing properties from the `properties` object (don't fail the whole batch). The skill degrades gracefully — it still does the core work, it just loses some state tracking until George creates the missing properties.

Splitting into two `_status` / `_checked_at` pairs (rather than one) is deliberate: Part 1 and Part 2 have different re-check cadences (90 days vs 90 days, but tracked separately) and different concerns. A single status field would be overwritten and lose information.

---

## Part 1 — Missing-field enrichment

**Goal:** fill `firstname` / `lastname` on contacts that are on active deals and have an email but no firstname.

### 1.1 Query

Search HubSpot contacts where:
- `num_associated_deals > 0`
- `firstname` is NOT set
- `email` IS set
- AND (`enrichment_name_checked_at` is empty OR older than 90 days) — don't re-check recent `unparseable` markers

Pull up to 200 per page, paginate. If the raw result exceeds model context, save to disk and parse in a subprocess (this happens at ~150+ results).

### 1.2 Email parsing rules

For each contact:
- Split the local part on `.`, `_`, `-`
- Drop tokens that are ≤2 chars, numeric-only, or in the department wordlist: `info, admin, contact, sales, office, support, hr, team, kanri, soumu, jinji, keiri, eigyo, kikaku, pro, sd, kv, aw, pc, ii, ap, hc, biz, sus`
- Require at least 2 alphabetic tokens
- Reject tokens with 3+ consecutive consonants (catches `ksc`, `benhc`-style initials)
- Reject tokens in a small non-names list: `dreamplan, product, company, corp, group, ltd, test`
- For Japanese TLDs (`.co.jp, .jp, .or.jp, .ac.jp, .ne.jp`): assume `lastname.firstname` order, BUT skip as ambiguous if the first token matches a list of common Japanese given names (otherwise the rule inverts real names — e.g. `hideto.iwata@…` becomes "Iwata Hideto" which is wrong)
- For Western TLDs: assume `firstname.lastname`; for personal domains (`gmail.com, yahoo.com, hotmail.com, outlook.com, icloud.com, aol.com, protonmail.com, live.com, msn.com, mail.com`) skip email parsing and defer to Apollo

### 1.3 Apollo fallback (budget: 10 credits)

For contacts where email parsing failed AND the domain is Western (including personal domains above): try Apollo `people_match` one at a time. Prioritise corporate domains over personal, then most-recently-modified.

### 1.4 Writes

Batch via `manage_crm_objects` with `CONFIRMATION_WAIVED_FOR_SESSION`, max 10 objects per call.

**For resolved contacts (name found):**
- `firstname`, `lastname`
- `enrichment_name_status = enriched`
- `enrichment_name_checked_at = <now>`
- `enrichment_notes = "Part 1: resolved via <email_parse_jp | email_parse_western | apollo_match>"`

**For skipped / unresolvable contacts:**
- `enrichment_name_status = unparseable`
- `enrichment_name_checked_at = <now>`
- `enrichment_notes = "Part 1: <reason code, e.g. jp_ambiguous, insufficient_parts, apollo_no_name, apollo_role_based, apollo_catchall>"`

Do NOT write to `enrichment_employment_*` in Part 1.

---

## Part 2 — Stale-employment detection

**Goal:** flag contacts whose Apollo-reported current employer no longer matches the HubSpot associated company. Highest-value signal for deal protection.

### 2.1 Build the priority queue

Two-step process since HubSpot contact search can't directly filter on "associated to an open-stage deal":

1. Search **deals** where `dealstage NOT IN (closedwon, closedlost)`, sorted by `amount` descending. Collect deal IDs.
2. Search **contacts** using `associatedWith` filter on those deal IDs, restricted to contacts where `enrichment_employment_checked_at` is empty OR older than 90 days.

Take the top 40 by associated deal value (ties broken by most-recently-modified contact).

### 2.2 Apollo employment check (budget: 40 credits)

For each of the 40 contacts, one `people_match` call with `email` as the only parameter. Read `employment_history` from the response.

**Match criteria** (contact is still there — set `enrichment_employment_status = match`):
- Apollo's current employer (`employment_history` entry with `current: true`) has a `primary_domain` equal to the HubSpot associated company domain, OR
- Apollo's current org name fuzzy-matches the HubSpot company name (Levenshtein distance ≤ 3, or one is substring of the other after lowercasing and stripping punctuation / corp suffixes like "Inc", "Ltd", "（株）")

**Known edge case:** many Zevero companies are Japanese and may appear in Apollo with a Japanese-script name (e.g. `株式会社メディアシステム`) while the HubSpot record has the English name (`Media System`) — fall back to comparing the Apollo organisation's `primary_domain` against the contact's email domain. If those match, treat as match regardless of name strings.

**Mismatch criteria** (likely leaver — set `enrichment_employment_status = leaver_flagged`):
- Apollo has a `current: true` employment record
- AND the organization domain AND name both differ materially from the HubSpot company
- AND we have both sides of the comparison populated (if the HubSpot company is missing, treat as `no_apollo_data` instead — we can't confirm a mismatch without a baseline)

**No-data:**
- No `current: true` employment in the Apollo response
- OR Apollo returned a role-based/catchall flag
- OR Apollo returned no person match at all
- Set `enrichment_employment_status = no_apollo_data`

### 2.3 Writes

For each contact, update:
- `enrichment_employment_status = <match | leaver_flagged | no_apollo_data>`
- `enrichment_employment_checked_at = <now>`
- `enrichment_notes` — append (don't overwrite Part 1's entry): `"Part 2: <detail>. Apollo current: <org_name> (<domain>). Title: <title>. LinkedIn: <url>"` for leaver_flagged; shorter for match/no_apollo_data.

Do NOT write to `enrichment_name_*` in Part 2.

---

## Part 3 — Replacement-contact surfacing (report-only)

**Goal:** for each `leaver_flagged` contact from Part 2, surface the most likely replacement at the same company in the same role. No writes to create new contacts; this is a suggestion for George to review.

### 3.1 For each leaver

1. Pull the leaver's HubSpot `jobtitle` and associated company domain.
2. Call `apollo_mixed_people_api_search` with:
   - `q_organization_domains_list` = [leaver's company domain]
   - `person_titles` = [leaver's jobtitle] (if set; if not, skip Part 3 for this leaver — title-less search is noise)
   - Limit 3 results
3. Take the top result (or none if search returns nothing).

### 3.2 Cost note

`apollo_mixed_people_api_search` is a *search* call. On Apollo's paid plans, search is generally unmetered, but *revealing* a person's email typically costs an enrich credit. The tool's response may already include the email if Apollo has previously revealed it for our workspace; if it doesn't, do NOT call an enrich endpoint to reveal it — surface whatever is already available (name + title + LinkedIn is enough to review).

On the first live run, the skill should record the Apollo credit balance before and after to verify actual cost, and include that in the Slack summary. If search ends up costing credits, the skill must be adjusted in a follow-up.

### 3.3 Writes to the leaver's record

- `enrichment_replacement_candidate = "<name> — <title> — <email or 'email not available via search'>"`
- Append to `enrichment_notes`: `"Part 3: replacement candidate <name>, LinkedIn <url>"`

### 3.4 Explicitly do NOT

- Create a new contact in HubSpot
- Demote or alter the leaver's association to the deal
- Send any email

---

## Slack summary

Send to `U01SRM118T1` (George Wade DM). No markdown tables (Slack rejects them — use bullet points).

Structure:

```
*Weekly CRM Hygiene Sweep — <YYYY-MM-DD>*

*Setup*
• All 6 custom properties present: <yes/no>  (if no, list missing)
• Apollo credit balance before run: <n>  (if available)

*Part 1 — Missing names*
• Candidates: <n>  •  Enriched: <n> (email <n>, Apollo <n>)  •  Marked unparseable: <n>
• Apollo credits used: <n>/10
• Notable enrichments: <up to 3 bullets — focus on high-profile companies>

*Part 2 — Stale employment*
• Contacts checked: <n>  (selected from open-deal queue by amount)
• Leavers flagged: <n>  •  Confirmed in-seat: <n>  •  No Apollo data: <n>
• Apollo credits used: <n>/40

*Part 3 — Replacement candidates*
For each of the <n> leavers, one entry:
• *Leaver:* <name> — <title> — <company> — HubSpot link
  *Open deal(s):* <amount, stage, link>
  *Suggested replacement:* <name> — <title> — <email | 'search-only'> — <LinkedIn url>

*Deals at risk*
Total open-deal amount tied to flagged leavers: <sum>
Top 5 deals: <dealname — amount — stage — link>

*Apollo credits used this run: <total> / 50 budget*
```

No "reply in thread to approve" language — there's no automation listening. Just present the data; George actions it in HubSpot directly.

---

## Error handling

- HubSpot search result > model context budget → save to file, parse in subprocess (proven approach from v1).
- Apollo error on an individual lookup → count against budget, continue. Record `apollo_error` in notes.
- HubSpot write failure (e.g. property doesn't exist) → retry that individual contact's write with only the properties that exist; report in Slack which properties failed.
- Apollo credit balance approaching zero mid-run → finish whatever write is in flight, stop making new Apollo calls, surface in Slack.
- Slack send failure → save the summary to `/sessions/nifty-festive-lovelace/mnt/outputs/weekly-sweep-<date>.md` so nothing is lost.

---

## Metrics in the first-of-month run

On the first scheduled run of each calendar month, also compute and include in the Slack summary:

- **Zevero decay rate:** of contacts whose `enrichment_employment_status` went from `match` to `leaver_flagged` in the previous 90 days, what fraction of all checked contacts that represents (expressed as % / month)
- **Apollo credit efficiency:** (writes that changed CRM state) / (credits consumed) over the previous month
- **Backlog:** count of contacts with `enrichment_name_status = not_checked` or `enrichment_employment_status = not_checked`

These replace industry-generic claims ("2.5%/month decay") with numbers grounded in our actual CRM.
