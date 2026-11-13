# Machine Learning and Deep Learning · Part 11 of 28: Embeddings, Drift and Online Evaluation

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Embeddings
2. Drift: data, concept and prediction
3. Offline versus online evaluation

## Key takeaways

- Learned vectors; scores never compare across models
- Data, concept, prediction drift; alert on effect size
- Offline gate, then shadow, canary, gradual rollout

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_an_embedding_layer_in_pytorch.py` | An embedding layer in PyTorch | yes |
| `code/02_lab_cosine_similarity_by_hand.py` | Cosine similarity by hand | yes |
| `code/03_psi_counting_the_bins.py` | PSI: counting the bins | yes |
| `code/04_psi_the_score_itself.py` | PSI: the score itself | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_cosine_similarity_by_hand.py` prints:

```text
cat~dog: 0.994
cat~car: 0.03
model 2: 0.667
```

## Try it without a key

- [Embedding Projector](https://projector.tensorflow.org): Explore word embeddings in 3D and find nearest neighbours. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Two items score 0.9 cosine similarity. What does that tell you?**

- A. They are close in this model
- B. It beats 0.7 in any model
- C. The match is 90 percent correct

<details><summary>Answer</summary>

**A. They are close in this model**. Similarity is relative to one model, not correctness

</details>

**2. Input distributions have not moved at all. Is the model fine?**

- A. Yes, no data drift means no problem
- B. Not necessarily: concept drift can still occur
- C. Yes, if the KS p-value is large

<details><summary>Answer</summary>

**B. Not necessarily: concept drift can still occur**. Identical inputs can still hide concept drift

</details>

**3. Offline metrics passed. What can offline data never show you?**

- A. Accuracy on held-out data
- B. Whether the model beats a baseline
- C. Feedback loops, latency under load, new behaviour

<details><summary>Answer</summary>

**C. Feedback loops, latency under load, new behaviour**. Offline says worth trying; online says it works

</details>

## Say it in the interview

**Embeddings, in your own words**

- Discrete item in, dense learned vector out
- Trainable lookup table; search by meaning
- New embedding model means re-embed everything

**Drift, in your own words**

- Inputs change, or the meaning changes
- Prediction drift is often the first visible sign
- A stale index is freshness failure, not drift

**Offline and online, in your words**

- Offline: worth trying. Online: it works.
- Shadow mode first, then a canary
- A random holdout keeps measurement honest

## Homework

- [ ] Rerun the cosine lab with your vectors
- [ ] Code PSI and test a bigger shift
- [ ] Define three drifts, one sentence each
- [ ] Sketch offline gate to rollout
