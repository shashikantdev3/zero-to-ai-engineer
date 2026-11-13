# LLM Fundamentals · Part 4 of 18: Tokens, Cost, Latency and Context Rot

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Cost per token maths
2. Prefill, decode, time to first token
3. Streaming
4. Effective context length and context rot

## Key takeaways

- Every call counts. Judge cost per resolved task.
- Shorter outputs are the biggest latency win.
- Streaming changes perception, not speed or cost.
- Measure effective context. Fail closed on overflow.

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_worked_cost_estimate.py` | A worked cost estimate | yes |
| `code/02_lab_a_latency_budget_in_python.py` | A latency budget in Python | yes |
| `code/03_streaming_with_the_anthropic_sdk.py` | Streaming with the Anthropic SDK | yes |
| `code/04_sweep_length_and_position.py` | Sweep length and position | yes |
| `code/05_fail_closed_on_overflow.py` | Fail closed on overflow | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_a_latency_budget_in_python.py` prints:

```text
600 tokens: 12.5 s
150 tokens: 3.5 s
saved: 9.0 s
decode share: 0.96
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Where do hidden reasoning tokens show up on the bill?**

- A. Billed as output tokens
- B. Billed as input tokens
- C. Not billed, since you never see them

<details><summary>Answer</summary>

**A. Billed as output tokens**. Reasoning tokens bill as output, seen or not

</details>

**2. For a 600-token answer, what dominates latency?**

- A. The prompt length
- B. The output length
- C. The network connection

<details><summary>Answer</summary>

**B. The output length**. For long answers, output length dominates

</details>

**3. Does streaming make the model generate faster?**

- A. Yes, it cuts generation time
- B. Yes, and it cuts the cost
- C. No, it only feels faster

<details><summary>Answer</summary>

**C. No, it only feels faster**. Streaming improves perceived latency only

</details>

**4. A model passed needle-in-a-haystack at full length. Is long context solved?**

- A. No, multi-hop tasks still degrade
- B. Yes, if the needle was mid-prompt
- C. Yes, it found the needle every time

<details><summary>Answer</summary>

**A. No, multi-hop tasks still degrade**. Needle tests are the easy case

</details>

## Say it in the interview

**Say it in the interview**

- Requests times tokens times price, in and out
- Add history, tools, retries, loops, reasoning
- Report cost per resolved task

**Say it in the interview**

- Prefill is parallel. Decode is one at a time.
- Shorter prompts and caching cut first token time
- Shorter outputs are the biggest latency win

**Say it in the interview**

- Better perceived latency, same time and cost
- Buffer, validate, then release
- Cancel upstream on disconnect

**Say it in the interview**

- Advertised is not effective context
- Measure at real lengths. Question last.
- Count tokens. Fail closed on overflow.

## Homework

- [ ] Price one feature with the cost formula
- [ ] Add retries, loops and reasoning tokens
- [ ] Rerun the latency lab with your numbers
