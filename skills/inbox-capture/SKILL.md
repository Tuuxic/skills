---
name: inbox-capture
description: "Capture an idea, a source, or a requested vault edit into the Obsidian second-brain inbox as a new note. Use when the user says capture, save this, note this, put it in my inbox, or wants to keep something from the conversation."
---

# Inbox capture

Captures go into the vault's `inbox/`, one new file per capture. Never write to `wiki/`, and never read it for a capture. The vault's own `CLAUDE.md` wins over this skill wherever they disagree.

## Find the vault

The vault path differs per device, so never assume one. The vault is the folder that holds `CLAUDE.md`, `inbox/`, and `templates/Inbox Note.md`. Take the first of these that applies:

1. The current working directory, or one of its parents, is the vault.
2. The environment variable `SECOND_BRAIN_VAULT` names the vault folder.
3. Your memory or instructions on this device already name the vault path.
4. Otherwise ask the user for the path once. Then offer to remember it for this device in your user-level memory or instructions. Don't search the disk for it.

If the device has no file access (a phone, a chat app), follow [Without file access](#without-file-access).

## Steps

1. **Pick the type.** `idea` for a thought, plan, insight, or a requested edit to a vault page. `source` for something to read or watch (article, video, book, link).
2. **Title the note with the idea, not the topic.** "Reading Manhua on the Train Reclaims Commute Time", not "Commute". Title case, English, even when the source is German. A German source title stays as it is.
3. **Name the file** `YYYY-MM-DD HHMM - <Title>.md`, using the current local time. A new capture always gets a new file, even when it updates an earlier one.
4. **Start from the template** in the vault's `templates/`: `Inbox Note.md` for an idea, `Inbox Source.md` for a source. Replace `{{date}}` with `YYYY-MM-DD`. Fill `url:` for a source. Keep the template's fields and headings. When the vault isn't readable, use the fallback copies under [Templates](#templates).
5. **Write the body** under `# <Title>`, in the user's voice: plain, concise, first person for their own thoughts. Bullets for separate points.
   - Keep the user's reflections apart from what a source claims.
   - Write only opinions the user stated. Mark every idea, suggestion, or conclusion of yours with 💭: a whole section goes in `> [!quote] 💭 Suggestions`, a single line gets a prefix (`- 💭 ...`, `- [ ] 💭 ... #todo`).
   - Tasks are `- [ ] ... #todo`, with a due date as `📅 YYYY-MM-DD`. Say in the reply when a due date is your estimate.
   - For a source with no takeaways from the user, leave `# My Takeaways` empty. Takeaways get proposed at ingest.
   - For a requested edit, name the page and describe the change so the ingest can apply it.
6. **Report in one line**: the file name. Don't echo the note back. Don't offer to ingest unless the inbox holds about 10 notes or the note is time-sensitive.

## Without file access

Reply with the file name, then the full note in one markdown code block for the user to paste into `inbox/`.

## Templates

Fallback copies of the vault's templates. The vault's own files win when they're readable.

`Inbox Note.md`:

```markdown
---
type: idea
captured: {{date}}
tags:
  - inbox
---
```

`Inbox Source.md`:

```markdown
---
type: source
captured: {{date}}
url:
tags:
  - inbox
---
# My Takeaways
```

## Editing captures

Edit an existing inbox note only when the user asks. Never delete one without the user's OK.
