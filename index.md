---
layout: default
title: Training agents that perceive and act
---

I train multimodal models to act in the real world. Start from the capability we want, build the tasks, environments, rewards, and synthetic data that teach it, then train with RL.

At <img class="logo-inline" src="{{ '/assets/logos/meta.com.png' | relative_url }}" alt="" width="16" height="16">[**Meta Superintelligence Labs**](https://ai.meta.com/) I lead synthetic data and RL for [Muse](https://research.meta.ai/blog/bringing-your-muse-to-life), a real-time omni model for personal agents, and built the offline RL system behind [Vibes](https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/). Before that, I worked on **Visual Intelligence** at <img class="logo-inline" src="{{ '/assets/logos/apple.com.png' | relative_url }}" alt="" width="16" height="16">[Apple](https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/) and **foundation models** at <img class="logo-inline" src="{{ '/assets/logos/mitibmwatsonailab.mit.edu.png' | relative_url }}" alt="" width="16" height="16">[MIT-IBM Watson](https://mitibmwatsonailab.mit.edu/). I got my **Ph.D. in Computer Science** at <img class="logo-inline" src="{{ '/assets/logos/mit.edu.png' | relative_url }}" alt="" width="16" height="16">[**MIT**](https://www.mit.edu/), and **B.A. in Physics** at <img class="logo-inline" src="{{ '/assets/logos/berkeley.edu.png' | relative_url }}" alt="" width="16" height="16">[**UC Berkeley**](https://www.berkeley.edu/). Outside work I read, write, bike, and hike.

<dl class="now" markdown="0">
  <div class="now-row"><dt>Open questions</dt><dd>
    <ul>
      <li>What does an agent need to perceive and act continuously, rather than turn by turn? <a class="chip chip-jump" href="#muse">Muse ↓</a></li>
      <li>How far can a task definition alone take you: environment, reward, and data? <a class="chip chip-jump" href="#synthetic-data-rl">Synthetic Data RL ↓</a></li>
      <li>How small can a model be and still plan on-device? <a class="chip chip-jump" href="#octo-planner">Octo-planner ↓</a></li>
    </ul>
  </dd></div>
  <div class="now-row"><dt>Talk to me</dt><dd>I'm at <a href="https://colm.cc/">COLM 2026</a>, Oct 6–9, and want to compare notes on two things: rewards for real-time models that act while they perceive, and how far a task definition alone can carry an RL environment. If that's your problem too, <a href="mailto:{{ site.author.email }}">email me</a>. I reply.</dd></div>
</dl>

## Research

<div markdown="0" class="research">

<article class="rs-row" id="muse">
  <a class="rs-fig rs-fig--photo" href="https://research.meta.ai/blog/bringing-your-muse-to-life" aria-label="Muse Realtime Avatar announcement">
    <img src="{{ '/assets/papers/cards/muse.webp' | relative_url }}" width="800" height="600" alt="Grid of characters animated by Muse Realtime Avatar" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Muse · Meta Connect 2026</div>
    <h3><a href="https://research.meta.ai/blog/bringing-your-muse-to-life">Muse Realtime Voice and Avatar</a></h3>
    <p>Muse Realtime Voice carries the conversation as a stream of speech tokens, and Muse Realtime Avatar turns the same stream into a live, expressive character for as long as the conversation runs. I lead synthetic data and RL, and work on the distillation that makes it fast enough to serve in real time.</p>
    <p class="rs-refs"><a class="chip" href="https://research.meta.ai/blog/bringing-your-muse-to-life">Keynote</a></p>
  </div>
</article>

<article class="rs-row">
  <a class="rs-fig rs-fig--photo" href="https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/" aria-label="Vibes announcement">
    <img src="{{ '/assets/papers/cards/vibes.webp' | relative_url }}" width="800" height="589" alt="Vibes: AI video creation and remix in the Meta AI app" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Vibes · 2025</div>
    <h3><a href="https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/">Offline RL for a generated-video feed</a></h3>
    <p>Built the agentic long-form video workflow and the offline RL system behind Vibes, Meta AI's personalized video feed, and led its human-evaluation data.</p>
    <p class="rs-refs"><a class="chip" href="https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/">Blog</a></p>
  </div>
</article>

<article class="rs-row">
  <a class="rs-fig rs-fig--photo" href="https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/" aria-label="Apple Intelligence at WWDC 2025">
    <img src="{{ '/assets/papers/cards/visual-intelligence.webp' | relative_url }}" width="800" height="554" alt="Apple Intelligence features across iPhone, Mac, and iPad" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Apple · 2025</div>
    <h3><a href="https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/">Visual Intelligence on device</a></h3>
    <p>Built the datasets for on-device visual question answering on iPhone with privacy-preserving VLMs, and post-trained Apple's foundation model for proactive question answering on egocentric video. Shipped in Apple Intelligence at WWDC 2025.</p>
    <p class="rs-refs"><a class="chip" href="https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/">Blog</a></p>
  </div>
</article>

<article class="rs-row" id="synthetic-data-rl">
  <a class="rs-fig" href="https://arxiv.org/abs/2505.17063" aria-label="Synthetic Data RL paper">
    <img src="{{ '/assets/papers/cards/synthetic-data-rl.webp' | relative_url }}" width="800" height="408" alt="Synthetic Data RL pipeline: data synthesis, difficulty adaptation, selection and RL" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Synthetic Data RL · 2025</div>
    <h3><a href="https://arxiv.org/abs/2505.17063">Environments and rewards from task definitions</a></h3>
    <p>Given a target capability, synthesize the tasks, the environment, and the reward, then train with RL. No labeled dataset required; the task definition is the input.</p>
    <p class="rs-refs"><a class="chip" href="https://arxiv.org/abs/2505.17063">Paper</a><a class="chip" href="https://arxiv.org/abs/2402.09615">API Pack</a></p>
  </div>
</article>

<article class="rs-row">
  <a class="rs-fig" href="https://arxiv.org/abs/2404.07413" aria-label="JetMoE report">
    <img src="{{ '/assets/papers/cards/jetmoe.webp' | relative_url }}" width="800" height="344" alt="JetMoE-8B benchmark comparison against Llama2-13B" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">JetMoE · 2024</div>
    <h3><a href="https://arxiv.org/abs/2404.07413">Open MoE at Llama2-13B quality</a></h3>
    <p>JetMoE-8B, an open-source mixture-of-experts model trained for a fraction of the usual cost that outperforms Llama2-13B, with a synthetic corpus for pre-training and post-training.</p>
    <p class="rs-refs"><a class="chip" href="https://arxiv.org/abs/2404.07413">Paper</a><a class="chip" href="https://github.com/myshell-ai/JetMoE">Code</a></p>
  </div>
</article>

<article class="rs-row" id="octo-planner">
  <a class="rs-fig" href="https://arxiv.org/abs/2406.18082" aria-label="Octo-planner paper">
    <img src="{{ '/assets/papers/cards/octo-planner.webp' | relative_url }}" width="800" height="515" alt="Octo-planner decomposing a user request into web search, video search, and email actions on a phone" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Octo-planner · 2024</div>
    <h3><a href="https://arxiv.org/abs/2406.18082">On-device planner-action agents</a></h3>
    <p>Efficient on-device task planning and decomposition, trained on a synthetic planning dataset with a multi-LoRA post-training pipeline.</p>
    <p class="rs-refs"><a class="chip" href="https://arxiv.org/abs/2406.18082">Paper</a></p>
  </div>
</article>

</div>

<p class="more-link"><a href="{{ '/papers.html' | relative_url }}">All publications →</a></p>

## News

<ul class="newslist newslist--home" markdown="0">
{% for n in site.data.news limit:3 %}
  <li class="news-row">
    {% if n.link %}<a class="news-thumb" href="{{ n.link }}" aria-hidden="true" tabindex="-1"><img src="{{ n.thumb | relative_url }}" alt="" loading="lazy" decoding="async" width="640" height="360"></a>{% else %}<span class="news-thumb"><img src="{{ n.thumb | relative_url }}" alt="" loading="lazy" decoding="async" width="640" height="360"></span>{% endif %}
    <div class="news-body">
      <span class="item-date">{{ n.month }} {{ n.year }}{% if n.upcoming %} <span class="news-upcoming">· Upcoming</span>{% endif %}</span>
      <p>{{ n.text | markdownify | remove: '<p>' | remove: '</p>' }}</p>{% if n.link %}<a class="news-link" href="{{ n.link }}">Read more →</a>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>

<p class="more-link"><a href="{{ '/news.html' | relative_url }}">All news →</a></p>

## Essays on AI

<ul class="essay-list">
{% assign sorted_essays = site.data.essays | sort: "date_sort" | reverse %}
{% assign shown = 0 %}
{% for hit in sorted_essays %}
  {% if hit.tags contains "AI" and shown < 3 %}
    {% assign shown = shown | plus: 1 %}
    {% capture essay_url %}/articles/{{ hit.slug }}.html{% endcapture %}
    {% assign apage = site.articles | where: "url", essay_url | first %}
    <li><span class="item-date">{{ hit.date }}</span><a href="{{ essay_url | relative_url }}">{{ hit.title }}</a><span class="item-tag">AI</span>{% if apage.description %}<p class="essay-desc">{{ apage.description }}</p>{% endif %}</li>
  {% endif %}
{% endfor %}
</ul>

<p class="more-link"><a href="{{ '/essays.html' | relative_url }}">All essays →</a></p>
