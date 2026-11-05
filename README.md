# Zevero Sales Skills

Every sales skill the Zevero commercial team uses: our own playbooks plus vetted public skills for prospecting, discovery, deal reviews, proposals, negotiation and account management. Every skill knows Zevero (ICP, competitors, approved proof, pricing rules), and everything that goes out is checked for AI tells.

**→ [Browse the catalog](CATALOG.md)** (generated from the files in this repo; shows which kit each skill is in)

## Pick your kit

Install the kit for your role, not everything. Each kit includes the Zevero core: context, ai-tells, brand, presentations, EN↔JA translation, request-skill and skill-feedback.

| Kit | For | Install name |
|---|---|---|
| SDR | Prospecting, research, outbound, booking first meetings | `zevero-sales-sdr` |
| AE | Discovery through to signature (MEDDPICC), demos, value cases, proposals, negotiation | `zevero-sales-ae` |
| Account Manager | Account plans, health, QBRs, renewals, churn saves, expansion | `zevero-sales-am` |
| Leader | Pipeline, forecast, deal inspection, call coaching, win/loss, rep ramp | `zevero-sales-leader` |
| Everything | Every skill (power users only) | `zevero-sales` |

New to the team? Ask Claude to **"role-play a discovery call"** to practise, and see the [ramp path](skills/zevero/rep-ramp/references/ramp-path.md).

## Where the skills come from

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
claude plugin install zevero-sales-ae@zevero-sales
```

Swap `zevero-sales-ae` for your kit. Skills show up as `<kit>:<skill>`, e.g. `/zevero-sales-ae:discovery-brief`, and Claude also picks them automatically. Run `claude plugin update zevero-sales-ae` when a release is announced.

**Usage is logged** (which skill, who, when; never prompts or outputs) so we can see what's working. Details and opt-out: [docs/usage-tracking.md](docs/usage-tracking.md).

## Request or improve a skill

- **Easiest:** ask Claude "request a skill for …" or "the discovery-brief skill got this wrong". The `request-skill` skill drafts the request, shows it to you and files it here.
- **On GitHub:** go to [Issues → New issue](https://github.com/GeorgeWade0/zevero-sales-skills/issues/new/choose) and pick **Request a new skill**, **Improve an existing skill** or **Something's broken**.

Requests are reviewed weekly. You'll get a GitHub notification when yours is `approved` and again when it ships. After any skill output you can also just reply 👍 or "improve".

**Claude desktop / Cowork:** an org admin uploads the plugin once (Settings → Plugins → add from GitHub), and it's available to the whole team.

If you already have Anthropic's `sales` plugin installed, you can remove it. Its skills are included here.

Many skills work best with connectors: HubSpot, Gmail, Google Calendar, Slack, Granola and Apollo. See [`skills/anthropic-sales/CONNECTORS.md`](skills/anthropic-sales/CONNECTORS.md).

## How changes are tracked

- **Every change is a pull request.** CI validates every skill and checks that the catalog is up to date. CODEOWNERS sends Zevero-skill changes to the skill's owner for review.
- **[CHANGELOG.md](CHANGELOG.md)** gets a line for each change a rep would notice. `VERSION` is bumped on release, so people can see which version they're running.
- **Public skills are pinned.** [`sources.json`](sources.json) records the exact upstream commit for each public skill, and [`skills.lock.json`](skills.lock.json) records a content hash. CI fails if anyone hand-edits a vendored skill, so what we run always matches a known upstream version.
- `git log -- skills/zevero/<skill>` shows the full history of any skill.
- **Quality is tested.** [Evals](evals/README.md) check the guardrails (no invented prices or customers, no unreleased features, house style) with and without the plugin. Run them before changing Zevero skills.
- **Content stays current.** A [weekly refresh](docs/context-refresh.md) opens a PR updating the Zevero context from last week's deals, calls and Notion changes.
- **Releases are announced.** Bumping `VERSION` on `main` creates a GitHub release and posts the notes to Slack (set the `SLACK_WEBHOOK_URL` repo secret).

See [CONTRIBUTING.md](CONTRIBUTING.md) to add, edit or update a skill.

## Licensing

`skills/zevero/` is Zevero-internal and proprietary. Every other folder is third-party open source under its own `LICENSE` (MIT or Apache-2.0). See [NOTICE.md](NOTICE.md). Keep this repo **private**.
