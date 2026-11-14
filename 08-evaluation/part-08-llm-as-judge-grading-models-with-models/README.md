# Evaluation · Part 8 of 11: LLM-as-Judge: Grading Models With Models

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. LLM-as-judge
2. Pointwise, pairwise and rubric design
3. Judge biases
4. Calibrate the judge to humans

## Key takeaways

- A judge is a model. Calibrate it.
- Pointwise gates, pairwise comparisons, binary rubrics
- Test position, length and self-preference
- Kappa and failure catch rate, not raw agreement

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_judge_prompt_for_support_answers.py` | A judge prompt for support answers | yes |
| `code/02_a_pairwise_judge_prompt.py` | A pairwise judge prompt | yes |
| `code/03_pairwise_judging_in_both_orders.py` | Pairwise judging in both orders | yes |
| `code/04_lab_catch_a_position_biased_judge.py` | Catch a position-biased judge | yes |
| `code/05_kappa_and_failure_catch_rate.py` | Kappa and failure catch rate | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_catch_a_position_biased_judge.py` prints:

```text
5 vs 6 single: A both: TIE
6 vs 5 single: A both: TIE
2 vs 9 single: B both: B
```

## Try it without a key

- [Google AI Studio](https://aistudio.google.com): A real model with temperature, top-p, thinking level and output length controls. Needs a Google account, no credit card. Do not paste private data: free-tier prompts may be used to improve Google products.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A team says: we use GPT as judge, so it is objective. What do you ask first?**

- A. What is its agreement with human labels?
- B. How many tokens does each call cost?
- C. Which settings does the judge use?

<details><summary>Answer</summary>

**A. What is its agreement with human labels?**. A judge is a model. Measure it against humans.

</details>

**2. Someone proposes: score every answer 1 to 10 and average. What is the main problem?**

- A. Averages are too slow to compute
- B. Uneven steps, and runs do not agree
- C. Ten levels give too little detail

<details><summary>Answer</summary>

**B. Uneven steps, and runs do not agree**. Ten-point scales drift. Use binary checks.

</details>

**3. Does using the biggest available model as judge solve its biases?**

- A. No, you still measure each bias
- B. Yes, size removes position bias
- C. Yes, if it grades its own family

<details><summary>Answer</summary>

**A. No, you still measure each bias**. Bigger judges still have biases. Measure them.

</details>

**4. 90% of your cases pass and your judge agrees with humans 90% of the time. Is it good?**

- A. Yes, 90 percent is a strong result
- B. Yes, if the judge is a big model
- C. Unknown: always-PASS also scores 90 percent

<details><summary>Answer</summary>

**C. Unknown: always-PASS also scores 90 percent**. Percent agreement alone hides an always-PASS judge.

</details>

## Say it in the interview

**Say it in the interview**

- Useful: scales judgement for the cost of tokens
- Narrow rubric, binary verdicts, measured against humans
- If code can check it, skip the judge

**Say it in the interview**

- Pointwise for gates, pairwise for choosing
- One quality, binary verdict, reason first
- Nuance means several binary checks, not one score

**Say it in the interview**

- Position: run both orders, else tie
- Length: check score against length
- Measure biases, do not assume them away

**Say it in the interview**

- Human agreement is the ceiling
- Stratify so failures are well represented
- Kappa, true negative rate, fresh sample

## Homework

- [ ] Write a binary judge rubric for one quality
- [ ] Add three new pairs to the bias lab
- [ ] Label ten answers with a partner, compare
- [ ] Compute kappa for an always-PASS judge
