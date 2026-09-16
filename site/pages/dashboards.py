# -*- coding: utf-8 -*-
"""Guest dashboards — gold arbitrage and covered call.

Whether the computed columns are open or behind sign-up is decided by
config.PAYWALL; see site/paywall.py for the markers.
"""
import paywall

SIGNUP = """
  <div class="signup">
    <div>
      <h2>{h}</h2>
      <p>{p}</p>
      <ul><li>ثبت‌نام با شماره موبایل</li><li>بدون کارت بانکی</li><li>۷ روز دسترسی کامل</li></ul>
    </div>
    <div class="acts">
      <a class="btn btn-p" href="pricing.html">ثبت‌نام رایگان</a>
      <a class="btn btn-s" href="pricing.html" style="color:#DBE6FE;border-color:#334155">مشاهده پلن‌ها</a>
    </div>
  </div>
"""

# ═══════════════════════════ GOLD DASHBOARD ═══════════════════════════
GOLD = """
<div class="apphead">
<div class="wrap">
  <div class="ah-title">
    <span class="guest">نسخه مهمان</span>
    <h1>داشبورد آربیتراژ صندوق طلا</h1>
  </div>
  <!-- market state, with the time of the last data update under it -->
  <div class="ah-rail">
    <div class="hstat">
      <span class="live" data-session="funds"><i></i><span>—</span></span>
      <em>به‌روزرسانی <span class="num gupdated">—</span></em>
    </div>
  </div>
  <div class="ah-cta">
    <a class="btn btn-s" href="product-gold.html" style="padding:11px 20px;font-size:14px">معرفی محصول</a>
  </div>
</div>
</div>

<div class="subnav">
<div class="wrap">
  <a class="on" href="#overview">بازار امروز</a>
  <a href="#funds">صندوق‌های طلا</a>
  <a href="#spot">طلا و سکه</a>
  <a href="#nav">روند NAV</a>
  <a href="#mix">ترکیب دارایی</a>
  <a href="#tools">ابزارها</a>
</div>
</div>

<!-- OVERVIEW — today's market: compact number tiles, the market map beside them -->
<section class="dsec" id="overview">
<div class="wrap">
  <div class="sh"><div><h2>بازار امروز</h2></div>
    <div style="font-size:12px;color:var(--slate-500);display:flex;align-items:center;gap:7px">
      <span>بازدهی −</span>
      <i style="width:16px;height:12px;background:#B91C1C;border-radius:2px;display:inline-block"></i>
      <i style="width:16px;height:12px;background:#EF4444;border-radius:2px;display:inline-block"></i>
      <i style="width:16px;height:12px;background:#94A3B8;border-radius:2px;display:inline-block"></i>
      <i style="width:16px;height:12px;background:#4ADE80;border-radius:2px;display:inline-block"></i>
      <i style="width:16px;height:12px;background:#15803D;border-radius:2px;display:inline-block"></i>
      <span>+</span>
    </div>
  </div>
  <div class="ovgrid">
    <div class="mtiles" id="gTiles">
      <!-- free market first -->
      <div class="mtile" data-sym="geram18"><small>طلای ۱۸ عیار (تومان)</small><b class="num">—</b><div class="sub">—</div></div>
      <div class="mtile" data-sym="dollar"><small>دلار (تومان)</small><b class="num">—</b><div class="sub">—</div></div>
      <div class="mtile" data-sym="ons"><small>انس جهانی (دلار)</small><b class="num">—</b><div class="sub">—</div></div>
      <div class="mtile" data-sym="funds"><small>میانگین تغییر صندوق‌ها</small><b class="num">—</b><div class="sub">—</div></div>
      <!-- then the gold funds -->
      <div class="mtile hl"><small>میانگین حباب</small><b class="num" id="gAvg">—</b><div class="sub"><span class="gcount">—</span> صندوق</div></div>
      <div class="mtile"><small>ارزش معاملات</small><b class="num" id="gVal">—</b><div class="sub">مجموع امروز</div></div>
      <div class="mtile"><small>پرحباب‌ترین</small><b class="num" id="gMax">—</b><div class="sub" id="gMaxN">—</div></div>
      <div class="mtile"><small>کم‌حباب‌ترین</small><b class="num" id="gMin">—</b><div class="sub" id="gMinN">—</div></div>
    </div>
    <div class="ovmap">
      <div class="tmap" id="tmap"></div>
      <p class="ovcap">اندازه هر بلوک: ارزش معاملات امروز · رنگ: بازدهی روزانه</p>
    </div>
  </div>
</div>
</section>

<!-- FUNDS TABLE -->
<section class="dsec" id="funds">
<div class="wrap">
  <div class="sh">
    <div><h2>صندوق‌های طلای بورس</h2><p>ارزش ذاتی، حباب و دلار محاسباتی هر صندوق — لحظه‌ای و بدون ثبت‌نام</p></div>
@@IFLOCK@@    <a class="lockcell" href="pricing.html" style="font-size:12.5px;padding:7px 14px">🔒 باز کردن همه ستون‌ها</a>@@END@@
  </div>
  <div class="dwrap"><div class="tscroll twin">
    <table class="dt" id="gTable">
      <thead><tr><th data-sort="text">نماد</th>
        <th data-sort="num">آخرین قیمت<small>تومان</small></th>
        <th data-sort="num">تغییر<small>درصد</small></th>
        <th data-sort="num">تغییر<small>تومان</small></th>
        <th data-sort="num" class="gs">NAV<small>تومان</small></th>
        <th data-sort="num">حباب<small>نسبت به NAV</small></th>
        <th data-sort="num">حباب ذاتی<small>ترکیب دارایی</small></th>
        <th data-sort="num">دلار محاسباتی<small>تومان</small></th>
        <th data-sort="num" class="gs">ارزش معاملات<small>میلیارد تومان</small></th>
        <th data-sort="text">زمان<small>آخرین معامله</small></th></tr></thead>
      <tbody id="gBody"></tbody>
    </table>
  </div></div>
  <p style="font-size:12px;color:var(--slate-400);margin-top:10px"><span class="gcount">—</span> صندوق · برای مرتب‌سازی روی عنوان هر ستون بزنید · همه قیمت‌ها به تومان · حباب ذاتی = وزن سکه × حباب گواهی سکه + وزن شمش × حباب گواهی شمش · دلار محاسباتی = دلار × (۱ + حباب ذاتی)</p>
</div>
</section>

<!-- SPOT -->
<section class="dsec" id="spot">
<div class="wrap">
  <div class="sh"><div><h2>طلا و سکه — بازار نقدی</h2><p>مبنای محاسبه ارزش ذاتی گواهی‌های سپرده</p></div></div>
  <div class="dwrap"><div class="tscroll">
    <table class="dt" id="sTable">
      <thead><tr><th data-sort="text">عنوان</th>
        <th data-sort="num">آخرین قیمت<small>تومان</small></th>
        <th data-sort="num">تغییر<small>درصد</small></th>
        <th data-sort="num">تغییر<small>تومان</small></th>
        <th data-sort="num" class="gs">ارزش ذاتی<small>تومان</small></th><th data-sort="num">حباب ذاتی</th><th data-sort="num">دلار محاسباتی<small>تومان</small></th></tr></thead>
      <tbody id="sBody"></tbody>
    </table>
  </div></div>
  <p style="font-size:12px;color:var(--slate-400);margin-top:10px">ارزش ذاتی از انس جهانی و دلار محاسبه می‌شود · بهار آزادی، نیم و ربع سکه بر پایه سکه امامی</p>
</div>
</section>

<!-- NAV TREND — every fund's line, one highlighted, a ranked list to pick from -->
<section class="dsec" id="nav">
<div class="wrap">
  <div class="sh"><div><h2>روند ارزش خالص دارایی (NAV)</h2><p>تغییر NAV همه صندوق‌ها نسبت به آخرین NAV روز قبل · روی نمودار یا فهرست، صندوق را انتخاب کنید</p></div>
    <div class="navlegend">
      <span><i class="lg-sel"></i>صندوق انتخابی</span>
      <span><i class="lg-med"></i>میانه صندوق‌ها</span>
      <span><i class="lg-oth"></i>سایر صندوق‌ها</span>
      <span id="navDay">—</span>
    </div>
  </div>
  <div class="navgrid">
    <div class="card navchart">
      <div class="navhead">
        <div class="navwho">
          <small>صندوق انتخابی</small>
          <div><b id="navSel">—</b><span id="navSelV" class="navchip">—</span></div>
        </div>
        <div class="navnav">
          <small>آخرین NAV</small>
          <b class="num" id="navSelNav">—</b>
        </div>
      </div>
      <div class="navplot" id="navPlot">
        <svg id="navSvg" viewBox="0 0 640 300" preserveAspectRatio="none" role="img" aria-label="روند درون‌روزی NAV صندوق‌های طلا">
          <defs>
            <linearGradient id="navGrad" x1="0" y1="0" x2="0" y2="1">
              <stop id="navGradTop" offset="0%" stop-color="rgb(22,163,74)" stop-opacity=".26"/>
              <stop id="navGradBot" offset="100%" stop-color="rgb(22,163,74)" stop-opacity="0"/>
            </linearGradient>
          </defs>
          <g id="navGrid"></g>
          <g id="navLines" fill="none" stroke-linejoin="round" stroke-linecap="round"></g>
          <path id="navMed"></path>
          <path id="navArea" fill="url(#navGrad)"></path>
          <path id="navHot" fill="none" stroke-linejoin="round" stroke-linecap="round"></path>
          <line id="navGuide" y1="0" y2="300" style="display:none"></line>
        </svg>
        <div class="navyl" id="navYl"></div>
        <div class="navend" id="navEnd" hidden><i></i><span id="navEndV"></span></div>
        <div class="navdot" id="navDot" hidden></div>
        <div class="navtip" id="navTip" hidden></div>
        <div class="navempty" id="navEmpty">در حال دریافت داده…</div>
      </div>
      <div class="navaxis" id="navAxis"></div>
    </div>
    <div class="card navrank">
      <div class="navrank-h"><span>تغییر نسبت به دیروز</span><em><span class="gcount">—</span> صندوق</em></div>
      <div id="navList" class="navlist" role="listbox" aria-label="انتخاب صندوق"></div>
    </div>
  </div>
</div>
</section>

<!-- ASSET MIX -->
<section class="dsec" id="mix">
<div class="wrap">
  <div class="sh">
    <div><h2>ترکیب دارایی صندوق‌ها</h2><p>سهم سکه، شمش و سایر ابزارها — تعیین‌کننده اینکه حباب هر صندوق چقدر توجیه‌پذیر است</p></div>
    <div class="mixsort" role="group" aria-label="مرتب‌سازی صندوق‌ها">
      <button type="button" data-k="sekke" aria-pressed="true">بیشترین سکه</button>
      <button type="button" data-k="shemsh" aria-pressed="false">بیشترین شمش</button>
      <button type="button" data-k="other" aria-pressed="false">بیشترین نقد و سایر</button>
      <button type="button" data-k="cap" aria-pressed="false">بزرگ‌ترین صندوق</button>
      <button type="button" data-k="bubble" aria-pressed="false">کمترین حباب</button>
    </div>
  </div>
  <div class="mixgrid">
    <div class="card mixsum">
      <div class="lch mixsum-h">
        <span class="lbl" id="mixTitle">ترکیب کل بازار صندوق‌های طلا</span>
        <button type="button" class="mixreset" id="mixReset" hidden>کل بازار ←</button>
      </div>
      <svg viewBox="0 0 120 120" role="img" aria-labelledby="mixDonutT">
        <title id="mixDonutT">سهم سکه، شمش و سایر در کل بازار صندوق‌های طلا، وزنی با ارزش بازار</title>
        <g id="mixDonut" transform="rotate(-90 60 60)"></g>
        <text x="60" y="57" text-anchor="middle" font-size="15" font-weight="800" fill="var(--ink-800)" id="mixDonutV">—</text>
        <text x="60" y="73" text-anchor="middle" font-size="8.5" fill="var(--slate-500)">سهم سکه</text>
      </svg>
      <div class="mixleg" id="mixLegend"></div>
      <p style="font-size:11.5px;color:var(--slate-400);margin:12px 0 0" id="mixNote">میانگین وزنی با ارزش بازار هر صندوق · روی هر صندوق بزنید</p>
    </div>
    <div class="card" style="padding:20px">
      <div class="mbkey">
        <span><i style="background:var(--mix-coin)"></i>گواهی سکه</span>
        <span><i style="background:var(--mix-bar)"></i>گواهی شمش</span>
        <span><i style="background:var(--mix-other)"></i>نقد و سایر</span>
      </div>
      <div class="mixbars" id="mixBars"></div>
    </div>
  </div>
  <p style="font-size:12px;color:var(--slate-400);margin-top:10px">ترکیب دارایی از آخرین گزارش ماهانه هر صندوق · همبستگی با سکه و حباب تعدیل‌شده به‌زودی</p>
</div>
</section>

<!-- TOOLS -->
<section class="dsec" id="tools" style="border-bottom:0">
<div class="wrap">
  <div class="sh"><div><h2>ابزارها</h2><p>محاسبه‌گر و پرتفوی شخصی</p></div></div>
  <div class="lockgrid">
    <div class="lockpanel">
      <div class="ic">🧮</div>
      <h3>محاسبه‌گر ارزش ذاتی و حباب</h3>
      <p>ارزش ذاتی و حباب هر صندوق را بر اساس مقادیر دلخواه خودتان (انس، دلار، وزن سکه) محاسبه کنید و نتیجه را در جدول ببینید.</p>
      <span class="soon">به‌زودی</span>
    </div>
    <div class="lockpanel">
      <div class="ic">📁</div>
      <h3>ساخت سبد دارایی</h3>
      <p>صندوق‌های خودتان را وارد کنید و سود و زیان و ارزش دارایی طلای پرتفوتان را لحظه‌ای ببینید. هشدار عبور حباب از آستانه هم می‌گذارید.</p>
      <span class="soon">به‌زودی</span>
    </div>
  </div>
@@IFLOCK@@""" + SIGNUP.format(h="ارزش ذاتی، حباب و دلار محاسباتی را باز کنید",
                    p="با عضویت رایگان، جدول کامل همه صندوق‌ها به‌صورت لحظه‌ای در اختیارتان است. با پلن طلا، محاسبه‌گر، تاریخچه ۶ ماهه و هشدار هم اضافه می‌شود.") + """@@END@@
</div>
</section>

<div class="riskbar"><div class="wrap">
  اطلاعات ارائه‌شده در این داشبورد صرفاً جنبه تحلیلی و اطلاع‌رسانی دارد و توصیه به خرید یا فروش هیچ اوراق بهاداری محسوب نمی‌شود. مسئولیت تصمیم‌های معاملاتی بر عهده کاربر است.
</div></div>
"""

GOLD_JS = paywall.js_flag() + """
/* every number comes from the gold snapshot (site/gold-data.js).
   Derived columns are computed in one place so a row can never disagree
   with itself: bubble = price/NAV − 1 (from Nexus), implied dollar =
   dollar × price/NAV. */
function cell(v){return PAYWALL?LOCK:v}
function chgCells(f,abs){
  var cls=gTone(f,'up','dn');
  /* the arrow is a small marker in front of the number, not a character in it */
  var pct=gArrow(f).replace(/^(\S+)\s/,'<span class="arr">$1</span>');
  return gTd(pct,f,cls)+gTd(abs==null?'—':gNumT(Math.abs(abs)),abs,cls)}
function bubCell(b){
  if(PAYWALL) return LOCK;
  return '<span class="pill '+gTone(b,'up','dn')+'">'+gPct(b)+'</span>'}
/* "۳,۰۲۴ میلیارد" → the number at full weight, the unit small and grey */
function withUnit(text){return text.replace(/\s(\S+)$/,'<span class="unit">$1</span>')}
gSortable(document.getElementById('gTable'));
gSortable(document.getElementById('sTable'));

/* the header's market status is a data-session element (gold-data.js) */

/* overview tiles */
onGold(function(g){
  document.querySelectorAll('#gTiles [data-sym]').forEach(function(t){
    var k=t.getAttribute('data-sym'), v=t.querySelector('b'), sub=t.querySelector('.sub'), f, when;
    if(k==='funds'){
      f=g.summary.avg_change_pct; v.textContent=gPct(f); when=g.summary.last_trade_time;
    }else{
      var r=g.m[k]; if(!r) return;
      f=r.change_pct; when=r.updated_at;
      v.textContent=r.unit==='USD'?fa(r.price.toLocaleString('en-US',{maximumFractionDigits:2}))
                                  :gNum(goldShown(r));
    }
    if(k==='funds'){
      v.style.color=gColor(f);
      sub.textContent='آخرین معامله · '+gTime(when);
    }else sub.innerHTML='<span class="'+gTone(f,'up','dn')+'">'+gArrow(f)+'</span> · '+gTime(when);
  });
  var s=g.summary, e=gText('gAvg',gPct(s.avg_bubble));
  if(e) e.style.color=gColor(s.avg_bubble);
  if(s.max_bubble){gText('gMax',gPct(s.max_bubble.bubble)).style.color=gColor(s.max_bubble.bubble); gText('gMaxN',s.max_bubble.symbol)}
  if(s.min_bubble){gText('gMin',gPct(s.min_bubble.bubble)).style.color=gColor(s.min_bubble.bubble); gText('gMinN',s.min_bubble.symbol)}
  gText('gVal',gHemat(s.total_value));
});

/* funds table */
onGold(function(g){
  var b=document.getElementById('gBody'); if(!b) return;
  var rows=g.funds.slice().sort(function(x,y){return (y.value||0)-(x.value||0)});
  /* intrinsic bubble and implied dollar are computed in Nexus (gold_intrinsic.py) */
  b.innerHTML=rows.map(function(f){
    return '<tr>'+gTd(f.symbol,f.symbol)+
      gTd(gNumT(gToman(f.last_trade)),f.last_trade,'k')+chgCells(f.change_pct,gToman(f.change))+
      gTd(cell(gNumT(gToman(f.nav))),f.nav,'s gs')+
      gTd(bubCell(f.nominal_bubble),f.nominal_bubble)+
      gTd(bubCell(f.intrinsic_bubble),f.intrinsic_bubble)+
      gTd(cell(gNumT(f.implied_dollar)),f.implied_dollar,'s')+
      gTd(f.value==null?'—':gNumT(f.value/1e10),f.value,'s gs')+
      gTd(gTime(f.trade_time),f.trade_time,'m')+'</tr>'}).join('');
  gResort(document.getElementById('gTable'));
});

/* spot gold and coins — prices in rial. Intrinsic value, bubble and
   implied dollar need validated gold-content constants (docs/gold-data-map.md) */
var SPOT=[['طلا گرم ۱۸ عیار','geram18'],['سکه امامی','sekee'],['سکه بهار آزادی','sekee_bahar'],
 ['نیم سکه','nim'],['ربع سکه','rob'],['مظنه آبشده (مثقال)','mesghal'],
 ['گواهی سکه','govahi_sekke'],['گواهی شمش','govahi_shemsh']];
onGold(function(g){
  var b=document.getElementById('sBody'); if(!b) return;
  b.innerHTML=SPOT.map(function(s){
    var r=g.m[s[1]], k=r&&r.unit==='IRR'?0.1:1, px=goldToman(r);   /* toman */
    /* intrinsic value (row unit) → toman; only the certificates have one (Nexus) */
    var intr=r&&r.intrinsic!=null?r.intrinsic*k:null;
    return '<tr>'+gTd(s[0],s[0])+gTd(gNumT(px),px,'k')+
      chgCells(r?r.change_pct:null,r&&r.change!=null?r.change*k:null)+
      gTd(gNumT(intr),intr,'s gs')+
      gTd(r&&r.bubble!=null?bubCell(r.bubble):'—',r?r.bubble:null)+
      gTd(gNumT(r?r.implied_dollar:null),r?r.implied_dollar:null,'s')+'</tr>'}).join('');
  gResort(document.getElementById('sTable'));
});

/* treemap — block size by today's traded value, colour by day change */
onGold(function(g){
  var m=document.getElementById('tmap'); if(!m) return;
  var SIZE=[[5,3],[3,2],[2,2],[2,2],[2,1],[2,1]];
  var C=['#B91C1C','#EF4444','#94A3B8','#4ADE80','#15803D'];
  var TXT=['#FFFFFF','#FFFFFF','#0B1220','#0B1220','#FFFFFF'];  /* ink per cell */
  var rows=g.funds.filter(function(f){return f.value}).sort(function(x,y){return y.value-x.value});
  m.innerHTML=rows.map(function(f,i){
    var sz=SIZE[i]||[1,1], r=f.change_pct==null?0:f.change_pct*100;
    var k=r<-1.5?0:(r<-0.4?1:(r<0.4?2:(r<1.5?3:4)));
    return '<div title="'+f.symbol+' · '+gBillion(f.value)+' تومان" style="grid-column:span '+sz[0]+';grid-row:span '+sz[1]+
      ';background:'+C[k]+';color:'+TXT[k]+'">'+f.symbol+'<br><span style="font-size:10px;opacity:.9">'+
      gPct(f.change_pct)+'</span></div>'}).join('');
});

/* ── NAV trend — every fund's intraday NAV as % change from its previous-day
   close (prev_close; the first NAV of the day only when there is none), so
   the zero line means "unchanged since yesterday". The picked fund is drawn
   bold over faint lines for the rest, with the market median as a dashed
   reference. Own feed (GOLD_NAV_API): only this page needs it. ── */
(function(){
  var W=640, H=300, PAD=16;
  var svg=document.getElementById('navSvg'); if(!svg) return;
  var $=function(id){return document.getElementById(id)};
  var lines=$('navLines'), hot=$('navHot'), area=$('navArea'), med=$('navMed'), grid=$('navGrid'),
      guide=$('navGuide'), dot=$('navDot'), tip=$('navTip'), list=$('navList'), yl=$('navYl');
  var D=null, sel=null, lo=0, hi=0, MED=[];

  function pcts(f){
    var base=f.prev_close||null;
    return f.nav.map(function(v){
      if(v==null) return null;
      if(base==null) base=v;
      return (v/base-1)*100});
  }
  function X(i){return D.times.length<2?0:i/(D.times.length-1)*W}
  function Y(v){return PAD+(hi-v)/(hi-lo||1)*(H-2*PAD)}
  function path(ps){
    var d='', pen=false;
    ps.forEach(function(v,i){
      if(v==null){pen=false; return}
      d+=(pen?'L':'M')+X(i).toFixed(1)+' '+Y(v).toFixed(1)+' '; pen=true});
    return d;
  }
  function fmt(v){return gPct(v==null?null:v/100)}
  function tone(f){var s=gSign(f); return s>0?'pos':(s<0?'neg':'zero')}

  function select(isin){
    sel=D.funds.filter(function(f){return f.isin===isin})[0]||D.funds[0];
    if(!sel) return;
    var ps=sel.p, t=tone(sel.change_pct);
    var rgb=t==='neg'?'rgb(220,38,38)':(t==='pos'?'rgb(22,163,74)':'rgb(100,116,139)');
    var d=path(ps);
    hot.setAttribute('d',d); hot.setAttribute('class','nav-hot '+t);
    $('navGradTop').setAttribute('stop-color',rgb); $('navGradBot').setAttribute('stop-color',rgb);
    var first=ps.findIndex(function(v){return v!=null}), last=-1;
    for(var i=ps.length-1;i>=0;i--) if(ps[i]!=null){last=i;break}
    if(first>=0&&last>first){
      /* fill towards the chart's bottom, so the gradient fades out below the line */
      area.setAttribute('d',d+'L'+X(last).toFixed(1)+' '+H+' L'+X(first).toFixed(1)+' '+H+' Z');
      var end=$('navEnd');
      end.style.left=(X(last)/W*100)+'%'; end.style.top=(Y(ps[last])/H*100)+'%';
      end.className='navend '+t; gText('navEndV',fmt(ps[last])); end.hidden=false;
    } else { area.removeAttribute('d'); $('navEnd').hidden=true; }
    [].forEach.call(lines.children,function(p){p.style.display=p.getAttribute('data-isin')===sel.isin?'none':''});
    gText('navSel',sel.symbol);
    var chip=gText('navSelV',gPct(sel.change_pct)); chip.className='navchip '+t;
    gText('navSelNav',gNum(gToman(sel.last))+' تومان');
    [].forEach.call(list.children,function(b){
      var on=b.getAttribute('data-isin')===sel.isin;
      b.setAttribute('aria-selected',on?'true':'false');
      if(on&&b.scrollIntoView&&list.scrollHeight>list.clientHeight){
        var top=b.offsetTop-list.offsetTop, bottom=top+b.offsetHeight;
        if(top<list.scrollTop||bottom>list.scrollTop+list.clientHeight) list.scrollTop=top-list.clientHeight/2;
      }
    });
    hideTip();
  }

  function draw(d){
    D=d;
    var ok=d.funds.length&&d.times.length>1;
    $('navEmpty').hidden=!!ok; if(!ok) return;
    d.funds.forEach(function(f){f.p=pcts(f)});
    var all=[]; d.funds.forEach(function(f){f.p.forEach(function(v){if(v!=null)all.push(v)})});
    lo=Math.min(0,Math.min.apply(null,all)); hi=Math.max(0,Math.max.apply(null,all));
    var pad=(hi-lo)*0.1||0.1; lo-=pad; hi+=pad;

    /* market median at every bucket — the reference the picked fund is read against */
    MED=d.times.map(function(_,i){
      var col=d.funds.map(function(f){return f.p[i]}).filter(function(v){return v!=null}).sort(function(a,b){return a-b});
      if(!col.length) return null;
      var k=(col.length-1)/2; return (col[Math.floor(k)]+col[Math.ceil(k)])/2;
    });
    med.setAttribute('d',path(MED));

    var span=hi-lo, step=[0.1,0.2,0.25,0.5,1,2,5].filter(function(s){return span/s<=5})[0]||10, g='', labels='';
    for(var v=Math.ceil(lo/step)*step; v<=hi+1e-9; v+=step){
      var y=Y(v), zero=Math.abs(v)<1e-9;
      g+='<line class="'+(zero?'zl':'gl')+'" x1="0" x2="'+W+'" y1="'+y.toFixed(1)+'" y2="'+y.toFixed(1)+'"/>';
      labels+='<span'+(zero?' class="z"':'')+' style="top:'+(y/H*100).toFixed(2)+'%">'+(zero?'دیروز':fmt(v))+'</span>';
    }
    grid.innerHTML=g; yl.innerHTML=labels;

    lines.innerHTML=d.funds.map(function(f){
      return '<path data-isin="'+f.isin+'" d="'+path(f.p)+'"><title>'+f.symbol+' '+gPct(f.change_pct)+'</title></path>'}).join('');

    var n=d.times.length, mid=Math.floor((n-1)/2);
    $('navAxis').innerHTML='<span>'+gTime(d.times[0])+'</span><span>'+gTime(d.times[mid])+'</span><span>'+gTime(d.times[n-1])+'</span>';
    gText('navDay',gDate(d.times[n-1]));

    var ranked=d.funds.slice().sort(function(a,b){return (b.change_pct||0)-(a.change_pct||0)});
    var mx=Math.max.apply(null,ranked.map(function(f){return Math.abs(f.change_pct||0)}))||1;
    list.innerHTML=ranked.map(function(f,i){
      var t=tone(f.change_pct);
      return '<button type="button" role="option" data-isin="'+f.isin+'" class="'+t+'">'+
        '<span class="rk">'+fa(i+1)+'</span><span class="nm">'+f.symbol+'</span>'+
        '<span class="v">'+gPct(f.change_pct)+'</span>'+
        '<span class="bar"><i style="width:'+Math.max(4,Math.abs(f.change_pct||0)/mx*100).toFixed(1)+'%"></i></span></button>'}).join('');

    select(sel?sel.isin:ranked[0].isin);
  }

  function hideTip(){tip.hidden=true; dot.hidden=true; guide.style.display='none'}
  function at(ev){
    if(!D||!sel) return;
    var r=svg.getBoundingClientRect(), cx=(ev.touches?ev.touches[0].clientX:ev.clientX)-r.left;
    var i=Math.max(0,Math.min(D.times.length-1,Math.round(cx/r.width*(D.times.length-1))));
    var v=sel.p[i]; if(v==null){hideTip(); return}
    var px=X(i)/W*r.width, py=Y(v)/H*r.height;
    guide.setAttribute('x1',X(i)); guide.setAttribute('x2',X(i)); guide.style.display='';
    dot.style.left=px+'px'; dot.style.top=py+'px'; dot.className='navdot '+tone(v); dot.hidden=false;
    tip.innerHTML='<span class="t">'+gTime(D.times[i])+'</span>'+
      '<span class="r"><em>'+sel.symbol+'</em><b class="'+tone(v)+'">'+fmt(v)+'</b></span>'+
      '<span class="r m"><em>میانه</em><b>'+fmt(MED[i])+'</b></span>';
    tip.style.left=Math.min(Math.max(px,80),r.width-80)+'px'; tip.hidden=false;
  }
  svg.addEventListener('mousemove',at);
  svg.addEventListener('mouseleave',hideTip);
  svg.addEventListener('touchstart',at,{passive:true});
  svg.addEventListener('touchmove',at,{passive:true});
  lines.addEventListener('click',function(e){
    var p=e.target.closest('path'); if(p) select(p.getAttribute('data-isin'))});
  list.addEventListener('click',function(e){
    var b=e.target.closest('button'); if(b) select(b.getAttribute('data-isin'))});

  goldFeed(GOLD_NAV_API, 60, draw);
})();

/* ── asset mix — whole market as a donut, each fund as a 100% bar ── */
(function(){
  var bars=document.getElementById('mixBars'); if(!bars) return;
  var KEYS={
    sekke:{label:'سهم سکه',v:function(f){return f.w.sk},fmt:pct0},
    shemsh:{label:'سهم شمش',v:function(f){return f.w.sh},fmt:pct0},
    other:{label:'سهم نقد و سایر',v:function(f){return f.w.ot},fmt:pct0},
    cap:{label:'ارزش بازار',v:function(f){return f.market_cap||0},fmt:function(f){return gHemat(f.market_cap)}},
    bubble:{label:'حباب',v:function(f){return f.nominal_bubble==null?-1e9:-f.nominal_bubble},
      fmt:function(f){return '<span style="color:'+gColor(f.nominal_bubble)+'">'+gPct(f.nominal_bubble)+'</span>'}}
  };
  var key='sekke', G=null, pick=null;   /* pick: isin of the fund shown in the donut, or null for the market */
  function pct0(f){return fa(Math.round(KEYS[key].v(f)*100))+'٪'}

  function donut(funds){
    /* one fund's own mix when a fund is picked, else the market-cap-weighted whole */
    var f=pick&&funds.filter(function(x){return x.isin===pick})[0], sk, sh;
    if(f){ sk=f.w.sk; sh=f.w.sh; }
    else{
      pick=null;
      var cap=0; sk=0; sh=0;
      funds.forEach(function(x){var c=x.market_cap||0; cap+=c; sk+=x.w.sk*c; sh+=x.w.sh*c});
      if(!cap) return;
      sk/=cap; sh/=cap;
    }
    gText('mixTitle',f?'ترکیب دارایی صندوق '+f.symbol:'ترکیب کل بازار صندوق‌های طلا');
    gText('mixNote',f?'از آخرین گزارش ماهانه صندوق · ارزش بازار '+gHemat(f.market_cap)
                     :'میانگین وزنی با ارزش بازار هر صندوق · روی هر صندوق بزنید');
    document.getElementById('mixReset').hidden=!f;
    var parts=[['sekke',sk,'var(--mix-coin)','گواهی سکه'],['shemsh',sh,'var(--mix-bar)','گواهی شمش'],
               ['other',Math.max(0,1-sk-sh),'var(--mix-other)','نقد و سایر']];
    var R=46, C=2*Math.PI*R, off=0;
    document.getElementById('mixDonut').innerHTML=
      '<circle cx="60" cy="60" r="'+R+'" fill="none" stroke="var(--surface-3)" stroke-width="16"/>'+
      parts.map(function(p){
        var len=p[1]*C, s='<circle cx="60" cy="60" r="'+R+'" fill="none" stroke="'+p[2]+'" stroke-width="16"'+
          ' stroke-dasharray="'+len.toFixed(2)+' '+(C-len).toFixed(2)+'" stroke-dashoffset="'+(-off).toFixed(2)+'"/>';
        off+=len; return s}).join('');
    gText('mixDonutV',fa(Math.round(parts[0][1]*100))+'٪');
    document.getElementById('mixLegend').innerHTML=parts.map(function(p){
      return '<span><i style="background:'+p[2]+'"></i>'+p[3]+'<b>'+fa((p[1]*100).toFixed(1)).replace('.','٫')+'٪</b></span>'}).join('');
  }

  function render(){
    if(!G) return;
    var funds=G.funds.filter(function(f){return f.weights}).map(function(f){
      var sk=f.weights.sekke_weight||0, sh=f.weights.shemsh_weight||0;
      f.w={sk:sk,sh:sh,ot:Math.max(0,1-sk-sh)}; return f});
    donut(funds);
    var k=KEYS[key];
    funds.sort(function(a,b){return k.v(b)-k.v(a)});
    bars.innerHTML=funds.map(function(f){
      var t=f.symbol+' — سکه '+fa(Math.round(f.w.sk*100))+'٪، شمش '+fa(Math.round(f.w.sh*100))+'٪، سایر '+fa(Math.round(f.w.ot*100))+'٪';
      return '<button type="button" class="mb'+(f.isin===pick?' on':'')+'" data-isin="'+f.isin+'" aria-pressed="'+(f.isin===pick)+'" title="'+t+'">'+
        '<span class="mb-n">'+f.symbol+'</span><span class="mb-bar">'+
        '<i style="width:'+(f.w.sk*100).toFixed(1)+'%;background:var(--mix-coin)"></i>'+
        '<i style="width:'+(f.w.sh*100).toFixed(1)+'%;background:var(--mix-bar)"></i>'+
        '<i style="width:'+(f.w.ot*100).toFixed(1)+'%;background:var(--mix-other)"></i>'+
        '</span><span class="mb-v">'+k.fmt(f)+'</span></button>'}).join('');
  }

  /* pick a fund → the donut shows its mix; pick it again (or "کل بازار") → back to the market */
  bars.addEventListener('click',function(e){
    var b=e.target.closest('.mb'); if(!b) return;
    var isin=b.getAttribute('data-isin');
    pick=pick===isin?null:isin;
    render();
  });
  document.getElementById('mixReset').addEventListener('click',function(){pick=null; render()});

  document.querySelectorAll('.mixsort button').forEach(function(b){
    b.addEventListener('click',function(){
      key=b.getAttribute('data-k');
      document.querySelectorAll('.mixsort button').forEach(function(x){
        x.setAttribute('aria-pressed',x===b?'true':'false')});
      render();
    });
  });
  onGold(function(g){G=g; render()});
})();

(function(){
  var links=[].slice.call(document.querySelectorAll('.subnav a'));
  var secs=links.map(function(a){return document.querySelector(a.getAttribute('href'))});
  var nav=document.querySelector('.subnav');
  /* everything pinned above the content: the sticky top bar and this sub-nav.
     Measured each time — their heights change with the font, width and menus. */
  function covered(){
    /* where the sub-nav's bottom will be once it is stuck — not where it is
       now: from the top of the page it still sits lower, in normal flow */
    if(!nav) return 0;
    var top=parseFloat(getComputedStyle(nav).top)||0;
    return Math.round(top+nav.getBoundingClientRect().height);
  }
  var lock=null;
  function spy(){
    if(lock!==null) return;                   /* keep the clicked tab lit while we scroll to it */
    var y=covered()+24, act=0;
    secs.forEach(function(s,i){if(s&&s.getBoundingClientRect().top<=y)act=i});
    links.forEach(function(a,i){a.classList.toggle('on',i===act)});
  }
  window.addEventListener('scroll',spy,{passive:true});
  links.forEach(function(a,i){
    a.addEventListener('click',function(e){
      var s=secs[i]; if(!s) return;
      e.preventDefault();
      /* land with the section title just below the pinned bars, not under them */
      var top=window.scrollY+s.getBoundingClientRect().top-covered()+1;
      links.forEach(function(l,j){l.classList.toggle('on',j===i)});
      lock=i; clearTimeout(a._t); a._t=setTimeout(function(){lock=null;spy()},900);
      var calm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({top:Math.max(0,top),behavior:calm?'auto':'smooth'});
      if(history.replaceState) history.replaceState(null,'',a.getAttribute('href'));
    });
  });
  spy();
})();
"""

# ═══════════════════════════ COVERED CALL DASHBOARD ═══════════════════════════
CC = """
<div class="apphead">
<div class="wrap">
  <div>
    <h1><span class="guest">نسخه مهمان</span>داشبورد کاوردکال</h1>
    <p>آخرین روز معاملاتی: <b class="num">۱۴۰۵/۰۶/۱۶</b> · آخرین به‌روزرسانی: <b class="num" id="cClock">۱۷:۳۱:۰۴</b> · داده نمایشی — اتصال به داده زنده به‌زودی</p>
  </div>
  <div style="display:flex;gap:10px;flex-wrap:wrap">
    <a class="btn btn-s" href="product-covered-call.html" style="padding:11px 20px;font-size:14px">معرفی محصول</a>
    <a class="btn btn-p" href="pricing.html" style="padding:11px 20px;font-size:14px">ورود / عضویت</a>
  </div>
</div>
</div>

<div class="subnav">
<div class="wrap">
  <a class="on" href="#ov">نمای کلی</a>
  <a href="#watch">دیدبان قراردادها</a>
  <a href="#chain">زنجیره قراردادها</a>
  <a href="#pl">نمودار سود و زیان</a>
  <a href="#port">پرتفوی من</a>
  <a href="#ctools">ابزارها</a>
</div>
</div>

<!-- OVERVIEW -->
<section class="dsec" id="ov">
<div class="wrap">
  <div class="sh"><div><h2>نمای کلی بازار اختیار</h2><p>وضعیت کلی بازار اختیار معامله بورس تهران</p></div></div>
  <div class="tiles">
    <div class="tile"><small>ارزش معاملات اختیار</small><b class="num">۱۷٫۸ همت</b><div class="sub"><span class="up">▲ ۲۵٫۲٪</span></div></div>
    <div class="tile"><small>قرارداد فعال کال</small><b class="num">۳۶۸</b><div class="sub">در ۴۲ نماد پایه</div></div>
    <div class="tile" style="border-color:var(--gold-400);background:rgba(240,180,41,.05)"><small>فرصت با نرخ بالای ۵۰٪</small><b class="num" id="cOpp" style="color:var(--gold-700)">۱۲</b><div class="sub">کمتر از ۴٪ کل بازار</div></div>
    <div class="tile"><small>بیشترین نرخ معادل سالانه</small><b class="num" style="color:var(--up-text)">۶۹٫۴٪</b><div class="sub">ضستا۳۰۱۰ · ۱۵ روز</div></div>
  </div>
</div>
</section>

<!-- WATCHLIST -->
<section class="dsec" id="watch">
<div class="wrap">
  <div class="sh">
    <div><h2>دیدبان قراردادهای اختیار خرید</h2><p>حاشیه ریسک، سود دوره‌ای و نرخ معادل سالانه — محاسبه‌شده و باز برای همه</p></div>
@@IFLOCK@@    <a class="lockcell" href="pricing.html" style="font-size:12.5px;padding:7px 14px">🔒 باز کردن همه ستون‌ها</a>@@END@@
  </div>
  <div class="dwrap"><div class="tscroll">
    <table class="dt">
      <thead><tr><th>نماد</th><th>سهم پایه</th><th>آخرین</th><th>DTM</th><th>قیمت اعمال</th>
        <th>حاشیه ریسک</th><th>سود دوره‌ای</th><th>نرخ معادل سالانه</th></tr></thead>
      <tbody id="cBody"></tbody>
    </table>
  </div></div>
  <p style="font-size:12px;color:var(--slate-400);margin-top:10px">۱۲ قرارداد از ۳۶۸ قرارداد فعال در حال نمایش · فیلتر سفارشی و هشدار به‌زودی</p>
</div>
</section>

<!-- CHAIN -->
<section class="dsec" id="chain">
<div class="wrap">
  <div class="sh"><div><h2>زنجیره قراردادها — شستا</h2><p>قیمت‌های اعمال یک سررسید، روبه‌روی هم</p></div></div>
  <div class="dwrap"><div class="tscroll">
    <table class="dt">
      <thead><tr><th>نماد کال</th><th>آخرین</th><th>حجم</th><th>موقعیت باز</th><th>قیمت اعمال</th><th>حاشیه ریسک</th><th>نرخ معادل سالانه</th></tr></thead>
      <tbody>
        <tr><td>ضستا۳۰۰۶</td><td>۸۸۸</td><td>۲,۱۷۰</td><td>۱۱,۳۰۰</td><td>۱,۰۰۰</td><td>@@L:۸۷٫۳٪@@</td><td>@@L:<span class="up">۴۴٫۵٪</span>@@</td></tr>
        <tr><td>ضستا۳۰۰۸</td><td>۶۹۵</td><td>۱,۲۴۰</td><td>۸,۴۰۰</td><td>۱,۲۰۰</td><td>@@L:۵۶٫۱٪@@</td><td>@@L:<span class="up">۵۶٫۹٪</span>@@</td></tr>
        <tr style="background:rgba(240,180,41,.06)"><td>ضستا۳۰۱۰</td><td>۵۰۳</td><td>۳,۸۱۰</td><td>۲۴,۶۰۰</td><td>۱,۴۰۰</td><td>@@L:۳۳٫۸٪@@</td><td>@@L:<span class="up">۶۹٫۴٪</span>@@</td></tr>
        <tr><td>ضستا۳۰۱۲</td><td>۲۹۷</td><td>۲,۰۵۰</td><td>۱۵,۲۰۰</td><td>۱,۶۰۰</td><td>@@L:۱۷٫۱٪@@</td><td>@@L:<span class="up">۴۴٫۵٪</span>@@</td></tr>
        <tr><td>ضستا۳۰۱۴</td><td>۹۳</td><td>۹۸۰</td><td>۹,۷۰۰</td><td>۱,۸۰۰</td><td>@@L:۴٫۱٪@@</td><td>@@L:<span class="up">۳۱٫۲٪</span>@@</td></tr>
      </tbody>
    </table>
  </div></div>
  <p style="font-size:12px;color:var(--slate-400);margin-top:10px">زنجیره نماد شستا · ۴۲ نماد پایه دیگر به‌زودی</p>
</div>
</section>

<!-- P/L -->
<section class="dsec" id="pl">
<div class="wrap">
  <div class="sh"><div><h2>نمودار سود و زیان</h2><p>یک نمونه رایگان — استراتژی‌ساز کامل با عضویت</p></div></div>
  <div class="lockgrid">
    <div class="card">
      <h3 style="font-size:15px;margin-bottom:4px">ضستا۳۰۱۰ — کاوردکال ۱۵ روزه</h3>
      <p style="font-size:12.5px;color:var(--slate-500);margin:0 0 14px">P=۱٬۸۷۳ · K=۱٬۴۰۰ · C=۵۰۳ · نرخ معادل ۶۹٫۴٪</p>
      <svg viewBox="0 0 420 230" style="width:100%;height:auto;display:block">
        <line x1="40" y1="20" x2="40" y2="190" stroke="#CBD5E1"/>
        <line x1="40" y1="115" x2="406" y2="115" stroke="#CBD5E1" stroke-width="1.4"/>
        <rect x="180" y="20" width="120" height="170" fill="rgba(240,180,41,.10)"/>
        <path d="M40 182 L140 115" stroke="#DC2626" stroke-width="2.6" fill="none" stroke-linecap="round"/>
        <path d="M140 115 L180 62" stroke="#64748B" stroke-width="2.6" fill="none" stroke-linecap="round"/>
        <path d="M180 62 L406 62" stroke="#16A34A" stroke-width="3" fill="none" stroke-linecap="round"/>
        <line x1="140" y1="30" x2="140" y2="190" stroke="#94A3B8" stroke-dasharray="4 4"/>
        <line x1="180" y1="30" x2="180" y2="190" stroke="#C9861A" stroke-dasharray="4 4"/>
        <circle cx="140" cy="115" r="4.5" fill="#DC2626"/><circle cx="180" cy="62" r="5" fill="#16A34A"/>
        <text x="400" y="52" font-size="13" fill="#0F7233" font-weight="800" text-anchor="end" direction="rtl" font-family="Vazirmatn">سود سالانه ۶۹٫۴٪</text>
        <text x="140" y="208" font-size="12" fill="#475569" text-anchor="middle" font-family="Vazirmatn">۱٬۳۷۰</text>
        <text x="180" y="208" font-size="12" fill="#8A5A08" font-weight="700" text-anchor="middle" font-family="Vazirmatn">۱٬۴۰۰</text>
        <text x="34" y="119" font-size="11" fill="#94A3B8" text-anchor="end" font-family="Vazirmatn">۰</text>
      </svg>
    </div>
    <div class="lockpanel">
      <div class="ic">🔒</div>
      <h3>استراتژی‌ساز چندپایه</h3>
      <p>پاهای موقعیت را خودتان بچینید و نمودار سود و زیان، نقطه سربه‌سری، بیشینه سود و بیشینه زیان را پیش از ورود ببینید — از کاوردکال تا ساختارهای چندپایه.</p>
      <a class="btn btn-p" href="pricing.html" style="padding:11px 24px;font-size:14px">ورود / عضویت</a>
    </div>
  </div>
</div>
</section>

<!-- PORTFOLIO -->
<section class="dsec" id="port">
<div class="wrap">
  <div class="sh"><div><h2>پرتفوی من</h2><p>پایش موقعیت‌های باز، سررسید و فاصله تا نقطه سربه‌سری</p></div></div>
  <div class="lockpanel" style="padding:44px 26px">
    <div class="ic">📊</div>
    <h3>موقعیت‌های خود را ثبت کنید</h3>
    <p>هر موقعیت کاوردکال را یک بار ثبت کنید تا سود و زیان واقعی، روزهای باقی‌مانده تا سررسید و فاصله لحظه‌ای قیمت سهم تا نقطه سربه‌سری را در یک صفحه ببینید. هشدار نزدیک شدن به نقطه سربه‌سری هم می‌گیرید.</p>
    <a class="btn btn-p" href="pricing.html" style="padding:12px 28px">ورود / عضویت</a>
  </div>
</div>
</section>

<!-- TOOLS -->
<section class="dsec" id="ctools" style="border-bottom:0">
<div class="wrap">
  <div class="sh"><div><h2>ابزارها</h2><p>یکی رایگان، بقیه با عضویت</p></div></div>
  <div class="lockgrid">
    <div class="card" style="text-align:center;padding:26px">
      <div style="font-size:26px;margin-bottom:10px">🧮</div>
      <h3 style="font-size:16px;margin-bottom:7px">ماشین‌حساب کاوردکال</h3>
      <p style="margin:0 0 16px;font-size:13.5px;color:var(--slate-600);max-width:420px;margin-inline:auto">اعداد موقعیت خودتان را وارد کنید و نرخ معادل سالانه، حاشیه ریسک و نقطه سربه‌سری را ببینید.</p>
      <span class="live" style="margin-bottom:14px"><i></i>رایگان و بدون ثبت‌نام</span><br>
      <a class="btn btn-s" href="tools-covered-call.html" style="padding:11px 24px;font-size:14px;margin-top:12px">باز کردن ابزار</a>
    </div>
    <div class="lockpanel">
      <div class="ic">🔔</div>
      <h3>هشدار فرصت</h3>
      <p>شرط دلخواهتان را تعریف کنید — مثلاً «نرخ معادل بالای ۶۰٪ با حاشیه ریسک بیش از ۲۵٪» — و هر بار که چنین قراردادی در بازار ظاهر شد، پیامک بگیرید.</p>
      <a class="btn btn-p" href="pricing.html" style="padding:11px 24px;font-size:14px">ورود / عضویت</a>
    </div>
  </div>

""" + SIGNUP.format(h="نرخ معادل سالانه و حاشیه ریسک را باز کنید",
                    p="با عضویت رایگان، دیدبان کامل در اختیارتان است. با پلن حرفه‌ای، استراتژی‌ساز، پرتفوی و هشدار هم اضافه می‌شود.") + """
</div>
</section>

<div class="riskbar"><div class="wrap">
  بازده اعلام‌شده در صورت تحقق سناریوی مطلوب و تا سقف حاشیه ریسک محاسبه می‌شود و تضمین‌شده نیست. اطلاعات این داشبورد توصیه به خرید یا فروش هیچ اوراق بهاداری محسوب نمی‌شود.
</div></div>
"""

CC_JS = paywall.js_flag() + """
/* [نماد, سهم پایه, C = قیمت اختیار, DTM, K = قیمت اعمال, P = قیمت سهم]
   همان فرمول ماشین‌حساب و مقاله — یک منبع، سه صفحه:
     نرخ معادل سالانه = (K/(P−C))^(365/DTM) − 1
     حاشیه ریسک       = P/K − 1
     نقطه سربه‌سری     = P − C                                          */
var ROWS=[
 ['ضستا۳۰۱۰','شستا',503,15,1400,1873],['ضشنا۶۰۴۹','شنا',1851,20,6000,7696],
 ['ضخود۶۰۵۵','خودرو',1262,57,3000,4082],['ضملی۳۰۵۸','ملی',454,43,1260,1663],
 ['ضفولا۶۰۳۲','فولاد',1338,29,4500,5677],['ضهرم۷۰۲۲','اهرم',588,26,2100,2623],
 ['ضفزر۱۰۱۳','فزر',2283,71,7500,9180],['ضاهرم۴۰۲۲','اهرم',412,36,1800,2140],
 ['ضبمل۲۰۰۷','بمل',298,22,1150,1420],['ضشپنا۵۰۳۱','شپنا',760,34,2900,3558],
 ['ضتپکو۹۰۱۵','تپکو',195,18,880,1059],['ضونفت۴۰۴۰','ونفت',630,49,2400,2922]];
function n1(v){return fa(v.toFixed(1)).replace('.','٫')}
(function(){
  var b=document.getElementById('cBody'); if(!b) return;
  b.innerHTML=ROWS.map(function(r){
    return '<tr><td>'+r[0]+'</td><td>'+r[1]+'</td><td>'+fa(grp(r[2]))+'</td><td>'+fa(r[3])+'</td>'+
      '<td>'+fa(grp(r[4]))+'</td>'+
      (PAYWALL?'<td>'+LOCK+'</td><td>'+LOCK+'</td><td>'+LOCK+'</td>':(function(){
        var C=r[2],D=r[3],K=r[4],P=r[5],net=P-C;
        var rate=(Math.pow(K/net,365/D)-1)*100, risk=(P/K-1)*100, per=(K/net-1)*100;
        return '<td>'+n1(risk)+'٪</td><td>'+n1(per)+'٪</td>'+
               '<td><span class="up">'+n1(rate)+'٪</span></td>'})())+'</tr>'}).join('');
})();
var t0=new Date(); t0.setHours(17,31,4,0);
if(!(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches)){
  setInterval(function(){t0=new Date(t0.getTime()+1000);
    var c=document.getElementById('cClock'); if(c) c.textContent=
      fa(('0'+t0.getHours()).slice(-2)+':'+('0'+t0.getMinutes()).slice(-2)+':'+('0'+t0.getSeconds()).slice(-2))},1000);
  setInterval(function(){
    var n=document.getElementById('cOpp'), v=10+Math.floor(Math.random()*6);
    if(n && fa(v)!==n.textContent){n.textContent=fa(v)}},5000);
}
(function(){
  var links=[].slice.call(document.querySelectorAll('.subnav a'));
  var secs=links.map(function(a){return document.querySelector(a.getAttribute('href'))});
  var nav=document.querySelector('.subnav');
  /* everything pinned above the content: the sticky top bar and this sub-nav.
     Measured each time — their heights change with the font, width and menus. */
  function covered(){
    /* where the sub-nav's bottom will be once it is stuck — not where it is
       now: from the top of the page it still sits lower, in normal flow */
    if(!nav) return 0;
    var top=parseFloat(getComputedStyle(nav).top)||0;
    return Math.round(top+nav.getBoundingClientRect().height);
  }
  var lock=null;
  function spy(){
    if(lock!==null) return;                   /* keep the clicked tab lit while we scroll to it */
    var y=covered()+24, act=0;
    secs.forEach(function(s,i){if(s&&s.getBoundingClientRect().top<=y)act=i});
    links.forEach(function(a,i){a.classList.toggle('on',i===act)});
  }
  window.addEventListener('scroll',spy,{passive:true});
  links.forEach(function(a,i){
    a.addEventListener('click',function(e){
      var s=secs[i]; if(!s) return;
      e.preventDefault();
      /* land with the section title just below the pinned bars, not under them */
      var top=window.scrollY+s.getBoundingClientRect().top-covered()+1;
      links.forEach(function(l,j){l.classList.toggle('on',j===i)});
      lock=i; clearTimeout(a._t); a._t=setTimeout(function(){lock=null;spy()},900);
      var calm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({top:Math.max(0,top),behavior:calm?'auto':'smooth'});
      if(history.replaceState) history.replaceState(null,'',a.getAttribute('href'));
    });
  });
  spy();
})();
"""

# ── resolve the paywall markers for the current mode ──────────────────
GOLD = paywall.apply(GOLD)
CC = paywall.apply(CC)
