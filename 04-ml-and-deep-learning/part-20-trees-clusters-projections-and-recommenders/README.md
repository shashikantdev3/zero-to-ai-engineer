# Machine Learning and Deep Learning · Part 20 of 28: Trees, Clusters, Projections and Recommenders

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Neural networks versus trees on tabular data
2. DBSCAN, hierarchical clustering and Gaussian mixtures
3. t-SNE and UMAP: reading the plot
4. Recommender systems: two-stage and two-tower
5. Question drill: Features and model families

## Key takeaways

- Boosting by default, not always
- Density, merge tree, or soft membership
- Explore with t-SNE, never measure
- Retrieve cheap, rank rich, design diversity
- Answer with mechanisms, not slogans

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_dbscan_labels_mixture_probabilities.py` | DBSCAN labels, mixture probabilities | yes |
| `code/02_three_perplexities_one_honest_view.py` | Three perplexities, one honest view | yes |
| `code/03_stage_one_helper_cosine_top_k.py` | Stage one helper: cosine top k | yes |
| `code/04_retrieve_then_rank.py` | Retrieve, then rank | yes |
| `code/05_lab_lab_the_cost_of_scanning_everything.py` | Lab: the cost of scanning everything | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_lab_the_cost_of_scanning_everything.py` prints:

```text
score all: 2.8 hours
rank 500: 500 ms
kept 5 of 1000
best score: 0.99
```

## Try it without a key

- [Embedding Projector](https://projector.tensorflow.org): Explore word embeddings in 3D and find nearest neighbours. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A colleague says neural nets never win on tabular data. Best reply?**

- A. Neural nets always win now
- B. The benchmark was scoped to about 10k samples
- C. Agreed, trees always win on tables

<details><summary>Answer</summary>

**B. The benchmark was scoped to about 10k samples**. Trees by default, never always

</details>

**2. DBSCAN on unscaled data with a default eps gives one cluster or all noise. Why?**

- A. DBSCAN needs k set first
- B. eps does not fit the raw scale
- C. There are too many data points

<details><summary>Answer</summary>

**B. eps does not fit the raw scale**. Scale first, then choose eps

</details>

**3. Two clusters sit far apart on a t-SNE plot. What can you conclude?**

- A. Cluster distances never mean anything
- B. They are very different groups
- C. Nothing yet; recheck at other perplexities

<details><summary>Answer</summary>

**C. Nothing yet; recheck at other perplexities**. Gaps are conditional; verify across settings

</details>

**4. You evaluate a new recommender only on clicks logged by the old system. What's missing?**

- A. Clicks on items never shown
- B. A larger embedding size
- C. More training epochs

<details><summary>Answer</summary>

**A. Clicks on items never shown**. Logs only cover what was shown

</details>

**5. You target-encoded the full dataset before splitting. Is that a problem?**

- A. Yes, each row sees its own label
- B. Only when categories are rare
- C. No, it is just preprocessing

<details><summary>Answer</summary>

**A. Yes, each row sees its own label**. Encode inside folds, never before splitting

</details>

## Say it in the interview

**Interview answer: trees or nets**

- Logistic baseline, then tuned boosting
- Tuning often matters more than family
- Switch families only for a measured reason

**Interview answer: beyond k-means**

- DBSCAN: any shape, own count, noise
- One radius fails on varying density
- k-means is the hard-assignment mixture

**Interview answer: reading t-SNE**

- Pictures, not measurements
- Check gaps in the original space
- Never use the coordinates as features

**Interview answer: recommenders**

- Cheap retrieval, then an expensive ranker
- Content features bridge cold start
- Keep exploration; design diversity in

## Homework

- [ ] DBSCAN on scaled and unscaled data
- [ ] Compare t-SNE at three perplexities
- [ ] Change the lab's shortlist size
- [ ] Write your trees versus nets answer
