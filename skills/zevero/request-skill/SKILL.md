---
name: request-skill
description: File a request to add a new sales skill, or improve an existing one, in the Zevero sales skills library. Use when the user says "request a skill", "I wish Claude could…", "can we add a skill for…", "this skill should also…", "suggest a skill", "the [skill] skill got it wrong", or "log feedback on a skill".
---

# Request a skill

Turn a rep's idea or complaint into a well-formed GitHub issue on `GeorgeWade0/zevero-sales-skills`, so it can be triaged and built.

## 1. Check it doesn't already exist

Read the skill list available to you (skills named `zevero-sales:*`). If an existing skill already covers the request, tell the user which one and how to trigger it, and stop unless they say it falls short. If it falls short, file an **improvement** instead of a new skill.

## 2. Gather the details

Ask only for what's missing, in one message. Don't run an interview.

**New skill** needs:
- **job**: what Claude should do, as one sentence starting with a verb
- **when**: the moment or deal stage it's used, and what they'd type
- **today**: how they do it now and how long it takes
- **good**: what a great result looks like (optional)
- **sources**: HubSpot, Gmail/Calendar, Granola, Apollo, Slack, Zevero docs (optional)
- **frequency**: Daily, Weekly, Every deal or Occasionally
- **public**: a link to a public skill that does it (optional)

**Improvement** needs:
- **skill**: which skill
- **what**: what they asked, what they got, and what they expected
- **fix**: their suggested fix (optional)

Strip customer names, contact details, pricing and anything confidential before filing. Replace them with placeholders like `[Prospect]`.

## 3. Show the draft and confirm

Show the title and body exactly as they'll be filed, and ask the user to confirm. Never file without a yes.

- Title for a new skill: `[Skill request] <job>`
- Title for an improvement: `[Improve] <skill>: <short problem>`
- Body: one `### <Question>` heading per field, using the question wording from step 2, with the answer underneath.

## 4. File it

If the `gh` command is available and logged in (`gh auth status` succeeds), run:

```bash
gh issue create -R GeorgeWade0/zevero-sales-skills --title "<title>" --label "skill-request,triage" --body-file <tmpfile>
```

For an improvement, use `--label "skill-improvement,triage"`. Write the body to a temp file rather than passing it inline. Return the issue URL to the user.

Most reps install the kits from the Claude app and have no GitHub access. If `gh` isn't installed, isn't logged in, or can't see the repo (`gh repo view GeorgeWade0/zevero-sales-skills` fails), send the request to George on Slack instead:

- **If the Slack connector is available:** send the confirmed title and body as a DM to George Wade (Slack user ID `U01SRM118T1`). Start the message with `Skill request from <user's name>:`. This uses the same yes from step 3; don't ask again.
- **Otherwise:** give the user the message to paste to George in Slack or email.

George files it on GitHub, so it's still tracked.

## 5. Close out

Tell them in one line what happens next: requests are reviewed weekly. They'll get a GitHub notification when the issue is labelled `approved` or a pull request links to it.
