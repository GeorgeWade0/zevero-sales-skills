# Contributing

Every change goes through a pull request, never straight to `main`. All the scripts are standard-library Python 3.9+ and git.

## Triage requests (weekly)

Go through issues labelled `triage`:

1. **Already covered?** Reply with the skill name and close.
2. **Worth building?** Swap `triage` for `approved` and assign an owner. If a public skill fits, vendor it (see below) instead of writing one.
3. **Not going ahead?** Label `wontfix`, say why, and close.

Link the PR that ships it with `Closes #<issue>`, so the requester is notified when it merges.

## Edit a Zevero skill

1. Branch, then edit `skills/zevero/<skill>/SKILL.md` and any files in its `references/` folder.
2. Run `python3 scripts/build.py` to validate and regenerate the catalog.
3. Add a line to `CHANGELOG.md` under **Unreleased**.
4. Open a PR. The skill's owner in `.github/CODEOWNERS` reviews it.

## Add a new Zevero skill

1. Create `skills/zevero/<name>/SKILL.md`. Its frontmatter needs `name: <name>` matching the folder, plus a `description` that says what the skill does and when to use it.
2. Add `<name>` to the `zevero` entry in `sources.json`.
3. Add an owner line to `.github/CODEOWNERS`.
4. Run `python3 scripts/build.py`, add a CHANGELOG line, and open a PR.

## Add a public skill

Only use MIT, Apache-2.0, BSD or CC-BY licensed skills. Read the SKILL.md before adding it; reject thin prompt stubs.

1. Add the skill to an existing source in `sources.json`, or add a new source with `repo`, `ref` (a full commit SHA), `license`, `license_file`, `base` and `skills`.
2. Run `python3 scripts/vendor.py <source-id>`, then `python3 scripts/build.py`.
3. Add a CHANGELOG line and open a PR.

## Update public skills to upstream

```bash
python3 scripts/vendor.py --bump hard-half
```

```bash
python3 scripts/build.py
```

The PR diff shows exactly what changed upstream. Review it like any other change.

## Don't hand-edit vendored skills

CI fails if a file under a public group no longer matches `skills.lock.json`. If you want to change a public skill:

- **Small fix:** send it upstream, then bump the ref.
- **Zevero version:** copy the folder into `skills/zevero/` under a new name (e.g. `zevero-discovery-call`), list it under `zevero` in `sources.json`, and edit it there.

## Releasing

When enough has merged:

1. Bump `VERSION` and move the **Unreleased** CHANGELOG entries under the new version.
2. Run `python3 scripts/build.py`, then merge. This creates the GitHub release and posts to Slack.
3. Publish to the Claude org library, which is where reps install from:
   - Run `python3 scripts/package.py --out ~/zevero-kits`. Package outside the repo, because `dist/` is gitignored and gitignored files aren't uploaded.
   - In Claude, ask to "publish ~/zevero-kits/<kit> to the org library" for each changed kit. Replace the existing version when asked.
