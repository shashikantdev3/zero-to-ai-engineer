# Agents and Tools · Part 12 of 26: Checkpoints, Interrupts, Streaming and CrewAI

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Checkpoints and persistence
2. Interrupt (LangGraph human-in-the-loop)
3. Subgraphs and streaming modes
4. CrewAI

## Key takeaways

- Checkpoints are at least once. Add idempotency keys.
- Interrupt first. The node reruns on resume.
- Subgraphs for modules, stream mode by audience.
- CrewAI for roles, LangGraph for explicit gates.

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_tiny_graph_to_save.py` | A tiny graph to save | after `pip install langgraph` |
| `code/02_compile_run_read_the_history.py` | Compile, run, read the history | after `pip install langgraph` |
| `code/03_lab_crash_resume_pay_only_once.py` | Crash, resume, pay only once | yes |
| `code/04_a_node_that_asks_a_human.py` | A node that asks a human | after `pip install langgraph` |
| `code/05_pause_then_resume_the_thread.py` | Pause, then resume the thread | after `pip install langgraph` |
| `code/06_a_graph_to_reuse_as_a_node.py` | A graph to reuse as a node | after `pip install langgraph` |
| `code/07_plug_it_in_stream_updates.py` | Plug it in, stream updates | after `pip install langgraph` |
| `code/08_define_a_crewai_agent.py` | Define a CrewAI agent | after `pip install crewai` |
| `code/09_task_crew_kickoff.py` | Task, crew, kickoff | after `pip install crewai` |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_crash_resume_pay_only_once.py` prints:

```text
crashed, saved: {}
node ran 2 times
payments sent: 1
saved: {'paid': True}
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A node moves money and crashes mid-run. Does it run exactly once on resume?**

- A. No, a crash inside the node reruns it
- B. Yes, checkpoints make every step exactly once
- C. Only if the thread ID changes

<details><summary>Answer</summary>

**A. No, a crash inside the node reruns it**. Checkpoints are at least once. Idempotency makes them safe.

</details>

**2. A node sends a notification, then calls interrupt. After resume, why did it send twice?**

- A. The node reran from the top
- B. The checkpointer saved it twice
- C. Command resume was called twice

<details><summary>Answer</summary>

**A. The node reran from the top**. Resume reruns the node. Put interrupt first.

</details>

**3. Your agent now streams tokens. Does the whole run finish faster?**

- A. Yes, total latency drops
- B. Only in updates mode
- C. No, only perceived latency improves

<details><summary>Answer</summary>

**C. No, only perceived latency improves**. Streaming cuts time to first token, not total time.

</details>

**4. CrewAI and LangGraph do the same thing, so pick either. Good answer?**

- A. Yes, they are interchangeable
- B. No, manager delegation is less explicit
- C. Only CrewAI supports many agents

<details><summary>Answer</summary>

**B. No, manager delegation is less explicit**. Manager delegation is less explicit than a code edge.

</details>

## Say it in the interview

**Say it in the interview**

- State saved after each step, under a thread ID.
- Checkpointing is not exactly-once execution.
- Side effects need an idempotency key or state check.

**Say it in the interview**

- Interrupt pauses with the plan for a person.
- Resume reruns the node. Interrupt goes first.
- Bind the approval to this exact plan.

**Say it in the interview**

- Each agent is its own graph.
- Tokens for users, updates for logs.
- Faster first token, same total time.

**Say it in the interview**

- CrewAI: roles, fast. LangGraph: explicit graph.
- Approval gate: LangGraph. Short pipeline: CrewAI.
- State your hands-on level first.

## Homework

- [ ] Print state history for a checkpointed graph.
- [ ] Pause with interrupt, resume with Command.
- [ ] Compare updates and values stream modes.
- [ ] Write when you would choose CrewAI.
