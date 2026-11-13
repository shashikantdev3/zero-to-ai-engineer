# Machine Learning and Deep Learning · Part 7 of 28: Features, Scaling, Tuning and Three Classic Models

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Feature engineering
2. Feature scaling
3. Hyperparameter tuning
4. Linear regression
5. Logistic regression
6. k-nearest neighbours (k-NN)

## Key takeaways

- Past-only features, same code in serving
- Scale for distance models, fit on train
- Random search, CV, untouched test set
- Weighted sum, squared error, ridge
- Sigmoid probability, recalibrate after weighting
- Closest examples vote, scale first

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_past_only_average.py` | A Past-Only Average | yes |
| `code/02_no_missing_values_no_infinity.py` | No Missing Values, No Infinity | yes |
| `code/03_fit_on_train_apply_everywhere.py` | Fit on Train, Apply Everywhere | yes |
| `code/04_a_pipeline_to_tune.py` | A Pipeline to Tune | yes |
| `code/05_random_search_with_time_splits.py` | Random Search with Time Splits | yes |
| `code/06_plain_versus_ridge.py` | Plain Versus Ridge | yes |
| `code/07_data_for_a_classifier.py` | Data for a Classifier | yes |
| `code/08_balanced_weights_then_calibrate.py` | Balanced Weights, Then Calibrate | yes |
| `code/09_scaled_k_nn_in_a_pipeline.py` | Scaled k-NN in a Pipeline | yes |
| `code/10_lab_unscaled_neighbours_mislead.py` | Unscaled Neighbours Mislead | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/10_lab_unscaled_neighbours_mislead.py` prints:

```text
query age 59
raw B age 24
scaled A age 61
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your average-spend feature uses each customer's full history. What is wrong?**

- A. It should use the median instead
- B. Nothing, more data is always better
- C. It uses future data, so it leaks

<details><summary>Answer</summary>

**C. It uses future data, so it leaks**. Past data only, computed the same at serving

</details>

**2. You scaled features for a random forest and the score rose. Why?**

- A. Probably noise, trees ignore scale
- B. Scaling always helps every model
- C. Forests use distances between points

<details><summary>Answer</summary>

**A. Probably noise, trees ignore scale**. Trees split on thresholds, scale is irrelevant

</details>

**3. You tried 300 configs. Is the best CV score your production score?**

- A. Yes, cross validation is unbiased
- B. No, it is optimistically biased
- C. Yes, if the folds are large

<details><summary>Answer</summary>

**B. No, it is optimistically biased**. Best-of-many scores flatter you

</details>

**4. Can linear regression model a yes-or-no outcome well?**

- A. Yes, if the features are scaled
- B. No, use logistic regression
- C. Yes, round predictions to zero or one

<details><summary>Answer</summary>

**B. No, use logistic regression**. Yes or no targets need logistic regression

</details>

**5. Is logistic regression always well calibrated?**

- A. Yes, unless the dataset is huge
- B. Yes, sigmoid outputs are true probabilities
- C. No, class weights shift its probabilities

<details><summary>Answer</summary>

**C. No, class weights shift its probabilities**. Sigmoid output is not automatically calibrated

</details>

**6. Your k-NN neighbours all have the same income. Why?**

- A. The features were not scaled
- B. k is far too large
- C. The dataset has too few rows

<details><summary>Answer</summary>

**A. The features were not scaled**. Unscaled distance follows the biggest units

</details>

## Say it in the interview

**Feature Engineering in an Interview**

- Features usually beat model choice
- Past-only aggregates, encoding inside folds
- One pipeline for training and serving

**Feature Scaling in an Interview**

- Distances, gradients, penalties need scaling
- Trees and boosting do not care
- Fit on train, apply unchanged everywhere

**Tuning in an Interview**

- Defaults first, then random search
- Few settings matter, random explores them
- Report on a never-used test set

**Linear Regression in an Interview**

- Weighted sum, squared error, closed form
- Each weight: change per unit
- Linear, outlier-sensitive, ridge for correlation

**Logistic Regression in an Interview**

- Baseline: weighted sum, sigmoid, log loss
- Log-odds weights, linear boundary
- Recalibrate, scale, tune C

**k-NN in an Interview**

- Store data, closest examples vote
- Slow queries, so scale and index
- k of one memorises, huge k predicts majority

## Homework

- [ ] Build a past-only average feature on toy data
- [ ] Fit a scaler on train, apply to validation
- [ ] Rerun the lab with different scaling
- [ ] Explain C in two written sentences
