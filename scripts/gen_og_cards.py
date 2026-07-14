#!/usr/bin/env python3
"""Generate 1200x630 Open Graph card images for each essay in _articles/.

Cards use the site's palette and Charter (second font in the site's serif
stack). Run after adding a new essay, then commit the new PNG:

    python3 scripts/gen_og_cards.py

Each article's front matter should point at its card:

    image: /assets/cards/<slug>.png
"""

import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "_articles"
OUT = ROOT / "assets" / "cards"

W, H = 1200, 630
MARGIN = 90
MAX_TEXT_W = W - 2 * MARGIN

BG = "#faf9f6"
INK = "#1f1e1b"
MUTED = "#75716a"
ACCENT = "#a8442a"

CHARTER = "/System/Library/Fonts/Supplemental/Charter.ttc"
BOLD_INDEX = 3  # Charter.ttc faces: 0 Roman, 1 Italic, 2 Bold Italic, 3 Bold
REGULAR_INDEX = 0


def load_font(size, index):
    return ImageFont.truetype(CHARTER, size, index=index)


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, line = [], ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit_title(draw, text, max_w, max_lines=3, start=84, floor=48):
    size = start
    while size > floor:
        font = load_font(size, BOLD_INDEX)
        lines = wrap(draw, text, font, max_w)
        if len(lines) <= max_lines:
            return font, lines, size
        size -= 4
    font = load_font(floor, BOLD_INDEX)
    return font, wrap(draw, text, font, max_w), floor


def make_card(title, out_path):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    label_font = load_font(26, REGULAR_INDEX)
    label = "ESSAY  ·  GAVIN GUO"
    draw.text((MARGIN, MARGIN), " ".join(label), font=label_font, fill=MUTED)

    title_font, lines, size = fit_title(draw, title, MAX_TEXT_W)
    line_h = int(size * 1.22)
    block_h = line_h * len(lines)
    top = (H - block_h) // 2 + 10

    draw.rectangle([MARGIN, top - 36, MARGIN + 64, top - 30], fill=ACCENT)

    y = top
    for line in lines:
        draw.text((MARGIN, y), line, font=title_font, fill=INK)
        y += line_h

    footer_font = load_font(28, REGULAR_INDEX)
    draw.text((MARGIN, H - MARGIN - 28), "zguo0525.github.io",
              font=footer_font, fill=MUTED)

    img.save(out_path, optimize=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for md in sorted(ARTICLES.glob("*.md")):
        text = md.read_text()
        m = re.search(r'^title:\s*"?(.*?)"?\s*$', text, re.M)
        if not m:
            print(f"skip (no title): {md.name}")
            continue
        title = m.group(1)
        out = OUT / f"{md.stem}.png"
        make_card(title, out)
        print(f"wrote {out.relative_to(ROOT)}  ({title[:50]})")


if __name__ == "__main__":
    main()
