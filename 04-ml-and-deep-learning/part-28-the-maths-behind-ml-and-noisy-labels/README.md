# Machine Learning and Deep Learning · Part 28 of 28: The Maths Behind ML, and Noisy Labels

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Linear algebra for ML: vectors, matrices and shapes
2. Derivatives, gradients and the chain rule
3. Conditional probability, independence and expectation
4. scale_pos_weight versus class_weight in boosting libraries
5. Label noise in fraud labels

## Key takeaways

- Annotate and assert every shape.
- Gradient points uphill; backprop reverses the chain rule.
- Threshold by expected cost; split by group or time.
- Class weights shift scores and break calibration.
- Chargebacks are noisy; immature rows are unlabelled.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_linear_layer_with_shapes.py` | A Linear Layer With Shapes | yes |
| `code/02_checking_a_gradient_by_hand.py` | Checking a Gradient by Hand | yes |
| `code/03_lab_forward_versus_central_differences.py` | Forward Versus Central Differences | yes |
| `code/04_expected_cost_of_a_threshold.py` | Expected Cost of a Threshold | yes |
| `code/05_scale_pos_weight_in_xgboost.py` | scale_pos_weight in XGBoost | after `pip install numpy xgboost` |
| `code/06_inflated_scores_after_weighting.py` | Inflated Scores After Weighting | after `pip install numpy xgboost` |
| `code/07_a_tiny_labelled_table.py` | A Tiny Labelled Table | yes |
| `code/08_trust_weights_and_maturity.py` | Trust, Weights and Maturity | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_forward_versus_central_differences.py` prints:

```text
exact slope: 6.75
forward error: 0.004501
central error: 1e-06
central closer: True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. You type X * W where you meant X @ W. What can happen?**

- A. It gives the same result
- B. Python always raises a shape error
- C. It runs and gives wrong numbers

<details><summary>Answer</summary>

**C. It runs and gives wrong numbers**. Star is element-wise; catch it with shape asserts.

</details>

**2. Which way does the gradient of the loss point?**

- A. Uphill, where loss rises fastest
- B. Toward a weight of zero
- C. Downhill, where loss falls fastest

<details><summary>Answer</summary>

**A. Uphill, where loss rises fastest**. The gradient points uphill; you step against it.

</details>

**3. Rows share users, but you split them at random. What happens?**

- A. The score looks better than it is
- B. The score becomes more honest
- C. Nothing changes in the score

<details><summary>Answer</summary>

**A. The score looks better than it is**. Shared users or time windows: group or time splits.

</details>

**4. Your weighted model scores a transaction 0.5. What does that mean?**

- A. Exactly a fifty percent fraud chance
- B. Not even odds; the score is inflated
- C. The model failed to train

<details><summary>Answer</summary>

**B. Not even odds; the score is inflated**. Weighted scores are inflated; recalibrate before reading odds.

</details>

**5. You label immature rows as legit. How does recall look on your newest data?**

- A. Exactly the same as before
- B. Worse than it really is
- C. Better than it really is

<details><summary>Answer</summary>

**B. Worse than it really is**. Immature rows are unlabelled, not legit.

</details>

## Say it in the interview

**Linear Algebra in an Interview**

- Dot products, matrix multiplies, and norms.
- A linear layer maps n by d to n by k.
- A silent shape bug is worse than a crash.

**Gradients in an Interview**

- The gradient: which way each weight should move.
- Backprop is the chain rule in reverse, cached.
- Check hand-written gradients with finite differences.

**Probability in an Interview**

- Models output a label's probability given features.
- One card's transactions are not independent.
- Choose the threshold with the lowest expected cost.

**Class Weights in an Interview**

- Start at negatives over positives.
- Check PR-AUC moved, not just the threshold.
- Recalibrate before scores become probabilities.

**Label Noise in an Interview**

- A chargeback is not the same thing as fraud.
- An audited set is the most trusted evaluation.
- Immature rows are unlabelled, not negatives.

## Homework

- [ ] Write a linear layer with shape asserts.
- [ ] Check a gradient with central differences.
- [ ] Compare two thresholds by expected cost.
- [ ] List three ways fraud labels go wrong.
