# Production and LLMOps · Part 3 of 38: Rate Limits, Cost Tracking and Latency

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Quotas, rate limits and provisioned throughput
2. Cost attribution and FinOps
3. Time to first token and time per output token
4. Percentiles: p50, p95, p99

## Key takeaways

- Honour Retry-After, add jitter, cap concurrency
- Tag every call, log tokens and cost
- Shorter output beats prompt tweaks
- Budget at p95, never trust the mean

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_parsing_the_date_form.py` | Parsing the date form | yes |
| `code/02_reading_every_retry_after_form.py` | Reading every Retry-After form | yes |
| `code/03_honour_the_header_add_jitter.py` | Honour the header, add jitter | yes |
| `code/04_one_record_per_call.py` | One record per call | yes |
| `code/05_aggregate_cost_per_feature.py` | Aggregate cost per feature | yes |
| `code/06_set_up_the_timer.py` | Set up the timer | yes |
| `code/07_time_the_stream.py` | Time the stream | with your API key |
| `code/08_compute_time_per_token.py` | Compute time per token | with your API key |
| `code/09_lab_where_the_seconds_go.py` | Where the seconds go | yes |
| `code/10_mean_versus_percentiles.py` | Mean versus percentiles | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/09_lab_where_the_seconds_go.py` prints:

```text
Full answer: 8.6 s
Half answer: 4.6 s
Saved: 4.0 s
TTFT share: 7%
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Fifty workers get a 429 and all retry at once. What happens?**

- A. A retry storm keeps them throttled
- B. Each one succeeds on the second try
- C. The quota resets for all of them

<details><summary>Answer</summary>

**A. A retry storm keeps them throttled**. Blind retries cause storms. Honour Retry-After with jitter.

</details>

**2. The bill doubled this month. What tells you which feature caused it?**

- A. Total tokens used this month
- B. Per call logs tagged with feature
- C. The provider's monthly invoice

<details><summary>Answer</summary>

**B. Per call logs tagged with feature**. Invoices give totals. Tagged call logs give causes.

</details>

**3. You stream from a reasoning model. Why does the first word take eight seconds?**

- A. The prompt is badly worded
- B. Streaming is broken on the client
- C. It reasons before the first visible token

<details><summary>Answer</summary>

**C. It reasons before the first visible token**. Hidden reasoning delays the first visible token.

</details>

**4. Your request fans out to ten shards. How do you cut the tail?**

- A. Hedge idempotent reads after the p95 delay
- B. Hedge every call, including tool calls
- C. Report the mean instead of p95

<details><summary>Answer</summary>

**A. Hedge idempotent reads after the p95 delay**. Hedge safe reads. Never report only the mean.

</details>

## Say it in the interview

**Say it in the interview**

- Rate limits are a design input
- Honour Retry-After with jittered backoff
- Provisioned is predictable, but idle time costs

**Say it in the interview**

- Nobody knows who owns it or what it costs
- Every call carries tags, usage, and cost
- Dashboards, chargeback, and cost alerts

**Say it in the interview**

- Two numbers: TTFT and total time
- Shorter output is the biggest lever
- Measure both per route, at p95

**Say it in the interview**

- The average hides one user in twenty
- Budget at p95 or p99, per route
- Traces find the tail. Hedging cuts it.

## Homework

- [ ] Parse Retry-After as seconds and as a date
- [ ] Design a tagged per call cost record
- [ ] Rerun the lab with your own numbers
- [ ] Compute p50, p95, p99 on sample data
