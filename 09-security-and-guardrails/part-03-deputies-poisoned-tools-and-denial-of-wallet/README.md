# Security and Guardrails · Part 3 of 11: Deputies, Poisoned Tools and Denial of Wallet

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. The confused deputy
2. Tool poisoning and MCP server security
3. Data and model poisoning, and supply chain
4. Unbounded consumption (denial of wallet)
5. OWASP Top 10 for LLM Applications

## Key takeaways

- Check the user's rights, not the agent's
- Tool descriptions are prompts; pin and scope
- Pin hashes, prefer safetensors, patch PyTorch
- Enforce budgets before the call runs
- Name the edition, a control, a test

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_check_the_caller_not_the_agent.py` | Check the caller, not the agent | yes |
| `code/02_check_the_hash_before_loading.py` | Check the hash before loading | yes |
| `code/03_lab_build_a_tiny_budget_guard.py` | Build a tiny budget guard | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_build_a_tiny_budget_guard.py` prints:

```text
2000 ok, spent 0.0023
3000 ok, spent 0.0056
6000 too big
4800 blocked
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. The agent's service account can read every ticket. Is this user's request authorised?**

- A. Yes, because the agent is trusted
- B. Only if this user may read it
- C. Yes, the service account has access

<details><summary>Answer</summary>

**B. Only if this user may read it**. Authorised means authorised for this person

</details>

**2. Your agent uses an MCP server. Is it secure because MCP is a standard?**

- A. Depends who wrote it, what it calls
- B. Yes, standards make servers secure
- C. Only if the model skips descriptions

<details><summary>Answer</summary>

**A. Depends who wrote it, what it calls**. A standard is not a security review

</details>

**3. You load a pickle checkpoint with torch.load(path, weights_only=True). Is that safe?**

- A. Only on a patched version; prefer safetensors
- B. Yes, if the file is open data
- C. Yes, on any PyTorch version

<details><summary>Answer</summary>

**A. Only on a patched version; prefer safetensors**. Ask which version, and who can edit the data

</details>

**4. The provider rate-limits your API key. Are your bill and other tenants protected?**

- A. Yes, the provider's limit covers us
- B. Yes, if the model is cheap enough
- C. No, you need your own caps and budgets

<details><summary>Answer</summary>

**C. No, you need your own caps and budgets**. Provider limits protect the provider, not you

</details>

**5. An engineer quotes the 2023 OWASP LLM list as current. What is wrong?**

- A. Nothing, the list never changes
- B. It was revised; name the edition
- C. OWASP covers only web apps

<details><summary>Answer</summary>

**B. It was revised; name the edition**. Name the edition; know your vector store item

</details>

## Say it in the interview

**Answer: the confused deputy**

- Least privilege means the user's privilege
- Anyone can borrow the agent's power
- Delegated token, or check rights in code

**Answer: MCP server security**

- The tool layer is an injection surface
- Review, pin versions, minimal scopes
- Audience-bound tokens, no passthrough

**Answer: poisoning and supply chain**

- Poisoning is injection with patience
- Trusted registries, pinned hashes, safetensors
- An eval set catches behaviour changes

**Answer: unbounded consumption**

- No crash needed, just make it expensive
- Caps, rate limits, and a reserved budget
- Security control as much as FinOps

**Answer: the OWASP LLM Top 10**

- A checklist for threat modelling
- Agency, output handling, embedding weaknesses
- A canary document that fails the build

## Homework

- [ ] List every service account your agent uses
- [ ] Check one tool call for a rights check
- [ ] Try pip install --require-hashes on a lockfile
- [ ] Walk the OWASP 2025 list against one app
