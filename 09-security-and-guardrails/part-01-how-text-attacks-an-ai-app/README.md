# Security and Guardrails · Part 1 of 11: How Text Attacks an AI App

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Untrusted text
2. Prompt injection (direct)
3. Indirect prompt injection
4. Jailbreak

## Key takeaways

- Third-party text is data, never commands.
- Assume injection works; limit what it reaches.
- The user is the victim; check actions in code.
- Check the output, however it was produced.

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_fence_and_label_untrusted_text.py` | Fence and label untrusted text | with your API key |
| `code/02_lab_a_planted_ticket_meets_a_code_check.py` | A planted ticket meets a code check | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_a_planted_ticket_meets_a_code_check.py` prints:

```text
agent wants: close_all
change request: needs human
ran look
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your own tool fetched a log line. Is that text trusted?**

- A. Yes, our own tool produced it
- B. No, someone else wrote that text
- C. Only if the tool is read-only

<details><summary>Answer</summary>

**B. No, someone else wrote that text**. Who wrote the text decides trust, not who fetched it.

</details>

**2. Your prompt tells the model to ignore override attempts. What if it does not?**

- A. A control outside the model stops it
- B. Retry until the model refuses
- C. Add a firmer warning to the prompt

<details><summary>Answer</summary>

**A. A control outside the model stops it**. Only controls outside the model hold when it is fooled.

</details>

**3. With least privilege in place, is direct injection harmless?**

- A. No, the bot can still promise things
- B. Yes, the attacker gains nothing new
- C. Yes, if the system prompt is secret

<details><summary>Answer</summary>

**A. No, the bot can still promise things**. Least privilege limits actions, not what the bot promises.

</details>

**4. Our users are all employees. Is indirect injection still a risk?**

- A. Only if the app is public
- B. Yes, outsiders write what the agent reads
- C. No, employees are trusted users

<details><summary>Answer</summary>

**B. Yes, outsiders write what the agent reads**. Outsiders write the content your agent reads.

</details>

**5. We use a safety-tuned model. Are jailbreaks solved?**

- A. Yes, tuning teaches the model to refuse
- B. Only for prompts not in English
- C. No, universal jailbreak suffixes are published

<details><summary>Answer</summary>

**C. No, universal jailbreak suffixes are published**. Safety tuning helps, but never solves jailbreaks.

</details>

## Say it in the interview

**Untrusted text in the interview**

- No separate channel for instructions and data.
- Classify every text by where it came from.
- Authorization lives in code, not the prompt.

**Direct injection in the interview**

- Design for injection succeeding.
- User's permissions, checked tools, no secrets.
- Commitments come from tools, never free text.

**Indirect injection in the interview**

- The attacker never talks to my system.
- Fenced data, least-privilege tools.
- Code checks, human approval, sanitised output.

**Jailbreaks in the interview**

- Jailbreaks target the model's safety behaviour.
- Refusals are never the only layer.
- The output check ignores how they got there.

## Homework

- [ ] List every untrusted text source in one app.
- [ ] Add your own injected ticket to the lab.
- [ ] Write the direct injection answer from memory.
- [ ] Explain injection versus jailbreak in one minute.
