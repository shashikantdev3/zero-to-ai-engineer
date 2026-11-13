# Machine Learning and Deep Learning · Part 8 of 28: SVMs, Naive Bayes, Trees and Ensembles

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Support vector machines (SVM)
2. Naive Bayes
3. Decision trees
4. Random forests and bagging
5. Gradient boosting

## Key takeaways

- SVM: widest margin; scores are distances
- Naive Bayes: fast baseline, overconfident probabilities
- Trees: readable, but high variance
- Forests: bagging plus random features cut variance
- Boosting: sequential corrections cut bias

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_an_rbf_kernel_svm_in_scikit_learn.py` | An RBF kernel SVM in scikit-learn | yes |
| `code/02_a_ticket_classifier_baseline.py` | A ticket classifier baseline | yes |
| `code/03_a_small_tree_you_can_read.py` | A small tree you can read | yes |
| `code/04_lab_score_a_split_with_gini_impurity.py` | Score a split with Gini impurity | yes |
| `code/05_a_random_forest_with_oob_score.py` | A random forest with OOB score | yes |
| `code/06_boosting_with_early_stopping.py` | Boosting with early stopping | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_score_a_split_with_gini_impurity.py` prints:

```text
before split: 0.444
cut 25: 0.333
cut 50: 0.222
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your SVM's decision_function returns 2.3 for a row. What is it?**

- A. The count of support vectors
- B. A signed distance to the boundary
- C. A probability for class one

<details><summary>Answer</summary>

**B. A signed distance to the boundary**. Margins rank; calibrate, for example Platt scaling

</details>

**2. Naive Bayes assumes independent features. Why is it still a good text baseline?**

- A. Fast, needs little data, ranks well
- B. Words in text really are independent
- C. Its probabilities are well calibrated

<details><summary>Answer</summary>

**A. Fast, needs little data, ranks well**. Naive is not bad, but probabilities are overconfident

</details>

**3. You retrain a deep tree on a slightly different sample. What happens?**

- A. Nothing, trees are robust to everything
- B. The tree structure can change a lot
- C. Only the leaf values shift slightly

<details><summary>Answer</summary>

**B. The tree structure can change a lot**. Small data changes, very different tree

</details>

**4. You raise a forest from 500 to 5,000 trees. What is the main effect?**

- A. It badly overfits the training data
- B. Each tree becomes much deeper
- C. Mostly more compute, not overfitting

<details><summary>Answer</summary>

**C. Mostly more compute, not overfitting**. More trees cost compute; deep trees on noise overfit

</details>

**5. Which mainly reduces bias, and which mainly reduces variance?**

- A. Boosting cuts bias, bagging cuts variance
- B. Both mainly cut variance
- C. Bagging cuts bias, boosting cuts variance

<details><summary>Answer</summary>

**A. Boosting cuts bias, bagging cuts variance**. Boosting stacks corrections; bagging averages away variance

</details>

## Say it in the interview

**Say it: support vector machines**

- Widest gap to the nearest points
- Kernel trick for curves; scale features first
- Slow on big data; scores are margins

**Say it: naive Bayes**

- Multiply feature likelihoods with the class prior
- Fast, little data, strong text baseline
- Use it to rank; calibrate for probabilities

**Say it: decision trees**

- One question at a time, purest groups
- No scaling, interactions, readable
- Limit depth, or use trees in ensembles

**Say it: random forests**

- Bootstrap rows, random features, averaged trees
- Averaging cancels variance; low-effort baseline
- Prefer permutation importance over impurity importance

**Say it: gradient boosting**

- Each tree fits the gradient of the loss
- Usually the model to beat on tabular data
- Use early stopping; guard against leakage

## Homework

- [ ] Print a few SVM decision function scores
- [ ] Add tickets to the Naive Bayes example
- [ ] Compare tree rules at depth 2 and 8
- [ ] Compare out-of-bag scores at 50 and 500 trees
