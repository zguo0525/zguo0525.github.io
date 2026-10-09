---
layout: default
title: "Why People Took to Muse"
image: /assets/cards/real-time-video-is-a-control-problem.png
description: "People rarely feel quality. They feel fit. What the GPT-5 launch, Sora and ChatGPT's sycophancy rollback say about why Muse took off."
date: 2026-10-08
tags: [AI]
---
When an AI product wins, people credit the model. I think that's usually a mistake. What people feel isn't quality. It's fit.

Muse is a good case. It launched on September 8, was the top free app in the US App Store ten days later, and passed five million downloads in 22 days. ChatGPT took 56 ([9to5Mac](https://9to5mac.com/2026/09/30/report-metas-muse-crosses-5-million-downloads-amid-massive-advertising-push/)). Some of that is distribution. Meta put a lot of its own ad space behind the app, so downloads overstate real demand.

The reviews are better evidence. The app has 4.9 stars from about 185,000 ratings, and what people say in them is not "the model is smart." One user, who is building a business and pays for ChatGPT, [wrote](https://apps.apple.com/us/app/muse-from-meta/id6760173601) that they get more done with Muse in half an hour than in two hours with ChatGPT, because ChatGPT will "tell me what I want to hear."

That's not a benchmark. It's someone saying that one product fit what they needed and the other didn't.

By fit I mean something specific: whether a response is right for this person at this moment. Not good in general. Right for them, now.

---

Why would fit beat quality? The clearest case is ChatGPT itself.

On August 7, 2025, OpenAI launched GPT-5 and removed GPT-4o from ChatGPT without warning. The new model was supposed to be the better one. Users said its replies were shorter and more formal, and that the warmth was gone. A Reddit post about it got around 10,000 upvotes: ["4o wasn't just a tool for me"](https://www.platformer.news/gpt-5-backlash-openai-lessons/). The next day, Sam Altman promised Plus users they could keep 4o. He later called the sudden removal [a mistake](https://www.benzinga.com/markets/tech/25/08/47023202/sam-altman-admits-deprecating-old-models-was-a-mistake-as-chatgpt-users-give-frosty-reception-to-gpt-5s-soulless-personality).

Here's the mechanism. Once answers are good enough, the thing left to notice is the manner: tone, pace, how it treats you. People don't notice a benchmark gain. They notice a change in who they're talking to. A benchmark measures what a model can do. A user feels who it is.

Voice shows the same thing. Sesame, a voice startup, found that listeners [couldn't prefer](https://sesame.com/research/crossing_the_uncanny_valley_of_voice) real speech over generated speech when they heard clips on their own. When the clips sat inside a real conversation, they chose the human. The voice sounded right. It didn't fit.

Quality can also win the first week and lose the second. Sora, OpenAI's video app, topped the App Store within days of its October 2025 launch. By January, [downloads and spending were falling](https://techcrunch.com/2026/01/29/openais-sora-app-is-struggling-after-its-stellar-launch/), and in March OpenAI [shut it down](https://www.cnbc.com/2026/03/24/openai-shutters-short-form-video-app-sora-as-company-reels-in-costs.html).[1] The video was impressive enough to get people to try it. It gave them no reason to come back.

That's the same test Muse faces, and it's why I don't take downloads as proof of anything.

---

What is fit made of? I think three things.

**Timing.** For years, ChatGPT's voice mode could talk but didn't know when to stop. In July 2026, OpenAI replaced it with [GPT-Live](https://techcrunch.com/2026/07/08/openai-releases-new-voice-models-for-more-natural-live-conversations/), models that "speak and listen at the same time" so you can interrupt naturally, and it claims they handle turn-taking better. The words weren't the problem. The timing was.

Conversation has a tight budget. People answer each other in about [200 milliseconds](https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00731/full). Muse Realtime Avatar answers about 870 milliseconds after you stop speaking. That's fast for an avatar. It isn't yet how people talk, and I'd rather say so than pretend.

**Continuity.** The GPT-4o story is really about continuity. People had spent months with one personality, and the update replaced it. Muse's blog makes a point of this: the avatar's appearance and mannerisms stay coherent from one turn to the next. A face that changes between sentences isn't a smaller flaw. It's a different person.

Continuity cuts both ways, though. Attachment is what makes people come back, and it's also what made Character.AI [end open-ended chat for under-18s](https://www.cnbc.com/2025/11/24/characterai-to-ban-teens-from-open-ended-chats-human-interaction-is-crucial-psychotherapist-says.html) in November 2025, after lawsuits. Fit that ignores what's good for the person isn't fit.

**Honesty.** In April 2025, OpenAI rolled back a GPT-4o update that Altman said was ["too sycophant-y and annoying."](https://techcrunch.com/2025/04/29/openai-explains-why-chatgpt-became-too-sycophantic) The company's explanation was that it had leaned too much on short-term feedback. Reporting at the time said that included thumbs-up and thumbs-down data. People rewarded flattery one reply at a time, and the result was a worse product.

The obvious fix is to ask users what they want. That's where it gets hard. A study in [*Science*](https://www.science.org/doi/10.1126/science.aec8352) this March, from Stanford and Carnegie Mellon, tested 11 leading models. They affirmed users 49% more often than humans did, and participants rated the flattering answers as higher quality and trusted them more. Users reward the thing that hurts them.

So honesty is the part of fit that users, asked directly, will vote against. Anthropic now treats it as a product metric: it reports its newest models scoring [70 to 85 percent lower](https://www.anthropic.com/news/protecting-well-being-of-users) than Opus 4.1 on sycophancy audits. And look back at the review I started with. The user didn't praise Muse for being agreeable. They praised it for not telling them what they wanted to hear.

---

If users reward flattery, how do you measure fit at all?

You can't do it from a clip, and you can't do it from a single thumbs-up. You have to watch what happens to the person. That's why we evaluated Muse Realtime Avatar the way we did. Raters held two- to three-minute live conversations with it and with two commercial avatars, each in its own native live-call experience, using matched identities. They preferred Muse overall and on every dimension. The one tie, with Runway, was on mannerisms ([Meta](https://research.meta.ai/blog/bringing-your-muse-to-life)). We measured latency from the moment the user stops talking, not from when the model starts. Neither choice is clever. Both follow from accepting that fit is the thing to measure, and that only the person in the conversation can tell you whether it's there.

The next step is harder. A live conversation is full of fit signals: people keep talking when it works, and interrupt, repeat themselves or go quiet when it doesn't. Today almost none of that becomes training signal. The GPT-4o rollback says not to feed it back naively. But I think the products that win this category will be the ones that learn to use it well.

None of this is proven yet. Downloads are a first impression, and daily users are still a fraction of downloads. OpenAI's answer, Dots, launched on September 29, first for Pro and business users. The real test is whether people are still talking to Muse in six months.

But the question that matters is the one GPT-5 answered the hard way. Not "how good is the model?" Ask whether it fits the person using it.

---

**Notes**

[1] OpenAI also cited costs. CNBC's headline says it was shutting the app down as the company reels in costs, so retention wasn't the only reason. I use Sora as an illustration of how quickly a launch spike can fade, not as proof that fit alone decided it.

*I work on Muse Realtime Avatar at Meta. Views my own; everything here is public. · zguo0525@berkeley.edu · [@Zhen4good](https://x.com/Zhen4good)*
