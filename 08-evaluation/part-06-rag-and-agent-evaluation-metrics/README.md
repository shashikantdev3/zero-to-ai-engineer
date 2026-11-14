# Evaluation · Part 6 of 11: RAG and Agent Evaluation Metrics

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Context precision and context recall
2. Groundedness and faithfulness
3. Answer relevance
4. The RAG triad
5. Trajectory evals for agents

## Key takeaways

- Recall: everything needed. Precision: useful, on top.
- Every claim supported, but context may be stale.
- Did it answer the question asked?
- Three links, no gold answer, runs online.
- Grade the path, not just the answer.

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_rank_weighted_context_precision.py` | Rank-weighted context precision | yes |
| `code/02_lab_move_good_chunks_watch_the_score.py` | Move good chunks, watch the score | yes |
| `code/03_the_groundedness_judge_prompt.py` | The groundedness judge prompt | yes |
| `code/04_scoring_the_share_of_supported_claims.py` | Scoring the share of supported claims | yes |
| `code/05_a_toy_judge_quote_matching.py` | A toy judge: quote matching | yes |
| `code/06_a_rubric_judge_prompt.py` | A rubric judge prompt | yes |
| `code/07_running_the_judge_with_claude.py` | Running the judge with Claude | with your API key |
| `code/08_the_triad_as_three_scores.py` | The triad as three scores | yes |
| `code/09_grading_a_logged_trajectory.py` | Grading a logged trajectory | yes |
| `code/10_a_run_that_called_delete.py` | A run that called delete | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_move_good_chunks_watch_the_score.py` prints:

```text
top 1.0
bottom 0.42
none 0.0
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. In Ragas, does context recall need a reference answer?**

- A. No, it only reads the question
- B. No, it only counts relevant chunks
- C. Yes, it checks the reference's claims

<details><summary>Answer</summary>

**C. Yes, it checks the reference's claims**. Know exactly how your tool computes each metric.

</details>

**2. An answer scores 100% groundedness. Is it correct?**

- A. Not necessarily, the context may be wrong
- B. Yes, every claim is supported
- C. Yes, if an LLM judged it

<details><summary>Answer</summary>

**A. Not necessarily, the context may be wrong**. Grounded means faithful to context, not correct.

</details>

**3. Your judge rates longer answers as more relevant. What is wrong?**

- A. The judge has a length bias
- B. Longer answers really cover more
- C. Longer answers are better grounded

<details><summary>Answer</summary>

**A. The judge has a length bias**. Watch for length bias in relevance judges.

</details>

**4. All three triad checks pass on a superseded policy. What catches it?**

- A. A stricter groundedness threshold
- B. A freshness check on the index
- C. Nothing, the triad proves correctness

<details><summary>Answer</summary>

**B. A freshness check on the index**. The triad does not prove correctness.

</details>

**5. The answer was right, but the agent called delete on the way. Pass or fail?**

- A. Pass, the final answer was right
- B. Fail, a forbidden action was taken
- C. Pass, if within the step budget

<details><summary>Answer</summary>

**B. Fail, a forbidden action was taken**. Grade the trajectory, not only the final message.

</details>

## Say it in the interview

**Say it in the interview**

- Recall: everything needed. Precision: useful, on top.
- Fifty chunks: high recall, dead precision.
- Rerank, keep a few strong chunks, measure both.

**Say it in the interview**

- One invented sentence cannot hide behind nine.
- Calibrate with kappa against expert labels first.
- Faithful to context is not the same as true.

**Say it in the interview**

- Grounded can still be useless.
- Answer it, cover every part, no padding.
- Low scores on refusals catch over-refusal.

**Say it in the interview**

- Three arrows show where it broke.
- No gold answer: runs on live traffic.
- Pair it with freshness checks.

**Say it in the interview**

- Right answer, wrong path, still a failure.
- Tools, arguments, order, budget, final state.
- It needs full logging of every step.

## Homework

- [ ] Run the lab with your own rankings.
- [ ] Write a one-claim groundedness judge prompt.
- [ ] Sketch the RAG triad for a known system.
- [ ] List forbidden tools for one agent task.
