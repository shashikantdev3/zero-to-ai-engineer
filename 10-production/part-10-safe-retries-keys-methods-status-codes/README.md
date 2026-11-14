# Production and LLMOps · Part 10 of 38: Safe Retries: Keys, Methods, Status Codes

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Idempotency keys
2. HTTP method semantics: safe and idempotent
3. Status codes that get confused

## Key takeaways

- Same key, same result, one action.
- Safe implies idempotent. GET never mutates.
- 401 vs 403. 422 for bad input. Never 500.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_hashing_the_payload.py` | Hashing the payload | yes |
| `code/02_claiming_the_key.py` | Claiming the key | yes |
| `code/03_handling_a_repeated_key.py` | Handling a repeated key | after `pip install fastapi` |
| `code/04_doing_the_work_once.py` | Doing the work once | yes |
| `code/05_lab_build_a_tiny_key_store.py` | Build a tiny key store | yes |
| `code/06_a_retry_safe_create_setup.py` | A retry-safe create: setup | after `pip install fastapi pydantic` |
| `code/07_put_to_a_client_chosen_id.py` | PUT to a client-chosen ID | after `pip install fastapi pydantic` |
| `code/08_one_answer_missing_or_forbidden.py` | One answer: missing or forbidden | after `pip install fastapi` |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_build_a_tiny_key_store.py` prints:

```text
ticket 1
ticket 1
422
tickets made: 1
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A call times out after the ticket was created. What key should the retry send?**

- A. No key, retries are always safe
- B. A brand new key
- C. The same key as the first try

<details><summary>Answer</summary>

**C. The same key as the first try**. A new key per retry defeats idempotency.

</details>

**2. Is a PATCH that increments a counter by one idempotent?**

- A. No, each send adds one more
- B. Yes, PATCH is always idempotent
- C. Yes, as long as it uses HTTPS

<details><summary>Answer</summary>

**A. No, each send adds one more**. PATCH semantics depend on the body.

</details>

**3. A request body fails validation. Which status code should it get?**

- A. 403 Forbidden
- B. 422 Unprocessable Content
- C. 500 Internal Server Error

<details><summary>Answer</summary>

**B. 422 Unprocessable Content**. 4xx tells the client: do not retry, fix it.

</details>

## Say it in the interview

**Idempotency keys, in one answer**

- First request claims the key; retries get the result.
- Hash the payload. Keep the pending expiry short.
- Checkpointing is not exactly-once. The key is.

**Methods, in one answer**

- Safe changes nothing. Idempotent: twice equals once.
- PATCH: neither by spec, the body decides.
- Not idempotent? Add a key, or PUT to an ID.

**Status codes, in one answer**

- 401: unknown caller. 403: known, refused.
- 404 hides existence, at a usability cost.
- Never 500 for bad input.

## Homework

- [ ] Run the lab, then retry with a new key.
- [ ] List your POST routes and their retry story.
- [ ] Find any GET route that changes data.
- [ ] Confirm bad input returns 422, not 500.
