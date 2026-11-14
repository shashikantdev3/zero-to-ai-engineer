# RAG and Vector Search · Part 19 of 26: Images, Permissions, Honest Numbers, Split Questions

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Multimodal RAG
2. Permission-trimmed retrieval
3. Contextual retrieval: quoting the numbers correctly
4. Query decomposition and step-back prompting

## Key takeaways

- Caption and OCR at ingest, cite the image
- Filter before retrieval, deny by default
- 35 from context, 67 with reranker
- Route it, cap it, measure it

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_chunk_record_for_a_diagram.py` | A Chunk Record for a Diagram | yes |
| `code/02_resolving_the_users_groups.py` | Resolving the User's Groups | yes |
| `code/03_building_the_deny_by_default_filter.py` | Building the Deny-by-Default Filter | yes |
| `code/04_lab_trim_a_tiny_index_yourself.py` | Trim a Tiny Index Yourself | yes |
| `code/05_preparing_the_context_prompt.py` | Preparing the Context Prompt | yes |
| `code/06_one_text_for_both_indexes.py` | One Text for Both Indexes | yes |
| `code/07_splitting_the_question.py` | Splitting the Question | yes |
| `code/08_retrieve_each_then_compare.py` | Retrieve Each, Then Compare | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_trim_a_tiny_index_yourself.py` prints:

```text
hr user: ['hr1', 'pub']
legal: ['canary']
no groups: denied: no groups
canary seen by hr: False
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your manuals are full of scanned diagrams. When should you process the images?**

- A. At ingest, then retrieve text
- B. Skip the images entirely
- C. Send every page to a vision model per query

<details><summary>Answer</summary>

**A. At ingest, then retrieve text**. Convert at ingest, retrieve text, show the image

</details>

**2. The system prompt tells the model to hide restricted documents. What goes wrong?**

- A. Only the latency gets worse
- B. Injection can leak content already in context
- C. Nothing, system prompts are always obeyed

<details><summary>Answer</summary>

**B. Injection can leak content already in context**. Filter before retrieval; sync access lists like content

</details>

**3. Contextual retrieval cuts failures by 67%. Which setup produced that number?**

- A. Context plus BM25 plus a reranker
- B. Contextual embeddings alone
- C. Contextual BM25 alone

<details><summary>Answer</summary>

**A. Context plus BM25 plus a reranker**. 67 needs the reranker; context alone is 35

</details>

**4. Should every question be decomposed to improve recall?**

- A. Yes, recall always improves
- B. Yes, but always add step-back too
- C. No, route it; simple lookups gain nothing

<details><summary>Answer</summary>

**C. No, route it; simple lookups gain nothing**. Extra calls for no gain; route it

</details>

## Say it in the interview

**Say It: Multimodal RAG**

- OCR and captions at ingest, with a pointer
- Searchable as text, cited as an image
- Easier to evaluate, so start there

**Say It: Permission Trimming**

- Enforce at retrieval, not in the prompt
- Verified identity, prefilter, default deny
- Handle overage through Microsoft Graph, cached

**Say It: Contextual Retrieval**

- Embeddings 35, plus keyword index 49
- 67 percent includes the reranker
- Trial it on your golden set first

**Say It: Decompose and Step Back**

- One sub-question per document, then compare
- Too specific? Retrieve the general rule first
- Route them, then measure on the golden set

## Homework

- [ ] Write a chunk record for one diagram
- [ ] Add a second canary document to the lab
- [ ] Write 35, 49, 67 and their causes
- [ ] Decompose one hard question by hand
