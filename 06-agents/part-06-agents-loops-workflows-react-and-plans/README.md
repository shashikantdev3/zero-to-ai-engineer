# Agents and Tools · Part 6 of 26: Agents: Loops, Workflows, ReAct and Plans

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Agent loop
2. Workflow versus agent
3. The determinism boundary
4. ReAct
5. Plan-and-execute and replanning

## Key takeaways

- Agent: model in a loop, guarded by code
- Known steps: workflow. Open path: agent.
- The model proposes, code and humans decide
- ReAct needs a step limit and repeat check
- Validate the plan, replan with a cap

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_setup_the_client_and_one_tool.py` | Setup: the client and one tool | yes |
| `code/02_the_gate_code_decides.py` | The gate: code decides | yes |
| `code/03_the_loop_itself.py` | The loop itself | yes |
| `code/04_lab_lab_step_limit_and_loop_guard.py` | Lab: step limit and loop guard | yes |
| `code/05_the_plan_as_a_typed_object.py` | The plan as a typed object | yes |
| `code/06_validate_before_anything_runs.py` | Validate before anything runs | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_lab_step_limit_and_loop_guard.py` prints:

```text
finished at step 3
loop guard at step 2
step limit after 4
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Is a plain loop with no framework a real agent?**

- A. No, you need a framework
- B. Yes, the loop is the agent
- C. Only with a vector database

<details><summary>Answer</summary>

**B. Yes, the loop is the agent**. Frameworks add checkpoints and streaming, not agency.

</details>

**2. Fault detection checks are known and must be repeatable. What do you build?**

- A. An agent, since agents are more powerful
- B. An agent with more tools
- C. A fixed workflow, or plain rules

<details><summary>Answer</summary>

**C. A fixed workflow, or plain rules**. Known steps: write them down, skip the agent.

</details>

**3. Can a second model be the final check on the first?**

- A. No, it is still probabilistic
- B. Yes, two models agreeing is safe
- C. Yes, if the checker is bigger

<details><summary>Answer</summary>

**A. No, it is still probabilistic**. A reviewer model helps. Code and humans decide.

</details>

**4. What should the record of a ReAct agent rely on?**

- A. Its actions and evidence
- B. Only the final answer
- C. The model's reasoning text

<details><summary>Answer</summary>

**A. Its actions and evidence**. Log actions and evidence, not just thoughts.

</details>

**5. The plan assumes a database fault. Step two finds the database is fine. Now what?**

- A. Keep following the original plan
- B. Replan the remaining steps, with a cap
- C. Replan again and again until it fits

<details><summary>Answer</summary>

**B. Replan the remaining steps, with a cap**. Contradiction triggers a replan. Cap the replans.

</details>

## Say it in the interview

**Say it in the interview**

- An agent is a pattern, not a library.
- Next step depends on what the last found.
- Production grade lives around the loop.

**Say it in the interview**

- No agent if you can write the steps.
- Detection: rules. Investigation: agent.
- Switch when checks stop being enumerable.

**Say it in the interview**

- The model plans and drafts, it does not adjudicate.
- Model plans, code validates, humans approve.
- Mostly right is not an audit control.

**Say it in the interview**

- Reason, act, read the result, repeat.
- Adaptive, but no overall plan.
- Short tasks: ReAct. Long tasks: plan first.

**Say it in the interview**

- Long tasks: plan and execute.
- Validate the typed plan before running.
- Every new plan is validated again.

## Homework

- [ ] Write the agent loop from memory
- [ ] Add a budget stop to the lab
- [ ] Mark workflow and agent parts of one system
- [ ] Add one rule to validate_plan
