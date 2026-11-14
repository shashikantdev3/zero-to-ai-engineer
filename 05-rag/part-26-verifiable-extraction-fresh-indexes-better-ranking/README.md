# RAG and Vector Search · Part 26 of 26: Verifiable Extraction, Fresh Indexes, Better Ranking

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Extract rather than describe
2. Question drill: Document AI verification
3. Change and deletion detection in Azure AI Search indexers
4. MMR
5. Domain-adapting the embedder or reranker

## Key takeaways

- Extract: confidence and coordinates make values checkable
- One chunk per slide; budget images separately
- Hard deletes need a deletion policy or push
- MMR balances relevance and repetition; tune lambda
- Reranker first; never train on the golden set

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_keep_the_page_and_polygon.py` | Keep the page and polygon | yes |
| `code/02_a_change_detection_policy.py` | A change detection policy | yes |
| `code/03_add_a_deletion_detection_policy.py` | Add a deletion detection policy | yes |
| `code/04_redundancy_closest_to_anything_picked.py` | Redundancy: closest to anything picked | yes |
| `code/05_the_mmr_loop.py` | The MMR loop | yes |
| `code/06_lab_watch_lambda_change_the_pick.py` | Watch lambda change the pick | yes |
| `code/07_training_triples_with_hard_negatives.py` | Training triples with hard negatives | after `pip install sentence-transformers` |
| `code/08_train_with_in_batch_negatives.py` | Train with in-batch negatives | after `pip install sentence-transformers torch` |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_watch_lambda_change_the_pick.py` prints:

```text
first pick: A (most relevant)
lam 1.0: A2 0.940 B 0.800 -> A2
lam 0.7: A2 0.361 B 0.470 -> B
lam 0.5: A2 -0.025 B 0.250 -> B
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A vision model reads the page well. Why still use extraction?**

- A. Extraction always costs fewer tokens
- B. Extraction gives confidence and coordinates
- C. Vision models cannot read scanned text

<details><summary>Answer</summary>

**B. Extraction gives confidence and coordinates**. Unverifiable values cannot be routed or cited

</details>

**2. In a context budget, does an image count as one chunk?**

- A. Yes, one image equals one chunk
- B. No, it can cost many tokens
- C. Only when it has a caption

<details><summary>Answer</summary>

**B. No, it can cost many tokens**. Budget images separately; they cost many tokens

</details>

**3. A policy file was hard-deleted at the source. When does it leave the index?**

- A. Never, without deletion detection or push
- B. At the next scheduled indexer run
- C. When the index cache expires

<details><summary>Answer</summary>

**A. Never, without deletion detection or push**. Schedules do not catch hard deletes

</details>

**4. The answer needs two near-identical clauses from different years. What does a low lambda risk?**

- A. It pushes both clauses to the top
- B. Nothing, both are highly relevant
- C. It may drop one of the clauses

<details><summary>Answer</summary>

**C. It may drop one of the clauses**. Tune lambda on evals; delete stale versions

</details>

**5. General models miss your jargon, and no general model knows it. What next?**

- A. Domain-adapt, starting with the reranker
- B. Switch to another general model
- C. Fine-tune on the golden set questions

<details><summary>Answer</summary>

**A. Domain-adapt, starting with the reranker**. Adapt the reranker first; keep the golden set out

</details>

## Say it in the interview

**Say it in the interview**

- I extract rather than describe.
- Confidence routes; coordinates highlight the source.
- Descriptions only for diagrams.

**Say it in the interview**

- A change policy finds updates.
- Hard deletes need a deletion policy or push.
- Delete a canary; confirm it disappears.

**Say it in the interview**

- Duplicates hide the second fact.
- Reward relevance, penalise repetition.
- Tune lambda on the golden set.

**Say it in the interview**

- Cheaper fixes first.
- Mined pairs, hard negatives, contrastive loss.
- Reranker first; ship only a real gain.

## Homework

- [ ] Rerun the MMR lab with new numbers
- [ ] Sketch change and deletion policies for one source
- [ ] Plan a canary delete test
- [ ] Write five queries with a hard negative each
