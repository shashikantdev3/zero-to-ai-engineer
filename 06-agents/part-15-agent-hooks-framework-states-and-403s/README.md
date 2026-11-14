# Agents and Tools · Part 15 of 26: Agent Hooks, Framework States, and 403s

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Agent Framework middleware, checkpointing and request_info
2. Semantic Kernel, AutoGen and AG2: different states
3. Foundry data-plane roles: the 403 rule

## Key takeaways

- Three hooks. Approval bound to the exact plan.
- New work on Agent Framework. Verify releases.
- Owner is control plane. Assign data-plane roles.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_an_audit_middleware_simulated.py` | An audit middleware, simulated | yes |
| `code/02_check_the_release_pages_yourself.py` | Check the release pages yourself | yes |
| `code/03_the_data_plane_role_checklist.py` | The data-plane role checklist | yes |
| `code/04_lab_simulate_the_403_rule.py` | Simulate the 403 rule | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_simulate_the_403_rule.py` prints:

```text
Owner: 403, no data role
Keys only: denied, keys only
RBAC on: 200 OK
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. request_info returns 'approved'. What should the executor do next?**

- A. Execute at once, the human approved
- B. Rerun the whole workflow from scratch
- C. Verify approval matches the exact plan

<details><summary>Answer</summary>

**C. Verify approval matches the exact plan**. An approval is valid only for the exact plan.

</details>

**2. A candidate says 'Semantic Kernel is deprecated.' What is the best correction?**

- A. AG2 replaced it as Microsoft's product
- B. It still releases, on a successor path
- C. Correct, it went into maintenance

<details><summary>Answer</summary>

**B. It still releases, on a successor path**. Successor path is not deprecation.

</details>

**3. Your agent gets 403 from AI Search in Azure. A teammate grants Owner. What happens?**

- A. Still forbidden, Owner is control plane
- B. It works after a few minutes
- C. It works, Owner includes everything

<details><summary>Answer</summary>

**A. Still forbidden, Owner is control plane**. Owner is control plane. Data needs data-plane roles.

</details>

## Say it in the interview

**Say it in the interview**

- Policy around every call, not sprinkled through agents.
- A failure costs a step, not the run.
- Idempotency keys. Approval checked against the plan.

**Say it in the interview**

- AutoGen went quiet. Semantic Kernel kept shipping.
- New work on Agent Framework. Migrate calmly.
- Check release pages on the day.

**Say it in the interview**

- Laptop works, Azure 403: missing data-plane role.
- Enable role-based access first, then assign roles.
- Wait for propagation. Roles live in infrastructure code.

## Homework

- [ ] Run the middleware sketch, add one rule
- [ ] Check three packages' release history
- [ ] Add a second service to the lab
- [ ] Write your 403 answer in three sentences
