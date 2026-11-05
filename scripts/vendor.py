#!/usr/bin/env python3
"""Vendor public skills from GitHub into skills/<group>/ at the pinned ref in sources.json.

Usage:
  python3 scripts/vendor.py              # re-vendor every public source
  python3 scripts/vendor.py hard-half    # one source
  python3 scripts/vendor.py --bump X     # move source X to upstream HEAD, then vendor

Every run rewrites skills.lock.json (path, ref, content hash per skill), so a PR
that updates a public skill shows exactly what changed upstream.
Stdlib only; needs git on PATH.
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources.json"
LOCK = ROOT / "skills.lock.json"


def git(*args, cwd=None):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def head_sha(repo):
    return git("ls-remote", f"https://github.com/{repo}.git", "HEAD").split()[0]


def fetch(repo, ref, paths, dest):
    """Sparse, shallow checkout of just the paths we need at an exact commit."""
    git("init", "-q", str(dest))
    git("remote", "add", "origin", f"https://github.com/{repo}.git", cwd=dest)
    git("sparse-checkout", "set", "--no-cone", *paths, cwd=dest)
    git("fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", ref, cwd=dest)
    git("checkout", "-q", "FETCH_HEAD", cwd=dest)


def tree_hash(folder):
    h = hashlib.sha256()
    for f in sorted(p for p in folder.rglob("*") if p.is_file()):
        h.update(f.relative_to(folder).as_posix().encode())
        h.update(f.read_bytes())
    return h.hexdigest()[:16]


def apply_rewrites(folder, rewrites):
    for f in folder.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        new = text
        for pattern, repl in rewrites:
            new = re.sub(pattern, repl, new)
        if new != text:
            f.write_text(new, encoding="utf-8")


def vendor(src, lock):
    repo, ref, base = src["repo"], src["ref"], src.get("base", "").strip("/")
    group_dir = ROOT / "skills" / src["id"]
    rel = lambda p: f"{base}/{p}" if base else p
    paths = [rel(s) for s in src["skills"]] + list(src.get("extra_files", {})) + [src["license_file"]]
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        fetch(repo, ref, paths, tmp)
        if group_dir.exists():
            shutil.rmtree(group_dir)
        group_dir.mkdir(parents=True)
        shutil.copy(tmp / src["license_file"], group_dir / "LICENSE")
        for upstream, local in src.get("extra_files", {}).items():
            (group_dir / local).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(tmp / upstream, group_dir / local)
        rewrites = [(r["from"], r["to"]) for r in src.get("rewrites", [])]
        for s in src["skills"]:
            name = Path(s).name
            target = group_dir / name
            if not (tmp / rel(s) / "SKILL.md").exists():
                sys.exit(f"[{src['id']}] {rel(s)}/SKILL.md not found at {ref[:8]}")
            shutil.copytree(tmp / rel(s), target)
            apply_rewrites(target, rewrites)
            lock[f"{src['id']}/{name}"] = {
                "source": src["id"],
                "repo": repo,
                "path": rel(s),
                "ref": ref,
                "license": src["license"],
                "hash": tree_hash(target),
            }
    print(f"[{src['id']}] {len(src['skills'])} skills @ {ref[:8]} -> skills/{src['id']}/")


def main():
    args = sys.argv[1:]
    data = json.loads(SOURCES.read_text())
    bump = None
    if args[:1] == ["--bump"]:
        bump, args = args[1], [args[1]]
    lock = json.loads(LOCK.read_text()) if LOCK.exists() else {}
    for src in data["sources"]:
        if src.get("origin") != "public" or (args and src["id"] not in args):
            continue
        if bump == src["id"]:
            src["ref"] = head_sha(src["repo"])
        lock = {k: v for k, v in lock.items() if v.get("source") != src["id"]}
        vendor(src, lock)
    if bump:
        SOURCES.write_text(json.dumps(data, indent=2) + "\n")
    LOCK.write_text(json.dumps(dict(sorted(lock.items())), indent=2) + "\n")


if __name__ == "__main__":
    main()
