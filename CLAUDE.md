# Skill library

Each `skills/<name>/` folder is a skill: Matt Pocock's skills plus my own. Read `PROVENANCE.md` before you change a skill's origin or merge upstream, and follow its "Updating from upstream" steps for any merge.

Use the `writing-for-agents` skill when you edit a skill or this file, and the Writing rules in `skills/t-mode/SKILL.md` for prose a human reads.

## Keep the tracking in step

A skill's change is complete when these files agree with it:

| Change | Also update |
|---|---|
| Edit a skill's text | Its `PROVENANCE.md` row: what changed, and the label. An `upstream` skill becomes `adapted`, and it moves to the `adapted` rows. |
| Change what a skill does | Its `README.md` row. |
| Add a skill | `upstream.json` (`"source": "local"` and a `group` for my own), `README.md`, `PROVENANCE.md`, then run the build. |
| Change a `group` | Run the build. |
| Edit or add a skill | Raise `VERSION` in `scripts/build_marketplace.py`, then run the build. `/plugin upgrade` skips the new text until the version changes. |
| Change my working style | Both `personal/CLAUDE.md` (concise) and `skills/t-mode/SKILL.md` (full). |
| Make one of my own skills user-only | Set `disable-model-invocation: true` and hand-write its `agents/openai.yaml`, as `t-mode` does. |

Build: `python scripts/build_marketplace.py`. It owns `.claude-plugin/marketplace.json`, so change that file through the build.

## Checks

The repo has no test suite. Before you call a change done:

- `python scripts/sync_upstream.py report` shows `changed` for every skill labelled adapted, and `identical` for every skill labelled upstream.
- The build leaves `git status` without unexpected changes.

## Gotchas

- `vendor/matt` holds an untouched upstream copy. Only `sync_upstream.py import` writes to it. `vendor/pstack` is dormant: pstack is out for now, and `PROVENANCE.md` says how to bring it back.
- The skills loaded in a session come from the installed plugin, not this working tree. To see the current text of a skill, read it under `skills/`.
