---
layout: default
title: "What I Learned During the Siri Makeover"
description: "Demos wow; shipping is harder. Notification summaries show how integration, org design, and privacy limits decide who wins."
date: 2025-07-01
tags: [Apple Intelligence, Siri, AI, product, privacy, LLM, on-device, ChatGPT, OpenAI, growth]
---

# What I Learned During the Siri Makeover

At WWDC 2024, Apple unveiled a flashier Siri, and the demo dazzled—yet the hard work started afterward: turning a staged moment into reliable, everyday behavior. As [The Information](https://www.theinformation.com/articles/apple-fumbled-siris-ai-makeover) reported, the problems were real. The simple lesson is that, in AI, teams that connect the product end to end and learn quickly outperform teams with bigger raw models but slower integration.

What I mean by a few terms, stated clearly:

- **Integration**: How the whole product fits together across data access (with consent), privacy limits, latency (time to respond), the user interface, recovery states when things go wrong, and the evaluations and telemetry (metrics and logs) that tell us what to fix.
- **Org design**: Clear owners with decision rights, shared metrics, and a weekly working rhythm across Siri, platform, and privacy teams.
- **Model size**: The model’s raw capability (for example, number of parameters and benchmark scores). Size helps, but without integration and clear ownership, it does not turn into reliable features.

### Key Takeaways

- **What failed**: Summaries often misread tone and sarcasm, missed key details in group chats, and gave different results on separate runs.
- **Why**: On‑device privacy limited long‑term context; small token budgets (limited input length) forced aggressive trimming; split ownership slowed evaluations and fixes from shipping weekly.
- **Who got it right**: ChatGPT made the model the product, shipped fast (no waitlist, free), and turned research into durable features (search, memory, voice)—reaching about 700 million weekly active users (WAUs) by August 2025 ([CNBC](https://www.cnbc.com/2025/08/04/openai-chatgpt-700-million-users.html)).
- **Implication**: Speed of integration and a single accountable owner convert capability into user trust. Privacy must shape scope up front.
- **Action**: Pick one use case and one constraint (for example, on‑device only). Define tone and recall evaluations. Ship weekly. Expand only when trust improves.

Pricing note: ChatGPT normalized a $20 per month Plus plan and introduced a $200 per month Pro tier for heavier use ([TechCrunch](https://techcrunch.com/2025/02/25/how-much-does-chatgpt-cost-everything-you-need-to-know-about-openais-pricing-plans/)).

## The Anatomy of an AI Challenge

Siri’s big demos got the buzz, but notification summaries delivered the deeper lesson. A feature meant to condense alerts exposed the hard problems that matter in practice: tone, context, and constraints.

Think about a family group chat full of inside jokes. A useful summary needs recent history, who said what, and the social tone. When signals stay on device and are not retained, the model sees only a short window. Layer on tight token budgets (limited input length) and strict latency budgets (limited time to respond), and truncation, flat tone, and missed nuance become common—even with a strong base model. Without weekly evaluations and updates, these errors persist.

Independent reviews backed this up: summaries were inconsistent—off on tone, weak with sarcasm, prone to context loss, and sometimes simply wrong (see [Ars Technica](https://arstechnica.com/apple/2024/11/apple-intelligence-notification-summaries-are-honestly-pretty-bad/)). Apple paused some categories, then re‑introduced them with disclaimers and per‑app controls. The true constraint was context and iteration speed (how quickly teams can test and fix issues), not a missing billion parameters.

Internally, strategy swung between “Mini Mouse” (small, on‑device) and “Mighty Mouse” (large, cloud). Leaders later favored one big model—more cloud and more privacy tradeoffs—and delivery slowed.

## The Human Element

The bigger blocker was organizational: software’s default was “ship,” while AI’s default was “explore.” Incentives, working rhythms, and ownership clashed. Federighi’s “Intelligent Systems” team trained models and shipped demos, sometimes bypassing Siri—fueling turf tensions. On Vision Pro, “Link” reduced scope when Siri could not meet the needed quality and speed. AI quality depends on a closed loop—data → evaluations → model tweaks → shipped behavior → new data—and split ownership breaks that loop. The result is predictable: hot demos, cold delivery.

## What This Means for AI

The next wave will be won by integration rather than leaderboard scores. One path is to start from scratch (as ChatGPT did). Apple chose the harder path: upgrading Siri for a billion people without breakage. Software teams prototyped fast while AI teams moved more cautiously. Apple first barred third‑party models, then partnered with OpenAI so Siri could hand off requests.

Two implications:

- If you promise “context and tone,” either (a) gather the signals you need and iterate weekly, or (b) narrow the problem and lock evaluations to what on‑device systems can actually support.
- Privacy is a design variable. Treat it as a first‑class constraint and scope accordingly. Otherwise, you will make broad promises but deliver narrow behavior.

## What ChatGPT Got Right (and Why It Matters)

Here is ChatGPT’s playbook, in plain terms:

- **Model = product**: Improve the model the way we improve software. Watch how people actually use it (writing, coding, advice) and optimize those journeys. Treat evaluations as core product work with clear success criteria for tone, helpfulness, and safety.
- **Ship to learn**: Launch quickly. Rough edges produce the data you need. No waitlist, and a free, simple user interface lowers the barrier and reveals real demand.
- **Growth flywheel**:
  - Research‑driven capabilities (search/browse, memory, voice) unlock new jobs to be done.
  - Focus upgrades on the most common and valuable use cases you observe in the wild.
  - Add classic growth levers (no‑login try, simple onboarding) once infrastructure can handle the load.
- **Pricing as throttle**: $20 set consumer norms; higher tiers serve power users. Set price points based on value testing, not doctrine.
- **Natural language ≠ chat**: Natural language interfaces will persist, but chat is only one user experience. Let AI render purpose‑built interfaces and take action when appropriate. The destination is “your AI” that knows your goals, with visible controls.

Why this matters for Siri: Apple optimizes for privacy, stability, and platform fit. OpenAI optimizes for speed, breadth, and model iteration. Both are valid. But if a feature depends on long‑tail context and social tone, you must either (a) collect the needed signals and iterate quickly, or (b) narrow the scope and tighten evaluations and on‑device limits. The middle—broad scope with heavy limits—tends to underdeliver.

## A practical playbook for AI inside a mature product

- 1) Pick one user problem and one constraint (e.g., on‑device only). Write crisp success and failure examples.
- 2) Build a tiny, trustworthy slice. Keep input and output predictable. Add an obvious “undo.”
- 3) Instrument trust: tone errors, latency, task completion, user corrections. Review weekly.
- 4) Create evals that match the live distribution (tone, sarcasm, group chat). Update as behavior drifts.
- 5) Iterate model and product together. Ship small, frequent improvements. Avoid big‑bang releases.
- 6) Expand scope only when trust rises and regressions are rare. Prefer per‑app rollouts to global switches.
- 7) Let privacy shape the product: on‑device by default; escalate to cloud with consent and visible controls.

---

*These are my own views, not Apple’s. I’m grateful for my time in the AIML Residency and the chance to work with exceptional engineers.*

Liked this? Follow on X: [@Zhen4good](https://x.com/Zhen4good). Collaborations/advising: [zguo0525@mit.edu](mailto:zguo0525@mit.edu) • [LinkedIn](https://www.linkedin.com/in/gavin-guo-b764b6b4/)
