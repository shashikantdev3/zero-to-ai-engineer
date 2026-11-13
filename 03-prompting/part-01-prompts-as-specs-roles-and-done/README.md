# Prompting · Part 1 of 10: Prompts as Specs, Roles, and Done

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Prompt as spec
2. System prompt and message roles
3. Instruction hierarchy
4. Define done

## Key takeaways

- Prompt is a spec, code enforces
- Stable in system, variable in user
- Hierarchy helps, code protects
- One definition of done, two uses

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_spec_for_ticket_triage.py` | A Spec for Ticket Triage | yes |
| `code/02_building_the_message_list.py` | Building the Message List | yes |
| `code/03_done_as_a_function.py` | Done as a Function | yes |
| `code/04_lab_test_your_done_check.py` | Test Your Done Check | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_test_your_done_check.py` prints:

```text
valid cite: True
fake cite: False
no cite: False
too long: False
miss ok: True
```

## Try it without a key

- [Google AI Studio](https://aistudio.google.com): A real model with temperature, top-p, thinking level and output length controls. Needs a Google account, no credit card. Do not paste private data: free-tier prompts may be used to improve Google products.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What makes a prompt good?**

- A. Finding the right magic words
- B. A complete, clear spec, checked by evals
- C. Making it as long as possible

<details><summary>Answer</summary>

**B. A complete, clear spec, checked by evals**. Wording does not prove quality. Evals do.

</details>

**2. Is the system prompt a security boundary?**

- A. No, the weighting is a trained tendency
- B. Yes, users cannot override it
- C. Only when it is versioned

<details><summary>Answer</summary>

**A. No, the weighting is a trained tendency**. Weighting is a tendency. Security lives in code.

</details>

**3. Does the instruction hierarchy solve prompt injection?**

- A. No, it lowers attacks but not to zero
- B. Yes, newer models block it fully
- C. Yes, as long as documents are fenced

<details><summary>Answer</summary>

**A. No, it lowers attacks but not to zero**. Lower attack rate, never zero

</details>

**4. When is a model's answer done?**

- A. When the model says it is finished
- B. When it looks right to you
- C. When it meets written, testable criteria

<details><summary>Answer</summary>

**C. When it meets written, testable criteria**. Vibes are not evals

</details>

## Say it in the interview

**Prompt as Spec, in the Interview**

- Write it like a ticket for a new engineer
- Complete beats clever
- The prompt guides, the code enforces

**Message Roles, in the Interview**

- Stable in system, variable in user
- Caching works, and trust stays clean
- Role names change. Check the docs.

**Hierarchy, in the Interview**

- Provider, developer, user. Documents are data.
- Use it, but do not rely on it
- Access and approvals live in code

**Define Done, in the Interview**

- No definition, no target, no test
- Sourced, cited, short, honest when unsure
- Prompt and test share one definition

## Homework

- [ ] Rewrite one prompt as a full spec
- [ ] Split it into system and user
- [ ] Turn done into a Python check
- [ ] Test five answers, one not found
