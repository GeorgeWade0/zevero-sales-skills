---
name: hubspot-database-review
description: Monthly review of every HubSpot contact. Tidies what is safe to fix, lists contacts George should remove or archive with the reason for each, and recommends what to fix next. Use when asked to audit or review HubSpot, clean up the whole database, find contacts to delete, or check CRM data quality.
---

# HubSpot database review (monthly)

## What it does

Checks all contacts against a fixed list of problems, then:

1. Fixes the safe things itself (names, under the rules in `hubspot-contact-name-cleanup`).
2. Lists contacts to remove or archive, each with a reason, in a Google Sheet for George to tick.
3. Sends George a short Slack summary with the numbers, the change since last month and the top three things to fix.

It never deletes contacts, changes lifecycle stage, changes owners or changes marketing status. George decides and deletes by hand (or asks Claude to do it in Chrome).

## Baseline (17 Nov 2026)

| Check | Contacts |
|---|---|
| All contacts | 37,317 |
| Lifecycle stage Lead | 30,672 |
| Lead with no sales activity ever | 17,949 |
| No activity at all and created over a year ago | 3,751 |
| Hard bounced | 697 |
| Unsubscribed from all email | 646 |
| No company association | 1,007 |
| No job title | 4,811 |
| No email address | 213 |
| No owner | 23 |
| Marketing contacts (billed) | 4,665 |

Compare each run against the last run's numbers in the Sheet.

## Step 1. Count

Use `query_crm_data` for each check (one `COUNT(*)` query each), plus `GROUP BY lifecyclestage` and `GROUP BY hs_object_source_label`. Property names:

- Hard bounce: `hs_email_hard_bounce_reason_enum IS NOT NULL`
- Unsubscribed: `hs_email_optout = 'true'`
- Never contacted: `notes_last_contacted IS NULL AND hs_last_sales_activity_timestamp IS NULL`
- No company: `associations.COMPANY IS NULL`
- Marketing contact: `hs_marketable_status = 'true'`

## Step 2. Fix what is safe

Run `hubspot-contact-name-cleanup` over all contacts with no first and last name (not just the last 8 days). Report how many it named.

## Step 3. Removal and archive candidates

Pull the records with `search_crm_objects` (limit 200, page through, save to JSON before judging). Give each candidate exactly one reason. Never include a contact with an open deal or lifecycle stage Opportunity, User - Trial or User - Customer.

| Reason | Rule | Suggested action |
|---|---|---|
| Hard bounced | hard bounce set, no activity in 6 months | Delete |
| No email, no phone | `email` and `phone` both empty, no deal | Delete |
| Zevero's own address | @zevero.earth, @zevero.co, zevero.onmicrosoft.com | Delete |
| Relay or system address | reply., noreply, no-reply, mailer-daemon, notifications@, calendar-notification | Delete |
| Test address | mail-tester, mailgenius, test@, example@ | Delete |
| Job applicant or student | emails about "application", "interview", "intern", "CV"; st.*.ac.jp | Delete |
| Duplicate | same email in different case, or same name and company with two emails | Merge (name both ids) |
| Unsubscribed and cold | opted out, no sales activity in 12 months, not a customer | Delete or set to non-marketing |
| Never contacted, old | Lead, created over 12 months ago, never contacted, not a marketing contact | Set lifecycle to Other, or delete |
| Disqualified and cold | Disqualified, no activity in 12 months | Delete |

Sample before you list: if a reason catches more than 500 contacts, check 10 by hand and say in the Sheet how many of the 10 were right.

## Step 4. Write the Sheet

One Google Sheet, "HubSpot review YYYY-MM", one row per candidate: Reason, Suggested action, Name, Email, Company, Owner, Created, Last activity, HubSpot link, and an empty "George: OK to remove?" column. The first rows hold this run's counts next to last run's.

## Step 5. Recommendations

Pick the three changes that would most improve the data, using this month's numbers. Say what to change and in which HubSpot setting, in one or two sentences each. Things to look at:

- Contacts auto-created as Lead from logged emails (Sales extension, `EXTENSION`) and from integrations (`INTEGRATION`): most Leads are never contacted. Suggest setting new auto-created contacts to Other or Subscriber, and only Lead once a rep qualifies them.
- Marketing contacts HubSpot bills for who are unsubscribed, bounced or cold: set them to non-marketing.
- Contacts with no company: turn on automatic company association by domain, or fix the integration that creates them.
- Missing job titles on deal contacts: run `weekly-contact-enrichment`.
- Owners who left Zevero still owning contacts.

Write plainly. No labels like "quick wins" or "best practice".

## Step 6. Report to George in Slack

DM George Wade. Plain text, no tables:

- Contacts total and change since last month
- Names fixed this run
- Removal candidates by reason, with the Sheet link
- The three recommendations
- Anything that failed

## Running it

Monthly, first Monday at 9am, as the scheduled task `hubspot-database-review`. On demand: "run the HubSpot database review".
