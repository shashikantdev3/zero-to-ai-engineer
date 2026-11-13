# LLM Fundamentals · Part 3 of 18: Scaling Laws, Context Windows and Chat Costs

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Scaling laws and compute-optimal training
2. Context window
3. Lost in the middle
4. Stateless chat APIs

## Key takeaways

- About 20 tokens per parameter; over-train small models
- One window for everything; treat it as budget
- Position and volume matter; keep context short
- History resent every turn; caching discounts, not shrinks

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_chinchilla_maths_for_8b_params.py` | Chinchilla maths for 8B params | yes |
| `code/02_will_this_request_fit.py` | Will this request fit? | yes |
| `code/03_a_position_test_for_evals.py` | A position test for evals | yes |
| `code/04_watch_prompt_tokens_grow.py` | Watch prompt tokens grow | yes |
| `code/05_lab_count_a_pasted_emails_cost.py` | Count a pasted email's cost | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_count_a_pasted_emails_cost.py` prints:

```text
turn 1: 3000 email tokens
turn 2: 3000 email tokens
turn 3: 3000 email tokens
turn 4: 3000 email tokens
email billed: 12000 tokens
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Why are 8B models trained on trillions of tokens?**

- A. Chinchilla requires trillions of tokens
- B. It lowers lifetime inference cost
- C. Bigger models always win anyway

<details><summary>Answer</summary>

**B. It lowers lifetime inference cost**. Twenty per parameter optimises training, not serving

</details>

**2. Context windows are huge now. Is RAG dead?**

- A. Yes, if the documents fit the window
- B. Yes, just send every document
- C. No, cost, latency and freshness still matter

<details><summary>Answer</summary>

**C. No, cost, latency and freshness still matter**. A big window does not replace picking context

</details>

**3. Accuracy dropped after raising top-k from 5 to 50. Why?**

- A. The right chunk got buried among others
- B. Fifty chunks always beats five
- C. The model forgot its system prompt

<details><summary>Answer</summary>

**A. The right chunk got buried among others**. More context can make answers worse

</details>

**4. Does prompt caching make long chats free?**

- A. No, it discounts repeats, tokens still count
- B. Yes, once the server stores the chat
- C. Yes, cached tokens leave the window

<details><summary>Answer</summary>

**A. No, it discounts repeats, tokens still count**. Caching discounts repeats; it never shrinks context

</details>

## Say it in the interview

**Scaling laws in the interview**

- Loss falls predictably; about 20 tokens per parameter
- Training is paid once, inference every call
- Small model first, decided per task with evals

**Context window in the interview**

- Working memory for one request, shared by all
- A budget, not a bucket
- Few chunks, trimmed history, short tool lists

**Lost in the middle, answered**

- Middle placement hurt; newer models vary
- Short, ranked context; key instruction at the end
- Test positions on your own eval set

**Stateless chat in the interview**

- One pasted email, billed four times
- Strip, summarise, retrieve instead of resending
- Stable prefix first; caching doesn't shrink context

## Homework

- [ ] Compute Chinchilla tokens and FLOPs for one size
- [ ] Find training tokens on one model card
- [ ] Rerun the lab with new sizes and turns
- [ ] Sketch a start, middle, end position test
