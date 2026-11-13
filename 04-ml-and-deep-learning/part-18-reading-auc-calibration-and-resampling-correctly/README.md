# Machine Learning and Deep Learning · Part 18 of 28: Reading AUC, Calibration and Resampling Correctly

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. ROC-AUC as a ranking probability, and AUC below 0.5
2. Expected calibration error and its binning bias
3. Correcting probabilities after resampling
4. When SMOTE hurts
5. Question drill: Evaluation additions

## Key takeaways

- AUC ranks pairs; below 0.5 is a bug
- Report bins, diagram, and Brier score
- Undo resampling with beta or recalibration
- Metric, weights, threshold before SMOTE
- Calibration fixes numbers, not rankings

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_auc_from_the_mann_whitney_u.py` | AUC from the Mann-Whitney U | yes |
| `code/02_pick_the_right_probability_column.py` | Pick the right probability column | yes |
| `code/03_lab_count_the_winning_pairs_by_hand.py` | Count the winning pairs by hand | yes |
| `code/04_an_ece_function.py` | An ECE function | yes |
| `code/05_same_data_different_bins.py` | Same data, different bins | yes |
| `code/06_undo_the_undersampling.py` | Undo the undersampling | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_count_the_winning_pairs_by_hand.py` prints:

```text
pairs: 12
AUC: 0.875
more negs: 0.875
flipped: 0.125
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your model's ROC-AUC is 0.3. What do you check first?**

- A. Whether you need more data
- B. Flipped labels or wrong probability column
- C. Whether the model learned nothing

<details><summary>Answer</summary>

**B. Flipped labels or wrong probability column**. AUC 0.3 means a flipped ranking, usually a bug

</details>

**2. A colleague reports ECE 0.02. What do you ask first?**

- A. How many bins, equal width or mass
- B. What the model's accuracy is
- C. Nothing, it is well calibrated

<details><summary>Answer</summary>

**A. How many bins, equal width or mass**. No binning scheme, no meaningful ECE

</details>

**3. A model trained on 50/50 undersampled data outputs 0.5. What does that mean?**

- A. The real probability is much lower
- B. Even odds of fraud
- C. The model is useless

<details><summary>Answer</summary>

**A. The real probability is much lower**. Sampled scores need mapping back before use

</details>

**4. Fraud comes in two distinct schemes. What is a SMOTE point between them?**

- A. A harmless copy of real fraud
- B. A typical example of both schemes
- C. Fraud no real scheme produces

<details><summary>Answer</summary>

**C. Fraud no real scheme produces**. Between modes, SMOTE invents fraud that never happens

</details>

**5. Will recalibrating a classifier improve its accuracy?**

- A. Only if you use isotonic regression
- B. No, ranking and argmax stay put
- C. Yes, better probabilities mean more accuracy

<details><summary>Answer</summary>

**B. No, ranking and argmax stay put**. Recalibration makes probabilities usable, not more accurate

</details>

## Say it in the interview

**How to answer it**

- The chance a positive outranks a negative
- Prevalence matters? I use the PR curve
- AUC 0.3: check labels and probability column

**How to answer it**

- ECE depends on bins and tends to read low
- Report bins, diagram, and Brier score
- Recalibration makes thresholds trustworthy

**How to answer it**

- Undersampling inflates rare-class probabilities
- Ranking survives; thresholds on the number break
- Closed-form fix, or recalibrate at the true rate

**How to answer it**

- SMOTE assumes one connected minority region
- Noise, high dimensions, and leakage break it
- Metric, weights, threshold, then resampling

## Homework

- [ ] Compute AUC by counting pairs by hand
- [ ] Negate scores, confirm one minus AUC
- [ ] Run ECE with two different bin counts
- [ ] Unsample 0.5 with beta 0.1
