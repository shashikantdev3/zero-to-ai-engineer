# Fine-tuning and Model Choice · Part 7 of 10: KV Cache, GQA and Quantization

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. KV cache
2. GQA and MQA
3. Quantization (int8, int4, FP8)
4. KV cache quantization

## Key takeaways

- KV cache grows per token, layer and user
- Fewer KV heads, smaller cache
- Weight-only helps decode; always check evals
- FP8 cache: twice the tokens, separate switch

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_sizing_the_cache_in_python.py` | Sizing the cache in Python | yes |
| `code/02_reading_head_counts_from_config.py` | Reading head counts from config | yes |
| `code/03_lab_three_attention_designs_one_budget.py` | Three attention designs, one budget | yes |
| `code/04_serve_it_then_gate_it.py` | Serve it, then gate it | yes |
| `code/05_half_the_bytes_twice_the_tokens.py` | Half the bytes, twice the tokens | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_three_attention_designs_one_budget.py` prints:

```text
MHA: 512 KiB, 157.3 GB
GQA: 128 KiB, 39.3 GB
MQA: 16 KiB, 4.9 GB
MHA / GQA: 4 times
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Where does long context mainly cost you on a serving GPU?**

- A. Memory, through the KV cache
- B. Only extra compute
- C. Nothing, the cache is free

<details><summary>Answer</summary>

**A. Memory, through the KV cache**. Long context costs memory, mainly via the KV cache

</details>

**2. You size the KV cache with 32 query heads, not 8 KV heads. What happens?**

- A. The estimate is still correct
- B. Memory is overstated four times
- C. Memory is understated four times

<details><summary>Answer</summary>

**B. Memory is overstated four times**. Query heads overstate memory by the group factor

</details>

**3. Quantize everything to 4-bit: free memory, same answers?**

- A. No, show the eval delta first
- B. Yes, and every phase gets faster
- C. Yes, quality never changes

<details><summary>Answer</summary>

**A. No, show the eval delta first**. Show the eval delta; int4 mostly helps decode

</details>

**4. Which method keeps outlier features in 16-bit?**

- A. GPTQ
- B. AWQ
- C. LLM.int8

<details><summary>Answer</summary>

**C. LLM.int8**. Outliers in 16-bit is LLM.int8, not GPTQ or AWQ

</details>

**5. You served the weights in int4. Is the KV cache now quantized too?**

- A. Yes, it follows the weights
- B. No, it is a separate setting
- C. Yes, but only during prefill

<details><summary>Answer</summary>

**B. No, it is a separate setting**. KV cache precision is set separately from weights

</details>

## Say it in the interview

**KV cache in the interview**

- Cache past keys and values, compute one token
- About 128 KiB per token, per user
- The KV cache limits concurrency

**GQA and MQA in the interview**

- KV memory scales with KV heads
- GQA: groups share a KV head, 4x smaller
- Baked in at training, read from config

**Quantization in the interview**

- GPTQ fixes rounding, AWQ protects channels
- Weight-only helps decode; W8A8, FP8 help prefill
- Pick the lowest precision that passes

**KV cache quantization, interview**

- At peak, the KV cache runs out
- FP8 cache: roughly double the tokens
- Separate setting, rerun long-context evals

## Homework

- [ ] Size the KV cache from a real config
- [ ] Find both head counts, compute group size
- [ ] Weight memory at FP16, int8 and int4
- [ ] Rerun the lab with FP8 cache bytes
