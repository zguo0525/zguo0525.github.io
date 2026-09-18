---
layout: default
title: Essays
subtitle: Thinking in public about AI, product, and strategy.
permalink: /essays.html
---

<div class="essay-filters" role="group" aria-label="Filter essays by topic">
  <button type="button" class="filter-chip active" data-filter="all" aria-pressed="true">All</button>
  <button type="button" class="filter-chip" data-filter="AI" aria-pressed="false">AI</button>
  <button type="button" class="filter-chip" data-filter="Career" aria-pressed="false">Career</button>
  <button type="button" class="filter-chip" data-filter="Strategy" aria-pressed="false">Strategy</button>
</div>

<p class="start-here"><span class="start-here-label">Start here</span> <a href="./articles/agent-topology-manifesto.html">Agent Topology Follows Task, Not Template</a> · <a href="./articles/what-machines-cant-stake.html">What Machines Can't Stake</a> · <a href="./articles/intelligence-per-watt.html">Intelligence per Watt</a></p>

<ul class="essay-list">
{% assign sorted_essays = site.data.essays | sort: "date_sort" | reverse %}
{% for e in sorted_essays %}
  {% capture essay_url %}/articles/{{ e.slug }}.html{% endcapture %}
  {% assign apage = site.articles | where: "url", essay_url | first %}
  <li data-tags="{{ e.tags | join: ',' }}"><span class="item-date">{{ e.date }}</span><a href="./articles/{{ e.slug }}.html">{{ e.title }}</a>{% if e.tags %}<span class="item-tag">{{ e.tags | first }}</span>{% endif %}{% if apage.description %}<p class="essay-desc">{{ apage.description }}</p>{% endif %}</li>
{% endfor %}
</ul>

<p class="more-link"><a href="{{ '/predictions.html' | relative_url }}">Prediction log →</a></p>

<script>
(function() {
  const chips = document.querySelectorAll('.filter-chip');
  const items = document.querySelectorAll('.essay-list li');
  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      const filter = chip.dataset.filter;
      chips.forEach(c => {
        const selected = c === chip;
        c.classList.toggle('active', selected);
        c.setAttribute('aria-pressed', String(selected));
      });
      items.forEach(li => {
        const tags = (li.dataset.tags || '').split(',');
        li.style.display = (filter === 'all' || tags.includes(filter)) ? '' : 'none';
      });
    });
  });
})();
</script>
