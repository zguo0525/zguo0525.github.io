---
layout: default
title: About
---

I train models that perceive and act in real environments: turning a target capability into tasks, environments, rewards, and data, then post-training frontier multimodal models on them.

Now at **Meta Superintelligence Labs** on real-time omni models for personal agents. Previously **Visual Intelligence** at [Apple](https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/) and [MIT-IBM Watson](https://mitibmwatsonailab.mit.edu/) on synthetic data. **Ph.D. in Computer Science, MIT**; **B.A. in Physics, UC Berkeley**. I read, write, and hike.

## Research

<div markdown="0" class="research">

<article class="rs-row">
  <div class="rs-fig rs-fig--diagram" role="img" aria-label="Turn-based interaction alternates listening and responding; continuous interaction perceives and responds in overlapping streams">
    <svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" font-family="Inter, -apple-system, sans-serif">
      <defs>
        <pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
          <line x1="0" y1="0" x2="0" y2="7" stroke="var(--dg-ink)" stroke-opacity="0.4" stroke-width="1.4"/>
        </pattern>
      </defs>
      <text x="0" y="34" font-size="13" fill="var(--dg-muted)" letter-spacing="0.12em">TURN-BASED</text>
      <text x="0" y="66" font-size="15" fill="var(--dg-ink)">perceive</text>
      <text x="0" y="104" font-size="15" fill="var(--dg-ink)">act</text>
      <rect x="96" y="50" width="118" height="22" rx="4" fill="url(#hatch)" stroke="var(--dg-ink)" stroke-opacity="0.5"/>
      <rect x="220" y="88" width="88" height="22" rx="4" fill="var(--dg-accent)"/>
      <rect x="314" y="50" width="140" height="22" rx="4" fill="url(#hatch)" stroke="var(--dg-ink)" stroke-opacity="0.5"/>
      <rect x="460" y="88" width="98" height="22" rx="4" fill="var(--dg-accent)"/>

      <line x1="0" y1="146" x2="558" y2="146" stroke="var(--dg-ink)" stroke-opacity="0.14"/>

      <text x="0" y="180" font-size="13" fill="var(--dg-muted)" letter-spacing="0.12em">CONTINUOUS</text>
      <text x="0" y="212" font-size="15" fill="var(--dg-ink)">perceive</text>
      <text x="0" y="250" font-size="15" fill="var(--dg-ink)">act</text>
      <rect x="96" y="196" width="462" height="22" rx="4" fill="url(#hatch)" stroke="var(--dg-ink)" stroke-opacity="0.5"/>
      <rect x="128" y="234" width="76" height="22" rx="4" fill="var(--dg-accent)"/>
      <rect x="226" y="234" width="36" height="22" rx="4" fill="var(--dg-accent)"/>
      <rect x="290" y="234" width="126" height="22" rx="4" fill="var(--dg-accent)"/>
      <rect x="446" y="234" width="60" height="22" rx="4" fill="var(--dg-accent)"/>
      <line x1="262" y1="188" x2="262" y2="262" stroke="var(--dg-accent)" stroke-width="1.4" stroke-dasharray="3 3"/>
      <text x="268" y="184" font-size="12" fill="var(--dg-muted)">interrupted, re-plans</text>

      <line x1="96" y1="284" x2="558" y2="284" stroke="var(--dg-ink)" stroke-opacity="0.35"/>
      <text x="558" y="299" font-size="11" fill="var(--dg-muted)" text-anchor="end" letter-spacing="0.1em">TIME →</text>
    </svg>
  </div>
  <div class="rs-text">
    <div class="rs-kicker">Omni models · 2025–26</div>
    <h3>Muse: Real-time perception and action</h3>
    <p>Omni models and proactive question answering on egocentric streaming video: models that perceive and respond continuously instead of turn by turn, and can be interrupted mid-action.</p>
  </div>
</article>

<article class="rs-row">
  <a class="rs-fig" href="https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/" aria-label="Vibes announcement">
    <img src="{{ '/assets/papers/cards/vibes.png' | relative_url }}" alt="Vibes: AI video creation and remix in the Meta AI app" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Vibes · 2025</div>
    <h3>Preference learning and offline RL for a generated-video feed</h3>
    <p>Agentic long-form video generation with Midjourney and Flux, and the preference-learning and offline RL system behind Meta AI's personalized video feed.</p>
    <p class="rs-refs"><a class="chip" href="https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/">Announcement</a></p>
  </div>
</article>

<article class="rs-row">
  <a class="rs-fig" href="https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/" aria-label="Apple Intelligence at WWDC 2025">
    <img src="{{ '/assets/papers/cards/visual-intelligence.png' | relative_url }}" alt="Apple Intelligence features across iPhone, Mac, and iPad" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Apple · 2025</div>
    <h3>Visual Lookup and StreamingQA on device</h3>
    <p>Datasets for on-device visual question answering with privacy-preserving VLMs, and post-training AFM+ on 100K synthetic examples for proactive question answering on egocentric streaming video.</p>
    <p class="rs-refs"><a class="chip" href="https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/">WWDC 2025</a></p>
  </div>
</article>

<article class="rs-row">
  <a class="rs-fig" href="https://arxiv.org/abs/2505.17063" aria-label="Synthetic Data RL paper">
    <img src="{{ '/assets/papers/cards/synthetic-data-rl.png' | relative_url }}" alt="Synthetic Data RL pipeline: data synthesis, difficulty adaptation, selection and RL" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Synthetic Data RL · 2025</div>
    <h3>Environments and rewards from task definitions</h3>
    <p>Given a target capability, synthesize the tasks, the environment, and the reward, then train with RL. No labeled dataset required; the task definition is the input.</p>
    <p class="rs-refs"><a class="chip" href="https://arxiv.org/abs/2505.17063">Paper</a><a class="chip" href="https://arxiv.org/abs/2402.09615">API Pack</a></p>
  </div>
</article>

<article class="rs-row">
  <a class="rs-fig" href="https://arxiv.org/abs/2404.07413" aria-label="JetMoE report">
    <img src="{{ '/assets/papers/cards/jetmoe.png' | relative_url }}" alt="JetMoE-8B benchmark comparison against Llama2-13B" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">JetMoE · 2024</div>
    <h3>Llama2-13B quality from an open MoE trained on 96 H100s</h3>
    <p>JetMoE-8B, an open-source mixture-of-experts model trained on a 1.25T-token synthetic corpus for pre-training and post-training. Nearly 1,000 GitHub stars.</p>
    <p class="rs-refs"><a class="chip" href="https://arxiv.org/abs/2404.07413">Paper</a><a class="chip" href="https://github.com/myshell-ai/JetMoE">Code</a></p>
  </div>
</article>

<article class="rs-row">
  <a class="rs-fig" href="https://arxiv.org/abs/2406.18082" aria-label="Octo-Planner paper">
    <img src="{{ '/assets/papers/cards/octo-planner.png' | relative_url }}" alt="Octo-Planner decomposing a user request into web search, video search, and email actions on a phone" loading="lazy" decoding="async">
  </a>
  <div class="rs-text">
    <div class="rs-kicker">Octo-Planner · 2024</div>
    <h3>On-device planner-action agents</h3>
    <p>Efficient on-device task planning and decomposition, trained on a GPT-4-synthesized planning dataset with a multi-LoRA post-training pipeline. 100K+ downloads.</p>
    <p class="rs-refs"><a class="chip" href="https://arxiv.org/abs/2406.18082">Paper</a></p>
  </div>
</article>

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
