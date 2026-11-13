# Machine Learning and Deep Learning · Part 19 of 28: Calibration, F1 Averages and Feature Encoding

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Recalibration methods: Platt, isotonic and temperature scaling
2. Macro, micro and weighted averaging
3. Cyclical encoding
4. Missing-value indicators
5. High-cardinality categorical encoding

## Key takeaways

- Platt, isotonic, temperature, always on held-out data.
- Report macro plus the per-class table.
- Encode cycles with sine and cosine together.
- Impute inside the pipeline, keep a missing flag.
- Cross-fit, smooth, and plan for unseen values.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_isotonic_calibration_in_scikit_learn.py` | Isotonic calibration in scikit-learn | yes |
| `code/02_temperature_scaling_in_pytorch.py` | Temperature scaling in PyTorch | yes |
| `code/03_three_averages_from_one_metric.py` | Three averages from one metric | yes |
| `code/04_encoding_the_hour_in_pandas.py` | Encoding the hour in pandas | yes |
| `code/05_lab_clock_distances_in_pure_python.py` | Clock distances in pure Python | yes |
| `code/06_median_fill_plus_a_was_missing_flag.py` | Median fill plus a was-missing flag | yes |
| `code/07_targetencoder_in_scikit_learn.py` | TargetEncoder in scikit-learn | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_clock_distances_in_pure_python.py` prints:

```text
raw gap 23 to 0: 23
circle gap 23 to 0: 0.261
circle gap 12 to 0: 2.000
sin 3h, 9h: 0.707 0.707
cos 3h, 9h: 0.707 -0.707
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does calibration change ROC-AUC?**

- A. Barely, monotone maps keep the ranking
- B. Yes, it always raises AUC
- C. Yes, it reshuffles the whole ranking

<details><summary>Answer</summary>

**A. Barely, monotone maps keep the ranking**. Monotone maps keep ranking; isotonic ties nudge AUC.

</details>

**2. On imbalanced data, what can weighted F1 hide?**

- A. Nothing, it is the fairest average
- B. Poor scores on the small classes
- C. Poor scores on the largest class

<details><summary>Answer</summary>

**B. Poor scores on the small classes**. Weighted F1 hides small classes that fail.

</details>

**3. With only the sine, which two hours look identical?**

- A. Hours 3 and 9
- B. Hours 3 and 15
- C. Hours 6 and 18

<details><summary>Answer</summary>

**A. Hours 3 and 9**. Sine alone collides; the cosine separates.

</details>

**4. You imputed before the split. Whose median did you use?**

- A. Only the training rows
- B. The model's own estimate
- C. Everyone's, test rows included

<details><summary>Answer</summary>

**C. Everyone's, test rows included**. Split first, then fit the imputer.

</details>

**5. Target encoding before the split: great validation, poor production. Why?**

- A. Production data is always noisier
- B. Each row's encoding contains its own label
- C. The model needs more trees

<details><summary>Answer</summary>

**B. Each row's encoding contains its own label**. Split first, then encode inside folds.

</details>

## Say it in the interview

**Recalibration in the interview**

- Same accuracy? Calibration decides which I trust.
- Platt small, isotonic large, temperature for networks.
- Fit on one split, check on another.

**Averaging in the interview**

- Macro: an ignored rare class pulls it down.
- Micro tracks big classes, equals accuracy.
- Report macro plus the per-class table.

**Cyclical encoding in the interview**

- Encode the cycle, not the raw number.
- Sine and cosine; sine alone collides.
- Trees cope; the circle rarely hurts.

**Missing values in the interview**

- Impute, and add a was-missing flag.
- Imputer inside the pipeline, fit on train.
- HistGradientBoosting handles NaN natively.

**High cardinality in the interview**

- Too wide for one-hot: target, hash, embed.
- Cross-fit inside folds, smooth rare categories.
- An other bucket for unseen values.

## Homework

- [ ] Run the clock lab with your own hours.
- [ ] Compute macro and micro F1 by hand.
- [ ] Add a missing flag inside a pipeline.
- [ ] Explain target-encoding leakage in three sentences.
