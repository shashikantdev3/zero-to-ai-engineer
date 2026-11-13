# Python · Part 21 of 25: What to Retry, and How to Limit It

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. What to retry, and retry in one layer
2. Retry budgets, circuit breakers and deadline propagation

## Key takeaways

- Unknown outcomes need idempotency. Retry in one layer.
- Windowed budget, half-open breaker, one propagated deadline.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_sorting_the_errors.py` | Sorting the errors | yes |
| `code/02_classifying_an_exception.py` | Classifying an exception | yes |
| `code/03_the_final_decision.py` | The final decision | yes |
| `code/04_lab_classify_codes_count_attempts.py` | Classify codes, count attempts | yes |
| `code/05_retry_budget_the_window.py` | Retry budget: the window | yes |
| `code/06_retry_budget_may_we_retry.py` | Retry budget: may we retry? | yes |
| `code/07_circuit_breaker_its_state.py` | Circuit breaker: its state | yes |
| `code/08_breaker_may_we_call.py` | Breaker: may we call? | yes |
| `code/09_breaker_recording_results.py` | Breaker: recording results | yes |
| `code/10_deadline_use_what_is_left.py` | Deadline: use what is left | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_classify_codes_count_attempts.py` prints:

```text
429 write: True
502 refund: False
502 with key: True
404 any: False
attempts: 27
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A refund request gets a five oh two from the gateway. Is it safe to retry?**

- A. Only if it carries an idempotency key
- B. Yes, server errors are always safe
- C. No, a five oh two is permanent

<details><summary>Answer</summary>

**A. Only if it carries an idempotency key**. 502 on a write: unknown outcome. Retry only with a key.

</details>

**2. After the cooldown ends, what should a circuit breaker do first?**

- A. Stay open until someone restarts it
- B. Close and send all traffic again
- C. Let a single probe through

<details><summary>Answer</summary>

**C. Let a single probe through**. Half-open probes first. Close only on success.

</details>

**3. A retry budget uses lifetime counters. After a week of healthy traffic, an outage starts. How many retries does the first minute allow?**

- A. About ten percent of traffic
- B. Far too many, a retry burst
- C. None, the budget is empty

<details><summary>Answer</summary>

**B. Far too many, a retry burst**. Lifetime counters allow bursts. Use a sliding window.

</details>

## Say it in the interview

**Say it in the interview**

- Transient or permanent, then: did it already happen?
- Unknown outcomes need idempotency or a key.
- Retry in one layer, with one deadline.

**Say it in the interview**

- Retry budget: ten percent, over a sliding window.
- Breaker fails fast, then probes before closing.
- One deadline down the stack. Restart failed streams.

## Homework

- [ ] List the never-retry status codes from memory.
- [ ] Find max_retries. Pick one retry owner.
- [ ] Rerun the lab with a status of your own.
- [ ] Draw closed, open, half-open, and transitions.
