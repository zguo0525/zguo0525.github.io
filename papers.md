---
layout: default
title: Papers
subtitle: Publications, patents, and selected projects.
permalink: /papers.html
---

<div class="essay-filters" role="group" aria-label="Show selected or all papers">
  <button type="button" class="filter-chip active" data-filter="all" aria-pressed="true">All</button>
  <button type="button" class="filter-chip" data-filter="selected" aria-pressed="false">Selected</button>
</div>

{% for sec in site.data.papers %}
## {{ sec.title }}
{% for g in sec.groups %}{% if g.title %}
### {{ g.title }}
{% endif %}
<ul class="publist" markdown="0">
{% for p in g.items %}
  <li class="pub-row{% if p.selected %} is-selected{% endif %}" id="{{ p.id }}"{% if p.selected %} data-selected="1"{% endif %}>
    {% if p.url %}<a class="pub-thumb" href="{{ p.url }}" aria-hidden="true" tabindex="-1"><img src="{{ p.thumb | relative_url }}" alt="" loading="lazy" decoding="async" width="640" height="360"></a>{% else %}<span class="pub-thumb"><img src="{{ p.thumb | relative_url }}" alt="" loading="lazy" decoding="async" width="640" height="360"></span>{% endif %}
    <div class="pub-body">
      <strong>{% if p.url %}<a href="{{ p.url }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</strong>
      <div class="pub-meta">{{ p.meta | markdownify | remove: '<p>' | remove: '</p>' }}{% if p.note %} <span class="pub-note">{{ p.note }}</span>{% endif %}</div>
      {% if p.tldr %}<p class="pub-tldr">{{ p.tldr }}</p>{% endif %}
      {% if p.chips.size > 0 %}<div class="pub-chips">{% for c in p.chips %}<a class="chip" href="{{ c.url }}">{{ c.label }}</a>{% endfor %}</div>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
{% endfor %}{% endfor %}

<script>
(function() {
  const chips = document.querySelectorAll('.filter-chip');
  const rows = document.querySelectorAll('.pub-row');
  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      const sel = chip.dataset.filter === 'selected';
      chips.forEach(c => { const on = c === chip; c.classList.toggle('active', on); c.setAttribute('aria-pressed', String(on)); });
      rows.forEach(li => { li.style.display = (!sel || li.dataset.selected) ? '' : 'none'; });
      document.querySelectorAll('.pubs ul.publist').forEach(ul => {
        const any = [...ul.querySelectorAll('.pub-row')].some(li => li.style.display !== 'none');
        ul.style.display = any ? '' : 'none';
        let h = ul.previousElementSibling; while (h && !/^H[23]$/.test(h.tagName)) h = h.previousElementSibling;
        if (h && h.tagName === 'H3') h.style.display = any ? '' : 'none';
      });
      document.querySelectorAll('.pubs h2').forEach(h2 => {
        let el = h2.nextElementSibling, any = false;
        while (el && el.tagName !== 'H2') { if (el.classList.contains('publist') && el.style.display !== 'none') any = true; el = el.nextElementSibling; }
        h2.style.display = any ? '' : 'none';
      });
    });
  });
})();
</script>
