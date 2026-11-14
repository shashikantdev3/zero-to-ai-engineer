# Agents and Tools · Part 14 of 26: Inside Microsoft Agent Framework

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Microsoft Agent Framework: the object model
2. Agent Framework tools: local, hosted and MCP
3. Agent Framework workflows: executors and typed edges
4. Prebuilt orchestrations: sequential, concurrent, Magentic

## Key takeaways

- Client, instructions, tools. Pass a session.
- Three tool kinds, one security model
- Declared edges decide what runs next
- Pick the simplest shape that fits

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_toy_agent_with_the_real_nouns.py` | A toy agent with the real nouns | yes |
| `code/02_with_and_without_a_session.py` | With and without a session | yes |
| `code/03_lab_see_what_a_tool_tells_the_model.py` | See what a tool tells the model | yes |
| `code/04_toy_workflow_two_executors.py` | Toy workflow: two executors | yes |
| `code/05_run_along_declared_edges_only.py` | Run along declared edges only | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_see_what_a_tool_tells_the_model.py` prints:

```text
service_status
Read-only. Health of ONE service.
One of: api, worker, scheduler
{'ok': False, 'err': 'UNKNOWN'}
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. You call agent.run twice with no session. What does run two know about run one?**

- A. Only the tool results from run one
- B. Nothing, each run starts fresh
- C. Everything, the agent keeps history

<details><summary>Answer</summary>

**B. Nothing, each run starts fresh**. No session, no memory. Pass it every run.

</details>

**2. Is a hosted code interpreter safe because Microsoft runs it?**

- A. Depends on data sent and who reads output
- B. No, never use hosted tools
- C. Yes, the platform makes it safe

<details><summary>Answer</summary>

**A. Depends on data sent and who reads output**. Ask what data goes in and who reads it

</details>

**3. In an Agent Framework workflow, who decides which executor runs next?**

- A. The edges declared in the graph
- B. Whichever agent reacts first
- C. The model, like a group chat

<details><summary>Answer</summary>

**A. The edges declared in the graph**. In a workflow, edges decide what runs next

</details>

**4. The order of steps is known in advance. Which orchestration fits best?**

- A. Concurrent, because it is fastest
- B. Magentic, because it is most advanced
- C. Sequential, a simple pipeline

<details><summary>Answer</summary>

**C. Sequential, a simple pipeline**. Known order? Sequential beats Magentic.

</details>

## Say it in the interview

**Explaining the object model**

- Chat client plus instructions plus tools
- I pass a session and set budgets
- I check names against current docs

**Explaining tools**

- Descriptions are prompts. I write them carefully.
- Hosted from the platform, MCP plugs in
- Validation and the code gate stay mine

**Explaining workflows**

- A typed data-flow graph, explicit edges
- I can read what happens next
- Plain code marks the determinism boundary

**Explaining orchestrations**

- Pipeline, fan-out, or manager-orchestrated
- Cap rounds. Keep approval outside the manager.
- Known order means sequential

## Homework

- [ ] List the core nouns from memory
- [ ] Add a second described parameter to the lab
- [ ] Draw a workflow; mark the plain-code step
- [ ] Pick an orchestration for one task, write why
