# RAG and Vector Search · Part 23 of 26: Measuring RAG Quality and Finding Failures

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Context precision, context recall and faithfulness
2. Answerable, partially answerable and unanswerable cases
3. Context recall against the reference answer
4. The diagnostic ladder

## Key takeaways

- Faithful is not correct. Stale data still fails.
- Test refusal. Never trust the blended score.
- Recall from reference claims. Fix it first.
- Climb the ladder. The prompt is not step one.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_golden_case_marked_unanswerable.py` | A golden case marked unanswerable | yes |
| `code/02_lab_lab_the_blended_score_trap.py` | Lab: the blended score trap | yes |
| `code/03_a_toy_judge.py` | A toy judge | yes |
| `code/04_the_context_recall_function.py` | The context recall function | yes |
| `code/05_a_logged_trace.py` | A logged trace | yes |
| `code/06_walking_the_ladder_in_code.py` | Walking the ladder in code | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_lab_the_blended_score_trap.py` prints:

```text
answerable 1.0
unanswerable 0.0
blended 0.6
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. An answer scores perfect faithfulness. Is it correct?**

- A. Yes, faithful means correct
- B. Only if precision is also high
- C. Not always, the document may be stale

<details><summary>Answer</summary>

**C. Not always, the document may be stale**. Faithful to a stale document is still wrong

</details>

**2. Your golden set is all real, answerable questions. Do you know it refuses?**

- A. No, not until unanswerable cases exist
- B. Yes, if answer accuracy is high
- C. Yes, partial cases test refusal

<details><summary>Answer</summary>

**A. No, not until unanswerable cases exist**. No unanswerable cases, no proof of refusal

</details>

**3. In RAGAS, context recall is checked against what?**

- A. Claims in the reference answer
- B. Every relevant chunk in the corpus
- C. Keywords from the user's question

<details><summary>Answer</summary>

**A. Claims in the reference answer**. Recall uses claims from the reference answer

</details>

**4. It worked last month, nothing was deployed, now answers are wrong. Check first?**

- A. Switch to a larger model
- B. The corpus and its refresh
- C. Rewrite the prompt

<details><summary>Answer</summary>

**B. The corpus and its refresh**. Nothing deployed? The corpus changed.

</details>

## Say it in the interview

**Say it in the interview**

- Split quality into retrieval and generation
- Faithful but wrong: recall, ranking or staleness
- Calibrate the judge before it gates releases

**Say it in the interview**

- Most golden sets never test refusal
- Answerable, partial, unanswerable: three separate tests
- A blended number hides the dangerous case

**Say it in the interview**

- Recall is measured against the reference answer
- Chunk ids for hit rate, answers for recall
- No reranker promotes a passage never retrieved

**Say it in the interview**

- Start from failing cases, not the prompt
- Index, ranking, prompt use, then the model
- No deploy? Check the corpus first

## Homework

- [ ] Add three unanswerable questions
- [ ] Write five reference answers
- [ ] Add a partial case to the lab
- [ ] Trigger every rung of diagnose
