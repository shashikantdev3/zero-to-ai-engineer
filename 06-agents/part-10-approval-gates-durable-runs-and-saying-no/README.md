# Agents and Tools · Part 10 of 26: Approval Gates, Durable Runs, and Saying No

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Gate on the action, not the confidence
2. Durable execution and the two timeouts
3. When not to build an agent: the checklist
4. Question drill: Agents additions

## Key takeaways

- Gate on the action, then measure the gate
- Transport: stream or poll. Long runs: checkpoint.
- Any no means build something smaller
- Quote pass^k, make bad steps survivable

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_gate_with_no_confidence_input.py` | A gate with no confidence input | yes |
| `code/02_lab_measure_your_approval_gate.py` | Measure your approval gate | yes |
| `code/03_checkpoint_and_release_the_worker.py` | Checkpoint and release the worker | yes |
| `code/04_resume_expire_apply_once.py` | Resume, expire, apply once | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_measure_your_approval_gate.py` prints:

```text
reviewed: 6
rejection rate: 0%
p50 seconds: 2.5
rubber stamp? True
expired: True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Should actions auto-approve when model confidence is above 0.9?**

- A. No, gate on what it can break
- B. Yes, 0.9 is high enough
- C. Yes, if the model explains itself

<details><summary>Answer</summary>

**A. No, gate on what it can break**. Gate on the action, never on confidence

</details>

**2. A run waits hours for a human and keeps timing out. The fix?**

- A. Checkpoint state and release the worker
- B. Retry the whole run from scratch
- C. Raise the gateway timeout

<details><summary>Answer</summary>

**A. Checkpoint state and release the worker**. Long waits need checkpoints, not bigger timeouts

</details>

**3. Agents are more flexible. Should you always build one?**

- A. Yes, flexibility always wins
- B. Yes, if the model is strong
- C. No, run the checklist first

<details><summary>Answer</summary>

**C. No, run the checklist first**. No eval set or tool list means not ready

</details>

**4. Your approval gate has a 0% rejection rate. Is that good news?**

- A. Yes, reviewers trust the system
- B. Probably not, it suggests rubber stamping
- C. Yes, the model is always right

<details><summary>Answer</summary>

**B. Probably not, it suggests rubber stamping**. Zero rejections means check the reviewers

</details>

## Say it in the interview

**Say it in the interview**

- Gate on the action, not the confidence.
- Confidence can add review, never remove it.
- Zero rejections means delay, not control.

**Say it in the interview**

- Stream, poll, or batch the transport.
- Holding a process for hours is a leak.
- Deterministic steps, idempotent side effects.

**Say it in the interview**

- Six checks before any agent.
- Often the real problem is bad search.
- Offer the smaller thing that ships.

## Homework

- [ ] Write needs_human for three real actions
- [ ] Rerun the lab with a rejection
- [ ] Sketch a four hour approval run
- [ ] Run the six checks on one idea
