# Machine Learning and Deep Learning · Part 3 of 28: How Models Learn, and How to Judge Them

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Gradient descent
2. Stochastic and mini-batch gradient descent
3. Learning rate and schedules
4. Momentum, Adam and AdamW
5. Confusion matrix
6. Accuracy and the accuracy paradox

## Key takeaways

- Step against the gradient, scaled by learning rate
- Mini-batches: shuffle, and zero the gradients
- Tune learning rate first; warm up, then decay
- Default AdamW, tune its rate, verify
- Read the four cells, price each one
- Accuracy means nothing without the base rate

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_gradient_descent_in_numpy.py` | Gradient Descent in NumPy | yes |
| `code/02_setting_up_a_pytorch_run.py` | Setting Up a PyTorch Run | yes |
| `code/03_the_mini_batch_training_loop.py` | The Mini-Batch Training Loop | yes |
| `code/04_adamw_with_a_cosine_schedule.py` | AdamW With a Cosine Schedule | yes |
| `code/05_lab_three_learning_rates_one_loss.py` | Three Learning Rates, One Loss | yes |
| `code/06_creating_an_adamw_optimiser.py` | Creating an AdamW Optimiser | yes |
| `code/07_confusion_matrix_in_scikit_learn.py` | Confusion Matrix in scikit-learn | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_three_learning_rates_one_loss.py` prints:

```text
lr 0.01: w = 1.00
lr 0.1: w = 2.97
lr 1.1: w = -112.01
target: w = 3.00
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your training loss goes up every step. What is the likely cause?**

- A. Learning rate too high, or unscaled features
- B. Too much training data
- C. Too few training steps

<details><summary>Answer</summary>

**A. Learning rate too high, or unscaled features**. Rising loss: lower the learning rate, scale features

</details>

**2. Training explodes after the first batch. What did you likely forget?**

- A. Raising the batch size
- B. Calling zero grad each step
- C. Adding more epochs

<details><summary>Answer</summary>

**B. Calling zero grad each step**. Forget zero_grad and gradients accumulate

</details>

**3. An interviewer asks for the correct learning rate. Best answer?**

- A. It depends; run a log-scale sweep
- B. One value works for every model
- C. Always the optimiser's default

<details><summary>Answer</summary>

**A. It depends; run a log-scale sweep**. No universal rate: sweep on a log scale

</details>

**4. Adam adapts each weight's step. Does it still need tuning?**

- A. Only epsilon needs tuning
- B. Yes, the learning rate still needs tuning
- C. No, the defaults always work

<details><summary>Answer</summary>

**B. Yes, the learning rate still needs tuning**. Adam is forgiving, not tuning-free

</details>

**5. What is the false positive rate, from a confusion matrix?**

- A. fp divided by fp plus tp
- B. fp divided by the total
- C. fp divided by fp plus tn

<details><summary>Answer</summary>

**C. fp divided by fp plus tn**. False positive rate: out of all actual negatives

</details>

**6. 3% of labels are fraud. What accuracy does predicting all 0s get?**

- A. 50 percent
- B. 3 percent
- C. 97 percent, with zero recall

<details><summary>Answer</summary>

**C. 97 percent, with zero recall**. 97% accurate can mean zero fraud caught

</details>

## Say it in the interview

**Gradient Descent in the Interview**

- Step against the gradient, scaled by learning rate
- Too big diverges. Too small crawls.
- Not convex: check generalisation on validation

**Mini-Batches in the Interview**

- Estimate the gradient from a mini-batch
- Noisy but unbiased, many more updates
- Retune learning rate. Shuffle every epoch.

**Learning Rate in the Interview**

- Tune the learning rate first
- Warmup, then cosine decay
- Fine-tune low, or risk catastrophic forgetting

**Optimisers in the Interview**

- Adam scales each weight's step
- AdamW: the usual choice for transformers
- Default to AdamW, verify on validation

**Confusion Matrix in the Interview**

- One number hides which mistake you make
- Put a price on each cell
- Threshold becomes a business decision

**Accuracy in the Interview**

- Ask for the base rate first
- Base rate, then cost of each mistake
- Report recall at the review budget

## Homework

- [ ] Run gradient descent with a larger learning rate
- [ ] Explain Adam's two moments in your own words
- [ ] Build a confusion matrix by hand
- [ ] Compute the all-zeros accuracy for one dataset
