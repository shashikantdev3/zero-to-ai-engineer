# Production and LLMOps · Part 7 of 38: Shared Rate Limits and FastAPI Contracts

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Distributed token bucket in Redis (Lua)
2. Rate limit response headers
3. Question drill: Latency and resilience
4. Path, query, body and response models

## Key takeaways

- Shared bucket: one atomic Lua script
- 429 plus Retry-After; headers on every response
- Ask what changed; check p50
- Hints validate, models filter, token decides tenant

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_lua_script_part_one.py` | The Lua script, part one | yes |
| `code/02_the_lua_script_part_two.py` | The Lua script, part two | yes |
| `code/03_calling_the_script_from_python.py` | Calling the script from Python | after `pip install redis` |
| `code/04_lab_simulate_lazy_refill_offline.py` | Simulate lazy refill offline | yes |
| `code/05_setting_the_headers_in_fastapi.py` | Setting the headers in FastAPI | after `pip install fastapi` |
| `code/06_the_request_and_response_models.py` | The request and response models | after `pip install fastapi pydantic` |
| `code/07_the_route_that_uses_them.py` | The route that uses them | after `pip install fastapi pydantic` |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_simulate_lazy_refill_offline.py` prints:

```text
t=0 ok=True left=2
t=0 ok=False left=2
t=2 ok=True left=1
t=3 ok=False left=3
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Ten pods each run an in-memory limiter of 100 per minute. What is the real limit?**

- A. About ten times higher, and it shifts
- B. Exactly one hundred per minute
- C. One hundred shared evenly across pods

<details><summary>Answer</summary>

**A. About ten times higher, and it shifts**. Per-process limits multiply with every pod

</details>

**2. An office of 500 people shares one IP, and you limit by IP. What happens?**

- A. All five hundred share one quota
- B. The limiter skips shared addresses
- C. Each person still gets their own quota

<details><summary>Answer</summary>

**A. All five hundred share one quota**. IP is shared behind NAT; key on tenant

</details>

**3. Are RateLimit-Limit, Remaining and Reset an official HTTP standard?**

- A. Yes, the HTTP semantics RFC defines them
- B. No, de facto names and a draft
- C. Yes, the same RFC as status 429

<details><summary>Answer</summary>

**B. No, de facto names and a draft**. Only 429 and Retry-After are standardised

</details>

**4. A route reads tenant_id from the URL path and trusts it. What stops a user changing it?**

- A. The response model blocks other tenants
- B. Pydantic validation rejects the wrong tenant
- C. Nothing, unless checked against the token

<details><summary>Answer</summary>

**C. Nothing, unless checked against the token**. Tenant comes from the token, never the URL

</details>

## Say it in the interview

**Say it in the interview**

- One Lua script, so the limit cannot leak
- Lazy refill; keys declared for Cluster
- Redis clock; spend estimated tokens per call

**Say it in the interview**

- 429 with Retry-After; quota headers not standard
- Headers on every response, not only 429
- Key on tenant; limit endpoints by cost

**Say it in the interview**

- Type hints are the contract
- response_model filters what leaves
- Tenant from the token; OpenAPI from types

## Homework

- [ ] Rerun the lab with new numbers
- [ ] Explain KEYS in two sentences
- [ ] Return an extra field; watch it vanish
- [ ] Answer the drill from memory
