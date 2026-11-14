# RAG and Vector Search · Part 13 of 26: Securing and Pricing RAG in Production

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. The corpus as an injection surface
2. Question drill: RAG core in production
3. RAG cost per query and its levers
4. Vector and embedding weaknesses

## Key takeaways

- Corpus writers are prompt writers.
- Delete on update. Retrieve per turn. State windows.
- Cost is mostly chunk input tokens.
- Protect and erase vectors like the source.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_cost_of_one_query_in_code.py` | Cost of one query in code | yes |
| `code/02_lab_pull_the_cost_levers_yourself.py` | Pull the cost levers yourself | yes |
| `code/03_stand_ins_for_store_and_cache.py` | Stand ins for store and cache | yes |
| `code/04_a_deletion_check_for_nightly_runs.py` | A deletion check for nightly runs | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_pull_the_cost_levers_yourself.py` prints:

```text
base: 0.02565
fewer chunks: 0.01815
trim history: 0.01575
cap output: 0.01350
saved: 47%
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. We validate user input. Is prompt injection handled?**

- A. No, retrieved documents bypass it
- B. Yes, validation covers it
- C. Only if the model is large

<details><summary>Answer</summary>

**A. No, retrieved documents bypass it**. Input validation does nothing for retrieved content.

</details>

**2. Our refusal rate is very low. Is that good news?**

- A. Not alone, check false answers too
- B. Yes, users get more answers
- C. Only if latency is also low

<details><summary>Answer</summary>

**A. Not alone, check false answers too**. Low refusals can mean the system is guessing.

</details>

**3. To cut RAG cost, should we switch to a cheaper embedding model?**

- A. Yes, embeddings are the main cost
- B. No, chunk input tokens dominate
- C. Yes, and re-embed every night

<details><summary>Answer</summary>

**B. No, chunk input tokens dominate**. Split one query's cost before cutting anything.

</details>

**4. Embeddings are just numbers. Does that make them anonymised?**

- A. Yes, text cannot be recovered
- B. Only after you normalise them
- C. No, text can be largely reconstructed

<details><summary>Answer</summary>

**C. No, text can be largely reconstructed**. Vectors need the same protection as documents.

</details>

## Say it in the interview

**Who can write to the corpus?**

- Who can write to the corpus?
- The attacker is a document, not the user.
- Open sources: reviewed, excluded, or read only.

**How I would cut RAG cost**

- The bill is mostly chunks, not embeddings.
- Three or four strong chunks, not fifteen.
- Report cost per resolved question.

**Treat vectors like the documents**

- Vectors hold the same data as documents.
- Same access control, encryption, retention.
- Delete means vectors, caches, and summaries too.

## Homework

- [ ] List who can edit each indexed source.
- [ ] Run the cost function with your numbers.
- [ ] Answer the rapid fire questions from memory.
- [ ] Write an erasure check for vectors and caches.
