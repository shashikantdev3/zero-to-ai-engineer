# Machine Learning and Deep Learning · Part 6 of 28: Honest Evaluation for Rare Classes

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Cross validation
2. Class imbalance
3. Resampling and SMOTE, training set only
4. Class weights
5. Data leakage

## Key takeaways

- k folds, mean and spread, pipeline inside
- Metrics and data before modelling
- Split first, resample train only
- Weight the loss; check PR-AUC moved
- Would I know this at prediction time?

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_five_stratified_folds_in_code.py` | Five stratified folds, in code | yes |
| `code/02_scores_spread_and_the_time_gap.py` | Scores, spread and the time gap | yes |
| `code/03_split_first_then_resample.py` | Split first, then resample | yes |
| `code/04_the_smote_pipeline.py` | The SMOTE pipeline | yes |
| `code/05_lab_watch_oversampling_leak_into_test.py` | Watch oversampling leak into test | yes |
| `code/06_balanced_weights_in_code.py` | Balanced weights, in code | yes |
| `code/07_the_scaler_sees_training_rows_only.py` | The scaler sees training rows only | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_watch_oversampling_leak_into_test.py` prints:

```text
test rate: 0.49
195 of 195 seen in train
fair rate: 0.03
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your CV score is 0.9 but production is 0.6. What most likely happened?**

- A. The model needs more layers
- B. Five folds were too few
- C. Leakage or ignored time order

<details><summary>Answer</summary>

**C. Leakage or ignored time order**. Big offline gap: suspect leakage or time order

</details>

**2. Fraud is 3% of your data. What do you change first?**

- A. How you measure the model
- B. Switch to a bigger model
- C. Apply SMOTE straight away

<details><summary>Answer</summary>

**A. How you measure the model**. Fix the metrics before touching the model

</details>

**3. You oversample fraud to 50/50, then split. What is the test set's fraud rate?**

- A. Still 3 percent, like production
- B. About 50 percent, not the real 3
- C. Zero, the copies stay in training

<details><summary>Answer</summary>

**B. About 50 percent, not the real 3**. Resample after the split, never before

</details>

**4. After class_weight='balanced', what usually changes most?**

- A. PR-AUC always improves a lot
- B. The threshold, more than the ranking
- C. The data gains more fraud rows

<details><summary>Answer</summary>

**B. The threshold, more than the ranking**. Weights shift scores; check PR-AUC really moved

</details>

**5. Your newest month looks almost fraud-free. What is the likely reason?**

- A. Its labels have not matured yet
- B. The model overfit that month
- C. Fraudsters took the month off

<details><summary>Answer</summary>

**A. Its labels have not matured yet**. New rows look clean until labels mature

</details>

## Say it in the interview

**Cross validation in the interview**

- Five folds, report mean and spread
- Stratify, group, or forward-chain with a gap
- Preprocessing lives inside the pipeline

**Class imbalance in the interview**

- A metrics and data problem first
- Weights, threshold, and better labels

**Resampling in the interview**

- Resampling is fine, on training data only
- Split first, resample in the fold, recalibrate

**Class weights in the interview**

- Weights change the loss, not the data
- Recalibrate, then threshold from the budget

**Data leakage in the interview**

- Brilliant offline, poor in production
- Would I know this at prediction time?

## Homework

- [ ] Run five-fold CV, print mean and spread
- [ ] Rerun the lab, splitting before copying
- [ ] Compare plain and balanced mean scores
- [ ] Check three features for prediction-time leaks
