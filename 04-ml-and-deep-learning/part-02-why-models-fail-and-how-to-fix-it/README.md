# Machine Learning and Deep Learning · Part 2 of 28: Why Models Fail, and How to Fix It

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Overfitting and underfitting
2. Regularisation, L1 and L2
3. Dropout
4. Early stopping
5. Loss functions

## Key takeaways

- Overfitting is a gap. Check leakage first.
- L2 shrinks, L1 zeroes. Smaller C, stronger.
- Dropout in training only. Call eval().
- Stop at best. Keep the test set untouched.
- Train on the loss, report the metric

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_l1_and_l2_in_scikit_learn.py` | L1 and L2 in scikit-learn | yes |
| `code/02_dropout_in_pytorch.py` | Dropout in PyTorch | yes |
| `code/03_early_stopping_in_lightgbm.py` | Early stopping in LightGBM | yes |
| `code/04_the_scikit_learn_version.py` | The scikit-learn version | yes |
| `code/05_weighted_cross_entropy_in_pytorch.py` | Weighted cross-entropy in PyTorch | yes |
| `code/06_lab_feel_the_loss_in_plain_python.py` | Feel the loss in plain Python | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_feel_the_loss_in_plain_python.py` prints:

```text
p true 0.9: 0.105
p true 0.5: 0.693
p true 0.01: 4.605
MSE with one outlier: 25.75
MAE with one outlier: 3.25
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Train and validation scores match, but production is bad. Overfitting?**

- A. Yes, the model is too big
- B. No, distribution shift or shared leakage
- C. Yes, it trained too many epochs

<details><summary>Answer</summary>

**B. No, distribution shift or shared leakage**. No gap: look for shift or leakage

</details>

**2. In scikit-learn's LogisticRegression, what does a smaller C mean?**

- A. Stronger regularisation
- B. Less bias and more variance
- C. Weaker regularisation

<details><summary>Answer</summary>

**A. Stronger regularisation**. C is inverse strength: smaller C, stronger

</details>

**3. In serving, the same input gives different predictions. Most likely cause?**

- A. The learning rate is too high
- B. Model was never set to eval mode
- C. Features were dropped from the data

<details><summary>Answer</summary>

**B. Model was never set to eval mode**. Call eval() before validation and serving

</details>

**4. You early-stopped on a validation set. Which score do you report?**

- A. The last training score
- B. The best validation score
- C. A separate untouched test set

<details><summary>Answer</summary>

**C. A separate untouched test set**. Stopping data is tuning data. Report the test set.

</details>

**5. You apply softmax before CrossEntropyLoss and the loss is stuck. Why?**

- A. It already includes log softmax
- B. The learning rate is too small
- C. The class weights are too large

<details><summary>Answer</summary>

**A. It already includes log softmax**. Pass raw logits. Softmax is built in.

</details>

## Say it in the interview

**Overfitting in the interview**

- Memorising, not learning. The tell is a gap.
- Leakage first, then data, then regularise
- A set you tuned against is training data

**Regularisation in the interview**

- A little bias for less variance
- L2 shrinks all. L1 zeroes many.
- Tune by cross validation. Mind C.

**Dropout in the interview**

- Random zeroing stops co-adaptation
- Off at inference, scaled in training
- Classic bug: forgetting eval mode

**Early stopping in the interview**

- Stop when validation stalls, roll back
- Cheap regularisation. Still keep a test set.
- Time data: validate later, never random

**Loss functions in the interview**

- Differentiable. Squared error, or Huber.
- Cross-entropy punishes confident mistakes
- Train on log loss, choose by business metric

## Homework

- [ ] Explain the overfitting gap in two sentences
- [ ] Write down what C means
- [ ] Rerun the lab with your own numbers
- [ ] List three ways validation can mislead
