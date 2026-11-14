# Agents and Tools · Part 11 of 26: Agent Memory, LangChain and LangGraph Graphs

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Procedural memory and the four-kind vocabulary
2. LangChain, LCEL and Runnable
3. create_agent and the langchain-classic split
4. LangGraph state graph, typed state and reducers
5. Nodes, conditional edges and cycles

## Key takeaways

- Four memory kinds. Procedural changes need review.
- LCEL pipes Runnables into linear chains
- create_agent is current. Old code is classic.
- State is the contract. Reducers merge updates.
- Routing in code, so stop rules are testable

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_proposal_queue_not_a_live_edit.py` | A proposal queue, not a live edit | yes |
| `code/02_a_prompt_template.py` | A prompt template | after `pip install langchain_anthropic langchain-core` |
| `code/03_pipe_it_into_a_chain.py` | Pipe it into a chain | after `pip install langchain_anthropic langchain-core` |
| `code/04_building_an_agent.py` | Building an agent | after `pip install langchain` |
| `code/05_invoke_and_read_the_reply.py` | Invoke and read the reply | after `pip install langchain` |
| `code/06_a_state_with_reducers.py` | A state with reducers | after `pip install langgraph` |
| `code/07_lab_build_a_tiny_reducer_merge.py` | Build a tiny reducer merge | yes |
| `code/08_state_and_a_working_node.py` | State and a working node | after `pip install langgraph` |
| `code/09_the_router_is_plain_python.py` | The router is plain Python | yes |
| `code/10_wire_up_the_graph.py` | Wire up the graph | after `pip install langgraph` |

## Follow-along lab

Type it yourself, then compare your output.

`code/07_lab_build_a_tiny_reducer_merge.py` prints:

```text
['db'] 1
['db', 'io'] 2
{'findings': [], 'steps': 0}
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Where should a learned rule like 'always check X first' live?**

- A. In a vector store row
- B. In procedural memory, versioned and reviewed
- C. In the current context window

<details><summary>Answer</summary>

**B. In procedural memory, versioned and reviewed**. Learned rules are procedural: versioned and reviewed

</details>

**2. Do you need LangChain to call an LLM?**

- A. No, the SDK calls it directly
- B. Yes, it is required
- C. Only for streaming replies

<details><summary>Answer</summary>

**A. No, the SDK calls it directly**. LangChain adds swapping and composition, not access

</details>

**3. Asked how to build a LangChain agent, what is the safest answer?**

- A. Quote a popular older tutorial
- B. State the version, verify release notes
- C. Say AgentExecutor is the standard

<details><summary>Answer</summary>

**B. State the version, verify release notes**. Name your version. Verify the release notes.

</details>

**4. Two parallel nodes write the same list key with no reducer. What happens?**

- A. Both items are appended
- B. The lists merge silently
- C. LangGraph raises an error

<details><summary>Answer</summary>

**C. LangGraph raises an error**. Return updates, not mutations. Shared keys need reducers.

</details>

**5. How do you make sure the agent always escalates after five steps?**

- A. Keep that routing in tested code
- B. Add a stronger prompt instruction
- C. Let the LLM decide every edge

<details><summary>Answer</summary>

**A. Keep that routing in tested code**. Safety-critical routing belongs in testable code

</details>

## Say it in the interview

**Memory in the interview**

- Working, episodic, semantic, procedural
- Procedural is the forgotten, dangerous one
- A prompt change is a deploy

**LangChain in the interview**

- Standard interfaces, so parts are swappable
- LCEL for linear pipelines
- Loops go to LangGraph. Pin versions.

**create_agent in the interview**

- As of 1.0, create_agent on LangGraph
- AgentExecutor: plan a migration
- Check release notes. This area moves.

**State design in the interview**

- State first. It is the contract.
- Counters overwrite. Lists append.
- Nodes are testable plain functions

**Routing in the interview**

- Routers are plain, testable Python
- Code I can test, not a hope
- Stop rules live in the router

## Homework

- [ ] List four memory kinds, one example each
- [ ] Pipe prompt, model and parser
- [ ] Add a second reducer to the lab
- [ ] Unit test the router at five steps
