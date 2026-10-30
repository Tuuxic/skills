---
name: setup-project
description: "Configure this repo for the planning skills: where specs and tickets live (local markdown, or another tracker such as Notion) and where the glossary and ADRs live. Run once per repo before /to-spec, /to-tickets, or /code-review."
disable-model-invocation: true
---

# Setup project

Scaffold the per-repo configuration the planning skills read:

- **Issue tracker**: where specs and tickets live. Local markdown by default.
- **Domain docs**: where `GLOSSARY.md` and ADRs live, and how skills read them.

Explore, present what you found, confirm with the user, then write.

## 1. Explore

Read what exists; don't assume:

- `CLAUDE.md` and `AGENTS.md` at the repo root: does either exist? Is there already an `## Agent skills` section?
- `docs/agents/`: does this skill's earlier output exist?
- `.scratch/`: a sign the local-markdown tracker is already in use.
- `GLOSSARY.md`, `GLOSSARY-MAP.md`, `docs/adr/`.
- Monorepo signals (`pnpm-workspace.yaml`, a `workspaces` field, a populated `packages/*`). Their absence means single-context, which is almost every repo.

## 2. Ask, one section at a time

Lead each section with the recommended answer so the user can accept it in a word. Skip a section when exploration already settled it.

**Section A: Issue tracker.**

- **Local markdown** (recommended): specs and tickets are files under `.scratch/<feature>/`. Seed: [issue-tracker-local.md](./issue-tracker-local.md).
- **Other** (Notion, GitHub, Linear, ...): seed from [issue-tracker-other.md](./issue-tracker-other.md) and fill in each operation with the user. Confirm the agent can actually reach the tracker (an MCP server, a CLI) before writing, by running one read operation.

**Section B: Domain docs.** Default to single-context (one `GLOSSARY.md` plus `docs/adr/` at the root) and write it without asking. Offer multi-context (`GLOSSARY-MAP.md` pointing at one `GLOSSARY.md` per context) only when exploration found monorepo signals.

## 3. Confirm

Show a draft of the `## Agent skills` block and of `docs/agents/issue-tracker.md` and `docs/agents/domain.md`. Let the user edit before writing.

## 4. Write

Edit `CLAUDE.md` if it exists, else `AGENTS.md`. If neither exists, ask which to create. Update an existing `## Agent skills` block in place instead of appending a second one.

```markdown
## Agent skills

### Issue tracker

[one line: where specs and tickets live]. See `docs/agents/issue-tracker.md`.

### Domain docs

[one line: single-context or multi-context]. See `docs/agents/domain.md`.
```

Write `docs/agents/issue-tracker.md` from the chosen seed and `docs/agents/domain.md` from [domain.md](./domain.md).

## 5. Done

Say which skills now read these files (`to-spec`, `to-tickets`, `implement`, `code-review`, `domain-modeling`). Switching trackers later means editing `docs/agents/issue-tracker.md` or rerunning this skill.
