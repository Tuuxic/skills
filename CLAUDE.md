# Skill library

Each `skills/<name>/` folder is a skill, built from two upstream libraries plus my own. Read `PROVENANCE.md` before you change a skill's origin or merge upstream, and follow its "Updating from upstream" steps for any merge.

Use the `writing-for-agents` skill when you edit a skill or this file, and `unslop` for prose a human reads.

## Keep the tracking in step

A skill's change is complete when these files agree with it:

| Change | Also update |
|---|---|
| Edit a skill's text | Its `PROVENANCE.md` row: what changed, and the label. An `upstream` skill becomes `adapted`, and its row moves to the `adapted` rows. |
| Change what a skill does | Its `README.md` row. |
| Add a skill | `upstream.json` (`"source": "local"` and a `group` for my own), `README.md`, `PROVENANCE.md`, then run the build. |
| Change a `group` or `disable-model-invocation` | Run the build. |

Build: `python scripts/build_marketplace.py`. It owns `.claude-plugin/marketplace.json` and every `agents/openai.yaml`, so change those through the build.

## Checks

The repo has no test suite. Before you call a change done:

- `python scripts/sync_upstream.py report` shows `changed` for every skill labelled adapted or merged, and `identical` for every skill labelled upstream.
- The build leaves `git status` without unexpected changes.

## Gotchas

- `vendor/matt` and `vendor/pstack` hold untouched upstream copies. Only `sync_upstream.py import` writes to them.
- The skills loaded in a session come from the installed plugin, not this working tree. To see the current text of a skill, read it under `skills/`.
- Principles are user-only, so link to them by relative path to their `SKILL.md`, as `PROVENANCE.md` describes.
