---
layout: default
title: Training agents that perceive and act
nav_title: About
---

I train multimodal models to act in the real world. Start from the capability we want, build the tasks, environments, rewards, and synthetic data that teach it, then train with RL.

At <img class="logo-inline" src="{{ '/assets/logos/meta.com.png' | relative_url }}" alt="" width="16" height="16">[**Meta Superintelligence Labs**](https://ai.meta.com/) I lead synthetic data and RL for [Muse](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/), a real-time omni model for personal agents, and built the offline RL system behind [Vibes](https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/). Before that, I worked on **Visual Intelligence** at <img class="logo-inline" src="{{ '/assets/logos/apple.com.png' | relative_url }}" alt="" width="16" height="16">[Apple](https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/) and **foundation models** at <img class="logo-inline" src="{{ '/assets/logos/mitibmwatsonailab.mit.edu.png' | relative_url }}" alt="" width="16" height="16">[MIT-IBM Watson](https://mitibmwatsonailab.mit.edu/), and was a founding researcher at <img class="logo-inline" src="{{ '/assets/logos/myshell.ai.png' | relative_url }}" alt="" width="16" height="16">[MyShell AI](https://myshell.ai/) on multimodal agents and <img class="logo-inline" src="{{ '/assets/logos/pinai.com.png' | relative_url }}" alt="" width="16" height="16">[PIN AI](https://www.pinai.com/) on personal agents. I got my **Ph.D. in Computer Science** at <img class="logo-inline" src="{{ '/assets/logos/mit.edu.png' | relative_url }}" alt="" width="16" height="16">[**MIT**](https://www.mit.edu/), and **B.A. in Physics** at <img class="logo-inline" src="{{ '/assets/logos/berkeley.edu.png' | relative_url }}" alt="" width="16" height="16">[**UC Berkeley**](https://www.berkeley.edu/). Outside work I read, write, bike, and hike.

<dl class="now" markdown="0">
  <div class="now-row"><dt>Open questions</dt><dd>
    <ul>
      <li><a href="#muse">What does an agent need to perceive and act continuously, rather than turn by turn?</a></li>
      <li><a href="#synthetic-data-rl">How far can a task definition alone take you: environment, reward, and data?</a></li>
      <li><a href="#octo-planner">How small can a model be and still plan on-device?</a></li>
    </ul>
  </dd></div>
  <div class="now-row"><dt>Talk to me</dt><dd>If you work on real-time agents, RL environments, or post-training, <a href="mailto:{{ site.author.email }}">email me</a>. I reply. Meeting at <a href="https://colm.cc/">COLM 2026</a>, Oct 6–9.</dd></div>
</dl>

## Research

<div markdown="0" class="research">

<article class="rs-row" id="muse">
  <div class="rs-fig rs-fig--diagram" role="img" aria-label="Turn-based interaction alternates listening and responding; continuous interaction perceives and responds in overlapping streams">
    <svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" font-family="ui-monospace, Menlo, monospace" aria-hidden="true" focusable="false">
      <defs>
        <pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
          <line x1="0" y1="0" x2="0" y2="6" stroke="var(--dg-ink)" stroke-opacity="0.45" stroke-width="1.6"/>
        </pattern>
      </defs>
      <text x="0" y="22" font-size="13" fill="var(--dg-muted)" letter-spacing="0.08em">TURN-BASED</text>
      <text x="0" y="50" font-size="15" fill="var(--dg-ink)">perceive</text>
      <text x="0" y="82" font-size="15" fill="var(--dg-ink)">act</text>
      <rect x="82" y="36" width="80" height="20" rx="3" fill="url(#hatch)" stroke="var(--dg-ink)" stroke-opacity="0.55"/>
      <rect x="166" y="68" width="60" height="20" rx="3" fill="var(--dg-accent)"/>
      <rect x="230" y="36" width="80" height="20" rx="3" fill="url(#hatch)" stroke="var(--dg-ink)" stroke-opacity="0.55"/>
      <rect x="314" y="68" width="46" height="20" rx="3" fill="var(--dg-accent)"/>
      <line x1="0" y1="106" x2="360" y2="106" stroke="var(--dg-ink)" stroke-opacity="0.15"/>
      <text x="0" y="130" font-size="13" fill="var(--dg-muted)" letter-spacing="0.08em">CONTINUOUS</text>
      <text x="0" y="158" font-size="15" fill="var(--dg-ink)">perceive</text>
      <text x="0" y="190" font-size="15" fill="var(--dg-ink)">act</text>
      <rect x="82" y="144" width="278" height="20" rx="3" fill="url(#hatch)" stroke="var(--dg-ink)" stroke-opacity="0.55"/>
      <rect x="100" y="176" width="52" height="20" rx="3" fill="var(--dg-accent)"/>
      <rect x="164" y="176" width="24" height="20" rx="3" fill="var(--dg-accent)"/>
      <rect x="200" y="176" width="84" height="20" rx="3" fill="var(--dg-accent)"/>
      <rect x="302" y="176" width="40" height="20" rx="3" fill="var(--dg-accent)"/>
      <line x1="188" y1="140" x2="188" y2="198" stroke="var(--dg-accent)" stroke-width="1.5" stroke-dasharray="3 3"/>
    </svg>
  </div>
  <div class="rs-text">
    <div class="rs-kicker">Omni models · 2025–26</div>
    <h3>Muse: Real-time perception and action</h3>
    <p>An omni model that perceives and responds in real time instead of turn by turn, and can be interrupted mid-action. I lead efforts in synthetic data and RL, and work on the distillation that makes it fast and natural enough to talk to.</p>
  </div>
</article>

<article class="rs-row">
  <a class="rs-fig rs-fig--photo" href="https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/" aria-label="Vibes announcement">
    <img src="{{ '/assets/papers/cards/vibes.webp' | relative_url }}" width="800" height="589" alt="Vibes: AI video creation and remix in the Meta AI app" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Vibes · 2025</div>
    <h3><a href="https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/">Offline RL for a generated-video feed</a></h3>
    <p>Built the agentic long-form video generation workflow and the offline RL system behind Vibes, Meta AI's personalized video feed, and led the human-evaluation data behind it.</p>
    <p class="rs-refs"><a class="chip" href="https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/">Blog</a></p>
  </div>
</article>

<article class="rs-row">
  <a class="rs-fig rs-fig--photo" href="https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/" aria-label="Apple Intelligence at WWDC 2025">
    <img src="{{ '/assets/papers/cards/visual-intelligence.webp' | relative_url }}" width="800" height="554" alt="Apple Intelligence features across iPhone, Mac, and iPad" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Apple · 2025</div>
    <h3><a href="https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/">Visual Lookup and StreamingQA on device</a></h3>
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
  <a class="rs-fig" href="https://arxiv.org/abs/2406.18082" aria-label="Octo-Planner paper">
    <img src="{{ '/assets/papers/cards/octo-planner.webp' | relative_url }}" width="800" height="515" alt="Octo-Planner decomposing a user request into web search, video search, and email actions on a phone" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Octo-Planner · 2024</div>
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
      <span class="item-date">{{ n.month }} {{ n.year }}{% if n.upcoming %} · Upcoming{% endif %}</span>
      <p>{{ n.text | markdownify | remove: '<p>' | remove: '</p>' }}{% if n.link %} <a class="news-link" href="{{ n.link }}">Read more</a>{% endif %}</p>
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
