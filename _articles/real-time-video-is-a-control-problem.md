---
layout: default
title: "Start From the Person on the Other Side"
image: /assets/cards/real-time-video-is-a-control-problem.png
description: "A live avatar isn't worth building because a model can now do it. It's worth building if talking to it feels better. That changes what you train for."
date: 2026-09-27
tags: [AI]
---
Most model work starts from the model: a new architecture, a better benchmark, a bigger number. Then someone looks for a product to put it in.

Working on [Muse Realtime Avatar](https://research.meta.ai/blog/bringing-your-muse-to-life) taught me to go the other way. Start from the person on the other side of the screen, and ask what would make the conversation better for them.

**Why a face at all.** People don't talk to voices the way they talk to faces. A face tells you you're being heard: a nod while you're still talking, a pause that looks like thinking, an expression that matches the words. A voice assistant can be smart and still feel like a machine on the other end of a phone line. The reason to build a live avatar isn't that video models can finally do it. It's that presence changes how a conversation feels.

**Users don't notice what benchmarks measure.** Nobody in a conversation notices a frame score. They notice when the reply is slow, when the face freezes, when it stops looking like the same person, when it talks over them. These are small moments, and one bad one can break the whole conversation. A model can get better on every benchmark and still feel worse to talk to.

**So define quality from the user's side.** For Muse, that meant judging it the way a user would: people held real two-to-three-minute conversations and told us which avatar they'd rather talk to. Not single clips, not best takes. The question was always: would you rather keep talking to this one?

**Then let that drive the training.** Once the target is the experience, the technical choices follow from it. Speed isn't a record to set. It matters because people feel every pause, and a slow reply feels like nobody's there. Training data should look like real conversations, not a showcase reel. And when the model gets stronger but the conversation doesn't get better, that isn't progress.

**The best signal is the user.** Every live conversation is full of feedback: people lean in, interrupt, repeat themselves, or go quiet. Today most of it is thrown away. The models that feel best to use will be the ones trained on what people actually do with them.

Better models matter. But a model is only as good as the experience someone has with it. Build for that person first.

---

*First posted [on X](https://x.com/zhen4good/status/2104252038184091834). Views my own. · zguo0525@berkeley.edu · [@Zhen4good](https://x.com/Zhen4good)*
