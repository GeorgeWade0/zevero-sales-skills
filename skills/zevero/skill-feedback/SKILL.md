---
name: skill-feedback
description: Capture quick feedback on a Zevero sales skill output the moment it's used - "that was great", "that was off", "improve", "this was wrong", thumbs up or down. Use when the user reacts to a skill's output with praise or criticism, or replies "improve" after one.
---

# Skill feedback

Turn a one-word reaction into feedback the team can act on, without slowing the rep down.

1. **Identify the skill.** Work out which `zevero-sales*` skill produced the output being reacted to. If it isn't clear, ask in one line.
2. **Positive feedback ("great", 👍):**
   - Thank them in one line.
   - Ask whether the output is worth saving as a gold-standard example: "Want me to save this as an example for the skill? I'll strip customer details first."
   - On a yes, file it with `request-skill` as an improvement titled `[Example] <skill>: <short description>`, with the anonymised output in the body.
3. **Negative feedback ("off", "wrong", "improve", 👎):**
   - Ask one question: "What should it have done instead?"
   - Then hand off to `request-skill` as an improvement, filling in the skill name, what they asked, what they got and what they expected.
4. **Fix the current output** if the rep wants it fixed now. Filing feedback shouldn't block their work.

Never include customer names, contact details or prices in anything filed.
