"""Import upstream skill libraries onto vendor branches and report local changes.

  python scripts/sync_upstream.py import matt            # newest upstream onto vendor/matt
  python scripts/sync_upstream.py import pstack --at SHA # a specific upstream commit
  python scripts/sync_upstream.py report                 # local vs upstream, per skill

`import` only touches the vendor branch. Merge it yourself: git merge vendor/<source>.
"""

import argparse
import fnmatch
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = json.loads((ROOT / "upstream.json").read_text(encoding="utf8"))


def git(*args, cwd=ROOT, check=True):
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed:\n{result.stderr}")
    return result


def branch_exists(branch):
    return git("rev-parse", "--verify", "--quiet", branch, check=False).returncode == 0


def fetch_upstream(source, at, into):
    git("init", "-q", cwd=into)
    git("remote", "add", "origin", source["repo"], cwd=into)
    git("fetch", "-q", "--depth", "1", "origin", at or source["ref"], cwd=into)
    git("-c", "core.longpaths=true", "checkout", "-q", "FETCH_HEAD", "--", source["root"], cwd=into)
    return git("rev-parse", "FETCH_HEAD", cwd=into).stdout.strip()


def upstream_skill_paths(root):
    return sorted(p.parent.relative_to(root).as_posix() for p in root.rglob("SKILL.md"))


def tracked(name):
    return {n: s for n, s in MANIFEST["skills"].items() if s["source"] == name}


def import_source(name, at):
    source = MANIFEST["sources"][name]
    branch = f"vendor/{name}"
    with tempfile.TemporaryDirectory(prefix=f"upstream-{name}-") as tmp, \
         tempfile.TemporaryDirectory(prefix=f"vendor-{name}-") as wt_parent:
        sha = fetch_upstream(source, at, tmp)
        upstream_root = Path(tmp) / source["root"]

        worktree = Path(wt_parent) / "wt"
        if branch_exists(branch):
            git("worktree", "add", "-q", str(worktree), branch)
        else:
            first_commit = git("rev-list", "--max-parents=0", "HEAD").stdout.split()[0]
            git("worktree", "add", "-q", "-b", branch, str(worktree), first_commit)

        try:
            missing = []
            for skill, entry in tracked(name).items():
                src = upstream_root / entry["path"]
                dest = worktree / "skills" / skill
                shutil.rmtree(dest, ignore_errors=True)
                if not src.is_dir():
                    missing.append(f"{skill} ({entry['path']})")
                    continue
                shutil.copytree(src, dest, ignore=shutil.ignore_patterns(*source["exclude"]))

            git("add", "-A", "skills", cwd=worktree)
            if git("diff", "--cached", "--quiet", cwd=worktree, check=False).returncode == 0:
                print(f"{branch}: already at upstream {sha[:12]}, nothing changed.")
            else:
                stat = git("diff", "--cached", "--stat", cwd=worktree).stdout
                git("commit", "-q", "-m", f"Import {name} upstream at {sha[:12]}",
                    "-m", f"{source['repo']} @ {sha}", cwd=worktree)
                print(f"{branch}: imported upstream {sha[:12]}.\n{stat}")
                print(f"Next: git merge {branch}")
        finally:
            git("worktree", "remove", "--force", str(worktree))

        known = {e["path"] for e in tracked(name).values()}
        patterns = MANIFEST["left_out"].get(name, [])
        new = [p for p in upstream_skill_paths(upstream_root)
               if p not in known and not any(fnmatch.fnmatch(p, pat) for pat in patterns)]
        if new:
            print("New upstream skills (neither tracked nor in left_out):\n  " + "\n  ".join(new))
        if missing:
            print("Tracked skills gone from upstream (removed on the vendor branch):\n  " + "\n  ".join(missing))
        also = [f"{e['also']} -> {n}" for n, e in MANIFEST["skills"].items()
                if e.get("also", "").startswith(f"{name}:")]
        if also:
            print("Ideas merged from these are not tracked; check upstream by hand:\n  " + "\n  ".join(also))


def report():
    for name in MANIFEST["sources"]:
        branch = f"vendor/{name}"
        if not branch_exists(branch):
            print(f"{branch}: missing. Run: python scripts/sync_upstream.py import {name}")
            continue
        last = git("log", "-1", "--format=%s (%cs)", branch).stdout.strip()
        merged = git("merge-base", "--is-ancestor", branch, "HEAD", check=False).returncode == 0
        print(f"\n{branch}: {last}{'' if merged else '  <- not merged yet'}")
        for skill in tracked(name):
            changed = git("diff", "--quiet", branch, "--", f"skills/{skill}", check=False).returncode != 0
            print(f"  {'changed  ' if changed else 'identical'}  {skill}")
    local = [n for n, s in MANIFEST["skills"].items() if s["source"] == "local"]
    print("\nlocal (own text): " + ", ".join(local))
    print("\nExact changes for one skill: git diff vendor/<source> -- skills/<skill>")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    imp = sub.add_parser("import")
    imp.add_argument("source", choices=MANIFEST["sources"])
    imp.add_argument("--at", help="upstream commit to import instead of the branch head")
    sub.add_parser("report")
    args = parser.parse_args()
    if args.command == "import":
        import_source(args.source, args.at)
    else:
        report()


if __name__ == "__main__":
    main()
