# RAG and Vector Search · Part 2 of 26: Where Embedding Search Quietly Goes Wrong

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Similarity is not correctness
2. Multilingual embedding space
3. Dimensions versus memory
4. Re-embed everything
5. Dense versus sparse vectors

## Key takeaways

- Scores are relative; calibrate from labelled pairs
- One space, uneven quality; test each language
- Shrink vectors, then measure recall at k
- New model: re-embed all, switch by alias
- Dense for meaning, sparse for exact words

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_lab_lab_pick_a_threshold_from_data.py` | Lab: Pick a Threshold From Data | yes |
| `code/02_memory_arithmetic_in_python.py` | Memory Arithmetic in Python | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/01_lab_lab_pick_a_threshold_from_data.py` prints:

```text
0.65: kept 5 false 40%
0.7: kept 4 false 20%
0.75: kept 2 false 0%
chosen cut: 0.7
```

## Try it without a key

- [Embedding Projector](https://projector.tensorflow.org): Explore word embeddings in 3D and find nearest neighbours. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. In one model, English queries score 0.9 and Hindi queries 0.7. What follows?**

- A. The English answers are correct
- B. The Hindi answers are worse
- C. Nothing about correctness by itself

<details><summary>Answer</summary>

**C. Nothing about correctness by itself**. Calibrate per model and language from labelled pairs

</details>

**2. A model is called multilingual. What does that guarantee?**

- A. The same score scale everywhere
- B. One shared space, possibly uneven quality
- C. Equal quality in every language

<details><summary>Answer</summary>

**B. One shared space, possibly uneven quality**. Prove it with per-language recall on labelled queries

</details>

**3. Do more dimensions always mean better retrieval?**

- A. No, measure recall at k
- B. Yes, more is always better
- C. Yes, but only with float32

<details><summary>Answer</summary>

**A. No, measure recall at k**. Cut dimensions, then measure recall at k

</details>

**4. You switch embedding models. What needs the new model?**

- A. The whole corpus, and more
- B. Only the user queries
- C. Only the new documents

<details><summary>Answer</summary>

**A. The whole corpus, and more**. Re-embed all, then fix thresholds, caches, classifiers

</details>

**5. If dense vectors replaced keyword search, why do exact error codes miss?**

- A. Sparse vectors are always better
- B. Dense puts look-alike codes together
- C. The codes were never indexed

<details><summary>Answer</summary>

**B. Dense puts look-alike codes together**. Dense blurs codes, so keep keyword search

</details>

## Say it in the interview

**Say It: Scores Are Relative**

- Similarity scores are relative and model specific.
- Thresholds come from labelled pairs, not feel.
- High similarity means same topic, not true.

**Say It: Test Each Language**

- One space, so languages match directly.
- Uneven quality, so no single threshold.
- Measure recall per language, then fix gaps.

**Say It: Three Levers, One Check**

- Memory is count times dimensions times bytes.
- Truncate, int8, or binary with rescoring.
- Keep the saving only if recall holds.

**Say It: A Model Change Is a Release**

- New model means every stored vector is wrong.
- Re-embed side by side, switch with an alias.
- A model change is a release.

**Say It: They Fail Opposite Ways**

- Dense matches meaning, blurs exact tokens.
- Sparse nails exact terms, misses synonyms.
- Opposite failures, so use hybrid retrieval.

## Homework

- [ ] Rerun the threshold lab with new scores
- [ ] Compute memory for your own corpus size
- [ ] Sketch a blue-green index swap with alias
- [ ] List three queries where keywords beat dense
