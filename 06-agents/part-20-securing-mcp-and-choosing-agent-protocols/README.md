# Agents and Tools · Part 20 of 26: Securing MCP and Choosing Agent Protocols

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Tool shadowing and pinning MCP servers
2. MCP and A2A governance: neutral foundations
3. The A2A ownership test
4. Question drill: MCP and A2A additions
5. The agent protocol landscape: MCP, A2A and AG-UI

## Key takeaways

- Pin servers by hash; check arguments in code.
- Neutral governance fixes lock-in, not security.
- Own both? Handoff. Cross ownership? A2A.
- Stateless scales; side-effect tools need idempotency.
- MCP, A2A, AG-UI are layers, not rivals.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_fingerprint_the_tool_definitions.py` | Fingerprint the tool definitions | yes |
| `code/02_block_when_definitions_change.py` | Block when definitions change | no: PermissionError, see the note in the file |
| `code/03_lab_detect_a_rug_pull_offline.py` | Detect a rug pull offline | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_detect_a_rug_pull_offline.py` prints:

```text
approved: 0f2d8723eb75
reordered same: True
after edit same: False
action: block
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. All your MCP servers come from a marketplace. Does that make them safe?**

- A. Yes, if users confirm every call
- B. Yes, the marketplace vetted them
- C. No, pin them and re-review changes

<details><summary>Answer</summary>

**C. No, pin them and re-review changes**. Approval is a moment. Pinning makes it last.

</details>

**2. An interviewer says MCP is Anthropic's protocol. What is the better reply?**

- A. Nobody governs it, it is open source
- B. It now sits under the Linux Foundation
- C. Agreed, one vendor controls it

<details><summary>Answer</summary>

**B. It now sits under the Linux Foundation**. MCP is foundation governed, not single vendor.

</details>

**3. You own both agents in one repo. Should they talk over A2A?**

- A. No, use a supervisor and typed handoff
- B. Yes, for consistency everywhere
- C. Only when both use the same model

<details><summary>Answer</summary>

**A. No, use a supervisor and typed handoff**. Own both agents? A function call usually wins.

</details>

**4. MCP is governed by a foundation now. Does that make it secure?**

- A. Yes, the foundation audits every server
- B. No, security is still your job
- C. Only after A2A joins that foundation

<details><summary>Answer</summary>

**B. No, security is still your job**. Governance reduces lock-in. Security stays with you.

</details>

**5. A human must approve a change mid-run. Which wire carries it, and where is it enforced?**

- A. AG-UI carries it; server code enforces it
- B. AG-UI carries and enforces it
- C. A2A carries it; the UI enforces it

<details><summary>Answer</summary>

**A. AG-UI carries it; server code enforces it**. UI wire carries approval; server code enforces it.

</details>

## Say it in the interview

**Tool shadowing, in the interview**

- One server's text steers another's tool.
- Allowlist, pin by hash, block on change.
- Never all three of the lethal trifecta.

**Governance, in the interview**

- Governance answers the lock-in worry.
- Neutral is not secure. Verify versions.

**Ownership, in the interview**

- Own both? Supervisor and typed handoffs.
- Across ownership, the opaque contract is the point.
- Validate every reply before acting.

**The landscape, in the interview**

- Three wires: tools, agents, screen.
- AG-UI: a standard event stream to the frontend.
- Names move fast. The layering stays stable.

## Homework

- [ ] Run the lab; edit one tool description
- [ ] List your servers; mark outbound channels
- [ ] Write the A2A decision table from memory
- [ ] Sketch MCP, A2A and AG-UI for one system
