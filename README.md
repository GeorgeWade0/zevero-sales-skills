# Zevero Sales Skills

Every sales skill the Zevero commercial team uses, in one Claude plugin: our own playbooks plus vetted public skills for prospecting, discovery, deal reviews, proposals, negotiation and account management.

**→ [Browse the catalog](CATALOG.md)** (104 skills, generated from the files in this repo)

| Group | Folder | What's in it |
|---|---|---|
| Zevero originals | `skills/zevero/` | Our own skills: discovery briefs, HubSpot updates and enrichment, value follow-up PDFs, Commercial Pulse |
| Anthropic sales | `skills/anthropic-sales/` | Call prep, call summaries, deal reviews, pipeline, forecast, outreach |
| The Hard Half | `skills/hard-half/` | Discovery calls, objection maps, champions, economic buyers, negotiation, proposals, renewals |
| mbfinotti | `skills/mbfinotti/` | MEDDPICC scorecard, call review, deal red flags, ROI calculator, concession planner |
| marketingskills | `skills/marketingskills/` | Cold email, prospecting, sales enablement, RevOps, pricing, competitors |
| Apollo | `skills/apollo/` | Prospecting, enrichment and sequences (needs the Apollo connector) |
| Others | `skills/rfp/`, `skills/lmty/`, `skills/awesome-copilot/`, `skills/craig-hewitt/` | RFP responses, competitive POCs, enterprise account planning, LinkedIn outreach |

## Install

You need an invite to this private repo first. Ask George, and accept the email from GitHub.

**One-time setup:** install Claude Code and the GitHub CLI, then log in to GitHub:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

```bash
brew install gh && gh auth login --web --git-protocol https && gh auth setup-git
```

**Install the plugin** (open a new terminal tab first):

```bash
claude plugin marketplace add GeorgeWade0/zevero-sales-skills
```

```bash
claude plugin install zevero-sales@zevero-sales
```

Skills then show up as `zevero-sales:<skill>`, e.g. `/zevero-sales:discovery-brief`. Run `claude plugin update zevero-sales` to get new skills when they're released.

## Request or improve a skill

- **Easiest:** ask Claude "request a skill for …" or "the discovery-brief skill got this wrong". The `request-skill` skill drafts the request, shows it to you and files it here.
- **On GitHub:** go to [Issues → New issue](https://github.com/GeorgeWade0/zevero-sales-skills/issues/new/choose) and pick **Request a new skill**, **Improve an existing skill** or **Something's broken**.

Requests are reviewed weekly. You'll get a GitHub notification when yours is `approved` and again when it ships.

**Claude desktop / Cowork:** an org admin uploads the plugin once (Settings → Plugins → add from GitHub), and it's available to the whole team.

If you already have Anthropic's `sales` plugin installed, you can remove it. Its skills are included here.

Many skills work best with connectors: HubSpot, Gmail, Google Calendar, Slack, Granola and Apollo. See [`skills/anthropic-sales/CONNECTORS.md`](skills/anthropic-sales/CONNECTORS.md).

## How changes are tracked

- **Every change is a pull request.** CI validates every skill and checks that the catalog is up to date. CODEOWNERS sends Zevero-skill changes to the skill's owner for review.
- **[CHANGELOG.md](CHANGELOG.md)** gets a line for each change a rep would notice. `VERSION` is bumped on release, so people can see which version they're running.
- **Public skills are pinned.** [`sources.json`](sources.json) records the exact upstream commit for each public skill, and [`skills.lock.json`](skills.lock.json) records a content hash. CI fails if anyone hand-edits a vendored skill, so what we run always matches a known upstream version.
- `git log -- skills/zevero/<skill>` shows the full history of any skill.

See [CONTRIBUTING.md](CONTRIBUTING.md) to add, edit or update a skill.

## Licensing

`skills/zevero/` is Zevero-internal and proprietary. Every other folder is third-party open source under its own `LICENSE` (MIT or Apache-2.0). See [NOTICE.md](NOTICE.md). Keep this repo **private**.
