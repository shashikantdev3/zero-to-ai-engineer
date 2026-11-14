# Agents and Tools · Part 23 of 26: Audit Ledgers, Multi-Agent Debate, Agent Evaluation

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Audit ledger
2. The multi-agent debate: shared mutable state is the dividing line
3. MAST: the current numbers and "better models will not fix it"
4. Agent evaluation at four levels, with cost as a first-class metric

## Key takeaways

- Chain, verify, anchor the head hash
- Shared mutable state is the dividing line
- Fix the design; the model comes last
- Four levels; gate on accuracy and cost

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_hashing_one_entry.py` | Hashing one entry | yes |
| `code/02_appending_to_the_ledger.py` | Appending to the ledger | yes |
| `code/03_verifying_the_whole_chain.py` | Verifying the whole chain | yes |
| `code/04_lab_catch_an_edit_in_a_hash_chain.py` | Catch an edit in a hash chain | yes |
| `code/05_scoring_a_trajectory.py` | Scoring a trajectory | yes |
| `code/06_full_and_partial_credit.py` | Full and partial credit | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_catch_an_edit_in_a_hash_chain.py` prints:

```text
entry 0 intact: True
entry 1 intact: False
entry 2 intact: False
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Is a hash-chained audit ledger tamper-proof?**

- A. No, it is tamper-evident only
- B. Yes, if every entry is hashed
- C. Yes, edits become impossible

<details><summary>Answer</summary>

**A. No, it is tamper-evident only**. Tamper-evident, not tamper-proof: anchor the head hash

</details>

**2. Is a multi-agent system better than a single agent?**

- A. Yes, parallel agents always win
- B. No, multi-agent never really works
- C. It depends on shared mutable state

<details><summary>Answer</summary>

**C. It depends on shared mutable state**. Any answer without a condition is a slogan

</details>

**3. Will a stronger base model fix most multi-agent failures?**

- A. Mostly no, they are design failures
- B. Yes, if every agent uses it
- C. Yes, the failures are model weakness

<details><summary>Answer</summary>

**A. Mostly no, they are design failures**. Fix the design first; swap the model last

</details>

**4. Your agent scores 92% accuracy on the eval suite. Ship it?**

- A. Yes, ninety-two percent is enough
- B. Not before checking cost and reliability
- C. Yes, if transcripts match exactly

<details><summary>Answer</summary>

**B. Not before checking cost and reliability**. Ask cost per successful task, and pass^k

</details>

## Say it in the interview

**Say it in the interview**

- Who decided what, based on what
- Verify by recomputing from the start
- Tamper-evident; store the head hash apart

**Say it in the interview**

- Two published positions; I give both
- Parallel reads; shared writes serialised

**Say it in the interview**

- Most failures are design failures
- Specs, typed handoffs, stop rules, verification

**Say it in the interview**

- Step, trajectory, outcome, system
- CI gates on accuracy and cost per task

## Homework

- [ ] Run the lab; edit a different record
- [ ] Compare the head hash to a stored copy
- [ ] List four eval levels for one agent
- [ ] Practise the multi-agent answer
