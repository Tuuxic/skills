---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker (`docs/agents/issue-tracker.md`) and state its title before starting. If the reference is ambiguous, ask.

Work the **frontier**: tickets whose blockers are all done, one at a time, in number order.

Use the `tdd` skill where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Before calling a ticket done, apply `principle-prove-it-works`: run the real feature, not only the tests. Then mark the ticket done in the tracker.

Once done, use the `code-review` skill to review the work.

Commit your work to the current branch, one commit per ticket.
