---
name: flow
description: "Which skill to run next. Maps a situation (feature, bug, design, learning, writing, session end) to the commands in this library."
disable-model-invocation: true
argument-hint: "What are you about to do?"
---

# Flow

The router for this library: it names the user-invoked skills and when each fits. It points, it doesn't run them; the user types the command.

## Steps

1. **Place the user.** Read the argument and the conversation: which route below matches, and which step of it is already done (a spec exists, tickets exist, code is written)? When nothing is given and the conversation doesn't settle it, show the route list and stop.
2. **Name the next command**, with one line on why it fits now. Add the step after it only when the two belong together.
3. **Flag a skipped gate.** When the user is past a step the route needs (implementing with no agreed seams, opening a PR on shared code with no blast radius check), say which one in one line.

Done when the user knows the one command to type next.

## Routes

**Once per repo:** `/setup-project` before anything that reads the tracker (`/to-spec`, `/to-tickets`, `code-review`).

**Assigned feature, from a description:**

1. `/grill-with-docs` (or `/grill-me` when the repo has no glossary or ADRs): close the gaps in the description.
2. `/to-spec`: the spec, with the test seams confirmed.
3. `/architect`, only when the shape is the hard part. It implements after the agreement, so for design-heavy work it replaces 4 and 5; or stop it after the agreement and continue with 4.
4. `/to-tickets`: tracer-bullet slices with blocking edges. The last real checkpoint.
5. `/implement`: ticket by ticket with `tdd`, proven, one commit each, `code-review` at the end. `/handoff` to continue in a fresh session when context runs long.
6. `/blast-radius` before the PR, when the change touches shared code.
7. `/retro` after.

**Small feature:** `/grill-me`, then `/implement` from the conversation.

**Bug:** describe it; `diagnosing-bugs` starts by itself. `/blast-radius` on the fix when it touches shared code.

**Task feels shallow or misframed:** `/sharpen`, then the route it lands on.

**Unsure we mean the same goal:** `/in-your-own-words`.

**The last reply didn't land:** `/wait-what`.

**Learning a topic:** `/teach`, over several sessions.

**Session end:** `/handoff` to continue elsewhere, `/retro` to improve the setup and the skills.

**My working style for this session:** `/t-mode`.

The rest start by themselves from what you ask: `how` for code walkthroughs, `prototype` for design questions, `unslop` and `technical-writing` for prose, `inbox-capture` for saving notes. The principles come in through `/t-mode`'s index and the skills that link them.
