# Agents and Tools · Part 17 of 26: MCP: One Protocol for Tools

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Model Context Protocol (one open protocol)
2. Host, client, server
3. Tools, resources, prompts (and client features)
4. Transports: stdio versus streamable HTTP

## Key takeaways

- One protocol; trust stays in your code
- Host, one client per server, server enforces
- Model, application, user
- stdio runs as you; HTTP needs web security

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_resource_in_python.py` | A resource in Python | after `pip install mcp` |
| `code/02_a_prompt_template.py` | A prompt template | after `pip install mcp` |
| `code/03_lab_count_and_route_mcp_calls.py` | Count and route MCP calls | yes |
| `code/04_choosing_the_transport.py` | Choosing the transport | after `pip install mcp` |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_count_and_route_mcp_calls.py` prints:

```text
custom: 40
with MCP: 13
tools/call -> model
resources/read -> application
prompts/get -> user
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Who authorises a tools/call made over MCP?**

- A. Your server, with your rules
- B. Anthropic, since MCP is theirs
- C. The MCP protocol itself

<details><summary>Answer</summary>

**A. Your server, with your rules**. MCP connects; your server authorises

</details>

**2. In MCP, where does the model live?**

- A. Inside the MCP client
- B. With the host application
- C. Inside the MCP server

<details><summary>Answer</summary>

**B. With the host application**. The client is a connection, not the model

</details>

**3. Who decides when a resource enters the context?**

- A. The application
- B. The MCP server
- C. The model

<details><summary>Answer</summary>

**A. The application**. Resources are app-controlled, not model-controlled

</details>

**4. Is a third-party stdio server safe because it is local?**

- A. Yes, MCP sandboxes stdio servers
- B. Yes, local means no real risk
- C. No, it runs with your privileges

<details><summary>Answer</summary>

**C. No, it runs with your privileges**. Local is not safe; remote is not free

</details>

**5. A stdio server prints debug text to stdout. What happens?**

- A. Nothing, it shows in the log
- B. The JSON-RPC stream breaks
- C. Only HTTP clients are affected

<details><summary>Answer</summary>

**B. The JSON-RPC stream breaks**. Debug output on stdout is the classic bug

</details>

## Say it in the interview

**MCP in an interview**

- MCP solves the integration explosion
- One server, any compatible host
- It standardises connection, not permission

**Roles in an interview**

- Host creates one client per server
- The server never sees the model directly
- Host trusts servers; servers enforce calls

**Primitives in an interview**

- Model, application, user
- Sampling and elicitation flow back
- State changes go behind narrow tools

**Transports in an interview**

- Pick by location and users
- Review, pin, log to stderr
- Remote means owning web API security

## Homework

- [ ] Rerun the lab with your own counts
- [ ] Explain the three roles in three sentences
- [ ] Name one tool, resource, prompt
- [ ] Write a stdio server logging to stderr
