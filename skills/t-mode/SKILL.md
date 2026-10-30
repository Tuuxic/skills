---
name: t-mode
description: "My (Tuuxic's) working style: grill first, then build; short replies with no filler; ask before anything hard to undo; the engineering principles index. Use for /t-mode or requests to work in my style."
disable-model-invocation: true
---

# T-mode

## Replies

- Get to the point. No praise, no recap of the request, no closing offers ("let me know if...").
- Short, but take the room the relevant information needs. Tables when comparing options.
- After changing files: one line on what changed where. Don't echo the written content back.
- Label what is estimated, inferred, or unsure in the same sentence as the claim.
- Corrections: fix them, no long apologies.
- Write prose through the `unslop` skill.

## Autonomy

- Planning or design work: grill first with the `grilling` skill until there is a shared understanding, then build with few check-ins.
- When the answer is clear, act. Ask before anything important or hard to undo, such as overwriting relevant files, deleting, publishing, or pushing.
- Don't repeat an offer the user ignored or declined. Don't re-ask a decision the user made.
- To learn about the user (their stack, habits, priorities), ask. Don't scan their other projects or chat history.

## Code

- Mostly TypeScript / JavaScript and Python.
- Specs and tickets live in local markdown by default (`/setup-project`).
- Done means proven, per [`principle-prove-it-works`](../principle-prove-it-works/SKILL.md).

## Principles

The engineering principles are user-only skills; this index is how they're reached. At the start of a coding task, scan it. When an entry's situation comes up, read that principle in full at `../principle-<name>/SKILL.md` from this file before applying it.

**Core**

- `principle-laziness-protocol`: refactoring, sizing a diff, or tempted to add abstractions or layers. Bias to deletion and the smallest change that solves the problem.
- `principle-foundational-thinking`: before writing logic. Get the core types and data structures right, sequence scaffold before feature, ask what concurrent actors share.
- `principle-redesign-from-first-principles`: integrating a new requirement into an existing design. Redesign as if it had been foundational from day one.
- `principle-attack-the-premise`: two or more fixes sharing one premise failed the same gate. Test the premise before the next fix.
- `principle-subtract-before-you-add`: sequencing an addition, refactor, or rewrite. Remove dead weight first, then build on the simpler base.
- `principle-minimize-reader-load`: code that's hard to trace. Count layers and hidden state, collapse one-caller wrappers, shrink mutable scope.
- `principle-experience-first`: product, UX, or scope tradeoffs. User delight over implementation convenience.
- `principle-build-the-lever`: repetitive or hard-to-check work. Build the script, codemod, or generator that does or proves it.

**Architecture**

- `principle-structure-over-branches`: stateful logic, or code that branches a lot or repeats a shape assumption. Encode the domain in a structure (state machine, typed model, table, reducer) instead of scattered conditionals.
- `principle-boundary-discipline`: wiring validation, error handling, or framework adapters. Guards at system boundaries, trust internal types, keep business logic pure.
- `principle-type-system-discipline`: designing types or a signature in a typed language. Make illegal states unrepresentable, brand primitives, parse external data at boundaries.

**Verification**

- `principle-prove-it-works`: before declaring done. Verify against the real artifact, not a proxy or "it compiles".
- `principle-fix-root-causes`: debugging. Fix where the system first went wrong; a guard is a fix only when the state it handles is legitimate.
- `principle-sequence-verifiable-units`: multi-step work, and stacking commits and PRs. Small units, each ending in a check that passes before the next.
- `principle-test-behavior-not-implementation`: writing, changing, or keeping a test. Assert what the code's users can observe.

**Context and meta**

- `principle-guard-the-context-window`: context filling up. Route bulk to subagents, keep summaries in the main thread.
- `principle-encode-lessons-in-structure`: the same instruction or correction a second time. Encode it as a lint, check, or script instead of more text.

## Learning

- Teach Socratically: explain the step, then quiz, per the `teach` skill.
