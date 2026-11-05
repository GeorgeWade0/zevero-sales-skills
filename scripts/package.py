#!/usr/bin/env python3
"""Package each kit in the marketplace as a standalone plugin folder under dist/.

  python3 scripts/package.py            # all kits
  python3 scripts/package.py zevero-sales-ae
  python3 scripts/package.py --out ~/zevero-kits   # publish from outside the repo:
                                                   # dist/ is gitignored, and gitignored files aren't uploaded

Each dist/<kit>/ has .claude-plugin/plugin.json, hooks/, VERSION and only that kit's
skills (keeping the skills/<group>/<skill> layout, so hook paths and relative links work).
Upload these to the Claude org library; reps then install from the Claude app.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"


def main():
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    args = sys.argv[1:]
    global DIST
    if "--out" in args:
        i = args.index("--out")
        DIST = Path(args[i + 1]).expanduser().resolve()
        del args[i : i + 2]
    wanted = set(args)
    for p in market["plugins"]:
        if wanted and p["name"] not in wanted:
            continue
        out = DIST / p["name"]
        if out.exists():
            shutil.rmtree(out)
        (out / ".claude-plugin").mkdir(parents=True)
        shutil.copytree(ROOT / "hooks", out / "hooks")
        shutil.copy(ROOT / "VERSION", out / "VERSION")
        groups = set()
        for s in p["skills"]:
            rel = Path(s.removeprefix("./") if hasattr(s, "removeprefix") else s[2:])
            shutil.copytree(ROOT / rel, out / rel)
            groups.add(rel.parts[1])
        for g in groups:  # licence, shared files and notices for each source group
            for extra in ("LICENSE", "_shared", "CONNECTORS.md"):
                src = ROOT / "skills" / g / extra
                if src.is_dir():
                    shutil.copytree(src, out / "skills" / g / extra)
                elif src.exists():
                    shutil.copy(src, out / "skills" / g / extra)
        shutil.copy(ROOT / "NOTICE.md", out / "NOTICE.md")
        manifest = {k: p[k] for k in ("name", "displayName", "description", "version", "author", "skills")}
        manifest["hooks"] = "./hooks/hooks.json"
        (out / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n")
        for junk in out.rglob(".DS_Store"):
            junk.unlink()
        n = sum(1 for _ in out.rglob("SKILL.md"))
        size = sum(f.stat().st_size for f in out.rglob("*") if f.is_file()) // 1024
        print(f"{p['name']}: {n} skills, {size} KB -> {out}")


if __name__ == "__main__":
    main()
