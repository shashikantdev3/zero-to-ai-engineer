# RAG and Vector Search · Part 5 of 26: Vector Search at Scale: Azure, Shards, Memory

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Azure AI Search
2. Sharding and scaling vector indexes
3. Debugging fast but wrong search
4. HNSW memory arithmetic

## Key takeaways

- Hybrid, filter, rerank; monitor index freshness
- Shards for capacity, replicas for throughput
- Exact search tells you which layer broke
- Vectors dominate memory, not the graph

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_hybrid_plus_semantic_query.py` | A hybrid plus semantic query | yes |
| `code/02_estimating_hnsw_memory.py` | Estimating HNSW memory | yes |
| `code/03_lab_watch_the_graph_overhead_shrink.py` | Watch the graph overhead shrink | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_watch_the_graph_overhead_shrink.py` prints:

```text
d=128: graph adds 25.0%
d=768: graph adds 4.2%
d=1536: graph adds 2.1%
vectors 61.44 GB
graph 1.28 GB
pgvector ~122.88 GB
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What does the semantic ranker in Azure AI Search actually do?**

- A. Reranks results already retrieved
- B. Replaces the keyword search
- C. Runs its own vector search

<details><summary>Answer</summary>

**A. Reranks results already retrieved**. The semantic ranker reorders; it does not retrieve

</details>

**2. Your vector index no longer fits on one node. What do you add?**

- A. Replicas, to hold more vectors
- B. A faster coordinator node
- C. Shards, to split the vectors

<details><summary>Answer</summary>

**C. Shards, to split the vectors**. Replicas copy; shards add capacity

</details>

**3. Vector search is fast but returns wrong chunks. What is your first move?**

- A. Compare against exact search
- B. Increase efSearch right away
- C. Rebuild the index from scratch

<details><summary>Answer</summary>

**A. Compare against exact search**. Test exact search before tuning the index

</details>

**4. 10M vectors, 1,536 float32 dims, M = 16. How much does the HNSW graph add?**

- A. Between 20 and 50 percent
- B. About 2 percent
- C. Exactly double the vectors

<details><summary>Answer</summary>

**B. About 2 percent**. At high dimensions the vectors dominate memory

</details>

## Say it in the interview

**Azure AI Search in an interview**

- Hybrid index: BM25 plus vectors, fused by RRF
- Security filter, semantic ranker, synced ingestion
- The index is a copy; monitor freshness

**Sharding in an interview**

- Shard for capacity; slowest shard sets latency
- Replicas for throughput; shard by tenant
- First try to fit on one node

**Debugging in an interview**

- First, rerun the queries with exact search
- Index losing recall, or an upstream problem
- One test saves days of tuning the wrong layer

**Memory maths in an interview**

- 61 GB of vectors; graph adds about 2 percent
- pgvector: budget about twice the vector bytes
- The lever is the vectors, not the graph

## Homework

- [ ] Write the hybrid query body from memory
- [ ] Draw a three-shard fan-out with one replica
- [ ] List the upstream checklist in order
- [ ] Size memory for your own vector count
