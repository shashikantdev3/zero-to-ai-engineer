# Prompting · Part 9 of 10: Guarding Structured Output: Validate, Retry, Verify

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Pydantic gate
2. Retry with error
3. Validate the full object
4. Shape, not truth

## Key takeaways

- One Pydantic gate before anything runs
- Retry shape errors with exact errors, capped
- Act only on the complete object
- Schema checks shape; code checks truth

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_invoice_shape_part_one.py` | The invoice shape, part one | yes |
| `code/02_the_invoice_shape_part_two.py` | The invoice shape, part two | no: NameError, see the note in the file |
| `code/03_retry_loop_part_one_setup.py` | Retry loop, part one: setup | yes |
| `code/04_retry_loop_part_two_the_loop.py` | Retry loop, part two: the loop | yes |
| `code/05_retry_loop_part_three_helpers.py` | Retry loop, part three: helpers | yes |
| `code/06_stream_for_display_keep_a_buffer.py` | Stream for display, keep a buffer | no: NameError, see the note in the file |
| `code/07_check_the_end_then_validate.py` | Check the end, then validate | no: NameError, see the note in the file |
| `code/08_truth_check_one_the_totals.py` | Truth check one: the totals | yes |
| `code/09_truth_check_two_numbers_and_ids.py` | Truth check two: numbers and IDs | yes |
| `code/10_truth_check_three_grounding.py` | Truth check three: grounding | yes |
| `code/11_lab_lab_value_boundary_totals.py` | Lab: value, boundary, totals | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/11_lab_lab_value_boundary_totals.py` prints:

```text
value match: True
string match: False
12 in INV-1234: False
12 in Ref 12 paid: True
totals ok: False
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. The API guarantees the schema. Do you still validate the response?**

- A. Yes, for business rules and provider changes
- B. Only for smaller, cheaper models
- C. No, the API already guarantees it

<details><summary>Answer</summary>

**A. Yes, for business rules and provider changes**. The model proposes, the gate decides

</details>

**2. Your checks say the totals don't match. Do you send that error back to the model?**

- A. Yes, it is just another error
- B. Yes, retry until it passes
- C. No, route it to human review

<details><summary>Answer</summary>

**C. No, route it to human review**. Retry shape errors. Send truth errors to people

</details>

**3. You write fields to the database as they stream, and the stream dies at 80%. What do you have?**

- A. Valid data for the saved fields
- B. A partial record you cannot trust
- C. Nothing, the database undoes it

<details><summary>Answer</summary>

**B. A partial record you cannot trust**. Never act on partial JSON

</details>

**4. Valid JSON, perfect schema, wrong amount. Now what?**

- A. Code checks catch it, a human reviews
- B. A stricter schema would catch it
- C. Ask the model to correct it

<details><summary>Answer</summary>

**A. Code checks catch it, a human reviews**. Strict schema does not mean correct data

</details>

## Say it in the interview

**Say it in the interview**

- A Pydantic gate between model and everything
- Fail validation, nothing downstream runs
- The model proposes, the gate decides

**Say it in the interview**

- Exact errors back, two or three tries
- Retry shape errors, never truth errors
- Track retry rate per prompt version

**Say it in the interview**

- Show the stream, act on the whole
- A cut-off is a failure
- One helper for provider signals

**Say it in the interview**

- A schema checks shape, not truth
- Totals, lookups, grounding, all in code
- The model drafts, code adjudicates

## Homework

- [ ] Write an Invoice model with enum and limits
- [ ] Read the errors from a bad JSON string
- [ ] Make the lab's totals pass
- [ ] Sort errors: retry or human review
