---
layout: default
title: "Real-Time Video Is a Control Problem"
image: /assets/cards/real-time-video-is-a-control-problem.png
description: "A clip model never faces consequences. A real-time model does: any frame can change what the user does next. That makes it a policy, not a generator."
date: 2026-09-27
tags: [AI]
---
Everyone's racing to make video models faster than playback. That's solving the wrong problem. Real-time video isn't a rendering problem. It's a control problem.

We learned that building one: 120 evals down to 2, 12 real-time sessions on a single GB200 ([Muse Realtime Avatar](https://research.meta.ai/blog/bringing-your-muse-to-life)). Speed got us in the door. The hard part came after.

A clip model never faces consequences. Nothing it generates changes what happens next. The whole thing exists before anyone watches.

A real-time model answers to a live user. Any frame can change what the user does next, and that changes what it has to generate. That's not generation anymore. It's a policy, and the user is the environment.

So you can't evaluate it offline. A clip is scored on its best take. A conversation is scored live, on its worst second, on inputs your own model caused.

Yet video models are still trained on recorded clips nobody reacted to. Even self-forcing, which trains on the model's own rollouts, only closes the loop on its own frames, not on the person watching them.

The next leap in video won't come from fewer steps. It'll come from models that learn the consequences of their outputs — trained inside the loop, not on recordings of it.

---

*First posted [on X](https://x.com/zhen4good/status/2104252038184091834). Views my own. · zguo0525@berkeley.edu · [@Zhen4good](https://x.com/Zhen4good)*
