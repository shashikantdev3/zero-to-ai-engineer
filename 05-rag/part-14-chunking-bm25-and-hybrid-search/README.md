# RAG and Vector Search · Part 14 of 26: Chunking, BM25 and Hybrid Search

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Chunking strategies
2. Chunk overlap
3. Tune chunking with evals
4. BM25 and keyword search
5. Hybrid search

## Key takeaways

- Chunk on structure; embed the heading path
- Overlap protects boundaries; deduplicate the copies
- Measure chunking on a golden set
- BM25 wins on exact words, misses meaning
- Run both legs, fuse on ranks

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_split_on_headings_first.py` | Split on headings first | after `pip install langchain_text_splitters` |
| `code/02_put_the_heading_path_back_in.py` | Put the heading path back in | after `pip install langchain_text_splitters` |
| `code/03_lab_see_a_rule_cut_in_half.py` | See a rule cut in half | yes |
| `code/04_bm25_in_a_few_lines.py` | BM25 in a few lines | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_see_a_rule_cut_in_half.py` prints:

```text
Staff get ten leave days. Unused
days carry forward.
---
Staff get ten leave days. Unused
days. Unused days carry forward.
forward.
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What is the right chunk size for a RAG index?**

- A. As large as the context window
- B. No universal size; measure it with evals
- C. 512 tokens, the standard size

<details><summary>Answer</summary>

**B. No universal size; measure it with evals**. No universal chunk size; evals on the golden set decide

</details>

**2. Is more chunk overlap always safer?**

- A. No, duplicates crowd out other evidence
- B. Yes, as long as storage is cheap
- C. Yes, it never loses context

<details><summary>Answer</summary>

**A. No, duplicates crowd out other evidence**. Too much overlap: duplicates crowd out evidence

</details>

**3. Asked how you chose your chunk size, what is the strongest answer?**

- A. I named the metric that moved
- B. I picked what felt right
- C. I copied it from a popular blog

<details><summary>Answer</summary>

**A. I named the metric that moved**. Name the metric and the eval set

</details>

**4. Can vector search alone find ticket INC0012345 by meaning?**

- A. Only with a bigger embedding model
- B. Yes, embeddings capture everything
- C. No, keywords win on exact identifiers

<details><summary>Answer</summary>

**C. No, keywords win on exact identifiers**. Keywords win on identifiers

</details>

**5. How should you merge BM25 results with vector results?**

- A. Average the BM25 and cosine scores
- B. Fuse on ranks with RRF
- C. Keep only the higher-scoring list

<details><summary>Answer</summary>

**B. Fuse on ranks with RRF**. Scales differ, so merge on ranks

</details>

## Say it in the interview

**Chunking in the interview**

- Chunking decides what the retriever can find.
- Split on headings, keep tables, embed the path.
- Semantic chunking only if evals show a win.

**Overlap in the interview**

- Overlap is insurance for boundary cuts.
- I deduplicate after retrieval.
- Tune overlap with the eval set.

**Tuning in the interview**

- I do not argue about chunk size.
- Compare variants: hit rate at five, MRR.
- The winning config is versioned with the index.

**BM25 in the interview**

- Rare words weigh more; repeats saturate.
- Old, cheap, excellent at exact matches.
- Opposite blind spot from vectors, so run both.

**Hybrid search in the interview**

- They fail in opposite places.
- Exact identifiers are what vectors blur.
- Drop a leg only if evals say so.

## Homework

- [ ] Split one document by headings
- [ ] Rerun the lab with different overlaps
- [ ] Score three documents with BM25
- [ ] Write your answer, naming the metric
