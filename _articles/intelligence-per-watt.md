---
layout: default
title: "Nobody Got Rich Owning the Grid"
image: /assets/cards/intelligence-per-watt.png
description: "When the headline metric becomes output per joule, a technology has become a utility. Intelligence just did, and the money will go where it always goes: upstairs."
date: 2026-07-14
tags: [AI, Strategy]
---
Watch what the frontier labs brag about now. Two years ago every launch led with a benchmark table; this year's lead with a price.

The old launches were MMLU, GPQA, SWE-bench — bar charts with your model in a slightly darker color, two points ahead of the competition. The launches of 2026 lead with price per million tokens, latency, efficiency curves. And since inference cost is mostly electricity plus depreciation, tokens per dollar is really tokens per joule.

Nobody announced the change, but the scoreboard is different, and it has a name: the **Pareto frontier**. The race is no longer *how smart*. It's *how smart per dollar*, and since the dollar is mostly electricity plus depreciation, *how smart per watt*.

That shift is worth staring at, because an industry only changes its headline metric when it has changed what it is.

---

Electricity did this first. The 1880s were pure spectacle — arc lamps, world's fairs, Edison electrocuting an elephant to frighten people about alternating current. Then the spectacle wore off and electricity became cents per kilowatt-hour.

Chips did it a century later. The 1990s were the megahertz wars: raw clock speed printed on the box, bigger number wins. Then mobile arrived, batteries became the constraint, and the metric that mattered became performance per watt. Nobody puts clock speed on a billboard anymore.

Here is the rule hiding in both stories: when a technology's defining metric becomes **output per unit of energy**, the technology is confessing what it has become. An input. A commodity. A utility. Not a marvel anymore — an ingredient, priced like one.

Intelligence just made that confession.

---

## The frontier is the confession

Here is what that scoreboard looks like. [Artificial Analysis](https://x.com/ArtificialAnlys/status/2080384902571139386) plots every model by intelligence and cost per task, and defines the Pareto frontier as the models that no other model beats on both. In its words, everything else is paying more for less.

Read one of its recent posts as a price list. Anthropic's Fable 5 led the index at 60, at $2.75 a task. xAI's Grok 4.5 scored 54 at $0.31, about 9x cheaper, and also sat on the line. DeepSeek V4 Flash scored 44 at $0.04, about 69x cheaper than Fable. Six points of intelligence cost nine times as much. That is a price curve, not a leaderboard, and a price curve is what a utility has.

Three things about the frontier make it the heart of this argument, not an illustration of it.

**It moves down fast.** Arena.ai [reported](https://x.com/arena/status/2057486887938646370) that GPT-4-level quality now costs roughly 500x less than in 2023, about $50 per million tokens then and about $0.10 now. It also found that models under $0.20 per million tokens trailed the leader by about 350 Arena points in 2023 and about 60 today. The cheap end didn't just get cheaper. It caught up.

**Nobody owns a place on it.** One [June snapshot](https://artificialcuriositylabs.ai/posts/pareto-frontier-is-the-model-market-map/) of Artificial Analysis data found 13 of 351 priced models on the frontier. Alibaba held five slots, Xiaomi three, Google two, Anthropic one and OpenAI none. A week earlier the line had 15 models. A single 64% price cut by one lab pushed a rival off it. A position that can be taken away by a price cut isn't a position. It's a rental.

**Everything off the line is dead weight.** About 96% of priced models in that snapshot were beaten by something cheaper and at least as smart. In a market with a frontier, being second-best at the same price is the same as not existing.

This is the mechanism behind the rule above. The frontier is where a commodity market becomes visible: one axis of quality, one axis of cost, and a line that every competitor is pushed toward.

---

Why now? Because the labs did this to themselves, and they had no choice.

Capability leads that used to last a year now last a quarter, and the frontier above shows it: the same line, redrawn every few weeks by different labs. Every trick discovered at the frontier leaks downmarket within months — distilled, open-weighted, replicated. The price of a fixed unit of intelligence has been collapsing roughly ten-fold a year, not because anyone wanted it to, but because five labs are competing like hell and none of them can afford to stop. When your product is interchangeable with your rival's, and your rival's marginal cost is the same electrons through the same silicon, price doesn't drift toward value. It falls toward cost. That isn't a strategic failure. It's what competition does to anything that can be measured.

And intelligence, as the industry defines it, can be measured. That's the trap. Anything with a benchmark can be matched; anything that can be matched gets competed down to cost. The benchmark culture the labs built to prove their superiority is the same machinery that guarantees the superiority is temporary.

So the labs are pouring hundreds of billions of dollars a year into building what is, structurally, a grid.

And the thing about grids: nobody got rich owning one. Electric utilities keep civilization alive and pay out like bonds. The grid electrified everything and enriched almost no one who built it.

---

So where did electricity's fortunes go?

Radio. Hollywood. Refrigerators sold as status objects. Neon Times Square. Amusement parks strung with light bulbs. The money went to the people who took a cheap, abundant, boring input and turned it into something people *wanted* — which turned out to be mostly entertainment, comfort, and glamour. The frivolous layer, built on top of the serious one, captured nearly all the margin.

Telecom ran the same script a century later. Carriers spent fortunes on fiber and spectrum and became dumb pipes. Netflix, YouTube, TikTok, mobile games — the trivial things riding the pipes — took the value. The pipe delivers bits at cost. The show on top charges whatever attention will bear.

It offends the engineer in me, but the pattern doesn't care. The layer that touches human desire keeps the margin. The layer that delivers the electrons earns cost plus a thank-you.

---

The instinct is to resist this because it sounds unserious. Surely a trillion dollars of intelligence infrastructure pays for itself in cured diseases, written code, automated enterprises — utility in the noble sense.

Some of it will. But notice how each layer gets priced.

Usefulness saturates. A model that files your taxes correctly is worth exactly the price of the *cheapest* competent model that files your taxes correctly — and there is always a cheaper competent one next quarter. Correct is correct. Utility has a spec, the spec has a benchmark, and we already know what happens to things with benchmarks.

Delight doesn't saturate, because it was never graded against a spec, and it doesn't appear on the frontier chart at all. The chart has two axes, and both are things you can measure. What people actually come back for lives off the chart. It's graded against your attention. The image of you and your friends rendered before you finish describing it. The companion that remembers what you said at 1 a.m. The character, the game, the feed. There is no eval for wanting more. You can watch the revealed preference in real time: companionship apps out-earn productivity assistants, image generation ships inside social feeds rather than office suites, and the labs that swore they were building scientists keep shipping entertainment. Nobody is confused about which way the demand curve slopes. The superficial layer isn't a distraction from the business. It *is* the business — as it was for electricity, as it was for bandwidth.

---

Two honest objections. The first is about the frontier itself. It prices tokens, but people live with results. A cheap model that thinks longer, retries more, or needs more human correction can be [cheap on the price page and expensive in the workflow](https://x.com/ollobrains/status/2072141362435408301), and the snapshot above leaves out coding quality, reliability and latency. I think that makes the frontier a rough map, not a false one. The slope is still steep, and it is still falling.

The second is winner-take-all: some lab crosses into recursive self-improvement, capability stays scarce, the grid owner becomes the everything-company, and none of this history applies.

Maybe. But every visible dynamic points the other way. Leads compress. Distillation leaks. And the binding constraint at the frontier is energy — the same electrons, the same physics, available to every competitor at the same price per joule. Intelligence per watt converges *because* physics is shared. Permanent scarcity of intelligence is a bet against everything currently observable, made mostly by people who need it to be true.

---

So: the datacenters are the grid. Necessary, colossal, and headed for utility returns. The scarce things are the ones capex can't buy — distribution, attention, taste. The labs know it. That is why every one of them is scrambling to become a consumer company before intelligence finishes commoditizing underneath them.

Intelligence will be sold by the joule. Joy will be sold at whatever the market will bear.

---

*zguo0525@berkeley.edu · [@Zhen4good](https://x.com/Zhen4good)*
