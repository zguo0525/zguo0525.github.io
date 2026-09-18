---
layout: default
title: "Prediction log"
description: "Testable predictions extracted from my essays. Dated, specific, falsifiable. Updated as reality resolves them."
subtitle: "Dated, specific, and falsifiable forecasts from my essays."
permalink: /predictions.html
---

Every thesis essay I publish stakes a position on how the world will go. This page records those positions in falsifiable form — specific outcomes, dated resolution windows, and what would prove me wrong.

The point isn't to be right. It's to be **calibrated**: if I'm only right 60% of the time, I want that to be visible. Predictions written down can't be retroactively edited into wins. Predictions remembered can.

I update the **Status** column as evidence comes in. Resolved predictions keep their original text — corrections happen in the Notes column, not by rewriting history.

---

## Status overview

| ID | Essay | Resolve by | Status |
|---|---|---|---|
| P1 | [Agent Topology Follows Task, Not Template](../articles/agent-topology-manifesto.html) | 2029-Q1 | Open |
| P2 | [The $100B Monologue](../articles/the-100b-monologue.html) | 2029-Q1 | Open |
| P3 | [Why AI Has to Create Jobs](../articles/why-ai-has-to-create-jobs-or-fail-spectacularly.html) | 2029-12-31 | Open |
| P4 | [The OpenClaw Playbook](../articles/the-openclaw-playbook.html) | 2027-12-31 | Open |

Status legend: **Open** (waiting), **Right** (resolved correctly), **Wrong** (resolved against), **Partial** (mixed), **Voided** (premise invalidated).

---

## P1 — Agent topology will go dynamic

**Source essay**: [Agent Topology Follows Task, Not Template](../articles/agent-topology-manifesto.html) (April 2026)
**Written**: 2026-04-19
**Resolve by**: 2029-Q1
**Status**: Open

**Prediction.** By end of 2028, at least one major agent framework — LangGraph, AutoGen, or OpenAI's Agents SDK — will ship query-adaptive / dynamic topology as the recommended default execution mode, with fixed Planner → Executor → Critic relegated to a legacy import path.

**Wrong if.** All three of LangGraph, AutoGen, and OpenAI's Agents SDK still recommend static hierarchical topologies as the default execution mode by Q1 2029.

**How I'll check.** Read each framework's official "getting started" tutorial in Q1 2029. Default = whatever appears in the first runnable code example. Dynamic counts if the topology is computed by the framework or an LLM at runtime, not declared by the user.

**Notes.**
- _(none yet)_

---

## P2 — Latent reasoning will displace the visible monologue

**Source essay**: [The $100B Monologue](../articles/the-100b-monologue.html) (February 2026)
**Written**: 2026-02
**Resolve by**: 2029-Q1
**Status**: Open

**Prediction.** By end of 2028, at least one frontier lab — OpenAI, Anthropic, or Google DeepMind — will ship a production reasoning mode that matches or beats its visible-CoT counterpart on hard reasoning benchmarks (AIME, GPQA-Diamond, FrontierMath) while emitting under 30% the thinking tokens, or replaces token-level deliberation with latent-state reasoning entirely.

**Wrong if.** All three frontier labs continue to bill users for thousands of monologue tokens per hard query through Q1 2029, with no production mode at the <30%-tokens or latent-reasoning bar.

**How I'll check.** Compare published model cards / pricing pages in Q1 2029. Token counts visible to API users. Benchmark scores from third-party leaderboards (not vendor-reported only).

**Notes.**
- _(none yet)_

---

## P3 — AI either creates entry-level jobs or forces policy

**Source essay**: [Why AI Has to Create Jobs—or Fail Spectacularly](../articles/why-ai-has-to-create-jobs-or-fail-spectacularly.html) (September 2025)
**Written**: 2025-09-12
**Resolve by**: 2029-12-31
**Status**: Open

**Prediction.** By end of 2029, US labor force participation for 22–26 year-olds will either recover above the 2024 baseline (suggesting AI created replacement entry paths) or trigger explicit federal labor-policy intervention — retraining mandate, automation tax, or expanded UBI pilot. The silent default — AI hollowing out entry-level work with no policy response — will not survive four more years.

**Wrong if.** End of 2029 shows sub-2024 youth (22–26) labor force participation AND no federal AI-labor policy enacted (no automation tax, no federal retraining mandate, no expanded UBI pilot beyond pre-2025 scope).

**How I'll check.** BLS labor force participation series (22–26 age cohort). Cross-reference enacted federal legislation by 2029-12-31.

**Notes.**
- _(none yet)_

---

## P4 — Personal AI gets won by indie / open source, not VC

**Source essay**: [The OpenClaw Playbook](../articles/the-openclaw-playbook.html) (February 2026)
**Written**: 2026-02
**Resolve by**: 2027-12-31
**Status**: Open

**Prediction.** By end of 2027, the most-used personal AI tool in the US (by DAU) will be either open-source community-led (OpenClaw, Ollama-class) or a single-developer indie effort — not a VC-backed personal-AI startup (Pi, Rabbit-class, Humane-class).

**Wrong if.** A venture-funded personal-AI company holds the #1 DAU spot in the US at end of 2027.

**How I'll check.** Sensor Tower / SimilarWeb DAU rankings for personal AI assistant category at end of Q4 2027. "Personal AI" defined as: assistant tools running on consumer device or chat platform, not generic AI chatbots from foundation-model providers (ChatGPT, Claude.ai, Gemini app are out of scope — they're foundation-model UX, not personal-AI products).

**Notes.**
- _(none yet)_

---

{% comment %}
## How to add a new prediction

When publishing a new thesis essay:

1. Stress-test the thesis: write the prediction. If you can't make it specific + dated + falsifiable, the thesis isn't sharp enough.
2. Add an entry below the status table, following the P1–P4 format.
3. Add a row to the status overview.
4. Cross-reference: in the essay itself, you can optionally link `[testable prediction](../predictions.html#pN)` near the conclusion.

## Scorecard cadence

Every 12–18 months, write a scorecard essay that walks through resolved predictions: what was right, what was wrong, what the root cause of each error was. The scorecard essay is the brand vehicle. This log is the raw material.
{% endcomment %}
