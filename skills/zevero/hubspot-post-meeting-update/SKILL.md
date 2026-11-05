---
name: hubspot-post-meeting-update
description: >
  Update HubSpot after a meeting by pulling context from Google Calendar and Gmail, then logging notes and updating deal stages. Use this skill whenever someone says "update HubSpot after my meeting", "log my call with [company]", "post-meeting CRM update", "update the deal after my meeting with [person]", "sync my meeting notes to HubSpot", "I just had a call with [company]", "log meeting notes for [deal]", "CRM update after call", "update HubSpot for [company]", or any variation involving meeting/call follow-up and HubSpot/CRM. Also trigger when users mention "meeting follow-up", "after my call", "debrief [company]", or "what happened in my meeting with [company]" if HubSpot context is relevant. This skill works for any team member, not just a specific person.
---

# Post-Meeting HubSpot Update

This skill automates the tedious but critical task of updating HubSpot after meetings. Most CRM data goes stale because people forget to log notes or update deal stages after calls — this skill closes that gap by pulling context from Calendar and Email automatically, so the user only needs to add what's missing.

## Workflow

### Step 1: Identify the meeting context

When the user mentions a company, person, or deal name:

1. Search HubSpot for the company, contact, or deal using `search_crm_objects`. Try all three object types (companies, contacts, deals) to build the full picture.
2. If multiple matches exist, ask the user to confirm which one they mean.
3. Retrieve the deal's current stage, close date, amount, and associated contacts so you have baseline context.

The goal is to understand the current state of the relationship before logging anything new.

### Step 2: Gather meeting context automatically

Pull context from connected tools to reduce the burden on the user:

1. **Google Calendar**: Use `gcal_list_events` to search for recent meetings (past 7 days) that mention the company or contact name. Set `condenseEventDetails` to `false` so you get the full event detail including attachments. Extract the meeting title, date/time, attendees, and any description or agenda.

2. **Gemini Meeting Notes** (critical step): Google Meet automatically generates meeting notes via Gemini and attaches them as a Google Doc to the calendar event. After retrieving the calendar event, check the `attachments` array for any doc with a title containing "Notes by Gemini" or similar. If found:
   - Extract the `fileId` from the attachment
   - Use `google_drive_fetch` with that document ID to retrieve the full transcript/notes
   - These Gemini notes typically contain a structured summary, detailed discussion points, and suggested next steps — this is the richest source of meeting context available and should be the primary basis for the HubSpot note

   This is often the most valuable data source because it captures the actual conversation, not just the calendar metadata. Always check for it before falling back to asking the user to recount the meeting from memory.

3. **Gmail**: Use `gmail_search_messages` to find recent email threads (past 14 days) involving the contact's email address or company domain. Summarise key discussion points — don't dump raw emails.

4. Present a brief summary of what you found:
   - "I found a meeting on [date] with [attendees] titled '[title]'"
   - "Gemini captured notes — here's the summary: [key points]"
   - "Recent email threads cover: [topic 1], [topic 2]"

This context helps the user recall what happened and ensures nothing gets missed. When Gemini notes are available, you already have most of what's needed — the user only needs to confirm accuracy and add anything Gemini missed.

### Step 3: Ask the user for meeting outcomes

How much you need to ask depends on what data you already have:

**If Gemini notes were found:** You already have a detailed summary, discussion points, and suggested next steps. Present a draft note to the user and ask:
1. **Does this look accurate?** Let them correct anything Gemini got wrong.
2. **Should the deal stage change?** If there's an active deal, show the current stage and ask if it should move forward, stay, or go backwards.
3. **Anything Gemini missed?** One open question to capture anything not in the transcript.

**If no Gemini notes were found:** Fall back to asking more directly:
1. **What were the key outcomes or decisions?** (open text)
2. **Should the deal stage change?** If there's an active deal, show the current stage and ask if it should move forward, stay, or go backwards. Present the available stages as options.
3. **Any change to expected close date or amount?** Only ask if there's an active deal.
4. **Any follow-up actions needed?** Capture next steps so they can be referenced later.

Keep the questions concise. If the user gives a brief answer, that's fine — not every meeting needs a novel.

### Step 4: Compose and log the HubSpot note

Create a structured note using this format:

```
Meeting: [Title from Calendar or user input]
Date: [Date]
Attendees: [From Calendar]

Summary:
[User's key outcomes + context from emails if relevant]

Next Steps:
- [Action items from user]

[Deal update: Stage moved from X to Y / Close date updated to Z — if applicable]
```

Use `manage_crm_objects` to create a note (engagement) associated with the relevant contact, company, AND deal. Associating with all three ensures the note appears everywhere it should in HubSpot.

### Step 5: Update deal properties (if confirmed)

If the user confirmed a stage change, close date change, or amount change:

1. Show a confirmation table with current vs. proposed values
2. Only update after explicit approval
3. Use `manage_crm_objects` to update the deal

### Step 6: Confirm completion

Give the user a brief summary of what was logged and updated, with a direct link to the HubSpot record so they can verify.

## Important Notes

- **Don't over-ask.** If the user gives you everything in their initial message ("just had a great call with Acme, they want to proceed, move to negotiation stage"), skip the questions and go straight to logging.
- **Respect the user's time.** The whole point of this skill is speed. If you can infer the meeting from Calendar data, do it — don't ask the user to repeat information that's already available.
- **Work for any team member.** Use `get_user_details` or `search_owners` if you need to identify the current user's HubSpot owner ID, rather than hardcoding any specific person.
- **Handle missing tools gracefully.** If Google Calendar or Gmail isn't connected, skip those steps and ask the user for context directly. Don't fail just because one data source is unavailable.
