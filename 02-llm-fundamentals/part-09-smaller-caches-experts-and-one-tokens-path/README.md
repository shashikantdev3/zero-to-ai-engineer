# LLM Fundamentals · Part 9 of 18: Smaller Caches, Experts, and One Token's Path

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Multi-query and grouped-query attention
2. Mixture of experts
3. Tracing one token through the model
4. Implementing batched multi-head attention

## Key takeaways

- Fewer KV heads, smaller cache, faster decode
- MoE cuts compute, not weight memory
- IDs, blocks, final norm, last row, sample
- Heads as an axis, swapaxes, mask first

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_top_k_router_in_numpy.py` | A top-k router in NumPy | yes |
| `code/02_shapes_to_say_in_the_interview.py` | Shapes to say in the interview | yes |
| `code/03_projections_and_head_reshapes.py` | Projections and head reshapes | yes |
| `code/04_scores_mask_and_softmax.py` | Scores, mask, and softmax | yes |
| `code/05_lab_watch_the_shapes_move.py` | Watch the shapes move | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_watch_the_shapes_move.py` prints:

```text
Q shape: (2, 8, 5, 16)
.T shape: (16, 5, 8, 2)
swapaxes shape: (2, 8, 16, 5)
scores shape: (2, 8, 5, 5)
scale: 4.0 not 11.313708498984761
```

## Try it without a key

- [LLM Visualization](https://bbycroft.net/llm): A 3D walkthrough of every step inside a tiny GPT. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What is the main benefit of grouped-query attention?**

- A. Smaller KV cache and less memory traffic
- B. Better quality than full multi-head
- C. Much less compute per token

<details><summary>Answer</summary>

**A. Smaller KV cache and less memory traffic**. GQA saves cache and bandwidth, not compute

</details>

**2. An MoE has 47B parameters and uses 13B per token. How much weight memory does serving need?**

- A. Somewhere between the two
- B. Only the thirteen billion active
- C. All forty-seven billion

<details><summary>Answer</summary>

**C. All forty-seven billion**. MoE saves compute per token, not weight memory

</details>

**3. At inference, which positions does the LM head run on?**

- A. Only the last position
- B. Every position in the sequence
- C. Every position, inside every block

<details><summary>Answer</summary>

**A. Only the last position**. Inference: LM head on the last position only

</details>

**4. K has shape (B, h, n, dk). What does K.T give?**

- A. Same shape, transposed per head
- B. All four axes reversed
- C. Only the last two axes swapped

<details><summary>Answer</summary>

**B. All four axes reversed**. Use swapaxes for keys; scale by head dimension

</details>

## Say it in the interview

**Say it in the interview**

- Multi-query: one shared key value head
- Grouped-query: one KV head per group
- KV head count drives the cache

**Say it in the interview**

- Big in knowledge, cheaper per token
- Small-model compute, big-model capacity
- Lower compute does not mean lower memory

**Say it in the interview**

- IDs, embeddings, then identical blocks
- Norm, attention, add. Norm, feed-forward, add.
- Final norm, last row, logits, sample

**Say it in the interview**

- Heads become an axis after batch
- Scale, mask, stable softmax, merge, project
- Watch for full transposes and late masks

## Homework

- [ ] Compare query heads with key value heads
- [ ] Write the MoE router from memory
- [ ] Write the token trace with all shapes
- [ ] Rerun the lab with a different h
