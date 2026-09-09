#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated checks against the built site.

    python tests/check.py        or      make check

What it checks:
  1) internal links and anchors (#id) — nothing broken
  2) JavaScript errors on every page
  3) horizontal overflow at 4 widths (1440 / 1280 / 768 / 390)
  4) top-bar menus: hidden when closed, genuinely visible when open,
     and not running off the edge of the screen
  5) the top bar does not blow past its height

Note: check 4 deliberately measures the VISUAL state, not the JavaScript state.
The menu CSS once failed to reach a page, and because the test only asserted
class names, it passed anyway.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
WIDTHS = (1440, 1280, 768, 390)


def check_links():
    files = {os.path.basename(f) for f in glob.glob(os.path.join(DIST, "*.html"))}
    bad = []
    for name in sorted(files):
        s = open(os.path.join(DIST, name), encoding="utf-8").read()
        for h in set(re.findall(r'href="([^"]+)"', s)):
            if h.startswith(("http", "mailto:", "tel:")):
                continue
            if h.startswith("#"):
                if h != "#" and f'id="{h[1:]}"' not in s:
                    bad.append(f"{name} → {h} (anchor missing on this page)")
                continue
            target, _, anchor = h.partition("#")
            if target and target not in files:
                bad.append(f"{name} → {h} (file does not exist)")
                continue
            if anchor:
                t = open(os.path.join(DIST, target), encoding="utf-8").read()
                if f'id="{anchor}"' not in t:
                    bad.append(f"{name} → {h} (anchor missing on target page)")
    return bad


def check_render():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("… playwright is not installed; only links were checked.")
        print("   install:  pip install playwright && playwright install chromium")
        return []
    pages = sorted(os.path.basename(f) for f in glob.glob(os.path.join(DIST, "*.html")))
    bad = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for f in pages:
            for w in WIDTHS:
                pg = b.new_page(viewport={"width": w, "height": 900})
                errs = []
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.goto("file://" + os.path.join(DIST, f))
                pg.wait_for_timeout(700)
                if pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth+1"):
                    bad.append(f"{f} @{w}px — horizontal overflow")
                navh = pg.evaluate("Math.round(document.querySelector('.nav').getBoundingClientRect().height)")
                if navh > 84:
                    bad.append(f"{f} @{w}px — top bar broke (height {navh})")
                if errs:
                    bad.append(f"{f} @{w}px — JS error: {errs[0][:90]}")
                if w == 1280:
                    bad += _check_menus(pg, f)
                pg.close()
        b.close()
    return bad


def _check_menus(pg, f):
    """Measures the menus visually, not just by CSS class."""
    out = []
    for mid in pg.evaluate("[...document.querySelectorAll('.has-menu')].map(e=>e.id)"):
        panel = f"#mm-{mid}"
        st = pg.evaluate(f"""(()=>{{const g=getComputedStyle(document.querySelector('{panel}'));
            return g.visibility+'|'+g.opacity+'|'+g.position}})()""")
        if st != "hidden|0|absolute":
            out.append(f"{f} — menu {mid} is not hidden when closed ({st})")
        pg.hover(f"#{mid} .navbtn")
        pg.wait_for_timeout(380)
        o = pg.evaluate(f"""(()=>{{const m=document.querySelector('{panel}'),g=getComputedStyle(m),
            r=m.getBoundingClientRect(), li=document.getElementById('{mid}').getBoundingClientRect();
            return {{v:g.visibility,o:parseFloat(g.opacity),w:Math.round(r.width),h:Math.round(r.height),
                     drops:r.top>li.bottom, onscreen:r.left>=0&&r.right<=innerWidth}}}})()""")
        if not (o["v"] == "visible" and o["o"] > .9 and o["w"] >= 180 and o["h"] >= 120
                and o["drops"] and o["onscreen"]):
            out.append(f"{f} — menu {mid} does not open correctly: {o}")
        pg.mouse.move(5, 400)
        pg.wait_for_timeout(250)
    return out


def main():
    if not os.path.isdir(DIST):
        print("✗ dist/ does not exist. Run `make build` first."); sys.exit(1)
    problems = check_links() + check_render()
    n = len(glob.glob(os.path.join(DIST, "*.html")))
    if problems:
        print(f"\n✗ found {len(problems)} problem(s):\n")
        for p in problems:
            print("  •", p)
        sys.exit(1)
    print(f"✓ {n} pages — links, render, overflow and menus all healthy")


if __name__ == "__main__":
    main()
