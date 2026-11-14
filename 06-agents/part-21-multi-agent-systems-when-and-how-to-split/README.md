# Agents and Tools · Part 21 of 26: Multi-Agent Systems: When and How to Split

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Start with one agent
2. Orchestrator (supervisor) pattern
3. Other topologies: hierarchical, sequential, group chat, blackboard, network
4. Typed handoff
5. Shared state

## Key takeaways

- One agent first, split for a named reason
- Orchestrator owns the task, not the approval
- Most controlled topology that solves it
- Typed handoffs, validated on receipt
- One state, one owner per field

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_finding_schema.py` | The Finding schema | yes |
| `code/02_the_evidence_check.py` | The evidence check | yes |
| `code/03_lab_break_the_evidence_check.py` | Break the evidence check | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_break_the_evidence_check.py` prints:

```text
naive check: True
ok
too short
unknown source
no match
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A teammate adds a second, specialised agent. What do you ask first?**

- A. Can we add a third one?
- B. What did it improve, measured how?
- C. Which model does it run on?

<details><summary>Answer</summary>

**B. What did it improve, measured how?**. Every extra agent must earn its place with a measurement

</details>

**2. Should the orchestrator also approve risky steps?**

- A. Yes, it sees the whole task
- B. No, approval belongs outside it
- C. Only if it runs a strong model

<details><summary>Answer</summary>

**B. No, approval belongs outside it**. What tool output can steer must not authorise

</details>

**3. Someone says network is best because it is most flexible. What do you ask?**

- A. How do you guarantee termination?
- B. How many agents can join?
- C. Which framework supports it?

<details><summary>Answer</summary>

**A. How do you guarantee termination?**. Flexibility needs stop rules and loop detection

</details>

**4. Agent B misread agent A's summary. How would you detect it?**

- A. Validate a typed handoff on receipt
- B. Let agents read all messages
- C. Tell agent B to read carefully

<details><summary>Answer</summary>

**A. Validate a typed handoff on receipt**. Free text hides errors, schemas expose them

</details>

**5. Five agents work on one task. What should they share?**

- A. The full chat history
- B. Each agent's private copy
- C. Structured state with field owners

<details><summary>Answer</summary>

**C. Structured state with field owners**. Share structured state, not full transcripts

</details>

## Say it in the interview

**Interview: start with one agent**

- One agent first
- Split only for a reason I can name
- Least privilege, expressed as agent boundaries

**Interview: the orchestrator**

- One place owns the task
- Known order? The orchestrator is code

**Interview: choosing a topology**

- A line from most control to least
- Most controlled pattern that solves the problem

**Interview: typed handoffs**

- Most bugs are handoff bugs
- Schema, validated on receipt, with IDs
- Turn it said so into a code check

**Interview: shared state**

- One source of truth per task
- Who wrote what: half an audit trail

## Homework

- [ ] Sketch one agent, name one split reason
- [ ] Order the five topologies by control
- [ ] Add a failing test to the lab
- [ ] Write a field ownership table
