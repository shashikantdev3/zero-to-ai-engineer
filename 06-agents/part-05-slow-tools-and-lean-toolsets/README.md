# Agents and Tools · Part 5 of 26: Slow Tools and Lean Toolsets

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Long-running tools: return a handle, then poll
2. Progressive disclosure of tools
3. Question drill: Tool calling additions

## Key takeaways

- Slow tool: handle now, poll later
- Short stable index, details on demand
- Retry inside, cap loops, break circuits

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_starting_the_export.py` | Starting the export | yes |
| `code/02_the_status_tool.py` | The status tool | yes |
| `code/03_lab_test_the_idempotency_key.py` | Test the idempotency key | yes |
| `code/04_a_short_index_plus_describe_tool.py` | A short index plus describe_tool | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_test_the_idempotency_key.py` prints:

```text
first: job-1
retry: job-1
incident 2: job-2
next bucket: job-3
I2, bad key: job-1
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A tool takes 90 seconds and the gateway times out. Best fix?**

- A. Raise the timeout to five minutes
- B. Return a job ID, then poll status
- C. Ask the model to retry the call

<details><summary>Answer</summary>

**B. Return a job ID, then poll status**. Raising a timeout only moves the number

</details>

**2. "Past 15 to 20 tools, accuracy collapses, so we route." Right stance?**

- A. False, tool count never matters
- B. True, always route past fifteen tools
- C. A heuristic to measure on your evals

<details><summary>Answer</summary>

**C. A heuristic to measure on your evals**. Fifteen to twenty is a heuristic, not a law

</details>

**3. The downstream ticketing system is down. What should the agent do?**

- A. Open a circuit breaker and escalate
- B. Keep retrying with backoff
- C. Pass the error to the model

<details><summary>Answer</summary>

**A. Open a circuit breaker and escalate**. A dead dependency needs a breaker, not retries

</details>

## Say it in the interview

**Say it in the interview**

- A slow synchronous tool stalls everything
- Return a handle, poll later
- Key scoped to one intended export

**Say it in the interview**

- Two costs: worse selection, resent definitions
- Retrieval, applied to capabilities
- Stable index, measured on my evals

## Homework

- [ ] Rerun the lab with a changed key
- [ ] Add a per-tool poll cap
- [ ] Build a five tool index
- [ ] Rehearse both interview answers
