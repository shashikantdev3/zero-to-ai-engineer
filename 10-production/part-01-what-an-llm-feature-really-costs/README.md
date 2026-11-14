# Production and LLMOps · Part 1 of 38: What an LLM Feature Really Costs

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Tokens times price
2. Cap the input
3. Prompt caching
4. Semantic cache

## Key takeaways

- Calls × tokens × price; reasoning bills as output
- History is resent. Cap it and compact.
- Identical prefix: static first, variable last.
- Semantic cache: generic only, per tenant.

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_monthly_cost_function.py` | A monthly cost function | yes |
| `code/02_count_tokens_before_sending.py` | Count tokens before sending | yes |
| `code/03_keep_the_newest_turns_that_fit.py` | Keep the newest turns that fit | with your API key |
| `code/04_lab_watch_history_get_billed_again.py` | Watch history get billed again | yes |
| `code/05_mark_the_static_prefix.py` | Mark the static prefix | yes |
| `code/06_read_the_real_hit_rate.py` | Read the real hit rate | with your API key |
| `code/07_a_cache_key_per_tenant.py` | A cache key per tenant | yes |
| `code/08_look_up_with_a_strict_threshold.py` | Look up with a strict threshold | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_watch_history_get_billed_again.py` prints:

```text
turn 1: sent 3000 tokens
turn 2: sent 3050 tokens
turn 3: sent 3090 tokens
turn 4: sent 3150 tokens
total billed: 12290 tokens
```

## Try it without a key

- [OpenAI Tokenizer](https://platform.openai.com/tokenizer): Paste text and see how it splits into tokens. Free. It may ask you to sign in; no payment is needed.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. The estimate assumed 300 output tokens, but a reasoning model adds 1,200 hidden tokens per call. Monthly bill?**

- A. About 9,600 dollars
- B. Lower, reasoning tokens are free
- C. Still about 3,840 dollars

<details><summary>Answer</summary>

**A. About 9,600 dollars**. Hidden reasoning tokens are billed as output.

</details>

**2. Prompt caching is on. What do you do at turn 40 of a long chat?**

- A. Switch prompt caching off
- B. Compact by summarising older turns
- C. Nothing, cached tokens are free

<details><summary>Answer</summary>

**B. Compact by summarising older turns**. Caching is cheaper, not smaller. Still compact.

</details>

**3. Your prompt starts with today's date and the user's name. Why does nothing cache?**

- A. The prefix changes on every call
- B. Caching matches by similar meaning
- C. The model has no memory

<details><summary>Answer</summary>

**A. The prefix changes on every call**. Anything that varies goes at the end.

</details>

**4. "Cancel my policy" gets the cached answer for "keep my policy". What failed?**

- A. The model gave a wrong answer
- B. The threshold was too strict
- C. Similar meaning is not the same request

<details><summary>Answer</summary>

**C. Similar meaning is not the same request**. A cache hit skips the model. Nothing checks it.

</details>

## Say it in the interview

**Say it in the interview**

- I estimate bottom up, from traffic.
- Reasoning tokens can double or triple it.
- Write assumptions down. Input is usually wrong.

**Say it in the interview**

- Stateless API, so history is resent.
- Strip, summarise, retrieve less, set a ceiling.
- Caching does not shrink the window.

**Say it in the interview**

- Identical prefix, static parts first.
- Measure the hit rate from usage.
- Prompt caching is not semantic caching.

**Say it in the interview**

- A hit skips the model. Nothing catches it.
- Generic only, scoped per tenant, strict threshold.
- Write the cross-tenant leak test first.

## Homework

- [ ] Estimate one feature's monthly cost
- [ ] Add reasoning tokens to your estimate
- [ ] Rerun the lab with your own numbers
- [ ] Reorder a prompt: static first
