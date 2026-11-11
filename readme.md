# Personal Website

Source for <https://zguo0525.github.io>, a Jekyll site built and served by GitHub Pages.

## Local development

Requires Homebrew Ruby 3.3 (`brew install ruby@3.3`); the system Ruby (2.6) and Ruby 4.x do not work with the github-pages gem.

```sh
export PATH="$HOME/.gem/ruby33/bin:/opt/homebrew/opt/ruby@3.3/bin:$PATH"
export GEM_HOME=$HOME/.gem/ruby33
bundle install          # first time only
bundle exec jekyll serve
```

## Repo structure

| Path | What it is |
|---|---|
| `_config.yml` | Site settings, author links, plugins (`jekyll-sitemap`, `jekyll-feed`, `jekyll-seo-tag`), and the `articles` collection |
| `_layouts/default.html` | The only layout: head, navigation, page/essay chrome, footer, analytics |
| `assets/css/site.css` | The only stylesheet. Plain hand-written CSS, no Sass and no theme gem |
| `_includes/icon-*.svg` | Inline SVG icons used by the layout |
| `index.md` | Homepage: intro, research cards, latest news and essays |
| `news.md`, `essays.md`, `papers.md` | List pages, rendered from `_data/` |
| `pages/` | Bio and the prediction log |
| `_data/news.yml`, `_data/essays.yml`, `_data/papers.yml` | Content for the list pages |
| `_articles/` | Essays, one Markdown file each, published at `/articles/<slug>.html` |
| `assets/cards/` | Open Graph cards, one per essay |
| `assets/news/`, `assets/papers/`, `assets/logos/` | Thumbnails and logos |
| `papers/`, `slides/` | PDFs linked from `_data/papers.yml` |
| `scripts/gen_og_cards.py` | Generates the essay Open Graph cards (needs Pillow and the Charter font, i.e. macOS) |
| `GOATCOUNTER-SETUP.md` | Notes on the GoatCounter view-count setup |

## Adding content

- **Essay**: add `_articles/<slug>.md` with `title`, `description`, `date`, `image` and `tags` front matter, add a matching entry at the top of `_data/essays.yml`, then run `python3 scripts/gen_og_cards.py <slug>` and commit the new card.
- **News**: add an entry at the top of `_data/news.yml` with a thumbnail in `assets/news/`.
- **Paper**: add an entry to `_data/papers.yml` with a thumbnail in `assets/papers/thumbs/`.

Fonts (Source Serif 4, Inter) load from Google Fonts in the layout.
