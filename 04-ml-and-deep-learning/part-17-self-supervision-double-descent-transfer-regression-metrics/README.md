# Machine Learning and Deep Learning · Part 17 of 28: Self-Supervision, Double Descent, Transfer, Regression Metrics

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Self-supervised learning
2. Double descent
3. Transfer learning: feature extraction, linear probing and fine-tuning
4. Regression metrics: MAE, RMSE, R squared and MAPE

## Key takeaways

- Labels from the data: the next token.
- Measure validation error across model sizes.
- Probe first, LoRA next, full fine-tune last.
- Match metric to error cost; R squared can dip.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_next_token_labels_for_free.py` | Next-Token Labels for Free | yes |
| `code/02_freeze_then_add_a_probe.py` | Freeze, Then Add a Probe | yes |
| `code/03_regression_metrics_in_scikit_learn.py` | Regression Metrics in scikit-learn | yes |
| `code/04_lab_metrics_by_hand_one_big_miss.py` | Metrics by Hand, One Big Miss | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_metrics_by_hand_one_big_miss.py` prints:

```text
MAE:  3.00
RMSE: 5.42
R2:   -2.67
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. If LLM pretraining is unsupervised, where does its loss come from?**

- A. Cross-entropy on the next token
- B. Human ratings of each sentence
- C. Nowhere, pretraining has no loss

<details><summary>Answer</summary>

**A. Cross-entropy on the next token**. Self-made labels, but a real supervised loss.

</details>

**2. If double descent exists, is regularisation now useless?**

- A. Yes, bias variance no longer holds
- B. Yes, size fixes overfitting
- C. No, it can reduce the peak

<details><summary>Answer</summary>

**C. No, it can reduce the peak**. The decomposition holds; regularisation can shrink the peak.

</details>

**3. When can full fine-tuning do worse than a linear probe?**

- A. Small data or shifted test data
- B. Never, fine-tuning always wins
- C. Only when training runs too long

<details><summary>Answer</summary>

**A. Small data or shifted test data**. Fine-tuning can distort features; probes can win.

</details>

**4. Can R squared be negative on held-out data?**

- A. Only if targets contain zeros
- B. Yes, worse than predicting the mean
- C. No, it stays between 0 and 1

<details><summary>Answer</summary>

**B. Yes, worse than predicting the mean**. Negative R squared: worse than the mean.

</details>

## Say it in the interview

**Say It: Self-Supervised Learning**

- The label is cut from the data itself.
- The label is simply the next token.
- Pretrain at web scale, then teach behaviour.

**Say It: Double Descent**

- The U-curve still fits small models.
- Error peaks at memorising, then drops again.
- Measure across sizes. Observation, not law.

**Say It: Transfer Learning**

- Cheapest first: embeddings or a linear probe.
- Then LoRA. Full fine-tuning comes last.
- Evaluate on held-out labels, not smoke tests.

**Say It: Regression Metrics**

- Pick the metric from how errors hurt.
- R squared can go negative on test data.
- Avoid MAPE when targets sit near zero.

## Homework

- [ ] Shift a token list into inputs, targets.
- [ ] List transfer levels from memory, cheapest first.
- [ ] Shrink the big miss; watch R squared.
- [ ] Write the double descent answer, three sentences.
