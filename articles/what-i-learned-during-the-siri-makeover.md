# What I Learned During the Siri Makeover

*July 2025*

The new Siri demo was impressive, and for those of us with a background in engineering, it also hinted at the complexity ahead. [A recent article from *The Information*](https://www.theinformation.com/articles/apple-fumbled-siris-ai-makeover) detailed some of the hurdles, and the situation highlighted a broader observation: even the most well-resourced companies navigate significant obstacles when shipping products with evolving technology.

## The Anatomy of an AI Challenge

While Siri's new user-facing features captured headlines, I found the quieter work on notification summaries to be particularly instructive from a product development standpoint. The feature, designed to condense alerts, served as a powerful example of the challenges in applied AI.

The public stumbles—an AI turning a polite request into a blunt command or misreading a simple group chat—seemed to be more than just bugs; they pointed to a lack of social context in the underlying models. This highlights a fundamental tension in modern AI development: to work well, AI needs data from the cloud, but to remain private, it must run on-device.

The learning curve became especially clear when the feature was adjusted after media outlets like the BBC raised concerns. That moment felt significant, as it turned a technical hurdle into an opportunity to build public trust. It also illustrated the gap between a model's ability to process text and its capacity to understand human meaning.

## The Human Element

Beyond the technical hurdles, the organizational dynamics were also quite interesting. The reported friction between software engineering and AI teams highlights a familiar challenge: integrating a research-oriented AI division with a product-driven engineering organization.

The two groups often operate on different clocks. One is built for shipping products on a deadline, while the other is designed for exploration. Tensions can arise when the iterative, non-linear process of research is measured against the linear standards of a product roadmap.

## What This Means for AI

To me, Apple's experience with Siri points to a key lesson for the next era of AI: success will likely be determined not just by the best models, but by the best product integration.

While building a product from scratch offers a blank slate—as OpenAI did with ChatGPT—Apple faces a much harder task: making a core product smarter for a billion users without breaking the features they rely on daily.

## Lessons for Builders

The situation offers a few key takeaways for builders:

**First, the simplest-seeming AI features are often the most complex.** Notification summaries appeared trivial but demanded a grasp of context and tone that models still struggle to handle reliably.

**Second, organizational design shapes product outcomes.** The integration between research and product teams is a critical component of shipping great AI.

**Third, privacy works best as an architectural constraint, not a slogan.** On-device processing makes everything harder, but such constraints are often catalysts for innovation. For me, respecting privacy is a durable, long-term advantage.

---

*Disclaimer: This piece reflects my personal observations and does not represent Apple's official positions. I'm grateful for my time in the AIML Residency and for the opportunity to work alongside the talented engineers addressing these challenges.* 