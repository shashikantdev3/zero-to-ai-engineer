# Production and LLMOps · Part 2 of 38: Routing, Batching, Budgets and Real Cost

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Model routing and cascades
2. Batch it
3. Hard caps and budgets
4. Cost per resolved task

## Key takeaways

- Cheapest model that passes an external check
- No user waiting, use batch
- Reserve first, settle after
- Decide on cost per audited outcome

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_cascade_pieces.py` | The cascade pieces | yes |
| `code/02_escalate_only_the_failures.py` | Escalate only the failures | yes |
| `code/03_build_a_batch_file.py` | Build a batch file | yes |
| `code/04_a_reserve_and_settle_budget.py` | A reserve and settle budget | yes |
| `code/05_lab_check_after_versus_reserve_first.py` | Check after versus reserve first | yes |
| `code/06_compute_cost_per_resolved_task.py` | Compute cost per resolved task | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_check_after_versus_reserve_first.py` prints:

```text
all passed: True
spent, cents: 160
calls allowed: 10
max spend, cents: 80
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. In a cascade, what should decide whether the small model's answer is accepted?**

- A. An external check in code
- B. Whichever answer is longer
- C. The small model's own confidence

<details><summary>Answer</summary>

**A. An external check in code**. Never let the model grade its own confidence

</details>

**2. A user is waiting on screen for a reply. Should that call use the batch API?**

- A. Yes, it costs about half
- B. Yes, if the prompt is short
- C. No, batch is never for interactive work

<details><summary>Answer</summary>

**C. No, batch is never for interactive work**. A discount is useless if the user waits hours

</details>

**3. Twenty workers check the budget, all pass, and all spend. What prevents the overshoot?**

- A. Ask the prompt to be brief
- B. Reserve the worst case atomically first
- C. Check the budget after each call

<details><summary>Answer</summary>

**B. Reserve the worst case atomically first**. Reserve atomically before the call

</details>

**4. A team counts a ticket as resolved when the bot replies. What is wrong?**

- A. It can be gamed; audit resolution
- B. Nothing, a reply means resolved
- C. It should count tokens instead

<details><summary>Answer</summary>

**A. It can be gamed; audit resolution**. Resolved needs reopen checks and audits

</details>

## Say it in the interview

**Routing in one answer**

- Rules, then small, then large where evals win
- Pass a code check, or escalate
- Track quality per route, not just overall

**Batching in one answer**

- No user waiting, no real-time price
- Custom IDs: match results, retry failures
- Batch spares the real-time rate limit

**Budgets in one answer**

- Never trust a prompt with cost
- Reserve before, settle after
- Agent loops need a per-run budget

**Cost per outcome in one answer**

- Cheap per token can be costly per outcome
- Audited resolution, named denominator
- Forecast per token, decide per outcome

## Homework

- [ ] Build a stub cascade with a quote check
- [ ] Write a JSONL file with custom IDs
- [ ] Rerun the lab with new numbers
- [ ] Recompute cost per resolved ticket
