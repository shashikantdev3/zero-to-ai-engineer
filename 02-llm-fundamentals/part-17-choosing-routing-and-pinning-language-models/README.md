# LLM Fundamentals · Part 17 of 18: Choosing, Routing and Pinning Language Models

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. SLM versus LLM
2. Model selection and routing
3. Model versioning and pinning
4. Structured output and function calling (pointer)

## Key takeaways

- Smallest model that passes your eval.
- Rules, small, large fallback. Track quality per route.
- Pin dated versions. Log the model ID.
- Schema guarantees shape, not truth.

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_router_setup_two_models.py` | Router Setup: Two Models | yes |
| `code/02_the_route_function.py` | The Route Function | yes |
| `code/03_fallback_on_failed_validation.py` | Fallback on Failed Validation | yes |
| `code/04_pin_the_model_log_the_version.py` | Pin the Model, Log the Version | yes |
| `code/05_lab_shape_passes_code_still_blocks.py` | Shape Passes, Code Still Blocks | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_shape_passes_code_still_blocks.py` prints:

```text
valid JSON: True
tool proposed: refund
amount within order: False
blocked by code
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. How do you prove the cheapest model is good enough?**

- A. Same golden set, several runs, worst run passes
- B. Pick the biggest model to be safe
- C. Run each model once on a demo

<details><summary>Answer</summary>

**A. Same golden set, several runs, worst run passes**. Worst run must pass, then lowest cost per resolved task.

</details>

**2. Which model should serve your support tickets?**

- A. The top model on a public leaderboard
- B. Whatever model is newest
- C. The best on your own golden set

<details><summary>Answer</summary>

**C. The best on your own golden set**. Leaderboards shortlist. Your golden set decides.

</details>

**3. Answers got worse overnight and nobody changed code. What changed?**

- A. Users suddenly asked harder questions
- B. The model behind a floating alias
- C. The server's processor got slower

<details><summary>Answer</summary>

**B. The model behind a floating alias**. Latest is not stable. Pin and log the model ID.

</details>

**4. A model returns a refund tool call. Who checks the amount?**

- A. Your code, before running the tool
- B. Nobody, the schema guarantees it
- C. The model, when it calls the API

<details><summary>Answer</summary>

**A. Your code, before running the tool**. The model proposes. Your code checks and runs.

</details>

## Say it in the interview

**SLM Versus LLM, In Interview**

- Small models: cheap, fast, can run locally.
- Default: the smallest model that passes the eval.
- A reason to try small first, not proof.

**Selection and Routing, In Interview**

- Evidence, not leaderboards.
- No single model wins, so I route.
- Tune on evals. Track quality per route.

**Pinning, In Interview**

- The model is a locked dependency.
- Upgrades pass the eval gate and roll back.
- Log the model ID on every trace.

**Structured Output, In Interview**

- Next-token generation steered into a format.
- The model proposes. My code decides.
- A schema guarantees shape, not truth.

## Homework

- [ ] Name three narrow tasks a small model could handle.
- [ ] Sketch a router: rules, small, large fallback.
- [ ] Write down the exact model ID you call.
- [ ] Retype the lab. Change the refund amount.
