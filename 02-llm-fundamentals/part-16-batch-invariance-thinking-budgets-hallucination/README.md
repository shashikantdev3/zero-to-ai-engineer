# LLM Fundamentals · Part 16 of 18: Batch Invariance, Thinking Budgets, Hallucination

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Batch invariance
2. Test-time compute scaling
3. Question drill: Decoding and sampling
4. Hallucination

## Key takeaways

- Changing batches, not atomics, cause temp zero drift
- Tune the thinking budget; more can hurt
- Fixed batch repeats; determinism costs throughput
- Check retrieval before blaming the model

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_lab_same_numbers_different_grouping.py` | Same numbers, different grouping | yes |
| `code/02_sweep_the_effort_do_not_max_it.py` | Sweep the effort, do not max it | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/01_lab_same_numbers_different_grouping.py` prints:

```text
groups of 1: 0.9999999999999999
groups of 5: 1.0
rerun same: True
1 vs 5 equal: False
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Temperature 0 varies on a shared API. What is the main trigger?**

- A. The API hides a random seed
- B. Batch size shifts with server load
- C. Random GPU atomic adds every run

<details><summary>Answer</summary>

**B. Batch size shifts with server load**. Load changes the batch; kernels are not batch invariant

</details>

**2. Accuracy fell when you raised the reasoning budget. Why?**

- A. Higher effort ignores the prompt
- B. The model ran out of context
- C. Past some length, reasoning can hurt

<details><summary>Answer</summary>

**C. Past some length, reasoning can hurt**. More reasoning can hurt; measure the limit per task

</details>

**3. One request, temperature 0, quiet GPU. Is it repeatable?**

- A. Usually yes, for a fixed setup
- B. No, GPU atomics randomise each run
- C. Only if you pass a seed

<details><summary>Answer</summary>

**A. Usually yes, for a fixed setup**. Fixed batch, fixed path, same output

</details>

**4. Will setting temperature to 0 stop hallucinations?**

- A. No, it repeats the same wrong answer
- B. Yes, it removes randomness from facts
- C. Yes, if you also set a seed

<details><summary>Answer</summary>

**A. No, it repeats the same wrong answer**. Same wrong answer, every time; fix the evidence

</details>

## Say it in the interview

**Batch invariance in the interview**

- Fixed batch is repeatable; atomics are not it
- Load changes the batch; near ties flip
- Assume variation; guarantee with schemas and code

**Test-time compute in the interview**

- Second axis: more compute per question
- Helps hard problems; more is not always better
- Tune on evals with cost and latency

**Hallucination in the interview**

- Trained for plausible, rewarded for guessing
- First ask: was the evidence there?
- Ground, cite, check, refuse, review

## Homework

- [ ] Rerun the lab with groups of two
- [ ] Sketch an effort sweep for your task
- [ ] Add a refusal path to one prompt
- [ ] Write batch invariance in four sentences
