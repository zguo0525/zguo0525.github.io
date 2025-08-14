---
layout: default
title: "Siri’s AI Makeover: The Real Reason Apple Delayed — and 3 Rules to Ship AI That Works"
description: "Demos dazzle; delivery is hard. The notification summaries canary shows why integration, org alignment, and privacy constraints decide who wins."
date: 2025-07-01
tags: [Apple Intelligence, Siri, AI, product, privacy, LLM, on-device, ChatGPT, OpenAI, growth]
---

When I saw the new Siri on stage during WWDC 2024, I knew the hard work was ahead. The demo dazzled; delivery was harder. As [The Information](https://www.theinformation.com/articles/apple-fumbled-siris-ai-makeover) noted, the problems were real. The core lesson: in AI, the teams that wire the product end‑to‑end and run fast learning loops beat teams with bigger raw models but slower integration.

What I mean by terms in this essay:

- **Integration**: End‑to‑end product fit—data access (with consent), privacy boundaries, latency budgets, UI, recovery states, and eval/telemetry wiring.
- **Org design**: Clear ownership and decision rights, shared metrics, and a weekly cadence across Siri, platform, and privacy teams.
- **Model size**: Raw capability (e.g., parameters/benchmarks). It matters, but without integration and clear ownership, it doesn’t translate into reliable features.

### Key Takeaways

- **What failed (symptoms)**: Summaries misread tone and sarcasm, dropped key details in group chats, and varied run‑to‑run.
- **Why it failed (causes)**: On‑device privacy limited long‑term context; token budgets forced aggressive trimming; ownership was split, so evals and fixes didn’t ship weekly.
- **Who got it right**: ChatGPT made the model the product, launched fast (no waitlist, free), and turned research into durable features (search, memory, voice)—reaching ~700M WAUs by Aug 2025 ([CNBC](https://www.cnbc.com/2025/08/04/openai-chatgpt-700-million-users.html)).
- **Implication**: Speed of integration and a single owner convert model capability into user trust. Privacy must shape scope up front; it can’t be bolted on.
- **Action**: Pick one use case and one constraint (e.g., on‑device only). Define tone/recall evals. Ship weekly. Expand only when trust metrics improve.

Pricing context: ChatGPT normalized $20/month for Plus and introduced a $200/month Pro tier for heavier use ([TechCrunch](https://techcrunch.com/2025/02/25/how-much-does-chatgpt-cost-everything-you-need-to-know-about-openais-pricing-plans/)).

## The Anatomy of an AI Challenge

Siri’s headline features got the buzz, but notification summaries taught the lesson. A feature meant to condense alerts became a case study in AI limits—tone, context, and constraints.

Consider a family group chat full of inside jokes. A good summary needs recent history, who‑said‑what, and the social tone. If signals remain on device and aren’t retained, the model must infer from a short window. Add small token budgets and strict latency, and you get truncation, flat tone, and missed nuance—even with a strong base model. Without weekly evals and updates, those errors persist.

External reviews echoed this: summaries were inconsistent—tonally off, bad with sarcasm, prone to context loss, and sometimes just wrong (see: [Ars Technica](https://arstechnica.com/apple/2024/11/apple-intelligence-notification-summaries-are-honestly-pretty-bad/)). Apple paused some categories, then re‑introduced with disclaimers and per‑app controls—evidence that the binding constraint was context and iteration, not a missing billion parameters.

Inside, strategy swung between “Mini Mouse” (small, on‑device) and “Mighty Mouse” (large, cloud). Leaders later favored one big model—more cloud, more privacy tradeoffs—and churn slowed delivery.

## The Human Element

The larger blocker was organizational. Software’s default was “ship”; AI’s was “explore.” Incentives, rhythms, and ownership clashed. Federighi’s “Intelligent Systems” team trained models and shipped demos, sometimes bypassing Siri—fueling turf. On Vision Pro, “Link” cut scope when Siri couldn’t meet quality and speed.

This matters because AI quality depends on closed loops: data → evals → model tweaks → shipped behavior → new data. Split ownership breaks that loop. The result: “hot demo” energy, “cold delivery” reality.

## What This Means for AI

The next wave of AI will be won by integration, not leaderboard deltas. Starting from scratch (ChatGPT) is one path; Apple’s harder path is upgrading Siri for a billion people without breakage. Software prototyped fast; AI moved cautiously. Apple first barred third‑party models, then partnered with OpenAI so Siri could hand off. Even demos stretched norms: some 2024 features weren’t reliable internally yet.

Two clear implications:

- If your product promises “context and tone,” you must either (a) gather signals and iterate weekly, or (b) narrow the problem and lock evals to what on‑device can support.
- Privacy is a design variable. Treat it as a first‑class constraint and scope accordingly. Otherwise, you ship broad promises with narrow behavior.

## What ChatGPT Got Right (and Why It Matters)

ChatGPT’s trajectory offers a clear playbook:

- **Model = product**: Iterate the model like software. Start open, watch what users actually do (writing, coding, advice), and improve those journeys. Treat “evals” as product work—clear success criteria for tone, helpfulness, and safety.
- **Ship to learn**: Launch fast (days, not quarters). Rough edges are data. No waitlist; free and simple UI lower the barrier and reveal real demand.
- **Growth flywheel**:
  - Research‑driven capabilities (search/browse, memory, voice) unlock new jobs‑to‑be‑done.
  - Focused upgrades to the top use cases discovered in the wild.
  - Classic levers (no‑login try, simple onboarding) once infra allows.
- **Pricing as throttle**: $20 normalized consumer AI; higher tiers serve power users. Price from value testing, not doctrine.
- **Natural language ≠ chat**: NL persists; chat is just one UX. Let AI render purpose‑built interfaces and take action. The destination is “your AI” that knows goals, with visible control.

Why it matters for Siri: Apple optimizes for privacy, stability, and platform coherence; OpenAI optimizes for speed, breadth, and model iteration. Both are valid. But when features like notification summaries depend on long‑tail context and vibe, you either (a) collect signals and iterate quickly, or (b) narrow scope and tighten evals/on‑device constraints. The middle—broad scope with heavy constraints—tends to underdeliver.

## A practical playbook for AI inside a mature product

1) Define one user problem and one constraint (e.g., on‑device only). Write crisp success criteria and failure examples.
2) Build a tiny, trustworthy slice. Keep input/output predictable. Add an obvious “undo.”
3) Instrument trust: tone errors, latency, task completion, user corrections. Review weekly.
4) Create evals that mirror the live distribution (tone, sarcasm, group chat). Update evals as behavior drifts.
5) Iterate model and product together. Ship small, frequent improvements. Avoid “big bangs.”
6) Expand scope only when trust metrics rise and regressions are rare. Prefer per‑app rollouts to global switches.
7) Let privacy shape the product: on‑device by default; escalate to cloud with consent and visible controls.

## 3 Rules to Ship AI That Works

Three takeaways:

**First, simple‑looking AI is hardest.** Start narrow. Add guardrails. Measure trust. Summarization and tone look simple but hide long‑tail context. Win small before you go broad.

**Second, organizational design is product design.** Pick an owner. Unify roadmaps. Share metrics. AI needs tight loops; split incentives guarantee slow learning.

**Third, privacy is an engineering constraint.** Design on‑device first; escalate to cloud with consent. If privacy limits context, reduce scope or raise iteration speed—don’t promise both.

Building AI into a mature product? Choose a user problem, a constraint, and an owner—then ship small, trustworthy wins. Integration beats ambition.

---

*These are my own views, not Apple’s. I’m grateful for my time in the AIML Residency and the chance to work with exceptional engineers.*

Liked this? Follow on X: [@Zhen4good](https://x.com/Zhen4good). Collaborations/advising: [zguo0525@mit.edu](mailto:zguo0525@mit.edu) • [LinkedIn](https://www.linkedin.com/in/gavin-guo-b764b6b4/)
