# Agents and Tools · Part 19 of 26: A2A, Stateless MCP and Gateways

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. A2A (Agent2Agent protocol)
2. MCP versus A2A
3. MCP specification currency: the stateless revision
4. Designing an MCP gateway at scale

## Key takeaways

- A2A: agent cards, tasks, opaque internals
- Capability, MCP. Agent, A2A. Often both.
- Name the revision; verify; check the host
- Edge, limits, tenant-keyed cache, pinned registry

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_lab_back_of_envelope_gateway_sizing.py` | Back-of-envelope gateway sizing | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/01_lab_back_of_envelope_gateway_sizing.py` prints:

```text
average rps: 1389
peak rps: 4167
connections: 100
False
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Over A2A, can your agent see the remote agent's tool calls?**

- A. No, it is opaque by design
- B. Yes, agents share memory over A2A
- C. Only after the task completes

<details><summary>Answer</summary>

**A. No, it is opaque by design**. A2A shares tasks, never memory or internals

</details>

**2. MCP already connects everything. Is A2A redundant?**

- A. Yes, MCP fully covers agent delegation
- B. No, A2A delegates to opaque agents
- C. Yes, A2A is an older MCP

<details><summary>Answer</summary>

**B. No, A2A delegates to opaque agents**. MCP for tool calls; A2A for delegation

</details>

**3. An interviewer asks how the MCP handshake works. What is the safest answer?**

- A. Recite every deprecation from your notes
- B. Describe the handshake as permanent
- C. Name the revision and check host support

<details><summary>Answer</summary>

**C. Name the revision and check host support**. Which revision, and does your host support it?

</details>

**4. Should your gateway forward the user's token straight to MCP servers?**

- A. No, token passthrough is forbidden
- B. Yes, if the gateway holds an API key
- C. Yes, it saves a token exchange

<details><summary>Answer</summary>

**A. No, token passthrough is forbidden**. Never pass tokens through; check the audience

</details>

## Say it in the interview

**Explaining A2A**

- Agent card in, task out, clear lifecycle
- I see the contract, not the internals
- Treat it like any external service

**Explaining MCP versus A2A**

- Not competitors: different jobs
- A2A delegates to agents I don't control
- Capability, MCP. Agent, A2A.

**Explaining MCP spec currency**

- Name the revision every time
- Stateless headline; verify details; check the host
- Idempotency keys for safe reissue

**Explaining the MCP gateway**

- Stateless means a normal reverse proxy
- Claim-based tenant, budgets, tenant-keyed cache, tracing
- Pin servers; sticky routing if session-based

## Homework

- [ ] Draft an agent card for an imaginary agent
- [ ] Sort three integrations: MCP or A2A
- [ ] Record the latest MCP revision date
- [ ] Rerun the sizing lab with new numbers
