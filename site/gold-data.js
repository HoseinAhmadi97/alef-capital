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
var GOLD = null, GOLD_SUBS = [];

function onGold(fn) {
  GOLD_SUBS.push(fn);
  if (GOLD) goldRun(fn);
}
function goldRun(fn) {
  /* one broken renderer must not take the others down with it */
  try { fn(GOLD); } catch (e) { if (window.console) console.error(e); }
}

(function () {
  var timer = null, last = null;
  function load() {
    if (!window.fetch) return;
    fetch(GOLD_API, { cache: 'no-cache', headers: { Accept: 'application/json' } })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (d) {
        document.documentElement.classList.remove('gold-offline');
        if (d.generated_at === last) return;          /* 304 → same document */
        last = d.generated_at;
        GOLD = goldIndex(d);
        GOLD_SUBS.forEach(goldRun);
      })
      .catch(function (e) {
        document.documentElement.classList.add('gold-offline');
        if (window.console) console.warn('gold data unavailable:', e.message);
      });
  }
  function start() { if (!timer) { load(); timer = setInterval(load, GOLD_POLL_MS); } }
  function stop() { clearInterval(timer); timer = null; }
  document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
  /* a page opened in a background tab still loads once, so it is ready
     when shown; only the polling waits for the tab to be visible */
  if (document.hidden) load(); else start();
})();

/* lookups the pages need, built once per document */
function goldIndex(d) {
  d.m = {};
  d.market.forEach(function (r) { d.m[r.symbol] = r; });
  d.withBubble = d.funds.filter(function (f) { return f.nominal_bubble != null; });
  return d;
}

/* ── formatting — sources report native units; conversion happens only here ── */

/* toman → rial. Gold, coins and certificates are shown in rial. */
function goldRial(r) {
  if (!r || r.price == null) return null;
  return r.unit === 'IRT' ? r.price * 10 : r.price;
}
/* the value a price cell shows: dollar in toman, ounce in USD, the rest in rial */
function goldShown(r) {
  if (!r || r.price == null) return null;
  if (r.symbol === 'dollar' || r.unit === 'USD') return r.price;
  return goldRial(r);
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
function gText(id, text) { var e = document.getElementById(id); if (e) e.textContent = text; return e; }

/* ── pieces several pages share ── */

/* fund count wherever the copy mentions it: <span class="gcount"> */
onGold(function (g) {
  document.querySelectorAll('.gcount').forEach(function (e) { e.textContent = fa(g.summary.fund_count); });
  document.querySelectorAll('.gupdated').forEach(function (e) { e.textContent = gTime(g.generated_at, true); });
  document.querySelectorAll('.gdate').forEach(function (e) { e.textContent = gDate(g.generated_at); });
});

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
  var st = gText('tstate', g.summary.market_open ? 'بازار باز است' : 'بازار بسته است');
  if (st && st.previousElementSibling) st.previousElementSibling.style.background =
    g.summary.market_open ? '' : 'var(--slate-400)';
});

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
