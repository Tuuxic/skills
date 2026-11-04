# Provenance

Where every skill comes from, what I changed, and how to pull in upstream updates.

Source: [mattpocock/skills](https://github.com/mattpocock/skills), imported at `4ae2317` (2026-11-05).

`upstream.json` maps each skill to its upstream path. The untouched upstream copy lives on the branch `vendor/matt`.

## Labels

- **upstream**: byte-identical to the source.
- **adapted**: from the source, with my edits. The edits are listed below.
- **own**: written for this library, no upstream.

The table states intent. For the exact lines, run `git diff vendor/matt -- skills/<skill>`. `python scripts/sync_upstream.py report` checks which skills currently differ from upstream.

## Skills

| Skill | Label | What I changed |
|---|---|---|
| Every Matt skill not listed below (26) | upstream | |
| `grilling` | adapted | A round is a question-tool popup of up to four questions, the most unblocking first, replacing the numbered list template, with a one-question plain message as the fallback. |
| `t-mode` | own | My full working style, written from my vault's conversation rules. The proof and writing rules are in my own words. Its `agents/openai.yaml` is hand-written. |
| `inbox-capture` | own | Written from my vault's `CLAUDE.md`, its templates, and one existing capture. Finds the vault per device (working directory, `SECOND_BRAIN_VAULT`, memory, or asks). |

Other files that are my own: `README.md`, `CLAUDE.md`, `PROVENANCE.md`, `personal/`, `upstream.json`, `scripts/`, and `.claude-plugin/`.

## Decisions

| Decision | Why |
|---|---|
| Build on Matt's skills, with pstack out for now | A fresh start from one paradigm instead of merging two. |
| Take all 27 stable skills | `ask-matt` stays accurate without edits, and skills he calls by name are always installed. User-invoked skills cost no context until typed. `in-progress` and `misc` stay out. |
| Start from his text, and bring edits back when a real session shows the need | I can adapt freely, but only `grilling`'s popups earned a place in the reset. His setup skill already covers a local or "Other" (Notion) tracker. |
| Keep the question-tool popups in `grilling` | Matt rejects these for his skills. I prefer them, and "Other" still takes a free-text answer. |
| One `t-skills` plugin, with `inbox-capture` apart in `t-obsidian` | His skills call each other across folders, so a partial install would break real steps. |
| Style in both `personal/CLAUDE.md` and `t-mode` | I work from several devices. `CLAUDE.md` is the main home, symlinked per device. `t-mode` is the fuller version that travels with the plugin. |
| Import his `agents/openai.yaml` | Keeps Codex working and the folders identical to upstream, so the build needs no generator. |

The state before this reset is the tag `pre-matt-reset`, including pstack, its clash decisions, and my merged skills.

## Updating from upstream

1. Import the new upstream onto its vendor branch. This doesn't touch the current branch:

   ```
   python scripts/sync_upstream.py import matt
   ```

   The output shows which files changed upstream. It also lists upstream skills that are new (neither tracked nor in `left_out`).
2. Read what upstream changed: `git show vendor/matt`.
3. Merge it: `git merge vendor/matt`. Skills labelled upstream update cleanly. For adapted skills, git applies the upstream change on top of my edits, and it stops with a conflict only where both sides changed the same lines. Resolve conflicts against the decisions above.
4. Push the branch so other devices get it: `git push origin vendor/matt`.
5. For each new upstream skill, either add it to `skills` in `upstream.json` and import again, or add it to `left_out`.
6. If an update changes what a skill does, update its row here and in `README.md`.

## Bringing pstack back

`vendor/pstack` stays on `origin`, imported at `4dd1d05`. To bring it back, restore its entry under `sources` in `upstream.json` (see the tag `pre-matt-reset`) and add an entry under `skills` for each skill you want. Then run `python scripts/sync_upstream.py import pstack` and `git merge vendor/pstack`. Add its license back to `THIRD_PARTY_NOTICES.md`.
