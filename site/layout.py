# -*- coding: utf-8 -*-
"""
Shared shell for every page: <head>, top bar, price ticker, footer, mobile bottom bar.

No text or link is hard-coded here — it all comes from config.py.
To change the menu structure, edit config.NAV, not this file.
"""
import io, os, config as C

HERE = os.path.dirname(os.path.abspath(__file__))
THEME = io.open(os.path.join(HERE, "theme.css"), encoding="utf-8").read()

FONT_GOOGLE = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">"""

FONT_LOCAL = """<style>
@font-face{font-family:Vazirmatn;src:url(assets/fonts/Vazirmatn-Regular.woff2)format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:Vazirmatn;src:url(assets/fonts/Vazirmatn-Medium.woff2)format('woff2');font-weight:500;font-display:swap}
@font-face{font-family:Vazirmatn;src:url(assets/fonts/Vazirmatn-SemiBold.woff2)format('woff2');font-weight:600;font-display:swap}
@font-face{font-family:Vazirmatn;src:url(assets/fonts/Vazirmatn-Bold.woff2)format('woff2');font-weight:700;font-display:swap}
@font-face{font-family:Vazirmatn;src:url(assets/fonts/Vazirmatn-ExtraBold.woff2)format('woff2');font-weight:800;font-display:swap}
@font-face{font-family:Vazirmatn;src:url(assets/fonts/Vazirmatn-Black.woff2)format('woff2');font-weight:900;font-display:swap}
</style>"""

LOGO = ('<svg width="{s}" height="{s}" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#C9861A"/>'
        '{ring}<path d="M32 16v32" stroke="#FFFAF0" stroke-width="7.6" stroke-linecap="round"/></svg>')
RING = '<circle cx="32" cy="32" r="30" fill="none" stroke="#F0B429" stroke-width="2"/>'

# A lighter reading of the same mark — the alef inside an open ring instead of
# a filled disc — for places that sit next to text and must not shout.
# It takes its colour from the CSS `color` of its container, so one shape
# serves both products.
MARK = ('<svg viewBox="0 0 64 64" width="{s}" height="{s}" aria-hidden="true" focusable="false">'
        '<circle cx="32" cy="32" r="26" fill="none" stroke="currentColor" stroke-width="2.6" opacity=".38"/>'
        '<path d="M32 20v24" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>'
        '</svg>')


def _u(key):
    """page key → output file name"""
    return C.PAGES[key]


def _gold(active_group, gid):
    return ' style="color:var(--gold-700)"' if active_group == gid else ''


# ───────────────────────────── NAV ─────────────────────────────
def nav(active=""):
    grp = C.NAV_ACTIVE_GROUP.get(active, "")
    items = []
    for entry in C.NAV:
        kind = entry[0]

        if kind == "link":
            _, label, key = entry
            on = ' style="color:var(--gold-700);font-weight:700"' if active == key else ''
            items.append(f'    <li><a href="{_u(key)}"{on}>{label}</a></li>')

        elif kind == "mega":
            _, label, mid, cols, promo = entry
            colhtml = []
            for title, links in cols:
                rows = []
                for tone, icon, name, desc, key, hint in links:
                    h = f'<i>{hint}</i>' if hint else ''
                    rows.append(
                        f'            <a class="mm-i" role="menuitem" href="{_u(key)}">\n'
                        f'              <span class="mm-ic {tone}">{icon}</span>\n'
                        f'              <span><b>{name}</b><em>{desc}</em>{h}</span>\n'
                        f'            </a>')
                colhtml.append('          <div class="mm-col">\n'
                               f'            <div class="mm-h">{title}</div>\n'
                               + "\n".join(rows) + '\n          </div>')
            pt, ps, pa, pk = promo
            colhtml.append('          <div class="mm-promo">\n'
                           f'            <b>{pt}</b>\n            <span>{ps}</span>\n'
                           f'            <a href="{_u(pk)}">{pa}</a>\n          </div>')
            items.append(
                f'    <li class="has-menu" id="{mid}">\n'
                f'      <button class="navbtn" aria-expanded="false" aria-controls="mm-{mid}"{_gold(grp,mid)}>{label} <span class="cv">▾</span></button>\n'
                f'      <div class="mm" id="mm-{mid}" role="menu">\n        <div class="mm-in">\n'
                + "\n".join(colhtml) + '\n        </div>\n      </div>\n    </li>')

        elif kind == "mini":
            _, label, mid, links = entry
            rows = []
            for icon, name, key in links:
                if icon == "--":
                    rows.append('        <div class="sep"></div>')
                else:
                    rows.append(f'        <a role="menuitem" href="{_u(key)}"><span>{icon}</span>{name}</a>')
            items.append(
                f'    <li class="has-menu" id="{mid}">\n'
                f'      <button class="navbtn" aria-expanded="false" aria-controls="mm-{mid}"{_gold(grp,mid)}>{label} <span class="cv">▾</span></button>\n'
                f'      <div class="mini" id="mm-{mid}" role="menu">\n'
                + "\n".join(rows) + '\n      </div>\n    </li>')

    cta = ('    <button class="tglt" id="tglt" type="button" aria-pressed="false"'
           ' aria-label="تغییر تم روشن و تیره" title="تم روشن / تیره">'
           '<span class="ic sun">☀</span><span class="ic moon">☾</span></button>\n'
           + "\n".join(f'    <a class="{cls}" href="{_u(key)}{anch}">{label}</a>'
                       for label, key, cls, anch in C.NAV_CTA))

    return f"""<div class="topbar">
<header>
<div class="wrap nav">
  <a class="logo" href="{_u('home')}">
    {LOGO.format(s=32, ring=RING)}
    {C.BRAND['name']}
  </a>
  <ul>
{chr(10).join(items)}
  </ul>
  <div class="nav-cta">
{cta}
  </div>
</div>
</header>

<div class="ticker">
  <div class="tstate"><span class="dot"></span>بازار باز است</div>
  <div class="ttrack" id="ttrack"></div>
</div>
</div>"""


# ──────────────────────────── FOOTER ───────────────────────────
def footer():
    cols = []
    for title, links in C.FOOTER:
        li = "\n".join(f'    <li><a href="{_u(k)}">{n}</a></li>' for n, k in links)
        cols.append(f'  <div><h4>{title}</h4><ul>\n{li}\n  </ul></div>')
    bnav = "\n".join(f'  <a href="{_u(k)}"><i>{i}</i>{n}</a>' for i, n, k in C.BOTTOM_NAV)
    return f"""<footer>
<div class="wrap fgrid">
  <div>
    <div class="logo" style="color:#fff;margin-bottom:12px">
      {LOGO.format(s=30, ring='')}
      {C.BRAND['name']}
    </div>
    <p style="margin:0;max-width:280px">{C.BRAND['tagline']}</p>
  </div>
{chr(10).join(cols)}
</div>
<div class="wrap risk">
  {C.RISK_SHORT}
  <div style="margin-top:10px">© {C.BRAND['year']} {C.BRAND['name']} — همه حقوق محفوظ است.</div>
</div>
</footer>

<nav class="bnav"><div>
{bnav}
</div></nav>"""


# ─────────────────────── JS shared by every page ───────────────
def _ticker_rows():
    return ",\n ".join("{n:'%s',p:%d,d:%s}" % (n, p, d) for n, p, d in C.TICKER)


COMMON_JS = lambda: """
/* ═══════════════ LIVE DATA LAYER ═══════════════
   TODO(wire-up): point the values below at the market API.
   The expected output shape is exactly what you see here.
   ═══════════════════════════════════════════════ */
var FA='۰۱۲۳۴۵۶۷۸۹';
function fa(x){return String(x).replace(/\\d/g,function(d){return FA[+d]})}
function grp(n){return String(Math.round(n)).replace(/\\B(?=(\\d{3})+(?!\\d))/g,',')}
var TICK=[
 """ + _ticker_rows() + """];
function tiHTML(t){var c=t.d>0?'u':(t.d<0?'d':'n'),a=t.d>0?'▲':(t.d<0?'▼':'—');
 return '<div class="ti"><span class="tn">'+t.n+'</span><span class="tp">'+fa(grp(t.p))+
 '</span><span class="tc '+c+'">'+a+' '+fa(Math.abs(t.d).toFixed(2)).replace('.','٫')+'٪</span></div>'}
(function(){var e=document.getElementById('ttrack');if(e){var h=TICK.map(tiHTML).join('');e.innerHTML=h+h}})();

/* Publish the real height of the sticky top bar, so anything that sticks
   below it (the in-page sub-nav) lines up instead of guessing a pixel
   value that goes stale the moment a menu label or the font changes. */
(function(){
  var t=document.querySelector('.topbar'); if(!t) return;
  function set(){document.documentElement.style.setProperty(
    '--topbar-h', Math.round(t.getBoundingClientRect().height)+'px')}
  set();
  addEventListener('resize',set,{passive:true});
  addEventListener('load',set);
  /* the web font changes the bar's height when it lands, so re-measure then */
  if(document.fonts&&document.fonts.ready) document.fonts.ready.then(set).catch(function(){});
  if(window.ResizeObserver) new ResizeObserver(set).observe(t);
})();

/* light / dark theme — the stored choice wins, otherwise the OS preference.
   The <script> in <head> has already applied it before first paint; this
   only wires the button. */
(function(){
  var b=document.getElementById('tglt'); if(!b) return;
  function sync(){var d=document.documentElement.getAttribute('data-theme')==='dark';
    b.setAttribute('aria-pressed',d?'true':'false')}
  sync();
  b.addEventListener('click',function(){
    var d=document.documentElement.getAttribute('data-theme')!=='dark';
    document.documentElement.setAttribute('data-theme',d?'dark':'light');
    try{localStorage.setItem('alef-theme',d?'dark':'light')}catch(e){}
    sync();
  });
})();

/* top-bar menus — one implementation for all of them (.has-menu) */
(function(){
  document.querySelectorAll('.has-menu').forEach(function(li){
    var btn=li.querySelector('.navbtn'), t;
    if(!btn) return;
    function set(v){
      if(v) document.querySelectorAll('.has-menu.open').forEach(function(o){
        if(o!==li){o.classList.remove('open');o.querySelector('.navbtn').setAttribute('aria-expanded','false')}});
      li.classList.toggle('open',v); btn.setAttribute('aria-expanded',v?'true':'false');
    }
    btn.addEventListener('click',function(e){e.stopPropagation();set(!li.classList.contains('open'))});
    if(window.matchMedia('(hover:hover)').matches){
      li.addEventListener('mouseenter',function(){clearTimeout(t);set(true)});
      li.addEventListener('mouseleave',function(){t=setTimeout(function(){set(false)},180)});
    }
    document.addEventListener('click',function(e){if(!li.contains(e.target))set(false)});
    document.addEventListener('keydown',function(e){
      if(e.key==='Escape'&&li.classList.contains('open')){set(false);btn.focus()}});
  });
})();
"""


# ──────────────────────────── PAGE ─────────────────────────────
def page(title, description, active, body, js=""):
    font = FONT_LOCAL if C.SELF_HOSTED_FONT else FONT_GOOGLE
    return f"""<!DOCTYPE html>
<html dir="rtl" lang="fa">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fa_IR">
<meta name="color-scheme" content="light dark">
<script>
/* Applied before the first paint, so a dark-theme visitor never sees a
   white flash. Wrapped in try/catch: localStorage throws in a private
   window and in some embedded views, and a theme is not worth a broken page. */
(function(){{var t;try{{t=localStorage.getItem('alef-theme')}}catch(e){{}}
if(!t)t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
document.documentElement.setAttribute('data-theme',t)}})();
</script>
{font}
<style>
{THEME}
</style>
</head>
<body>
{nav(active)}
{body}
{footer()}
<script>
{COMMON_JS()}
{js}
</script>
</body>
</html>
"""
