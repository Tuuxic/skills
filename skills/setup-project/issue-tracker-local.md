# Issue tracker: Local Markdown

Specs and tickets for this repo live as markdown files in `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- The spec is `.scratch/<feature-slug>/spec.md`
- Tickets are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file
- Each spec and ticket has a `Status:` line near the top: `ready-for-agent`, `ready-for-human`, `in-progress`, or `done`
- Comments and history append to the bottom of the file under a `## Comments` heading

## When a skill says "publish to the issue tracker"

Create a new file under `.scratch/<feature-slug>/` (creating the directory if needed).

## When a skill says "fetch the relevant ticket"

Read the file at the referenced path. The user normally passes the path or the ticket number.

## When a skill says "close the ticket"

Set `Status: done` and append a one-line note under `## Comments` naming the commit that resolved it.
