#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
بررسی خودکار سایت ساخته‌شده.

    python tests/check.py        یا      make check

چه چیزی را چک می‌کند:
  ۱) لینک‌های داخلی و لنگرها (#id) — هیچ لینک شکسته‌ای نباشد
  ۲) خطای JavaScript در هر صفحه
  ۳) سرریز افقی در ۴ عرض مختلف (۱۴۴۰ / ۱۲۸۰ / ۷۶۸ / ۳۹۰)
  ۴) منوهای نوار بالا: بسته پنهان باشند، باز واقعاً دیده شوند و از صفحه بیرون نزنند
  ۵) ارتفاع نوار بالا نشکند

نکته: بند ۴ عمداً «وضعیت بصری» را می‌سنجد نه وضعیت JavaScript.
یک بار استایل منو به یک صفحه نرسید و چون فقط کلاس‌ها تست می‌شد، لو نرفت.
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
                    bad.append(f"{name} → {h} (لنگر داخل همین صفحه نیست)")
                continue
            target, _, anchor = h.partition("#")
            if target and target not in files:
                bad.append(f"{name} → {h} (فایل وجود ندارد)")
                continue
            if anchor:
                t = open(os.path.join(DIST, target), encoding="utf-8").read()
                if f'id="{anchor}"' not in t:
                    bad.append(f"{name} → {h} (لنگر در صفحه مقصد نیست)")
    return bad


def check_render():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("… playwright نصب نیست؛ فقط لینک‌ها بررسی شد.")
        print("   نصب:  pip install playwright && playwright install chromium")
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
                    bad.append(f"{f} @{w}px — سرریز افقی")
                navh = pg.evaluate("Math.round(document.querySelector('.nav').getBoundingClientRect().height)")
                if navh > 84:
                    bad.append(f"{f} @{w}px — نوار بالا شکسته (ارتفاع {navh})")
                if errs:
                    bad.append(f"{f} @{w}px — خطای JS: {errs[0][:90]}")
                if w == 1280:
                    bad += _check_menus(pg, f)
                pg.close()
        b.close()
    return bad


def _check_menus(pg, f):
    """منوها را بصری می‌سنجد، نه فقط با کلاس CSS."""
    out = []
    for mid in pg.evaluate("[...document.querySelectorAll('.has-menu')].map(e=>e.id)"):
        panel = f"#mm-{mid}"
        st = pg.evaluate(f"""(()=>{{const g=getComputedStyle(document.querySelector('{panel}'));
            return g.visibility+'|'+g.opacity+'|'+g.position}})()""")
        if st != "hidden|0|absolute":
            out.append(f"{f} — منوی {mid} در حالت بسته پنهان نیست ({st})")
        pg.hover(f"#{mid} .navbtn")
        pg.wait_for_timeout(380)
        o = pg.evaluate(f"""(()=>{{const m=document.querySelector('{panel}'),g=getComputedStyle(m),
            r=m.getBoundingClientRect(), li=document.getElementById('{mid}').getBoundingClientRect();
            return {{v:g.visibility,o:parseFloat(g.opacity),w:Math.round(r.width),h:Math.round(r.height),
                     drops:r.top>li.bottom, onscreen:r.left>=0&&r.right<=innerWidth}}}})()""")
        if not (o["v"] == "visible" and o["o"] > .9 and o["w"] >= 180 and o["h"] >= 120
                and o["drops"] and o["onscreen"]):
            out.append(f"{f} — منوی {mid} درست باز نمی‌شود: {o}")
        pg.mouse.move(5, 400)
        pg.wait_for_timeout(250)
    return out


def main():
    if not os.path.isdir(DIST):
        print("✗ پوشه dist/ وجود ندارد. اول `make build` بزنید."); sys.exit(1)
    problems = check_links() + check_render()
    n = len(glob.glob(os.path.join(DIST, "*.html")))
    if problems:
        print(f"\n✗ {len(problems)} مشکل پیدا شد:\n")
        for p in problems:
            print("  •", p)
        sys.exit(1)
    print(f"✓ {n} صفحه — لینک‌ها، رندر، سرریز و منوها همه سالم")


if __name__ == "__main__":
    main()
