# RAG and Vector Search · Part 21 of 26: Agentic Retrieval and Knowledge Graphs

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Managed agentic retrieval in Azure AI Search
2. Question drill: Advanced patterns and boundaries
3. Knowledge graphs and the property graph model
4. Cypher essentials: MATCH, WHERE, MERGE, paths and aggregation
5. Graph constraints, indexes and the native vector index

## Key takeaways

- Agentic retrieval: route only complex questions
- Match the pattern to the question
- Graph only when multi-hop evals fail
- MERGE nodes first; bound every path
- New embeddings mean rebuild the index

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_idempotent_load_with_merge.py` | Idempotent load with MERGE | yes |
| `code/02_bounded_multi_hop_query.py` | Bounded multi-hop query | yes |
| `code/03_lab_simulate_the_merge_trap.py` | Simulate the MERGE trap | yes |
| `code/04_constraint_and_vector_index.py` | Constraint and vector index | yes |
| `code/05_vector_search_then_traverse.py` | Vector search, then traverse | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_simulate_the_merge_trap.py` prints:

```text
whole path: 2
rerun: 2
nodes first: 1
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Is agentic retrieval always better than hybrid search plus a reranker?**

- A. Yes, it always retrieves more
- B. Yes, its cost matches plain search
- C. No, route only complex questions to it

<details><summary>Answer</summary>

**C. No, route only complex questions to it**. Higher latency and cost; route only complex questions

</details>

**2. Our data has relationships. Do we need a graph database?**

- A. No, vector search follows any link
- B. Only if questions have unknown depth
- C. Yes, relationships always need a graph

<details><summary>Answer</summary>

**B. Only if questions have unknown depth**. Unknown depth is the signal, not relationships

</details>

**3. Are graphs always better than vectors for RAG?**

- A. Yes, once extraction is automated
- B. No, add one when multi-hop evals fail
- C. Yes, graphs capture more meaning

<details><summary>Answer</summary>

**B. No, add one when multi-hop evals fail**. Multi-hop eval failures are the deciding signal

</details>

**4. Is MERGE (a)-[:R]->(b) with inline properties safe to rerun?**

- A. No, merge each node first
- B. Yes, MERGE never makes duplicates
- C. Yes, if the relationship has a type

<details><summary>Answer</summary>

**A. No, merge each node first**. MERGE nodes on keys first, then the relationship

</details>

**5. You switched embedding models. Can you just change the index dimension?**

- A. No, re-embed and rebuild the index
- B. Yes, old vectors adapt automatically
- C. Yes, alter the dimension in place

<details><summary>Answer</summary>

**A. No, re-embed and rebuild the index**. New embedding model means re-embed and rebuild

</details>

## Say it in the interview

**Say it: agentic retrieval**

- Managed: plan, fan out, rerank, cite
- Check GA and preview before committing
- Managed saves work; own loop gives control

**Say it: knowledge graphs**

- Nodes and typed relationships, both with properties
- Graph when the answer is a relationship

**Say it: Cypher essentials**

- Cypher is a picture of the pattern
- Merge nodes on keys, then the relationship
- Always bound variable-length paths

**Say it: constraints and vectors**

- Constraint first: no duplicates, fast MERGE
- Vector top-k, then traverse
- Check vector syntax for your version

## Homework

- [ ] Run the lab; fix merge_path yourself
- [ ] Write a bounded one-to-three hop query
- [ ] Sketch a Service, Team, Runbook, Incident graph
- [ ] Practise the agentic retrieval answer
