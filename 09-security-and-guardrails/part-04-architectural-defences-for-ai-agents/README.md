# Security and Guardrails · Part 4 of 11: Architectural Defences for AI Agents

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Trust boundary
2. Least privilege
3. Authorization checked in code
4. Spotlighting and fencing retrieved content

## Key takeaways

- The line sits between the model and what matters
- Minimum permissions make injection a non-event
- Prompts guide, code enforces
- Fencing is a hint, beside code controls

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_sample_orders_and_a_refund_cap.py` | Sample orders and a refund cap | yes |
| `code/02_the_refund_tool_checks_first.py` | The refund tool checks first | yes |
| `code/03_trying_three_model_proposals.py` | Trying three model proposals | yes |
| `code/04_lab_lab_the_model_proposes_code_decides.py` | Lab: the model proposes, code decides | yes |
| `code/05_a_fence_for_retrieved_text.py` | A fence for retrieved text | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_lab_the_model_proposes_code_decides.py` prints:

```text
allow
deny: not your order
deny: bad amount
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your model is hosted inside your private network. Is it inside the trust boundary?**

- A. Yes, the network makes it trusted
- B. No, it still reads untrusted text
- C. Yes, if the firewall blocks the internet

<details><summary>Answer</summary>

**B. No, it still reads untrusted text**. Network location is not trust. Ask what text it reads.

</details>

**2. A team uses one powerful service principal for every user. What is the problem?**

- A. The agent can read every user's data
- B. It makes the agent much slower
- C. Service principals cannot call Graph

<details><summary>Answer</summary>

**A. The agent can read every user's data**. One god-mode identity lets every injection reach everyone

</details>

**3. The system prompt says 'only refund eligible orders'. What enforces it when the model is wrong?**

- A. The system prompt, it has top priority
- B. The model's safety training
- C. Nothing, unless the tool checks in code

<details><summary>Answer</summary>

**C. Nothing, unless the tool checks in code**. Prompts guide, code enforces

</details>

**4. Should retrieved documents go in the system prompt, the most trusted spot?**

- A. No, that gives documents system authority
- B. Yes, the model reads them more carefully
- C. Yes, as long as they are fenced

<details><summary>Answer</summary>

**A. No, that gives documents system authority**. Retrieved text is data. Never give it system trust.

</details>

## Say it in the interview

**Trust boundary, in one answer**

- The model is an untrusted component
- The boundary sits between model and what matters
- The model proposes, code decides

**Least privilege, in one answer**

- Least privilege makes injection a non-event
- Narrow tools, narrow scopes, never god mode
- The agent that reads never acts

**Authorization in code, in one answer**

- Prompts are not an authorization system
- The tool checks token, ownership, eligibility, limit
- Prompts guide, code enforces

**Spotlighting, in one answer**

- Retrieved content is data, never system trust
- Spotlighting measurably reduces injection success
- A hint reduces risk. Code gates the action.

## Homework

- [ ] Draw every crossing in one AI system
- [ ] Type the refund tool and add a check
- [ ] Find one permission you could narrow
- [ ] Fence a doc that tries to close the tag
