# LLM Fundamentals · Part 5 of 18: Reasoning RL, Sycophancy, and Request Latency

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. RL with verifiable rewards and GRPO
2. Sycophancy
3. Question drill: Text to tokens
4. The life of an LLM API request

## Key takeaways

- GRPO: checkable rewards, group average baseline
- Trained to please, so check in code
- Measure effective context; overflow can truncate
- Measure TTFT and per-token time separately

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_group_advantage_in_code.py` | The Group Advantage in Code | yes |
| `code/02_a_pushback_eval_the_helper.py` | A Pushback Eval: The Helper | yes |
| `code/03_a_pushback_eval_the_flip.py` | A Pushback Eval: The Flip | yes |
| `code/04_measuring_time_to_first_token.py` | Measuring Time to First Token | yes |
| `code/05_time_per_output_token.py` | Time per Output Token | yes |
| `code/06_lab_a_latency_budget_in_python.py` | A Latency Budget in Python | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_a_latency_budget_in_python.py` prints:

```text
prefill: 0.40s
TTFT: 0.85s
total: 6.85s
capped at 100: 2.85s
TTFT at peak: 1.25s
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Did DPO retire reinforcement learning for LLMs?**

- A. Yes, except for very small models
- B. Yes, DPO replaced it fully
- C. No, RL returned for reasoning

<details><summary>Answer</summary>

**C. No, RL returned for reasoning**. DPO for preferences, GRPO for reasoning

</details>

**2. Does asking a model to double-check itself make it reliable?**

- A. No, it can still cave
- B. Yes, if you ask it twice
- C. Yes, self-checks catch the errors

<details><summary>Answer</summary>

**A. No, it can still cave**. Check decisions in code, not with are you sure

</details>

**3. What happens if a request goes over the context window?**

- A. Always a clear error message
- B. An error, or silent truncation
- C. The model summarises the overflow

<details><summary>Answer</summary>

**B. An error, or silent truncation**. Silent truncation is worse than an error

</details>

**4. TTFT doubled at peak and nothing was deployed. Why?**

- A. Queueing or KV cache pressure
- B. The model is thinking harder
- C. The prompt suddenly got longer

<details><summary>Answer</summary>

**A. Queueing or KV cache pressure**. Peak slowdown: check queue metrics first

</details>

## Say it in the interview

**GRPO in the Interview**

- DPO replaced RL is only half right
- Group average is the baseline
- Strong where a program can check

**Sycophancy in the Interview**

- Trained to sound right, not be right
- Caves on pushback, accepts wrong premises
- Neutral prompts, pushback evals, code checks

**The Request Path in the Interview**

- Queue plus prefill is time to first token
- Plus output tokens times time per token
- Pick the lever for the slow part

## Homework

- [ ] Run the group advantage with new rewards
- [ ] Write one pushback eval case
- [ ] Rerun the lab: longer prompt, shorter answer
- [ ] Practise the request answer in one minute
