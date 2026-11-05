# Usage tracking

The plugin logs **which skill was used, by whom, and when**, so we can see adoption, cut skills nobody uses, and check whether usage lines up with deal outcomes in HubSpot.

## What's logged

| Field | Example |
|---|---|
| timestamp | 2026-11-05 17:14 UTC |
| rep | Git email, e.g. `jane@zevero.earth` |
| kit | `zevero-sales-ae` |
| skill | `call-prep` |
| trigger | `auto` (Claude picked it) or `slash` (typed `/…`) |
| version | `0.2.0` |

Prompts, outputs, customer names and file contents are **never** logged. To opt out, set `ZEVERO_SKILLS_NO_TELEMETRY=1` in your shell.

## Switching it on (one-off, about 5 minutes, done by the repo owner)

1. Create a Google Sheet called **Zevero sales skills usage**.
2. Go to **Extensions → Apps Script**, replace the code with [`scripts/usage-sheet.gs`](../scripts/usage-sheet.gs), and save.
3. **Deploy → New deployment → Web app**. Set Execute as **Me** and Who has access **Anyone**, then authorise it.
4. Paste the web app URL as the only line of `hooks/usage-endpoint`, then commit and merge.
5. Reps get logging the next time they run `claude plugin update`.

The first event creates a `usage` tab (raw log) and a `summary` tab (top skills, active reps and weekly uses for the last 30 days).

While `hooks/usage-endpoint` is empty, logging is off and nothing is sent anywhere.
