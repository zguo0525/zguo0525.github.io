#!/usr/bin/env python3
"""Standardize paper-card thumbnails from real paper figures.

Each source figure in assets/papers/ gets a controlled crop (drop captions,
keep the most readable region), a slight saturation trim, and is centered on
a neutral warm matte at a uniform 16:9. Output: assets/papers/cards/.

    python3 scripts/gen_paper_thumbs.py
"""

from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "papers"
OUT = SRC / "cards"

W, H = 1200, 675          # uniform 16:9 card
MATTE_LIGHT = (246, 243, 236)  # neutral warm ground, sits on both themes
FIGURE_BOX = 0.86         # figure occupies at most this fraction of the card

# name -> (left, top, right, bottom) crop of the source, or None for full frame
CROPS = {
    # keep the two right-hand 3-shot charts; drop the caption text
    "api-pack": (400, 0, 800, 138),
    # Algorithm 1 header + first procedure block reads as clean pseudocode
    "authentigpt": (0, 0, 800, 260),
    # full chart is already clean
    "jetmoe": None,
    # full pipeline diagram
    "synthetic-data-rl": None,
}


def make_thumb(name, crop):
    im = Image.open(SRC / f"{name}.png").convert("RGBA")
    if crop:
        im = im.crop(crop)

    max_w, max_h = int(W * FIGURE_BOX), int(H * FIGURE_BOX)
    scale = min(max_w / im.width, max_h / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)),
                   Image.Resampling.LANCZOS)

    card = Image.new("RGBA", (W, H), MATTE_LIGHT + (255,))
    card.alpha_composite(im, ((W - im.width) // 2, (H - im.height) // 2))
    card = ImageEnhance.Color(card.convert("RGB")).enhance(0.9)
    card.save(OUT / f"{name}.png", optimize=True)
    print(f"wrote assets/papers/cards/{name}.png")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, crop in CROPS.items():
        make_thumb(name, crop)


if __name__ == "__main__":
    main()
