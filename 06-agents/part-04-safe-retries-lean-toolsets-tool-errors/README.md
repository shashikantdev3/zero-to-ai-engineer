# Agents and Tools · Part 4 of 26: Safe Retries, Lean Toolsets, Tool Errors

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Idempotency for side-effect tools
2. Too many tools: tool selection at scale
3. Four failure classes for tool errors

## Key takeaways

- Atomic key reservation turns retries into lookups
- Narrow tools; measure accuracy and cache hits
- Each error class goes to who can fix it

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_building_the_idempotency_key.py` | Building the idempotency key | yes |
| `code/02_reserve_first_then_act.py` | Reserve first, then act | yes |
| `code/03_same_key_same_result.py` | Same key, same result | yes |
| `code/04_lab_check_then_act_versus_atomic_reserve.py` | Check-then-act versus atomic reserve | yes |
| `code/05_naming_the_four_classes.py` | Naming the four classes | yes |
| `code/06_the_classify_function.py` | The classify function | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_check_then_act_versus_atomic_reserve.py` prints:

```text
check then act: 2
atomic reserve: 1
owner: retry 1
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A node crashed after the API call, before the checkpoint saved. What happens on resume?**

- A. The framework rolls it back
- B. The action runs again
- C. The checkpoint skips it safely

<details><summary>Answer</summary>

**B. The action runs again**. Checkpoints replay; downstream idempotency makes it safe

</details>

**2. Your wrong-tool rate doubled after adding the CRM tools. Why?**

- A. CRM tools are always unreliable
- B. The context window ran out
- C. More similar tools confuse selection

<details><summary>Answer</summary>

**C. More similar tools confuse selection**. Room in context is not accuracy; measure it

</details>

**3. Why did your agent spend six turns apologising for a 503?**

- A. The 503 was sent to the model
- B. The breaker opened too late
- C. The model needed the valid values

<details><summary>Answer</summary>

**A. The 503 was sent to the model**. Transient stays in the wrapper; semantic goes to the model

</details>

## Say it in the interview

**Idempotency in the interview**

- Every state-changing tool gets an idempotency key
- Reserve atomically, or two retries both act
- A timeout becomes a lookup, not a change

**Tool selection in the interview**

- Each agent or step gets only what it needs
- Route or retrieve; measure on my eval set
- Least privilege and good selection are one design

**Tool errors in the interview**

- Transient: retry inside the tool
- Semantic to the model; permanent never retried
- A rising retry average means contract drift

## Homework

- [ ] Run the lab with three retries
- [ ] Change one argument; confirm the key changes
- [ ] Write a structured semantic error
- [ ] Split one agent's tools by workflow step
