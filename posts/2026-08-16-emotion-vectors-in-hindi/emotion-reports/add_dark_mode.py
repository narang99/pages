#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""
Add dark-mode support to circuitsvis emotion-report HTML pages (and their
index.html pages).

Usage:
    uv run add_dark_mode.py report1.html report2.html ...
    uv run add_dark_mode.py emotion-reports/**/*.html
    uv run add_dark_mode.py --force report1.html   # re-apply even if already patched

Idempotent: running it twice on the same file is a no-op (detected via the
MARKER string below), unless --force is passed.

Why this works for the circuitsvis token spans specifically: circuitsvis
renders every token as a <span> with an *inline* style. Tokens with zero
activation get "background-color: rgb(255, 255, 255); color: black", while
activated tokens get their own heatmap color with an already-contrasting
text color (black or white) baked in by the library. So dark mode only needs
to repaint the *zero-activation* (pure white) spans -- everything else
already contrasts fine against a dark page background. We target those
spans with an attribute-substring selector on the literal inline style
string, overridden with !important since inline styles otherwise win.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

MARKER = "data-dark-mode-support"

DARK_STYLE_BLOCK = f"""    <style {MARKER}="1">
        @media (prefers-color-scheme: dark) {{
            body {{ background: #1e1e1e; color: #ddd; }}
            h1 {{ border-bottom-color: #555; color: #eee; }}
            h2 {{ color: #aaa; }}
            hr {{ border-top-color: #444; }}
            a {{ color: #6ea8fe; }}
            table {{ color: #ddd; }}
            th {{ background: #2a2a2a; }}
            th, td {{ border-bottom-color: #444; }}
            /* circuitsvis draws each token as a <span> with an inline style;
               only repaint the zero-activation (pure white) tokens -- colored
               tokens already carry a contrasting text color from the library */
            span[style*="background-color: rgb(255, 255, 255)"] {{
                background-color: #2b2b2b !important;
                color: #ccc !important;
                border-color: #444 !important;
            }}
        }}
    </style>
"""


def add_dark_mode(path: Path, force: bool = False) -> bool:
    """Returns True if the file was modified."""
    content = path.read_text(encoding="utf-8")

    if not force and MARKER in content:
        return False

    if force and MARKER in content:
        # strip the previously-inserted block before re-adding a fresh one
        start = content.find(f"    <style {MARKER}")
        end = content.find("</style>", start) + len("</style>") + 1
        content = content[:start] + content[end:]

    head_close = content.find("</head>")
    if head_close == -1:
        raise ValueError(f"no </head> tag found in {path}")

    content = content[:head_close] + DARK_STYLE_BLOCK + content[head_close:]
    path.write_text(content, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="+", type=Path, help="report HTML files to patch")
    parser.add_argument("--force", action="store_true", help="re-apply dark mode block even if already present")
    args = parser.parse_args()

    for path in args.files:
        if not path.exists():
            print(f"skip (not found): {path}", file=sys.stderr)
            continue
        changed = add_dark_mode(path, force=args.force)
        print(f"{'patched' if changed else 'already patched, skipped'}: {path}")


if __name__ == "__main__":
    main()
