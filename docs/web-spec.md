# Alef Capital Website Design Specification — Version 2

> **This document is written to be handed directly to an AI development model.**
> Input: the first version of the "Gold Fund Landing Page" (Arca Landing) + the "Financial Products Introduction" document.
> Expected output: a multi-page, Persian/RTL website with two subscription products and a complete pricing page.

---

## 0. Executive Summary

The current version is a **single-product landing page** built for lead capture (a free-consultation form). The goal of version 2 is to turn it into a **product-led platform with a subscription revenue model**:

| | V1 (current) | V2 (target) |
|---|---|---|
| Business model | Lead capture → phone call | SaaS subscription + enterprise lead capture |
| Product | One arbitrage algorithm | Two financial dashboards + execution services |
| Pages | 5 static pages | 20+ routes (public + knowledge base + user account) |
| Primary CTA | «مشاوره رایگان بگیر» (Get a free consultation) | «شروع رایگان» (Start free) / «خرید اشتراک» (Buy subscription) |
| Proof of claims | Copy + one chart | Free live data, dashboard samples, auditable performance |
| Content | None | A categorized knowledge base — the organic acquisition engine |

**Five key structural changes:**

1. **From "landing page" to "product hub"** — the home page acts as a control room (the Bambo pattern): within 10 seconds the user understands how many products exist, what each one does, and where to start.
2. **Add a subscription layer** — a pricing page with three plans and a billing-period toggle (the Rahavard pattern), plus the sign-up / payment / account routes.
3. **Add a free-data layer** — part of the data (fund bubbles, spot prices, the gold market pulse) is available without registration (the Optionbaaz pattern). This is simultaneously an SEO engine, a reason for users to return daily, and proof of data quality.
4. **Add a content layer** — a categorized knowledge base instead of a time-ordered blog; every article links to a product (Section 8).
5. **Add an institutional-trust layer** — licenses, team, audited performance, risk disclosure (the Toranj / portfolio-manager pattern). In Iranian finance this layer is a **precondition for conversion**, not decoration.

---

## 1. Reference Site Analysis — What We Take From Each

### 1-1. Bambo (bambo.fund) — the "product ecosystem" pattern

Bambo's home page structure is exactly what version 2 needs. Its section order:

1. **Glass header + mobile bottom bar** (bottom nav with 5 items — an app-like pattern)
2. **Hero** with: a live badge (`نمای بازار امروز / زنده` — today's market view / live), a main headline, a paragraph, two CTAs (`شروع رایگان` — start free + `کشف امکانات` — explore features), and **small data cards beside the hero** (`اختیار معامله +۱۲.۴٪`, `طلا +۳.۸٪`, `صندوق‌ها +۷.۱٪`)
3. **A three-item stat bar** (`۴ بازار کلیدی` / `۱۰۰K+ تحلیل` / `۲۴/۷ همراهی`)
4. **Ecosystem grid** — 6 product cards with an icon, a title, a one-line description, and an arrow
5. **Three-step process** (`۰۱ رصد کنید` → `۰۲ سناریو بسازید` → `۰۳ اجرا کنید` — monitor / build a scenario / execute)
6. **Trust and credibility** — a user testimonial + 4 key figures + 3 differentiators
7. **Education** — course cards with duration and chapter count
8. **Subscription plans** — 4 cards with a struck-through price, a discount percentage, and a «محبوب» (popular) badge
9. **Closing CTA** with 3 check marks

**What we take:** the section order, the "live data cards in the hero" pattern, the numbered process, the mobile bottom nav, and plan cards with discounts.
**What we do not take:** the green color, stock illustrations (far too generic — we use real dashboard screenshots instead), and unsourced numeric claims (`۹۸٪ رضایت` — 98% satisfaction).

### 1-2. Rahavard 365 (rahavard365.com/pricing) — the "subscription architecture" pattern

Its subscription page structure:

- Headline: `مقایسه و خرید اشتراک ره‌آورد` (compare and buy a Rahavard subscription) + one explanatory paragraph
- **Two subscription families as tabs**: `اشتراک اصلی` | `اشتراک تخصصی` (core | specialized, with a `جدید` / new badge)
- **Period toggle**: `۱ ماهه` / `۳ ماهه` / `۱۲ ماهه` (1 / 3 / 12 months)
- **Discount bar**: `تا ۲۷ درصد تخفیف خرید اشتراک سالیانه` (up to 27% off annual plans)
- **4 plan cards** (Platinum / Gold / Silver / Basic) — each with a `ویژگی‌ها و مقایسه` (features and comparison) link, a price in `تومان`, and its own button
- A `محبوب‌ترین اشتراک` (most popular) badge on the Gold plan, `بزودی` (coming soon) on Platinum
- An entry gift: `دریافت ۳ روز اشتراک طلایی هدیه` (get 3 days of Gold as a gift) on the free plan
- A **7-item FAQ accordion** specific to purchasing (upgrades, discount codes, expiry, enterprise purchase)

**What we take:** the period toggle + discount bar, the "features and comparison" link under each plan (which scrolls to the comparison table), the popular badge, the gift on the free plan, and a purchase-specific FAQ at the bottom of the same page.
**Note:** Rahavard has two subscription **families**. So do we (Gold / Covered Call) — so this pattern applies directly.

### 1-3. Toranj Capital (toranjcapital.com) — the "institutional credibility" pattern

> The site was unreachable from this network at review time; its information architecture was reconstructed from its public URL structure: `/about-us`, `/products/<fund name>`, `/portfolio-management-service/`.

**What we take:** the **dedicated page per product** pattern (`/products/gold-arbitrage`, `/products/covered-call`) instead of compressing everything onto the home page; and a standalone page for the **execution service** (portfolio management), separate from the data product. Plus the more formal tone and the licenses / performance-report sections that regulated portfolio managers carry.

### 1-4. Optionbaaz (optionbaaz.ir) — the "open data + knowledge base" pattern ← **your most important reference**

This is the closest direct competitor to your second product and has the smartest content-product architecture of the four sites. Its home page structure:

1. **A short hero** + an onboarding bar: `اولین بار است؟ ببینید آپشن‌باز چطور کار می‌کند` (First time? See how Optionbaaz works)
2. **"بازار در یک نگاه"** (the market at a glance) — tabs `بازار سهام` | `بورس کالا`, a `بازار باز است` (market is open) status, and 4 live KPIs: options trading value · options share of the total market · put/call ratio (PCR) · total open interest
3. **Tools grid** — every tool with a one-line description **and a dedicated guide link** (`راهنمای دیده‌بان`, `راهنمای زنجیره`…)
4. **"معرفی آپشن‌باز" — one trade told end to end**: "the watchlist finds the opportunity, the strategy column scores it, and the profit-and-loss chart opens before the order is placed."
5. **"نبض بازار"** (market pulse) — 7 free live charts (order-book depth, retail money inflow, trade intensity, buyer strength…)
6. **"نبض بازار اختیار"** (options market pulse) + **Iran VIX index** — proprietary analytical data available nowhere else
7. **Market map** · **Top movers** · **Near expirations**
8. **"کانال"** (channel) — an announcement and market-analysis feed right on the home page
9. **Products grid split by market** — equity options / commodity-exchange options / funds (fixed income, gold, silver)
10. **"دانشنامه"** (knowledge base) — 5 educational categories + `راهنمای استفاده از سایت` (site usage guide)
11. **"پیشنهاد مطالعه مقاله"** (suggested reading) — one flagship article with a real abstract
12. **Long-form SEO prose block** — "آپشن‌باز چه ابزارهایی برای بازار اختیار معامله دارد؟" with 6 `h3` subheadings and roughly 800 words of natural Persian copy plus internal links
13. **Support and ticketing**

**Four key lessons that go straight into version 2:**

| Lesson | Why it matters | How it is implemented on your site |
|---|---|---|
| **Free data, paid tools** | The home page is itself a product. The user gets value without registering, forms a habit, and then pays for the tools. | A free "نبض بازار طلا" (gold market pulse) on the home page: fund bubbles, NAV, spot prices — while filters, history, alerts and signals are paid |
| **One guide per tool** | A guide link next to each tool raises activation and creates an SEO page at the same time. | Next to each dashboard capability, a `راهنمای ...` link into the knowledge base |
| **A knowledge base, not a blog** | A "blog" is a time-ordered stream that goes stale. A "knowledge base" is a categorized, durable structure — far stronger for Persian SEO. | `/wiki` replaces `/blog` (Section 8) |
| **Long-form SEO prose at the bottom of the home page** | Persian Google weights long, natural copy with internal links heavily. Optionbaaz does this thoroughly. | A 700–900 word block at the bottom of the home page and of every product page |

**One freemium tactic you should copy:** "Outside trading hours the tools are open to everyone, and you can work with the last trading day's data without a subscription." The user gets to touch the full tool, but the **real-time** advantage is only available with a subscription. Exactly what your product (real-time arbitrage) needs.

**What we do not take:** the extremely high visual density of its home page (20+ charts). Optionbaaz is built for professional traders; your primary audience is "the gold-fund holder" and needs a calmer page. We reduce "market pulse" to **a compact 4-card strip** and move the full version to a standalone `/market` page.

### 1-5. Your first version (Arca Landing) — what is kept

Current sections: `NAV` → `HERO` → `WHY OPPORTUNITY` → `HOW IT WORKS` → `BENEFITS OF GOLD FUNDS` → `ABOUT TEAM` → `LEAD FORM` → `FOOTER`, plus the `Performance` / `About` / `FAQ` / `Contact` pages.

**Kept (do not throw away the equity you have already built):**

- The gold-and-navy color identity and the Alef logo
- The Vazirmatn font and the RTL setup
- The animated hero SVG illustration (bullion / vault) — as a signature brand element
- The strong existing copy: «قیمت هر صندوق طلا، دقیقاً برابر ارزش واقعی‌اش نیست» (a gold fund's price is not exactly its true value), «چهار مرحله، کاملاً خودکار» (four steps, fully automated), «همان طلا، با ساختاری هوشمندتر» (the same gold, with a smarter structure), «تیمی از دانشگاه، پشت یک الگوریتم» (a university team behind an algorithm)
- The `Performance` page comparing the algorithm against simple buy-and-hold

**Changed:**

- The hero CTA goes from `مشاوره رایگان بگیر` → `شروع رایگان` (the consultation form moves to the enterprise plan)
- The `BENEFITS OF GOLD FUNDS` section moves from the home page to the gold product page
- On the home page, `LEAD FORM` is replaced by the «پلن‌ها» (plans) section

---

## 2. Positioning, Audience and Message

### Core value proposition (one sentence)

> **Alef Capital turns the two low-risk return engines of the Iranian stock market — gold-fund arbitrage and covered calls — into usable real-time dashboards.**

### Three personas

| Persona | What they want | Where on the site they are sold |
|---|---|---|
| **Gold holder** — capital sits in a gold fund, worried about inflation | Extra return without leaving gold and without new risk | Home page → gold product → Gold plan |
| **Professional trader** — familiar with options | A tool to scan covered-call opportunities quickly | Covered-call product → Diamond plan |
| **Institutional investor / large portfolio** | Running the algorithm on their own account | Services page → lead form → phone call |

### Tone of voice rules

- **Precise, not hyped.** «۵ تا ۱۰ درصد سالانه از محل آربیتراژ» (5 to 10 percent a year from arbitrage) — not "astronomical returns".
- **Every number carries a source and a time window.** An unsourced number on a financial site is a legal risk.
- **Do not hide risk; show it as managed.** Give the "break-even point" and "risk margin" sections prominence — that honesty is your differentiator.
- **Never use "guarantee".** Instead: "historically", "over the reviewed window", "based on the last 12 months of data".
- Banned: «قطعاً» (certainly), «تضمینی» (guaranteed), «بدون ریسک» (risk-free), «سود ۱۰۰٪ مطمئن» (100% sure profit).
- **Hold the product boundary.** What the subscription sells is **the dashboard and the data**, not the execution of the algorithm. Anywhere the copy mentions "signals", "automatic switching" or "running the algorithm", it must either move to `/services` or be explicitly labeled as a separate service. The home page and the product pages sell dashboards only.

---

## 3. Information Architecture

```
/                          Home page (hub)
│
├── /products
│   ├── /gold-arbitrage    Gold fund arbitrage dashboard        ← Product 1
│   └── /covered-call      Covered-call dashboard (fixed yield) ← Product 2
│
├── /market                Gold market pulse — free live data   ← Acquisition and SEO engine
│   ├── /market/funds       Bubble table for every gold fund
│   └── /market/gold        Spot prices: 18k gold, bullion, coin, ounce, USD
│
├── /pricing               Plans and subscriptions   ← Primary conversion page
├── /performance           Performance and returns    (from v1, rewritten)
├── /services              Portfolio management / algorithm execution  (enterprise leads)
│
├── /wiki                  Knowledge base — content hub  ← SEO engine
│   ├── /wiki/gold-funds        Gold funds and ETFs
│   ├── /wiki/arbitrage         Arbitrage and the bubble
│   ├── /wiki/options           Options and covered calls
│   ├── /wiki/risk              Risk and capital management
│   ├── /wiki/guides            Dashboard usage guides
│   └── /wiki/<slug>            Article page
│
├── /about                 About us and the team     (from v1)
├── /faq                   Frequently asked questions (from v1, expanded)
├── /contact               Contact us                (from v1)
│
├── /legal/terms           Terms and conditions
├── /legal/privacy         Privacy policy
├── /legal/risk            Risk disclosure           ← Mandatory
│
└── User account (behind login)
    ├── /auth/login /auth/register /auth/otp
    ├── /app/dashboard/gold        Gold dashboard
    ├── /app/dashboard/covered-call Covered-call dashboard
    ├── /app/alerts                Alerts
    ├── /app/billing               Subscription and invoices
    └── /app/settings              Settings
```

### Main menu (desktop — right-aligned)

```
[لوگو الف کپیتال]   محصولات ▾   بازار   قیمت‌گذاری   عملکرد   دانشنامه ▾   درباره ما      [ورود]  [شروع رایگان]
```

(Alef Capital logo · Products ▾ · Market · Pricing · Performance · Knowledge base ▾ · About us · [Log in] [Start free])

**The «محصولات» (Products) mega menu** (two columns + one promotional column):

| Column 1 — Dashboards | Column 2 — Services | Column 3 |
|---|---|---|
| 🟡 **آربیتراژ صندوق طلا** (Gold fund arbitrage)<br>پایش لحظه‌ای حباب و NAV (real-time bubble and NAV monitoring)<br><small>`راهنما ←` (Guide →)</small> | 📈 **مدیریت پرتفوی** (Portfolio management)<br>اجرای خودکار روی حساب شما (automated execution on your account) | Promo card:<br>«۷ روز رایگان، بدون کارت بانکی» (7 days free, no bank card)<br>[شروع کنید] (Get started) |
| 🔵 **کاوردکال / بهره ثابت** (Covered call / fixed yield)<br>دیدبان اختیار معامله و نرخ معادل سالانه (options watchlist and annualized equivalent rate)<br><small>`راهنما ←` (Guide →)</small> | 📊 **گزارش عملکرد** (Performance report)<br>داده ممیزی‌شده (audited data) | |

> The Optionbaaz pattern: **a guide link next to every product.** The link goes into the knowledge base; it raises activation and creates an SEO page at the same time.

**Mega-menu technical specification (tree structure):**

| Property | Value |
|---|---|
| Trigger | `hover` on desktop (`@media (hover:hover)`) + `click` on all devices + closes on `Escape` and outside click |
| Accessibility | The menu title is a `<button>` with `aria-expanded` and `aria-controls`; items are `role="menuitem"` — not an `<a href="#">` |
| **Tree rail** | Each column has a 1px vertical line (`.mm-col::before`) and each item connects to it with a 12px horizontal line (`.mm-i::before`). On hover the horizontal line turns gold. This is what makes the menu read as a "tree" rather than as a plain list. |
| Layout | Three columns: `داشبوردها` (dashboards, 1.25fr) · `خدمات` (services, 1fr) · promo card (0.85fr) — below 1080px it collapses to two columns with a full-width promo card |
| Direction | `inset-inline-start: -24px` relative to the menu item; the small arrow above the menu aligns with the button |
| Fine detail | The «راهنمای این داشبورد ←» (guide for this dashboard →) link is hidden with `opacity:0` and appears on hover — so the resting state stays uncluttered |
| Reduced motion | Under `prefers-reduced-motion` all transitions are removed |

**The «دانشنامه» (Knowledge base) mega menu:** five categories (صندوق‌های طلا · آربیتراژ و حباب · اختیار معامله و کاوردکال · مدیریت ریسک · راهنمای داشبوردها — gold funds · arbitrage and the bubble · options and covered calls · risk management · dashboard guides) + a "latest article" card.

### Bottom navigation bar (mobile — the Bambo pattern)

Five fixed items: `خانه` · `بازار` · `محصولات` · `دانشنامه` · `حساب من` (Home · Market · Products · Knowledge base · My account)
64px tall, glass background, gold active icon.

---

## 3-5. User Experience Map

This map is the backbone of the site. **Every page must know which stage the user is in and which stage it moves them to.** The overall flow is taken from Optionbaaz: free data → limited tool → subscription → daily habit.

### 3-5-1. The five journey stages

```
   ①  Discover        ②  Understand     ③  Experience     ④  Convert        ⑤  Habit & referral
  ──────────         ──────────        ──────────        ──────────        ──────────
  Google, Telegram,  Learns what the   Touches the free  Realizes that     Opens the
  a friend's         bubble is and     data and the      without real      dashboard
  recommendation     why it is an      limited           time, the         every morning
                     opportunity       dashboard         opportunity
                                                         is missed
       │                │                 │                 │                 │
       ▼                ▼                 ▼                 ▼                 ▼
  /wiki/<article>   /products/*      /market  +        /pricing          /app/dashboard
  /market           chart and a      free basic plan   → payment          + alerts
                    worked example
       │                │                 │                 │                 │
  ── Success signal for each stage ───────────────────────────────────────────────
  Scroll > 50%      Click on          Sign-up with      Subscription      4 return
  or an internal    "مشاهده محصول"    mobile number     purchase          visits
  click             (view product)                      (target 4–6%)     per week
```

### 3-5-2. Detailed journey table

| | ① Discover | ② Understand | ③ Experience | ④ Convert | ⑤ Habit |
|---|---|---|---|---|---|
| **What the user is thinking** | «طلا خریدم ولی نمی‌دونم کدوم صندوق» (I bought gold but I don't know which fund) | «پس اختلاف قیمت با NAV یعنی فرصت» (so the gap to NAV is an opportunity) | «داده‌شون واقعیه، جدولشون درست کار می‌کنه» (their data is real, their table works) | «داده تأخیری به دردم نمی‌خوره» (delayed data is useless to me) | «قبل از سفارش، اول اینجا رو چک می‌کنم» (before ordering, I check here first) |
| **Entry point** | Knowledge base article · Google search · Telegram channel | Product page | `/market` · free plan | `/pricing` | Email/SMS alert · bookmark |
| **What the site must do** | Answer their question precisely, **with no paywall** | Explain the problem with one chart and one worked example | Show real, working data — not a screenshot | Make the value of real time tangible | Send an alert and bring the user back |
| **Primary CTA** | `ادامه مطلب` / `دیدن داده زنده` (read more / see live data) | `شروع رایگان` (start free) | `ارتقا به طلا` (upgrade to Gold) | `خرید اشتراک` (buy subscription) | `تنظیم هشدار جدید` (set a new alert) |
| **Main obstacle** | Does not know what this site is | "Does it actually work?" | "Is it worth it?" | Price · trusting the payment | Forgetting |
| **Design antidote** | Human prose, no pop-up in the first 30 seconds | Performance chart + methodology block | Locked features are **visible**, not hidden | Payment trust bar + 7 days free + easy cancellation | SMS alerts + weekly email digest |
| **Metric** | New organic users | Click-through rate to the product | Sign-up rate | Free→paid conversion rate | DAU/MAU · renewal rate |

### 3-5-3. Three key flows by persona

**Flow A — "the gold fund holder" (highest volume)**

```
Search for «حباب صندوق طلا چیست» (what is the gold fund bubble)
    → /wiki/arbitrage/gold-fund-bubble   [educational article, ending with a live card of today's bubble]
    → /market/funds                       [bubble table for every fund — free, 15-minute delay]
    → Sign up with mobile + OTP           [to see one fund's bubble history]
    → /products/gold-arbitrage             [«این جدول لحظه‌ای هم می‌شود» — this table can be real-time too]
    → /pricing → Gold plan
```

**Flow B — "the options trader"**

```
Search for «نرخ سود کاوردکال» (covered-call yield) or a referral from a channel
    → /wiki/options/covered-call-rate     [article + a calculator embedded in the copy]
    → Calculator: enters their own numbers, sees the annualized equivalent rate
    → «۱۲ موقعیت با نرخ بالای ۶۰٪ امروز در بازار هست» (12 positions above 60% in the market today) [locked]
    → Sign up → Professional plan
```

> The covered-call calculator inside the article is **the strongest conversion tool on the whole site**: the user enters their own numbers, sees the result, and immediately understands what the full version is worth. Build it.

**Flow C — "the institutional investor"**

```
/ → /services → reads the three delivery models → lead form (portfolio size, phone number)
    → team phone call → meeting → contract
```
This flow **must not** pass through the subscription funnel. Its button everywhere is `درخواست مشاوره` (request a consultation), not `خرید` (buy).

### 3-5-4. Paywall rules

| Tier | What they see | Why |
|---|---|---|
| **Guest (not registered)** | The whole knowledge base · `/market` with a 15-minute delay · the top 5 funds · all marketing pages | SEO and trust. **No educational content goes behind login.** |
| **Free account** | 1 day of history · 1 alert · the full fund table with a delay · outside trading hours: full previous-day data | Captures the mobile number; the user touches the tool |
| **Gold plan** | Everything real-time in the gold domain | |
| **Professional plan** | + covered calls + API + unlimited history | |

**The golden rule:** a locked feature must **always be visible** — table rows blurred with a 🔒 icon and a «با پلن طلا لحظه‌ای ببینید» (see it in real time with the Gold plan) label. Hiding a feature kills the sale; showing it creates the sale.

### 3-5-5. Retention moments

| When | Trigger | Message |
|---|---|---|
| Day 1 | After sign-up | Welcome SMS + a link to the 2-minute guide |
| Day 2 | First visit | A 4-step in-app tour of the dashboard |
| Day 3 | — | «۳ صندوق امروز حباب منفی داشتند» (3 funds had a negative bubble today) — an email with sample data |
| Day 5 | — | «۲ روز از دوره رایگان مانده» (2 days left in your free trial) + a plan comparison |
| Weekly (ongoing) | Friday night | **The weekly gold market digest** — the best retention tool. Send it even to free users. |
| Real-time | A fund's bubble crosses a threshold | SMS/push notification — this is what renews subscriptions |

---

## 4. Design System

### 4-1. Color (CSS tokens)

```css
:root{
  /* برند — طلایی (از نسخه ۱ حفظ شده) */
  --gold-300:#FFD873;  --gold-400:#F0B429;  --gold-500:#E0A82E;
  --gold-600:#C9861A;  --gold-700:#8A5A08;

  /* سرمه‌ای — متن و سطوح تیره */
  --ink-950:#070C16;  --ink-900:#0B1220;  --ink-800:#0F172A;  --ink-700:#1E293B;

  /* خاکستری */
  --slate-600:#475569; --slate-500:#64748B; --slate-400:#94A3B8;

  /* سطوح روشن */
  --surface:#FFFFFF;  --surface-2:#F8FAFC;  --surface-3:#F1F5F9;
  --border:#E2E8F0;   --border-strong:#CBD5E1;

  /* سطوح تیره (سکشن‌های نمایش داشبورد) */
  --dark-bg:#0B1220;  --dark-panel:#111A2B;  --dark-border:#1E2A3F;

  /* معنایی — قواعد بازار ایران */
  --up:#16A34A;       /* رشد/مثبت — سبز */
  --down:#DC2626;     /* افت/منفی — قرمز */
  --info:#0E7490;     /* اطلاع */
  --warn:#D97706;     /* هشدار */

  /* گرادیان‌های برند */
  --grad-gold:linear-gradient(135deg,#FFD873,#C9861A);
  --grad-gold-text:linear-gradient(135deg,#C9861A,#8A5A08);
}
```

(Comment glosses, top to bottom: brand — gold, preserved from v1 · navy — text and dark surfaces · grays · light surfaces · dark surfaces, dashboard showcase sections · semantic — Iranian market conventions: up/positive green, down/negative red, info, warning · brand gradients.)

**Color usage rules:**

- Gold is used **only** for: the primary CTA, badges, key figures, and headline highlights. Never for body copy.
- Page bodies: light background (`--surface`). Dashboard showcase sections: dark background (`--dark-bg`) — because the real product dashboard is dark, and this creates visual continuity.
- Green/red only for market data. Never for buttons or branding.
- At most one solid gold CTA per viewport.

### 4-2. Typography

Font: **Vazirmatn** — weights 400, 500, 600, 700, 800, 900.
`font-feature-settings:"ss02"` for nicer Persian digits. Latin numerals in tables use `font-variant-numeric:tabular-nums`.

| Role | Size | Weight | Line height |
|---|---|---|---|
| `display` (hero) | `clamp(36px, 4.6vw, 62px)` | 800 | 1.16 |
| Page `h1` | `clamp(30px, 3.4vw, 44px)` | 800 | 1.25 |
| Section `h2` | `clamp(24px, 2.6vw, 34px)` | 700 | 1.35 |
| Card `h3` | `19px` | 700 | 1.5 |
| Large body | `17.5px` | 400 | 2.0 |
| Body | `15.5px` | 400 | 1.9 |
| Caption / label | `13px` | 600 | 1.6 |
| Data figure (KPI) | `clamp(28px,3vw,40px)` | 800 | 1.1 · `tabular-nums` |

**Persian rules:** body line height is never below 1.8 (Persian needs more vertical breathing room). `text-wrap:pretty` on headings. Money figures always use thousands separators, with the «تومان» (toman) unit set apart.

### 4-3. Spacing, radius, shadow

```css
--sp-1:4px; --sp-2:8px; --sp-3:12px; --sp-4:16px; --sp-5:24px;
--sp-6:32px; --sp-7:48px; --sp-8:64px; --sp-9:96px; --sp-10:128px;

--r-sm:8px; --r-md:12px; --r-lg:16px; --r-xl:24px; --r-full:999px;

--sh-sm:0 1px 2px rgba(11,18,32,.06);
--sh-md:0 4px 16px -4px rgba(11,18,32,.10);
--sh-lg:0 18px 44px -18px rgba(11,18,32,.22);
--sh-gold:0 14px 30px -12px rgba(184,120,26,.55);
```

- Max content width: `1200px`. Side gutters: `clamp(20px, 6vw, 80px)`.
- Vertical spacing between sections: `--sp-9` on desktop / `--sp-7` on mobile.
- Grid: 12 columns, `gap: 24px`.

### 4-4. RTL rules

- `dir="rtl" lang="fa"` on `<html>`.
- Every directional icon (arrows, chevrons) is mirrored in RTL: `arrow_back` means "go forward".
- Charts: the time axis stays **left to right** (the global financial standard), but labels and the legend are right-aligned.
- Latin numbers and symbols (NAV, ITM, DTM) are wrapped in `<span dir="ltr">`.
- Phone numbers and email addresses are always `dir="ltr"`.

### 4-5. Icons and imagery

- Icon set: **Material Symbols Rounded** (weight 300, size 24) — the same set Bambo uses, with good financial coverage.
- **No stock photography.** Instead: real dashboard screenshots (with data blurred in the free tier), hand-built SVG charts, and the brand SVG illustration from v1.
- Every dashboard image sits inside a browser chrome mockup with a 12px radius and the `--sh-lg` shadow.

---

## 5. Component Library

| Component | Specification |
|---|---|
| `Button/primary` | Background `--grad-gold`, text `#1A1200`, `padding:16px 34px`, `--r-md`, shadow `--sh-gold`, hover: `translateY(-1px)` |
| `Button/secondary` | Transparent, border `1px solid var(--border-strong)`, text `--ink-800` |
| `Button/ghost` | Text only, `--gold-700` |
| `Badge/live` | 7px dot with a `pulse` animation, 13px text, background `rgba(240,180,41,.18)` |
| `Badge/popular` | Solid gold, absolutely positioned at the top of the plan card |
| `Card/product` | `1px` border, `--r-lg`, `padding:28px`, a 48px icon in a pale gold circle, hover: `border-color:var(--gold-400)` + `--sh-md` |
| `Card/pricing` | The same, plus the recommended plan gets a 2px gold border and a 1.03 scale |
| `Card/metric` (KPI) | Small label on top, large figure, colored delta, optional sparkline |
| `Table/market` | Sticky header, alternating rows in `--surface-2`, percentage cells with a soft colored background, horizontal scroll on mobile |
| `Chart/*` | Library: **ECharts** (better RTL and Persian support than Chart.js) |
| `Accordion/faq` | `+`/`−`, 200ms height animation, only one open at a time |
| `Toggle/billing` | Three-state pill (monthly / 3 months / annual) with a gold slider |
| `Stepper/process` | Two-digit number `۰۱`, dashed connector line, icon |
| `Form/lead` | Name, mobile (validated with `^09\d{9}$`), portfolio size (optional), terms-acceptance checkbox |
| `Modal/demo` | Dashboard video/GIF, no sign-up required |
| `Nav/bottom` | Mobile only, 5 items, `position:fixed; bottom:0` |
| `Banner/risk` | A thin bar at the bottom of every product page carrying the risk disclosure text |

---

## 6. Page-by-Page Design (with ready Persian copy)

> Text inside guillemets is **final, ready-to-use copy**. Values inside `{{ }}` must be replaced with real data.

---

### 6-1. Home page `/`

**Goal:** in 10 seconds, make clear "who we are, how many products we have, where I should start". The section order is taken from the Bambo pattern.

#### Section 1 — Header (sticky)

Glass, with `backdrop-filter:blur(12px)`, background `rgba(255,255,255,.88)`, 1px bottom border. It gains a shadow after 8px of scroll.

#### Section 2 — Hero

- **Live badge:** `● داشبورد آربیتراژ صندوق طلا و کاوردکال بورس تهران — داده زنده` (Gold fund arbitrage and covered-call dashboard for the Tehran exchange — live data)
- **Headline:**
  > سرمایه شما،
  > **با دو موتور بازده کم‌ریسک**

  (Your capital, powered by two low-risk return engines — the second line uses `--grad-gold-text` with `background-clip:text`)
- **Subheadline:**
  > «الف کپیتال حباب صندوق‌های طلا و فرصت‌های کاوردکال بورس تهران را لحظه‌به‌لحظه رصد می‌کند و آن‌ها را به دو داشبورد قابل استفاده تبدیل می‌کند — تا تصمیم شما بر پایه داده باشد، نه حدس.»

  (English gloss: Alef Capital tracks gold-fund bubbles and Tehran-exchange covered-call opportunities moment by moment and turns them into two usable dashboards — so your decision rests on data, not guesswork.)
- **CTAs:** `[شروع رایگان]` (Start free — primary) + `[نمایش داشبورد]` (Show the dashboard — secondary, video modal)
- **Left side:** three **live cards** (replacing the v1 illustration in the primary slot; the SVG illustration moves to the `/about` page). Full specification in Section 6-1-a.

#### Section 2-a — Ticker price bar (between the header and the hero)

A sticky 42px bar with an `--ink-900` background, directly below the header. On the right, a fixed block reading `● بازار باز است` / `بازار بسته است` (market is open / market is closed); the rest is a moving ticker.

| Property | Value |
|---|---|
| Items | طلای ۱۸ عیار · مثقال طلا · گواهی شمش · گواهی سکه · سکه امامی · اونس جهانی · دلار · شاخص صندوق‌های طلا (18k gold · gold mithqal · bullion certificate · coin certificate · Emami coin · global ounce · USD · gold fund index) |
| Structure of each item | `نام` (name, gray) · `قیمت` (price, white, `tabular-nums`) · `▲/▼ درصد` (percent, green/red) |
| Motion | `transform: translateX(0 → -50%)` on a strip whose content is **duplicated** — the only way to get a seamless loop |
| Duration | 46 seconds, `linear`, `infinite` |
| Pause | `:hover` → `animation-play-state: paused` |
| Edge fade | A `::before`/`::after` gradient 70px wide on both sides |

> ⚠️ **The RTL trap you will definitely hit:** the moving strip must have `direction:ltr` and `position:absolute; left:0`. If you leave it in the normal flow of an RTL container, the `width:max-content` element is pinned to the right edge and the animation carries it entirely out of the viewport — the bar goes empty after a few seconds. Each item inside the strip gets its own `dir="rtl"`.

#### Section 2-b — Three live cards

Each card has a header: a label + a `● زنده` (live) indicator (a green dot with a `pulse` animation).

**Card 1 — Gold fund bubbles**

- Large figure: **the average bubble across 30 funds**, in a semantic color — a negative bubble is green (`--up-text`), a positive bubble is red (`--down`). Because a negative bubble is an opportunity for the buyer.
- Below it, a **distribution strip**: 30 vertical bars, one per fund, height proportional to the bubble and color by sign. A thin gray line at zero.
- Footnote: `کم‌حباب‌ترین <نام> <درصد>` (lowest-bubble <name> <percent>) and `پرحباب‌ترین <نام> <درصد>` (highest-bubble <name> <percent>) — fund names update with the data.
- This distribution strip is **the visual signature of the first product**: at a glance it shows how wide the bubble spread is, which is exactly what creates the arbitrage opportunity.

**Card 2 — Today's covered-call opportunities**

- Large figure: the number of positions with an equivalent rate above 50%.
- Below it, a **small three-row table of real option symbols**: `نماد` | `روزهای تا سررسید` | `نرخ معادل سالانه` (symbol | days to expiry | annualized equivalent rate). For example `ضستا۳۰۱۰ · ۱۵ روز · ۶۹٫۰٪`.
- The rows cycle through today's positions every few seconds with a soft fade (`opacity`, 340ms).
- **Why this matters:** "12 positions" is an abstract number; `ضستا۳۰۱۰ با ۶۹٪ سالانه` (symbol X at 69% annualized) is a verifiable claim. A trader can check that symbol on the exchange board right now. That is the difference between a claim and a proof.

**Card 3 — 18k gold**

- Large figure + a percentage chip, plus an **SVG sparkline** (40 points) with a gradient area beneath it and a dot on the latest value.

**Footer bar under the cards:** `آخرین به‌روزرسانی HH:MM:SS` (last updated HH:MM:SS — the clock must actually tick) + a **thin progress bar** that fills until the next update + a data-status label.

#### Rules for the feeling of "liveness"

These five things are what separate a static page from a live one. In order of importance:

| # | Technique | Detail |
|---|---|---|
| 1 | **Value-change flash** | Whenever a number changes, give it a pale green or red background for 700ms. The most effective liveness cue, and the cheapest. |
| 2 | **A ticking clock** | A real seconds counter, not a fixed timestamp. The user's brain notices immediately. |
| 3 | **A progress bar to the next update** | Makes the wait predictable and proves the system is working. |
| 4 | **A `● زنده` (live) indicator with a pulsing dot** | On every card carrying real-time data. |
| 5 | **The moving price ticker** | Continuous motion in peripheral vision, even when nothing has changed. |

> ⚠️ **Two rules whose violation burns trust:**
> 1. These elements must be fed by a **real API**. A hardcoded constant on a financial site is worse than nothing — a user who notices never comes back.
> 2. When the market is closed or the connection drops, **say so honestly**: the `زنده` (live) indicator changes to `آخرین داده معاملاتی` (last trading data) and the pulsing dot switches off. Never pass stale data off as live.

> ♿ All animations must be disabled under `@media (prefers-reduced-motion: reduce)`: the ticker stops and becomes manually scrollable, the pulsing dot goes static, the value flash is removed.

#### Section 3 — Stat bar

Three columns on a `--surface-2` background:

| `{{ ۳۰+ }}` | `{{ ۳۶۸ }}` | `۲۴/۷` |
|---|---|---|
| صندوق طلای تحت پایش (gold funds monitored) | قرارداد اختیار معامله در دیدبان (option contracts on the watchlist) | رصد پیوسته در ساعات معاملاتی (continuous monitoring during trading hours) |

#### Section 4 — The two products (the heart of the page)

Headline: **«دو محصول، دو مسیر کسب بازده»** (Two products, two paths to returns)
Subheadline: «هر دو بر یک اصل استوارند: فرصت‌هایی که با چشم و به‌صورت دستی قابل شناسایی نیستند، اما الگوریتم آن‌ها را لحظه‌ای پیدا می‌کند.» (Both rest on one principle: opportunities that cannot be spotted by eye or by hand, but that an algorithm finds in real time.)

Two large cards side by side (stacked on mobile):

**Card A — Gold fund arbitrage dashboard** 🟡
> «قیمت هر صندوق طلا دقیقاً برابر ارزش واقعی‌اش (NAV) نیست؛ این اختلاف را «حباب» می‌گویند. داشبورد آربیتراژ، حباب همه صندوق‌های طلای بورس را لحظه‌ای محاسبه می‌کند و صندوق‌های ارزنده را نشان می‌دهد.»
> - پایش لحظه‌ای حباب و NAV همه صندوق‌ها
> - تحلیل ترکیب دارایی (سکه، شمش، گواهی سپرده)
> - شناسایی خودکار صندوق ارزنده برای جابه‌جایی
> - **بازده هدف: ۵ تا ۱۰ درصد سالانه طلای اضافه**
> `[مشاهده محصول ←]`

(English gloss: a gold fund's price is not exactly its true value (NAV); that gap is called the "bubble". The arbitrage dashboard computes the bubble for every listed gold fund in real time and highlights the undervalued ones. Bullets: real-time bubble and NAV monitoring for every fund · asset-composition analysis (coin, bullion, deposit certificates) · automatic identification of the undervalued fund to switch into · **target return: 5 to 10 percent a year in additional gold**. Button: view product →)

**Card B — Covered-call dashboard (fixed yield)** 🔵
> «کاوردکال یعنی خرید سهم و هم‌زمان فروش اختیار خرید همان سهم. نتیجه، یک بازده از پیش تعیین‌شده در بازه‌ای مشخص است. داشبورد ما هزاران قرارداد را می‌سنجد و بهترین نسبت بازده به ریسک را بیرون می‌کشد.»
> - دیدبان کامل قراردادهای اختیار خرید
> - محاسبه خودکار نرخ سود معادل سالانه و حاشیه ریسک
> - پایش سررسید و نقطه سربه‌سری هر موقعیت
> - **بازده هدف: ۶۰ تا ۱۰۰ درصد سالانه با ریسک پایین**
> `[مشاهده محصول ←]`

(English gloss: a covered call means buying a stock and simultaneously selling a call option on it. The result is a predetermined return over a defined window. Our dashboard evaluates thousands of contracts and surfaces the best return-to-risk ratio. Bullets: a complete watchlist of call contracts · automatic calculation of the annualized equivalent yield and risk margin · expiry and break-even monitoring for every position · **target return: 60 to 100 percent a year at low risk**. Button: view product →)

#### Section 5 — Dashboard showcase (dark section)

Background `--dark-bg`. Tabs `آربیتراژ طلا` | `کاوردکال` (gold arbitrage | covered call). Under each tab, a real dashboard screenshot inside a browser frame, with three gold annotation dots pointing at the key areas.

Headline: **«این چیزی است که هر روز می‌بینید»** (This is what you see every day)

> **Removed from the home page — the «چهار مرحله، کاملاً خودکار» (four steps, fully automated) section.**
> That section sold the **algorithm's** process, whereas the site sells **a dashboard**. Its fourth step («سیگنال جابه‌جایی صادر می‌شود؛ اجرا با شما یا الگوریتم» — a switch signal is issued; execution is up to you or the algorithm) promised something the subscription product does not deliver.
> This content is not deleted, it is **relocated**: to the `/services` page, which sells the execution service and portfolio management, and is its proper home.
> The gap it leaves on the home page is not filled — the "dashboard showcase" section (Section 5) does the same job better: instead of describing what the system does, it shows what the user sees.

#### Section 6 — Why a gold fund

(Move over from v1, 6 cards, per the product document):
امنیت بالا در نگهداری · شفافیت و نظارت · معافیت مالیاتی · کارمزد زیر ۰.۲٪ (در برابر تا ۲٪ در بازار فیزیکی) · نقدشوندگی بالا · حذف ریسک طلای تقلبی
(High custody security · transparency and oversight · tax exemption · fees under 0.2% versus up to 2% in the physical market · high liquidity · no counterfeit-gold risk)

#### Section 7 — Trust

- Team: «تیمی از دانشگاه، پشت یک الگوریتم» (a university team behind an algorithm — from v1)
- Licenses and partnerships (logos of partner brokerages)
- Performance: a chart comparing «الگوریتم در برابر نگهداری ساده صندوق طلا» (the algorithm versus simply holding a gold fund) + `[گزارش کامل عملکرد ←]` (full performance report →)
- **No fake testimonials.** If you do not have real customers, remove this block until you do.

#### Section 8 — Knowledge base and flagship article

(The Optionbaaz pattern.) Headline: **«قبل از سرمایه‌گذاری، بدانید چه می‌کنید»** (Before investing, know what you are doing)
A 5-card grid of knowledge base categories + a "پیشنهاد مطالعه" (suggested reading) block with a real abstract of the flagship article + `[ورود به دانشنامه ←]` (enter the knowledge base →)

#### Section 9 — Plans preview

Three compact cards + `[مقایسه کامل پلن‌ها ←]` (full plan comparison →) linking to `/pricing`

#### Section 10 — SEO prose block

(The Optionbaaz pattern — **do not remove it, it is the home page's SEO engine**)
`h2` headline: «الف کپیتال چه ابزارهایی برای بازار طلا و اختیار معامله دارد؟» (What tools does Alef Capital offer for the gold and options markets?)
700–900 words of natural Persian prose with 5 `h3` subheadings and internal links to `/market`, both product pages, and the knowledge base. Suggested subheadings:

- حباب صندوق‌های طلا: چرا قیمت با ارزش واقعی فرق می‌کند (Gold fund bubbles: why price differs from true value)
- داشبورد آربیتراژ: چه چیزی را لحظه‌ای می‌بینید (The arbitrage dashboard: what you see in real time)
- کاوردکال: بهره ثابت از بازار سهام (Covered calls: fixed yield from the equity market)
- نبض بازار طلا: داده‌ای که رایگان در اختیار شماست (The gold market pulse: the data you get for free)
- اگر تازه با صندوق‌های طلا آشنا می‌شوید (If you are new to gold funds)

#### Section 11 — Closing CTA + Section 12 — Footer

---

### 6-2. Product page 1 — `/products/gold-arbitrage`

| # | Section | Content |
|---|---|---|
| 1 | Product hero | Badge `محصول ۱` (Product 1) · headline «حباب صندوق‌های طلا را قبل از بقیه ببینید» (See gold fund bubbles before everyone else) · CTAs `[شروع رایگان]` (start free) + `[دیدن نمونه داده]` (see sample data) |
| 2 | The problem | «قیمت هر صندوق طلا در بورس، به‌جای تبعیت دقیق از NAV، بیشتر تحت تأثیر عرضه و تقاضای لحظه‌ای معامله‌گران است. همین باعث می‌شود برخی صندوق‌ها بالاتر از ارزش واقعی‌شان معامله شوند (حباب بالا) و برخی نزدیک‌تر یا پایین‌تر (حباب پایین). چون دارایی پایه همه این صندوق‌ها یکسان است — گواهی سپرده سکه و شمش طلا — این اختلاف قیمت یک فرصت آربیتراژ می‌سازد.» + a scatter chart of "nominal bubble versus coin weight in the fund"<br>(English gloss: a listed gold fund's price is driven more by traders' moment-to-moment supply and demand than by strict adherence to NAV. As a result some funds trade above their true value (a high bubble) and others closer to or below it (a low bubble). Since every one of these funds holds the same underlying asset — coin and gold-bullion deposit certificates — that price gap creates an arbitrage opportunity.) |
| 3 | The solution | «خروج از صندوق حباب‌دار و ورود به صندوق کم‌حباب، بدون افزودن ریسک به پرتفو.» (Exit the inflated fund and enter the low-bubble one, without adding risk to the portfolio.) |
| 4 | **Four dashboard capabilities** | ← see the table below |
| 5 | Two benefits | **Benefit one — earning gold returns:** «۵ تا ۱۰ درصد سالانه از ارزش طلای موجود در پرتفو، به‌صورت طلای اضافه.» (5 to 10 percent a year on the gold held in the portfolio, paid in additional gold.)<br>**Benefit two — building credit from portfolio turnover:** «هر جابه‌جایی، گردش معاملاتی در کارگزاری ثبت می‌کند. کارگزاری‌ها بر اساس این گردش، اعتبار با نرخ ۳۰ تا ۴۰ درصد در اختیار مشتری می‌گذارند — نرخی که در برابر تورم بالای ۶۰ درصد، مقرون‌به‌صرفه است. این اعتبار داخل کارگزاری برای خرید طلا، خرید سهام یا ورود به استراتژی کاوردکال قابل استفاده است.» (Every switch registers trading turnover at the brokerage. Brokerages extend credit against that turnover at 30 to 40 percent — a rate that is economical against inflation above 60 percent. That credit can be used inside the brokerage to buy gold, buy equities, or enter the covered-call strategy.) |
| 6 | Live data sample | A real table with the columns `نماد` `آخرین` `زمان` `ارزش ذاتی` `حباب` `دلار تعدیل‌شده` (symbol, last, time, intrinsic value, bubble, adjusted USD) — the free plan shows only 5 rows, the rest blurred behind a lock |
| 7 | Why a gold fund | 6 benefits |
| 8 | Product FAQ | 5 questions |
| 9 | CTA + risk disclosure bar | |

**The four dashboard capabilities (taken directly from the product document):**

| Capability | Display details |
|---|---|
| 1. Price and key-indicator monitoring | Real-time prices for 18k gold, bullion, coin, the global ounce and USD; a real-time gold fund index and its intraday trend |
| 2. Bubble calculation and monitoring | Each fund's bubble versus NAV in real time; the intraday bubble trend and cross-fund comparison |
| 3. NAV trend monitoring | Three charts — `Latent NAV` · `Latent/Pure` · `Pure NAV` — per fund |
| 4. Asset-composition analysis | The share of coin, bullion and other instruments in each fund — used to detect correlation with the coin/USD price and to gauge risk |

---

### 6-3. Product page 2 — `/products/covered-call`

| # | Section | Content |
|---|---|---|
| 1 | Hero | Headline «بهره ثابت سالانه، بدون خروج از بازار سرمایه» (Fixed annual yield without leaving the capital market) · subheadline: «استراتژی کاوردکال امکان دستیابی به بهره ثابت سالانه ۶۰ تا ۱۰۰ درصد را با ریسک پایین فراهم می‌کند — فرصتی که در بازار سرمایه ایران کمتر شناخته شده است.» (The covered-call strategy makes a fixed annual yield of 60 to 100 percent achievable at low risk — an opportunity that is little known in the Iranian capital market.) |
| 2 | The problem | «ابزارهای درآمد ثابت متداول — سپرده بانکی، صندوق درآمد ثابت، اوراق اخزا — نرخ سالانه‌شان معمولاً از نرخ تورم عقب می‌ماند و در نهایت به کاهش ارزش واقعی دارایی منجر می‌شود.» (Conventional fixed-income instruments — bank deposits, fixed-income funds, treasury bills — typically pay an annual rate that trails inflation and ultimately erodes the asset's real value.) |
| 3 | **What a covered call is** | «کاوردکال به موقعیتی گفته می‌شود که با خرید یک سهم و فروش اختیار خرید (Call) همان سهم ساخته می‌شود. با این کار می‌توان تا حد زیادی جلوی ضرر ناشی از ریزش سهم را گرفت و در یک بازه زمانی مشخص به سود ثابت و از پیش تعیین‌شده دست یافت.» (A covered call is a position built by buying a stock and selling a call option on that same stock. Doing so largely limits the loss from a decline in the stock and delivers a fixed, predetermined profit over a defined window.) |
| 4 | **Worked numeric example** | ← see the block below — this is the most persuasive section on the page |
| 5 | **Profit-and-loss chart** | Rebuild the chart on the last page of the product document as an interactive SVG |
| 6 | Three delivery models | ← see the table below |
| 7 | Dashboard capabilities | A contract watchlist with the columns `نماد` `ask` `bid` `DTM` `K` `ITM` `نرخ سود دوره‌ای` `نرخ معادل سالانه` (symbol, ask, bid, DTM, K, ITM, period yield, annualized equivalent rate); filtering and sorting; automatic color-coding of the best opportunities; real-time monitoring of the existing portfolio (expiry, break-even point, distance to it) |
| 8 | Why an algorithm is needed | «تعداد قراردادهای اختیار خرید با قیمت‌های اعمال و سررسیدهای متفاوت بسیار زیاد است. موقعیت‌های جذاب در این انبوه، محدود و کمیاب‌اند و شناسایی و ورود به‌موقع به آن‌ها به‌صورت دستی عملاً غیرممکن است. اجرای موفق این استراتژی تنها با یک الگوریتم که به‌صورت دائمی بازار را پایش می‌کند ممکن است.» (The number of call contracts across different strikes and expiries is very large. Attractive positions within that mass are few and rare, and identifying and entering them in time by hand is effectively impossible. Executing this strategy successfully is only possible with an algorithm that monitors the market continuously.) |
| 9 | FAQ + CTA + risk disclosure | |

**The worked-example block (final copy — the numbers have been verified):**

> **فرض کنید موقعیتی با این شرایط باز می‌کنیم:**
> خرید سهم به قیمت **۳٬۰۰۰ تومان** و هم‌زمان فروش اختیار خرید با سررسید **۶۰ روزه** و قیمت اعمال **۲٬۵۰۰ تومان** به قیمت **۷۰۰ تومان**.
>
> (English gloss: Suppose we open a position on these terms: buy the stock at **3,000 toman** and simultaneously sell a call with a **60-day** expiry and a **2,500 toman** strike for **700 toman**.)
>
> | مشخصه | نماد | مقدار |
> |---|---|---|
> | قیمت خرید سهم | P | ۳٬۰۰۰ تومان |
> | قیمت اعمال | K | ۲٬۵۰۰ تومان |
> | قیمت اختیار فروخته‌شده | C | ۷۰۰ تومان |
> | مدت تا سررسید | DTM | ۶۰ روز |
>
> (Rows: stock purchase price · strike price · price of the option sold · days to maturity.)
>
> **نرخ سود معادل سالانه:** (annualized equivalent yield)
> $$\text{Covered Call Rate} = \left(\frac{K}{P-C}\right)^{\frac{365}{DTM}} - 1 = \left(\frac{۲۵۰۰}{۳۰۰۰-۷۰۰}\right)^{\frac{365}{60}} - 1 = ۶۶\%$$
>
> **حاشیه ریسک:** (risk margin)
> $$\frac{P}{K} - 1 = \frac{۳۰۰۰}{۲۵۰۰} - 1 = ۲۰\%$$
>
> **سه سناریو در سررسید:** (three scenarios at expiry)
> - 🟢 **حالت مطلوب** — تا زمانی که قیمت سهم در روز سررسید بالای ۲٬۵۰۰ تومان بماند (یعنی ریزشی معادل ۲۰ درصد یا بیشتر در بازه ۶۰ روزه رخ ندهد)، نرخ سود معادل **۶۶ درصد سالانه** محقق می‌شود.
>   (Favorable case — as long as the stock stays above 2,500 toman on the expiry date, i.e. no drop of 20 percent or more occurs over the 60-day window, the equivalent yield of **66 percent a year** is realized.)
> - 🟡 **حالت ریزش سهم** — اگر قیمت سهم زیر ۲٬۵۰۰ تومان (قیمت اعمال) بیاید، خریدار اختیار، سهم را با قیمت اعمال خریداری نخواهد کرد و سهم در پرتفو باقی می‌ماند.
>   (Stock-decline case — if the stock falls below 2,500 toman (the strike), the option buyer will not exercise at the strike and the stock stays in the portfolio.)
> - 🔴 **نقطه سربه‌سری** — تا زمانی که قیمت سهم بالای **۲٬۳۰۰ تومان** (قیمت اعمال منهای قیمت اختیار فروخته‌شده) بماند، ضرری متوجه پرتفو نخواهد شد و صرفاً سود موقعیت از دست می‌رود. تنها با ریزش زیر این سطح، موقعیت وارد ضرر می‌شود.
>   (Break-even point — as long as the stock stays above **2,300 toman** (the strike minus the premium received), the portfolio takes no loss and only the position's profit is forgone. Only a fall below that level puts the position into a loss.)

**The three delivery models (taken directly from the product document):**

| Model | Description |
|---|---|
| 1. Standalone covered-call portfolio | The strategy is run separately, with no dependency on the gold portfolio; suited to an investor whose only goal is a fixed, relatively assured yield from the equity market. |
| 2. Combined with a gold portfolio | Part of the capital sits in gold (with its security and inflation-hedging benefits) and part in covered calls; this mix lowers overall portfolio risk and produces a more balanced return. |
| 3. Executed against gold credit | No new cash required: the credit generated by arbitrage and gold-fund turnover flows directly into the covered-call strategy. In effect this produces a return without tying up the client's principal. |

---

### 6-4. Pricing page `/pricing` ← **the most important conversion page**

The structure is taken directly from the Rahavard pattern.

#### Layout, top to bottom

1. **Headline:** «پلن مناسب خود را انتخاب کنید» (Choose the plan that suits you)
   **Subheadline:** «همه پلن‌ها ۷ روز رایگان، بدون نیاز به کارت بانکی. هر زمان بخواهید لغو کنید.» (Every plan comes with 7 days free, no bank card required. Cancel whenever you want.)

2. **Period toggle** (a three-state pill): `ماهانه` · `۳ ماهه` · `سالانه` (monthly · 3 months · annual)
   Next to it, a gold discount bar: `تا ۳۰٪ تخفیف با پرداخت سالانه` (up to 30% off with annual billing)

3. **Three plan cards** (the middle one emphasized):

| | 🔓 **پایه** (Basic) | 🟡 **طلا** (Gold) ⭐محبوب‌ترین (most popular) | 💎 **حرفه‌ای** (Professional) |
|---|---|---|---|
| **Who it is for** | آشنایی با پلتفرم (getting to know the platform) | دارندگان صندوق طلا (gold fund holders) | معامله‌گران حرفه‌ای (professional traders) |
| **Monthly price** | رایگان (free) | `{{ ۱٬۹۰۰٬۰۰۰ }}` تومان | `{{ ۳٬۹۰۰٬۰۰۰ }}` تومان |
| **Annual price** | — | `{{ ۱٬۳۳۰٬۰۰۰ }}` تومان/ماه | `{{ ۲٬۷۳۰٬۰۰۰ }}` تومان/ماه |
| Gold arbitrage dashboard | Top 5 funds | ✓ All funds | ✓ All funds |
| Covered-call dashboard | — | — | ✓ Full |
| Data delay | 15 minutes | Real-time | Real-time |
| Data history | 1 day | 6 months | Unlimited |
| Bubble alerts | 1 alert | 20 alerts | Unlimited |
| Covered-call opportunity alerts | — | — | ✓ |
| Fund asset-composition analysis | — | ✓ | ✓ |
| NAV monitoring (Latent/Pure) | — | ✓ | ✓ |
| Covered-call profit-and-loss chart | — | — | ✓ |
| Excel export | — | ✓ | ✓ |
| API access | — | — | ✓ |
| Support | Online guide | Ticketing (24-hour) | Dedicated phone line |
| **Button** | `شروع رایگان` (start free) | `خرید اشتراک طلا` (buy Gold) | `خرید اشتراک حرفه‌ای` (buy Professional) |

   Under each card, a `ویژگی‌ها و مقایسه ↓` (features and comparison ↓) link that scrolls to the full table.

4. **Enterprise plan bar** (full width, dark background):
   > **پلن سازمانی و مدیریت پرتفوی** (Enterprise plan and portfolio management)
   > «اجرای خودکار الگوریتم روی حساب کارگزاری شما، گزارش اختصاصی، و دسترسی چندکاربره برای تیم‌های سرمایه‌گذاری.» (Automated execution of the algorithm on your brokerage account, dedicated reporting, and multi-user access for investment teams.)
   > `[درخواست مشاوره]` (request a consultation) → lead form

5. **Full comparison table** — every feature, with a header that sticks while scrolling; on mobile it becomes collapsible cards.

6. **Payment trust bar:** payment gateway logo, `پرداخت امن` (secure payment), `صدور فاکتور رسمی` (official invoicing), `لغو در هر زمان` (cancel anytime), `بازگشت وجه تا ۷ روز` (refund within 7 days)

7. **Purchase FAQ** (7 items — following the Rahavard pattern):
   - آیا می‌توانم قبل از خرید، داشبورد را ببینم؟ (Can I see the dashboard before buying?)
   - تفاوت پلن طلا و حرفه‌ای در عمل چیست؟ (What is the practical difference between the Gold and Professional plans?)
   - امکان ارتقای پلن در میانه دوره وجود دارد؟ (Can I upgrade mid-period?)
   - داده‌ها از چه منبعی و با چه تأخیری می‌آیند؟ (What is the data source and what is the delay?)
   - اگر اشتراکم تمام شود، هشدارها و تنظیماتم را از دست می‌دهم؟ (If my subscription ends, do I lose my alerts and settings?)
   - آیا فاکتور رسمی صادر می‌شود؟ (Is an official invoice issued?)
   - برای خرید سازمانی چطور اقدام کنم؟ (How do I arrange an enterprise purchase?)

> **Pricing note:** the numbers above are proposals, calibrated against comparable products in the market — Bambo charges 2,390,000 toman monthly and 14,490,000 toman annually; Rahavard's Gold is 570,000 and Platinum 2,535,000 toman monthly. Your product is more specialized than Rahavard and narrower than Bambo, so it sits above Rahavard's range and near Bambo's. The final number is yours to set.

---

### 6-5. Performance page `/performance`

(A rewrite of the v1 `Performance.dc.html` page)

- **Hero:** «عملکرد الگوریتم، عدد به عدد» (The algorithm's performance, number by number) + a methodology bar: `بازه: {{ }}` (window) · `منبع داده: {{ }}` (data source) · `آخرین به‌روزرسانی: {{ }}` (last updated)
- **Four KPIs:** algorithm return · plain gold-fund buy-and-hold return · excess return · maximum drawdown
- **Main chart:** the algorithm versus buy-and-hold — with a range selector (1 month / 3 months / 6 months / 1 year)
- **Monthly return table** — month by month, with green/red cells
- **The «الگوریتم دقیقاً چه کاری انجام می‌دهد» (exactly what the algorithm does) section** (from v1)
- **Methodology and limitations block** — fees, slippage, and this sentence:
  > «عملکرد گذشته تضمینی برای بازده آینده نیست. ارقام ارائه‌شده پس از کسر کارمزد معاملات محاسبه شده و بر پایه داده {{ منبع }} در بازه {{ تاریخ }} است.»
  > (Past performance is no guarantee of future returns. The figures shown are net of trading fees and are based on {{ source }} data over the {{ date }} window.)

---

### 6-6. Other pages (summary)

| Page | Structure |
|---|---|
| `/services` | Execution-service hero · **the algorithm's four-step process** (monitor ← analyze ← identify ← act; relocated from the home page) · the three covered-call delivery models · the onboarding process · minimum capital · lead form |
| `/market` | ← Section 6-7 |
| `/wiki` | ← Section 8 (content strategy) |
| `/about` | Keep in full from v1: «از یک مشاهده ساده شروع شد» (it started with a simple observation) / «دو تخصص، یک محصول» (two disciplines, one product) / «اصولی که به آن پایبندیم» (the principles we hold to) + add a team grid and a timeline |
| `/faq` | Organized into 4 groups: product · data · subscription and payment · risk |
| `/contact` | From v1 + add a map, response hours, and a "subject" selector (sales / technical support / enterprise) |
| `/legal/risk` | **Mandatory** — full risk disclosure; sample text in Section 13 |

---

### 6-7. Market page `/market` — the gold market pulse (free)

The Optionbaaz "market pulse" pattern, but more compact and focused on gold. **This page is open without registration** and does two jobs: attracting daily organic traffic, and proving data quality.

| # | Section | Content |
|---|---|---|
| 1 | Status bar | `بازار باز است` / `بازار بسته است` (market open / closed) · `آخرین روز معاملاتی: {{ }}` (last trading day) · `آخرین به‌روزرسانی: {{ }}` (last updated) |
| 2 | **4 gold market KPIs** | `میانگین حباب صندوق‌ها` (average fund bubble) · `پرحباب‌ترین صندوق` (highest-bubble fund) · `کم‌حباب‌ترین صندوق` (lowest-bubble fund) · `ارزش معاملات صندوق‌های طلا` (gold fund trading value) — each with a delta versus yesterday |
| 3 | **Fund bubble table** `/market/funds` | Columns: `نماد` `آخرین قیمت` `NAV` `حباب` `ارزش معاملات` `زمان` (symbol, last price, NAV, bubble, trading value, time) — freely sortable; the first 5 rows for guests, the rest with a free account |
| 4 | **Spot prices** `/market/gold` | طلای ۱۸ عیار · مثقال · گواهی شمش · گواهی سکه · سکه امامی · اونس جهانی · دلار (18k gold · mithqal · bullion certificate · coin certificate · Emami coin · global ounce · USD) — numeric cards with sparklines |
| 5 | Scatter chart | "Nominal bubble versus coin weight in the fund" — your signature brand chart |
| 6 | Intraday bubble trend | A multi-series line chart with fund selection |
| 7 | Upgrade CTA | «این جدول با تأخیر ۱۵ دقیقه است. نسخه لحظه‌ای + هشدار + تاریخچه، در پلن طلا.» (This table is on a 15-minute delay. The real-time version + alerts + history come with the Gold plan.) |
| 8 | SEO prose block | 600–800 words: «حباب صندوق طلا چیست و چطور محاسبه می‌شود؟» (What is a gold fund bubble and how is it calculated?) with internal links into the knowledge base |

> **Critical rule:** during trading hours this page must refresh every 30 seconds and show a real timestamp. A "live data" page that is stale does more damage than no page at all.

---

### 6-8. Footer (all pages)

Five columns: **محصولات** (Products) · **شرکت** (Company) · **منابع** (Resources) · **قوانین** (Legal) · **تماس و شبکه‌های اجتماعی** (Contact and social)
Bottom bar: `© ۱۴۰۴ الف کپیتال` + registration number + the e-commerce trust seal + a **thin risk disclosure bar**.

---

## 7. Subscription and Account Flow

```
Landing page ──► [شروع رایگان] ──► Sign up with mobile ──► OTP verification
                                                                │
                                                                ▼
                              3-question onboarding (investor type / portfolio size / interest)
                                                                │
                                                                ▼
                    Basic-plan dashboard (locked features with a 🔒 icon and an "upgrade" label)
                                                                │
                                                                ▼
                    Pricing page ──► Payment (Iranian gateway) ──► Instant activation
```

**Key rules:**

- Sign-up is **mobile + OTP only**. A password is optional and can come later.
- No bank card requested for the free trial.
- Locked features must be **visible** (blurred with a lock over them), not hidden — this is the strongest upgrade driver.
- 3 days before expiry: an in-app warning + an SMS.
- Payment gateway: Zarinpal or a direct bank gateway. Support discount codes and referral codes (the Rahavard pattern).

---

## 8. Content Strategy and the Knowledge Base

### 8-1. Why a "knowledge base" and not a "blog"

A blog is a **time-ordered stream**: posts go stale, the archive becomes useless, and you have to produce new content constantly or the traffic dies. A knowledge base is a **tree structure**: every article has a defined place in the map, it gets updated rather than replaced, and internal links between articles build a semantic network that Persian Google weights heavily. Optionbaaz did exactly this, and that is why it ranks on specialized options keywords.

**Decision: the `/wiki` route with five fixed categories.** Also add a `/wiki/news` section for time-bound material (announcements, monthly market reports), but keep it secondary.

### 8-2. Knowledge base architecture

```
/wiki                          Hub — a 5-category grid + flagship article + search
│
├── /wiki/gold-funds           Gold funds and ETFs
├── /wiki/arbitrage            Arbitrage, the bubble and NAV
├── /wiki/options              Options and covered calls
├── /wiki/risk                 Risk and capital management
├── /wiki/guides               Dashboard usage guides
└── /wiki/news                 Periodic market reports (secondary)
```

**The `/wiki` hub page:** headline «دانشنامه الف کپیتال — مرجع صندوق‌های طلا و اختیار معامله» (The Alef Capital knowledge base — the reference for gold funds and options) · internal search · 5 category cards with article counts · a "پیشنهاد مطالعه" (suggested reading) block with a real abstract (the Optionbaaz pattern) · "پرخواننده‌ترین‌ها" (most read).

### 8-3. Article page template

| Part | Specification |
|---|---|
| Breadcrumb | `دانشنامه ← آربیتراژ و حباب ← حباب صندوق طلا چیست` (Knowledge base ← Arbitrage and the bubble ← What is a gold fund bubble) |
| Header | `h1` title · reading time · last-updated date (not the publication date) · author with photo |
| **"در یک نگاه" (at a glance) box** | 3 to 5 summary bullets, before the main body — this produces the highest retention rate |
| Table of contents | Sticky in the desktop sidebar, collapsible on mobile |
| Body | 720px wide · `line-height:2` · `h2`/`h3` · pull quotes |
| **Live data block** | At least one real data card inside the body — for example «حباب صندوق‌های طلا، همین الان» (gold fund bubbles, right now) |
| **Embedded tool** | In key articles, an interactive calculator (the covered-call calculator, the bubble calculator) |
| Mid-body CTA | After roughly 60% scroll, a card related to the product — not a pop-up |
| Related articles | 3 cards from the same category |
| Closing CTA | Tied to the product relevant to the article's topic |
| Structured data | `Article` + `FAQPage` (if the article has a questions section) + `BreadcrumbList` |

### 8-4. Initial content map — 24 articles

Each article with its target keyword, search intent, and the product it connects to:

**Category 1 — Gold funds and ETFs** (intent: educational, top of funnel)

| # | Title | Target keyword | Connects to |
|---|---|---|---|
| 1 | صندوق طلا چیست و چطور کار می‌کند؟ (What is a gold fund and how does it work?) | `صندوق طلا` | `/market` |
| 2 | مقایسه کامل صندوق‌های طلای بورس تهران (A full comparison of Tehran-listed gold funds) | `بهترین صندوق طلا` | `/market/funds` |
| 3 | صندوق طلا یا طلای فیزیکی؟ مقایسه شش‌بعدی (Gold fund or physical gold? A six-dimension comparison) | `صندوق طلا یا طلای فیزیکی` | Product 1 |
| 4 | معافیت مالیاتی و کارمزد صندوق‌های طلا (Tax exemption and fees for gold funds) | `مالیات صندوق طلا` | Product 1 |
| 5 | گواهی سپرده سکه و شمش طلا چیست؟ (What is a coin and gold-bullion deposit certificate?) | `گواهی سپرده سکه` | `/market/gold` |

**Category 2 — Arbitrage, the bubble and NAV** (intent: specialized, mid-funnel — **your most important category**)

| # | Title | Target keyword | Connects to |
|---|---|---|---|
| 6 | حباب صندوق طلا چیست و چگونه محاسبه می‌شود؟ (What is a gold fund bubble and how is it calculated?) | `حباب صندوق طلا` | `/market/funds` + the bubble calculator |
| 7 | NAV چیست؟ تفاوت NAV ابطال، صدور و لحظه‌ای (What is NAV? Redemption, issuance and real-time NAV) | `NAV صندوق` | Product 1 |
| 8 | آربیتراژ بین صندوق‌های طلا چگونه سود می‌سازد؟ (How does arbitrage between gold funds generate profit?) | `آربیتراژ صندوق طلا` | Product 1 |
| 9 | چرا حباب صندوق‌ها با هم فرق دارد؟ نقش ترکیب دارایی (Why do fund bubbles differ? The role of asset composition) | `ترکیب دارایی صندوق طلا` | Product 1 |
| 10 | اعتبار کارگزاری از محل گردش معاملاتی چطور ساخته می‌شود؟ (How is brokerage credit built from trading turnover?) | `اعتبار کارگزاری` | Product 1 |
| 11 | Latent NAV و Pure NAV — دو نگاه به ارزش واقعی صندوق (Latent NAV and Pure NAV — two views of a fund's true value) | `latent nav` | Product 1 |

**Category 3 — Options and covered calls** (intent: specialized, mid to bottom of funnel)

| # | Title | Target keyword | Connects to |
|---|---|---|---|
| 12 | کاوردکال چیست؟ راهنمای کامل با مثال عددی (What is a covered call? A complete guide with a worked example) | `کاوردکال` | Product 2 + **the calculator** |
| 13 | نرخ سود معادل سالانه چطور محاسبه می‌شود؟ (How is the annualized equivalent yield calculated?) | `نرخ سود معادل سالانه` | Product 2 + the calculator |
| 14 | نقطه سربه‌سری در کاوردکال — کجا وارد ضرر می‌شویم؟ (The break-even point in a covered call — where do we start losing?) | `نقطه سربه سری کاوردکال` | Product 2 |
| 15 | حاشیه ریسک (ITM) در اختیار خرید یعنی چه؟ (What does risk margin (ITM) mean for a call option?) | `حاشیه ریسک اختیار معامله` | Product 2 |
| 16 | DTM، قیمت اعمال و سررسید — الفبای قرارداد اختیار (DTM, strike price and expiry — the basics of an option contract) | `قیمت اعمال اختیار معامله` | Product 2 |
| 17 | چرا شناسایی دستی فرصت‌های کاوردکال شکست می‌خورد (Why manually spotting covered-call opportunities fails) | `استراتژی کاوردکال` | Product 2 |
| 18 | کاوردکال در برابر سپرده بانکی و صندوق درآمد ثابت (Covered calls versus bank deposits and fixed-income funds) | `بهترین سرمایه گذاری بدون ریسک` | Product 2 |

**Category 4 — Risk and capital management**

| # | Title | Target keyword |
|---|---|---|
| 19 | تورم و ارزش واقعی دارایی — چرا سود اسمی گمراه‌کننده است (Inflation and real asset value — why nominal returns mislead) | `تورم و سرمایه گذاری` |
| 20 | چگونه پرتفوی طلا و سهام را متوازن کنیم؟ (How to balance a gold and equity portfolio) | `تنوع بخشی پرتفوی` |
| 21 | ریسک‌های استراتژی کاوردکال که کمتر گفته می‌شود (The covered-call risks that are rarely mentioned) | `ریسک کاوردکال` |
| 22 | معاملات الگوریتمی در بورس ایران — امکانات و محدودیت‌ها (Algorithmic trading on the Iranian exchange — what is possible and what is not) | `معاملات الگوریتمی بورس` |

**Category 5 — Dashboard guides** (intent: existing users, raising activation and retention)

| # | Title |
|---|---|
| 23 | راهنمای داشبورد آربیتراژ: از باز کردن تا اولین سیگنال (Arbitrage dashboard guide: from opening it to your first signal) |
| 24 | راهنمای دیدبان کاوردکال: فیلترها، ستون‌ها و هشدارها (Covered-call watchlist guide: filters, columns and alerts) |

### 8-5. Interactive in-content tools (the conversion lever)

These are standalone pages and are also embedded inside articles. **The highest return on investment in the entire content project.**

| Tool | Route | User input | Output | Sales hook |
|---|---|---|---|---|
| **Covered-call calculator** | `/tools/covered-call-calculator` | P, K, C, DTM | Annualized equivalent rate, risk margin, break-even point, profit-and-loss chart | «امروز {{ ۱۲ }} موقعیت با نرخ بالاتر از این در بازار هست 🔒» (there are {{ 12 }} positions in the market today with a higher rate 🔒) |
| **Fund bubble calculator** | `/tools/bubble-calculator` | Fund symbol | Real-time bubble + comparison against the average | «تاریخچه ۶ ماهه این صندوق را ببینید 🔒» (see this fund's 6-month history 🔒) |
| **Fund comparator** | `/tools/fund-comparison` | Pick 2–4 funds | A table of bubble, NAV and asset composition | «هشدار بگذارید 🔒» (set an alert 🔒) |

### 8-6. Distribution channels

| Channel | Role | Cadence |
|---|---|---|
| **Organic SEO** | The main engine — 60% of target traffic | 4 articles per month |
| **Telegram** | The primary channel for Iran's financial audience | Daily: an end-of-day bubble summary + a link to `/market` |
| **Email / SMS** | Retention | A weekly Friday-night digest + real-time alerts |
| **LinkedIn** | Professional credibility and enterprise leads | Weekly: deeper analysis |
| **Short video** | Quick introduction | 2 videos a month: «حباب صندوق طلا در ۹۰ ثانیه» (the gold fund bubble in 90 seconds) |

### 8-7. Content quality rules

- **Every article must contain a real number from your own data.** This is what competitors cannot copy and the main reason you will rank.
- **Show the "last updated" date, not the publication date.** Update the article instead of writing a new one.
- **No keyword stuffing.** Write natural Persian; Persian Google responds better to human prose — see the Optionbaaz prose block.
- **At least 3 internal links per article** to same-category articles, plus 1 link to the relevant product page.
- **No article recommends buying a specific symbol.** Analysis yes, recommendations no — it is both a legal risk and a credibility burner.
- Target length: educational articles 1,200–1,800 words; specialized articles 2,000+ words.

---

## 9. Mobile and Responsive

Breakpoints: `sm 640` · `md 768` · `lg 1024` · `xl 1280`

| Element | Mobile behavior |
|---|---|
| Main menu | Full-screen hamburger + a 5-item bottom nav bar |
| Hero | Single column, illustration below the copy, data cards scroll horizontally |
| Product cards | Single column, full width |
| Plan cards | Horizontal scroll with pagination dots; the popular plan centered by default |
| Comparison table | Becomes an accordion, one per plan |
| Market tables | Horizontal scroll with a sticky symbol column |
| Charts | Fixed height of 280px, legend below the chart |

**Critical:** more than 70% of Iranian financial traffic is mobile. **Design mobile first.**

---

## 10. SEO and Metadata

| Page | Title | Meta description |
|---|---|---|
| `/` | الف کپیتال — داشبورد آربیتراژ صندوق طلا و کاوردکال بورس تهران | پایش لحظه‌ای حباب صندوق‌های طلا و فرصت‌های کاوردکال. دو داشبورد تخصصی برای کسب بازده کم‌ریسک. ۷ روز رایگان. |
| `/products/gold-arbitrage` | داشبورد آربیتراژ صندوق‌های طلا | حباب و NAV همه صندوق‌های طلای بورس تهران، لحظه‌ای. شناسایی صندوق ارزنده و سیگنال جابه‌جایی. |
| `/products/covered-call` | داشبورد کاوردکال — بهره ثابت سالانه | دیدبان قراردادهای اختیار خرید با نرخ سود معادل سالانه و حاشیه ریسک. |
| `/pricing` | پلن‌ها و قیمت اشتراک الف کپیتال | سه پلن با پرداخت ماهانه یا سالانه. ۷ روز رایگان بدون کارت بانکی. |
| `/market` | حباب لحظه‌ای صندوق‌های طلای بورس تهران | جدول زنده حباب و NAV همه صندوق‌های طلا، قیمت طلای ۱۸ عیار، سکه و اونس جهانی. رایگان. |
| `/wiki` | دانشنامه صندوق طلا، آربیتراژ و اختیار معامله | مرجع آموزشی حباب، NAV، آربیتراژ و کاوردکال با مثال عددی و داده واقعی بازار ایران. |

(Titles and meta descriptions are shipped copy and stay in Persian. In order: home — Alef Capital, gold fund arbitrage and Tehran covered-call dashboard; gold arbitrage product; covered-call product — fixed annual yield; pricing — Alef Capital plans and subscription prices; market — real-time bubbles for Tehran-listed gold funds; wiki — the gold fund, arbitrage and options knowledge base.)

- Target keywords: `حباب صندوق طلا` · `آربیتراژ صندوق طلا` · `NAV صندوق طلا` · `بهترین صندوق طلا` · `کاوردکال` · `نرخ سود معادل سالانه` · `اختیار معامله بورس تهران` · `بهره ثابت سالانه`
- Structured data: `Organization` · `Product` + `Offer` (on `/pricing`) · `FAQPage` (on every page with an FAQ) · `Article` (on knowledge base articles) · `BreadcrumbList` (on every knowledge base page)
- **Internal linking rule:** every knowledge base article ← 3 same-category articles + 1 product page. Every product page ← 2 related articles. `/market` ← the arbitrage category of the knowledge base. This network is what builds rankings.
- `sitemap.xml` · `robots.txt` · `hreflang="fa-IR"` · a dedicated `og:image` for each product page

---

## 11. Performance and Accessibility

**Performance budget:** LCP < 2.5s · CLS < 0.1 · INP < 200ms · initial JS payload < 180KB gzipped

- Self-host the Vazirmatn font with `font-display:swap` and a Persian subset — not from Google's CDN (which is slow or blocked in Iran).
- Images in `WebP`/`AVIF` with `loading="lazy"` and explicit dimensions.
- Load the charting library via `dynamic import`, only on pages that have charts.
- **Host inside Iran** — network latency for Iranian users translates directly into conversion rate.

**Accessibility (WCAG 2.1 AA):**

- Text contrast ≥ 4.5:1. ⚠️ Gold text on white does not have enough contrast — use `--gold-700` for text, not `--gold-400`.
- Color must never be the sole carrier of meaning: put a `▲`/`▼` marker next to green/red.
- Every control is keyboard operable, with a 2px gold `focus-visible` ring.
- Data tables use `<caption>`, `<th scope>` and Persian `aria-label`s.
- Respect `prefers-reduced-motion` (the hero SVG animations).

---

## 12. Proposed Tech Stack

| Layer | Proposal | Why |
|---|---|---|
| Framework | **Next.js 14+ (App Router)** | SSR for Persian SEO, API routes, image optimization |
| Styling | **Tailwind CSS** + an RTL plugin (`tailwindcss-rtl`) or `logical properties` | Build speed, RTL compatibility |
| Components | shadcn/ui with a custom gold-and-navy theme | |
| Charts | **ECharts** (`echarts-for-react`) | Better RTL and Persian label support than Chart.js |
| Tables | TanStack Table | Filtering, sorting, virtualization for 368 contracts |
| Live data | WebSocket or SSE with a fallback to 5-second polling | |
| Backend | **FastAPI + PostgreSQL** (compatible with your current stack) | Time-series data; `TimescaleDB` for NAV history |
| Authentication | SMS OTP (Kavenegar / Melipayamak) + JWT | |
| Payments | Zarinpal or a direct gateway | |
| Analytics | Google Analytics 4 + one Iranian tool (Yektanet/Metrix) | |

**Architecture note:** your current dashboards are built with **Dash**. The low-cost path is to keep Dash for the dashboard application (`app.alefcapital.com`) and build the marketing site with Next.js (`alefcapital.com`) — with a shared authentication layer. **Do not pull a dashboard rewrite into this project.**

---

## 13. Mandatory Legal and Risk Copy

**Risk disclosure bar (at the bottom of every product page and the pricing page):**

> «اطلاعات ارائه‌شده در این وب‌سایت صرفاً جنبه تحلیلی و اطلاع‌رسانی دارد و توصیه به خرید یا فروش هیچ اوراق بهاداری محسوب نمی‌شود. سرمایه‌گذاری در بازار سرمایه با ریسک همراه است و مسئولیت تصمیم‌های معاملاتی بر عهده کاربر است. بازده گذشته تضمینی برای بازده آینده نیست.»
> (English gloss: the information provided on this website is analytical and informational only and does not constitute a recommendation to buy or sell any security. Investing in the capital market carries risk and responsibility for trading decisions rests with the user. Past returns are no guarantee of future returns.)

**Next to every return figure:**
> `* بر اساس داده {{ منبع }} در بازه {{ تاریخ شروع }} تا {{ تاریخ پایان }}، پس از کسر کارمزد.`
> (* Based on {{ source }} data from {{ start date }} to {{ end date }}, net of fees.)

**In the covered-call section:**
> «بازده اعلام‌شده در صورت تحقق سناریوی مطلوب و تا سقف حاشیه ریسک محاسبه‌شده است. در صورت ریزش قیمت سهم به زیر نقطه سربه‌سری، موقعیت وارد زیان می‌شود.»
> (The stated return assumes the favorable scenario is realized and is computed up to the calculated risk margin. If the stock falls below the break-even point, the position moves into a loss.)

⚠️ The phrases «تضمین‌شده» (guaranteed), «بدون ریسک» (risk-free) and «سود قطعی» (certain profit) must not appear anywhere on the site.

---

## 14. Phase Prioritization

| Phase | Scope | Output | Estimated duration |
|---|---|---|---|
| **Phase 1 — sales MVP** | `/` · both product pages · `/pricing` · `/about` · `/faq` · `/contact` · `/legal/*` + OTP sign-up and payments | A site that can sell | 3–4 weeks |
| **Phase 2 — data and trust** | `/market` with live data · `/performance` · `/services` · real dashboard screenshots · the home page KPI bar | A jump in conversion rate and returning traffic | 3 weeks |
| **Phase 3 — content** | `/wiki` with the first 12 articles (categories 2 and 3 take priority) · the covered-call calculator · the SEO prose blocks | The organic traffic engine switches on | 4 weeks + ongoing production |
| **Phase 4 — retention** | Alerts · the weekly digest · the remaining 12 articles · PWA · API access | Lower churn, higher renewals | Ongoing |

> **Do not reorder these.** Content (phase 3) is ineffective without live data (phase 2), because every article's competitive advantage is that "real number from your own data".

---

## 15. Delivery Checklist

- [ ] `dir="rtl" lang="fa"` on `<html>`; every directional icon mirrored
- [ ] Vazirmatn self-hosted with a Persian subset
- [ ] No return figure without a source and a time window
- [ ] No fake testimonials or client logos
- [ ] A risk disclosure bar on every product page and the pricing page
- [ ] Mobile: bottom nav bar + horizontally scrolling plan cards
- [ ] The plan comparison table becomes an accordion on mobile
- [ ] Every CTA lands on a real destination (no `href="#"`)
- [ ] Forms with Persian error messages and Iranian mobile-number validation
- [ ] LCP under 2.5 seconds on mobile over a 3G connection
- [ ] Contrast: gold text uses `--gold-700`
- [ ] `sitemap.xml`, `robots.txt`, `Product`+`Offer` structured data
- [ ] A Persian 404 page linking to the products
- [ ] Test on iOS Safari (Persian rendering differs there)
- [ ] `/market` and the whole knowledge base must be open **without login** (SEO)
- [ ] Every article: ≥3 internal links + 1 product link + one real number from your own data
- [ ] Locked features are blurred and visible, not hidden
- [ ] A real timestamp on every piece of live data (`آخرین به‌روزرسانی: HH:MM` — last updated: HH:MM)

---

## Appendix — Mapping the Product Document's Content to Site Pages

| Section of the "Financial Products Introduction" document | Destination on the site |
|---|---|
| Gold funds and their 6 benefits | `/` section 6 + `/products/gold-arbitrage` section 7 |
| Arbitrage between gold funds · the bubble concept | `/products/gold-arbitrage` sections 2 and 3 |
| Benefit one: earning gold returns (5–10%) | `/products/gold-arbitrage` section 5 + the product card on `/` |
| Benefit two: building credit from portfolio turnover | `/products/gold-arbitrage` section 5 |
| The four arbitrage dashboard capabilities | `/products/gold-arbitrage` section 4 + the `/pricing` feature table |
| The fixed annual yield strategy (60–100%) | `/products/covered-call` hero and section 2 |
| Definition of a covered call | `/products/covered-call` section 3 |
| The three strategy execution models | `/products/covered-call` section 6 + `/services` |
| The worked example and the annualized equivalent rate formula | `/products/covered-call` section 4 |
| The profit-and-loss chart and the break-even point | `/products/covered-call` section 5 |
| The contract watchlist and Algo Manager | `/products/covered-call` section 7 |
| The necessity of an algorithm (scarcity of positions) | `/products/covered-call` section 8 |
