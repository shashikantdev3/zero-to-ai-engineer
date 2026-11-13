# Prompting · Part 10 of 10: Temperature, Escape Hatches, Agent Context, Schemas

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Temperature and structure
2. Escape hatches in the schema
3. Context for long-running agents
4. Schema design is prompt design

## Key takeaways

- Temperature is randomness, not structure
- Nullable fields and status stop invention
- Manage the window; fuller means less reliable
- Names, enums and formats are instructions

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_schema_with_a_way_out.py` | A schema with a way out | yes |
| `code/02_trim_a_tool_result.py` | Trim a tool result | yes |
| `code/03_lab_watch_a_result_shrink.py` | Watch a result shrink | yes |
| `code/04_descriptions_written_as_rules.py` | Descriptions written as rules | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_watch_a_result_shrink.py` prints:

```text
status ok
2000 chars before
48 chars after
True
```

## Try it without a key

- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): A small GPT-2 running in your browser. Type a prompt, move the temperature slider and watch the next-token probabilities change. Free, no account.
- [Google AI Studio](https://aistudio.google.com): A real model with temperature, top-p, thinking level and output length controls. Needs a Google account, no credit card. Do not paste private data: free-tier prompts may be used to improve Google products.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your extractor runs at temperature 0. Is its JSON always valid?**

- A. Only if the prompt says JSON
- B. No, likely tokens can still break it
- C. Yes, zero removes all randomness

<details><summary>Answer</summary>

**B. No, likely tokens can still break it**. Temperature zero is not a format guarantee

</details>

**2. Every field is required and the PO number is missing. What does the model write?**

- A. A made-up PO number
- B. An empty JSON object
- C. A clean parse error

<details><summary>Answer</summary>

**A. A made-up PO number**. Required with no way out means invented data

</details>

**3. Your model has a huge context window. Does a 30-step agent still need context management?**

- A. Only when using sub-agents
- B. No, everything fits anyway
- C. Yes, fuller windows are used less reliably

<details><summary>Answer</summary>

**C. Yes, fuller windows are used less reliably**. Fitting in the window is not being used

</details>

**4. The amount is a plain string with no format rule. The model writes 1,250.00. What happens?**

- A. Decimal parsing rejects the comma
- B. It parses as one point two five
- C. Pydantic strips the comma silently

<details><summary>Answer</summary>

**A. Decimal parsing rejects the comma**. Specify or normalise the number format

</details>

## Say it in the interview

**Temperature in the interview**

- Temperature zero does not make JSON valid.
- Low temperature for extraction, where supported.
- Schema gives structure. Validation gives correctness.

**Escape hatches in the interview**

- No way out means invented values.
- A refusal is not a parse error.

**Agent context in the interview**

- Fetch just in time, not up front.
- Trim results, keep notes, isolate sub-agents.
- Check summaries with long-task evals.

**Schema design in the interview**

- The schema is part of the prompt.
- Enums for fixed values. Keep it flat.
- Spell out formats, then validate.

## Homework

- [ ] Add a status enum to one schema
- [ ] Make uncertain fields nullable, add evidence
- [ ] Rewrite three descriptions as rules
- [ ] Trim a tool result, keep its ID
