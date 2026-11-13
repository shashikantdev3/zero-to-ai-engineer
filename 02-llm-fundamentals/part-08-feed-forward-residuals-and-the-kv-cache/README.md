# LLM Fundamentals · Part 8 of 18: Feed-Forward, Residuals and the KV Cache

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Feed-forward network
2. Residual connections and layer norm
3. KV cache
4. KV cache memory maths

## Key takeaways

- FFN: per-token expand and project; most parameters
- x + f(x) with pre-norm keeps depth trainable
- KV cache: reuse past keys and values
- At peak, the cache, not weights, fills the GPU

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_feed_forward_network_in_numpy.py` | A feed-forward network in NumPy | yes |
| `code/02_rmsnorm_and_a_pre_norm_block.py` | RMSNorm and a pre-norm block | yes |
| `code/03_kv_cache_maths_in_python.py` | KV cache maths in Python | yes |
| `code/04_lab_lab_move_the_dials.py` | Lab: move the dials | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_lab_move_the_dials.py` prints:

```text
per token: 131 KB
one user: 393 MB
100 users: 39.3 GB
no GQA: 157.3 GB
8-bit cache: 19.7 GB
```

## Try it without a key

- [LLM Visualization](https://bbycroft.net/llm): A 3D walkthrough of every step inside a tiny GPT. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. In a typical dense transformer, where are most of the parameters?**

- A. In the layer norms
- B. In the attention layers
- C. In the feed-forward blocks

<details><summary>Answer</summary>

**C. In the feed-forward blocks**. Most weights live in the feed-forward blocks

</details>

**2. Why does layer norm still work at batch size 1?**

- A. It is switched off at inference
- B. It normalises each token's own features
- C. It averages across the whole batch

<details><summary>Answer</summary>

**B. It normalises each token's own features**. Layer norm works per token, so batch size one is fine

</details>

**3. Does the KV cache store your conversation between API requests?**

- A. No, it lives for one sequence
- B. Yes, it keeps the whole chat
- C. Only the latest user message

<details><summary>Answer</summary>

**A. No, it lives for one sequence**. Cache lives per sequence; prompt caching needs an exact prefix

</details>

**4. For this model, what goes wrong if you plug 32 attention heads into the formula?**

- A. Cache size is overstated four times
- B. Nothing, heads are just heads
- C. Cache size is understated by half

<details><summary>Answer</summary>

**A. Cache size is overstated four times**. Use KV heads, not attention heads

</details>

## Say it in the interview

**Say it: feed-forward network**

- Attention gathers. Feed-forward decides what to do.
- Most parameters; partly a key-value memory
- MoE: many expert blocks, a few per token

**Say it: residuals and norm**

- Input plus correction: a clean gradient path
- Pre-norm trains more stably at depth
- RMSNorm is cheaper: it skips the mean

**Say it: the KV cache**

- Past keys and values never change, so cache them
- Fast steps, but memory grows with tokens and users
- Why long context is expensive to serve

**Say it: KV cache memory**

- About 131 KB per token, in 16-bit
- 100 users: 39 GB cache versus 16 GB weights
- First lever: cap context length and concurrency

## Homework

- [ ] Write the FFN in NumPy from memory
- [ ] Wrap it in a pre-norm residual block
- [ ] Rerun the KV maths for 8,000 tokens
- [ ] Explain why the cache outgrows the weights
