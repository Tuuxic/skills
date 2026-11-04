# skills

My skill library for AI agents, built on [Matt Pocock's skills](https://github.com/mattpocock/skills). His skills stay close to upstream. My own layer adds question popups in `grilling`, my working style, and a note-capture skill.

## Install

**Claude Code.** Add the marketplace from GitHub (or from a local clone by its path), then install:

```
claude plugin marketplace add Tuuxic/skills
claude plugin install t-skills@tuuxic
claude plugin install t-obsidian@tuuxic
```

| Plugin | Contents |
|---|---|
| `t-skills` | Matt's 27 skills and `t-mode`. |
| `t-obsidian` | `inbox-capture`. Optional. |

Then run `/setup-matt-pocock-skills` once in each repo where you use the engineering skills. It records the issue tracker and the domain doc layout.

**My working style.** A plugin can't install a global `CLAUDE.md`, so on each device, link `personal/CLAUDE.md` from a clone of this repo. Update it with `git pull`.

On Windows, this needs Developer Mode or an admin PowerShell:

```powershell
New-Item -ItemType SymbolicLink -Path "$HOME\.claude\CLAUDE.md" -Target "<clone>\personal\CLAUDE.md"
```

On macOS or Linux:

```sh
ln -s "<clone>/personal/CLAUDE.md" ~/.claude/CLAUDE.md
```

Where there is no link or no global `CLAUDE.md`, type `/t-mode` for the full version.

**Codex.** Copy or symlink each folder in `skills/` into the agent's skills directory. Each skill carries an `agents/openai.yaml`.

## Which skill to run

Type `/ask-matt` and describe your situation. The usual route for a feature is:

`/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement` or `/implement-spec` → `/retro`

`/setup-matt-pocock-skills` comes first in each repo. `/implement` and `/implement-spec` drive `tdd` and close with `code-review`.

## Skills

"User" means you type `/name` to run it. "Auto" means the agent can also pick it up from its description.

### Planning

| Skill | Run | What it does |
|---|---|---|
| `ask-matt` | user | Router: says which skill or flow fits your situation. |
| `setup-matt-pocock-skills` | user | Configures a repo's issue tracker, triage labels, and domain doc layout. |
| `grilling` | auto | Interview over a decision tree, in question popups of up to four questions with a recommended answer for each. |
| `grill-me` | user | `grilling` with nothing saved, for work outside a repo. |
| `grill-with-docs` | user | `grilling` plus `domain-modeling`: updates `GLOSSARY.md` and ADRs as terms settle. |
| `domain-modeling` | auto | Sharpens terms against `GLOSSARY.md` and records hard-to-reverse decisions as ADRs. |
| `codebase-design` | auto | Deep-module vocabulary: module, interface, seam, depth, leverage. |
| `to-spec` | user | Turns the conversation into a spec in the tracker. |
| `to-tickets` | user | Breaks a plan into tracer-bullet tickets with blocking edges. |
| `wayfinder` | user | Plans work too big for one session as a map of decision tickets. |
| `research` | auto | Investigates a question in primary sources and saves a cited Markdown file. |
| `to-questionnaire` | user | Turns a decision only someone else can answer into a questionnaire for them. |

### Building and debugging

| Skill | Run | What it does |
|---|---|---|
| `implement` | user | Builds a spec or ticket with `tdd`, then runs `code-review` and commits. |
| `implement-spec` | user | Builds a whole spec on one integration branch, with parallel subagents across the ready tickets. |
| `tdd` | auto | Red-green-refactor, one vertical slice at a time. |
| `prototype` | auto | Throwaway code to answer a logic or UI question. |
| `diagnosing-bugs` | auto | Builds a loop that goes red on the bug, then hypothesises, instruments, fixes, and adds a regression test. |
| `wizard` | auto | Generates an interactive bash script for steps only a human can do. |

### Review and upkeep

| Skill | Run | What it does |
|---|---|---|
| `code-review` | auto | Two parallel reviews of a diff: standards (plus a Fowler smell baseline) and spec. |
| `pr` | auto | Shapes a pull request body: smallest visual, before/after evidence, and a merge-danger call. |
| `triage` | user | Moves incoming issues through a state machine of triage roles. |
| `improve-codebase-architecture` | user | Surveys a codebase for deepening opportunities and grills through the one you pick. |
| `retro` | user | Suggests improvements to the agent's environment after a session. |

### Session and learning

| Skill | Run | What it does |
|---|---|---|
| `handoff` | user | Compacts the session into a doc for another agent. |
| `wait-what` | user | Re-pitches the last message plainly, with the context you were missing. |
| `teach` | user | Multi-session teaching workspace with lessons, quizzes, and learning records. |
| `writing-for-agents` | auto | How to write skills, `CLAUDE.md`, and other docs agents read. |

### Personal

| Skill | Run | What it does |
|---|---|---|
| `t-mode` | user | My full working style: replies, autonomy, proof, plain writing, and code. |
| `inbox-capture` | auto | Writes a capture into my Obsidian vault's `inbox/` the way the vault's `CLAUDE.md` asks. |

## Where the skills come from

[PROVENANCE.md](PROVENANCE.md) labels each skill as upstream, adapted, or own. It lists what changed, records the design decisions, and explains how to pull in upstream updates.

Built from Matt Pocock's skills, MIT. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
