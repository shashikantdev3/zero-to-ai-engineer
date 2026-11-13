# Machine Learning and Deep Learning · Part 26 of 28: Five ML Interview Functions From Scratch

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Cosine similarity and top-k with argpartition
2. Precision, recall and F1 from scratch
3. Numerically stable sigmoid
4. Logistic regression with SGD, L2 and early stopping
5. Linear regression by gradient descent, and the step-size limit

## Key takeaways

- Normalise, argpartition with k minus one, sort k
- Guard each division, return zero, say so
- Both branches from exp of minus absolute z
- p minus y, no bias decay, best weights
- Step below 2 over λmax; standardise first

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_top_k_with_argpartition.py` | top_k with argpartition | yes |
| `code/02_prf_with_zero_division_guards.py` | prf with zero-division guards | yes |
| `code/03_a_sigmoid_that_never_overflows.py` | A sigmoid that never overflows | yes |
| `code/04_lab_break_and_fix_a_sigmoid.py` | Break and fix a sigmoid | yes |
| `code/05_one_epoch_of_mini_batch_sgd.py` | One epoch of mini-batch SGD | yes |
| `code/06_validation_loss_and_sample_data.py` | Validation loss and sample data | yes |
| `code/07_early_stopping_keeps_the_best.py` | Early stopping keeps the best | yes |
| `code/08_linear_regression_by_gradient_descent.py` | Linear regression by gradient descent | yes |
| `code/09_computing_the_safe_learning_rate.py` | Computing the safe learning rate | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_break_and_fix_a_sigmoid.py` prints:

```text
naive: overflow at -1000
stable(-1000) = 0.000
stable(0) = 0.500
stable(1000) = 1.000
```

## Try it without a key

- [Embedding Projector](https://projector.tensorflow.org): Explore word embeddings in 3D and find nearest neighbours. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What does np.argpartition(-s, k) do when k equals len(s)?**

- A. It raises an out-of-bounds error
- B. It returns every item, fully sorted
- C. It quietly returns k minus one items

<details><summary>Answer</summary>

**A. It raises an out-of-bounds error**. kth must be at most n minus one: pass k minus one

</details>

**2. The model flags nothing. What should a careful precision function return?**

- A. One, since nothing was wrongly flagged
- B. Zero, stated as a convention
- C. Let it raise a division error

<details><summary>Answer</summary>

**B. Zero, stated as a convention**. Undefined precision: return zero and name the convention

</details>

**3. Is the two-branch np.where sigmoid safe from overflow?**

- A. Yes, where runs only the chosen branch
- B. No, where computes both branches
- C. Only when all inputs are positive

<details><summary>Answer</summary>

**B. No, where computes both branches**. np.where is not lazy: both branches run

</details>

**4. Why does the bias update have no lam term?**

- A. The bias gradient is always zero
- B. L2 only works on matrices
- C. The bias carries the base rate

<details><summary>Answer</summary>

**C. The bias carries the base rate**. The bias holds the base rate: do not decay it

</details>

**5. Gradient descent on linear regression diverged. What is the most likely cause?**

- A. The learning rate is above the limit
- B. Linear regression is the wrong model
- C. Too few training epochs

<details><summary>Answer</summary>

**A. The learning rate is above the limit**. Divergence: shrink the step, or scale the features

</details>

## Say it in the interview

**Cosine top-k in the interview**

- Normalise both sides, epsilon for zero vectors
- argpartition with k minus one, then sort k
- In production: HNSW, recall against latency

**Metrics in the interview**

- Count, then guard every division
- Macro or micro? On imbalance, they differ enormously

**Stable sigmoid in the interview**

- np.where computes both branches, then picks
- Build both branches from one safe exponential

**Logistic SGD in the interview**

- Gradient: prediction minus label
- L2 on weights only; watch liblinear
- Patience on validation, return the best weights

**Step-size limit in the interview**

- Diverging? Check the learning rate
- Step below 2 over the Hessian's top eigenvalue
- Standardise first, so the safe step is reasonable

## Homework

- [ ] Write top_k and test k equal to n
- [ ] Run prf on a model that flags nothing
- [ ] Make the np.where sigmoid fail with raise
- [ ] Compare lr max before and after scaling
