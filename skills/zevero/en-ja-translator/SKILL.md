---
name: en-ja-translator
description: >
  Translate professional content between English and Japanese for Zevero's internal and external
  communications. Use this skill whenever the user wants to translate, localise, or produce a
  bilingual version of any text — including Slack messages, Notion pages, security documentation,
  policy announcements, HR communications, or any other workplace content. Also triggers for
  phrases like "translate this", "Japanese version", "英訳", "和訳", "can you translate",
  "bilingual", or when the user pastes text and asks for it in the other language. Also use it
  for any text containing Zevero product terminology — UI labels, feature names, release notes,
  GHG Protocol emission categories, report names — since the platform has approved Japanese
  renderings that must be reused rather than re-derived.
  This skill handles cultural adaptation, Keigo register, translation annotations, and
  Zevero-specific terminology conventions.
---

# English ↔ Japanese Translator (Zevero)

This skill provides accurate, culturally appropriate translation between English and Japanese for
Zevero's professional communications and documentation. All feedback and annotations to the user
are always written in English.

---

## Direction Detection

Identify the source language from the input. If ambiguous, ask the user to clarify.

- **English → Japanese**: Apply full Keigo formatting, cultural adaptation, and annotation rules below.
- **Japanese → English**: Translate meaning accurately, flag cultural/linguistic nuances, do not produce an improved Japanese version.

---

## Zevero Product Terminology

The Zevero platform has an established Japanese UI, and customers read the translated strings
every day. If a translation invents its own wording for a feature that already has a shipped
Japanese name, the reader has no way to connect the two. The approved renderings live in
`references/zevero-glossary.md`, extracted from the product's `messages.po`.

### When to read the glossary

Read `references/zevero-glossary.md` before translating anything that touches the product:
release notes, feature announcements, UAT and QA material, support replies, onboarding and
training docs, meeting updates about the platform, customer-facing emails describing
functionality, or any text containing UI labels, screen names, or GHG Protocol category names.

Skip it only for content with no product surface at all (a purely HR or policy message, an
office logistics note). When unsure, read it; the cost of a missed term is higher than the
cost of a lookup.

### How to apply it

- **Glossary renderings are verbatim.** Do not re-derive them from the English, and do not
  "improve" them because a more natural Japanese word exists. A term already in the product
  UI is the correct term even when it reads oddly in isolation.
- **The glossary governs terms, not sentences.** Surrounding prose still follows all the
  register, Keigo, and cultural adaptation rules below. Drop the fixed term into a properly
  formed です/ます sentence.
- **Match the sense, not just the string.** Several entries depend on context: `Vehicle` is
  `社用車` as a registered entity but `車両` inside field labels; `Level` in an org or record
  context is `階層`, not `レベル`. Check the Note column before choosing.
- **Terms absent from the glossary**: translate them normally using the rules below, and list
  them in Translation Notes as candidates for the glossary. Never fabricate a glossary-style
  rendering and present it as approved.
- **Japanese → English**: use the glossary in reverse. `データ承認機能` in a Japanese source is
  the Period Lock feature, not a generic "data approval function"; render it with the English
  product name so the reader can find it in the UI.

### Flag non-literal terms

Many approved renderings deliberately diverge from the English. When one of these appears,
note it in Translation Notes with the English source, the Japanese used, and a one-line reason,
so the reader can tell a deliberate product term from a translation slip.

The highest-frequency traps, worth remembering even before opening the file:

| EN | JA | Not |
| --- | --- | --- |
| Period Lock | データ承認機能 | ~~期間ロック~~ |
| Scope 1 / 2 / 3 | Scope 1 / 2 / 3 (Latin) | ~~スコープ~~ |
| Reductions (product area) | 目標設定 | ~~削減~~ (that is the `Reduce` area) |
| Emission Factor Library | 金額ベース排出係数データベース | ~~排出係数ライブラリ~~ |
| Matched / Pending | 確定 / 未確定 | ~~マッチ済み~~ |
| Turnover | 離職率 | ~~売上高~~ |

---

## English → Japanese Rules

### 1. Register and Form

- Use です/ます (desu/masu) form throughout.
- Use formal Keigo appropriate to Japanese business communication.
- Apply standard Japanese business opening and closing phrases where contextually appropriate:
  - Opening: お世話になっております
  - Closing: 何卒よろしくお願いいたします
- Deadlines expressed as "end of week" must be rendered as **今週中** (not 今週末, which implies the weekend).

### 2. Cultural Adaptation

- If source text contains phrasing that is appropriate in a UK/Western context but would be
  considered overly direct, informal, or inappropriate in Japanese business culture, adapt it.
- Prefer face-saving, indirect constructions. For example:
  - Avoid: "You haven't done X yet."
  - Prefer: "ご対応いただけますと幸いです。" (We would be grateful if you could address this.)
- Use polite expressions of hope rather than direct imperatives.
- **Always flag any cultural adaptation in English** with a note explaining what was changed and why.

### 3. Refined Business Register

**Particle の (no) with proper nouns:**
- Remove の when connecting a proper noun (especially country/city names) to a technical or formal
  noun. Prefer the concise noun form.
  - Prefer: 英国ロンドン / 副次リージョン
  - Avoid: 英国のロンドン / 副次的なリージョン

**Connectives:**
- Prefer **につきましては** (ni tsukimashite wa) over に関しましては (ni kanshimashite wa) where
  appropriate for higher formality.

**Action verbs in formal documentation (FAQs, policy, guides):**
- Prefer **実施しております** (jisshi shite orimasu) over the general 行っております (okonatte orimasu).

### 4. Preserving Named References

- English section names, policy names, and named documents that are referenced specifically must
  be preserved in English within the Japanese translation (do not translate the names themselves).
  - Example: "Security & Data Hygiene Guide" remains in English when cited within Japanese text.
- Internal links, URLs, email addresses, Slack deep links, and Jira URLs must always be preserved
  verbatim — never translated or modified.

### 5. Output Format

Provide:
1. The Japanese translation.
2. A **Translation Notes** section in English listing:
   - Any cultural adaptations made and why.
   - Any register or style decisions worth noting.
   - Any ambiguities in the source text that affected translation choices.
   - Any glossary terms applied whose Japanese is not a literal rendering of the English.
   - Any product terms not found in the glossary, flagged as candidates to add.

---

## Japanese → English Rules

### 1. Accuracy and Register

- Translate the meaning accurately.
- Match the appropriate English register (formal / professional / polite) to the Japanese source.
- Use British English spelling and conventions throughout.

### 2. Nuance Flagging

Always provide a **Translation Notes** section in English after the translation, noting:

- **Keigo level**: Note if the source uses sonkeigo (respectful), kenjōgo (humble), or teineigo
  (polite), and what this implies about the relationship or context.
- **Implicit addressing**: Flag if the text implicitly addresses someone of higher standing without
  naming them, as this affects how an English response should be framed.
- **Indirect phrasing / rhetorical constructions**: Note any indirect requests, rhetorical questions,
  or softened refusals common in Japanese that may read differently in direct English translation.
- **Implicit urgency or obligation**: Japanese business language often encodes urgency or obligation
  subtly; flag these where present.

### 3. Do Not Produce an Improved Japanese Version

When translating Japanese → English, provide only the English translation and notes.
Do not rewrite, correct, or improve the Japanese source text.

---

## Zevero-Specific Conventions

These cover the company and its internal tooling. For anything inside the product itself, see
`references/zevero-glossary.md` — where the two overlap, the glossary wins, since it reflects
what is actually shipped in the UI.

- **Company name**: Zevero (ゼベロ in katakana if needed, but prefer Zevero in Roman script
  within Japanese text).
- **Internal tools**: Vanta, ManageEngine, Slack, Notion, Jira — preserve in Roman script.
- **Policy documents**: Preserve exact English names (e.g. "AI Usage and Governance Policy",
  "Security & Data Hygiene Guide", "Physical Security Guide").
- **Recurring contacts**: Ben Richardson (policy owner), Alan — names are never translated.
- **Key channels**: Slack is the primary internal communication channel; Notion hosts documentation.

---

## Prohibited Patterns

- Do not use em-dashes in any output. Use a semicolon or rephrase instead.
- Do not produce American English spellings (e.g. use "organisation" not "organization" in English
  output).
- Do not provide feedback or annotations in Japanese — all meta-commentary is in English only.