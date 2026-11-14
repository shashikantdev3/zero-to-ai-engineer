# Evaluation · Part 9 of 11: Judge Disputes, Judge Choice, and Hallucination

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Label disagreements: when users and the judge disagree
2. Choosing the judge model
3. Hallucination: plausible, not true
4. Why models hallucinate

## Key takeaways

- Disagreements go to experts, then rubric or product.
- Cheapest judge above the bar, pinned.
- Plausible is not true.
- Map each cause to a system fix.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_spotting_a_disagreement.py` | Spotting a Disagreement | yes |
| `code/02_sending_cases_to_experts.py` | Sending Cases to Experts | yes |
| `code/03_lab_pick_the_cheapest_passing_judge.py` | Pick the Cheapest Passing Judge | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_pick_the_cheapest_passing_judge.py` prints:

```text
big: kappa 0.82 clears
mid: kappa 0.79 clears
small: kappa 0.64 below
pick mid at $2.0/1k
```

## Try it without a key

- [Google AI Studio](https://aistudio.google.com): A real model with temperature, top-p, thinking level and output length controls. Needs a Google account, no credit card. Do not paste private data: free-tier prompts may be used to improve Google products.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your judge is calibrated and passes 90%, yet users are unhappy. Who is right?**

- A. Neither; experts label the disagreements
- B. The users, because they define good
- C. The judge, because it is calibrated

<details><summary>Answer</summary>

**A. Neither; experts label the disagreements**. Calibrated once is not calibrated forever.

</details>

**2. Which judge model should you choose for an eval suite run on every PR?**

- A. The strongest model available
- B. One from your system's model family
- C. Cheapest one that clears the human bar

<details><summary>Answer</summary>

**C. Cheapest one that clears the human bar**. Measure agreement first, then pay for the cheapest pass.

</details>

**3. Retrieval finds nothing relevant, and a strong model invents a policy clause. Why?**

- A. The model is simply too weak
- B. It produces plausible text without support
- C. A vendor bug that will be fixed soon

<details><summary>Answer</summary>

**B. It produces plausible text without support**. Design around hallucination; it is not a bug.

</details>

**4. An interviewer asks why models hallucinate. Which answer lands best?**

- A. Named mechanisms, each mapped to a fix
- B. Because the model is too small
- C. Because the model does not understand

<details><summary>Answer</summary>

**A. Named mechanisms, each mapped to a fix**. Name the mechanism, then name your system fix.

</details>

## Say it in the interview

**Label Disagreements, in One Breath**

- Neither the judge nor users win automatically.
- Experts label; fix the rubric or the product.
- Retest on new held-out cases.

**Choosing the Judge, in One Breath**

- Not by size: bigger judges are biased too.
- Cheapest judge that clears agreement and catch rate.
- Different family. Pinned version. Rescore on change.

**Hallucination, in One Breath**

- Trained for plausible, not true.
- Faithfulness: measured with groundedness checks.
- Answer from sources, cite, refuse when uncovered.

**Why Models Hallucinate, in One Breath**

- Objective, incentives, gaps, context.
- Work around gaps and context.
- Always give the model a way to refuse.

## Homework

- [ ] Write the disagreement filter from memory
- [ ] Change the lab bar; watch the pick
- [ ] One faithfulness, one factuality example
- [ ] Map four causes to four fixes
