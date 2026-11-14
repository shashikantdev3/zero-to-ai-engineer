# Agents and Tools · Part 26 of 26: Agent Take-Homes, Approval Gates, Copilot Studio

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Agent take-homes: the control is the exam
2. Human-in-the-loop in a take-home with no humans
3. Question drill: Design briefs and take-homes
4. Tool calling in Copilot Studio

## Key takeaways

- The controls are the exam
- Persist, bind to plan hash, execute once
- Cut features, never controls
- Descriptions steer; credentials decide reach

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_requesting_approval.py` | Requesting approval | yes |
| `code/02_resuming_after_approval.py` | Resuming after approval | yes |
| `code/03_lab_break_the_gate_on_purpose.py` | Break the gate on purpose | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_break_the_gate_on_purpose.py` prints:

```text
rejected: stale or mismatched
rejected: stale or mismatched
executed refund 42
skipped: already executed
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Which take-home submission scores better with reviewers?**

- A. Five features with no approval gate
- B. One action with a gate and evals
- C. Many features, limits left unstated

<details><summary>Answer</summary>

**B. One action with a gate and evals**. Reviewers grade the gate, not the feature count

</details>

**2. The agent waits on input('approve? '). What breaks?**

- A. A restart loses the pending approval
- B. Nothing, a human still approves
- C. The model can type its own yes

<details><summary>Answer</summary>

**A. A restart loses the pending approval**. Persist the pause, and bind it to the plan

</details>

**3. No framework is mandated. What should the take-home use?**

- A. The framework with most features
- B. A full multi-agent graph framework
- C. The smallest thing that works

<details><summary>Answer</summary>

**C. The smallest thing that works**. An unneeded framework reads as poor judgement

</details>

**4. With generative orchestration, can the agent call anything in the tenant?**

- A. No: added tools, DLP and credentials limit it
- B. Yes, the model decides freely
- C. Only when classic topics are off

<details><summary>Answer</summary>

**A. No: added tools, DLP and credentials limit it**. The model picks; the maker, DLP and credentials limit

</details>

## Say it in the interview

**The take-home answer**

- The agent is easy; the controls are the exam
- Cut features, never controls, and write it down
- Smallest stack, unless the brief mandates one

**The approval answer**

- The gate is a durable pause
- Bound to the plan hash, executed once
- Survives restarts, like real production approvals

**The Copilot Studio answer**

- The platform owns the loop; descriptions are prompts
- Connector authentication is the identity choice
- Platform buys speed; code buys control

## Homework

- [ ] Draft a README in the five-part order
- [ ] Run the gate lab and add a case
- [ ] Write one tool description: when, and when not
- [ ] Rehearse the take-home answer in one minute
