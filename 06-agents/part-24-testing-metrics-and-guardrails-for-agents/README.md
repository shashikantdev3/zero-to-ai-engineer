# Agents and Tools · Part 24 of 26: Testing, Metrics and Guardrails for Agents

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Testing the agent harness deterministically
2. Agent operating metrics: iterations per run as a leading indicator
3. In-loop guardrails
4. Question drill: Multi-agent additions

## Key takeaways

- Mock the model, unit test the harness
- Rising iterations warn before anything errors
- Guard consequences between deciding and acting
- Design and verification beat a bigger model

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_testing_the_step_cap.py` | Testing the step cap | yes |
| `code/02_testing_refusal_with_full_fixtures.py` | Testing refusal with full fixtures | yes |
| `code/03_lab_an_iterations_alert_by_hand.py` | An iterations alert by hand | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_an_iterations_alert_by_hand.py` prints:

```text
p50 last week: 5
p50 this week: 7
rise: 40 percent
errors: 0
ALERT
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Which part of an agent is non-deterministic?**

- A. The tools and the router
- B. The whole agent loop
- C. Only the model call

<details><summary>Answer</summary>

**C. Only the model call**. Only the model varies, so test everything else

</details>

**2. Can error rate and latency show a tool returning worse search results?**

- A. Yes, errors would rise
- B. No, nothing errors
- C. Yes, latency would spike

<details><summary>Answer</summary>

**B. No, nothing errors**. Quality decay is silent to error dashboards

</details>

**3. Is a vendor SDK guardrail enough as your in-loop control?**

- A. Not if injected text can steer it
- B. Yes, vendors handle consequences
- C. Yes, if the model checks itself

<details><summary>Answer</summary>

**A. Not if injected text can steer it**. Ask what can steer the guardrail itself

</details>

**4. Would a stronger model fix most multi-agent failures?**

- A. Mostly no, they are design problems
- B. Yes, smarter models coordinate better
- C. Yes, if every agent is upgraded

<details><summary>Answer</summary>

**A. Mostly no, they are design problems**. Fix the design, not the model size

</details>

## Say it in the interview

**Say it in the interview**

- Everything except the model call is code
- Mock the model, assert the harness
- An untested limit is just a hope

**Say it in the interview**

- Iterations and cost per run lead
- An alert, not just a dashboard
- Per-tool success and approval rejections

**Say it in the interview**

- In-loop guardrails are about consequence
- The last point before something irreversible
- Self-checking is quality, not control

## Homework

- [ ] Write a step-cap test with a looping mock
- [ ] Test self-approval refusal with a full fixture
- [ ] Rerun the lab with your own numbers
- [ ] List in-loop checks for one action
