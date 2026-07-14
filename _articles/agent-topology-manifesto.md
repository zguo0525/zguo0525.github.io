---
layout: default
title: "Agent Topology Follows Task, Not Template"
description: "Hierarchical multi-agent systems import human coordination constraints into a substrate that doesn't have them. The evidence, the mechanism, and the alternative."
date: 2026-04-19
tags: [AI, LLM, multi-agent, architecture, topology]
---

# Agent Topology Follows Task, Not Template

*April 2026*

Everyone is building org-chart agents.

Planner → Executor → Critic. Manager → Worker → Validator. Trees of LLMs wired into patterns that look suspiciously like the company structure on a whiteboard.

It feels right because it mirrors how *we* organize. But humans invented hierarchy to compensate for being human: slow sequential thinking, limited bandwidth, memory that doesn't transfer between heads. Machines have none of these constraints, so when you wire LLMs into a fixed hierarchy you aren't solving a coordination problem—you're importing one.

I've been watching the 2025–2026 papers converge on the same conclusion from different angles. The pattern is hard to miss once you see it.

---

## The evidence

The empirical record keeps saying the same thing.

[MacNet (ICLR 2025)](https://arxiv.org/abs/2406.07155) scaled to a thousand agents and found irregular topologies beat regular ones—chains, stars, trees plateaued early. [Kim et al. (2025)](https://arxiv.org/abs/2512.08296) measured **17× error amplification** in uncoordinated groups, with performance swinging ±80% on architecture alone.

[Graph of Thoughts (AAAI 2024)](https://arxiv.org/abs/2308.09687) delivered **62% quality improvement** over Tree of Thoughts at **31% lower cost**. [Shen et al. (EMNLP 2025)](https://arxiv.org/abs/2505.23352) showed query-adaptive topologies hitting **91.38%** on MMLU and GSM8K, beating every fixed shape.

Even the field's trajectory—Chain of Thought → Tree of Thoughts → Graph of Thoughts—points the same way. The next step isn't another fixed structure. It's **no fixed structure at all**.

---

## The shift

Here's the move: topology stops being input. It becomes output.

Static systems hardcode human assumptions about how agents should interact; dynamic systems let the task dictate the shape. A cheap LLM call—$0.001, 200ms—reads the problem and emits the graph: which models to call, in what order, with what parallelism, with back-edges where needed.

```python
# Human designs topology
topology = org_chart(human_team)
result = topology.execute(task)

# Model designs topology  
topology = llm("emit graph for this task", task, available_agents)
result = topology.execute()
```

Sometimes the model emits a chain (data pipeline). Sometimes parallel fan-out (brainstorm). Sometimes a loop with back-edges (design → code → critique → redesign). Sometimes a hierarchy—but because the task demands it, not because your framework ships it as a default.

The topology is not architecture. It's **output**—chosen from a design space you define, not infinite chaos.

---

## The design surface

Dynamic topology doesn't eliminate design. It moves it one level up.

You still design the **agent pool**—heterogeneous beats homogeneous, with [X-MAS (2025)](https://arxiv.org/abs/2505.16997) reporting +47% on AIME by mixing reasoners and chatbots instead of stacking identical models. You still design the **edge vocabulary**: what can flow between nodes, what kinds of back-edges are allowed, whether agents share state or only messages. You still design the **density default**—moderate sparsity with small-world structure (local clustering plus a few long-range shortcuts) is the strongest known inductive bias across [Shen et al.](https://arxiv.org/abs/2505.23352) and [Wang et al.](https://arxiv.org/abs/2512.18094). And you still design the **objective and constraints**: whether the solver optimizes cost, latency, quality, or consistency, and what bounds it must respect—max depth, max cost per query, safety rules.

What's still open: the right task-to-objective mapping, when to regenerate the graph versus reuse a cached one, whether topology should change within a single execution, how dynamic graphs degrade under adversarial agents, and what the theoretical frame is for scaling. The research is early. Treat the rules above as starting defaults, not a finished system.

This is more work than hardcoding a pipeline—much more—but the schlep is where the advantage is. Everyone else is wiring graphs by hand because the alternative is harder.

Compiler writers don't write machine code—they design the rules that generate it. Agent builders should do the same, and be honest about which rules we don't yet have.

---

Static agent topologies are training wheels for a bicycle that doesn't need them.

The best agent system is not the one with the cleanest org chart. It is the one you cannot draw—because it vanishes into the problem it solves.

Stop wiring. Start compiling.

---

*If you're building agent compilers: zguo0525@berkeley.edu · [@Zhen4good](https://x.com/Zhen4good)*
