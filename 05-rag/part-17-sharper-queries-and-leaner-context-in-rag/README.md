# RAG and Vector Search · Part 17 of 26: Sharper Queries and Leaner Context in RAG

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Query rewriting
2. Multi-query retrieval
3. HyDE
4. Self-query retrieval
5. Contextual compression
6. Parent-document retrieval

## Key takeaways

- Standalone query; log original and rewrite.
- Several phrasings, fused with RRF.
- Search with a draft, never show it.
- Model proposes filters; code adds permissions.
- Trim chunks, cite originals, evaluate.
- Match children, send capped parents.

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_building_the_rewrite_prompt.py` | Building the rewrite prompt | yes |
| `code/02_one_small_model_call.py` | One small model call | yes |
| `code/03_fusion_and_a_stand_in_search.py` | Fusion and a stand-in search | yes |
| `code/04_running_the_phrasings_in_parallel.py` | Running the phrasings in parallel | yes |
| `code/05_asking_for_a_hypothetical_passage.py` | Asking for a hypothetical passage | yes |
| `code/06_searching_with_the_draft.py` | Searching with the draft | yes |
| `code/07_a_schema_for_the_search_plan.py` | A schema for the search plan | yes |
| `code/08_code_builds_the_user_filter.py` | Code builds the user filter | yes |
| `code/09_permissions_added_by_code.py` | Permissions added by code | yes |
| `code/10_lab_a_toy_compressor_drops_a_rule.py` | A toy compressor drops a rule | yes |
| `code/11_a_parent_store_and_child_hits.py` | A parent store and child hits | yes |
| `code/12_from_children_to_parents.py` | From children to parents | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/10_lab_a_toy_compressor_drops_a_rule.py` prints:

```text
sentences before: 3
sentences after: 1
cafe kept: False
exception kept: False
```

## Try it without a key

- [Google AI Studio](https://aistudio.google.com): A real model with temperature, top-p, thinking level and output length controls. Needs a Google account, no credit card. Do not paste private data: free-tier prompts may be used to improve Google products.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What should you do if a rewrite changes the meaning of the question?**

- A. Log it, evaluate, keep original as fallback
- B. Always search with the rewrite only
- C. Let it add helpful extra facts

<details><summary>Answer</summary>

**A. Log it, evaluate, keep original as fallback**. Rewrites resolve references. They never add facts.

</details>

**2. Should you run multi-query retrieval on every request?**

- A. Yes, if searches run one by one
- B. Yes, more queries always help
- C. Only where evals show recall misses

<details><summary>Answer</summary>

**C. Only where evals show recall misses**. Parallel calls, and only where recall needs it.

</details>

**3. In HyDE, what happens to the generated draft answer?**

- A. Stored in the index as a document
- B. Embedded for search, then thrown away
- C. Shown to the user as the answer

<details><summary>Answer</summary>

**B. Embedded for search, then thrown away**. The draft steers search. It is never the answer.

</details>

**4. What if the model's filter drops the tenant clause?**

- A. Ask the model to include it again
- B. Code adds tenant and permission filters
- C. Trust the model's whole filter string

<details><summary>Answer</summary>

**B. Code adds tenant and permission filters**. Tenant and permission filters come from code.

</details>

**5. Is contextual compression free accuracy?**

- A. Yes, fewer tokens mean better answers
- B. Yes, the model ignores noise anyway
- C. No, it can drop the exception clause

<details><summary>Answer</summary>

**C. No, it can drop the exception clause**. Compression can cut the sentence that mattered.

</details>

**6. Parent sections can be huge. How do you protect the token budget?**

- A. Cap parent size, or use sentence window
- B. Switch to bigger child chunks
- C. Send every parent in full anyway

<details><summary>Answer</summary>

**A. Cap parent size, or use sentence window**. Cap parents, or fall back to sentence window.

</details>

## Say it in the interview

**Say it: query rewriting**

- Rewrite the message into a standalone query.
- One small, cheap model call.
- Log both. Bad rewrites are a common cause.

**Say it: multi-query retrieval**

- Several phrasings catch different wording.
- Parallel searches, fused with RRF.
- Use it where evals show recall misses.

**Say it: HyDE**

- Search with an answer-shaped draft.
- The draft is never shown.
- Evaluate against plain search before adopting.

**Say it: self-query retrieval**

- The model fills in implied filters.
- Validate every field against a schema.
- Permissions come from code, never the model.

**Say it: contextual compression**

- Trim chunks to what matters.
- It can drop the exception clause.
- Cite originals. Compare groundedness both ways.

**Say it: parent-document retrieval**

- Match small, return big.
- Children point to parents. Deduplicate.
- Great when the exception follows the rule.

## Homework

- [ ] Rewrite three vague follow-ups as standalone queries
- [ ] Fuse two ranked lists with RRF by hand
- [ ] Make the lab keep the exception
- [ ] Sketch a two-field self-query schema
