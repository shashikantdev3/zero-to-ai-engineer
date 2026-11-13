# Machine Learning and Deep Learning · Part 4 of 28: Precision, Recall, F1, AUC and Thresholds

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Precision and recall
2. F1 score
3. ROC curve and ROC-AUC
4. Precision-recall curve and PR-AUC
5. Decision threshold

## Key takeaways

- Precision: trust in flags. Recall: completeness.
- F1 punishes imbalance and needs a threshold.
- ROC-AUC: ranking quality, blind to prevalence.
- PR-AUC floor is the positive rate.
- Tune thresholds on validation, never on test.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_precision_and_recall_in_code.py` | Precision and Recall in Code | yes |
| `code/02_f1_and_f_beta_in_code.py` | F1 and F-beta in Code | yes |
| `code/03_lab_precision_recall_f1_by_hand.py` | Precision, Recall, F1 by Hand | yes |
| `code/04_roc_auc_needs_scores.py` | ROC-AUC Needs Scores | yes |
| `code/05_average_precision_in_code.py` | Average Precision in Code | yes |
| `code/06_a_cost_function_for_thresholds.py` | A Cost Function for Thresholds | yes |
| `code/07_tuning_the_threshold_by_cost.py` | Tuning the Threshold by Cost | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_precision_recall_f1_by_hand.py` prints:

```text
thr 0.85: P 1.00 R 0.25 F1 0.40
thr 0.65: P 1.00 R 0.75 F1 0.86
thr 0.45: P 0.80 R 1.00 F1 0.89
thr 0.0: P 0.50 R 1.00 F1 0.67
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Which metric can you make 100% with no skill at all?**

- A. Accuracy, by flagging nothing
- B. Precision, by flagging everything
- C. Recall, by flagging everything

<details><summary>Answer</summary>

**C. Recall, by flagging everything**. Flag everything: perfect recall, useless precision

</details>

**2. A model reports F1 = 0.8. What should you ask first?**

- A. Which learning rate was used?
- B. At which threshold?
- C. Nothing, F1 is threshold-free

<details><summary>Answer</summary>

**B. At which threshold?**. F1 always lives at one threshold

</details>

**3. Your ROC-AUC dropped when you used predict instead of predict_proba. Why?**

- A. Hard labels throw away the ranking
- B. The model itself got worse
- C. ROC-AUC needs a higher threshold

<details><summary>Answer</summary>

**A. Hard labels throw away the ranking**. ROC-AUC needs scores, never hard 0/1 labels

</details>

**4. Your fraud model has a PR-AUC of 0.4. Is that good?**

- A. No, random already scores 0.5
- B. It depends on the positive rate
- C. Yes, anything above 0.3 is good

<details><summary>Answer</summary>

**B. It depends on the positive rate**. PR-AUC means nothing without the base rate

</details>

**5. You tune the threshold on the test set. What happens?**

- A. Your test score becomes optimistic
- B. The model's weights change
- C. Nothing, test sets are for tuning

<details><summary>Answer</summary>

**A. Your test score becomes optimistic**. Tune on validation, freeze, test once

</details>

## Say it in the interview

**Precision and Recall**

- Precision is trust. Recall is completeness.
- The threshold trades one against the other.
- Fix capacity, maximise recall, keep a precision floor.

**F1 Score**

- Harmonic mean: no hiding a weak side.
- Known costs: F-beta, or better, direct cost.
- Always say macro or micro.

**ROC-AUC**

- Ranking quality: half random, one perfect.
- 1% FPR on a million: 10,000 alarms.
- Rare positives: compare on PR-AUC.

**PR-AUC**

- PR curve: what the review team feels.
- Baseline is prevalence, not 0.5.
- Report average precision; set threshold separately.

**Decision Threshold**

- The threshold is a business decision.
- Capacity: rank daily. Cost: minimise expected loss.
- The threshold decides who does the work.

## Homework

- [ ] Compute precision and recall by hand
- [ ] Rerun the lab with your own scores
- [ ] Compare ROC-AUC on scores versus hard labels
- [ ] State the PR-AUC baseline at 5% positives
