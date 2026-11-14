# Security and Guardrails · Part 6 of 11: Four Architectural Leaks and Their Fixes

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Group overage in token claims
2. Tenant isolation and the semantic cache leak
3. Sandboxing code execution
4. Improper output handling

## Key takeaways

- Handle overage: app roles, Graph, default deny
- Filter every cache lookup by tenant and scope
- Sandbox it: no network, no secrets, hard limits
- Treat model output as untrusted input

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_reading_groups_safely.py` | Reading groups safely | yes |
| `code/02_three_tokens_three_paths.py` | Three tokens, three paths | yes |
| `code/03_filter_inside_the_similarity_search.py` | Filter inside the similarity search | yes |
| `code/04_exact_match_keys_carry_the_tenant.py` | Exact-match keys carry the tenant | yes |
| `code/05_lab_watch_a_semantic_cache_leak.py` | Watch a semantic cache leak | yes |
| `code/06_building_the_sandbox_command.py` | Building the sandbox command | yes |
| `code/07_limits_mount_and_timeout.py` | Limits, mount, and timeout | yes |
| `code/08_validating_an_action_with_pydantic.py` | Validating an action with Pydantic | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_watch_a_semantic_cache_leak.py` prints:

```text
shared: A refund terms
scoped to B: None
scoped to A: A refund terms
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A user is in 400 groups and your filter reads only the groups claim. What do they get?**

- A. Entra ID blocks their sign in
- B. Empty results
- C. The token lists the first 200

<details><summary>Answer</summary>

**B. Empty results**. Overage drops groups; handle it and store object IDs

</details>

**2. One shared semantic cache saves money. Tenant B asks what Tenant A asked. What happens?**

- A. B gets an answer from A's documents
- B. The cache misses because keys differ
- C. The model blocks it on permissions

<details><summary>Answer</summary>

**A. B gets an answer from A's documents**. Ask: whose documents built the cached answer?

</details>

**3. Generated code runs in Docker as root, network on, API key in the environment. Safe?**

- A. No, it can leak the key
- B. Yes, if the image is official
- C. Yes, containers isolate everything

<details><summary>Answer</summary>

**A. No, it can leak the key**. A container alone is not a sandbox

</details>

**4. It's our model, so we render its answer as raw HTML. A retrieved page added a script tag. What happens?**

- A. It shows up as plain text
- B. The model strips it out first
- C. The script runs in the browser

<details><summary>Answer</summary>

**C. The script runs in the browser**. Escape model output before rendering it

</details>

## Say it in the interview

**Group overage, in the interview**

- Past the limit, groups become an overage marker
- App groups or roles; otherwise Graph, cached briefly
- Default deny, always

**Tenant isolation, in the interview**

- The leak people miss is the cache
- Mandatory tenant filter or namespace; generic answers only
- Same rule for index and logs, plus canary tests

**Sandboxing, in the interview**

- Generated code is a stranger's code
- No network, no secrets, non-root, limits, throwaway
- Hostile code: gVisor, microVM, or managed sandbox

**Output handling, in the interview**

- Model output is user input with extra steps
- Escape, allowlist, parameterise, validate
- Schema checks shape, not truth

## Homework

- [ ] Add a scope check to the cache lab
- [ ] Cache the Graph call briefly
- [ ] Feed three bad outputs to the Action model
- [ ] List the sandbox flags from memory
