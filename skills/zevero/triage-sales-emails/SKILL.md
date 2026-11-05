---
name: triage-sales-emails
description: Clears unsolicited sales pitches out of the Gmail inbox and stars the emails that genuinely need George. Use when asked to clean up, triage, or sweep the inbox, or to get rid of sales or cold emails.
---

# Triage Sales Emails

Sort every inbox thread into one of three buckets. A thread that is not clearly a pitch stays in the inbox. Archiving a real email costs far more than leaving one pitch behind.

| Bucket | Meaning | Action |
| --- | --- | --- |
| `pitch` | Unsolicited selling aimed at George or Zevero | Add the `Sales Pitch` label, then remove `INBOX` |
| `flag` | A real person or customer who needs George to read or reply | Add `STARRED` and the `Needs George` label, leave in inbox |
| `leave` | Anything else, or anything uncertain | Do nothing |

Never trash, delete, mark as spam, reply, or unsubscribe. Archiving with a label is reversible. The rest are not.

## Procedure

1. Call `list_labels`. Create `Sales Pitch` (gray) and `Needs George` (red) with `create_label` if either is missing, then record both label IDs.
2. Fetch the inbox with `search_threads` using `in:inbox newer_than:7d`, paging with `pageToken` until no token remains. Use a different window only when George names one.
3. Classify each thread from its sender, subject, and snippet. Call `get_thread` only when those are not enough to decide.
4. For any sender that looks cold, run `search_threads` with `from:me to:<sender address>`. If George has ever written to that address, the thread is never `pitch`.
5. Apply the actions in the table with `label_thread` and `unlabel_thread`.
6. Report back in this shape, with one line per thread:

```text
Archived 14 pitches · Starred 3 · Left 22 untouched

Starred
- Jane Doe (Acme Foods): asking for revised pricing before Friday's board

Archived
- Lemlist rep: "Quick question about Zevero's outbound"
- ...

Borderline, left in inbox
- ...
```

List borderline calls separately so George can correct the rules.

[Read the classification rules and worked examples](./references/classification.md) before classifying anything, because sales emails disguise themselves as replies and warm intros.
