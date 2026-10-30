---
name: how
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which module owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, and onboarding mental models."
---

# How

Explore the codebase to answer "how does X work?" questions. Produce an architectural explanation at the level of a senior engineer onboarding onto a subsystem: enough to build a working mental model, not so much that it reads like annotated source code.

Subagents are read-only: tell each one not to edit files.

## 1. Assess complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. Explore and explain in one pass yourself, using the output format in [references/explainer-prompt.md](references/explainer-prompt.md). Go to step 4.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): go to step 2.

When in doubt, take the simple path.

## 2. Explore (complex only)

Split the question into 2 to 4 angles, each a distinct slice of the subsystem. Spawn one explorer subagent per angle in parallel, each with [references/explorer-prompt.md](references/explorer-prompt.md) and its angle filled in. Without subagents, work the angles one after another yourself.

## 3. Synthesize (complex only)

Once every explorer has returned, write the explanation from their findings per [references/explainer-prompt.md](references/explainer-prompt.md). Check contradictions against the code yourself.

## 4. Present

Use the sections from the explainer prompt, dropping any that don't apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas. Use the project's `GLOSSARY.md` terms when it exists.
