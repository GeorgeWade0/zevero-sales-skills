# Weekly context refresh

A scheduled Claude task keeps `zevero-sales-context` current, so battlecards, objections and proof don't go stale. Every Monday at 08:00 it:

1. Reads the last 7 days of data, read-only:
   - Closed-won and closed-lost deals in HubSpot (aggregates only)
   - Granola call notes
   - Notion pages that changed
2. Opens a PR updating `references/context.md`, with a source for every change and a "Needs George" list. It never merges.
3. Opens an issue for any new objection or competitor that came up 3+ times this week and isn't covered yet.

It runs on George's Mac through the Claude desktop app's scheduled tasks, because that's where the HubSpot, Granola and Notion connectors are. If the app is closed when it's due, it runs on the next launch.

## Set it up

In the Claude desktop app, ask: **"Create a weekly scheduled task from docs/context-refresh.md"**, and approve it. Or create it by hand under Scheduled tasks: Monday 08:00, using the prompt below.

## Prompt

```text
You keep the Zevero sales skills library current. Repo: ~/code/sales-skills (GitHub: GeorgeWade0/zevero-sales-skills, use /opt/homebrew/bin/gh). The file that matters is skills/zevero/zevero-sales-context/references/context.md, the facts every sales skill relies on (ICP, personas, competitors and landmine questions, proof/approved customers, regulations, pricing rules, objections, loss reasons, open questions).

Each run:
1. cd ~/code/sales-skills && git switch main && git pull. Read context.md fully.
2. Gather what changed in the last 7 days. READ ONLY in every tool: never write, send or comment.
   - HubSpot (load its tools with ToolSearch; call get_user_details first): deals closed won/lost in the last 7 days across UK, JP and Singapore pipelines. Aggregates only: counts, industries, competitors named in closed-lost reasons, new loss-reason themes, new feature gaps. Do not copy contact or prospect names.
   - Granola (search_meetings / search_transcripts, last 7 days): new competitor mentions, objections, buying triggers, regulations prospects raised. Patterns only, no personal details.
   - Notion (notion-search): pages edited in the last 7 days about battle cards, case studies/customer approvals, pricing, positioning, Trust Centre/security, ICP, product releases.
3. Decide which facts in context.md are now wrong, missing or stale. Only propose a change a source supports; tag it like the rest of the file (N:/D:/HS/G). Resolve an "Open questions" item only if a source clearly answers it. Never add prices or customer names that aren't explicitly approved in a source.
4. If there are changes: create branch context-refresh-YYYY-MM-DD, edit context.md (update "Last reviewed"), add a CHANGELOG.md line under "## Unreleased" like "- [zevero-sales-context] Weekly refresh: <summary> (@context-bot)", run python3 scripts/build.py (must end with 0 errors), commit, push, and open a PR to main titled "Weekly context refresh YYYY-MM-DD". PR body: one bullet per change with its source, then a "Needs George" list for anything ambiguous or conflicting. Never merge.
5. For each new objection or competitor seen 3+ times this week with no coverage in context.md, open one GitHub issue labelled skill-improvement,triage titled "[Improve] zevero-sales-context: <topic>", unless an open issue already covers it.
6. If nothing changed, create no branch or PR.
Finish with a 3-line summary: PR link (or "no changes"), issues opened, and anything that needs George.
```
