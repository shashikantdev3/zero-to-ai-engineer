# Agents and Tools · Part 8 of 26: Human Gates, Reliability Math, Agent Prompts

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Human-in-the-loop gates
2. Agents work per step and fail per task
3. Agent reliability benchmarks: tau-bench, tau2-bench, METR time horizons
4. The agent system prompt: six blocks

## Key takeaways

- Gate irreversible actions. Keep approval volume low.
- Per-step reliability compounds. Measure pass^k.
- Ask which k, which domain, audited?
- Six blocks. Boundaries and uncertainty first.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_compounding_in_three_lines.py` | The compounding in three lines | yes |
| `code/02_lab_measure_pass_k_from_replays.py` | Measure pass^k from replays | yes |
| `code/03_building_a_six_block_prompt.py` | Building a six block prompt | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_measure_pass_k_from_replays.py` prints:

```text
refund all 8 passed: False
address all 8 passed: True
cancel all 8 passed: False
pass^1 = 0.88
pass^8 = 0.33
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A human approves every agent action. Is the system safe?**

- A. Yes, a person sees every action
- B. Only if the reviewer is an expert
- C. No, approval fatigue makes it a formality

<details><summary>Answer</summary>

**C. No, approval fatigue makes it a formality**. Gates fail on volume. Cut volume upstream.

</details>

**2. Two agents at 90 percent give 81 percent. Does that prove multi-agent is bad?**

- A. No, the errors are usually not independent
- B. Yes, the multiplication proves it
- C. Only when tasks are long

<details><summary>Answer</summary>

**A. No, the errors are usually not independent**. Arithmetic is intuition. Measured pass^k is evidence.

</details>

**3. A vendor reports one tau-bench percentage. Can you quote it as a service level?**

- A. No, ask which pass^k and which domain
- B. Yes, if it beats other models
- C. Yes, it is a public benchmark

<details><summary>Answer</summary>

**A. No, ask which pass^k and which domain**. One score is not a service level.

</details>

**4. Should you put every rule in the system prompt, to be safe?**

- A. Yes, if the model is large enough
- B. No, it costs every turn and rules clash
- C. Yes, more rules make it safer

<details><summary>Answer</summary>

**B. No, it costs every turn and rules clash**. Rules in tool descriptions. Enforcement in code.

</details>

## Say it in the interview

**Say it: human gates**

- Gate anything irreversible, and make it judgeable.
- Escalate with the full context.
- Reduce volume, never weaken the gate.

**Say it: per step, per task**

- Agents work per step, fail per task.
- Measure pass^k, not one lucky run.
- Fewer model steps, bounded consequences.

**Say it: benchmarks**

- Cite pass^k. Buyers get the eighth attempt.
- Coordination and task length both hurt.
- Bound steps. Verify outcomes in code.

**Say it: the system prompt**

- Never skip boundaries and uncertainty.
- Uncertainty decides the bad day.
- Prompts guide. Code enforces.

## Homework

- [ ] Compute 0.95 ** 20 and 0.99 ** 20
- [ ] List one agent's irreversible actions
- [ ] Write one boundary and one uncertainty rule
- [ ] Ask four questions of one benchmark score
