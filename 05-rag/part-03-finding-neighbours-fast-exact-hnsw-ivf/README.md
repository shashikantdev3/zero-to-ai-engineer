# RAG and Vector Search · Part 3 of 26: Finding Neighbours Fast: Exact, HNSW, IVF

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Nearest neighbour search
2. Exact search baseline
3. Approximate nearest neighbour and recall@k
4. HNSW
5. IVF

## Key takeaways

- Return the k closest vectors to the query
- Exact is the truth, at linear cost
- Recall@k: overlap with exact top k, over k
- HNSW: raise efSearch before rebuilding
- IVF: train, probe, retrain on drift

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_exact_top_k_in_numpy.py` | Exact top k in NumPy | yes |
| `code/02_recall_at_k_in_four_lines.py` | Recall at k in four lines | yes |
| `code/03_lab_measure_a_shortcuts_recall.py` | Measure a shortcut's recall | yes |
| `code/04_an_hnsw_vector_profile.py` | An HNSW vector profile | yes |
| `code/05_an_ivf_index_in_faiss.py` | An IVF index in Faiss | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_measure_a_shortcuts_recall.py` prints:

```text
vectors stored: 5000
vectors visited: 194
recall@10: 1.0
```

## Try it without a key

- [Embedding Projector](https://projector.tensorflow.org): Explore word embeddings in 3D and find nearest neighbours. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your RAG app has 10,000 chunks. Do you need a vector database?**

- A. Yes, every RAG app needs one
- B. No, exact search in memory is fine
- C. Yes, exact search cannot fit in RAM

<details><summary>Answer</summary>

**B. No, exact search in memory is fine**. Small corpus: exact search in memory is fine.

</details>

**2. ANN can miss neighbours. Should you use exact search at ten million vectors?**

- A. No, use ANN and measure recall
- B. Yes, exact is always worth it
- C. Yes, exact gets faster with more data

<details><summary>Answer</summary>

**A. No, use ANN and measure recall**. Exact is the yardstick, not always the engine.

</details>

**3. ANN recall@10 is 0.99, but answers are still wrong. Why?**

- A. The exact neighbours are wrong too
- B. Recall must reach exactly 1.0
- C. The index is still missing neighbours

<details><summary>Answer</summary>

**A. The exact neighbours are wrong too**. High ANN recall is not answer quality.

</details>

**4. Your HNSW recall is too low. Which knob do you turn first?**

- A. Raise efConstruction
- B. Raise efSearch
- C. Raise m

<details><summary>Answer</summary>

**B. Raise efSearch**. Low recall? Raise efSearch first, no rebuild.

</details>

**5. Does IVFFlat always use less memory than HNSW at 1,536 dimensions?**

- A. Yes, clustering shrinks each vector
- B. Yes, IVF always uses less memory
- C. No, the full vectors dominate

<details><summary>Answer</summary>

**C. No, the full vectors dominate**. IVF saves memory only with product quantisation.

</details>

## Say it in the interview

**Say it in the interview**

- Give me the k closest stored vectors
- Exact is linear, fine for a few hundred thousand
- Trade latency for recall, and measure it

**Say it in the interview**

- Exact search is correct by definition
- Linear scan per query; tuned HNSW is far faster
- Compare index top ten with exact top ten

**Say it in the interview**

- Recall at k measures what speed cost
- Compare top ten on real queries, then tune
- Index recall and retrieval recall: need both

**Say it in the interview**

- A layered graph, searched from the top down
- m and efConstruction need a rebuild; efSearch doesn't
- Raise efSearch before you touch m

**Say it in the interview**

- Cluster the space; probe only the closest
- Saves memory with PQ, builds faster
- Boundaries and drift: probe more, retrain

## Homework

- [ ] Run exact_top_k on your own random vectors
- [ ] Compute recall@10 for two lists you invent
- [ ] Draw HNSW layers and label the three knobs
- [ ] Explain nprobe and retraining in two sentences
