# RAG and Vector Search · Part 11 of 26: Long Context, Debugging, and Stale Chunks

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Long context versus RAG
2. Check retrieval first
3. Quoting a RAG accuracy benchmark honestly
4. Context rot
5. A document update is a delete plus an insert

## Key takeaways

- One document: long context. Shared corpus: RAG.
- Check retrieval before prompt or model.
- Name CRAG, its year, its hard data.
- Concede accuracy. Win on cost and focus.
- Write new chunks, then delete leftovers.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_tiny_stand_in_index.py` | A Tiny Stand-In Index | yes |
| `code/02_reindex_one_document.py` | Reindex One Document | yes |
| `code/03_lab_watch_stale_chunks_survive.py` | Watch Stale Chunks Survive | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_watch_stale_chunks_survive.py` prints:

```text
after v1: 12
upsert only: 12
stale left: 3
after delete: 9
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Context windows are huge now. Is RAG dead?**

- A. Yes, prompt caching solves the cost
- B. Yes, put the whole corpus in
- C. No, access control needs retrieval filtering

<details><summary>Answer</summary>

**C. No, access control needs retrieval filtering**. One giant prompt cannot enforce permissions.

</details>

**2. A RAG answer is wrong but the document exists. What do you do first?**

- A. Switch to a bigger model
- B. Replay the query and read the chunks
- C. Rewrite the system prompt

<details><summary>Answer</summary>

**B. Replay the query and read the chunks**. No prompt fixes a chunk never retrieved.

</details>

**3. An interviewer asks how accurate RAG is. Which answer holds up?**

- A. Name CRAG, its year, and its data
- B. RAG is 63 percent accurate
- C. RAG is accurate when retrieval works

<details><summary>Answer</summary>

**A. Name CRAG, its year, and its data**. Name CRAG and its year, or skip the number.

</details>

**4. A client's own test shows long context beating their RAG. Your move?**

- A. Concede accuracy, argue cost and permissions
- B. Say their test must be flawed
- C. Insist long context is less accurate

<details><summary>Answer</summary>

**A. Concede accuracy, argue cost and permissions**. Concede accuracy. Win on cost, permissions, focus.

</details>

**5. A policy goes from 12 chunks to 9. Does upsert alone handle the update?**

- A. Yes, if the ids are stable
- B. No, three old chunks survive
- C. Yes, upsert replaces the document

<details><summary>Answer</summary>

**B. No, three old chunks survive**. Extra old chunks survive unless deleted.

</details>

## Say it in the interview

**Long Context in the Interview**

- Every question pays for every document.
- Caching fixes cost, not permissions or freshness.
- One document: long context. Shared corpus: RAG.

**Debugging in the Interview**

- Replay the exact query as the exact user.
- Missing chunk: retrieval. Present chunk: generation.
- Debug from the trace, not from memory.

**Benchmarks in the Interview**

- CRAG 2024: about 44 and 63 percent.
- Built hard. Not your policy corpus.
- The lesson transfers. The number does not.

**Context Rot in the Interview**

- Concede accuracy where it is true.
- Cost, citations, access control, then focus.
- Not cannot read it. Should not make it.

**Updates in the Interview**

- An update treated as an insert breeds staleness.
- No error. Evals pass. Old text wins.
- Key by document id. Write, then delete.

## Homework

- [ ] Write why long context does not kill RAG
- [ ] List your per-request retrieval log fields
- [ ] Rerun the lab: twelve chunks, then seven
- [ ] Practise the CRAG caveat with its year
