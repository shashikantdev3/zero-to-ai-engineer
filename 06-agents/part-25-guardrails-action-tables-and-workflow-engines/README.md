# Agents and Tools · Part 25 of 26: Guardrails, Action Tables and Workflow Engines

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Guardrail frameworks: what each one actually is
2. The action table: start from the actions
3. Machine coding: a minimal workflow engine

## Key takeaways

- Guardrails score text; code authorizes actions
- List actions, cost if wrong, and approval first
- Iterative loop, step cap, node-plus-state fingerprint

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_check_is_just_a_function.py` | A check is just a function | yes |
| `code/02_wrapping_the_model_call.py` | Wrapping the model call | yes |
| `code/03_errors_and_the_fingerprint.py` | Errors and the fingerprint | yes |
| `code/04_one_step_of_the_engine.py` | One step of the engine | yes |
| `code/05_the_loop_with_two_guards.py` | The loop with two guards | yes |
| `code/06_test_a_loop_that_ends.py` | Test: a loop that ends | yes |
| `code/07_test_a_cycle_with_no_progress.py` | Test: a cycle with no progress | yes |
| `code/08_tests_step_cap_and_unknown_node.py` | Tests: step cap and unknown node | yes |
| `code/09_lab_spot_the_repeating_fingerprint.py` | Spot the repeating fingerprint | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/09_lab_spot_the_repeating_fingerprint.py` prints:

```text
a {'x': 1} 613fe5aa new
a {'x': 2} 24f57260 new
b {'x': 2} 24f57260 new
a {'x': 1} 613fe5aa SEEN
unique steps: 3
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. An injected tool call is scored as safe by the classifier. What stops it?**

- A. A second safety classifier on top
- B. A stricter Llama Guard threshold
- C. Code-level authorization and approval gates

<details><summary>Answer</summary>

**C. Code-level authorization and approval gates**. Classifiers filter. Code and approvals authorize.

</details>

**2. You get an agent design brief. What do you open with?**

- A. The actions, their cost, and their approval
- B. The model choice
- C. The conversation flow

<details><summary>Answer</summary>

**A. The actions, their cost, and their approval**. Autonomy is a list of unapproved actions, not a dial

</details>

**3. Your engine has only a step cap. What can it not tell you?**

- A. How many steps ran
- B. Where and why it looped
- C. That the run stopped

<details><summary>Answer</summary>

**B. Where and why it looped**. A cap says it stopped, not why

</details>

## Say it in the interview

**Guardrails in the interview**

- Group them by what they actually are
- Useful layers, never the thing that authorizes
- Permissions in code, filters tuned per category

**The action table in the interview**

- The action list decides the architecture
- Measure tool-call accuracy first
- Hand the pen back. Edit the table.

**The engine in the interview**

- Node functions, edge functions, merged updates
- Iterative loop, step cap, node plus state fingerprint
- Test: ends, cycles, caps, unknown node

## Homework

- [ ] Build guarded with one input check
- [ ] Draw an action table with human gates
- [ ] Code the engine, run the four tests
- [ ] Add a per-node visit limit
