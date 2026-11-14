# Fine-tuning and Model Choice · Part 8 of 10: How Servers Make LLMs Fast and Cheap

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. PagedAttention and vLLM
2. Continuous batching
3. Prefix caching and prompt caching
4. FlashAttention
5. Speculative decoding

## Key takeaways

- PagedAttention: KV blocks plus a block table
- Continuous batching: schedule every decode step
- Prefix caching: static first, dynamic last
- FlashAttention: exact, tiled, less memory traffic
- Speculative decoding: draft fast, verify once

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_starting_vllm_with_sensible_flags.py` | Starting vLLM with sensible flags | yes |
| `code/02_lab_simulate_static_versus_continuous.py` | Simulate static versus continuous | yes |
| `code/03_prompt_caching_with_a_cache_marker.py` | Prompt caching with a cache marker | with your API key |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_simulate_static_versus_continuous.py` prints:

```text
static: [10, 1000, 1012, 1008]
continuous: [10, 1000, 22, 30]
request 3 saved: 990
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What does PagedAttention actually make better?**

- A. How efficiently KV memory is used
- B. The quality of the model's answers
- C. The speed of the attention maths

<details><summary>Answer</summary>

**A. How efficiently KV memory is used**. PagedAttention fixes memory, not the attention maths

</details>

**2. What happens if you keep raising max-num-seqs?**

- A. The model's answers get less accurate
- B. Per-user TPOT worsens and preemption appears
- C. Throughput keeps rising with no downside

<details><summary>Answer</summary>

**B. Per-user TPOT worsens and preemption appears**. Bigger batch: more throughput, slower per user

</details>

**3. You add a timestamp at the top of the system prompt. What happens?**

- A. Nothing, caches skip timestamps
- B. Every cache hit breaks
- C. Only the first request misses the cache

<details><summary>Answer</summary>

**B. Every cache hit breaks**. Changing values go last, never at the top

</details>

**4. Which statement about FlashAttention is true?**

- A. Exact result, compute still quadratic
- B. It makes attention compute linear
- C. It approximates attention to save time

<details><summary>Answer</summary>

**A. Exact result, compute still quadratic**. Memory linear, compute quadratic, result exact

</details>

**5. With correct verification, what does speculative decoding change?**

- A. Output quality drops slightly
- B. Outputs become bit-for-bit identical
- C. Only latency; same output distribution

<details><summary>Answer</summary>

**C. Only latency; same output distribution**. Same distribution, lower latency, not identical bits

</details>

## Say it in the interview

**PagedAttention in the interview**

- Virtual memory paging, applied to the KV cache
- Less waste, bigger batches, shared prefixes
- vLLM adds continuous batching and an OpenAI-compatible server

**Continuous batching in the interview**

- Static batching holds short requests hostage
- Schedule per step; the GPU stays full
- Orca introduced it; vLLM does it by default

**Prefix caching in the interview**

- Reuse the shared prefix; first token comes sooner
- Exact match: static first, dynamic last
- Cached tokens still fill the context window

**FlashAttention in the interview**

- The bottleneck is memory traffic, not maths
- Tiles in on-chip memory; exact and faster
- FLOPs stay quadratic; biggest win in prefill

**Speculative decoding in the interview**

- Cheap draft guesses, big model verifies once
- Quality unchanged; only latency improves
- Best on predictable text like code

## Homework

- [ ] Rerun the lab with new request lengths
- [ ] Draw a block table for two requests
- [ ] Reorder a prompt: static first, dynamic last
- [ ] Explain FlashAttention's speed-up in two sentences
