# Changelog

One line per change a rep would notice. Newest first. Format: `- [skill] what changed (@who)`.

## Unreleased

- [zevero-sales-context] Weekly refresh: unreleased PCF tool, supplier survey and free-format upload added to don't-promise list; EPD/grant buying trigger; Greenly parent-group loss and Planet Mark co-existence notes; incumbents named on calls (Workiva, Deepki, Brownlow Hub, Mondra angle); supplier engagement added as a feature gap; YCH case study marked unpublished (@context-bot)
- [hubspot-contact-name-cleanup] New: weekly clean-up that fills missing names, company and job title on contacts the HubSpot Sales extension auto-creates, using the email signatures on the record, and fixes romaji or junk last names (@GeorgeWade0)
- [hubspot-contact-name-cleanup] Shared inboxes now get a readable name ("環境政策課 ご担当者", "ESG Compliance") instead of showing the email address; placeholder names like "ご担当者" are tidied into that format (@GeorgeWade0)
- [hubspot-database-review] New: monthly review of all HubSpot contacts that lists removal candidates with reasons in a Google Sheet and recommends the top three fixes (@GeorgeWade0)
- Fix: kits failed to load in Claude Code ("hooks: the file-path and array forms are not yet supported in a marketplace entry"). Marketplace entries no longer set `hooks`; `hooks/hooks.json` is picked up automatically (@GeorgeWade0)
- Role kits published to the Zevero Claude org library: reps install with one click, no GitHub needed (@GeorgeWade0)
- [request-skill] Sends the request to George on Slack when the rep has no GitHub access (@GeorgeWade0)

## 0.2.0 (2026-11-05)

- Role kits: install `zevero-sales-sdr`, `-ae`, `-am` or `-leader` instead of everything (@GeorgeWade0)
- [zevero-sales-context] New: Zevero ICP, buying committee, competitors and landmine questions, approved proof, regulations, pricing rules and MEDDPICC, loaded automatically for every sales task (@GeorgeWade0)
- [ai-tells] Now runs automatically on every customer-facing draft (@GeorgeWade0)
- [zevero-brand] [zevero-presentation] [en-ja-translator] Added, so PDFs and decks come out on-brand and Japanese uses approved terms (@GeorgeWade0)
- [buyer-roleplay] New: practise discovery, objections and Japan meetings against realistic Zevero buyers, with scored debriefs and certification (@GeorgeWade0)
- [rep-ramp] New: 8-week ramp path and certification tracking for new reps (@GeorgeWade0)
- [skill-feedback] New: reply 👍 or "improve" after any skill output (@GeorgeWade0)
- Usage logging (skill, rep, time; opt-out available), guardrail evals, release notes to Slack (@GeorgeWade0)
- [request-skill] New: ask Claude to request or improve a skill and it files a GitHub issue for you (@GeorgeWade0)
- Skill request, improvement and problem forms on GitHub Issues (@GeorgeWade0)

## 0.1.0 (2026-11-05)

- Initial library: 104 skills.
  - 6 Zevero originals.
  - 36 from Anthropic's sales plugin.
  - 39 sales, account and deal skills from The Hard Half.
  - 7 from marketingskills.
  - 4 from Apollo.
  - 12 vetted community skills: MEDDPICC scorecard, sales call review, deal red flags, deal value calculator, concession planner, champion mapping, pipeline coverage, discovery questions, RFP responder, enterprise account planning, LinkedIn outreach, competitive POC plan.
- Every public skill is pinned to an upstream commit and checked by CI.
