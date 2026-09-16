---
layout: default
title: Papers
subtitle: Publications, patents, and selected projects.
permalink: /papers.html
---

{% for sec in site.data.papers %}
## {{ sec.title }}
{% for g in sec.groups %}{% if g.title %}
### {{ g.title }}
{% endif %}
<ul class="publist" markdown="0">
{% for p in g.items %}
  <li class="pub-row" id="{{ p.id }}">
    {% if p.url %}<a class="pub-thumb" href="{{ p.url }}" aria-hidden="true" tabindex="-1"><img src="{{ p.thumb | relative_url }}" alt="" loading="lazy" decoding="async" width="640" height="360"></a>{% else %}<span class="pub-thumb"><img src="{{ p.thumb | relative_url }}" alt="" loading="lazy" decoding="async" width="640" height="360"></span>{% endif %}
    <div class="pub-body">
      <strong>{% if p.url %}<a href="{{ p.url }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</strong>
      <div class="pub-meta">{{ p.meta | markdownify | remove: '<p>' | remove: '</p>' }}</div>
      {% if p.chips.size > 0 %}<div class="pub-chips">{% for c in p.chips %}<a class="chip" href="{{ c.url }}">{{ c.label }}</a>{% endfor %}</div>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
{% endfor %}{% endfor %}
