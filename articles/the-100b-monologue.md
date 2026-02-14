# The $100B Monologue

*February 2026*

The AI industry spends over a hundred billion dollars a year making computers talk to themselves.

Not to users. To themselves. The internal monologue — the "thinking" that reasoning models do before answering — is now the majority of all tokens generated on Earth. Thousands of words of self-talk that no human reads, no human asked for, and no human would pay for if they understood what was happening.

The smarter the model, the more it talks to itself. That should strike you as suspicious.

---

Here's how we got here.

Pretraining was hitting diminishing returns. Bigger models, more data, same benchmarks. The industry needed a new story. OpenAI found one: let models think before they answer. Chain of thought. Deliberation. Self-reflection.

It worked. On benchmarks, thinking models crushed everything. So everyone followed. A year later, every major lab ships reasoning models. The meta is clear: think harder, score higher.

But something strange is happening. Ask a reasoning model a hard question and it might generate 5,000 tokens of thinking to produce a 200-token answer. You pay for all 5,200. Only 200 were for you. The rest was the model having a conversation with itself — rehearsing, second-guessing, rephrasing, going in circles.

We built an industry around AI talking to humans. Then we discovered it mostly talks to itself.

---

The obvious defense: "But it makes the answers better!"

Sure. But *why* does it work? Not because thinking is inherently good. Because the architecture has no other option.

A transformer can only carry information forward by generating tokens. Each token updates the hidden state. No token, no state update. The model literally cannot think without speaking. The monologue is not a strategy. It's a prosthesis.

Humans don't have this limitation. When you recognize a friend's face in a crowd, there's no inner monologue. When a chess grandmaster sees the right move, she doesn't narrate the search tree. Most human cognition is silent — patterns firing in neural substrate, not words forming in sequence.

Language is how we *communicate* thoughts. Not how we *produce* them. The AI industry confused the two, and now spends $100 billion a year on the confusion.

---

It gets worse. The returns are collapsing.

Going from zero thinking to some thinking is transformative. Going from some to a lot is incremental. Going from a lot to a massive amount is almost nothing.

This is not a scaling law. Scaling laws are the magic of deep learning — more compute, reliably better results. What we have with thinking tokens is a logarithmic curve pretending to be a power law. The industry is extrapolating a trend that's already flattening, and building infrastructure on the extrapolation.

Ten thousand GPUs generating text that nobody reads. That's not the future of intelligence. That's a very expensive diary.

---

You can see the problem most clearly at the edges.

Voice assistants. If thinking takes 15 seconds, voice is broken. Nobody waits 15 seconds in a conversation. So you either give up on voice, or you give up on thinking. Today, most products give up on voice.

Real-time agents. An agent that takes 30 seconds to decide its next action is not an agent. It's a committee. Reasoning models are too slow for the agentic future everyone is betting on.

Embodied AI. A robot that pauses to monologue before picking up a cup is a robot that drops the cup. Physical interaction happens at the speed of physics, not the speed of text generation.

The monologue is not just expensive. It's a ceiling on what AI can become.

---

Some people think the answer is making the monologue faster. Distillation, speculative decoding, efficient attention. Make the same thinking happen in fewer milliseconds.

This is like making a faster horse. You're optimizing within a paradigm that's the problem.

Others think the answer is making the monologue shorter. Prune redundant reasoning steps. Stop the model when it's confident. Tax verbosity during training.

Better. But still treating symptoms. You're still paying the thinking tax — just a smaller one.

The real question is: **why does thinking need to happen in language at all?**

---

It doesn't. And we already know this.

A few research groups have shown that you can achieve equivalent reasoning performance in the model's hidden states — continuous vectors, not discrete tokens. No monologue. No text. Just computation happening in the space where the model actually lives.

The implications are hard to overstate. If reasoning doesn't require language, then the entire infrastructure we've built around generating, storing, and billing for thinking tokens is unnecessary overhead. Not a moat. Not a feature. Overhead.

We are probably living through the vacuum tube era of AI reasoning. Everything works. Everything is expensive. And something much simpler is about to make it all obsolete.

---

I don't know what replaces the monologue. Nobody does yet. The research is early, the results are promising, the engineering is hard. It might take two years or ten.

But I'm fairly confident about one thing: we will look back at this era and find it absurd. A hundred billion dollars a year, generating text that no one reads, in a medium the model doesn't natively think in, to solve a problem that doesn't require language.

The best thinking is the thinking you never see. The best AI is the one that just *knows*.

We're not there. But the monologue is not the way.

---

*zguo0525@berkeley.edu · [@Zhen4good](https://x.com/Zhen4good)*
