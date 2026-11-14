# RAG and Vector Search · Part 22 of 26: Graph Extraction, Hybrid Retrieval and Retrieval Metrics

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. LLM-based entity and relationship extraction
2. Vector plus graph hybrid retrieval
3. Golden dataset and synthetic evaluation data
4. Hit rate, MRR and NDCG

## Key takeaways

- Closed schema, validated, resolved, with provenance
- Vectors start, graph expands, filter every hop
- Real questions, synthetic coverage, held-out split
- Measure at the k you actually send

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_closed_schema_in_pydantic.py` | A closed schema in Pydantic | yes |
| `code/02_off_schema_output_fails.py` | Off-schema output fails | yes |
| `code/03_one_golden_record.py` | One golden record | yes |
| `code/04_hit_rate_and_mrr_in_code.py` | Hit rate and MRR in code | yes |
| `code/05_ndcg_at_k_in_code.py` | NDCG at k in code | yes |
| `code/06_lab_watch_hit_rate_climb_with_k.py` | Watch hit rate climb with k | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_watch_hit_rate_climb_with_k.py` prints:

```text
hit rate@1: 0.33
hit rate@2: 0.67
hit rate@3: 1.00
MRR: 0.61
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your graph has WORKS_WITH, COLLABORATES_WITH and PARTNERS_WITH for one fact. What fixes it?**

- A. Let the model invent more types
- B. A bigger extraction model
- C. Closed schema, validation, entity resolution

<details><summary>Answer</summary>

**C. Closed schema, validation, entity resolution**. Closed schema, validation, entity resolution

</details>

**2. Chunk A is visible, but links to a restricted document. Where must filtering happen?**

- A. At every hop, server side, default deny
- B. In the prompt, by asking the model
- C. Only on the first vector search

<details><summary>Answer</summary>

**A. At every hop, server side, default deny**. Filter every hop, server side, default deny

</details>

**3. You generated 1,000 synthetic questions and they score very well. Why?**

- A. Your retriever is truly excellent
- B. They reuse the chunk's own words
- C. A thousand questions covers every case

<details><summary>Answer</summary>

**B. They reuse the chunk's own words**. Synthetic scores overstate recall; check with real questions

</details>

**4. You send five chunks to the model but report hit rate@50. What is wrong?**

- A. Measure at the k you actually use
- B. Nothing, a bigger k is more complete
- C. You should report only NDCG

<details><summary>Answer</summary>

**A. Measure at the k you actually use**. Measure at the k you actually send

</details>

## Say it in the interview

**Extraction in the interview**

- Extraction is a structured output problem
- Entity resolution is the hard part
- Measure extraction precision before trusting it

**Hybrid retrieval in the interview**

- Vectors find the start, graph finds connections
- Bound the hops, then rerank
- Permissions apply to every traversed node

**Eval data in the interview**

- Gate releases on real questions
- Synthetic widens coverage but overstates recall
- Mix both, review, keep a held-out set

**Retrieval metrics in the interview**

- Hit rate: there at all. MRR: how high.
- NDCG: ordering of all relevant chunks
- Hit rate for owners, MRR for rerankers

## Homework

- [ ] Write a three-type, three-relation schema
- [ ] Write five golden records from real questions
- [ ] Add NDCG to the lab code
