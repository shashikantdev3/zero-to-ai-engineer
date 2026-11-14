# Fine-tuning and Model Choice · Part 9 of 10: Sizing and Protecting GPUs for LLM Serving

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Mixture of experts at inference
2. Tensor and pipeline parallelism
3. Peak concurrency
4. Admission queue and preemption

## Key takeaways

- MoE: memory is total, speed is active.
- Tensor inside a node, pipeline across nodes.
- Peak concurrency, p95 context, then load test.
- Cap admission, queue the rest, avoid thrash.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_lab_size_the_kv_cache_by_hand.py` | Size the KV Cache by Hand | yes |
| `code/02_a_tiny_bounded_gateway.py` | A Tiny Bounded Gateway | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/01_lab_size_the_kv_cache_by_hand.py` prints:

```text
concurrent seqs: 40
floor (mean): 15.7 GB
plan (p95): 31.5 GB
fits in room: True
next: load test at 40 seqs
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. For a mixture-of-experts model, which number sets the GPU memory you need?**

- A. Total parameters
- B. Active parameters
- C. Experts per token

<details><summary>Answer</summary>

**A. Total parameters**. Memory follows total parameters, speed follows active.

</details>

**2. You run tensor parallelism across slow network links. Why did adding GPUs make it slower?**

- A. Pipeline bubbles left GPUs idle
- B. The model got bigger
- C. GPUs exchange data at every layer

<details><summary>Answer</summary>

**C. GPUs exchange data at every layer**. Tensor parallelism needs fast links inside one node.

</details>

**3. Your app has 10,000 registered users. What do you size GPUs for?**

- A. All 10,000 registered users
- B. Peak requests in flight at once
- C. The average request rate

<details><summary>Answer</summary>

**B. Peak requests in flight at once**. Size for peak concurrency, then load test it.

</details>

**4. Users wait at peak. Should you raise --max-num-seqs to serve more?**

- A. No, it causes more preemption
- B. Yes, the engine queue absorbs it
- C. Yes, more sequences serve more users

<details><summary>Answer</summary>

**A. No, it causes more preemption**. More sequences than KV room means thrash.

</details>

## Say it in the interview

**Mixture of Experts, in Three Lines**

- Each token uses a few experts per layer.
- Memory follows total, speed follows active.
- Cheap per token, not cheap in memory.

**Splitting a Model, in Three Lines**

- Tensor parallel: slice matrices, stay in one node.
- Pipeline parallel: blocks of layers, idle gaps.
- First try one GPU: quantize or go smaller.

**Peak Concurrency, in Three Lines**

- Size from peak concurrency, not user count.
- Use p95 context, cap with max model length.
- Load test throughput, queue the bursts.

**Admission Control, in Three Lines**

- KV cache is the budget: cap what gets in.
- Gateway: bounded wait, timeouts, 429s, metrics.
- Waiting beats thrashing.

## Homework

- [ ] Find total and active parameters on an MoE card
- [ ] Apply Little's law to your own traffic guess
- [ ] Rerun the lab with a longer p95 context
- [ ] Resize the gateway queue, predict the output
