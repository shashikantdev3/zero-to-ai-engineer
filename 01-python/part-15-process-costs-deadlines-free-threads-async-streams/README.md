# Python · Part 15 of 25: Process Costs, Deadlines, Free Threads, Async Streams

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Multiprocessing overhead, pickling, and threads that slow CPU work down
2. Timeout placement: per call or for the whole batch
3. Question drill: concurrency
4. Free-threaded CPython and subinterpreters
5. Async generators and async context managers

## Key takeaways

- Pools pay for pickling; batch tiny tasks
- Per call inside tasks; batch uses asyncio.wait
- Direct awaits run one at a time
- Optional build: check, measure, keep locks
- Stream with async for; close with aclosing

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_send_paths_batch_with_chunksize.py` | Send Paths, Batch With Chunksize | no: FileNotFoundError, see the note in the file |
| `code/02_a_batch_deadline_part_one.py` | A Batch Deadline, Part One | yes |
| `code/03_a_batch_deadline_part_two.py` | A Batch Deadline, Part Two | yes |
| `code/04_lab_watch_a_deadline_split_a_batch.py` | Watch a Deadline Split a Batch | yes |
| `code/05_is_the_gil_on_right_now.py` | Is the GIL On Right Now? | yes |
| `code/06_the_client_in_async_with.py` | The Client in Async With | yes |
| `code/07_streaming_lines_one_by_one.py` | Streaming Lines One by One | yes |
| `code/08_stop_early_clean_up_now.py` | Stop Early, Clean Up Now | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_watch_a_deadline_split_a_batch.py` prints:

```text
done: [0.1, 0.2]
timed out: 1
cancelled: True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Each task in your process pool takes about one microsecond, so what dominates the total time?**

- A. Pickling and inter-process communication
- B. Starting too few processes
- C. The actual CPU work

<details><summary>Answer</summary>

**A. Pickling and inter-process communication**. Tiny tasks: overhead dominates, so batch them

</details>

**2. You wrap gather in one async I O timeout to keep partial results, so what do you get back when it fires?**

- A. A timeout error and no results
- B. Only the results that finished
- C. Every result, with late ones empty

<details><summary>Answer</summary>

**A. A timeout error and no results**. Timeout around gather keeps nothing; use asyncio.wait

</details>

**3. You await three one-second calls one after another in a loop, so how long does it take?**

- A. About one second
- B. About three seconds
- C. Almost no time at all

<details><summary>Answer</summary>

**B. About three seconds**. Plain awaits in a loop run one at a time

</details>

**4. What did Python 3.1 three actually do about the GIL?**

- A. Removed the GIL for everyone
- B. Made unlocked shared code safe
- C. Added a separate, optional free-threaded build

<details><summary>Answer</summary>

**C. Added a separate, optional free-threaded build**. Free threading is an opt-in build, not the default

</details>

**5. You put the plain context manager decorator on an async function and use it, so what happens?**

- A. It works, just a little slower
- B. It fails at runtime
- C. Python quietly makes it async

<details><summary>Answer</summary>

**B. It fails at runtime**. Async resources need async with

</details>

## Say it in the interview

**Multiprocessing Is Not Free**

- Tiny tasks make a pool slower than a loop
- Batch with chunksize, build clients in the initialiser
- CPU threads fight over the GIL

**Which Thirty Seconds?**

- Thirty seconds per request, or per batch?
- asyncio.wait, keep done, cancel and await pending
- Separate results so only failures get retried

**The GIL Is Still Default**

- Experimental in 3.13, supported in 3.14
- LLM calls are I/O-bound; asyncio stays default
- Until proven, CPU-bound work goes to processes

**Streaming Tokens Safely**

- Yield chunks; the caller uses async for
- The client is always closed
- aclosing stops socket leaks on early exit

## Homework

- [ ] Time a process pool against a loop
- [ ] Send a lambda to a pool; read the error
- [ ] Rerun the lab with a longer deadline
- [ ] Check your build flag and GIL status
