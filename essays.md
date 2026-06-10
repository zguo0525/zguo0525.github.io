---
layout: default
title: Essays
permalink: /essays.html
---

## Essays

<div class="essay-filters">
  <button class="filter-chip active" data-filter="all">All</button>
  <button class="filter-chip" data-filter="AI">AI</button>
  <button class="filter-chip" data-filter="Career">Career</button>
  <button class="filter-chip" data-filter="Strategy">Strategy</button>
</div>

<ul class="essay-list">
{% assign sorted_essays = site.data.essays | sort: "date_sort" | reverse %}
{% for e in sorted_essays %}
  <li data-tags="{{ e.tags | join: ',' }}"><span class="item-date">{{ e.date }}</span><a href="./articles/{{ e.slug }}.html">{{ e.title }}</a></li>
{% endfor %}
</ul>

<script>
(function() {
  const chips = document.querySelectorAll('.filter-chip');
  const items = document.querySelectorAll('.essay-list li');
  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      const filter = chip.dataset.filter;
      chips.forEach(c => c.classList.toggle('active', c === chip));
      items.forEach(li => {
        const tags = (li.dataset.tags || '').split(',');
        li.style.display = (filter === 'all' || tags.includes(filter)) ? '' : 'none';
      });
    });
  });
})();
</script>
