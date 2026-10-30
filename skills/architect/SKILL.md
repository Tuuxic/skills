---
name: architect
description: "Sketch types, signatures, and module structure before code, agree the shape with the user, then implement against it. Use for /architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the wrong shape."
disable-model-invocation: true
---

# Architect

Sketch types, function signatures, class shapes, and module boundaries with `not implemented` bodies and pseudocode. Agree the sketch with the user, then fill in code against it.

Open a todolist with one entry per phase: Ground, Sketch, Agree, Implement, Scrap.

## Phase A: Ground the problem

Build a real mental model of every system the new code touches. Run the `how` skill over the relevant subsystems. Naming a file isn't grounding.

Skip Phase A only when the work is greenfield with no surrounding system to integrate.

## Phase B: Sketch

Design it twice. Follow [DESIGN-IT-TWICE.md](../codebase-design/DESIGN-IT-TWICE.md) with the Phase A grounding as the brief: parallel subagents, each with a different design constraint, each producing a structurally distinct candidate. Whole-shape alternatives, not point fixes inside one shape. Where subagents are unavailable, write at least two distinct candidates yourself, one after the other.

Each candidate writes the caller's usage first (two or three realistic call sites) and derives the types from it. Apply these while sketching:

- Data structures first, per `principle-foundational-thinking` and `principle-model-the-domain`.
- Encode invariants in types, per `principle-type-system-discipline`.
- Validate at boundaries, trust types inside, per `principle-boundary-discipline`.
- Short call chains, per `principle-minimize-reader-load`.

Screen every candidate against [references/design-red-flags.md](references/design-red-flags.md). Assume the next contributor is an agent that sees only the files it opened, copies the nearest example, and takes the shortest path that compiles. Prefer the design where a change that looks right from one file is right for the whole repo.

Compare on interface depth using the `codebase-design` vocabulary. Pick a base, graft the strongest parts of the others into it, and write the rationale per [references/rationale-template.md](references/rationale-template.md).

## Phase C: Agree

Show the user the synthesized sketch and rationale, and stop. Treat the "Open questions and risks" section as a grilling round: number each question and give your recommended answer, per the `grilling` skill. Proceed only after the user confirms the shape.

Skip the checkpoint only when the user explicitly says so ("no checkpoint", "just build it").

If the user pushes back on the shape, treat that as Phase A evidence. Re-ground and rerun Phase B before writing code.

## Phase D: Implement against the sketch

Replace `not implemented` bodies with code and pseudocode with logic. The sketch is the contract. Deviations from it are signal to surface, not friction to absorb silently. If a function needs a parameter the sketch didn't anticipate, ask whether the sketch was wrong, the requirement was missed, or the implementation is overreaching.

The sketch can ship as its own commit first, as the scaffold-first mode of `principle-foundational-thinking`.

## Phase E: Scrap when the architecture is wrong

If implementation keeps producing friction the sketch can't absorb, throw the sketch out. Don't bolt fixes onto a wrong design, per `principle-redesign-from-first-principles` and `principle-fix-root-causes`.

The signal is a pattern, not a single instance:

- The same shape of workaround appearing across unrelated code.
- Several unrelated edge cases that all need special-case branches.
- Types that need escape hatches (`any`, casts, optional fields always set in practice) to compile.
- Callers having to know the abstraction's internal rules to use it.
- Two or more independent Phase D deviations of the same shape.

A few edge cases don't condemn an architecture. Complexity in the data is not complexity in the design.

When you scrap, tell the user why, rerun `how` over what's been built, subtract before adding (`principle-subtract-before-you-add`), and return to Phase B. The new sketch should be smaller than the old one before it grows.

## Outputs

One file with new types and signatures for small changes. A module map plus type definitions for larger work. The rationale ships alongside.
