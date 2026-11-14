# RAG and Vector Search · Part 4 of 26: Compress, Filter, and Choose a Vector Store

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Quantisation of vectors
2. Filtered search, prefilter versus postfilter
3. pgvector
4. The vector database landscape

## Key takeaways

- Search compressed, rescore with originals
- Prefilter, always for access control
- pgvector: check iterative scans, dimension limit
- Choose the store by requirements, not brand

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_product_quantisation_in_faiss.py` | Product quantisation in Faiss | yes |
| `code/02_a_prefilter_in_azure_ai_search.py` | A prefilter in Azure AI Search | yes |
| `code/03_lab_watch_postfilter_run_dry.py` | Watch postfilter run dry | yes |
| `code/04_the_table_and_its_index.py` | The table and its index | yes |
| `code/05_the_filtered_query.py` | The filtered query | yes |
| `code/06_the_shape_of_a_pinecone_query.py` | The shape of a Pinecone query | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_watch_postfilter_run_dry.py` prints:

```text
eligible docs: 10
postfilter, k=10: 0
postfilter, k=100: 2
prefilter, k=10: 10
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Quantisation cost you some recall. How do you get it back?**

- A. Oversample, then rescore with full vectors
- B. Switch to binary quantisation
- C. Nothing, quantisation never loses recall

<details><summary>Answer</summary>

**A. Oversample, then rescore with full vectors**. Oversample, then rescore with full-precision vectors

</details>

**2. Only 0.1% of documents match the filter. What should you do?**

- A. Postfilter, and just ask for more results
- B. Prefilter, so only eligible vectors compete
- C. Postfilter with k of ten

<details><summary>Answer</summary>

**B. Prefilter, so only eligible vectors compete**. Selective filter? Prefilter. Raising k only partly helps.

</details>

**3. When does relational Postgres beat a dedicated vector database?**

- A. Strong filters, joins, transactions, existing ops
- B. Only when vectors exceed 2,000 dimensions
- C. Never, Postgres cannot do vectors at scale

<details><summary>Answer</summary>

**A. Strong filters, joins, transactions, existing ops**. Relational wins: filters, joins, transactions, existing ops

</details>

**4. In FAISS, how do you delete a document and enforce permissions?**

- A. Use the built-in FAISS access control
- B. Save the index, permissions come free
- C. You build that layer yourself

<details><summary>Answer</summary>

**C. You build that layer yourself**. Faiss is a library: storage and permissions are yours

</details>

## Say it in the interview

**Say it in the interview**

- A little recall for a lot of memory
- Cheap compressed search, then full-precision rescore
- Measure recall at ten before and after

**Say it in the interview**

- Postfilter can leave two results, or none
- Prefilter keeps every top k result eligible
- Access control: prefilter, test selective filters

**Say it in the interview**

- On Postgres with relational filters? pgvector
- Check iterative scans and the dimension limit
- Huge scale or serverless: dedicated vector database

**Say it in the interview**

- Pick by requirements, not brand
- Postgres: pgvector. Managed: Pinecone. Notebook: Chroma.
- With Faiss, you build storage and access control

## Homework

- [ ] Bytes per vector: float32, int8, binary
- [ ] Rerun the lab with a stricter filter
- [ ] Write pgvector's three operators from memory
- [ ] Choose a store for a Postgres team
