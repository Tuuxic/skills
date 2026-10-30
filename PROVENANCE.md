# Provenance

Where every skill comes from, what I changed, and how to pull in upstream updates.

Sources:

- **matt**: [mattpocock/skills](https://github.com/mattpocock/skills), imported at `a496f55` (2026-10-29).
- **pstack**: [cursor/plugins `pstack/skills`](https://github.com/cursor/plugins/tree/main/pstack), by Lauren Tan (poteto), imported at `4dd1d05` (2026-10-29).

`upstream.json` maps each skill to its upstream path. The untouched upstream copies live on the branches `vendor/matt` and `vendor/pstack`.

## Labels

- **upstream**: byte-identical to the source.
- **adapted**: one source, with my edits. The edits are listed below.
- **merged**: one source as the base, plus ideas or text from the other library.
- **own**: written for this library, no upstream.

The table states intent. For the exact lines, run `git diff vendor/<source> -- skills/<skill>`. `python scripts/sync_upstream.py report` checks which skills currently differ from upstream.

## Skills

| Skill | Label | Base | Merged in | What I changed |
|---|---|---|---|---|
| `grilling` | upstream | matt | | |
| `domain-modeling` | upstream | matt | | |
| `codebase-design` | upstream | matt | | |
| `prototype` | upstream | matt | | |
| `teach` | upstream | matt | | |
| `writing-for-agents` | upstream | matt | | |
| `in-your-own-words` | upstream | pstack | | |
| `sharpen` | upstream | pstack | | |
| `grill-me` | adapted | matt | | "Call the Skill tool" became "use the `grilling` skill", so the wording works in any harness. |
| `grill-with-docs` | adapted | matt | | Same wording change, plus one clause on capturing terms as they settle. |
| `handoff` | adapted | matt | | Same wording change. |
| `code-review` | adapted | matt | | Points to `docs/agents/issue-tracker.md` and `/setup-project`. |
| `to-spec` | adapted | matt | | Tracker pointer, plus a `Status:` line instead of triage labels. |
| `to-tickets` | adapted | matt | | Tracker pointer, status instead of triage labels, and Notion named as another tracker. |
| `setup-project` | adapted, mostly own text | matt `setup-matt-pocock-skills` | | `SKILL.md` rewritten: local or "other" tracker, no triage labels, no GitHub or GitLab. The local tracker lost its wayfinder and triage parts and gained a status list and a "close" operation. `issue-tracker-other.md` is new (the Notion slot). The GitHub, GitLab, and triage-label files are deleted. |
| `implement` | merged | matt | pstack `principle-prove-it-works` | Adds working the ticket frontier in order, proving each ticket before calling it done, closing tickets in the tracker, and one commit per ticket. |
| `tdd` | merged | matt | pstack `tdd`, pstack `principle-test-behavior-not-implementation` | "What a good test is" now points to the principle. Added pstack's "prefer no new test over a bad test" and its red/green evidence report. |
| `diagnosing-bugs` | merged | matt | pstack `principle-attack-the-premise`, `principle-fix-root-causes` | Two added paragraphs that link the principles in the hypothesis and fix phases. |
| `wait-what` | merged | matt | pstack `bro` | Rewritten as a list: context first, plain human language (from `bro`), Simplified Technical English, and glossary terms. |
| `retro` | merged | matt | pstack `reflect` | New "Skills" category for routing learnings into skill edits (the idea behind `reflect`). Nothing is applied before you pick. |
| `architect` | merged, mostly own text | pstack | matt `DESIGN-IT-TWICE.md`, matt `grilling` | Same phases as pstack. Arena (multi-model, Cursor-only) is replaced by Matt's design-it-twice subagents. The checkpoint is on by default and runs as a grilling round. Cursor model routing and links to dropped skills are removed. `runner-prompt.md` is deleted, and one line of `rationale-template.md` changed. |
| `how` | adapted | pstack | | Cursor model and subagent routing removed. Falls back to working alone without subagents. Uses glossary terms. Now model-invoked. |
| `blast-radius` | adapted | pstack | | Links to `why` and `arena` (both dropped) removed. Framework examples are made generic. |
| `unslop` | adapted | pstack | | Model-invoked, with a description that says when to trigger. |
| `technical-writing` | adapted | pstack | | Model-invoked. Removed the Cursor adapter line and poteto-specific rules (tab indentation, "swarm logs"). |
| `typescript-best-practices` | adapted | pstack | | Model-invoked. |
| `principle-*` (17) | adapted | pstack | | Only the frontmatter changed: `disable-model-invocation` is removed, so each principle triggers on its own. `principle-prove-it-works` also lost the Cursor adapter line and its link to `show-me-your-work`. |
| `inbox-capture` | own | | | Written from my vault's `CLAUDE.md`, its templates, and one existing capture. Finds the vault per device (working directory, `SECOND_BRAIN_VAULT`, memory, or asks). |
| `t-mode` | own | | | Written from my vault's conversation rules and the decisions made while building this library. |

Other files that are my own: `README.md`, `PROVENANCE.md`, `upstream.json`, `scripts/`, and `.claude-plugin/`.

## Clash decisions

| Overlap | Kept | Why |
|---|---|---|
| Autonomy: Matt grills, pstack's `never-block-on-the-human` decides alone | Matt | Grill first, then build. `never-block-on-the-human` is dropped, and `architect`'s checkpoint is on by default. |
| `tdd` (both) | Matt's loop, plus pstack's guardrails | Matt's seam agreement fits grill-first. pstack stops forced bad tests. |
| What a good test is | The pstack principle is the single source | One meaning, one place. |
| `teach` (both) | Matt | Socratic with quizzes. pstack's `teach` forbids quizzes. |
| `wait-what` vs `bro` | Merged into `wait-what` | Same job. |
| `code-review` vs `interrogate` | `code-review` plus `blast-radius` | `interrogate` needs pstack's multi-model arena. |
| `retro` vs `reflect` | `retro`, with the routing idea from `reflect` | `reflect` is built on Cursor transcripts and model routing. |
| `setup-matt-pocock-skills` | `setup-project` | No triage. Notion comes in through the "other" tracker. |

What was left out, and so isn't tracked, is listed under `left_out` in `upstream.json`.

## Updating from upstream

1. Import the new upstream onto its vendor branch. This doesn't touch `main`:

   ```
   python scripts/sync_upstream.py import matt
   ```

   The output shows which files changed upstream. It also lists upstream skills that are new (neither tracked nor in `left_out`) and the merged-in sources you need to check by hand.
2. Read what upstream changed: `git show vendor/matt`.
3. Merge it: `git merge vendor/matt`. Skills labelled upstream update cleanly. For adapted and merged skills, git applies the upstream change on top of my edits, and it stops with a conflict only where both sides changed the same lines. Resolve conflicts against the clash decisions above.
4. For each new upstream skill, either add it to `skills` in `upstream.json` and import again, or add it to `left_out`.
5. If an update changes what a skill does, update its row here.

Ideas taken from a skill that isn't tracked (pstack `tdd`, `bro`, `reflect`) never reach a vendor branch. The import prints them as a reminder to check them by hand.
