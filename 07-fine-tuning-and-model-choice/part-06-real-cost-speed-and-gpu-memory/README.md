# Fine-tuning and Model Choice · Part 6 of 10: Real Cost, Speed and GPU Memory

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Cost per resolution
2. Provisioned throughput, pay-as-you-go and batch
3. Prefill and decode, TTFT and TPOT
4. GPU memory budget

## Key takeaways

- Choose models on cost per resolved task.
- Reserve only above break-even utilisation.
- Prefill sets TTFT. Decode is bandwidth-bound.
- KV cache, not weights, limits concurrent users.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_cost_per_ticket_in_code.py` | Cost per ticket in code | yes |
| `code/02_lab_do_the_memory_budget_yourself.py` | Do the memory budget yourself | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_do_the_memory_budget_yourself.py` prints:

```text
usable GB: 72
weights GB: 16
KV cache GB: 50
KV tokens: 381,470
seqs of 3000: 127
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Model A costs 0.3 cents per ticket, model B costs 2 cents. Which is cheaper?**

- A. Depends on resolve rate and human cost
- B. Model B, quality always pays off
- C. Model A, its token price is lower

<details><summary>Answer</summary>

**A. Depends on resolve rate and human cost**. Compare total cost per resolved task, not token price.

</details>

**2. At high volume, is reserved capacity always cheaper than pay-as-you-go?**

- A. Only above break-even utilisation
- B. No, pay-as-you-go always wins
- C. Yes, always at scale

<details><summary>Answer</summary>

**A. Only above break-even utilisation**. Reserved capacity is only cheaper if it is used.

</details>

**3. Decode is slow. Will a GPU with more raw compute fix it?**

- A. Yes, more compute means faster decode
- B. Only if the prompts are short
- C. Not usually, decode is bandwidth-bound

<details><summary>Answer</summary>

**C. Not usually, decode is bandwidth-bound**. Slow decode is a bandwidth and batching problem.

</details>

**4. An 8B model fits on your GPU. How many users at 8k context can you serve?**

- A. As many as you like, it fits
- B. Work it out from KV cache maths
- C. Always 125, like before

<details><summary>Answer</summary>

**B. Work it out from KV cache maths**. Fitting the weights is not enough. Do the KV maths.

</details>

## Say it in the interview

**Say it in the interview**

- Per-token price is the wrong unit.
- The pricier model can be cheaper per ticket.
- Define resolved. Price reopens separately.

**Say it in the interview**

- Pricing mode follows traffic shape.
- Idle reserved capacity is pure waste.
- If it can wait, batch it.

**Say it in the interview**

- Prefill is compute-heavy and sets TTFT.
- Decode is limited by memory bandwidth.
- Batching, speculative decoding, chunked prefill.

**Say it in the interview**

- Size serving as a memory budget.
- KV cache decides how many users fit.
- At peak, KV cache runs out first.

## Homework

- [ ] Run cost_per_ticket with three resolve rates.
- [ ] Define 'resolved' in one line.
- [ ] Write the break-even formula from memory.
- [ ] Rerun the lab at 8,000 tokens.
