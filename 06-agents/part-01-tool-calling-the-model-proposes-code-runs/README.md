# Agents and Tools · Part 1 of 26: Tool Calling: The Model Proposes, Code Runs

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Tool calling (model proposes)
2. Tool schema (JSON Schema)
3. The action description is a prompt
4. Tool choice modes

## Key takeaways

- Model proposes, code executes
- Schema guides; code still validates
- Descriptions are prompts; fix them first
- Set tool choice per step

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_describe_the_tool.py` | Describe the tool | yes |
| `code/02_ask_then_keep_the_turn.py` | Ask, then keep the turn | yes |
| `code/03_treat_arguments_as_untrusted.py` | Treat arguments as untrusted | yes |
| `code/04_package_the_results.py` | Package the results | yes |
| `code/05_send_the_results_back.py` | Send the results back | yes |
| `code/06_the_argument_schema.py` | The argument schema | yes |
| `code/07_the_tool_in_a_stable_order.py` | The tool, in a stable order | yes |
| `code/08_lab_check_the_shape_of_arguments.py` | Check the shape of arguments | yes |
| `code/09_a_bad_and_a_good_description.py` | A bad and a good description | yes |
| `code/10_a_tool_to_classify_incidents.py` | A tool to classify incidents | yes |
| `code/11_force_that_one_tool.py` | Force that one tool | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/08_lab_check_the_shape_of_arguments.py` prints:

```text
missing a required field
invented field rejected
service not in enum
shape ok
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. When the model makes a tool call, who actually calls your API?**

- A. The provider, using your key
- B. The model calls it directly
- C. Your code, after checking the call

<details><summary>Answer</summary>

**C. Your code, after checking the call**. The model proposes. Your code executes.

</details>

**2. The arguments match your schema. Are they safe to run?**

- A. No, it checks shape, not permission
- B. Yes, the schema guarantees valid arguments
- C. Only if extra fields are blocked

<details><summary>Answer</summary>

**A. No, it checks shape, not permission**. A schema checks shape, not truth or permission

</details>

**3. Your agent keeps calling the wrong tool. What do you change first?**

- A. The descriptions, then rerun evals
- B. Switch to a bigger model
- C. Add comments to the function code

<details><summary>Answer</summary>

**A. The descriptions, then rerun evals**. Fix descriptions and evals, not the model

</details>

**4. With ten tools and tool choice set to required, which tool is called?**

- A. The first tool in the list
- B. Some tool, picked by the model
- C. The right tool for the task

<details><summary>Answer</summary>

**B. Some tool, picked by the model**. required forces a call, not the right call

</details>

## Say it in the interview

**Say it in the interview**

- Filling in a form, not pressing a button
- The model proposes, my code executes
- Safety and audit live in my code

**Say it in the interview**

- The schema is the whole interface
- Enums, required fields, stable order
- It guides. It does not protect.

**Say it in the interview**

- The description is a prompt
- What, when, when not, side effects
- Version it and rerun evals

**Say it in the interview**

- Tool choice is set per step
- Force, auto, or none, by step
- Code decides the model's freedom

## Homework

- [ ] Run the lab and add a bad case
- [ ] Add an enum field to a tool
- [ ] Rewrite one vague tool description
- [ ] Make your tool list order stable
