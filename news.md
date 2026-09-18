---
layout: default
title: News
subtitle: Milestones, releases, and appearances.
permalink: /news.html
description: Milestones, releases, and appearances from Gavin Guo, research scientist at Meta Superintelligence Labs.
---

{% assign years = site.data.news | map: "year" | uniq %}
{% for y in years %}
## {{ y }}

<ul class="newslist" markdown="0">
{% for n in site.data.news %}{% if n.year == y %}
  <li class="news-row">
    {% if n.link %}<a class="news-thumb" href="{{ n.link }}" aria-hidden="true" tabindex="-1"><img src="{{ n.thumb | relative_url }}" alt="" loading="lazy" decoding="async" width="640" height="360"></a>{% else %}<span class="news-thumb"><img src="{{ n.thumb | relative_url }}" alt="" loading="lazy" decoding="async" width="640" height="360"></span>{% endif %}
    <div class="news-body">
      <span class="item-date">{{ n.month }} {{ n.year }}{% if n.upcoming %} · Upcoming{% endif %}</span>
      <p>{{ n.text | markdownify | remove: '<p>' | remove: '</p>' }}{% if n.link %} <a class="news-link" href="{{ n.link }}">Read more</a>{% endif %}</p>
    </div>
  </li>
{% endif %}{% endfor %}
</ul>
{% endfor %}
