/* ═══════════════ LIVE DATA — the Nexus gold snapshot ═══════════════
   Every gold number on the site comes from ONE document:
   GET __GOLD_API__  (Nexus /v1/gold/snapshot — see docs/gold-data-map.md)

   Load rules, so visitors cost the data layer nothing:
   - one request when the page opens (even in a background tab), then a
     re-poll every __POLL__ s
   - polling stops while the tab is hidden and resumes (with an immediate
     refresh) when it is visible again
   - `cache: 'no-cache'` makes the browser revalidate with the ETag, so an
     unchanged poll is a body-less 304 and nothing re-renders

   A page shows its numbers by registering a renderer:
       onGold(function (g) { ... });
   It runs once as soon as data is available and again on every change.
   Until then — or if the API is unreachable — elements keep their "—".
   ═════════════════════════════════════════════════════════════════════ */
var GOLD_API = '__GOLD_API__', GOLD_POLL_MS = __POLL__ * 1000;
var GOLD_NAV_API = '__GOLD_NAV_API__';
var GOLD = null, GOLD_SUBS = [];

function onGold(fn) {
  GOLD_SUBS.push(fn);
  if (GOLD) goldRun(fn);
}
function goldRun(fn) {
  /* one broken renderer must not take the others down with it */
  try { fn(GOLD); } catch (e) { if (window.console) console.error(e); }
}

/* Poll one Nexus document with the load rules above; `fn` gets it only
   when it changed (a 304 revalidation yields the same generated_at). */
function goldFeed(url, seconds, fn) {
  var timer = null, last = null;
  function load() {
    if (!window.fetch) return;
    fetch(url, { cache: 'no-cache', headers: { Accept: 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        /* the server's clock, so market hours and countdowns don't depend
           on a visitor's clock being right */
        var server = Date.parse(r.headers.get('Date') || '');
        if (!isNaN(server)) GOLD_CLOCK_OFFSET = server - Date.now();
        return r.json();
      })
      .then(function (d) {
        document.documentElement.classList.remove('gold-offline');
        if (d.generated_at === last) return;
        last = d.generated_at;
        try { fn(d); } catch (e) { if (window.console) console.error(e); }
      })
      .catch(function (e) {
        document.documentElement.classList.add('gold-offline');
        if (window.console) console.warn('gold data unavailable (' + url + '):', e.message);
      });
  }
  function start() { if (!timer) { load(); timer = setInterval(load, seconds * 1000); } }
  function stop() { clearInterval(timer); timer = null; }
  document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
  /* a page opened in a background tab still loads once, so it is ready
     when shown; only the polling waits for the tab to be visible */
  if (document.hidden) load(); else start();
}

goldFeed(GOLD_API, GOLD_POLL_MS / 1000, function (d) {
  GOLD = goldIndex(d);
  GOLD_SUBS.forEach(goldRun);
});

/* lookups the pages need, built once per document */
function goldIndex(d) {
  /* farabi is the NAV of record; `nav` carries it. Older Nexus builds only
     had nav_farabi, so fall back to that rather than show nothing. */
  d.funds.forEach(function (f) { if (f.nav == null) f.nav = f.nav_farabi; });
  d.m = {};
  d.market.forEach(function (r) { d.m[r.symbol] = r; });
  d.withBubble = d.funds.filter(function (f) { return f.nominal_bubble != null; });
  return d;
}

/* ── formatting — sources report native units; conversion happens only here ── */

/* Every Iranian price on the site is shown in TOMAN; only the global ounce
   stays in USD. Convert here and nowhere else. */

/* rial → toman */
function gToman(rial) { return rial == null ? null : rial / 10; }
/* a market row's price in toman, whatever unit its source reports */
function goldToman(r) {
  if (!r || r.price == null) return null;
  return r.unit === 'IRR' ? r.price / 10 : r.price;
}
/* the value a price shows: the ounce in USD, everything else in toman */
function goldShown(r) {
  if (!r || r.price == null) return null;
  return r.unit === 'USD' ? r.price : goldToman(r);
}
function gNum(n) { return n == null ? '—' : fa(grp(n)); }
/* a fraction (0.0123) as a signed Persian percentage (‎+۱٫۲۳٪) */
function gPct(f, dec) {
  if (f == null) return '—';
  var v = f * 100, s = Math.abs(v).toFixed(dec == null ? 2 : dec);
  if (+s === 0) return fa(s).replace('.', '٫') + '٪';
  return (v < 0 ? '‎−' : '‎+') + fa(s).replace('.', '٫') + '٪';
}
/* ▲ / ▼ / — with an unsigned percentage, for change cells */
function gArrow(f, dec) {
  if (f == null) return '—';
  var s = Math.abs(f * 100).toFixed(dec == null ? 2 : dec);
  var a = +s === 0 ? '—' : (f > 0 ? '▲' : '▼');
  return a + ' ' + fa(s).replace('.', '٫') + '٪';
}
function gSign(f) { return f == null || Math.abs(f) < 0.00005 ? 0 : (f > 0 ? 1 : -1); }

/* The site's one colour rule for signed numbers — price changes, bubbles,
   anything with a sign: positive is green, negative is red, zero neutral.
   Every page takes its colours from these, so no page can invert it. */
function gColor(f) { var s = gSign(f); return s > 0 ? 'var(--up-text)' : (s < 0 ? 'var(--down)' : ''); }
/* the class for a sign, given a page's class names: gTone(f, 'up', 'down', 'neu') */
function gTone(f, pos, neg, zero) { var s = gSign(f); return s > 0 ? pos : (s < 0 ? neg : (zero || '')); }
function gBarColor(f, strong) {
  var s = gSign(f), a = strong ? '.75' : '.45';
  return s > 0 ? 'rgba(22,163,74,' + a + ')' : (s < 0 ? 'rgba(220,38,38,' + a + ')' : 'rgba(148,163,184,.6)');
}

/* ── sortable tables ──
   Mark sortable headers with data-sort="num" or data-sort="text" and give
   each body cell data-v (the raw value to sort by). gSortable() wires the
   headers once; call gResort() after every re-render so the order a
   visitor picked survives the 20-second refresh. Missing values sort last. */
function gSortable(table) {
  if (!table || table._sort) return;
  table._sort = { col: -1, dir: -1 };
  [].forEach.call(table.tHead.rows[0].cells, function (th, i) {
    if (!th.hasAttribute('data-sort')) return;
    th.tabIndex = 0;
    th.setAttribute('aria-sort', 'none');
    function go() {
      var s = table._sort, text = th.getAttribute('data-sort') === 'text';
      s.dir = s.col === i ? -s.dir : (text ? 1 : -1);   /* numbers start largest first */
      s.col = i;
      gResort(table);
    }
    th.addEventListener('click', go);
    th.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(); }
    });
  });
}
function gResort(table) {
  var s = table && table._sort; if (!s) return;
  var head = table.tHead.rows[0].cells;
  [].forEach.call(head, function (th, i) {
    if (th.hasAttribute('data-sort'))
      th.setAttribute('aria-sort', i === s.col ? (s.dir > 0 ? 'ascending' : 'descending') : 'none');
  });
  if (s.col < 0) return;
  var text = head[s.col].getAttribute('data-sort') === 'text', body = table.tBodies[0];
  var rows = [].slice.call(body.rows);
  rows.sort(function (a, b) {
    var x = a.cells[s.col].getAttribute('data-v'), y = b.cells[s.col].getAttribute('data-v');
    if (text) return s.dir * String(x || '').localeCompare(String(y || ''), 'fa');
    x = x === null || x === '' ? NaN : +x; y = y === null || y === '' ? NaN : +y;
    if (isNaN(x) || isNaN(y)) return isNaN(x) - isNaN(y);
    return s.dir * (x - y);
  });
  rows.forEach(function (r) { body.appendChild(r); });
}
/* a <td> carrying its sort value */
function gTd(html, v, cls) {
  return '<td' + (cls ? ' class="' + cls + '"' : '') + ' data-v="' + (v == null ? '' : v) + '">' + html + '</td>';
}
/* "14:39:21" or an ISO timestamp → ۱۴:۳۹ (Tehran — Nexus already sends +03:30) */
function gTime(t, secs) {
  if (!t) return '—';
  var m = /(\d\d:\d\d)(:\d\d)?/.exec(t.indexOf('T') > 0 ? t.split('T')[1] : t);
  return m ? fa(m[1] + (secs && m[2] ? m[2] : '')) : '—';
}
/* the Jalali date of a timestamp, e.g. ۱۴۰۵/۰۶/۲۵ */
function gDate(iso) {
  try {
    return new Intl.DateTimeFormat('fa-IR-u-ca-persian', {
      timeZone: 'Asia/Tehran', year: 'numeric', month: '2-digit', day: '2-digit'
    }).format(new Date(iso));
  } catch (e) { return '—'; }
}
/* rial → «۷٫۶ همت» (1 همت = هزار میلیارد تومان = 10^13 rial) */
function gHemat(rial) {
  if (rial == null) return '—';
  return fa((rial / 1e13).toFixed(1)).replace('.', '٫') + ' همت';
}
/* rial → «۸۴۰ میلیارد» (toman) */
function gBillion(rial) {
  if (rial == null) return '—';
  return fa(grp(rial / 1e10)) + ' میلیارد';
}
/* A number for a data table:
   - Persian digits with the Persian thousands separator «٬» (U+066C), not ","
   - for values of a million or more, the last three digits are set quieter,
     so the significant part reads first: ۲۳۲٬۸۰۰<quiet>٬۰۰۰</quiet>
   Digits are tabular (theme.css), so right-aligned columns line up by place. */
function gNumT(n) {
  if (n == null || isNaN(n)) return '—';
  var s = fa(grp(Math.abs(n))).replace(/,/g, '٬');
  var sign = n < 0 ? '−' : '';
  if (Math.abs(n) >= 1e6) {
    var i = s.lastIndexOf('٬');
    return sign + '<span class="nh">' + s.slice(0, i) + '</span><span class="nt">' + s.slice(i) + '</span>';
  }
  return sign + s;
}
function gText(id, text) { var e = document.getElementById(id); if (e) e.textContent = text; return e; }

/* ── pieces several pages share ── */

/* fund count wherever the copy mentions it: <span class="gcount"> */
onGold(function (g) {
  document.querySelectorAll('.gcount').forEach(function (e) { e.textContent = fa(g.summary.fund_count); });
  document.querySelectorAll('.gupdated').forEach(function (e) { e.textContent = gTime(g.generated_at, true); });
  document.querySelectorAll('.gdate').forEach(function (e) { e.textContent = gDate(g.generated_at); });
  document.querySelectorAll('.gweekday').forEach(function (e) {
    try {
      e.textContent = new Intl.DateTimeFormat('fa-IR', { timeZone: 'Asia/Tehran', weekday: 'long' })
        .format(new Date(g.generated_at));
    } catch (err) { e.textContent = ''; }
  });
  GOLD_RECEIVED_AT = Date.now();
});

/* a thin bar that fills until the next poll: <span class="gpoll"><i></i></span> */
var GOLD_RECEIVED_AT = null;
setInterval(function () {
  if (GOLD_RECEIVED_AT == null) return;
  var w = Math.min(100, (Date.now() - GOLD_RECEIVED_AT) / GOLD_POLL_MS * 100) + '%';
  document.querySelectorAll('.gpoll i').forEach(function (i) { i.style.width = w; });
}, 500);

/* ticker — built once, then updated in place so the marquee never jumps */
onGold(function (g) {
  var track = document.getElementById('ttrack'); if (!track) return;
  var items = TICK.map(function (t) {
    if (t.k === 'funds') return { n: t.n, p: null, d: g.summary.avg_change_pct };
    var r = g.m[t.k];
    return { n: t.n, p: goldShown(r), d: r ? r.change_pct : null };
  });
  if (track.children.length !== items.length * 2) {
    var h = items.map(tiHTML).join('');
    track.innerHTML = h + h;
  }
  for (var i = 0; i < track.children.length; i++) {
    var t = items[i % items.length], el = track.children[i];
    el.querySelector('.tp').textContent = t.p == null ? '' : gNum(t.p);
    var c = el.querySelector('.tc'), s = gSign(t.d);
    c.className = 'tc ' + (s > 0 ? 'u' : (s < 0 ? 'd' : 'n'));
    c.textContent = gArrow(t.d);
  }
});

/* ── market hours ──
   Schedules come from config.MARKET_HOURS. Tehran is a fixed UTC+3:30
   (no DST since 2022), so local time is computed from UTC plus the
   server-clock offset, not from the visitor's timezone setting.

   Mark an element with data-session="funds" or "physical":
   - a .live badge gets its dot/colour state and a short label
   - #tstate (ticker) and .gsession (long text) get a sentence
   Everything re-renders every second, which is what drives the countdown. */
var MARKET_HOURS = __MARKET_HOURS__, GOLD_CLOCK_OFFSET = 0;

function gMinutes(hhmm) { var p = hhmm.split(':'); return +p[0] * 60 + +p[1]; }
function gClockText(secs) {
  var h = Math.floor(secs / 3600), m = Math.floor(secs % 3600 / 60), s = Math.floor(secs % 60);
  return fa(h + ':' + ('0' + m).slice(-2) + ':' + ('0' + s).slice(-2));
}
/* {state: 'open' | 'soon' | 'closed', secsToOpen} for one schedule, now */
function gSession(key) {
  var cfg = MARKET_HOURS[key];
  var t = new Date(Date.now() + GOLD_CLOCK_OFFSET + 3.5 * 3600e3);
  var secs = t.getUTCHours() * 3600 + t.getUTCMinutes() * 60 + t.getUTCSeconds();
  var open = gMinutes(cfg.open) * 60, close = gMinutes(cfg.close) * 60;
  if (cfg.days.indexOf(t.getUTCDay()) < 0) return { state: 'closed' };
  if (secs >= open && secs < close) return { state: 'open' };
  if (secs < open && open - secs <= (cfg.countdown || 0) * 60) return { state: 'soon', secsToOpen: open - secs };
  return { state: 'closed' };
}

var GOLD_SESSION_TEXT = {
  funds: {
    badge: { open: 'بازار باز', closed: 'بازار بسته' },
    long: { open: 'بازار صندوق‌های طلا باز است', closed: 'بازار صندوق‌های طلا بسته است' },
    soon: function (t) { return t + ' تا بازگشایی'; },
    soonLong: function (t) { return 'بازگشایی بازار صندوق‌های طلا تا ' + t; }
  },
  physical: {
    badge: { open: 'بازار باز', closed: 'بازار بسته' },
    long: { open: 'بازار طلا باز است', closed: 'بازار طلا بسته است' },
    soon: function (t) { return t + ' تا بازگشایی'; },
    soonLong: function (t) { return 'بازگشایی بازار طلا تا ' + t; }
  }
};

function gRenderSessions() {
  document.querySelectorAll('[data-session]').forEach(function (el) {
    var key = el.getAttribute('data-session'), s = gSession(key), T = GOLD_SESSION_TEXT[key];
    var clock = s.state === 'soon' ? gClockText(s.secsToOpen) : '';
    if (el.classList.contains('live')) {
      el.classList.toggle('is-closed', s.state === 'closed');
      el.classList.toggle('is-soon', s.state === 'soon');
      /* under a label that already names the market (dashboard header), say only the state */
      var badge = el.closest('.hstat') ? { open: 'باز است', closed: 'بسته است' } : T.badge;
      var label = s.state === 'soon' ? T.soon(clock) : badge[s.state];
      var span = el.querySelector('span') || el.appendChild(document.createElement('span'));
      if (span.textContent !== label) span.textContent = label;
      return;
    }
    var text = s.state === 'soon' ? T.soonLong(clock) : T.long[s.state];
    if (el.textContent !== text) el.textContent = text;
    if (el.id === 'tstate' && el.previousElementSibling)
      el.previousElementSibling.style.background = s.state === 'open' ? '' : 'var(--slate-400)';
  });
}
gRenderSessions();
setInterval(gRenderSessions, 1000);

/* a schedule as words, from MARKET_HOURS: <em class="gsched" data-sched="funds">
   → «شنبه–چهارشنبه · ۱۲ تا ۱۸» */
(function () {
  var NAMES = ['یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه', 'شنبه'];
  var WEEK = [6, 0, 1, 2, 3, 4, 5];                    /* the Iranian week starts on Saturday */
  function hour(t) { return /:00$/.test(t) ? fa(+t.split(':')[0]) : fa(t); }
  document.querySelectorAll('.gsched').forEach(function (el) {
    var cfg = MARKET_HOURS[el.getAttribute('data-sched')]; if (!cfg) return;
    var days = WEEK.filter(function (d) { return cfg.days.indexOf(d) >= 0; });
    var span = days.length === 7 ? 'همه روزها'
      : NAMES[days[0]] + (days.length > 1 ? '–' + NAMES[days[days.length - 1]] : '');
    el.textContent = span + ' · ' + hour(cfg.open) + ' تا ' + hour(cfg.close);
  });
})();

/* ── bubble vs coin weight (product and market pages) ──
   Drop <div class="bmix" data-bmix></div> anywhere; it renders itself.
   x = the fund's coin weight this month (zoomed to the funds' actual range,
   not 0–100%), y = its bubble now. Circle area = market cap, colour = sign of
   the bubble. The dashed gold line is the least-squares trend: a fund below it
   trades cheaper than funds with a similar coin share — the tooltip says by
   how much. The largest funds and both extremes are labelled. */
function goldBubbleMix(g, box) {
  var pts = g.withBubble.filter(function (f) { return f.weights && f.weights.sekke_weight != null; })
    .map(function (f) { return { f: f, x: f.weights.sekke_weight * 100, y: f.nominal_bubble * 100, cap: f.market_cap || 0 }; });
  if (pts.length < 2) { box.innerHTML = '<div class="bmix-empty">داده کافی نیست</div>'; return; }

  var W = 460, H = 300, L = 46, R = 450, T = 12, B = 266;
  function nice(v, step, up) { return (up ? Math.ceil(v / step) : Math.floor(v / step)) * step; }
  var xs = pts.map(function (p) { return p.x; }), ys = pts.map(function (p) { return p.y; });
  var xStep = Math.max.apply(null, xs) > 25 ? 10 : (Math.max.apply(null, xs) > 10 ? 5 : 2);
  var x0 = 0, x1 = nice(Math.max.apply(null, xs) * 1.08 + 0.5, xStep, true);
  var yLo = Math.min(0, Math.min.apply(null, ys)), yHi = Math.max(0, Math.max.apply(null, ys));
  var ySpan = yHi - yLo || 1, yStep = ySpan > 6 ? 2 : (ySpan > 2.5 ? 1 : 0.5);
  var y0 = nice(yLo - ySpan * 0.08, yStep, false), y1 = nice(yHi + ySpan * 0.08, yStep, true);
  function X(v) { return L + (v - x0) / (x1 - x0) * (R - L); }
  function Y(v) { return T + (y1 - v) / (y1 - y0) * (B - T); }
  var maxCap = Math.max.apply(null, pts.map(function (p) { return p.cap; })) || 1;
  function rad(p) { return 4 + 9.5 * Math.sqrt(p.cap / maxCap); }

  /* least-squares trend */
  var n = pts.length, sx = 0, sy = 0, sxx = 0, sxy = 0;
  pts.forEach(function (p) { sx += p.x; sy += p.y; sxx += p.x * p.x; sxy += p.x * p.y; });
  var den = n * sxx - sx * sx, b = Math.abs(den) > 1e-9 ? (n * sxy - sx * sy) / den : 0, a = (sy - b * sx) / n;
  pts.forEach(function (p) { p.res = p.y - (a + b * p.x); });

  function pc(v, d) { return fa(v.toFixed(d == null ? 0 : d)).replace('.', '٫') + '٪'; }
  var o = [];
  /* zones: premium above NAV (green wash), discount below (red wash) */
  var zy = Math.max(T, Math.min(B, Y(0)));
  o.push('<defs>' +
    '<linearGradient id="bmUp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="bm-s u0"/><stop offset="1" class="bm-s u1"/></linearGradient>' +
    '<linearGradient id="bmDn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="bm-s d0"/><stop offset="1" class="bm-s d1"/></linearGradient>' +
    '<radialGradient id="bmGp" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#4ADE80"/><stop offset="1" stop-color="#15803D"/></radialGradient>' +
    '<radialGradient id="bmGn" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#F87171"/><stop offset="1" stop-color="#B91C1C"/></radialGradient>' +
    '<radialGradient id="bmGm" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#FCD34D"/><stop offset="1" stop-color="#CA8A04"/></radialGradient>' +
    '<filter id="bmSh" x="-50%" y="-50%" width="200%" height="200%"><feDropShadow dx="0" dy="1.5" stdDeviation="1.8" flood-color="#0F172A" flood-opacity=".22"/></filter>' +
    '<clipPath id="bmCu"><rect x="' + L + '" y="' + T + '" width="' + (R - L) + '" height="' + (zy - T) + '"/></clipPath>' +
    '<clipPath id="bmCd"><rect x="' + L + '" y="' + zy + '" width="' + (R - L) + '" height="' + (B - zy) + '"/></clipPath>' +
    '<clipPath id="bmClip"><rect x="' + L + '" y="' + T + '" width="' + (R - L) + '" height="' + (B - T) + '" rx="12"/></clipPath></defs>');
  o.push('<g clip-path="url(#bmClip)"><rect x="' + L + '" y="' + T + '" width="' + (R - L) + '" height="' + (B - T) + '" class="bm-bg"/>' +
    '<rect x="' + L + '" y="' + T + '" width="' + (R - L) + '" height="' + (zy - T) + '" fill="url(#bmUp)"/>' +
    '<rect x="' + L + '" y="' + zy + '" width="' + (R - L) + '" height="' + (B - zy) + '" fill="url(#bmDn)"/></g>');
  if (zy - T > 22) o.push('<text class="bm-zone up" direction="rtl" unicode-bidi="embed" x="' + (R - 10) + '" y="' + (T + 18) + '" text-anchor="start">بالای NAV · گران</text>');
  if (B - zy > 22) o.push('<text class="bm-zone dn" direction="rtl" unicode-bidi="embed" x="' + (R - 10) + '" y="' + (B - 10) + '" text-anchor="start">زیر NAV · ارزان</text>');
  for (var gx = x0; gx <= x1 + 1e-9; gx += xStep) {
    o.push('<line class="bm-grid" x1="' + X(gx) + '" x2="' + X(gx) + '" y1="' + T + '" y2="' + B + '"/>');
    o.push('<text class="bm-tick" x="' + X(gx) + '" y="' + (B + 20) + '" text-anchor="middle">' + pc(gx) + '</text>');
  }
  for (var gy = y0; gy <= y1 + 1e-9; gy += yStep) {
    var zero = Math.abs(gy) < 1e-9;
    o.push('<line class="' + (zero ? 'bm-zero' : 'bm-grid') + '" x1="' + L + '" x2="' + R + '" y1="' + Y(gy) + '" y2="' + Y(gy) + '"/>');
    o.push('<text class="bm-tick' + (zero ? ' z' : '') + '" x="' + (L - 8) + '" y="' + (Y(gy) + 4) + '" text-anchor="end">' +
      (zero ? 'NAV' : (gy > 0 ? '+' : '−') + pc(Math.abs(gy), yStep < 1 ? 1 : 0)) + '</text>');
  }
  /* trend line, clipped to the plot */
  var tx0 = x0, tx1 = x1;
  var sd = Math.sqrt(pts.reduce(function (m, p) { return m + p.res * p.res; }, 0) / n);
  var bandD = 'M' + X(tx0) + ' ' + Y(a + b * tx0 + sd) + ' L' + X(tx1) + ' ' + Y(a + b * tx1 + sd) +
    ' L' + X(tx1) + ' ' + Y(a + b * tx1 - sd) + ' L' + X(tx0) + ' ' + Y(a + b * tx0 - sd) + ' Z';
  o.push('<path class="bm-band up" clip-path="url(#bmCu)" d="' + bandD + '"/>');
  o.push('<path class="bm-band dn" clip-path="url(#bmCd)" d="' + bandD + '"/>');
  o.push('<line class="bm-trend" x1="' + X(tx0) + '" y1="' + Math.max(T, Math.min(B, Y(a + b * tx0))) + '" x2="' + X(tx1) + '" y2="' + Math.max(T, Math.min(B, Y(a + b * tx1))) + '"/>');
  o.push('<text class="bm-trend-l" x="' + (R - 6) + '" y="' + (Math.max(T + 12, Math.min(B - 6, Y(a + b * tx1) - 8))) + '" text-anchor="end">روند</text>');

  /* biggest circles first, so small funds stay clickable on top */
  pts.slice().sort(function (p, q) { return q.cap - p.cap; }).forEach(function (p) {
    var tone = Math.abs(p.res) <= sd ? 'mid' : (gSign(p.f.nominal_bubble) > 0 ? 'pos' : (gSign(p.f.nominal_bubble) < 0 ? 'neg' : 'zero'));
    o.push('<circle class="bm-pt ' + tone + '" filter="url(#bmSh)" data-isin="' + p.f.isin + '" cx="' + X(p.x).toFixed(1) + '" cy="' + Y(p.y).toFixed(1) + '" r="' + rad(p).toFixed(1) + '"/>');
  });
  /* label the five largest funds and the two extremes */
  var label = {};
  pts.slice().sort(function (p, q) { return q.cap - p.cap; }).slice(0, 5).forEach(function (p) { label[p.f.isin] = p; });
  var lo = pts.reduce(function (m, p) { return p.y < m.y ? p : m; }), hi = pts.reduce(function (m, p) { return p.y > m.y ? p : m; });
  label[lo.f.isin] = lo; label[hi.f.isin] = hi;
  Object.keys(label).forEach(function (k) {
    var p = label[k], r = rad(p), right = X(p.x) + r + 60 < R;
    o.push('<text class="bm-label" x="' + (X(p.x) + (right ? r + 5 : -r - 5)) + '" y="' + (Y(p.y) + 4.5) + '" text-anchor="' + (right ? 'start' : 'end') + '">' + p.f.symbol + '</text>');
  });

  box.innerHTML =
    '<svg viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="حباب هر صندوق در برابر سهم سکه در ترکیب دارایی">' + o.join('') + '</svg>' +
    '<div class="bm-axis-x">سهم گواهی سکه در دارایی صندوق</div>' +
    '<div class="bm-legend"><span><i class="lg-pos"></i>حباب مثبت</span><span><i class="lg-neg"></i>حباب منفی</span>' +
    '<span><i class="lg-size"></i>اندازه: ارزش بازار</span><span><i class="lg-mid"></i>هم‌تراز با روند</span><span><i class="lg-trend"></i>روند و محدوده معمول</span></div>' +
    '<div class="btip bm-tip" hidden></div>';

  var svg = box.querySelector('svg'), tip = box.querySelector('.bm-tip');
  var byIsin = {}; pts.forEach(function (p) { byIsin[p.f.isin] = p; });
  function show(ev) {
    var c = ev.target.closest && ev.target.closest('.bm-pt');
    if (!c) { tip.hidden = true; return; }
    var p = byIsin[c.getAttribute('data-isin')], r = svg.getBoundingClientRect();
    var verdict = Math.abs(p.res) < 0.05 ? 'هم‌تراز با روند'
      : (p.res < 0 ? pc(Math.abs(p.res), 2) + ' ارزنده‌تر از روند' : pc(p.res, 2) + ' گران‌تر از روند');
    tip.innerHTML = '<b>' + p.f.symbol + '</b> · حباب <b style="color:' + (gColor(p.f.nominal_bubble) || 'inherit') + '">' + gPct(p.f.nominal_bubble) + '</b>' +
      '<br>سهم سکه ' + pc(p.x, 1) + ' · ' + verdict;
    tip.style.left = (Number(c.getAttribute('cx')) / W * r.width) + 'px';
    tip.style.top = (Number(c.getAttribute('cy')) / H * r.height - rad(p) * r.height / H) + 'px';
    tip.hidden = false;
  }
  svg.addEventListener('mousemove', show);
  svg.addEventListener('click', show);
  svg.addEventListener('mouseleave', function () { tip.hidden = true; });
}
onGold(function (g) {
  document.querySelectorAll('[data-bmix]').forEach(function (box) { goldBubbleMix(g, box); });
});

/* ── bubble spectrum (home and product pages) — every fund as a dot on one axis ──
   x = bubble (price vs farabi NAV), stacked beeswarm-style so funds with
   nearly the same bubble sit above/below each other instead of on top.
   The track shades red → green; the dashed tick is NAV (0%), the gold
   marker the average. Colours follow the site rule: negative red, positive green. */
(function(){
  var svg=document.getElementById('bSpec'); if(!svg) return;
  var X0=8, X1=292, MID=46, R=4.6, GAP=10.4;
  var tip=document.getElementById('bTip'), box=svg.parentNode;
  onGold(function(g){
    var fs=g.withBubble.slice().sort(function(a,b){return a.nominal_bubble-b.nominal_bubble});
    if(!fs.length) return;
    var vals=fs.map(function(f){return f.nominal_bubble*100});
    /* a symmetric-enough domain that always includes 0 and has 10% headroom */
    var lo=Math.min(0,vals[0]), hi=Math.max(0,vals[vals.length-1]), pad=Math.max(0.15,(hi-lo)*0.1);
    lo-=pad; hi+=pad;
    function X(v){return X0+(v-lo)/(hi-lo)*(X1-X0)}

    /* beeswarm: place each dot on the lowest free lane (0, +1, −1, +2, …) */
    var lanes=[], placed=fs.map(function(f,i){
      var x=X(vals[i]), lane=0;
      for(var k=0;k<12;k++){
        var l=k===0?0:(k%2?(k+1)/2:-k/2);
        if(!(lanes[l]||[]).some(function(px){return Math.abs(px-x)<R*2+0.6})){lane=l;break}
      }
      (lanes[lane]=lanes[lane]||[]).push(x);
      return {f:f,x:x,lane:lane,v:vals[i]};
    });
    /* keep the swarm inside the card: squeeze lanes if a cluster runs deep */
    var deepest=Math.max.apply(null,placed.map(function(p){return Math.abs(p.lane)}));
    var gap=deepest>3?GAP*3/deepest:GAP;
    placed.forEach(function(p){p.y=MID+p.lane*gap});

    document.getElementById('bDots').innerHTML=placed.map(function(p,i){
      return '<circle data-i="'+i+'" cx="'+p.x.toFixed(1)+'" cy="'+p.y.toFixed(1)+'" r="'+R+'" fill="'+
        gBarColor(p.f.nominal_bubble,true).replace('.75','.9')+'" stroke="var(--surface)" stroke-width="1.2"/>'}).join('');

    var zx=X(0).toFixed(1);
    document.getElementById('bZero').innerHTML=
      '<line x1="'+zx+'" x2="'+zx+'" y1="8" y2="84" stroke="var(--slate-400)" stroke-dasharray="2 3"/>';
    var s=g.summary, ax=X(s.avg_bubble*100).toFixed(1);
    document.getElementById('bAvgMark').innerHTML=
      '<path d="M'+ax+' 91 l-5 -7 h10 z" fill="var(--gold-600)"/>';
    document.getElementById('bAxis').innerHTML=
      '<text x="'+X0+'" y="8">'+gPct(lo/100,1)+'</text>'+
      '<text x="'+zx+'" y="8" text-anchor="middle" font-weight="700">NAV</text>'+
      '<text x="'+X1+'" y="8" text-anchor="end">'+gPct(hi/100,1)+'</text>';

    var below=fs.filter(function(f){return f.nominal_bubble<0}).length, above=fs.length-below;
    gText('bBelow',fa(below)); gText('bAbove',fa(above));
    document.getElementById('bBelowBar').style.width=(below/fs.length*100)+'%';
    document.getElementById('bAboveBar').style.width=(above/fs.length*100)+'%';

    svg._placed=placed;
  });

  /* hover / tap a dot to name it */
  function show(ev){
    var c=ev.target.closest&&ev.target.closest('circle[data-i]');
    if(!c||!svg._placed){tip.hidden=true; return}
    var p=svg._placed[+c.getAttribute('data-i')], r=svg.getBoundingClientRect();
    tip.innerHTML='صندوق '+p.f.symbol+' <b style="color:'+gColor(p.f.nominal_bubble)+'">'+gPct(p.f.nominal_bubble)+'</b>';
    tip.style.left=(p.x/300*r.width)+'px'; tip.style.top=(p.y/92*r.height)+'px';
    tip.hidden=false;
  }
  svg.addEventListener('mousemove',show);
  svg.addEventListener('click',show);
  svg.addEventListener('mouseleave',function(){tip.hidden=true});
})();

