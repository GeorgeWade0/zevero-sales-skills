---
name: "value-follow-up-pdf"
description: "Create a branded one-page Zevero PDF to send after a prospect or client replies, asks for something or needs internal sign-off. Input is the company, the contact and what they said. Not for cold outreach."
---

# Value follow-up PDF

This skill makes a one-page, Zevero-branded PDF for a salesperson to send. The page answers what the prospect or client asked about, uses their own situation, and ends with one clear next step.

Use it for follow-ups that return with value: after a reply, a call, a meeting, an event, or when a client's wider team must sign off. Do not use it for cold first messages. If there was no contact before, say so and suggest the discovery-brief skill and a short intro message.

## Step 1. Get the context

You need these inputs. Take them from the conversation first (screenshots, pasted messages, a discovery brief made earlier), and then from HubSpot (Step 2). Use AskUserQuestion only for an input that you cannot find.

1. **Company** (name or website).
2. **Contact** (name, and the LinkedIn URL if available).
3. **What they said.** Their reply, message, call notes or screenshot.
4. **The topic of the page.** What the salesperson promised to send, or what the deal is waiting for.

## Step 2. Check HubSpot

- Find the company and its open deals. Read the deal name, stage, amount and **next step**. The next step often holds the real signal (for example "Waiting sign off from wider team").
- Read the latest **incoming** emails and notes on the deal. The newest email is often our own chaser, so do not treat it as "what they said".
- Note the **deal owner**. If the owner is not the current user, the page signs off with both names (Step 4).
- If this conversation already has a discovery brief, use it and do not research again.

## Step 3. Choose the page type

| Situation | Page type | Main table columns |
|---|---|---|
| Prospect, a rule or customer requirement applies (NHS, CSRD, CDP, retailer) | Gap page | Requirement · Applies from · On your website today · What to do |
| Existing client, upsell or new scope that needs sign-off (PCF, EPD, SBTi, B Corp) | Scope page | Item · What we measure or deliver · What we need from you · Status |
| Prospect asks "what would this involve?" with no rule behind it | Scope page | as above |

Tell the salesperson which type you chose, in one line.

## Step 4. Research from sources

Every fact on the page must have a link in the sources footer.

- **Rules and standards.** Fetch the primary source (NHS England, GOV.UK, EFRAG, SBTi, B Lab, the standard body). If the web page has no detail (for example a standard's landing page), do not quote requirements from memory. Leave them out, or name the standard without details.
- **Their position.** For a prospect, fetch their own sustainability page, CRP, report or B Corp profile. For a client, prefer what we already hold (HubSpot, project files) over the web.
- **Source quality.** Label each fact by source type. A primary source can stand alone. A trade-press or third-party source (for example a sustainability tracker) is allowed, but give it the publisher name and date in the footer. If the third party says the data is unverified, do not use it as the main fact on the page. Write a supplier's or manufacturer's figure as "[Company] reports…", never as a fact.
- Keep a list of every URL that you opened.

## Step 5. Write the content

Write in the salesperson's voice: first person, plain words, short sentences. Reuse the words the salesperson used in their own message.

The page has these parts. Remove a part if there is nothing true to put in it.

1. **Header.** "Prepared for [Company] · [Month Year]" on the left, Zevero logo on the right.
2. **Title.** Two lines, with line 2 in Azure.
3. **Lead (2 to 3 sentences).** The main point and its date or reason. Start with "As promised," only if the salesperson promised it.
4. **Cards (optional, 4 to 6).** For a gap page: dated milestones of the rule. For a scope page: "why now" drivers from sources (their targets, recertification dates, retailer or industry commitments). Make the most important card the dark card.
5. **Main table** (from Step 3, maximum 7 rows). Use pills: Met (sky blue), Gap or Data needed (yellow), Done (sky blue).
6. **One-line note.** For a gap page: "I've only looked at public pages…". For a scope page: a practical ask, for example "please send all the data in one go".
7. **Reference box (optional).** One published number that sets expectations, labelled with who reported it.
8. **Steps (3 to 5 numbered).** For a gap page: how to close the gap. For a scope page: sign-off, data, calculation, review, use.
9. **Next step card (dark).** One specific ask and the sign-off. If the deal owner is not the current user, show the current user and "Your [topic] lead: [owner name, email]".
10. **Sources footer** with links and "Viewed [date]".

Do not invent numbers, customer names, scope items or results. **Zevero claims to confirm:** if the page states a Zevero method or standard (for example "following ISO 14067"), a price, a timeline or a deliverable, list it in Step 8 for the salesperson to confirm.

## Step 6. Run the AI tells check automatically

Do not wait for the salesperson to ask. Before you render, invoke the `ai-tells` skill on all the page text and on the cover message.

- Follow that skill: read its `references/ai-tells-list.md` in full and scan literally. Check each replacement word against the list again.
- Also remove text that sounds generated even if it is not on the list: impersonal phrases ("This page compares…"), formal labels ("Suggested next step"), sales slogans and highlighted buzzwords.
- Make sure that there is no em dash character.
- In chat, report the result in one line (for example "AI tells check: clean" or "3 fixes"), not a full table, unless the salesperson asks.

## Step 7. Render the PDF

Load the `zevero-brand` skill. Then:

1. **Font.** Manrope. Google Fonts can be blocked in the sandbox, so run `npm pack @fontsource/manrope` and use `files/manrope-latin-{400,600,700}-normal.woff2` with `@font-face`.
2. **Logo.** Copy `logo-base-green.png` from the `zevero-presentation` skill's `assets` folder.
3. **Build** one HTML page: `@page{size:A4;margin:0}`, a page box of 210mm × 297mm, padding of about 14mm × 15mm, a body of about 9.5pt, Base Green `#004646` headings, Azure `#265a62` labels and numbers, Midnight Green `#002321` for the dark cards, Soft Yellow `#f7ff8a` only for Gap or Data needed pills and the key date, and Seastone Grey `#dbe5e7` rules. Pills must have `white-space:nowrap`. The card grid uses one column per card (`repeat(N,1fr)`).
4. **Print** with Playwright Chromium: `page.pdf(format='A4', print_background=True, prefer_css_page_size=True)`.
5. **Verify.** `pdfinfo` must show `Pages: 1`. Render to PNG with `pdftoppm` and look at it. Check that no text is cut, no pill wraps, the table fits and the footer does not overlap. If it is longer than one page, shorten the text. Do not use fonts smaller than 8pt.
6. Save as `/mnt/user-data/outputs/[Company]_[topic]_one_pager.pdf` and send it with SendUserFile. If a folder is connected, also save it there.

## Step 8. Deliver

Give the salesperson:

- The PDF.
- A cover message of 2 or 3 lines for the channel the contact used, in the salesperson's voice, already checked with ai-tells.
- **Check before sending** (maximum 5 lines): the Zevero claims to confirm, facts from secondary or unverified sources, scope items you took from emails, and any conflict with HubSpot.

Do not summarise the PDF in chat.