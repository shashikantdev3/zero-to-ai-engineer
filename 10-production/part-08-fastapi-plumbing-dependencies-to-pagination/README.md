# Production and LLMOps · Part 8 of 38: FastAPI Plumbing: Dependencies to Pagination

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Dependency injection
2. Lifespan and shared clients
3. Middleware and correlation IDs
4. Error handlers and the error contract
5. Pagination and API versioning

## Key takeaways

- Depends supplies needs; bad tokens get 401
- Shared clients live in the lifespan
- One validated ID follows every request
- One error shape, with retryable
- Cursors for pages, new versions for breaks

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_setup_and_a_token_verifier.py` | Setup and a token verifier | after `pip install fastapi jwt` |
| `code/02_the_current_user_dependency.py` | The current user dependency | after `pip install fastapi` |
| `code/03_using_the_dependencies.py` | Using the dependencies | after `pip install fastapi` |
| `code/04_the_lifespan_function.py` | The lifespan function | after `pip install fastapi httpx` |
| `code/05_wire_it_up_and_share_it.py` | Wire it up and share it | after `pip install fastapi httpx` |
| `code/06_the_id_format_rule.py` | The ID format rule | after `pip install fastapi` |
| `code/07_the_correlation_middleware.py` | The correlation middleware | after `pip install fastapi` |
| `code/08_two_custom_exceptions.py` | Two custom exceptions | after `pip install fastapi` |
| `code/09_one_builder_for_every_error.py` | One builder for every error | yes |
| `code/10_handler_for_a_failing_provider.py` | Handler for a failing provider | after `pip install fastapi` |
| `code/11_handler_for_bad_model_output.py` | Handler for bad model output | after `pip install fastapi` |
| `code/12_router_and_data_stand_ins.py` | Router and data stand-ins | after `pip install fastapi` |
| `code/13_the_paginated_endpoint.py` | The paginated endpoint | after `pip install fastapi` |
| `code/14_lab_see_offset_pages_break.py` | See offset pages break | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/14_lab_see_offset_pages_break.py` prints:

```text
page 1: [100, 99, 98]
offset page 2: [98, 97, 96]
repeated: {98}
cursor page 2: [97, 96, 95]
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. You send an expired token to /v1/me. What status should you get?**

- A. 200 with an error message
- B. 500 Internal Server Error
- C. 401 with a WWW-Authenticate header

<details><summary>Answer</summary>

**C. 401 with a WWW-Authenticate header**. Expired or forged token means 401, never 500

</details>

**2. Every handler runs async with httpx.AsyncClient(). What breaks at peak?**

- A. Requests speed up with fresh clients
- B. Latency rises and socket errors appear
- C. Nothing, creating clients is free

<details><summary>Answer</summary>

**B. Latency rises and socket errors appear**. Shared clients live in the lifespan

</details>

**3. A worker processes a queued job later. How does it get the correlation ID?**

- A. Put the ID inside the queue message
- B. The worker reads the original HTTP headers
- C. The HTTP middleware runs in the worker

<details><summary>Answer</summary>

**A. Put the ID inside the queue message**. The ID travels inside the message

</details>

**4. Your model provider is briefly down. What should your API return?**

- A. 500 Internal Server Error
- B. 503, retryable, with a Retry-After header
- C. 200 with an error field

<details><summary>Answer</summary>

**B. 503, retryable, with a Retry-After header**. Status plus retryable tells clients when to retry

</details>

**5. With offset pagination, page 10,000 takes 8 seconds. Why?**

- A. The database walks past every skipped row
- B. JSON encoding slows down on deep pages
- C. The limit of 50 is too small

<details><summary>Answer</summary>

**A. The database walks past every skipped row**. Deep offsets are slow; cursors seek directly

</details>

## Say it in the interview

**Dependencies in the interview**

- Auth as a dependency: no endpoint can forget it
- Override the LLM client; tests are fast and free

**Lifespan in the interview**

- Create shared clients once, in the lifespan
- Pooling: no handshake per call
- After yield, close cleanly on shutdown

**Correlation IDs in the interview**

- One ID at the edge, everywhere after
- Rebuild retrieval, model and cost from one ID
- Strict format, or a fresh ID

**Error contract in the interview**

- One shape for every error, never parse strings
- 503, 502, 429, 422: each failure has a home
- Retryable stops pointless hammering

**Pagination and versions in interviews**

- Cursor pagination: correct pages, fast deep pages
- URL prefix; breaking changes get a new version
- The response shape is a contract

## Homework

- [ ] Write an auth dependency returning 401
- [ ] Move a shared client into a lifespan
- [ ] Add correlation ID middleware
- [ ] Rerun the lab with two new rows
