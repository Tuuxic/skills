"""Generate .claude-plugin/marketplace.json from the groups in upstream.json.

  python scripts/build_marketplace.py

Each group becomes one installable plugin. Rerun after adding a skill or changing its group.
Also prints where a skill names a skill from another group, so you know which groups work best together.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = json.loads((ROOT / "upstream.json").read_text(encoding="utf8"))
VERSION = "0.2.0"


def main():
    skills = MANIFEST["skills"]
    plugins = []
    for group, description in MANIFEST["groups"].items():
        members = sorted(n for n, e in skills.items() if e["group"] == group)
        plugins.append({
            "name": group,
            "description": description,
            "version": VERSION,
            "author": {"name": "Tuuxic"},
            "source": "./",
            "strict": False,
            "skills": [f"./skills/{n}" for n in members],
        })
    marketplace = {
        "name": "tuuxic",
        "owner": {"name": "Tuuxic"},
        "description": "Tuuxic's skill library, built on Matt Pocock's skills.",
        "plugins": plugins,
    }
    out = ROOT / ".claude-plugin" / "marketplace.json"
    out.write_text(json.dumps(marketplace, indent=2) + "\n", encoding="utf8", newline="\n")
    print(f"Wrote {out.relative_to(ROOT)}: " + ", ".join(f"{p['name']} ({len(p['skills'])})" for p in plugins))

    name_pattern = re.compile(r"`(" + "|".join(map(re.escape, sorted(skills, key=len, reverse=True))) + r")`")
    for name, entry in sorted(skills.items()):
        text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf8")
        others = sorted({m for m in name_pattern.findall(text) if skills[m]["group"] != entry["group"]})
        if others:
            print(f"  {name} ({entry['group']}) uses: " + ", ".join(f"{o} ({skills[o]['group']})" for o in others))


if __name__ == "__main__":
    main()
