# Issue tracker: <Name, e.g. Notion>

Specs and tickets for this repo live in <where: workspace, database, project>.

## Access

<How the agent reaches it: an MCP server name, a CLI, an API. Name the exact tool.>

## Statuses

The planning skills use four statuses: `ready-for-agent`, `ready-for-human`, `in-progress`, `done`. Map each to this tracker's field and value:

- `ready-for-agent` → <...>
- `ready-for-human` → <...>
- `in-progress` → <...>
- `done` → <...>

## When a skill says "publish to the issue tracker"

<Exact operation: which database or project, which properties to set, where the body goes.>

## When a skill says "fetch the relevant ticket"

<How to look one up from an ID, URL, or title.>

## Blocking edges

<Does the tracker have a native "blocked by" relation? If yes, name the property. If no, write "Blocked by: <ticket refs>" in the body.>

## When a skill says "close the ticket"

<Exact operation.>
