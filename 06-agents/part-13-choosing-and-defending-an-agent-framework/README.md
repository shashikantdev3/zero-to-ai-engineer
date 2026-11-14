# Agents and Tools · Part 13 of 26: Choosing and Defending an Agent Framework

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Microsoft Agent Framework, Semantic Kernel, AutoGen and AG2
2. Vendor agent SDKs (currency)
3. Plain code as a framework choice
4. Defending a framework choice to an auditor

## Key takeaways

- Agent Framework leads. Each older line differs.
- Vendor SDKs: verify versions, gate in code.
- Plain code: own the loop, test the gates.
- Defend controls the model cannot bypass.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_lab_a_loop_with_a_code_gate.py` | A loop with a code gate | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/01_lab_a_loop_with_a_code_gate.py` prints:

```text
step 0: look allowed=True
step 1: look allowed=True
step 2: change allowed=False
resume at 3
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Which statement about AG2 is true?**

- A. A community fork of AutoGen
- B. The new name for Semantic Kernel
- C. Microsoft's renamed AutoGen product

<details><summary>Answer</summary>

**A. A community fork of AutoGen**. AG2 is a community fork. Each line has its own state.

</details>

**2. A vendor SDK ships guardrails. Do you still need your own gate?**

- A. Only if the vendor is small
- B. Yes, a gate that runs as code
- C. No, the guardrail covers it

<details><summary>Answer</summary>

**B. Yes, a gate that runs as code**. A guardrail the model can steer is not a gate.

</details>

**3. How do you resume a paused plain-code run after a restart?**

- A. Load state from a database by run ID
- B. Rerun the whole loop from the start
- C. You cannot without a framework

<details><summary>Answer</summary>

**A. Load state from a database by run ID**. Persist state by run ID. Plain code is real.

</details>

**4. Is 'LangGraph is compliant' a good answer to a bank auditor?**

- A. Yes, if the version is pinned
- B. Yes, the framework is certified
- C. No, show the control itself

<details><summary>Answer</summary>

**C. No, show the control itself**. Frameworks are not controls. Commit to one choice.

</details>

## Say it in the interview

**The Microsoft family answer**

- Currency question: give the state and the date.
- Different lines, different states. Check the migration guide.
- New Microsoft work starts on Agent Framework.

**The vendor SDK answer**

- Three vendor SDKs, known at knowledge level.
- A guardrail counts only if it runs as code.
- State your level. Check the docs first.

**The four part defence**

- Twenty lines. Every rule is testable code.
- Choice, alternative, reason.
- Then say exactly when you would switch.

**The auditor answer**

- Defend controls, not a framework.
- The model proposes. Code decides. Logs never change.
- Can the model bypass it? No, by construction.

## Homework

- [ ] Write each Microsoft line's state from memory
- [ ] Check the release page and note the date
- [ ] Write your four part framework defence
- [ ] Rerun the lab with a signed change
