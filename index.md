---
layout: default
title: About
---

**Multi-Avocado** and **Multi-Mango** at **Meta Superintelligence Labs**.

Previously, I worked on **Visual Intelligence** at [Apple Siri](https://www.apple.com/siri/), and interned at [MIT-IBM Watson](https://mitibmwatsonailab.mit.edu/) on synthetic data and model training. I hold a **Ph.D. in Computer Science** from **MIT** and a **B.A. in Physics** with a minor in English from **UC Berkeley**. Outside of work, I read, write, and hike.

## Selected Research

<div markdown="0">
<a class="paper-feature" href="https://arxiv.org/abs/2505.17063">
  <div class="paper-thumb"><img src="{{ '/assets/papers/cards/synthetic-data-rl.png' | relative_url }}" alt="" loading="lazy" decoding="async"></div>
  <div class="paper-meta">
    <div class="paper-kicker">Featured · arXiv 2025</div>
    <div class="paper-title">Synthetic Data RL: Task Definition Is All You Need</div>
    <p class="paper-desc">Reinforcement fine-tuning from a task definition alone — synthesize the data, adapt the difficulty, train with RL. No labeled dataset required.</p>
  </div>
</a>
</div>

<div class="paper-grid">

<a class="paper-card" href="https://arxiv.org/abs/2402.09615">
  <div class="paper-thumb"><img src="{{ '/assets/papers/cards/api-pack.png' | relative_url }}" alt="" loading="lazy" decoding="async"></div>
  <div class="paper-meta">
    <div class="paper-title">API Pack</div>
    <div class="paper-sub">ICLR 2025</div>
  </div>
</a>

<a class="paper-card" href="https://arxiv.org/abs/2404.07413">
  <div class="paper-thumb"><img src="{{ '/assets/papers/cards/jetmoe.png' | relative_url }}" alt="" loading="lazy" decoding="async"></div>
  <div class="paper-meta">
    <div class="paper-title">JetMoE</div>
    <div class="paper-sub">MyShell AI, 2024</div>
  </div>
</a>

<a class="paper-card" href="https://arxiv.org/abs/2311.07700">
  <div class="paper-thumb"><img src="{{ '/assets/papers/cards/authentigpt.png' | relative_url }}" alt="" loading="lazy" decoding="async"></div>
  <div class="paper-meta">
    <div class="paper-title">AuthentiGPT</div>
    <div class="paper-sub">NeurIPS 2023</div>
  </div>
</a>

</div>

<p class="more-link"><a href="{{ '/papers.html' | relative_url }}">All publications →</a></p>

## Recent Essays

<ul class="essay-list">
{% assign recent_essays = site.data.essays | sort: "date_sort" | reverse %}
{% for e in recent_essays limit:3 %}
  {% capture essay_url %}/articles/{{ e.slug }}.html{% endcapture %}
  {% assign apage = site.articles | where: "url", essay_url | first %}
  <li><span class="item-date">{{ e.date }}</span><a href="{{ essay_url | relative_url }}">{{ e.title }}</a>{% if e.tags %}<span class="item-tag">{{ e.tags | first }}</span>{% endif %}{% if apage.description %}<p class="essay-desc">{{ apage.description }}</p>{% endif %}</li>
{% endfor %}
</ul>

<p class="more-link"><a href="{{ '/essays.html' | relative_url }}">All essays →</a></p>
