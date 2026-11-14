# RAG and Vector Search · Part 18 of 26: Smarter Chunks, Agents and Graphs

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Sentence-window retrieval
2. Contextual retrieval
3. Late chunking
4. Agentic RAG
5. GraphRAG and graph retrieval

## Key takeaways

- Match sentences, return windows, watch storage
- Prepend context at ingest, cache the document
- Embed whole document, then pool per chunk
- Loop with a cap; filter inside the tool
- Graphs for relationships and global questions

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_lab_expand_and_merge_sentence_windows.py` | Expand and merge sentence windows | yes |
| `code/02_the_cheap_version_heading_path.py` | The cheap version: heading path | yes |
| `code/03_the_agent_loop_with_a_hard_cap.py` | The agent loop with a hard cap | yes |
| `code/04_cypher_hops_and_a_vector_index.py` | Cypher: hops and a vector index | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/01_lab_expand_and_merge_sentence_windows.py` prints:

```text
hits: [2, 3, 8]
0 5 S0 S1 S2 S3 S4 S5
6 9 S6 S7 S8 S9
vectors stored: 10
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. With sentence-window retrieval, how many vectors does a 10,000-page corpus need?**

- A. One per sentence in the corpus
- B. One per page
- C. One per document

<details><summary>Answer</summary>

**A. One per sentence in the corpus**. Storage grows with sentence count. Do the maths.

</details>

**2. When does contextual retrieval write the context line for a chunk?**

- A. At query time, for each question
- B. After the answer is generated
- C. At ingest, before embedding

<details><summary>Answer</summary>

**C. At ingest, before embedding**. Ingest step. Cache the prefix, measure the gain.

</details>

**3. What does "late" mean in late chunking?**

- A. Chunks cut after retrieval
- B. Chunks cut after embedding the whole document
- C. Chunks cut at query time

<details><summary>Answer</summary>

**B. Chunks cut after embedding the whole document**. Late means after embedding, not after retrieval

</details>

**4. An agent searched wider and another client's runbook came back. Why?**

- A. The embedding model was too small
- B. Permission was not enforced in the tool
- C. The step cap was set too low

<details><summary>Answer</summary>

**B. Permission was not enforced in the tool**. Enforce permissions inside the tool, default deny

</details>

**5. Graphs beat vectors on multi-hop questions. Should every query use GraphRAG?**

- A. No, only relationship or global questions
- B. Yes, once the graph is built
- C. Yes, graphs always beat vectors

<details><summary>Answer</summary>

**A. No, only relationship or global questions**. Use graphs where relationships matter

</details>

## Say it in the interview

**Sentence windows in an interview**

- Match one sentence, return its neighbours
- Use it where evals show precision problems

**Contextual retrieval in an interview**

- Chunks lose their policy, country and year
- Prepend generated context at ingest
- Test heading path against generated context

**Late chunking in an interview**

- Isolated chunks lose their references
- Embed the whole document, then pool per chunk
- Needs long context and token-level outputs

**Agentic RAG in an interview**

- Search as a tool, in a loop
- Cap steps; filter inside the tool
- Simple lookups: hybrid search plus reranking

**GraphRAG in an interview**

- Graphs win when the answer is a relationship
- Global uses summaries; local expands from entities
- Simple lookups stay on hybrid search

## Homework

- [ ] Estimate vectors for one-per-sentence indexing
- [ ] Rerun the lab with N of 1 and 3
- [ ] Write heading-path prefixes for three chunks
- [ ] Sketch an agent loop with cap and permissions
