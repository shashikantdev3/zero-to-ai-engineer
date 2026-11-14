# Production and LLMOps · Part 5 of 38: Fallbacks, Queues, Routing and Rate Limits

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Fallback model
2. Queue long jobs (202 plus poll)
3. Route by difficulty
4. Rate limiting with a token bucket

## Key takeaways

- Fallback: same evals, same zone, traced
- Long jobs: 202, durable queue, outbox
- Route by difficulty, tuned on evals
- Bucket caps bursts; share across replicas

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_fallback_in_async_python.py` | A Fallback in Async Python | yes |
| `code/02_accept_the_job_return_202.py` | Accept the Job, Return 202 | after `pip install fastapi` |
| `code/03_the_status_endpoint.py` | The Status Endpoint | after `pip install fastapi` |
| `code/04_a_router_in_plain_python.py` | A Router in Plain Python | yes |
| `code/05_a_token_bucket_class.py` | A Token Bucket Class | yes |
| `code/06_lab_watch_a_bucket_cap_a_burst.py` | Watch a Bucket Cap a Burst | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_watch_a_bucket_cap_a_burst.py` prints:

```text
burst of 5 at t=0: 3
t=1, two tries: True False
after long idle: 3
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A European tenant's primary model is throttled. Which fallback is acceptable?**

- A. Same model in another European region
- B. Any healthy region in the world
- C. The fastest model, even if untested

<details><summary>Answer</summary>

**A. Same model in another European region**. Fallback: same evals, same data zone

</details>

**2. The process crashed after saving the job, before sending the message. What prevents this?**

- A. A transactional outbox or stuck-job sweeper
- B. A longer HTTP timeout
- C. FastAPI background tasks

<details><summary>Answer</summary>

**A. A transactional outbox or stuck-job sweeper**. Outbox fixes dual writes; background tasks die with the pod

</details>

**3. How do you know hard cases aren't going to the small model?**

- A. Send every request to the small model
- B. Tune on evals, track quality per route
- C. Ask the model to rate its difficulty

<details><summary>Answer</summary>

**B. Tune on evals, track quality per route**. Validate routing with evals, not self-guesses

</details>

**4. Ten pods each run a per-process limiter of 100 per minute. What is the real limit?**

- A. 100 per minute
- B. 10 per minute
- C. 1000 per minute

<details><summary>Answer</summary>

**C. 1000 per minute**. Per-process limiters multiply by replica count

</details>

## Say it in the interview

**Say It: Fallback Model**

- A fallback keeps the feature alive
- Same evals, same residency
- Trace which model served each response

**Say It: Queue Long Jobs**

- Return 202, then queue the work
- No timeouts, steady rate, durable retries
- Solve the dual write with an outbox

**Say It: Route by Difficulty**

- Find the slow step, try cheap levers
- Big model only where evals show it wins
- Watch quality and p95 per route

**Say It: Token Bucket**

- Bucket size caps bursts
- Inbound per tenant, outbound under quota
- Share the bucket across replicas

## Homework

- [ ] Run the fallback code, read the label
- [ ] Draw the 202 flow with an outbox
- [ ] Add a test case to the router
- [ ] Change capacity and rate, predict output
