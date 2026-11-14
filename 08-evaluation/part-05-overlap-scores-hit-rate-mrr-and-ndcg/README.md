# Evaluation · Part 5 of 11: Overlap Scores, Hit Rate, MRR and NDCG

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Text overlap metrics: BLEU, ROUGE, BERTScore
2. Retrieval hit rate and recall@k
3. MRR (Mean Reciprocal Rank)
4. NDCG

## Key takeaways

- Overlap is a drift alarm, not a gate
- Measure retrieval on chunks the model sees
- MRR: how high the first hit sits
- NDCG: graded ranking versus the true ideal

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_rouge_on_a_correct_paraphrase.py` | ROUGE on a correct paraphrase | after `pip install rouge_score` |
| `code/02_hit_rate_at_k_in_code.py` | Hit rate at k in code | yes |
| `code/03_recall_at_k_in_code.py` | Recall at k in code | yes |
| `code/04_mrr_in_code.py` | MRR in code | yes |
| `code/05_lab_hit_rate_versus_mrr.py` | Hit rate versus MRR | yes |
| `code/06_ndcg_at_k_in_code.py` | NDCG at k in code | yes |
| `code/07_two_ndcg_cases.py` | Two NDCG cases | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_hit_rate_versus_mrr.py` prints:

```text
before hit@3: 1.0
before MRR: 0.42
after hit@3: 1.0
after MRR: 1.0
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Would ROUGE catch a fluent answer with the wrong number in it?**

- A. No, most words still match
- B. Yes, numbers carry extra weight
- C. Yes, if stemming is turned on

<details><summary>Answer</summary>

**A. No, most words still match**. Never report ROUGE as answer quality

</details>

**2. You measure hit rate on whole documents, not the chunks sent to the model. What's the risk?**

- A. None, documents are the right unit
- B. The right section may never reach the model
- C. Hit rate then needs an LLM judge

<details><summary>Answer</summary>

**B. The right section may never reach the model**. Measure the chunks actually passed to the model

</details>

**3. A query needs several documents with graded relevance. Which metric fits?**

- A. NDCG
- B. Hit rate at k
- C. MRR

<details><summary>Answer</summary>

**A. NDCG**. MRR only counts the first hit

</details>

**4. If a relevant document was never retrieved, does your NDCG notice?**

- A. Yes, always, by design
- B. No, NDCG ignores missed documents
- C. Only if the ideal uses all judged docs

<details><summary>Answer</summary>

**C. Only if the ideal uses all judged docs**. Build the ideal from all known relevant documents

</details>

## Say it in the interview

**Overlap metrics, in your words**

- Overlap misses paraphrases and rewards copied words
- For RAG, prefer task metrics
- A drift alarm, not a release gate

**Hit rate, in your words**

- Retrieval quality caps answer quality
- No judge, so it runs on every change

**MRR, in your words**

- Hit rate says found. MRR says where.
- A good reranker shows up in MRR

**NDCG, in your words**

- Graded relevance, discounted by position
- Better signal, but graded labels cost more

## Homework

- [ ] Write three paraphrases, predict overlap scores
- [ ] Code hit rate and recall, test abstain cases
- [ ] Move the right document to rank four
- [ ] Compute one NDCG by hand
