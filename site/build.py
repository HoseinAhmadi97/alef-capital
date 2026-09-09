#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the whole site into dist/.

    python site/build.py          or      make build

Every page is one row in SITE below. To add a new page:
  1) write its content in site/pages/<something>.py
  2) add its key to config.PAGES
  3) add one row here
"""
import io, os, shutil, sys, time

sys.dont_write_bytecode = True   # keeps a stale config from being cached

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "pages"))

import config as C
import layout as L
import product_gold, product_covered_call, dashboards, pricing, market, misc_a, misc_b

DIST = os.path.join(ROOT, "dist")

# key ─ title ─ meta description ─ body HTML ─ page JS
SITE = [
    ("home", "الف کپیتال — داشبورد آربیتراژ صندوق طلا و کاوردکال بورس تهران",
     "پایش لحظه‌ای حباب صندوق‌های طلا و فرصت‌های کاوردکال. دو داشبورد تخصصی برای کسب بازده کم‌ریسک.",
     None, None),  # ← home page comes from home.py (substituted below)

    ("dgold", "داشبورد آربیتراژ صندوق طلا | الف کپیتال",
     "حباب، ارزش ذاتی و ترکیب دارایی ۳۰ صندوق طلای بورس تهران. نسخه مهمان رایگان.",
     dashboards.GOLD, dashboards.GOLD_JS),

    ("dcc", "داشبورد کاوردکال | الف کپیتال",
     "دیدبان قراردادهای اختیار خرید با نرخ معادل سالانه و حاشیه ریسک. نسخه مهمان رایگان.",
     dashboards.CC, dashboards.CC_JS),

    ("gold", "داشبورد آربیتراژ صندوق‌های طلا | الف کپیتال",
     "حباب و NAV همه صندوق‌های طلای بورس تهران، لحظه‌ای. شناسایی صندوق ارزنده بر پایه ترکیب دارایی.",
     product_gold.HTML, product_gold.JS),

    ("cc", "داشبورد کاوردکال — بهره ثابت سالانه | الف کپیتال",
     "دیدبان قراردادهای اختیار خرید با نرخ سود معادل سالانه و حاشیه ریسک محاسبه‌شده.",
     product_covered_call.HTML, product_covered_call.JS),

    ("pricing", "پلن‌ها و قیمت اشتراک | الف کپیتال",
     "سه پلن با پرداخت ماهانه، سه‌ماهه یا سالانه. ۷ روز رایگان بدون کارت بانکی.",
     pricing.HTML, pricing.JS),

    ("market", "نبض بازار طلا — حباب لحظه‌ای صندوق‌ها | الف کپیتال",
     "جدول زنده حباب و NAV صندوق‌های طلای بورس تهران، قیمت طلای ۱۸ عیار، سکه و اونس جهانی. رایگان.",
     market.HTML, market.JS),

    ("perf", "گزارش عملکرد الگوریتم | الف کپیتال",
     "بازده استراتژی آربیتراژ در برابر نگهداری ساده صندوق طلا، با روش‌شناسی و محدودیت‌های شفاف.",
     misc_a.PERF, misc_a.PERF_JS),

    ("services", "مدیریت پرتفوی و اجرای الگوریتم | الف کپیتال",
     "اجرای خودکار الگوریتم آربیتراژ طلا و کاوردکال روی حساب کارگزاری شما. سه مدل ارائه.",
     misc_a.SERVICES, ""),

    ("wiki", "دانشنامه صندوق طلا، آربیتراژ و اختیار معامله | الف کپیتال",
     "مرجع آموزشی حباب، NAV، آربیتراژ و کاوردکال با مثال عددی و داده واقعی بازار ایران.",
     misc_a.WIKI, ""),

    ("about", "درباره ما | الف کپیتال",
     "تیمی از دانشگاه پشت یک الگوریتم — داستان، اصول و مسیر الف کپیتال.",
     misc_a.ABOUT, ""),

    ("faq", "سوالات متداول | الف کپیتال",
     "پاسخ سوالات رایج درباره محصول، داده، اشتراک و ریسک.",
     misc_a.FAQ, ""),

    ("contact", "تماس با ما | الف کپیتال",
     "تلفن، ایمیل و فرم درخواست تماس الف کپیتال.",
     misc_a.CONTACT, ""),

    ("article", "کاوردکال چیست؟ راهنمای کامل با مثال عددی | الف کپیتال",
     "فرمول نرخ معادل سالانه، حاشیه ریسک و نقطه سربه‌سری با مثال عددی و ماشین‌حساب تعاملی.",
     misc_b.ARTICLE, misc_b.ARTICLE_JS),

    ("calc", "ماشین‌حساب کاوردکال — نرخ معادل سالانه | الف کپیتال",
     "نرخ سود معادل سالانه، حاشیه ریسک و نقطه سربه‌سری هر موقعیت کاوردکال را رایگان محاسبه کنید.",
     misc_b.CALC, misc_b.CALC_JS),

    ("risk", "افشای ریسک | الف کپیتال", "افشای کامل ریسک‌های استفاده از خدمات الف کپیتال.",
     misc_b.legal("افشای ریسک", "افشای ریسک", misc_b.RISK_BODY), ""),
    ("terms", "شرایط استفاده | الف کپیتال", "شرایط و ضوابط استفاده از خدمات الف کپیتال.",
     misc_b.legal("شرایط استفاده", "شرایط استفاده", misc_b.TERMS_BODY), ""),
    ("privacy", "حریم خصوصی | الف کپیتال", "سیاست حریم خصوصی و نحوه نگهداری داده کاربران.",
     misc_b.legal("حریم خصوصی", "حریم خصوصی", misc_b.PRIVACY_BODY), ""),
]


def build():
    import home  # noqa: after sys.path setup
    t0 = time.time()
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    n = 0
    for key, title, desc, body, js in SITE:
        if key == "home":
            body, js = home.HTML, home.JS
        html = L.page(title, desc, key, body, js or "")
        out = os.path.join(DIST, C.PAGES[key])
        io.open(out, "w", encoding="utf-8").write(html)
        n += 1

    # static files (fonts, images) copied verbatim into dist/
    static = os.path.join(HERE, "static")
    if os.path.isdir(static):
        for item in os.listdir(static):
            s = os.path.join(static, item)
            d = os.path.join(DIST, item)
            shutil.copytree(s, d) if os.path.isdir(s) else shutil.copy2(s, d)

    _write_seo()
    print(f"✓ built {n} pages into dist/  ({time.time()-t0:.2f}s)")


def _write_seo():
    base = f"https://{C.BRAND['domain']}"
    urls = "\n".join(
        f"  <url><loc>{base}/{f if f != 'index.html' else ''}</loc></url>"
        for f in C.PAGES.values())
    io.open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    io.open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n")


if __name__ == "__main__":
    build()
