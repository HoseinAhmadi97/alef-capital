# Gold section — data needs, mapped to Nexus

Every number on the gold pages, where it comes from, and what does not
exist yet. Checked against the live datasources on `alpha` (2026-09-16).

Status legend:

- **nexus** — served by Nexus today
- **added** — the data exists on the server; this change adds it to Nexus
- **missing** — no datasource on the server has it; see the gap list at the end

## 1. How the site gets the data

```
market_fetcher ─┐                         (one process reads the market)
atlas ──────────┼─► Redis / Postgres
gold-algo ──────┘          │
                           ▼
            Nexus  — rebuilds ONE gold snapshot every 10 s in the background
                           │  GET /v1/gold/snapshot  (cached bytes, ETag)
                           ▼
            nginx  — /api/gold/snapshot, 5 s micro-cache
                           │
                           ▼
            browser — site/gold-data.js: one fetch per page, polls every
                      20 s only while the tab is visible, 304 when unchanged
```

Why this shape:

- **Visitors never cause a database query.** The snapshot is built on a
  timer, not per request, so 1 or 1,000 visitors cost the same upstream.
- **One request per page.** Every gold page reads the same ~4 KB (gzipped)
  document instead of calling several endpoints.
- **Hidden tabs cost nothing.** Polling pauses while the tab is in the
  background and resumes with an immediate refresh when it comes back.
- **The HTML stays static.** nginx still serves pages from `dist/`; only the
  numbers are filled in by the browser.

## 2. Existing Nexus gold structure

| Endpoint | What it has |
|---|---|
| `GET /v1/gold/market` | ons, geram18, geram24, sekee, govahi_sekke, govahi_shemsh, dollar — price, source, time |
| `GET /v1/gold/funds` | 31 funds — last trade, bid/ask, value, volume, NAV (TSE live, tadbir, farabi), nominal bubble, monthly weights |

This change **extends those two** (more fields and instruments) and adds
`GET /v1/gold/snapshot`, which composes them plus summary stats and two
intraday series. No parallel data path is introduced.

## 3. Needs by page

### Every page — price ticker

| Item | Status | Source |
|---|---|---|
| 18k gold gram + day change | added (change) | estjt `geram18` |
| Mesghal (melted gold) | added | tabdeal `gold_melt` — *confirm this is the intended mesghal price* |
| Gold bar certificate | added (change) | IME `GoldBar` |
| Gold coin certificate | added (change) | IME `GoldCoin` |
| Emami coin | added (change) | estjt `sekee_new` |
| Ounce | added (change) | estjt `ons_tala` |
| Dollar | added (change) | avg(wallex USDTTMN, tabdeal dollar) |
| Gold funds index | **missing** | — replaced by the funds' average daily return until an index exists |

Day change for Atlas instruments = latest price vs the last tick before
Tehran midnight in `atlas.raw_ticks`.

### Home

| Item | Status |
|---|---|
| Bubble of every fund, average / min / max | nexus |
| 18k gold price, day change | added |
| 18k gold intraday sparkline | added (`series.geram18`, from `atlas.raw_ticks`) |

### Product — gold arbitrage

| Item | Status |
|---|---|
| Bubble distribution, average / min / max | nexus |
| Scatter: bubble vs coin weight | nexus (bubble + `weights.sekke_weight`) |

### Market pulse

| Item | Status |
|---|---|
| Average / max / min bubble | nexus |
| Average bubble vs yesterday | **missing** (no fund price history) |
| Total traded value of gold funds | added (sum of `value`) |
| Traded value vs weekly average | **missing** (no fund trade history) |
| Funds table: price, NAV, bubble, value, time | added (`trade_time`) |
| Base prices with day change (8 tiles) | added |
| Scatter: bubble vs coin weight | nexus |
| Intraday bubble of 5 funds | **missing** (no fund price history) |

### Gold dashboard

| Item | Status |
|---|---|
| Tiles: ounce, 18k gold, dollar with change and time | added |
| Tile: gold funds index | **missing** |
| Average / max / min bubble, total traded value | nexus / added |
| Funds table: price, day change %, day change, NAV, bubble, implied dollar, time | added (`change`, `change_pct`, `trade_time`); implied dollar = dollar × price / NAV |
| Spot table: price and day change for 18k, emami, bahar, half, quarter, melted, both certificates | added |
| Spot table: intrinsic value, bubble, implied dollar per coin | **missing** — needs validated gold-content and unit constants |
| Treemap: traded value and daily return per fund | added |
| NAV intraday trend (one fund) | added (`series.nav`, from `hist.gold_fund_nav`) |
| Intraday bubble trend | **missing** (no fund price history) |
| Asset mix: coin / bar / other weights | nexus |
| Asset mix: correlation with coin, adjusted bubble | **missing** — the bubble decomposition was deliberately not ported (Nexus CLAUDE.md invariant 9) |

### Performance report

| Item | Status |
|---|---|
| Strategy monthly returns vs buy-and-hold | **missing** — `hist.account_gold_portfolio` is empty; not market data |

## 4. Units

Sources do not share a unit. Nexus reports each price in its **native unit**
with a `unit` field and never converts silently:

| Source | Unit |
|---|---|
| TSE funds (market_fetcher) | IRR |
| IME certificates | IRR (`GoldBar` is per 100 mg — `ContractSize` 10) |
| estjt, tabdeal, wallex | IRT (toman) |
| estjt ounce | USD |

The site converts toman to rial for display, except the dollar, which stays
in toman as the design shows it.

## 5. Gaps to work on

In priority order — each unblocks visible parts of the site:

1. **Fund price history** (intraday + daily). Unblocks the intraday bubble
   chart, "vs yesterday", and a weekly traded-value baseline. `market_fetcher`
   only keeps the latest snapshot; nothing writes fund prices to Postgres.
2. **Gold funds index.** No source on the server.
3. **Coin intrinsic value / implied dollar.** Needs agreed constants
   (gold content per coin, ounce→gram, which dollar) validated against real
   prices before anything is shown.
4. **Correlation with coin and adjusted bubble.** Depends on (1) and on the
   decomposition that was intentionally left out.
5. **Strategy performance series** for the performance page.
6. **Official market status.** "Market open" is currently inferred from the
   freshness of the latest fund trade.
7. **Fund count wording.** Pages say 30 funds; the data has 31.
