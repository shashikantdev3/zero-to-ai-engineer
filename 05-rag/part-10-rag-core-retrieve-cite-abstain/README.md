# RAG and Vector Search · Part 10 of 26: RAG Core: Retrieve, Cite, Abstain

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Retrieval-augmented generation
2. Offline indexing and online query path
3. Grounding and citations
4. Abstain, never guess
5. Index freshness

## Key takeaways

- Retrieve, then generate; weights never change
- Two pipelines, one index, rerun safely
- Validate ids; eval groundedness separately
- Refuse in code on a calibrated score
- Monitor lag, delete superseded content

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_retrieval_with_a_permission_filter.py` | Retrieval with a permission filter | yes |
| `code/02_calling_the_model.py` | Calling the model | yes |
| `code/03_the_answer_function.py` | The answer function | yes |
| `code/04_lab_an_idempotent_sync_job.py` | An idempotent sync job | yes |
| `code/05_a_citation_validator.py` | A citation validator | yes |
| `code/06_testing_the_validator.py` | Testing the validator | yes |
| `code/07_gate_on_the_reranker_score.py` | Gate on the reranker score | yes |
| `code/08_testing_the_gate.py` | Testing the gate | yes |
| `code/09_measuring_index_lag.py` | Measuring index lag | yes |
| `code/10_a_freshness_scoring_profile.py` | A freshness scoring profile | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_an_idempotent_sync_job.py` prints:

```text
'ab' 2 chunks
'ab' 2 chunks
'ac' 2 chunks
'' 0 chunks
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does RAG teach the model your company's data?**

- A. Yes, it updates the model's weights
- B. Yes, after enough questions
- C. No, it reads passages at question time

<details><summary>Answer</summary>

**C. No, it reads passages at question time**. Facts in retrieval, behaviour in weights

</details>

**2. A document is deleted at the source. What must ingestion do?**

- A. Delete its chunks from the index
- B. Lower that document's ranking
- C. Nothing, the chunks can stay

<details><summary>Answer</summary>

**A. Delete its chunks from the index**. Ingestion is a pipeline, not a script

</details>

**3. The model cites a chunk that was retrieved. Is it grounded?**

- A. Not proven, the chunk may disagree
- B. Yes, a valid id proves it
- C. Yes, because the prompt said cite

<details><summary>Answer</summary>

**A. Not proven, the chunk may disagree**. A valid id is not proof of support

</details>

**4. Should you refuse when the hybrid RRF score is below 0.5?**

- A. Yes, 0.5 is a safe middle
- B. No, RRF scores are rank-based
- C. Yes, if tuned once per index

<details><summary>Answer</summary>

**B. No, RRF scores are rank-based**. Threshold the reranker score, never RRF

</details>

**5. You re-index weekly. What happens to a policy withdrawn on Monday?**

- A. The freshness boost hides it
- B. It is served until the next run
- C. It disappears from answers at once

<details><summary>Answer</summary>

**B. It is served until the next run**. Event-driven deletes, monitored lag

</details>

## Say it in the interview

**Explaining RAG**

- Retrieve first, then generate
- Fresh answers, citations, access control
- No prompt fixes a bad corpus

**Explaining the two pipelines**

- Two systems sharing one index
- Online has a latency budget
- Most failures live offline

**Explaining citations**

- From trust me to check me
- Code checks every cited id
- Quote exists is not quote supports

**Explaining abstention**

- I do not know must be available
- Decide in code, hand to a human
- Reranker score, plus refusal rate

**Explaining index freshness**

- A stale index fails silently
- Lag alerts, propagated deletes, document dates
- A boost never replaces a delete

## Homework

- [ ] Run the sync lab, add a chunk
- [ ] Test the permission filter, two users
- [ ] Break the citation validator three ways
- [ ] Write the RAG answer in three sentences
