# Production and LLMOps · Part 4 of 38: Streaming, Parallel Calls, Timeouts and Retries

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Streaming and server-sent events
2. Parallel calls
3. Timeouts
4. Backoff with jitter

## Key takeaways

- Streaming cuts felt latency, not cost.
- Parallel takes the slowest, not the sum.
- Timeouts everywhere. Timeout means unknown.
- Jittered backoff, one retry layer.

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_an_sse_generator_over_a_model_stream.py` | An SSE generator over a model stream | yes |
| `code/02_the_post_route_that_streams.py` | The POST route that streams | after `pip install fastapi pydantic` |
| `code/03_a_semaphore_around_each_call.py` | A semaphore around each call | yes |
| `code/04_gather_three_calls_at_once.py` | Gather three calls at once | yes |
| `code/05_client_timeouts_plus_a_deadline.py` | Client timeouts plus a deadline | yes |
| `code/06_which_errors_deserve_a_retry.py` | Which errors deserve a retry | yes |
| `code/07_the_retry_loop_with_full_jitter.py` | The retry loop with full jitter | yes |
| `code/08_lab_watch_jitter_and_stacked_retries.py` | Watch jitter and stacked retries | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/08_lab_watch_jitter_and_stacked_retries.py` prints:

```text
try 0: max 0.5, wait 0.16
try 1: max 1.0, wait 0.15
try 2: max 2.0, wait 1.30
try 3: max 3.0, wait 0.22
3 layers x 3 retries: 64 calls
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does streaming an answer reduce what the model call costs?**

- A. Yes, because the call finishes sooner
- B. No, the same tokens cost the same
- C. Yes, streamed tokens are billed less

<details><summary>Answer</summary>

**B. No, the same tokens cost the same**. Streaming cuts perceived latency, not cost.

</details>

**2. Three tasks run in a TaskGroup and one fails. What happens to the other two?**

- A. They keep running to the end
- B. They restart automatically
- C. They are cancelled

<details><summary>Answer</summary>

**C. They are cancelled**. TaskGroup cancels the rest. gather can keep going.

</details>

**3. A refund call timed out. Did the refund happen?**

- A. Unknown, check the state first
- B. No, a timeout means it failed
- C. Yes, timeouts only follow success

<details><summary>Answer</summary>

**A. Unknown, check the state first**. Timeout means unknown. Check state before retrying.

</details>

**4. The SDK already retries. Should your own code retry too?**

- A. No, retry in one layer only
- B. Yes, more retries are always safer
- C. Yes, but with no waits between

<details><summary>Answer</summary>

**A. No, retry in one layer only**. Retry in one layer only.

</details>

## Say it in the interview

**Streaming in the interview**

- Streaming changes felt time, not model speed.
- SSE over POST, read with fetch.
- No buffering. Close on disconnect. Check in chunks.

**Parallel calls in the interview**

- Sequential adds up. Parallel takes the maximum.
- gather or TaskGroup, capped by a semaphore.
- One failed branch degrades, not kills, the answer.

**Timeouts in the interview**

- Timeout per call, deadline per request.
- Read timeout is per read. Add a deadline.
- Unknown, not failed. Verify before retrying.

**Backoff in the interview**

- Retry transient errors only. Never a 400.
- Exponential backoff with full jitter.
- Honour Retry-After, cap attempts, one layer.

## Homework

- [ ] Stream a reply and print each piece
- [ ] Time three fake calls with gather
- [ ] Add an asyncio.timeout deadline
- [ ] Rerun the lab with a cap of 20
