#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated checks against the built site.

    python tests/check.py        or      make check

What it checks:
  1) internal links and anchors (#id) — nothing broken
  1b) one address per page: the clean URL, the canonical tag and the sitemap
      all agree, and nothing still links to the .html form
  2) JavaScript errors on every page
  3) horizontal overflow at 4 widths (1440 / 1280 / 768 / 390)
  4) top-bar menus: hidden when closed, genuinely visible when open,
     and not running off the edge of the screen
  5) the top bar does not blow past its height
  6) the sticky bars (header, ticker, sub-nav) stack flush at every width

Note: check 4 deliberately measures the VISUAL state, not the JavaScript state.
The menu CSS once failed to reach a page, and because the test only asserted
class names, it passed anyway.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
WIDTHS = (1440, 1280, 768, 390)


def _resolve(href, files):
    """A link as written → the file that must exist, the way the server sees it.

    The site links to clean addresses (/wiki, and / for the home page) while
    the files on disk are still wiki.html and index.html. Without this the
    checker would call every single link broken — or, worse, be loosened
    until it stopped catching real ones.
    """
    if href in ("/", ""):
        return "index.html"
    t = href[1:] if href.startswith("/") else href
    if t in files:
        return t
    if t + ".html" in files:
        return t + ".html"
    return None


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
            resolved = _resolve(target, files)
            if resolved is None:
                bad.append(f"{name} → {h} (no page at this address)")
                continue
            if anchor:
                t = open(os.path.join(DIST, resolved), encoding="utf-8").read()
                if f'id="{anchor}"' not in t:
                    bad.append(f"{name} → {h} (anchor missing on target page)")
    return bad


def check_urls():
    """Every page must link to, and declare, exactly one address for itself."""
    import sys as _s
    _s.path.insert(0, os.path.join(ROOT, "site"))
    _s.dont_write_bytecode = True
    import config as C
    bad = []
    for key, fname in C.PAGES.items():
        page = os.path.join(DIST, fname)
        if not os.path.exists(page):
            bad.append("%s is in config.PAGES but was not built" % fname)
            continue
        html = open(page, encoding="utf-8").read()
        want = "/" if fname == "index.html" else "/" + fname[:-5]
        if not C.CLEAN_URLS:
            want = fname
        if 'rel="canonical" href="https://%s%s"' % (C.BRAND["domain"], want) not in html:
            bad.append("%s — canonical does not point at %s" % (fname, want))
        if C.CLEAN_URLS and 'href="%s"' % fname in html:
            bad.append("%s — still links to %s instead of the clean address"
                       % (fname, fname))
    sm = os.path.join(DIST, "sitemap.xml")
    if os.path.exists(sm):
        x = open(sm, encoding="utf-8").read()
        for fname in C.PAGES.values():
            want = "/" if fname == "index.html" else "/" + fname[:-5]
            if C.CLEAN_URLS and ("<loc>https://%s%s</loc>" % (C.BRAND["domain"], want)) not in x:
                bad.append("sitemap.xml is missing %s" % want)
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
                bad += _check_sticky(pg, f, w)
                if w == 1280:
                    bad += _check_menus(pg, f)
                pg.close()
        b.close()
    return bad


def _check_sticky(pg, f, w):
    """The sticky bars must stack flush at every width.

    The header, the price ticker and the in-page sub-nav all pin to the top.
    They used to do it with hard-coded offsets (top:59px, top:101px, and a
    top:99px override under 900px), so any change to the bar's real height —
    a longer menu label, a different font, a breakpoint — left the ticker
    bleeding through the header on scroll. Measured, not assumed.
    """
    out = []
    pg.evaluate("scrollTo(0,1600)")
    pg.wait_for_timeout(220)
    r = pg.evaluate("""(()=>{const q=s=>document.querySelector(s);
        const t=q('.topbar'),h=q('header'),k=q('.ticker'),s=q('.subnav');
        if(!t) return null;
        const T=t.getBoundingClientRect();
        const o={top:Math.round(T.top),
                 tickerGap:k?Math.round(k.getBoundingClientRect().top-h.getBoundingClientRect().bottom):0};
        if(s) o.subGap=Math.round(s.getBoundingClientRect().top-T.bottom);
        return o})()""")
    pg.evaluate("scrollTo(0,0)")
    if r is None:
        return ["%s @%dpx — .topbar is missing" % (f, w)]
    if r["top"] != 0:
        out.append("%s @%dpx — the top bar did not stick (top %d)" % (f, w, r["top"]))
    if r["tickerGap"] != 0:
        out.append("%s @%dpx — a %dpx gap between the header and the ticker"
                   % (f, w, r["tickerGap"]))
    if "subGap" in r and r["subGap"] != 0:
        out.append("%s @%dpx — the sub-nav is %dpx out of line with the top bar"
                   % (f, w, r["subGap"]))
    return out


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
    problems = check_links() + check_urls() + check_render()
    n = len(glob.glob(os.path.join(DIST, "*.html")))
    if problems:
        print(f"\n✗ found {len(problems)} problem(s):\n")
        for p in problems:
            print("  •", p)
        sys.exit(1)
    print(f"✓ {n} pages — links, render, overflow and menus all healthy")


if __name__ == "__main__":
    main()
