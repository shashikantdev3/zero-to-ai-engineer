# Python · Part 14 of 25: Async Pitfalls and Process Start Methods

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Blocking inside async def: to_thread and run_in_executor
2. Cancellation and timeouts
3. Coroutine, task and future
4. Forgotten await, and asyncio.run inside a running loop
5. Multiprocessing start methods: fork, spawn and forkserver

## Key takeaways

- Blocking calls go to to_thread or executors
- Timeout means unknown outcome; re-raise CancelledError
- Coroutine paused, task scheduled, task is future
- Missing await only warns; never nest asyncio.run
- Set the start method explicitly

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_moving_a_legacy_call_to_threads.py` | Moving a legacy call to threads | yes |
| `code/02_a_timeout_around_a_slow_call.py` | A timeout around a slow call | yes |
| `code/03_awaiting_in_a_loop_sequential.py` | Awaiting in a loop: sequential | yes |
| `code/04_taskgroup_three_calls_overlap.py` | TaskGroup: three calls overlap | yes |
| `code/05_lab_time_it_yourself.py` | Time it yourself | yes |
| `code/06_the_missing_await.py` | The missing await | yes |
| `code/07_choosing_the_start_method.py` | Choosing the start method | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_time_it_yourself.py` prints:

```text
is future: True
in order: 0.3
together: 0.1
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. If you put a blocking call inside an async function, does the async keyword make it non-blocking?**

- A. Only when debug mode is turned on
- B. No, it still freezes the event loop
- C. Yes, async makes any call non-blocking

<details><summary>Answer</summary>

**B. No, it still freezes the event loop**. async def does not make blocking code non-blocking

</details>

**2. A refund call to a payment service times out. What should you do next?**

- A. Check state, or retry with an idempotency key
- B. Retry it, because the call failed
- C. Nothing, a timeout means nothing happened

<details><summary>Answer</summary>

**A. Check state, or retry with an idempotency key**. A timeout is an unknown outcome, not a failure

</details>

**3. Three one-second calls are awaited one by one in a for loop. About how long does it take?**

- A. Almost no time at all
- B. About one second
- C. About three seconds

<details><summary>Answer</summary>

**C. About three seconds**. Awaiting in a loop is sequential, not parallel

</details>

**4. What happens when you forget the await on a coroutine call?**

- A. It raises an error straight away
- B. It only warns, and the work never runs
- C. It runs later in the background

<details><summary>Answer</summary>

**B. It only warns, and the work never runs**. A missing await warns; it does not raise

</details>

**5. On Python 3.14, what is the default multiprocessing start method on Linux?**

- A. forkserver
- B. spawn
- C. fork

<details><summary>Answer</summary>

**A. forkserver**. Defaults change by version; set the method explicitly

</details>

## Say it in the interview

**Say it in the interview**

- A sync call inside async def serialises requests
- Async client, to_thread, or a process pool
- Plain def endpoints use a threadpool

**Say it in the interview**

- Every network call gets a timeout
- Let CancelledError propagate after cleanup
- Idempotency keys before retrying side effects

**Say it in the interview**

- A coroutine is a paused recipe
- A task is a scheduled future
- To overlap, use tasks, TaskGroup or gather

**Say it in the interview**

- Created, thrown away, only a warning
- Debug mode plus a linter catches it
- Inside a running loop, await or create_task

**Say it in the interview**

- fork is fast but inherits locks and sockets
- spawn is clean; forkserver is fast and clean
- Pick it with get_context, survive upgrades

## Homework

- [ ] Compare to_thread with a direct blocking call
- [ ] Add a timeout, re-raise CancelledError
- [ ] Remove an await and read the warning
- [ ] Try the pool with spawn and forkserver
