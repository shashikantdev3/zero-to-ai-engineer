# Fine-tuning and Model Choice · Part 5 of 10: Choosing, Routing, Pinning and Pricing Models

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Model catalogue
2. OpenAI-compatible API
3. Model routing and cascades
4. Model versioning and pinning
5. Cost per token maths

## Key takeaways

- Approved catalogue on top of the cloud's
- Same shape; re-run evals after any swap
- Escalate on code checks; escalations pay twice
- Pin versions and watch retirement dates
- Count every input token, every turn

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_one_catalogue_entry.py` | One catalogue entry | yes |
| `code/02_the_same_request_for_two_backends.py` | The same request for two backends | yes |
| `code/03_stand_in_models_and_a_check.py` | Stand-in models and a check | yes |
| `code/04_the_cascade_itself.py` | The cascade itself | yes |
| `code/05_pinned_config_with_a_retirement_date.py` | Pinned config with a retirement date | yes |
| `code/06_cost_of_one_call.py` | Cost of one call | yes |
| `code/07_lab_watch_history_grow_the_bill.py` | Watch history grow the bill | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/07_lab_watch_history_grow_the_bill.py` prints:

```text
turn 1: 700 input tokens
turn 2: 1200 input tokens
turn 3: 1700 input tokens
3 turns cost $0.001080
```

## Try it without a key

- [OpenAI Tokenizer](https://platform.openai.com/tokenizer): Paste text and see how it splits into tokens. Free. It may ask you to sign in; no payment is needed.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A model is in your cloud's catalogue. Is it approved for HR data?**

- A. Yes, if it is the newest version
- B. Yes, the cloud lists it
- C. Only if our approved list allows it

<details><summary>Answer</summary>

**C. Only if our approved list allows it**. A cloud catalogue is not governance

</details>

**2. You swapped to an OpenAI-compatible backend and structured output broke. Why?**

- A. Same request shape, but features can differ
- B. The new backend needs a different path
- C. Compatible servers never return JSON

<details><summary>Answer</summary>

**A. Same request shape, but features can differ**. Compatible shape is not identical behaviour

</details>

**3. In a cascade, what should trigger escalation to the big model?**

- A. The small model says it is unsure
- B. A check in code fails
- C. Every long request, to be safe

<details><summary>Answer</summary>

**B. A check in code fails**. Escalate on code checks, not self-confidence

</details>

**4. Answers got worse overnight and nobody deployed anything. Why?**

- A. Users asked harder questions overnight
- B. The model version moved or retired
- C. The prompt file got corrupted

<details><summary>Answer</summary>

**B. The model version moved or retired**. Pin the version and track retirement dates

</details>

**5. Users pasted long emails into the chat and the bill doubled. Why?**

- A. Each email is resent every turn
- B. Replies got longer, not inputs
- C. Providers charge extra for emails

<details><summary>Answer</summary>

**A. Each email is resent every turn**. History is billed again on every turn

</details>

## Say it in the interview

**Say it in the interview**

- An approved catalogue sits on top
- Teams pick through the gateway
- Plan migrations before calls fail

**Say it in the interview**

- Change the base URL and model name
- Swappable behind a thin adapter
- A swap goes through the eval gate

**Say it in the interview**

- Route by difficulty
- Escalate on a check in code
- Prove it saves money, not adds hops

**Say it in the interview**

- Pin the model like any dependency
- Version in every trace and release
- Track retirement, migrate weeks ahead

**Say it in the interview**

- Bottom up: tokens times price, both sides
- History is billed every turn
- Biggest lever: cut input tokens

## Homework

- [ ] Write one catalogue entry with owner and retirement
- [ ] Add a check and log the route
- [ ] Find one model version's retirement date
- [ ] Run the lab for ten turns
