# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════╗
║  Site settings — the things that change most often               ║
║                                                                  ║
║  To change the brand name, phone, plan prices or menu items,     ║
║  edit ONLY this file and run `make build`.                       ║
╚══════════════════════════════════════════════════════════════════╝

Note: the values below are the website's own copy, so they stay in Persian.
Only the comments are English.
"""
import glob
import os

# ─────────────────────────── Brand & contact ───────────────────────
BRAND = {
    "name":     "الف کپیتال",
    "domain":   "alefcapital.ir",
    "phone":    "۰۲۱-۹۱۰۰۱۲۳۴",
    "phone_ltr": "+982191001234",      # used by href="tel:"
    "email":    "info@alefcapital.ir",
    "telegram": "@alefcapital",
    "address":  "{{ نشانی کامل }}",
    "reg_no":   "{{ شماره ثبت }}",
    "nat_id":   "{{ شناسه ملی }}",
    "year":     "۱۴۰۴",
    "tagline":  "پایش لحظه‌ای حباب صندوق‌های طلا و فرصت‌های کاوردکال بورس تهران.",
}

# ─────────────────────────── Page map ──────────────────────────────
# key = the name used in code, value = the output file name
PAGES = {
    "home":     "index.html",
    "dgold":    "dashboard-gold.html",
    "dcc":      "dashboard-covered-call.html",
    "gold":     "product-gold.html",
    "cc":       "product-covered-call.html",
    "pricing":  "pricing.html",
    "market":   "market.html",
    "perf":     "performance.html",
    "services": "services.html",
    "wiki":     "wiki.html",
    "article":  "wiki-covered-call.html",
    "calc":     "tools-covered-call.html",
    "about":    "about.html",
    "faq":      "faq.html",
    "contact":  "contact.html",
    "risk":     "legal-risk.html",
    "terms":    "legal-terms.html",
    "privacy":  "legal-privacy.html",
}

# ─────────────────────────── Top navigation ────────────────────────
# To add / remove / reorder menu items, change only this structure.
#   ("link",  label, page key)
#   ("mega",  label, id, columns, promo card)      ← mega menu
#   ("mini",  label, id, items)                    ← small dropdown
NAV = [
    ("mega", "محصولات", "pmenu", [
        ("داشبوردها", [
            ("g", "🪙", "داشبورد طلا", "حباب، NAV و ترکیب دارایی ۳۰ صندوق طلا", "dgold", "معرفی محصول ←"),
            ("b", "📈", "داشبورد کاوردکال", "دیدبان اختیار خرید با نرخ معادل سالانه و حاشیه ریسک", "dcc", "معرفی محصول ←"),
        ]),
        ("خدمات و ابزار", [
            ("n", "📈", "مدیریت پرتفوی", "اجرای الگوریتم روی حساب کارگزاری شما", "services", ""),
            ("n", "🧮", "ماشین‌حساب کاوردکال", "نرخ معادل سالانه و نقطه سربه‌سری — رایگان", "calc", ""),
        ]),
    ], ("۷ روز رایگان", "بدون نیاز به کارت بانکی. هر زمان بخواهید لغو کنید.", "شروع کنید ←", "pricing")),

    ("link", "بازار",       "market"),
    ("link", "قیمت‌گذاری",  "pricing"),
    ("link", "دانشنامه",    "wiki"),

    ("mini", "درباره ما", "amenu", [
        ("🏛",  "درباره الف کپیتال", "about"),
        ("✉️", "تماس با ما",        "contact"),
        ("❓",  "سوالات متداول",     "faq"),
        ("--", "", ""),                       # separator
        ("📊", "گزارش عملکرد",       "perf"),
    ]),
]

# Buttons on the left of the top bar — (label, page key, css class, anchor)
NAV_CTA = [
    ("مشاوره رایگان",  "services", "btn btn-s btn-consult", "#lead"),
    ("ورود / ثبت‌نام", "pricing",  "btn btn-p",             ""),
]

# Which menu item is highlighted as "active" on which page
NAV_ACTIVE_GROUP = {
    "about": "amenu", "contact": "amenu", "faq": "amenu", "perf": "amenu",
    "gold": "pmenu", "cc": "pmenu", "dgold": "pmenu", "dcc": "pmenu",
    "services": "pmenu", "calc": "pmenu",
}

# ─────────────────────────── Footer ────────────────────────────────
FOOTER = [
    ("محصولات", [("داشبورد طلا","dgold"), ("داشبورد کاوردکال","dcc"),
                 ("معرفی آربیتراژ طلا","gold"), ("معرفی کاوردکال","cc"),
                 ("نبض بازار","market"), ("مدیریت پرتفوی","services")]),
    ("منابع",   [("دانشنامه","wiki"), ("ماشین‌حساب کاوردکال","calc"),
                 ("گزارش عملکرد","perf"), ("پلن‌ها و قیمت","pricing")]),
    ("شرکت",    [("درباره ما","about"), ("تماس با ما","contact"), ("سوالات متداول","faq")]),
    ("قوانین",  [("شرایط استفاده","terms"), ("حریم خصوصی","privacy"), ("افشای ریسک","risk")]),
]

# Mobile bottom bar — (icon, label, page key)
BOTTOM_NAV = [
    ("🏠", "خانه",      "home"),
    ("📊", "بازار",     "market"),
    ("🧩", "داشبورد",   "dgold"),
    ("📚", "دانشنامه",  "wiki"),
    ("👤", "حساب من",   "pricing"),
]

# ─────────────────────────── Plan prices ───────────────────────────
# Change only these numbers; the pricing page and its period toggle follow.
PRICING = {
    "monthly":   {"gold": "۱,۹۰۰,۰۰۰", "pro": "۳,۹۰۰,۰۰۰", "note": "ماهانه"},
    "quarterly": {"gold": "۱,۶۱۵,۰۰۰", "pro": "۳,۳۱۵,۰۰۰", "note": "ماهانه، با پرداخت ۳ ماهه (۱۵٪ تخفیف)"},
    "yearly":    {"gold": "۱,۳۳۰,۰۰۰", "pro": "۲,۷۳۰,۰۰۰", "note": "ماهانه، با پرداخت سالانه (۳۰٪ تخفیف)"},
}

# ─────────────────────────── Price ticker ──────────────────────────
# Until the API is wired up, these are the numbers that get displayed.
TICKER = [
    ("طلای ۱۸ عیار",    182257000, -0.14),
    ("مثقال طلا",       789500000, -0.14),
    ("گواهی شمش",       23900550,  -1.79),
    ("گواهی سکه",       1816000000, 1.94),
    ("سکه امامی",       1826000000, 2.50),
    ("اونس جهانی",      4005,       0.00),
    ("دلار",            189000,     0.00),
    ("شاخص صندوق طلا",  23418,      0.62),
]

# ─────────────────────────── Repeated copy ─────────────────────────
RISK_SHORT = ("اطلاعات ارائه‌شده در این وب‌سایت صرفاً جنبه تحلیلی و اطلاع‌رسانی دارد و توصیه به خرید "
              "یا فروش هیچ اوراق بهاداری محسوب نمی‌شود. سرمایه‌گذاری در بازار سرمایه با ریسک همراه است "
              "و مسئولیت تصمیم‌های معاملاتی بر عهده کاربر است. بازده گذشته تضمینی برای بازده آینده نیست.")

# ─────────────────────────── Paywall ───────────────────────────────
# False = every dashboard column, row and tool is open to every visitor.
# True  = the computed columns sit behind sign-up (the launch behaviour).
#
# This is the ONLY switch. The markup keeps both variants, so flipping this
# back once the site has traffic needs no edits anywhere else.
PAYWALL = False

# ─────────────────────────── Font ──────────────────────────────────
# Google Fonts is fine for local development but slow or blocked for Iranian
# users, so production serves Vazirmatn from /assets/fonts instead.
#
# This resolves itself — do NOT edit this file on the server:
#   • run `make fonts` and the woff2 files appear → self-hosted automatically
#   • no font files (a plain laptop checkout)     → Google Fonts
#   • force either way with the environment variable:
#       ALEF_SELF_HOSTED_FONT=1   or   ALEF_SELF_HOSTED_FONT=0
#
# Editing this as a local change is what used to make `git pull` fail on the
# server with "local changes would be overwritten".
_FONT_ENV = os.environ.get("ALEF_SELF_HOSTED_FONT")
if _FONT_ENV is not None:
    SELF_HOSTED_FONT = _FONT_ENV.strip().lower() in ("1", "true", "yes", "on")
else:
    SELF_HOSTED_FONT = bool(glob.glob(
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "static", "assets", "fonts", "*.woff2")))
