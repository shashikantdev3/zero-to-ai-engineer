# RAG and Vector Search · Part 7 of 26: Where Vector Search Quietly Loses Recall

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Oversampling and rescoring
2. Filtered graph search and recall collapse
3. Azure semantic ranker: tune recall at 50
4. Azure AI Search capacity limits for tenancy

## Key takeaways

- Search compressed wide, rescore with kept originals
- In-graph filters risk islands; selective ones scan
- Ranker sees top 50: measure both stages
- Tier caps indexes; partitions add capacity

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_rescoring_options_in_azure_ai_search.py` | Rescoring Options in Azure AI Search | yes |
| `code/02_index_the_filter_field.py` | Index the Filter Field | after `pip install qdrant_client` |
| `code/03_hit_rate_at_k.py` | Hit Rate at K | yes |
| `code/04_measure_both_stages.py` | Measure Both Stages | yes |
| `code/05_lab_the_tenant_planning_check.py` | The Tenant Planning Check | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_the_tenant_planning_check.py` prints:

```text
indexes needed: 60
S1 cap 50: too many
S2 cap 200: fits
S3 cap 200: fits
vector bytes: 6.14 GB
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your index kept only the compressed vectors. Can you still rescore?**

- A. Yes, just raise the oversampling
- B. No, the originals are gone
- C. Yes, rescoring is always free

<details><summary>Answer</summary>

**B. No, the originals are gone**. Keeping originals is decided at index creation

</details>

**2. Which filters are usually cheapest in vector search?**

- A. Very selective ones, via direct scan
- B. None, filtering always slows search
- C. Broad filters matching most rows

<details><summary>Answer</summary>

**A. Very selective ones, via direct scan**. Very selective filters: direct scan beats the graph

</details>

**3. Which filtering style can strand the walk on islands?**

- A. Filtering inside the graph walk
- B. Extra edges built per field
- C. Post-filtering after the walk

<details><summary>Answer</summary>

**A. Filtering inside the graph walk**. Post-filter loses count; in-graph filter risks islands

</details>

**4. The right chunk ranks 60th in hybrid results. Can the semantic ranker save it?**

- A. Yes, if hit rate at 10 is good
- B. No, it only sees the top 50
- C. Yes, the reranker fixes ordering

<details><summary>Answer</summary>

**B. No, it only sees the top 50**. Below rank 50 is invisible to the ranker

</details>

**5. On Azure AI Search, what adds vector capacity?**

- A. Adding more replicas
- B. Creating more indexes per tenant
- C. Partitions, or a higher tier

<details><summary>Answer</summary>

**C. Partitions, or a higher tier**. Replicas add throughput; partitions add capacity

</details>

## Say it in the interview

**Say It: Oversampling and Rescoring**

- Search compressed vectors wide, four times over
- Rescore the candidates with full-precision originals
- Tune oversampling against recall like any knob

**Say It: Filtered Graph Search**

- Post-filtering leaves too few rows
- In-graph filtering risks islands; engines choose per query
- Selective entitlement filters favour direct scan

**Say It: Recall at Fifty**

- The ranker only sees the first-stage top 50
- Measure hit rate at 50, then at 5
- Check the raw hybrid rank first

**Say It: Tenancy Limits**

- Index per tenant is a tier decision
- Shared index, tenant from a validated token
- Size vector storage per partition

## Homework

- [ ] Explain oversampling with 10 results, 40 candidates
- [ ] Write hit rate at k from memory
- [ ] Rerun the planning check for 100 tenants
