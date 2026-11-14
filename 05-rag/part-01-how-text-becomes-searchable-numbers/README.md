# RAG and Vector Search · Part 1 of 26: How Text Becomes Searchable Numbers

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Embedding
2. Embedding model selection
3. Query and document encoding
4. Cosine similarity, dot product and Euclidean distance
5. Vector normalisation

## Key takeaways

- Embeddings: learned, lossy vectors of meaning
- Leaderboards shortlist; your recall decides
- Right prefix per side; chunks under the limit
- Match the metric to the model card
- Stored side breaks ranking; query breaks thresholds

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_embedding_one_sentence.py` | Embedding One Sentence | after `pip install sentence-transformers` |
| `code/02_record_the_model_on_every_vector.py` | Record the Model on Every Vector | yes |
| `code/03_query_side_with_a_prefix.py` | Query Side With a Prefix | after `pip install sentence-transformers` |
| `code/04_passage_side_in_batches.py` | Passage Side in Batches | after `pip install sentence-transformers` |
| `code/05_cosine_similarity_in_numpy.py` | Cosine Similarity in NumPy | yes |
| `code/06_truncate_then_re_normalise.py` | Truncate, Then Re-normalise | yes |
| `code/07_lab_watch_length_change_the_winner.py` | Watch Length Change the Winner | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/07_lab_watch_length_change_the_winner.py` prints:

```text
dot: 0.9 3.0
cos: 0.99 0.83
dot x5: 4.5 15.0
```

## Try it without a key

- [Embedding Projector](https://projector.tensorflow.org): Explore word embeddings in 3D and find nearest neighbours. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does an embedding store a text's meaning exactly?**

- A. No, it is a lossy learned compression
- B. Only when the text is short
- C. Yes, every detail is kept

<details><summary>Answer</summary>

**A. No, it is a lossy learned compression**. Embeddings compress meaning; they do not store it

</details>

**2. Your corpus is half Hindi. Does the top leaderboard row still apply?**

- A. Yes, if the model is large enough
- B. No, test on your languages and queries
- C. Yes, the top score always wins

<details><summary>Answer</summary>

**B. No, test on your languages and queries**. Benchmarks shortlist; your own data decides

</details>

**3. Recall dropped after moving to an open model. Nothing errored. Why?**

- A. Missing query and passage prefixes
- B. Open models always recall less
- C. The index lost some vectors

<details><summary>Answer</summary>

**A. Missing query and passage prefixes**. Asymmetric models need the right prefix per side

</details>

**4. The card says dot product and vectors are unnormalised. Is cosine safe?**

- A. Yes, cosine is always best
- B. Yes, all metrics rank the same
- C. No, ranking can change; match the card

<details><summary>Answer</summary>

**C. No, ranking can change; match the card**. Metrics agree only on unit-length vectors

</details>

**5. Only the query vector is unnormalised. What happens to the ranking?**

- A. Different documents come back
- B. Ranking stays; only scores shift
- C. Only the top result changes

<details><summary>Answer</summary>

**B. Ranking stays; only scores shift**. Query side breaks thresholds, not ranking

</details>

## Say it in the interview

**Embedding in an Interview**

- Distance means difference in meaning
- Trained on pairs, so questions find answers
- Pair vectors with keyword search

**Model Selection in an Interview**

- A benchmark is a shortlist, not a decision
- Compare recall at ten and MRR
- Smallest model that clears the bar

**Encoding in an Interview**

- Asymmetric models need matching prefixes
- A wrong prefix fails silently
- Check limits; re-embedding is a batch job

**Similarity Metrics in an Interview**

- Angle, angle plus length, straight-line gap
- Unit vectors: pick the fastest metric
- Match the model card, or lose silently

**Normalisation in an Interview**

- Unit length makes dot product equal cosine
- Stored side: ranking. Query side: thresholds.
- An eval set catches it; a demo does not

## Homework

- [ ] Type the lab; change the query
- [ ] Write cosine from memory, with the guard
- [ ] Read a model card: prefixes, limit, metric
- [ ] Practise the embedding answer in a minute
