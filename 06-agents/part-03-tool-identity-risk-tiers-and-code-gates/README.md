# Agents and Tools · Part 3 of 26: Tool Identity, Risk Tiers, and Code Gates

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Whose identity does the tool run as?
2. Read-only first: tools split by risk
3. The code gate (check the real order)

## Key takeaways

- Delegated by default; never app-only plus a model
- Look free, gate changes, drop destructive tools
- Prompts guide, code enforces

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_build_the_confidential_client.py` | Build the confidential client | after `pip install msal` |
| `code/02_exchange_the_token_on_behalf_of.py` | Exchange the token on behalf of | after `pip install msal` |
| `code/03_allowed_tools_and_real_records.py` | Allowed tools and real records | yes |
| `code/04_the_gate_function.py` | The gate function | yes |
| `code/05_lab_type_a_tiny_code_gate.py` | Type a tiny code gate | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_type_a_tiny_code_gate.py` prints:

```text
reject: not allowed
reject: over limit
ok: send to human
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. An agent reads mail with tenant-wide Mail.Read app permission. What stops an injected email reading the CFO's mailbox?**

- A. Nothing in code, only the prompt
- B. The prompt limits it to the current user
- C. The model refuses suspicious requests

<details><summary>Answer</summary>

**A. Nothing in code, only the prompt**. If the credential allows it, the prompt is not a wall

</details>

**2. Your agent has a delete tool. How do you stop it deleting when a ticket body says to?**

- A. Tell it in the prompt never to delete
- B. Remove the tool and scope the credential
- C. Ask the model to double-check first

<details><summary>Answer</summary>

**B. Remove the tool and scope the credential**. Remove the tool, scope the credential, gate in code

</details>

**3. The model proposed a refund for a tracking request. What is the right fix?**

- A. Send every unchecked call to a human
- B. A stronger instruction in the system prompt
- C. A code gate checking intent and records

<details><summary>Answer</summary>

**C. A code gate checking intent and records**. Gate in code; never send humans unchecked calls

</details>

## Say it in the interview

**Say it in the interview**

- First question: whose identity does it run as?
- Delegated by default; the API enforces permissions
- Never app-only plus a model reading untrusted text

**Say it in the interview**

- Split tools by risk before any prompt
- Look tools run free; change tools are gated
- Not registered means no prompt can call it

**Say it in the interview**

- Confidence is not evidence.
- Check intent, records, and policy limits
- Prompts guide, code enforces.

## Homework

- [ ] Run the lab, add a wrong-user call
- [ ] Tag each tool by its risk tier
- [ ] Write down each tool's identity
- [ ] Practise the three interview answers
