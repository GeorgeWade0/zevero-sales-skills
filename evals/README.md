# Output-quality evals

Each folder is a test case: a realistic prompt (`prompt.md`) plus pass/fail criteria (`graders/criteria.md`). Most check the Zevero guardrails:

- no invented prices
- only approved customers cited
- no unreleased features promised
- no SOC 2 claims
- no CSRD hook for mid-market
- no urgency in Japan
- house style (no em dashes, word limits, no buzzwords)

`claude plugin eval` runs each case **with and without** the plugin and reports the score difference. That shows whether the skills make outputs better, not just different.

## Run them

One-off setup: run `claude` once and log in.

To test local changes, add this checkout as a marketplace and install the full plugin:

```bash
claude plugin marketplace add ./ && claude plugin install zevero-sales@zevero-sales
```

Then run the suite:

```bash
claude plugin eval zevero-sales@zevero-sales -j 3 --max-cost-usd 10
```

Run it before merging any change to `skills/zevero/` or `zevero-sales-context`, and paste the score table into the PR. A case that passed before and fails now blocks the merge.

## Add a case

- Run `claude plugin eval init --bare <name>`, then write the prompt and the criteria.
- Base it on something that went wrong for a rep. `skill-feedback` and `request-skill` issues are the best source.
- Good gold-standard outputs from real deals belong in `docs/examples/<skill>/`, anonymised. Turn them into criteria ("matches the structure of the example: …").
