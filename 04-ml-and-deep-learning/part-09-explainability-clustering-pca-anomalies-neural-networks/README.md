# Machine Learning and Deep Learning · Part 9 of 28: Explainability, Clustering, PCA, Anomalies, Neural Networks

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Model explainability
2. k-means clustering
3. Principal component analysis (PCA)
4. Anomaly detection and Isolation Forest
5. Neural networks (multilayer perceptron)

## Key takeaways

- Permutation globally, SHAP locally, not causation.
- Assign, update, repeat. Scale first.
- Combinations of features, ordered by variance.
- Short path means unusual, not fraud.
- Stacked non-linear layers. Boosting for tabular.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_permutation_importance_in_scikit_learn.py` | Permutation importance in scikit-learn | yes |
| `code/02_shap_values_for_five_cases.py` | SHAP values for five cases | after `pip install pandas shap` |
| `code/03_k_means_with_a_silhouette_score.py` | k-means with a silhouette score | yes |
| `code/04_lab_two_centres_six_points_by_hand.py` | Two centres, six points, by hand | yes |
| `code/05_pca_keeping_95_percent_of_variance.py` | PCA keeping 95 percent of variance | yes |
| `code/06_scoring_with_isolation_forest.py` | Scoring with Isolation Forest | yes |
| `code/07_a_multilayer_perceptron_in_pytorch.py` | A multilayer perceptron in PyTorch | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_two_centres_six_points_by_hand.py` prints:

```text
step 1: centres [1.0, 7.6]
step 2: centres [2.0, 11.0]
step 3: centres [2.0, 11.0]
clusters: [[1, 2, 3], [10, 11, 12]]
```

## Try it without a key

- [Embedding Projector](https://projector.tensorflow.org): Explore word embeddings in 3D and find nearest neighbours. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A fraud model ranks 'new device' as its top feature. What can you safely say?**

- A. The model relies on it heavily
- B. New devices cause fraud
- C. Blocking new devices stops fraud

<details><summary>Answer</summary>

**A. The model relies on it heavily**. Importance shows what the model uses, not causes

</details>

**2. Every k-means cluster just splits on income. What most likely went wrong?**

- A. Income truly defines customers
- B. k was set too high
- C. Features were not scaled

<details><summary>Answer</summary>

**C. Features were not scaled**. Scale features before distance-based clustering

</details>

**3. A teammate says PCA picked the 10 best features. What is wrong?**

- A. Nothing, that is correct
- B. It creates combinations, not a subset
- C. It should have picked 20 features

<details><summary>Answer</summary>

**B. It creates combinations, not a subset**. PCA builds combinations, it does not select

</details>

**4. Your Isolation Forest ranked today's transactions. What are the top scores?**

- A. Data entry mistakes
- B. Unusual points, not yet proven fraud
- C. Confirmed fraud cases

<details><summary>Answer</summary>

**B. Unusual points, not yet proven fraud**. Unusual is not fraud until labels confirm it

</details>

**5. Why do deep plain networks get harder to train?**

- A. Gradients vanish through many layers
- B. They have too few parameters
- C. ReLU makes them linear

<details><summary>Answer</summary>

**A. Gradients vanish through many layers**. Deeper is not always better: gradients vanish

</details>

## Say it in the interview

**Say it: explaining a flagged case**

- Shuffle a feature, watch the metric fall.
- SHAP splits one score into reason codes.
- Importance is not causation.

**Say it: k-means in an interview**

- Assign to nearest, move to the mean.
- Pick k, scale, expect round clusters.
- Silhouette score plus business meaning.

**Say it: PCA in an interview**

- Right-angled axes, ordered by variance.
- Scale first, fit on train only.
- Most variance is not most predictive.

**Say it: anomaly detection**

- Few labels? Start with anomaly detection.
- Rank by score, review the top.
- Go supervised once labels arrive.

**Say it: neural networks**

- Weighted sum, then a non-linearity.
- Without it, ten layers equal one.
- Tabular: boosting first. Text, images: networks.

## Homework

- [ ] Rerun the k-means lab with three centres
- [ ] Sum the explained variance ratios in PCA
- [ ] Add a second outlier, check its score
- [ ] Remove ReLU, explain why the network collapses
