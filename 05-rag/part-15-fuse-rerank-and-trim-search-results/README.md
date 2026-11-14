# RAG and Vector Search · Part 15 of 26: Fuse, Rerank and Trim Search Results

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Reciprocal rank fusion
2. Bi-encoder versus cross-encoder reranking
3. Context budget
4. Exact-match field
5. Reranking as the biggest measured lever

## Key takeaways

- RRF fuses ranks, not scores
- Retrieve with bi, rerank with cross
- Cap by tokens; prove k with evals
- Normalised code field, validated, boosted
- Reranker is the biggest measured lever

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_reciprocal_rank_fusion_in_python.py` | Reciprocal rank fusion in Python | yes |
| `code/02_lab_third_in_both_versus_first_in_one.py` | Third in both versus first in one | yes |
| `code/03_reranking_with_a_cross_encoder.py` | Reranking with a cross-encoder | after `pip install sentence-transformers` |
| `code/04_the_code_pattern_and_catalogue.py` | The code pattern and catalogue | yes |
| `code/05_normalise_and_validate_codes.py` | Normalise and validate codes | yes |
| `code/06_testing_the_normaliser.py` | Testing the normaliser | yes |
| `code/07_two_retrieval_metrics.py` | Two retrieval metrics | yes |
| `code/08_compare_variants_on_a_golden_set.py` | Compare variants on a golden set | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_third_in_both_versus_first_in_one.py` prints:

```text
solo: 0.0164
both: 0.0317
winner: both
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What does reciprocal rank fusion use as its input?**

- A. Scores rescaled to one range
- B. The raw similarity scores
- C. Rank positions in each list

<details><summary>Answer</summary>

**C. Rank positions in each list**. RRF fuses ranks, never raw scores

</details>

**2. In a million-document search, where should the cross-encoder run?**

- A. Only on a short candidate list
- B. Over the whole corpus each query
- C. Once at ingest, like embeddings

<details><summary>Answer</summary>

**A. Only on a short candidate list**. Cross-encoders rerank a short list only

</details>

**3. Going from 5 chunks to 10 did not raise groundedness. What are the extra 5?**

- A. Free context for the model
- B. Just extra cost
- C. A safer, better answer

<details><summary>Answer</summary>

**B. Just extra cost**. No groundedness gain means pure cost

</details>

**4. Search misses XR4410B when users type XR-4410B. What fixes it?**

- A. Switch to a bigger embedding model
- B. Normalise codes into a metadata field
- C. Turn up the BM25 weight

<details><summary>Answer</summary>

**B. Normalise codes into a metadata field**. Different tokens need a normalised field

</details>

**5. On Microsoft's benchmark, what gave the largest NDCG@3 lift?**

- A. Adding a semantic reranker
- B. Switching from keyword to vector
- C. Adding keyword search to vector

<details><summary>Answer</summary>

**A. Adding a semantic reranker**. Hybrid is robustness; the reranker is the lift

</details>

## Say it in the interview

**Say it in the interview**

- RRF fuses on ranks, not scores
- Third in both beats first in one
- Simple, robust, no tuning

**Say it in the interview**

- Bi-encoder: fast, but they never meet
- Cross-encoder: reads both, runs per candidate
- Retrieve fifty, rerank, keep five

**Say it in the interview**

- More context is not better answers
- Weak chunks bury the one that matters
- Prove the chunk count with evals

**Say it in the interview**

- Three reasons hybrid misses codes
- Normalised code field plus a strong boost
- Validate first; filter only when verified

**Say it in the interview**

- Add a reranker first
- Hybrid is robustness; the reranker is the lift
- Measure on your own golden set

## Homework

- [ ] Run the RRF lab with your lists
- [ ] Change k and compare the order
- [ ] Test the normaliser on three spellings
- [ ] Plan an eval: five versus ten chunks
