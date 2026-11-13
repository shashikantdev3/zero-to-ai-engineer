# LLM Fundamentals · Part 15 of 18: Stops, Repeat Runs, Effort and Correctness

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Stop sequences and max tokens
2. Determinism, seed and repeat runs
3. Reasoning models and reasoning effort
4. Variety, not correctness

## Key takeaways

- Check the stop reason before you parse
- Greedy is not deterministic: measure agreement
- Pick reasoning effort with evals
- Sampling sets variety; checks set correctness

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_check_the_stop_reason.py` | Check the Stop Reason | yes |
| `code/02_a_helper_that_asks_once.py` | A Helper That Asks Once | yes |
| `code/03_repeat_runs_measure_agreement.py` | Repeat Runs, Measure Agreement | yes |
| `code/04_lab_watch_a_rounding_error_flip_a_token.py` | Watch a Rounding Error Flip a Token | yes |
| `code/05_set_effort_read_the_usage.py` | Set Effort, Read the Usage | yes |
| `code/06_define_the_shape_exactly.py` | Define the Shape Exactly | yes |
| `code/07_correctness_lives_in_code.py` | Correctness Lives in Code | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_watch_a_rounding_error_flip_a_token.py` prints:

```text
order A: 0.6000000000000001
order B: 0.6
equal: False
greedy pick A: cat
greedy pick B: dog
```

## Try it without a key

- [Google AI Studio](https://aistudio.google.com): A real model with temperature, top-p, thinking level and output length controls. Needs a Google account, no credit card. Do not paste private data: free-tier prompts may be used to improve Google products.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your lenient parser repaired the JSON, and three line items are missing. Why?**

- A. The output hit the token limit
- B. The temperature was set too high
- C. The model chose to skip them

<details><summary>Answer</summary>

**A. The output hit the token limit**. Check the finish reason before you parse

</details>

**2. Temperature 0, same eval case. It passed Monday and failed Tuesday. Why?**

- A. Someone must have edited the prompt
- B. A near tie flipped from tiny numeric noise
- C. Temperature 0 was silently ignored

<details><summary>Answer</summary>

**B. A near tie flipped from tiny numeric noise**. Temperature 0 plus seed is not deterministic

</details>

**3. High effort doubled latency, and ticket routing accuracy did not change. What now?**

- A. Add a temperature to speed it up
- B. Raise effort further for quality
- C. Lower effort, and confirm with evals

<details><summary>Answer</summary>

**C. Lower effort, and confirm with evals**. Effort is not free quality

</details>

**4. Temperature 0 gave valid JSON, perfect schema, wrong amount. What fixes it?**

- A. A business rule check in code
- B. An even lower temperature
- C. Switching on JSON mode

<details><summary>Answer</summary>

**A. A business rule check in code**. Settings never verify the numbers

</details>

## Say it in the interview

**Cheapest Controls, Checked Every Time**

- The cheapest controls I have
- Truncated output is a failure, not data
- Leave room for hidden reasoning

**Greedy Is Not Deterministic**

- Greedy is not the same as deterministic
- Seeds are best effort, where they exist
- Consistent is not correct

**Effort Chosen by Evals**

- Hidden reasoning is still billed
- Effort pays off on multi-step problems
- Choose effort from evals, not habit

**Two Layers: Settings, Then Checks**

- Layer one: settings for variety
- Layer two: validation and evals
- Low temperature repeats mistakes consistently

## Homework

- [ ] Find another float sum that changes with order
- [ ] Force a max_tokens stop and detect it
- [ ] Write one business rule for invoices
- [ ] Write why temperature 0 is not a guarantee
