# RAG and Vector Search · Part 9 of 26: Choosing, Filtering and Re-indexing Vector Stores

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. The store decision sequence
2. Question drill: Vector search operations
3. pgvector iterative index scans
4. Zero-downtime re-index with an alias swap

## Key takeaways

- Ask in order; data location comes first
- efSearch tunes live; rebuild time is recovery
- Filter after scan; iterative scan fills LIMIT
- Build beside, validate, swap the alias

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_lab_estimate_hnsw_memory.py` | Estimate HNSW memory | yes |
| `code/02_filter_after_the_scan.py` | Filter after the scan | yes |
| `code/03_iterative_scan_with_a_cap.py` | Iterative scan with a cap | yes |
| `code/04_an_alias_swap_in_miniature.py` | An alias swap in miniature | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/01_lab_estimate_hnsw_memory.py` prints:

```text
vectors: 61.4 GB
graph: 1.3 GB
total: 62.7 GB
graph share: 2 percent
pgvector: 123 GB
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Retrieval quality is poor. Which lever do you pull first?**

- A. Switch to another vector database
- B. Move to a bigger server
- C. Reranking and chunking

<details><summary>Answer</summary>

**C. Reranking and chunking**. The store changes operations, not relevance.

</details>

**2. Does a tight entitlement filter make vector search slow?**

- A. Usually not, it can be the fast path
- B. Yes, the graph walk always slows down
- C. Only on disk-based indexes

<details><summary>Answer</summary>

**A. Usually not, it can be the fast path**. Very selective filters can scan the matches directly.

</details>

**3. Is a pgvector WHERE filter applied inside the HNSW index?**

- A. Only when ef_search is above 100
- B. No, it runs after the index scan
- C. Yes, so results are always complete

<details><summary>Answer</summary>

**B. No, it runs after the index scan**. The filter runs after the scan. Check row counts.

</details>

**4. Can you re-embed documents into the same live index overnight?**

- A. No, mixed embedding spaces give wrong results
- B. Yes, it is only slower for one night
- C. Yes, if you start at midnight

<details><summary>Answer</summary>

**A. No, mixed embedding spaces give wrong results**. Mixed embedding spaces are wrong, not slow.

</details>

## Say it in the interview

**Say it in the interview**

- A sequence, not a feature table.
- On call, filter, hybrid, residency.
- Switching stores fixes neither.

**Say it in the interview**

- Selective filters quietly return fewer rows.
- Pull until satisfied or capped.
- Partial index or partition; test filtered recall.

**Say it in the interview**

- Never re-index in place.
- Validate, swap atomically, keep rollback.
- Dual-write or replay during the build.

## Homework

- [ ] Write the five store questions in order
- [ ] Rerun the memory lab at 512 dimensions
- [ ] Lower the cap until rows fall short
- [ ] Sketch an alias swap with dual writes
