---
name: zevero-sales-context
description: Zevero's company, product, ICP, personas, value propositions, competitors, pricing, proof points, regulations and messaging rules - the facts every sales skill needs. Load this before any Zevero sales task (outreach, discovery, demos, proposals, objections, pricing, battlecards, account plans) and whenever another skill asks for a product-marketing or sales-context file. Also use when the user asks "what do we say about X", "who's our ICP", "how do we position against [competitor]", or "what can I quote as proof".
---

# Zevero sales context

The facts are in [references/context.md](references/context.md). Read the sections the task needs before writing anything customer-facing.

## How to use it

- **It is the context file other skills ask for.** When a skill says to read `.agents/product-marketing.md`, `.agents/sales-context.md` or `product-marketing-context.md`, use `references/context.md` instead and don't ask the user questions it already answers.
- **Never invent Zevero facts.** If a price, customer name, metric, certification or capability isn't in the file, say it's unknown and ask the user. Don't fill the gap with a plausible guess. Items marked `TODO` are gaps, not facts.
- **Check permission before naming customers.** Only cite customers listed as citable. For anyone else, describe them by sector and size.
- **Follow the market's rules.** Use UK English for UK prospects. For Japan, also load `en-ja-translator` and follow its terminology.
- **De-tell everything you write.** Run every draft through `ai-tells` and show only the cleaned version. That includes internal docs, decks, agendas, briefs and plans, not just what goes to customers.
- **Use the brand for anything visual.** Decks, PDFs and one-pagers go through `zevero-brand` or `zevero-presentation`.

## Keeping it current

Anyone can propose an edit to `references/context.md` with a PR or the `request-skill` skill. Each fact carries a source tag, so the source should be updated when the fact changes. The owner reviews it quarterly. The last review date is at the top of the file.
