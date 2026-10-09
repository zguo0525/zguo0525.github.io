---
layout: default
title: "Real-Time Video Is a Control Problem"
image: /assets/cards/real-time-video-is-a-control-problem.png
description: "A clip model is judged on a finished video. A real-time model is judged mid-conversation, on inputs it helped cause. That makes it a policy, not just a generator."
date: 2026-09-27
tags: [AI]
---
Making a video model fast enough to run live is hard. For [Muse Realtime Avatar](https://research.meta.ai/blog/bringing-your-muse-to-life), we went from 120 model evaluations per chunk to 2, and now serve 12 live sessions on a single GB200.

Once it was fast, a different problem showed up. Speed got us in the door. It didn't tell us whether the avatar was good to talk to.

A clip model makes a finished video. Nobody reacts while it's being made, so nothing it generates changes what it has to generate next.

A real-time model is in the middle of a conversation. Every frame lands in front of a person, and the person reacts: they keep talking, pause, interrupt, or repeat themselves. That reaction is the model's next input. Its outputs shape its own future inputs.

That makes it a control problem. The model is a policy, and the user is part of the environment.

Three things follow.

**Evaluation has to be live.** A clip is judged on its best take. A conversation is judged on its worst moment, a frozen face or a drifting identity, on inputs no fixed test set contains. Offline metrics still catch regressions, but only live sessions tell you whether it works. That's why we evaluated Muse with people holding 2–3 minute conversations, not with frame scores.

**Training data is off-policy.** Video models are trained on recorded clips nobody reacted to. Self-forcing helps: training on the model's own rollouts closes the loop on its own frames. It doesn't close the loop on the person watching them.

**The missing signal is the user's reaction.** A live session is full of feedback on what the model just did: interruptions, pauses, repeated questions. Today almost none of it becomes training signal.

Fewer steps made real-time video possible. I think the next gains come from training inside the loop, where what people do in response to the model becomes the reward.

---

*First posted [on X](https://x.com/zhen4good/status/2104252038184091834). Views my own. · zguo0525@berkeley.edu · [@Zhen4good](https://x.com/Zhen4good)*
