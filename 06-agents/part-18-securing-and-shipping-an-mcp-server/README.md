# Agents and Tools · Part 18 of 26: Securing and Shipping an MCP Server

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. MCP authorization: audience-bound tokens
2. Untrusted data and MCP security
3. Building and deploying an MCP server

## Key takeaways

- Token must be for you; no passthrough
- Tool output is untrusted; humans approve changes
- FastMCP is quick; remote means hardened service

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_validating_the_token_with_pyjwt.py` | Validating the token with PyJWT | yes |
| `code/02_checking_the_scope_claim.py` | Checking the scope claim | yes |
| `code/03_lab_reject_the_wrong_audience.py` | Reject the wrong audience | yes |
| `code/04_a_read_only_tool_with_fastmcp.py` | A read-only tool with FastMCP | after `pip install mcp` |
| `code/05_a_tool_that_only_requests.py` | A tool that only requests | after `pip install mcp` |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_reject_the_wrong_audience.py` prints:

```text
mcp accepted
hr rejected: audience
old rejected: expired
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A valid token from your own identity provider, issued for your HR API, reaches your MCP server. Accept it?**

- A. Yes, the signature is valid
- B. Yes, if the scopes look right
- C. No, the audience is wrong

<details><summary>Answer</summary>

**C. No, the audience is wrong**. Valid is not enough: the audience must be you

</details>

**2. You filter tool output with a keyword blocklist. Does that stop prompt injection?**

- A. Yes, if it blocks the word ignore
- B. No, paraphrases and translations slip past
- C. Yes, if the list is long enough

<details><summary>Answer</summary>

**B. No, paraphrases and translations slip past**. Blocklists are one weak layer, never the defence

</details>

**3. How should your MCP server know which user is calling?**

- A. From the validated token or launch environment
- B. From a user ID in the arguments
- C. By checking the model's intent

<details><summary>Answer</summary>

**A. From the validated token or launch environment**. Identity comes from the token or environment

</details>

## Say it in the interview

**Audience binding, in your words**

- Optional, but every remote server gets it
- The token must be issued for my server
- No passthrough: own scoped token downstream

**Untrusted data, in your words**

- Instructions and data are one token stream
- Authorization lives outside the model
- Worst case: a request a human must sign

**Building a server, in your words**

- The docstring is a prompt; I write it like one
- Inspector first, then a real host
- Remote means a normal, hardened web service

## Homework

- [ ] Add a scope check to the lab
- [ ] Write the five token checks from memory
- [ ] Write one tool docstring like a prompt
- [ ] List three actions that need a human
