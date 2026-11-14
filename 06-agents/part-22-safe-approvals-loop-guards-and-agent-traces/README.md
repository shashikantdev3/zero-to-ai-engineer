# Agents and Tools · Part 22 of 26: Safe Approvals, Loop Guards and Agent Traces

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Signed approval
2. Stop rule for handoff loops
3. MAST failure taxonomy
4. Tracing and trajectory evals for agents

## Key takeaways

- Human signs exact plan; executor checks everything
- Cap handoffs, hash progress, escalate
- 14 modes, 3 categories, version-dependent numbers
- Trace every step, grade the path

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_approval_message.py` | The approval message | yes |
| `code/02_the_console_signs.py` | The console signs | yes |
| `code/03_who_may_approve_this_plan.py` | Who may approve this plan? | yes |
| `code/04_rebuild_the_message_then_verify.py` | Rebuild the message, then verify | yes |
| `code/05_expiry_and_a_one_time_nonce.py` | Expiry and a one-time nonce | yes |
| `code/06_tampered_valid_replayed.py` | Tampered, valid, replayed | yes |
| `code/07_the_loop_guard_in_code.py` | The loop guard in code | yes |
| `code/08_lab_why_timestamps_break_the_guard.py` | Why timestamps break the guard | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/08_lab_why_timestamps_break_the_guard.py` prints:

```text
101 whole: False progress: False
102 whole: False progress: True
103 whole: False progress: True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. An approval's signature verifies. Is that enough to run the plan?**

- A. No, also check authority, expiry and nonce
- B. Yes, if a reviewer agent also agrees
- C. Yes, a valid signature proves approval

<details><summary>Answer</summary>

**A. No, also check authority, expiry and nonce**. Signature proves who; authority decides whether

</details>

**2. Two agents keep handing a task back and forth. What is the real fix?**

- A. A stronger model for both agents
- B. Better prompts so the agents agree
- C. A handoff cap and repeated-state check

<details><summary>Answer</summary>

**C. A handoff cap and repeated-state check**. Code, not prompts, guarantees termination

</details>

**3. An interviewer asks for MAST's failure percentages. What is the safe answer?**

- A. Average the figures from both versions
- B. Name the version; figures changed between versions
- C. Quote 44, 32, 24 as fixed facts

<details><summary>Answer</summary>

**B. Name the version; figures changed between versions**. Figures depend on the paper version

</details>

**4. Your agent called refund on a tracking request. You logged only the final answer. What can you explain?**

- A. Almost nothing; you need the trace
- B. The cause, from the final token count
- C. Everything; the answer shows the reasoning

<details><summary>Answer</summary>

**A. Almost nothing; you need the trace**. No trace, no explanation

</details>

## Say it in the interview

**Signed approval, in the interview**

- A reviewer agent can be steered
- The signature covers the plan hash
- Agents never hold the signing key

**Stop rule, in the interview**

- The bug is a missing stop rule
- Cap, hash progress, require something new
- Escalate with both agents' views

**MAST, in the interview**

- Most failures are not the model
- Spec, misalignment, verification and termination
- Fix the system before a bigger model

**Tracing, in the interview**

- A right answer can hide a bad path
- Trace every step, evaluate trajectories
- Correlation IDs, cost per query, CI scorecard

## Homework

- [ ] Tamper with the approved plan, watch it fail
- [ ] Break the loop guard with a timestamp
- [ ] Three MAST categories, one control each
- [ ] List the fields of a tool span
