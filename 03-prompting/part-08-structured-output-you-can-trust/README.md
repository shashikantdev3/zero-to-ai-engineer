# Prompting · Part 8 of 10: Structured Output You Can Trust

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Structured output: schema plus code
2. JSON mode vs schema-constrained output
3. Constrained decoding
4. Function calling as structured output

## Key takeaways

- API enforces shape. Code checks meaning.
- JSON mode is syntax. Schemas promise fields.
- Masked tokens: shape guaranteed, truth not.
- The model proposes. Your code authorises.

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_wire_schema_and_domain_model.py` | Wire schema and domain model | yes |
| `code/02_making_the_schema_strict.py` | Making the schema strict | yes |
| `code/03_calling_with_the_schema.py` | Calling with the schema | yes |
| `code/04_lab_build_a_tiny_token_mask.py` | Build a tiny token mask | yes |
| `code/05_defining_the_tool.py` | Defining the tool | yes |
| `code/06_handler_setup.py` | Handler setup | yes |
| `code/07_validate_check_then_run.py` | Validate, check, then run | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_build_a_tiny_token_mask.py` prints:

```text
1 wants Sure gets [
2 wants Sure gets true
3 wants Sure gets ]
output: [true]
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. You ask for JSON in the prompt and call json.loads. What breaks it?**

- A. A trailing comma or missing field
- B. Nothing, models always return valid JSON
- C. Only very long prompts

<details><summary>Answer</summary>

**A. A trailing comma or missing field**. Asking for JSON is a request, not a guarantee.

</details>

**2. JSON mode is on, yet a field went missing. Why?**

- A. Strict mode was too strict
- B. The schema had a typo
- C. JSON mode only aims for valid syntax

<details><summary>Answer</summary>

**C. JSON mode only aims for valid syntax**. JSON mode checks syntax. Schemas check fields.

</details>

**3. Valid JSON, perfect schema, wrong amount. What did constrained decoding guarantee?**

- A. Only the shape of the output
- B. Shape plus correct values
- C. That the values are correct

<details><summary>Answer</summary>

**A. Only the shape of the output**. Constrained decoding guarantees shape, never values.

</details>

**4. The model picks a tool. Where is authorisation checked?**

- A. The tool description itself
- B. Your code, on every call
- C. The model, before calling the tool

<details><summary>Answer</summary>

**B. Your code, on every call**. The model proposes. Your code authorises.

</details>

## Say it in the interview

**Two layers of protection**

- Layer one: the API enforces the schema.
- Layer two: Pydantic plus business checks.
- Retry shape. Send meaning failures to humans.

**Syntax versus schema**

- JSON mode: valid syntax, no field promise.
- Strict schema via the SDK helper.
- Strings on the wire, Decimal in code.

**Why the guarantee is real**

- Masking turns the schema into a guarantee.
- Shape, not truth.
- Measure format effects on your own evals.

**The model never runs anything**

- The model proposes. My code decides.
- Validate, re-check, authorise, then run.
- A tool description is a prompt.

## Homework

- [ ] Write a three-field invoice Pydantic model
- [ ] Find what strict mode would reject
- [ ] Edit the lab so false wins
- [ ] Write one read-only tool description
