#!/usr/bin/env python3
"""Generate 1200x630 Open Graph card images for essays in _articles/.

Cards deliberately keep the light card palette and Charter (second font in
the site's serif stack) used by the committed cards in assets/cards/, so a
new card matches the existing ones. They do not follow the site's dark theme.

Generate the card for a new essay only (existing cards are left untouched):

    python3 scripts/gen_og_cards.py <slug>

With no slug, every essay's card is regenerated (overwrites assets/cards/).
Use --out DIR to write somewhere else (e.g. /tmp) for a preview.

Charter is read from the macOS system font by default. Elsewhere, pass
--font-regular/--font-bold, but note a different font changes the look, so
do not commit cards rendered that way alongside the Charter ones.

Each article's front matter should point at its card:

    image: /assets/cards/<slug>.png
"""

import argparse
import json
import re
import sys
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

# (path, face index) for each weight; replaced by --font-regular/--font-bold
FONTS = {REGULAR_INDEX: (CHARTER, REGULAR_INDEX), BOLD_INDEX: (CHARTER, BOLD_INDEX)}


def load_font(size, index):
    path, face = FONTS[index]
    return ImageFont.truetype(path, size, index=face)


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


def read_title(text):
    """Return the front-matter title, or None. Only the front matter is read."""
    m = re.match(r"---\s*\n(.*?)\n---\s*(\n|$)", text, re.S)
    if not m:
        return None
    front = m.group(1)
    try:
        import yaml
    except ImportError:
        yaml = None
    if yaml is not None:
        title = (yaml.safe_load(front) or {}).get("title")
        return str(title) if title is not None else None
    # Fallback without PyYAML: single-line `title:` scalars only.
    t = re.search(r"^title:[ \t]*(.*?)[ \t]*$", front, re.M)
    if not t or not t.group(1):
        return None
    raw = t.group(1)
    if raw.startswith('"'):
        return json.loads(raw)  # YAML double-quoted escapes match JSON's
    if raw.startswith("'"):
        return raw[1:-1].replace("''", "'")
    return re.sub(r"\s+#.*$", "", raw)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("slugs", nargs="*",
                    help="article slugs to render (default: all)")
    ap.add_argument("--out", type=Path, default=OUT,
                    help="output directory (default: assets/cards)")
    ap.add_argument("--font-regular", help="regular font file (default: Charter)")
    ap.add_argument("--font-bold", help="bold font file (default: Charter)")
    args = ap.parse_args()

    if bool(args.font_regular) != bool(args.font_bold):
        ap.error("pass both --font-regular and --font-bold, or neither")
    if args.font_regular:
        FONTS[REGULAR_INDEX] = (args.font_regular, 0)
        FONTS[BOLD_INDEX] = (args.font_bold, 0)
    for path, _ in FONTS.values():
        if not Path(path).is_file():
            sys.exit(f"font not found: {path}\n"
                     "Charter ships with macOS; elsewhere pass "
                     "--font-regular/--font-bold (the cards will look different).")

    if args.slugs:
        mds = [ARTICLES / f"{s}.md" for s in args.slugs]
        missing = [str(p.relative_to(ROOT)) for p in mds if not p.is_file()]
        if missing:
            sys.exit("no such article: " + ", ".join(missing))
    else:
        mds = sorted(ARTICLES.glob("*.md"))

    args.out.mkdir(parents=True, exist_ok=True)
    for md in mds:
        title = read_title(md.read_text(encoding="utf-8"))
        if not title:
            print(f"skip (no title): {md.name}")
            continue
        out = args.out / f"{md.stem}.png"
        make_card(title, out)
        print(f"wrote {out}  ({title[:50]})")


if __name__ == "__main__":
    main()
