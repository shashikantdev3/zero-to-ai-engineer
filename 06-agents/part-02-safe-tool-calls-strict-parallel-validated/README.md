# Agents and Tools · Part 2 of 26: Safe Tool Calls: Strict, Parallel, Validated

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Strict mode and schema-constrained arguments
2. Parallel tool calls and call IDs
3. Errors as results
4. Argument validation in code

## Key takeaways

- Strict mode: shape, not truth
- Every call gets a result, matched by ID
- Return permanent errors, retry safe transient ones
- Validate, check ownership, guard other systems

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_strict_ready_tool_schema.py` | A strict-ready tool schema | yes |
| `code/02_three_calls_with_their_own_ids.py` | Three calls with their own IDs | yes |
| `code/03_run_together_answer_by_id.py` | Run together, answer by ID | yes |
| `code/04_a_not_found_error_the_model_can_use.py` | A not-found error the model can use | yes |
| `code/05_pydantic_checks_the_shape.py` | Pydantic checks the shape | yes |
| `code/06_validate_then_check_the_owner.py` | Validate, then check the owner | yes |
| `code/07_allowlist_the_host_for_urls.py` | Allowlist the host for URLs | yes |
| `code/08_keep_paths_inside_a_base_folder.py` | Keep paths inside a base folder | yes |
| `code/09_lab_three_attacks_three_refusals.py` | Three attacks, three refusals | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/09_lab_three_attacks_three_refusals.py` prints:

```text
inside base: False
url allowed: False
injection rows: 0
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Strict mode is on and the refund arguments are valid JSON. Is the amount correct?**

- A. Not necessarily, it guarantees shape only
- B. Only if temperature is zero
- C. Yes, strict mode guarantees it

<details><summary>Answer</summary>

**A. Not necessarily, it guarantees shape only**. Valid JSON, wrong amount: shape is not truth

</details>

**2. One of three parallel tool calls times out. What do you send back?**

- A. Only the two that succeeded
- B. A result for each call, by ID
- C. Results in call order, no IDs

<details><summary>Answer</summary>

**B. A result for each call, by ID**. Every call gets a result, matched by ID

</details>

**3. The refund call timed out. What should your code do next?**

- A. Check state, retry only if idempotent
- B. Assume it failed and refund again
- C. Retry until it works

<details><summary>Answer</summary>

**A. Check state, retry only if idempotent**. Timeout means unknown: check state before retrying

</details>

**4. Should user_id be an argument in the refund tool's schema?**

- A. Yes, the model knows the user
- B. Yes, if strict mode is on
- C. No, it comes from the verified token

<details><summary>Answer</summary>

**C. No, it comes from the verified token**. Identity is never a model argument

</details>

## Say it in the interview

**Strict mode in the interview**

- Removes malformed, missing and invented fields
- Shape guaranteed, meaning still checked in code
- Strict, then Pydantic, then business rules

**Parallel calls in the interview**

- Independent lookups, one turn, run together
- The ID matters, the order does not
- Parallel reads, serial writes

**Errors as results in the interview**

- Clear errors let the model self-correct
- Retry transient, return permanent
- Error text becomes context

**Validation in the interview**

- Model arguments are like a web form
- Identity from the token, always
- Parameterise, allowlist, confine, no shell

## Homework

- [ ] Write a strict-ready schema with a nullable field
- [ ] Run three fake calls with asyncio gather
- [ ] Validate refund arguments with Pydantic
- [ ] Rerun the lab with a safe path
