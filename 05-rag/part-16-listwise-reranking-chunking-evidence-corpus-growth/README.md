# RAG and Vector Search · Part 16 of 26: Listwise Reranking, Chunking Evidence, Corpus Growth

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Listwise reranking
2. Chunk size and overlap evidence
3. Chunking by document type
4. Question drill: Chunk and rerank evidence
5. Corpus growth and retrieval dilution

## Key takeaways

- Listwise: compare all, validate the ids
- Small chunks, small overlap, then tune
- Splitter per type, recorded in metadata
- Reranker first; skip heavy overlap
- Growth dilutes: filter, widen, rerank

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_build_one_prompt_for_the_list.py` | Build one prompt for the list | yes |
| `code/02_validate_the_returned_order.py` | Validate the returned order | yes |
| `code/03_lab_pick_a_chunking_config.py` | Pick a chunking config | yes |
| `code/04_two_plain_splitters.py` | Two plain splitters | yes |
| `code/05_route_by_document_type.py` | Route by document type | yes |
| `code/06_filter_wide_then_rerank.py` | Filter wide, then rerank | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_pick_a_chunking_config.py` prints:

```text
configs tried: 4
best MRR: 72.0
within one point: 3
pick: (256, 0, 'recursive')
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Which reranker compares candidates against each other?**

- A. A cross-encoder scoring each pair
- B. A listwise reranker
- C. A bigger bi-encoder

<details><summary>Answer</summary>

**B. A listwise reranker**. Comparing candidates needs a listwise reranker

</details>

**2. 800 tokens with 400 overlap: what does the overlap cost?**

- A. Slower model downloads
- B. Nothing, it only adds safety
- C. Duplicate entries and duplicate results

<details><summary>Answer</summary>

**C. Duplicate entries and duplicate results**. Overlap duplicates; parent-child handles boundaries

</details>

**3. One department's answers are worse than everyone else's. Likely cause?**

- A. Their format uses a splitter tuned elsewhere
- B. The model dislikes their topic
- C. Their questions are just harder

<details><summary>Answer</summary>

**A. Their format uses a splitter tuned elsewhere**. Check the chunker before blaming the questions

</details>

**4. Is heavy chunk overlap the safe way to handle boundaries?**

- A. Yes, more overlap is always safer
- B. No, use parent-child retrieval
- C. Yes, as long as chunks are large

<details><summary>Answer</summary>

**B. No, use parent-child retrieval**. Boundaries: parent-child, not heavy overlap

</details>

**5. You sent more chunks. Cost tripled, and the answer still cites the old version. Why?**

- A. More context made it worse
- B. The model needs more output tokens
- C. Still too few chunks were sent

<details><summary>Answer</summary>

**A. More context made it worse**. More context is not a fix for dilution

</details>

## Say it in the interview

**Listwise reranking, in an interview**

- Listwise: all candidates at once, one ordering
- Validate the permutation, fall back if broken
- Test against a cross-encoder first

**Chunking, in an interview**

- Start plain: a few hundred tokens
- Heavy overlap and semantic chunking: weak evidence
- Effort goes to reranking and evaluation

**Chunking by type, in an interview**

- One splitter for everything is expensive
- Slides get deck and section titles
- Tag the chunker, slice evals by type

**Dilution, in an interview**

- Assume dilution before blaming the model
- In top fifty, not top five: fix ranking
- Not in top fifty: measure index recall

## Homework

- [ ] Feed the validator a broken reply
- [ ] Rerun the grid with your own scores
- [ ] Pick a splitter for each document type
- [ ] Write the top fifty versus top five check
