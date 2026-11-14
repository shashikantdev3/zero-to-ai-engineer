# Production and LLMOps · Part 9 of 38: Running, Scaling and Testing FastAPI Services

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. async def versus def
2. Uvicorn, Gunicorn and workers
3. WebSockets
4. Testing with TestClient and mocking the LLM
5. Flask versus FastAPI

## Key takeaways

- Never block inside async def.
- Each worker has its own memory.
- Two-way: WebSockets. One-way: SSE.
- Fake via Depends; test the failures.
- FastAPI for waiting; Flask for Flask teams.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_bad_and_the_legacy_endpoint.py` | The bad and the legacy endpoint | after `pip install fastapi requests` |
| `code/02_the_good_endpoint.py` | The good endpoint | after `pip install fastapi httpx` |
| `code/03_lab_count_the_token_buckets.py` | Count the token buckets | yes |
| `code/04_a_stand_in_model_stream.py` | A stand-in model stream | after `pip install fastapi` |
| `code/05_the_websocket_endpoint.py` | The WebSocket endpoint | after `pip install fastapi` |
| `code/06_app_setup_and_a_fake_model.py` | App setup and a fake model | after `pip install fastapi` |
| `code/07_the_endpoint_under_test.py` | The endpoint under test | after `pip install fastapi` |
| `code/08_override_and_test_the_happy_path.py` | Override and test the happy path | after `pip install fastapi` |
| `code/09_test_the_malformed_reply.py` | Test the malformed reply | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_count_the_token_buckets.py` prints:

```text
buckets: 12
limit per bucket: 10
real cluster limit: 120
intended limit: 10
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does async def make your code run faster?**

- A. Only for CPU-heavy work
- B. No, it makes waiting cheap
- C. Yes, every line runs faster

<details><summary>Answer</summary>

**B. No, it makes waiting cheap**. Async makes waiting cheap, not computing faster.

</details>

**2. You have 4 workers and 3 pods. How many token buckets?**

- A. One, shared by everything
- B. Four, one per worker
- C. Twelve, one per process

<details><summary>Answer</summary>

**C. Twelve, one per process**. In-memory state lives in one process.

</details>

**3. Your app only streams tokens from server to browser. What fits best?**

- A. Either, proxies treat them the same
- B. Server-sent events
- C. A WebSocket connection

<details><summary>Answer</summary>

**B. Server-sent events**. One-way streaming: use server-sent events.

</details>

**4. Your override is set, but the endpoint calls the client directly. What happens?**

- A. The override silently does nothing
- B. FastAPI raises a clear error
- C. The fake is used anyway

<details><summary>Answer</summary>

**A. The override silently does nothing**. Overrides only work through Depends.

</details>

**5. True or false: Flask cannot do async.**

- A. False, but each request holds a worker
- B. True, Flask has no async at all
- C. False, it matches FastAPI concurrency

<details><summary>Answer</summary>

**A. False, but each request holds a worker**. Flask async views still hold a worker.

</details>

## Say it in the interview

**Say it in the interview**

- async def shares the loop: never block.
- Blocking library: plain def or to_thread.
- CPU-heavy work goes to a process pool.

**Say it in the interview**

- One process, one loop, one core.
- VM: workers. Containers: replicas.
- Per-worker state does not add up.

**Say it in the interview**

- Token streaming: server-sent events.
- WebSockets when the client talks back.
- Costs: auth, heartbeats, reconnects, sticky scaling.

**Say it in the interview**

- Unit tests mock the model, deterministically.
- Fakes prove the failure paths.
- Evals on a golden set gate releases.

**Say it in the interview**

- LLM work is waiting; async is cheap.
- Validation and OpenAPI come free.
- Team consistency can beat the framework.

## Homework

- [ ] Find and fix one blocking call.
- [ ] Rerun the lab with your numbers.
- [ ] Write a malformed JSON test.
- [ ] Pick WebSockets or server-sent events.
