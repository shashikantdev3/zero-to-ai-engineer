# LLM Fundamentals · Part 12 of 18: Longer Context, MoE Engineering, Image Tokens

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Context extension: position interpolation and YaRN
2. MoE load balancing, capacity and expert parallelism
3. Vision-language models and image token cost
4. Question drill: Inside the transformer

## Key takeaways

- Extend RoPE, then measure quality
- Balance, cap, all-to-all; compare on evals
- Image tokens grow with area
- Mask with large negatives, not zero

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_scaling_positions_down.py` | Scaling Positions Down | yes |
| `code/02_memory_versus_compute.py` | Memory Versus Compute | yes |
| `code/03_counting_patches.py` | Counting Patches | yes |
| `code/04_lab_watch_image_tokens_grow.py` | Watch Image Tokens Grow | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_watch_image_tokens_grow.py` prints:

```text
224 px: 196 tokens
448 px: 784 tokens
896 px: 3136 tokens
ratio: 4
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does RoPE extrapolate to any length on its own?**

- A. No, quality collapses past trained length
- B. Yes, rotations work at any length
- C. Only if the batch is large

<details><summary>Answer</summary>

**A. No, quality collapses past trained length**. RoPE extends after training, not by itself

</details>

**2. Is a 671B MoE as good as a 671B dense model?**

- A. Exactly as good as 671B dense
- B. Between active-size and total-size dense
- C. Exactly as good as 37B dense

<details><summary>Answer</summary>

**B. Between active-size and total-size dense**. No conversion rule; compare on evals

</details>

**3. Users upload phone photos and the bill jumps. Why?**

- A. Each image is one token
- B. Cost grows linearly with resolution
- C. Bigger images mean many more tokens

<details><summary>Answer</summary>

**C. Bigger images mean many more tokens**. Tokens grow with area, not side length

</details>

**4. To mask a token, can you set its score to zero?**

- A. No, use a large negative value
- B. Yes, softmax cancels zeros out
- C. Yes, zero removes the token

<details><summary>Answer</summary>

**A. No, use a large negative value**. Mask with a large negative, not zero

</details>

## Say it in the interview

**Say It in the Interview**

- Extendable after training, not self-extrapolating
- Interpolation squeezes; YaRN scales frequencies unevenly
- Test quality at the new length

**Say It in the Interview**

- Collapse, overflow, and all-to-all traffic
- 671B total, about 37B active
- Compare on evals; memory follows the total

**Say It in the Interview**

- Encoder, projection, then just more tokens
- Downscale to the smallest size that passes
- Low-confidence fields go to human review

## Homework

- [ ] Find rope_scaling in a model config
- [ ] Recompute MoE memory and compute
- [ ] Count patches for your photo sizes
- [ ] Practise the three interview answers
