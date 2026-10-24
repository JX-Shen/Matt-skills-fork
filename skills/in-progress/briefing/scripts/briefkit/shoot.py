"""Screenshot a briefkit gh page and split into readable slices.

Usage:
    python shoot.py out/work.gh.html
    python shoot.py out/work.gh.html --slice 1800 --out /path/to/dir

Passes --virtual-time-budget=8000 to the browser so Mermaid loaded from a CDN
has time to render before the screenshot is taken. Splits the full-page capture
into vertical slices of --slice pixels (default 1800) so every slice is
readable without scrolling. Lists the slice paths on stdout.

Needs Pillow (already installed with briefkit) and a Chromium-based browser
(Brave, Chrome or Chromium).
"""

import argparse
import os
import subprocess
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("shoot.py needs Pillow: uv pip install pillow")


_BROWSERS = [
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]


def _find_browser():
    for path in _BROWSERS:
        if os.path.exists(path):
            return path
    raise FileNotFoundError(
        "No Chromium-based browser found under /Applications. "
        "Install Brave, Chrome or Chromium and re-run."
    )


def shoot(html_path, slice_height=1800, out_dir=None):
    """Screenshot html_path and return a list of slice PNG paths."""
    html_path = os.path.abspath(html_path)
    if out_dir is None:
        out_dir = os.path.join(os.path.dirname(html_path), "shoot")
    os.makedirs(out_dir, exist_ok=True)

    browser = _find_browser()
    full_png = os.path.join(out_dir, "_full.png")

    subprocess.run(
        [
            browser,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1000,10000",
            "--virtual-time-budget=8000",
            f"--screenshot={full_png}",
            f"file://{html_path}",
        ],
        check=True,
        capture_output=True,
    )

    img = Image.open(full_png)
    width, height = img.size
    slices = []
    top = 0
    idx = 1
    while top < height:
        bottom = min(top + slice_height, height)
        crop = img.crop((0, top, width, bottom))
        name = f"p{idx:02d}.png"
        dest = os.path.join(out_dir, name)
        crop.save(dest)
        slices.append(dest)
        top = bottom
        idx += 1

    os.remove(full_png)
    return slices


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Screenshot a briefkit gh page, wait for Mermaid, split into slices."
    )
    ap.add_argument("html", help="Path to the .gh.html file")
    ap.add_argument(
        "--slice",
        type=int,
        default=1800,
        metavar="PX",
        help="Slice height in pixels (default 1800)",
    )
    ap.add_argument(
        "--out",
        default=None,
        metavar="DIR",
        help="Output directory (default: shoot/ beside the html file)",
    )
    args = ap.parse_args(argv)

    slices = shoot(args.html, slice_height=args.slice, out_dir=args.out)
    print(f"{len(slices)} slice(s) written:")
    for p in slices:
        print(f"  {p}")


if __name__ == "__main__":
    main()
