# Fine-tuning and Model Choice · Part 4 of 10: Choosing a Model You Can Defend

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Smallest model that passes
2. Public leaderboards and contamination
3. SLM vs LLM
4. Open weights

## Key takeaways

- Smallest model whose worst run passes
- Leaderboard shortlists; your golden set decides
- Small for narrow work, large for hard cases
- Check licence, then real total cost

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_lab_when_does_self_hosting_pay_off.py` | When does self-hosting pay off? | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/01_lab_when_does_self_hosting_pay_off.py` prints:

```text
GPU cost per hour: 4.0
Million tokens per hour: 4.5
Self-host per million: 0.889
Ignoring utilisation: 0.444
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. How do you prove a cheaper model is good enough?**

- A. Golden set, repeated runs, worst run passes
- B. It ranks high on a public leaderboard
- C. Its average score clears the bar

<details><summary>Answer</summary>

**A. Golden set, repeated runs, worst run passes**. Golden set, repeated runs, worst run clears the bar

</details>

**2. Why might the number one leaderboard model do worse for us?**

- A. Leaderboards update too slowly
- B. Contamination, task mismatch, ignored cost
- C. Top models refuse business tasks

<details><summary>Answer</summary>

**B. Contamination, task mismatch, ignored cost**. Contamination, task mismatch, and cost and latency ignored

</details>

**3. What would make a small model safe for a task?**

- A. Nothing; never use small models
- B. A longer and stricter system prompt
- C. Narrow task, grounding, validation, escalation

<details><summary>Answer</summary>

**C. Narrow task, grounding, validation, escalation**. Narrow task, grounding, code validation, escalation

</details>

**4. Is an open-weights model free to run?**

- A. No, GPUs, on-call and upgrades cost
- B. Yes, the weights cost nothing
- C. Only with a permissive licence

<details><summary>Answer</summary>

**A. No, GPUs, on-call and upgrades cost**. Free weights, paid running costs

</details>

## Say it in the interview

**Say it in the interview**

- A selection, not a pick
- Users meet the bad run, not the average
- Lowest total cost, human fallback included

**Say it in the interview**

- A shortlist, not a decision
- Judges favour length and position
- Decide on our own golden set

**Say it in the interview**

- Small is relative
- Narrow task, context does the lifting
- Big models earn cost on open-ended work

**Say it in the interview**

- Data control, no per-token bill, GPU costs
- First check: the licence
- Second check: total cost at your volume

## Homework

- [ ] Write a pass bar for one task
- [ ] Shortlist three models from a leaderboard
- [ ] Read one open-weights licence file
- [ ] Rerun the lab with lower utilisation
