# Production and LLMOps · Part 6 of 38: Circuit Breakers, Bulkheads and Slow Tails

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Circuit breaker
2. Bulkhead, backpressure and load shedding
3. The p99 debugging order
4. Diagnosing a blocked event loop

## Key takeaways

- Breaker: count, open, fail fast, probe, close
- Isolate pools, bound queues, shed low priority
- What changed, p50, one trace, cheap causes
- Slow, idle, no errors: blocked event loop

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_simple_breaker_part_one.py` | A simple breaker, part one | yes |
| `code/02_a_simple_breaker_part_two.py` | A simple breaker, part two | yes |
| `code/03_lab_trip_a_breaker_by_hand.py` | Trip a breaker by hand | yes |
| `code/04_bulkhead_a_pool_per_dependency.py` | Bulkhead: a pool per dependency | yes |
| `code/05_backpressure_a_bounded_queue.py` | Backpressure: a bounded queue | after `pip install fastapi` |
| `code/06_did_only_the_tail_move.py` | Did only the tail move? | yes |
| `code/07_turn_on_asyncio_debug_mode.py` | Turn on asyncio debug mode | after `pip install fastapi` |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_trip_a_breaker_by_hand.py` prints:

```text
t=0 allowed: True
t=2 allowed: False
t=40 probe allowed: True
closed again: True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. The model API is fully down. Why not just retry harder?**

- A. A breaker is just a retry loop
- B. Enough retries always get through
- C. Retries add load and tie up workers

<details><summary>Answer</summary>

**C. Retries add load and tie up workers**. Retry for blips; break for outages

</details>

**2. Requests time out under load. Should you just add a bigger queue?**

- A. No, items deep in it wait too long
- B. Yes, unbounded queues prevent timeouts
- C. Yes, a bigger queue never drops work

<details><summary>Answer</summary>

**A. No, items deep in it wait too long**. Unbounded queues turn overload into timeouts

</details>

**3. You added instances, and now errors say 'too many connections'. What happened?**

- A. Extra pools exhausted the database
- B. Each request got faster instead
- C. All instances share one pool

<details><summary>Answer</summary>

**A. Extra pools exhausted the database**. Every instance brings its own connection pool

</details>

**4. A handler got faster when changed from async def to def. Why?**

- A. Async is simply slower than sync
- B. The threadpool gave it concurrency
- C. Plain def compiles to faster code

<details><summary>Answer</summary>

**B. The threadpool gave it concurrency**. The async version blocked; the threadpool hid it

</details>

## Say it in the interview

**Circuit breaker in the interview**

- Retries make a real outage worse
- Count, open, fail fast, probe, close
- Alert when the breaker opens

**Bulkheads in the interview**

- Separate compartments keep one hang contained
- Bounded queues, then 429 or 503
- Shed batch and free tier first

**The p99 order in the interview**

- Step means a switch; ramp means growth
- Both moved: saturation. Tail only: traces
- Free fixes first; never scale out first

**Blocked loop in the interview**

- Slow, idle, no errors: a blocked loop
- Confirm with debug mode or a profiler
- Faster as plain def? Something blocks

## Homework

- [ ] Rerun the lab breaker with threshold two
- [ ] Draw closed, open, half-open from memory
- [ ] Write the four p99 causes in order
- [ ] Write why scaling out can make it worse
