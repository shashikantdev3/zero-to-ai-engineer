# Machine Learning and Deep Learning · Part 21 of 28: From Business Goals to Production ML

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Business objective versus ML objective
2. Batch versus online prediction
3. Training-serving skew
4. ML technical debt and glue code
5. Covariate shift is an assumption

## Key takeaways

- Turn the business goal into label, loss, metric
- Batch first; online when the decision demands it
- Train on served features; diff every field
- Risk lives in plumbing, not model code
- Drift is seen; covariate shift is assumed

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_diff_serving_against_training.py` | Diff serving against training | yes |
| `code/02_lab_catch_skew_in_a_few_lines.py` | Catch skew in a few lines | yes |
| `code/03_train_a_domain_classifier.py` | Train a domain classifier | yes |
| `code/04_turn_odds_into_weights.py` | Turn odds into weights | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_catch_skew_in_a_few_lines.py` prints:

```text
Same name: True
Rows compared: 3
Rows that disagree: 1
Share: 0.33
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. You are asked to design ticket routing. What do you pin down first?**

- A. The label, and who produces it
- B. Which model architecture to use
- C. How many GPUs to train on

<details><summary>Answer</summary>

**A. The label, and who produces it**. Settle the label before the model

</details>

**2. A retention team reads a churn list every Monday. Which setup fits?**

- A. A weekly batch table
- B. An online model per request
- C. A streaming model updated each second

<details><summary>Answer</summary>

**A. A weekly batch table**. Match freshness to how fast anyone acts

</details>

**3. Training and serving use identical feature names. Is skew ruled out?**

- A. Yes, same names mean same values
- B. No, only diffing the values tells you
- C. Yes, as long as the types match

<details><summary>Answer</summary>

**B. No, only diffing the values tells you**. Matching names prove nothing. Diff the values.

</details>

**4. Where does the paper's '5 percent ML code' remark actually appear?**

- A. As numbers in the famous figure
- B. In the famous figure's caption
- C. In a sentence about glue code

<details><summary>Answer</summary>

**C. In a sentence about glue code**. The figure has no numbers. Cite accurately.

</details>

**5. Inputs moved and no labels have arrived. Can you claim covariate shift?**

- A. Yes, the input drift proves it
- B. Only as an assumption
- C. Yes, if the domain AUC is high

<details><summary>Answer</summary>

**B. Only as an assumption**. Drift is observed. Covariate shift is assumed.

</details>

## Say it in the interview

**Say it in the interview**

- Separate the business goal from the ML objective
- Ask if a rules baseline is enough
- Most time goes to serving, fallback, monitoring

**Say it in the interview**

- Start from how fast the decision must change
- Online is something to justify, not the default
- Hybrid: heavy features batch, small model online

**Say it in the interview**

- Same name, different value, no error
- Train on served features, share the code
- Replay live requests and diff every field

**Say it in the interview**

- Most of an ML system is not the model
- The five percent line is about glue code
- Risk lives in the plumbing. Test it there.

**Say it in the interview**

- Without labels, I can only see data drift
- Covariate shift is assumed until labels arrive
- Shift: reweight. Concept drift: relabel, retrain.

## Homework

- [ ] Write one business goal and its observable label
- [ ] Name one batch and one online prediction
- [ ] Rerun the lab with a different default
- [ ] Rehearse the covariate shift answer, thirty seconds
