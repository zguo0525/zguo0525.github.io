---
layout: default
title: "The Purpose Model"
image: /assets/cards/purpose-model.png
description: "When execution gets cheap, direction gets expensive. Why long-horizon agents need a purpose model, and how you would evaluate one."
date: 2026-10-19
tags: [AI]
---
After AGI, the scarce thing won't be intelligence. It will be purpose.

Models will keep getting more capable. Writing code, reading papers, running experiments, shipping products, operating processes: all of it keeps getting cheaper. But capability doesn't answer a harder question. What is worth doing?

---

## Prompts make human attention the clock

Today's AI is mostly prompt-driven. A person asks, the model answers. A person instructs, the model executes.

The trouble is that this makes human attention the system's clock. Every step needs someone to start it, judge it and correct it. That works for short tasks. It breaks on long ones.

What makes a long-horizon task hard isn't that one step is beyond the model. It's that **purpose drifts.** After three days the goal may have changed. After three months, local optima have slowly eaten the original intent. An agent can work very hard on the wrong thing. It can finish every subtask and end up further from the result that mattered.

So long-horizon work needs more than a stronger capability model. It needs a purpose model.

---

## Feasibility versus worthiness

Three questions, three kinds of model:

- A **planner** answers: given a goal, how do I get there?
- A **reward model** answers: is this result good?
- A **purpose model** answers the question above both: which goals deserve time, compute and risk? Which tasks should continue and which should stop? Which problems will cost more if I leave them alone now?

Put differently, a capability model optimizes **feasibility**. A purpose model optimizes **worthiness**.

This is also why a prompt isn't enough. A prompt is one sample of human intent, and a sparse, short-lived one. A long task needs something that persists: a standing field of intent. It knows the background and the constraints. It knows what not to touch, what counts as a meaningful result, when to ask a person and when not to bother them.

---

## Where the judgment actually sits

Say you give an agent a month to advance a research program. It can read every paper, run many experiments and write a lot of code. But what decides whether the month was well spent is rarely at the execution layer:

- Which anomaly is noise, and which is a lead?
- Which negative result is a dead end, and which one means we asked the wrong question?
- Which experiment deserves a week of scarce compute?

None of these is purely a capability problem. They are purpose problems.

Companies are the same. A startup never lacks tasks. Every team has a hundred things it could do this week. What's scarce is **ranking, and giving things up**: putting resources behind the few things that compound. People, labs and companies don't finally compete on who is busier. They compete on whose sense of direction holds steadier.

---

## From prompter to principal

Here is what changes after AGI. When execution costs fall, asking questions loses value too. People still matter, but their role shifts. They stop being the prompter on every turn and become more like a **principal**: they set values, boundaries, taste and no-go zones, then audit the results.

The model, in turn, doesn't just wait for questions. It proposes the questions worth working on, keeps hold of the long-term goal, and corrects course when the environment changes.

---

## How you would evaluate it

This needs new evaluation. Task success rate isn't enough. A purpose model should be judged on:

- **Regret.** Did it spend resources on low-value goals?
- **Coherence.** Three months on, is it still pursuing the same important thing?
- **Abandonment quality.** Does it kill goals that have expired, and in time?
- **Opportunity cost.** When it chose A, did it know it was giving up B?

---

## The risk

A capability error means the work isn't done well. A purpose error means the whole system does the wrong thing, very efficiently. A purpose model nobody can question could be more dangerous than a weak model.

So it has to be legible, open to challenge, and under human override. Purpose can't be an ideology locked in a black box. It should be a judgment process that can be audited.

---

I'm not sure purpose can be modeled on its own. It may not be a single model at all. It may be a set of mechanisms: long-term memory, value assessment, authorization boundaries, exit conditions, and simulation of consequences.

But the question has already changed. We used to ask: can the model finish this task?

The question that matters next: if no one asks, what will it choose to do?

---

*zguo0525@berkeley.edu · [@Zhen4good](https://x.com/Zhen4good)*
