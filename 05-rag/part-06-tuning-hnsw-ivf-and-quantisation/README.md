# RAG and Vector Search · Part 6 of 26: Tuning HNSW, IVF and Quantisation

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. HNSW parameter ranges by dimension
2. IVF training and probes in pgvector
3. pgvector index builds and partial indexes
4. Quantisation defaults and the accuracy footnote

## Key takeaways

- M follows dimensions; tune efSearch first
- IVF: load first, then raise probes
- Build memory matters; partial indexes for few values
- int8 near free; binary depends on the model

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_m_and_ef_search_in_pgvector.py` | M and ef_search in pgvector | yes |
| `code/02_build_ivfflat_after_loading.py` | Build IVFFlat after loading | yes |
| `code/03_lab_planning_lists_and_probes.py` | Planning lists and probes | yes |
| `code/04_give_the_build_room.py` | Give the build room | yes |
| `code/05_a_partial_index_per_tenant.py` | A partial index per tenant | yes |
| `code/06_binary_quantisation_then_measure.py` | Binary quantisation, then measure | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_planning_lists_and_probes.py` prints:

```text
   100000 rows: lists=100 probes=10
  1000000 rows: lists=1000 probes=32
  4000000 rows: lists=2000 probes=45
probes=1 of 1000 lists: 0.1%
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Recall stays capped even at a high efSearch. What is the likely cause?**

- A. M is too low for the dimensionality
- B. efSearch still needs to go higher
- C. The corpus is too large

<details><summary>Answer</summary>

**A. M is too low for the dimensionality**. Capped recall at high efSearch: M too low, rebuild

</details>

**2. Recall is poor even with high probes on a new IVF index. Why?**

- A. There are too many lists
- B. The index was built before loading data
- C. Probes still is not high enough

<details><summary>Answer</summary>

**B. The index was built before loading data**. Built on an empty table: rebuild after loading

</details>

**3. Row-level security is on. Is the vector search prefiltered?**

- A. No, it filters after the index scan
- B. Yes, RLS prefilters the vector index
- C. Only when ef search is high

<details><summary>Answer</summary>

**A. No, it filters after the index scan**. RLS always filters, but after the scan

</details>

**4. A vendor claims binary gives 32x compression at 95% accuracy. What do you ask?**

- A. Is int8 smaller than binary?
- B. Can we skip rescoring then?
- C. Which embedding model was it measured on?

<details><summary>Answer</summary>

**C. Which embedding model was it measured on?**. Binary accuracy holds for compatible models; measure yours

</details>

## Say it in the interview

**Say it in the interview**

- M follows dimensionality, not corpus size
- Start at 16. Tune efSearch first.
- On Azure, efSearch and efConstruction are the levers

**Say it in the interview**

- Check probes first: default searches one cluster
- Built before the data? Rebuild, not tuning
- HNSW skips training, so it is the default

**Say it in the interview**

- The notice tells you where the build slowed
- Raise build memory, check parallel workers
- Few tenants: partial indexes. Many: iterative scans

**Say it in the interview**

- Default: int8, ~99% accuracy, quarter the memory
- Binary's accuracy comes with a footnote
- Measure recall@10 on your own model

## Homework

- [ ] Run the lab with ten million rows
- [ ] Write the fix for capped HNSW recall
- [ ] Explain why RLS does not prefilter
- [ ] Rehearse the quantisation answer, under a minute
