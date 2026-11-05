# Classification

George is CCO of Zevero, a carbon-accounting platform. Two kinds of sender look alike and must not be confused. A vendor selling to Zevero is a pitch. A prospect, customer, or partner who might buy from or work with Zevero is never a pitch, even when the email is commercial.

## Pitch Signals

Classify as `pitch` only when at least two of these hold and no protective signal applies.

- George has never emailed the sender (step 4 of the procedure).
- The sender offers a product, service, agency, lead list, recruiting, funding, or "partnership" that is really a resale.
- Fake familiarity: `Re:` or `Fwd:` on a first message, "following up on my last email", "circling back", "bumping this to the top".
- Calendar-link asks: "15 minutes next week?", "worth a quick chat?", a Calendly or Chili Piper link.
- Personalisation tokens built from public data: "saw Zevero is hiring", "congrats on the raise", "noticed you're the CCO".
- Sequence tooling footprints: a sending domain that differs from the company name, an unsubscribe line in a 1:1-looking email, "if you're not the right person".

## Protective Signals

Any one of these forces `flag` or `leave`, never `pitch`.

- George has sent mail to this address or domain before.
- The sender's domain belongs to a Zevero customer, prospect, investor, or partner, or the email references an existing deal, contract, invoice, or meeting.
- A Zevero colleague (`@zevero.earth`) is on the thread.
- The email comes from a recruiter or candidate George engaged with, a journalist, or an event George is speaking at.
- Automated mail from tools Zevero already uses (HubSpot, Slack, Google, billing systems). These are `leave`, not `pitch`.

## Flag Signals

Classify as `flag` when a real person needs George specifically: a direct question, a decision, a deadline, an intro waiting on him, or a customer or prospect message. Newsletters, receipts, and CC-only FYIs are `leave`.

## Examples

```text
# BAD: classified as pitch because the subject says "partnership".
From: Priya Shah <priya@greenretail.co.uk>
Subject: Partnership on scope 3 reporting
Snippet: Following our call with Ben, we'd like to explore rolling Zevero out across our 40 suppliers...

# GOOD: flag. This is a prospect wanting to buy from Zevero, and it references a prior call.
```

```text
# BAD: left in inbox because it looks like a reply.
From: Tom <tom@getleadsflow.io>
Subject: Re: Zevero growth
Snippet: Bumping this up, George. We help climate SaaS teams book 20+ meetings a month...

# GOOD: pitch. There is no earlier message from George, and the "Re:" is a sequence trick.
```

```text
# BAD: classified as pitch because it is a stranger with a calendar link.
From: Hiro Tanaka <h.tanaka@mitsui-example.co.jp>
Subject: Introduction via Kenji
Snippet: Kenji suggested I reach out about decarbonisation reporting for our Japan subsidiaries...

# GOOD: flag. A named warm intro about buying carbon reporting is a lead, not a vendor.
```

When the signals conflict or the evidence is thin, choose `leave` and list the thread under "Borderline" in the report.
