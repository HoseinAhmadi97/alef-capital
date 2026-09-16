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

/* bubble vs coin-weight scatter (product page and market page).
   x = the fund's coin weight this month, y = its bubble now; the dashed
   line is the least-squares fit of the funds shown. */
function goldScatter(g, ids) {
  var box = document.getElementById(ids.g); if (!box) return;
  var pts = g.withBubble.filter(function (f) { return f.weights && f.weights.sekke_weight != null; })
    .map(function (f) { return { s: f.symbol, x: f.weights.sekke_weight, y: f.nominal_bubble * 100 }; });
  if (!pts.length) { box.innerHTML = ''; return; }
  var X0 = ids.x0, X1 = ids.x1, Y0 = ids.y0, H = ids.h;       /* plot geometry of that SVG */
  var M = Math.max(1, Math.ceil(Math.max.apply(null, pts.map(function (p) { return Math.abs(p.y); }))));
  function px(x) { return X0 + x * (X1 - X0); }
  function py(y) { return Y0 - Math.max(-M, Math.min(M, y)) / M * H; }
  var lo = pts.reduce(function (a, p) { return p.y < a.y ? p : a; });
  box.innerHTML = pts.map(function (p) {
    var big = p === lo;
    return '<circle cx="' + px(p.x).toFixed(1) + '" cy="' + py(p.y).toFixed(1) + '" r="' + (big ? 7 : 4) +
      '" fill="' + (big ? '#0891B2' : 'currentColor') + '" opacity="' + (big ? '.95' : '.55') + '">' +
      '<title>' + p.s + ' — ' + gPct(p.y / 100) + '</title></circle>';
  }).join('');
  var n = pts.length, sx = 0, sy = 0, sxx = 0, sxy = 0;
  pts.forEach(function (p) { sx += p.x; sy += p.y; sxx += p.x * p.x; sxy += p.x * p.y; });
  var den = n * sxx - sx * sx, line = document.getElementById(ids.line);
  if (line) {
    if (n > 1 && Math.abs(den) > 1e-9) {
      var b = (n * sxy - sx * sy) / den, a = (sy - b * sx) / n;
      line.setAttribute('x1', px(0)); line.setAttribute('y1', py(a).toFixed(1));
      line.setAttribute('x2', px(1)); line.setAttribute('y2', py(a + b).toFixed(1));
      line.style.display = '';
    } else line.style.display = 'none';
  }
  gText(ids.top, '‎+' + fa(M) + '٪');
  gText(ids.bottom, '‎−' + fa(M) + '٪');
}
