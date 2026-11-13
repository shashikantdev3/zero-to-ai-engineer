# Python · Part 13 of 25: The GIL, asyncio, and Safe Concurrency

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. The GIL
2. I/O-bound versus CPU-bound: threading, multiprocessing or asyncio
3. asyncio: event loop, coroutines, async and await
4. gather versus TaskGroup
5. Semaphore and bounded concurrency

## Key takeaways

- One thread runs bytecode; I/O releases the GIL
- Waiting: asyncio. Pure-Python CPU: processes.
- One thread, turns at await, keep references
- gather carries on; TaskGroup cancels the rest
- Semaphore caps in flight; bucket caps rate

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_process_pool_from_asyncio.py` | A process pool from asyncio | yes |
| `code/02_keep_a_reference_to_tasks.py` | Keep a reference to tasks | yes |
| `code/03_lab_watch_the_loop_take_turns.py` | Watch the loop take turns | yes |
| `code/04_gather_with_return_exceptions.py` | gather with return_exceptions | yes |
| `code/05_taskgroup_fails_as_one.py` | TaskGroup fails as one | yes |
| `code/06_a_thousand_calls_twenty_at_once.py` | A thousand calls, twenty at once | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_watch_the_loop_take_turns.py` prints:

```text
coroutine
A starts
B starts
B done
A done
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Someone says Python cannot do parallelism, so how does PyTorch use every core?**

- A. It runs many bytecode threads at once
- B. Its native code runs outside the GIL
- C. A newer Python removed the GIL

<details><summary>Answer</summary>

**B. Its native code runs outside the GIL**. Native code and processes escape the GIL

</details>

**2. You need to make a thousand API calls, so which approach fits best?**

- A. Multiprocessing for true parallelism
- B. One thread per call, no limit
- C. Async I O with a semaphore

<details><summary>Answer</summary>

**C. Async I O with a semaphore**. Waiting work needs asyncio, not processes

</details>

**3. What happens if one async handler calls time dot sleep for five seconds?**

- A. Other tasks move to new threads
- B. Every coroutine on that loop stalls
- C. Only that one handler waits

<details><summary>Answer</summary>

**B. Every coroutine on that loop stalls**. Async is cooperative, not parallel

</details>

**4. Ten calls run under gather without return exceptions, and one fails, so what happens to the other nine?**

- A. They keep running and keep billing
- B. They pause until you retry
- C. They are all cancelled at once

<details><summary>Answer</summary>

**A. They keep running and keep billing**. gather raises, but does not cancel

</details>

**5. Your semaphore allows sixty calls at once and each takes one second, so about how many requests per minute can you send?**

- A. About three thousand six hundred
- B. About one thousand
- C. At most sixty

<details><summary>Answer</summary>

**A. About three thousand six hundred**. Concurrency is not rate

</details>

## Say it in the interview

**Say it in the interview**

- One thread runs bytecode at a time
- Threads for I/O, processes for CPU
- LLM calls are network-bound anyway

**Say it in the interview**

- Network waiting: asyncio, not processes
- Semaphore, token bucket, backoff on 429
- CPU work: process pool. Blocking SDK: threads.

**Say it in the interview**

- Cooperative multitasking on one thread
- Await it, or keep the task referenced
- One blocking call freezes the loop

**Say it in the interview**

- gather re-raises, others keep running
- return_exceptions for independent batches
- TaskGroup when tasks form one answer

**Say it in the interview**

- Semaphore sized from limits and latency
- Concurrency, not rate: add a token bucket
- Create it inside the running loop

## Homework

- [ ] Run the lab, swap the delays
- [ ] Add time.sleep and watch everything stall
- [ ] Try gather with return_exceptions=False
- [ ] Compute rate: 20 slots, half-second calls
