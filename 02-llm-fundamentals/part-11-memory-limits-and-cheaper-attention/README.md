# LLM Fundamentals · Part 11 of 18: Memory limits and cheaper attention

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Arithmetic intensity
2. Multi-head latent attention (MLA)
3. Sparse, sliding-window and hybrid attention

## Key takeaways

- Decode waits on memory; batching shares weights only
- MLA: quality per cached byte, not smallest
- Windows cap cache; sparse cuts compute only

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_one_flop_per_byte.py` | One flop per byte | yes |
| `code/02_lab_batching_raises_intensity.py` | Batching raises intensity | yes |
| `code/03_cache_size_per_token_compared.py` | Cache size per token, compared | yes |
| `code/04_a_sliding_window_mask_is_a_band.py` | A sliding-window mask is a band | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_batching_raises_intensity.py` prints:

```text
weights read: 16 GB
batch 1: 1 flop/byte
batch 8: 8 flop/byte
batch 64: 64 flop/byte
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. At batch size 1, why is decode slow?**

- A. The GPU lacks compute power
- B. It waits on memory reads
- C. The prompt is too long

<details><summary>Answer</summary>

**B. It waits on memory reads**. Decode waits on memory, not compute

</details>

**2. Which of these has the smallest KV cache?**

- A. MQA, with one KV head
- B. MLA, with its latent
- C. GQA with eight KV heads

<details><summary>Answer</summary>

**A. MQA, with one KV head**. MLA wins on quality per byte, not size

</details>

**3. What does selection-based sparse attention actually save?**

- A. Size of the KV cache
- B. Memory for the model weights
- C. Attention compute per query

<details><summary>Answer</summary>

**C. Attention compute per query**. Sparse selection saves compute, not cache

</details>

## Say it in the interview

**Say it: arithmetic intensity**

- Intensity is work per byte moved
- Decode: one flop per byte, waits on memory
- Shrink the cache, speed up decode

**Say it: multi-head latent attention**

- Cache a latent; never store full keys, values
- Not the smallest; strong quality per byte
- A live alternative, not the new default

**Say it: efficient attention**

- Efficient attention has not converged
- Sparse cuts compute; the full cache stays
- Test long, multi-hop recall before trusting

## Homework

- [ ] Run the batching lab with a new batch size
- [ ] Compute the cache size for 4 KV heads
- [ ] Print the sliding mask with window 3
- [ ] Practise the intensity answer in under a minute
