---
layout: default
title: "Siri’s AI Makeover: The Real Reason Apple Delayed — and 3 Rules to Ship AI That Works"
description: "Demos dazzle; delivery is hard. The notification summaries canary shows why integration, org alignment, and privacy constraints decide who wins."
date: 2025-07-01
tags: [Apple Intelligence, Siri, AI, product, privacy, LLM, on-device]
---

When I saw the new Siri on stage, I knew the hard work was ahead. The demo dazzled; delivery was harder. As [The Information](https://www.theinformation.com/articles/apple-fumbled-siris-ai-makeover) noted, the problems were real. The lesson: winners in AI nail product integration and org alignment—not just bigger models.

TL;DR: Apple delayed Siri’s AI because integration and privacy are hard at billion‑user scale. Notification summaries exposed the gap. Here’s what broke—and 3 rules to ship AI that works.

## The Anatomy of an AI Challenge

Siri’s headline features got the buzz, but notification summaries taught the lesson. A feature meant to condense alerts became a case study in AI limits—tone, context, and constraints.

Public examples showed the gap: polite turned blunt; group chats misread. The core tension: AI wants rich cloud context, while privacy pushes on‑device.

External reviews matched this: [Ars Technica](https://arstechnica.com/apple/2024/11/apple-intelligence-notification-summaries-are-honestly-pretty-bad/) found summaries inconsistent—tonally off, bad with sarcasm, prone to context loss/overload, and sometimes just wrong. Others flagged lost nuance in texts ([The Atlantic](https://www.theatlantic.com/technology/archive/2024/11/apple-intelligence-text-messages/680717/)), Apple pausing error‑prone news/entertainment summaries ([AP News](https://apnews.com/article/6b37a11b9cdd0e100c299e922d58b530)), and their return with disclaimers and per‑app controls ([Tom’s Guide](https://www.tomsguide.com/ai/apple-intelligence/apple-intelligence-will-summarize-news-again-in-ios-26-after-false-headline-debacle)).

Inside, strategy swung between “Mini Mouse” (small, on‑device) and “Mighty Mouse” (large, cloud). Leadership later favored one big model—more cloud, more privacy tradeoffs—and churn slowed delivery.

## What Changed Inside Apple

- 2026 delay for most Siri AI features; oversight moved to Craig Federighi, with Mike Rockwell running day‑to‑day.
- Model strategy pivots (Mini/Mighty → single large model) increased cloud reliance and tradeoffs.
- Vision Pro’s “Link” voice ambitions were cut back when Siri couldn’t sustain quality/speed.
- OpenAI partnership let Siri hand off what Apple’s models couldn’t handle yet.

## The Human Element

The bigger issue was organizational. Software’s default was “ship”; AI’s was “explore.” Incentives, rhythms, and ownership clashed. Federighi’s “Intelligent Systems” team trained models and shipped demos, sometimes bypassing Siri—fueling turf. On Vision Pro, “Link” cut scope when Siri couldn’t meet quality/speed.

## What This Means for AI

The next wave of AI will be won by integration, not model metrics. Starting from scratch (ChatGPT) is one path; Apple’s harder one is upgrading Siri for a billion people without breakage. Software prototyped fast; AI moved cautiously. Apple first barred third‑party models, then partnered with OpenAI so Siri could hand off. Even demos stretched norms: some 2024 features weren’t reliable internally yet.

## 3 Rules to Ship AI That Works

Three takeaways:

**First, simple‑looking AI is hardest.** Start narrow, add guardrails, measure trust.

**Second, organizational design is product design.** Pick an owner, unify roadmaps, share metrics.

**Third, privacy is an engineering constraint.** Design on‑device first; escalate to cloud with consent.

Building AI into a mature product? Choose a user problem, a constraint, and an owner—then ship small, trustworthy wins. Integration beats ambition.

---

*These are my own views, not Apple’s. I’m grateful for my time in the AIML Residency and the chance to work with exceptional engineers.*

Liked this? Follow on X: [@Zhen4good](https://x.com/Zhen4good). Collaborations/advising: [zguo0525@mit.edu](mailto:zguo0525@mit.edu) • [LinkedIn](https://www.linkedin.com/in/gavin-guo-b764b6b4/)
