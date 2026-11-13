# Python · Part 22 of 25: Idempotency, Fan-outs and Rate Limiters

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Idempotency keys
2. Timeouts and partial failures in a fan-out
3. Rate limiter: fixed window versus token bucket

## Key takeaways

- Key from the operation, minted once
- Per-call timeouts, keep successes, retry safely
- Bounded bursts, shared bucket across pods

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_deterministic_key.py` | A deterministic key | yes |
| `code/02_one_attempt_with_the_key.py` | One attempt, with the key | yes |
| `code/03_same_key_on_every_retry.py` | Same key on every retry | yes |
| `code/04_fan_out_with_limits.py` | Fan out with limits | yes |
| `code/05_split_successes_from_failures.py` | Split successes from failures | yes |
| `code/06_the_token_buckets_state.py` | The token bucket's state | yes |
| `code/07_refill_and_the_capacity_check.py` | Refill and the capacity check | yes |
| `code/08_acquire_and_why_it_is_unfair.py` | Acquire, and why it is unfair | yes |
| `code/09_refunds_and_token_limits.py` | Refunds and token limits | yes |
| `code/10_lab_a_token_bucket_with_a_fake_clock.py` | A token bucket with a fake clock | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/10_lab_a_token_bucket_with_a_fake_clock.py` prints:

```text
t=0 served=True
t=0 served=True
t=0 served=True
t=0 served=False
t=1 served=True
t=1 served=False
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Where should the idempotency key for a retried side effect come from?**

- A. A fresh UUID inside the retried function
- B. A fresh UUID on each attempt
- C. The logical operation, saved before attempt one

<details><summary>Answer</summary>

**C. The logical operation, saved before attempt one**. Mint the key once, outside every retry

</details>

**2. You fan out a hundred calls and need a timeout, so where should it go?**

- A. Around each call
- B. Around the whole batch
- C. Nowhere, just retry later

<details><summary>Answer</summary>

**A. Around each call**. Timeouts per call, never one for the batch

</details>

**3. A limiter counts calls and resets every minute, so what is the worst burst at the boundary?**

- A. Half the limit
- B. About twice the limit
- C. Exactly the limit

<details><summary>Answer</summary>

**B. About twice the limit**. Fixed windows allow about double at the edge

</details>

**4. Ten pods each keep their own token bucket, so what is the real limit?**

- A. Ten times the intended limit
- B. One tenth of the limit
- C. The intended limit

<details><summary>Answer</summary>

**A. Ten times the intended limit**. Share the bucket; update it atomically

</details>

## Say it in the interview

**Idempotency in the interview**

- A timeout tells me nothing about what happened
- Key from the operation, saved before attempt one
- No key support? Check state before retrying

**Fan-out in the interview**

- Per-call timeout, bounded concurrency, split results
- Bare gather loses nine hundred good results
- A timed-out call may still have run

**Rate limiting in the interview**

- Token bucket: bounded bursts, O(1) per check
- Reserve prompt plus max tokens, refund later
- Many pods: one bucket in Redis

## Homework

- [ ] Write operation_key; confirm it is deterministic
- [ ] Fan out a flaky fake call; check split
- [ ] Make the lab bucket reject oversized costs
- [ ] Explain the ten-pod problem in two sentences
