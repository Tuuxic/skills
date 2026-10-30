# skills

My skill library for AI agents. It started from [Matt Pocock's skills](https://github.com/mattpocock/skills) and poteto's [pstack](https://github.com/cursor/plugins/tree/main/pstack), kept what fits how I work, and resolved the places where the two disagree.

How the library works:

- **Grill first, then build.** Planning goes through an interview until we share an understanding. After that, the agent works with few check-ins.
- **Proof over claims.** Work is done when it's verified against the real thing.
- **Plain writing.** Prose goes through `unslop`.
- **Local first.** Specs and tickets are markdown files in the repo. The tracker is swappable (Notion later) through `/setup-project`.

## Install

**Claude Code.** The marketplace offers `t-skills` with everything, plus one plugin per group. Install either `t-skills` or the groups you want, not both: both together load each skill twice.

| Plugin | Contents |
|---|---|
| `t-skills` | All skills. |
| `t-coding` | Planning, building, debugging, review, and the principles. |
| `t-writing` | `unslop`, `technical-writing`, `writing-for-agents`. |
| `t-learning` | `teach`. |
| `t-core` | `t-mode` and session tools. |
| `t-obsidian` | `inbox-capture`. |

Add the marketplace from this folder (or as `Tuuxic/skills` once it's on GitHub), then install:

```
claude plugin marketplace add C:/Users/Nikolai/Desktop/Dev/Projekte/skills
claude plugin install t-skills@tuuxic
```

Or by group:

```
claude plugin install t-coding@tuuxic
claude plugin install t-writing@tuuxic
claude plugin install t-learning@tuuxic
claude plugin install t-core@tuuxic
claude plugin install t-obsidian@tuuxic
```

From GitHub in one step: `/plugin install t-skills --marketplace Tuuxic/skills` (same for each group).

Groups refer to each other by skill name. `t-core`'s `t-mode` uses skills from `t-coding`, `t-writing`, and `t-learning`, and `t-coding`'s `blast-radius` uses `unslop`. A missing group only means those pointers go nowhere. `python scripts/build_marketplace.py` lists every cross-group reference.

A skill's group is its `group` field in `upstream.json`. After changing one, run `python scripts/build_marketplace.py` to regenerate `.claude-plugin/marketplace.json`.

**Codex and other agents:** copy or symlink each folder in `skills/` into the agent's skills directory.

**claude.ai / Claude app:** zip one skill folder and upload it under Settings, Capabilities, Skills. `disable-model-invocation` is a Claude Code field. Other harnesses ignore it, so those skills can trigger on their own there.

## Skills

"User" means you type `/name` to run it. "Auto" means the agent can also pick it up from its description.

### Planning

| Skill | Run | What it does |
|---|---|---|
| `grilling` | auto | Interview in rounds over a decision tree, with a recommended answer for each question. |
| `grill-me` | user | Shortcut to `grilling`. |
| `grill-with-docs` | user | `grilling` plus `domain-modeling`: writes the glossary and ADRs as terms settle. |
| `domain-modeling` | auto | Sharpens terms against `GLOSSARY.md`, offers ADRs sparingly. |
| `setup-project` | user | Configures the tracker (local markdown, or Notion and others) and domain-doc layout per repo. |
| `to-spec` | user | Turns the conversation into a spec in the tracker. |
| `to-tickets` | user | Breaks a spec into tracer-bullet tickets with blocking edges. |
| `architect` | user | Sketches types and modules (designed twice), agrees the shape with you, then implements against it. |
| `codebase-design` | auto | Deep-module vocabulary: module, interface, seam, depth, leverage. |

### Building and debugging

| Skill | Run | What it does |
|---|---|---|
| `implement` | user | Works through tickets with `tdd`, proves each one, then runs `code-review`. |
| `tdd` | auto | Red-green loop at agreed seams. Prefers no test over a bad test. Reports red/green evidence. |
| `prototype` | auto | Throwaway code to answer a logic or UI question. |
| `diagnosing-bugs` | auto | Builds a tight red feedback loop, then hypothesises, instruments, and fixes at the root cause. |
| `typescript-best-practices` | auto | Discriminated unions, branded types, no `as`, parse at boundaries. |

### Review

| Skill | Run | What it does |
|---|---|---|
| `code-review` | auto | Two parallel reviews: standards (plus a Fowler smell baseline) and spec. |
| `blast-radius` | user | Finds what a change breaks outside the diff and proves the one fact it's safe because of. |

### Learning

| Skill | Run | What it does |
|---|---|---|
| `teach` | user | Multi-session Socratic teaching workspace: mission, short HTML lessons, quizzes, learning records. |
| `how` | auto | Explains how a part of a codebase works, with parallel explorers for big subsystems. |
| `wait-what` | user | Re-pitches the last message plainly. |
| `in-your-own-words` | user | Restates your goal and problem, to check alignment. |

### Writing

| Skill | Run | What it does |
|---|---|---|
| `unslop` | auto | Catalog of AI writing tells and their fixes. |
| `technical-writing` | auto | Diátaxis, Google style, Simplified Technical English, Global English. |
| `writing-for-agents` | auto | How to write skills, `CLAUDE.md`, and other docs agents read. |

### Session and meta

| Skill | Run | What it does |
|---|---|---|
| `handoff` | user | Compacts the session into a doc for a fresh agent. |
| `retro` | user | Suggests improvements to the agent's environment and to these skills after a session. |
| `sharpen` | user | Rewrites a task to be deeper, not bigger. |

### Personal

| Skill | Run | What it does |
|---|---|---|
| `t-mode` | user | My working style in one place. |
| `inbox-capture` | auto | Writes a capture into my Obsidian vault's `inbox/` the way the vault's `CLAUDE.md` asks. |

### Principles

Small rules from pstack that each trigger on their own situation (all auto): `attack-the-premise`, `boundary-discipline`, `build-the-lever`, `encode-lessons-in-structure`, `experience-first`, `fix-root-causes`, `foundational-thinking`, `guard-the-context-window`, `laziness-protocol`, `minimize-reader-load`, `model-the-domain`, `prove-it-works`, `redesign-from-first-principles`, `sequence-verifiable-units`, `subtract-before-you-add`, `test-behavior-not-implementation`, `type-system-discipline`. Each is `principle-<name>`.

## Where the skills come from

[PROVENANCE.md](PROVENANCE.md) labels each skill as upstream, adapted, merged, or own. It lists what changed, records the clash decisions, and explains how to pull in upstream updates. The skills I left out are in `upstream.json`.

Adapted from Matt Pocock's skills and Lauren Tan's (poteto) pstack, both MIT. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
