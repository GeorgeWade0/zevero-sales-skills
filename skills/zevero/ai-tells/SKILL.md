---
name: ai-tells
description: >-
  Scan a piece of writing for "AI tells" (words, phrases and constructions that
  signal machine authorship) and produce a de-telled rewrite that keeps the
  meaning. Use whenever the user asks to "de-tell", "scan for AI tells", "make
  this sound human", "does this sound like AI?", "remove the AI-isms", "check
  this before I send it", or invokes /ai-tells by name, on any draft (email,
  LinkedIn post, doc, message, proposal, web copy). Also use when the user has
  just asked for human-sounding prose and is about to send or publish it. In the
  Zevero sales plugin it also runs automatically on every customer-facing draft
  (emails, LinkedIn, proposals, decks, one-pagers) before it is shown. Not for translation, tone rewrites into a new voice, or grammar
  fixes; this specifically targets the tics that read as AI.
---

# AI tells

This skill removes the vocabulary and constructions that make writing read as AI-generated. The authoritative list lives in `references/ai-tells-list.md`. That file is the skill: your job is to apply it faithfully to a specific draft.

## The one rule that makes this work: scan against the open file, not from memory

The single most important instruction, stated at the top of the reference list, is that the scan must be literal, run with `references/ai-tells-list.md` open in front of you, checking the draft word by word against the entries. Do not scan from memory. There are two reasons this matters, and both cause real failures:

1. A recall-based scan only catches the tells that happen to be salient today, and the list is long. You will miss the quieter entries every time.
2. The rewrite itself is the dangerous moment. When you replace a flagged phrase, your instinct reaches for a synonym, and synonyms are drawn from exactly the banned vocabulary. A from-memory rewrite routinely removes one tell and introduces another. So every replacement phrase you write must itself be checked back against the list before you commit to it.

So the workflow always begins by reading the reference file, and you keep returning to it during the rewrite. This is not optional throat-clearing; it is the mechanism.

## Workflow

1. **Read `references/ai-tells-list.md` in full.** Every time. It is the checklist you are about to run.

2. **Identify the exact text to scan.** Scan the draft the user is actually presenting, which means the content of the file or the passage itself, not the covering note that introduces it. If the user hands you a document and a message about the document, the document is the draft. If they built this draft by editing an earlier one, treat every line as new: reused lines feel already-approved and are where tells hide most often, so they get the same scrutiny as fresh text.

3. **Scan literally, category by category.** Walk the draft against each section of the list. For the mechanical entries (em dashes, "genuinely", "honestly", "in real time", "Tuesday", "quiet/quietly", and the like) a literal string check is enough. For the constructional entries (abstraction-as-protagonist epigrams, "the kind of X that makes you Y", unnamed-transformation fragments, self-labelling, unearned insider claims) you are matching a pattern, so read for the shape, not the exact words. The list gives worked examples of each shape; use them as templates.

4. **Report what you found (flag).** Before rewriting, show the user the tells you caught, so they can see the diagnosis and trust the fix. Use this format, one row per tell:

   > **[category]** — "the flagged phrase, quoted exactly" → why it reads as AI here, in one line.

   Group by severity of obviousness if the list is long (em dashes and filler affirmations first, subtle constructional tells after). When a single span trips two entries at once, combine them into one row if the list itself treats them as a stacked pair (for example the "from the moment..." opener towing "something shifts", or "really matters" plus "matters to us"), and split them into separate rows when they are independent tells that happen to sit close together. If the draft is genuinely clean, say so plainly and stop; do not invent tells to look busy.

5. **Rewrite (fix).** Produce the corrected draft. The governing principle behind the whole list, stated in its header, is that the tell is a symptom of a claim that was asserted instead of shown. So the fix is almost never a straight synonym swap. When you hit an intensifier ("genuinely", "really matters"), the impulse to add it is itself the signal that the underlying claim needs a concrete reason or should be stated plainly: supply the reason or delete the word, do not soften it. When you hit a performed-impact phrase (something "landing" or "mattering", "the kind of thing that makes you pay attention"), replace it with the specific fact that would produce the impact on its own. When you hit an abstraction-as-protagonist epigram, apply the list's test: can you picture the subject doing the verb? If not, give the sentence a concrete human subject and a literal verb, or cut it, because it is usually just restating the sentence before it.

   As you write each replacement, check it back against the list. This is where new tells sneak in.

   **When the draft has no substance to expose.** Some drafts, especially marketing and sales copy, are almost entirely performance: strip the tells and there is no concrete claim left underneath, because the writer never stated one. Do not invent facts to fill the hole, and do not paper over it with a different-sounding but equally empty line. Instead, rewrite as far as the real content allows and leave a clearly marked placeholder for the missing specific, for example "[name the pattern your tool actually finds]", then say in the delivery note what you need from the user to finish it. A hollow draft is exactly the kind most likely to be handed to this skill, so expect this case rather than treating it as an edge case.

6. **Preserve voice and meaning.** You are removing tics, not rewriting the person's argument or flattening their style into generic corporate prose. Keep their structure, their facts, their register, and their intent. If removing a tell would change what they are claiming, flag it and ask rather than silently altering the substance. The goal is that it sounds like them on a good day, not like a different author.

7. **Deliver.** Give the flag report first, then the clean rewrite, then a one-line note on anything you deliberately left (for example, an em dash inside a quotation you should not edit, or a phrase that matched a pattern but is correct in context), plus anything you need from the user to finish a placeholder. If the draft came from a file, offer to write the cleaned version back; if it was pasted straight into the chat, just return it inline.

## A note on em dashes

The list flags the em dash character ("—") specifically, because it is one of the strongest single signals. When rewriting, actually check the output for the "—" character rather than trusting your eye, and resolve each one by restructuring the sentence or using a comma, colon, brackets, or full stop. Leave em dashes untouched only inside material you should not edit, such as a direct quotation.

## Scope and judgement

This is a scan for AI tells, not a general copyedit. Do not fix grammar, restructure arguments, or impose a house style unless the user asks. Equally, use judgement: the list is a set of strong defaults, not a set of absolute bans. A flagged word can occasionally be the right word in context (a piece literally about Tuesdays; a quotation you are reproducing). When that happens, keep it and say why in the delivery note. The list itself makes this point, that these are patterns to catch, not a machine to run blindly.
