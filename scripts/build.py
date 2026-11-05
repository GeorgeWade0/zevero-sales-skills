#!/usr/bin/env python3
"""Validate every skill and regenerate CATALOG.md + the plugin manifests.

  python3 scripts/build.py          # validate and write generated files
  python3 scripts/build.py --check  # CI: fail if anything is invalid or generated files are stale

Errors (fail CI): missing/invalid frontmatter, name != folder, duplicate names,
skills on disk but not in sources.json (or the reverse), public skills edited by hand.
Warnings: links to sibling skills we didn't vendor, very long descriptions.
Stdlib only.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
VERSION_FILE = ROOT / "VERSION"


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out, key, buf = {}, None, []
    for line in m.group(1).splitlines():
        top = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if top and not line.startswith(" "):
            if key and buf:
                out[key] = " ".join(buf).strip()
            key, val = top.group(1), top.group(2).strip()
            buf = [] if val in (">", "|", ">-", "|-", "") else None
            if buf is None:
                out[key] = val.strip("\"'")
        elif buf is not None and key:
            buf.append(line.strip())
    if key and buf:
        out[key] = " ".join(buf).strip()
    return out


def tree_hash(folder):
    h = hashlib.sha256()
    for f in sorted(p for p in folder.rglob("*") if p.is_file()):
        h.update(f.relative_to(folder).as_posix().encode())
        h.update(f.read_bytes())
    return h.hexdigest()[:16]


def first_sentence(desc, limit=150):
    s = re.split(r"(?<=[.!?])\s", desc, maxsplit=1)[0]
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def main():
    check = "--check" in sys.argv
    sources = json.loads((ROOT / "sources.json").read_text())["sources"]
    lock = json.loads((ROOT / "skills.lock.json").read_text())
    errors, warnings, rows, seen = [], [], [], {}

    declared = {f"{s['id']}/{Path(k).name}": s for s in sources for k in s["skills"]}
    on_disk = {p.parent.relative_to(SKILLS).as_posix(): p for p in SKILLS.glob("*/*/SKILL.md")}

    for key in sorted(set(declared) - set(on_disk)):
        errors.append(f"{key}: listed in sources.json but skills/{key}/SKILL.md is missing")
    for key in sorted(set(on_disk) - set(declared)):
        errors.append(f"{key}: on disk but not listed in sources.json")

    for key, path in sorted(on_disk.items()):
        if key not in declared:
            continue
        src, folder = declared[key], path.parent
        fm = frontmatter(path)
        if not fm or not fm.get("name") or not fm.get("description"):
            errors.append(f"{key}: SKILL.md needs frontmatter with name and description")
            continue
        if fm["name"] != folder.name:
            errors.append(f"{key}: frontmatter name '{fm['name']}' must match folder '{folder.name}'")
        if fm["name"] in seen:
            errors.append(f"{key}: duplicate skill name, also in {seen[fm['name']]}")
        seen[fm["name"]] = key
        if len(fm["description"]) > 1024:
            warnings.append(f"{key}: description is {len(fm['description'])} chars (>1024 may be truncated)")
        if src["origin"] == "public":
            entry = lock.get(key)
            if not entry:
                errors.append(f"{key}: public skill missing from skills.lock.json - run scripts/vendor.py")
            elif entry["hash"] != tree_hash(folder):
                errors.append(f"{key}: edited by hand. Public skills are vendored - fix upstream or move it to skills/zevero/")
        for link in set(re.findall(r"\]\((\.\./[a-z0-9-]+)/SKILL\.md\)", path.read_text(encoding="utf-8"))):
            if not (folder / link).resolve().exists():
                warnings.append(f"{key}: links to {link.split('/')[-1]}, which isn't in this repo")
        rows.append((src, fm, key))

    # ---- generated files
    version = VERSION_FILE.read_text().strip()
    kits = json.loads((ROOT / "kits.json").read_text())
    key_of = {fm["name"]: key for _, fm, key in rows}
    kit_membership = {}

    def entry(name, display, description, skill_names):
        missing = [n for n in skill_names if n not in key_of]
        for n in missing:
            errors.append(f"kits.json: '{n}' in {name} is not a skill in this repo")
        keys = sorted({key_of[n] for n in skill_names if n in key_of})
        for k in keys:
            kit_membership.setdefault(k, []).append(name.replace("zevero-sales-", ""))
        return {
            "name": name,
            "displayName": display,
            "description": description,
            "version": version,
            "author": {"name": "Zevero Commercial team"},
            "source": "./",
            "strict": False,
            "skills": [f"./skills/{k}" for k in keys],
            "hooks": "./hooks/hooks.json",
        }

    plugins = [entry(k["name"], k["displayName"], k["description"], kits["core"] + k["skills"]) for k in kits["kits"]]
    a = kits["all"]
    plugins.append(entry(a["name"], a["displayName"], a["description"], [fm["name"] for _, fm, _ in rows]))
    marketplace = {
        "name": "zevero-sales",
        "owner": {"name": "Zevero"},
        "metadata": {"description": "Zevero's internal sales skills: one kit per role, plus everything.", "version": version},
        "plugins": plugins,
    }

    lines = [
        "# Skill catalog",
        "",
        "<!-- Generated by scripts/build.py from sources.json and each SKILL.md. Do not edit by hand. -->",
        "",
        f"**{len(rows)} skills** · plugin version {version} · "
        + " · ".join(f"{s['title'].split(' (')[0]}: {sum(1 for r in rows if r[0] is s)}" for s in sources),
        "",
    ]
    for s in sources:
        mine = [r for r in rows if r[0] is s]
        if not mine:
            continue
        lines += [f"## {s['title']}", ""]
        if s["origin"] == "public":
            lines += [
                f"Source: [{s['repo']}](https://github.com/{s['repo']}/tree/{s['ref']}/{s.get('base', '')}) "
                f"@ `{s['ref'][:8]}` · License: {s['license']}",
                "",
            ]
        else:
            lines += ["Owned and edited in this repo. Changes go through a PR.", ""]
        lines += ["| Skill | Kits | What it does |", "|---|---|---|"]
        for _, fm, key in sorted(mine, key=lambda r: r[1]["name"]):
            desc = first_sentence(fm["description"]).replace("|", "\\|")
            in_kits = [k for k in kit_membership.get(key, []) if k != "zevero-sales"]
            label = "all" if len(in_kits) == len(kits["kits"]) else ", ".join(in_kits) or "–"
            lines.append(f"| [`{fm['name']}`](skills/{key}/SKILL.md) | {label} | {desc} |")
        lines.append("")

    outputs = {
        ROOT / ".claude-plugin" / "marketplace.json": json.dumps(marketplace, indent=2) + "\n",
        ROOT / "CATALOG.md": "\n".join(lines),
    }
    for path, content in outputs.items():
        current = path.read_text() if path.exists() else None
        if current == content:
            continue
        if check:
            errors.append(f"{path.relative_to(ROOT)} is out of date - run python3 scripts/build.py and commit")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            print(f"wrote {path.relative_to(ROOT)}")

    dangling = [w for w in warnings if "isn't in this repo" in w]
    if dangling and "--verbose" not in sys.argv:
        warnings = [w for w in warnings if w not in dangling]
        warnings.append(f"{len(dangling)} links point at upstream skills we didn't vendor (harmless; --verbose to list)")
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"{len(rows)} skills, {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
