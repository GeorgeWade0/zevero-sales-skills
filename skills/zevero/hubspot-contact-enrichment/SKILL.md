---
name: hubspot-contact-enrichment
description: >
  Enrich HubSpot contacts and companies with missing data using Apollo and email pattern parsing. Use this skill whenever someone says "enrich contacts", "enrich [company]", "fill in missing contact data", "clean up contacts", "find missing names", "who is [email]?", "look up [contact]", "enrich my CRM", "contact data cleanup", "fill in HubSpot gaps", or any variation involving enriching, cleaning, or completing CRM contact/company data. Also trigger for "Apollo lookup", "parse email names", "bulk enrich", or "data hygiene" in a CRM context. Works for individual lookups and bulk operations.
---

# HubSpot Contact & Company Enrichment

This skill fills in missing data on HubSpot contacts and companies using two complementary methods: Apollo enrichment (for rich external data) and email pattern parsing (for extracting names from email addresses at zero cost). The two approaches work best together — Apollo for Western contacts where it has strong coverage, and email parsing for Japanese and other contacts where Apollo has gaps.

## When to use which method

- **Apollo enrichment**: Best for Western contacts (.com, .co.uk, .org domains). Returns full name, job title, LinkedIn URL, company details, and more. Costs 1 credit per lookup. Coverage is weak for Japanese (.co.jp, .jp) contacts.
- **Email pattern parsing**: Best for Japanese corporate contacts where the email follows a `lastname.firstname@company.co.jp` pattern. Zero cost. Only extracts first/last names — no job title or other data.
- **Both together**: For bulk operations, try Apollo first on Western contacts, then fall back to email parsing for the rest.

## Workflow: Individual enrichment

When the user asks to enrich a specific contact or look someone up:

### Step 1: Find the contact in HubSpot

Search `contacts` by email, name, or company. Retrieve current properties to see what's missing (firstname, lastname, email, company, jobtitle, phone).

### Step 2: Try Apollo first

Use `apollo_people_match` with the contact's email and domain. If Apollo returns data, extract:
- First name, last name
- Job title
- LinkedIn URL
- Company name
- Phone (if available)

Present the Apollo findings to the user and propose updates.

### Step 3: Fall back to email parsing if Apollo misses

If Apollo returns no personal data, attempt to parse the name from the email address:

1. Take the local part (before @)
2. Split on `.`, `_`, and `-`
3. Filter out parts that are:
   - 2 characters or fewer (likely initials)
   - Numeric only
   - Common department/function words: info, admin, contact, sales, office, support, hr, team, hello, mail, web, sus, biz, general, inquiry, service, kanri, soumu, jinji, keiri, eigyo, kikaku, hanbai, koho, pro, sd, kv, aw, pc, ii, ap, hc
4. If 2+ valid name parts remain and both are alphabetic:
   - For Japanese domains (.co.jp, .jp, .or.jp, .ac.jp, .ne.jp): assume **lastname.firstname** order (Japanese corporate convention)
   - For Western domains (.com, .org, .co.uk, etc.): assume **firstname.lastname** order
5. Capitalise both parts

If parsing is ambiguous or low-confidence, tell the user rather than guessing.

### Step 4: Also enrich the company

If the contact is associated with a company, or you can identify one from the email domain, use `apollo_organizations_enrich` to fill in company details like industry, size, location, and description. This often succeeds even when the individual person lookup doesn't.

### Step 5: Update HubSpot

Show a confirmation table with current vs. proposed values. Only update after the user approves.

## Workflow: Bulk enrichment

When the user asks to enrich contacts in bulk (e.g. "clean up my contacts", "enrich contacts on deals"):

### Step 1: Identify the scope

Ask or infer what subset to target. Good starting points:
- Contacts tied to active deals missing key fields (`num_associated_deals > 0` + `firstname NOT_HAS_PROPERTY`)
- Contacts missing names entirely (`firstname NOT_HAS_PROPERTY` + `email HAS_PROPERTY`)
- Contacts at a specific company

Pull the full set using `search_crm_objects` with pagination.

### Step 2: Segment by domain type

Split the contacts into:
- **Western domains** (.com, .co.uk, .org, .io, etc.) — try Apollo first
- **Japanese domains** (.co.jp, .jp, .or.jp, .ac.jp, .ne.jp) — use email parsing

### Step 3: Run Apollo on Western contacts

Use `apollo_people_bulk_match` (up to 10 per call) for Western contacts. Track credits consumed. If the user hasn't set a credit limit, suggest a sensible cap (e.g. 10-20 per session) and confirm before proceeding.

Important: Always warn the user about Apollo credit costs before bulk lookups.

### Step 4: Run email parsing on the rest

Apply the email parsing logic from the individual workflow above to all remaining contacts. Be conservative — skip ambiguous parses rather than adding wrong data.

### Step 5: Present results before pushing

Show a summary:
- How many contacts found with missing data
- How many enriched via Apollo (with credit cost)
- How many enriched via email parsing (free)
- How many couldn't be enriched
- Sample of proposed updates

Get explicit approval before pushing changes.

### Step 6: Push updates in batches

Use `manage_crm_objects` to update contacts in batches of 10. Report progress and any failures.

### Step 7: Summary

Provide a final count of updates made, with links to a few example records the user can spot-check.

## Important notes

- **Always confirm before updating.** Never push data to HubSpot without showing the user what will change first.
- **Be conservative with parsing.** It's better to skip 10 ambiguous contacts than to add one wrong name. Wrong data in a CRM is worse than missing data.
- **Apollo credit awareness.** Always mention credit costs before Apollo lookups. For bulk operations, suggest a cap and confirm.
- **Japanese name order.** In HubSpot's Western-centric UI, "First Name" = given name and "Last Name" = family name. For Japanese contacts, this means the family name goes in "Last Name" even though it comes first in Japanese convention. The email parsing handles this correctly.
- **Don't enrich with outdated info.** If Apollo returns data that conflicts with what's already in HubSpot (e.g. different job title), flag it for the user rather than overwriting silently.
