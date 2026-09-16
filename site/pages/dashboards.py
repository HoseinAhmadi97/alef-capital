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
  <div>
    <h1><span class="guest">نسخه مهمان</span>داشبورد آربیتراژ صندوق طلا</h1>
    <p>آخرین روز معاملاتی: <b class="num gdate">—</b> · آخرین به‌روزرسانی: <b class="num gupdated">—</b> · <span id="gState">در حال دریافت داده</span></p>
  </div>
  <div style="display:flex;gap:10px;flex-wrap:wrap">
    <a class="btn btn-s" href="product-gold.html" style="padding:11px 20px;font-size:14px">معرفی محصول</a>
    <a class="btn btn-p" href="pricing.html" style="padding:11px 20px;font-size:14px">ورود / عضویت</a>
  </div>
</div>
</div>

<div class="subnav">
<div class="wrap">
  <a class="on" href="#overview">نمای کلی</a>
  <a href="#funds">صندوق‌های طلا</a>
  <a href="#spot">طلا و سکه</a>
  <a href="#map">نقشه بازار</a>
  <a href="#nav">روند NAV</a>
  <a href="#mix">ترکیب دارایی</a>
  <a href="#tools">ابزارها</a>
</div>
</div>

<!-- OVERVIEW -->
<section class="dsec" id="overview">
<div class="wrap">
  <div class="sh"><div><h2>نمای کلی بازار</h2><p>قیمت دارایی‌های پایه که ارزش ذاتی صندوق‌ها از روی آن‌ها محاسبه می‌شود</p></div></div>
  <div class="tiles" id="gTiles">
    <div class="tile" data-sym="ons"><small>انس جهانی طلا (دلار)</small><b class="num">—</b><div class="sub">—</div></div>
    <div class="tile" data-sym="geram18"><small>طلای گرمی ۱۸ عیار (ریال)</small><b class="num">—</b><div class="sub">—</div></div>
    <div class="tile" data-sym="funds"><small>میانگین تغییر صندوق‌های طلا</small><b class="num">—</b><div class="sub">—</div></div>
    <div class="tile" data-sym="dollar"><small>دلار (تومان)</small><b class="num">—</b><div class="sub">—</div></div>
  </div>
  <div class="tiles" style="margin-top:14px">
    <div class="tile" style="border-color:var(--gold-400);background:rgba(240,180,41,.05)"><small>میانگین حباب صندوق‌ها</small><b class="num" id="gAvg">—</b><div class="sub"><span class="gcount">—</span> صندوق تحت پایش</div></div>
    <div class="tile"><small>پرحباب‌ترین صندوق</small><b class="num" id="gMax" style="color:var(--down)">—</b><div class="sub" id="gMaxN">—</div></div>
    <div class="tile"><small>کم‌حباب‌ترین صندوق</small><b class="num" id="gMin" style="color:var(--up-text)">—</b><div class="sub" id="gMinN">—</div></div>
    <div class="tile"><small>ارزش معاملات صندوق‌ها</small><b class="num" id="gVal">—</b><div class="sub">مجموع امروز</div></div>
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
  <div class="dwrap"><div class="tscroll">
    <table class="dt">
      <thead><tr><th>نماد</th><th>آخرین قیمت</th><th>درصد تغییر</th><th>مقدار تغییر</th>
        <th>ارزش ذاتی (NAV)</th><th>حباب</th><th>دلار محاسباتی</th><th>زمان</th></tr></thead>
      <tbody id="gBody"></tbody>
    </table>
  </div></div>
  <p style="font-size:12px;color:var(--slate-400);margin-top:10px"><span class="gcount">—</span> صندوق به ترتیب ارزش معاملات · قیمت و NAV به ریال · دلار محاسباتی = دلار × قیمت ÷ NAV</p>
</div>
</section>

<!-- SPOT -->
<section class="dsec" id="spot">
<div class="wrap">
  <div class="sh"><div><h2>طلا و سکه — بازار نقدی</h2><p>مبنای محاسبه ارزش ذاتی گواهی‌های سپرده</p></div></div>
  <div class="dwrap"><div class="tscroll">
    <table class="dt">
      <thead><tr><th>عنوان</th><th>آخرین قیمت</th><th>درصد تغییر</th><th>مقدار تغییر</th>
        <th>ارزش ذاتی</th><th>حباب</th><th>دلار محاسباتی</th></tr></thead>
      <tbody id="sBody"></tbody>
    </table>
  </div></div>
  <p style="font-size:12px;color:var(--slate-400);margin-top:10px">قیمت‌ها به ریال · ارزش ذاتی، حباب و دلار محاسباتی سکه‌ها به‌زودی</p>
</div>
</section>

<!-- MAP -->
<section class="dsec" id="map">
<div class="wrap">
  <div class="sh"><div><h2>نقشه بازار صندوق‌های طلا</h2><p>اندازه هر بلوک: ارزش معاملات · رنگ: بازدهی روزانه</p></div>
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
  <div class="tmap" id="tmap"></div>
</div>
</section>

<!-- NAV TREND -->
<section class="dsec" id="nav">
<div class="wrap">
  <div class="sh"><div><h2>روند ارزش خالص دارایی (NAV)</h2><p>در نسخه مهمان فقط یک صندوق نمایش داده می‌شود</p></div></div>
  <div class="lockgrid">
    <div class="card">
      <h3 style="font-size:15px;margin-bottom:4px">صندوق <span id="navFund">—</span> — روند NAV درون‌روزی</h3>
      <p style="font-size:12.5px;color:var(--slate-500);margin:0 0 14px">بزرگ‌ترین صندوق طلا · تغییر NAV نسبت به ابتدای روز · <span id="navLast">—</span></p>
      <svg viewBox="0 0 420 220" style="width:100%;height:auto;display:block">
        <rect x="34" y="10" width="372" height="160" fill="var(--surface-2)" rx="8"/>
        <line x1="34" y1="90" x2="406" y2="90" stroke="var(--border-strong)" stroke-dasharray="3 3"/>
        <path id="navLine" fill="none" stroke="#C9861A" stroke-width="2.5" stroke-linejoin="round"/>
        <text x="34" y="192" font-size="11" fill="#64748B" font-family="Vazirmatn" id="navT0"></text>
        <text x="406" y="192" font-size="11" fill="#64748B" text-anchor="end" font-family="Vazirmatn" id="navT1"></text>
        <text x="28" y="22" font-size="10" fill="#94A3B8" text-anchor="end" font-family="Vazirmatn" id="navTop"></text>
        <text x="28" y="94" font-size="10" fill="#94A3B8" text-anchor="end" font-family="Vazirmatn">۰٪</text>
        <text x="28" y="166" font-size="10" fill="#94A3B8" text-anchor="end" font-family="Vazirmatn" id="navBottom"></text>
      </svg>
    </div>
    <div class="lockpanel">
      <div class="ic">🔒</div>
      <h3>مقایسه هم‌زمان <span class="gcount">—</span> صندوق</h3>
      <p>روند <span dir="ltr">Latent NAV</span>، <span dir="ltr">Pure NAV</span> و نسبت این دو، به تفکیک هر صندوق و قابل مقایسه روی یک نمودار.</p>
      <a class="btn btn-p" href="pricing.html" style="padding:11px 24px;font-size:14px">ورود / عضویت</a>
    </div>
  </div>
</div>
</section>

<!-- ASSET MIX -->
<section class="dsec" id="mix">
<div class="wrap">
  <div class="sh"><div><h2>ترکیب دارایی صندوق‌ها</h2><p>سهم سکه، شمش و سایر ابزارها — تعیین‌کننده اینکه حباب هر صندوق چقدر توجیه‌پذیر است</p></div></div>
  <div class="dwrap"><div class="tscroll">
    <table class="dt">
      <thead><tr><th>صندوق</th><th>سهم گواهی سکه</th><th>سهم گواهی شمش</th><th>سایر / نقد</th><th>همبستگی با سکه</th><th>حباب تعدیل‌شده</th></tr></thead>
      <tbody id="mixBody"></tbody>
    </table>
  </div></div>
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
                    p="با عضویت رایگان، جدول کامل ۳۰ صندوق با تأخیر ۱۵ دقیقه در اختیارتان است. با پلن طلا، همان جدول لحظه‌ای می‌شود و محاسبه‌گر، تاریخچه ۶ ماهه و هشدار هم اضافه می‌شود.") + """@@END@@
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
  var s=gSign(f), cls=s<0?'dn':(s>0?'up':'');
  return '<td class="'+cls+'">'+gArrow(f)+'</td><td class="'+cls+'">'+(abs==null?'—':gNum(Math.abs(abs)))+'</td>'}
function bubCell(b){
  if(PAYWALL) return LOCK;
  var s=gSign(b); return '<span class="'+(s<0?'up':(s>0?'dn':''))+'">'+gPct(b)+'</span>'}

/* header state */
onGold(function(g){
  gText('gState',g.summary.market_open?'بازار در حال معامله است':'بازار بسته است · آخرین معامله '+gTime(g.summary.last_trade_time));
});

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
    var s=gSign(f);
    if(k==='funds'){
      v.style.color=s<0?'var(--down)':(s>0?'var(--up-text)':'');
      sub.textContent='آخرین معامله · '+gTime(when);
    }else sub.innerHTML='<span class="'+(s<0?'dn':(s>0?'up':''))+'">'+gArrow(f)+'</span> · '+gTime(when);
  });
  var s=g.summary, e=gText('gAvg',gPct(s.avg_bubble));
  if(e) e.style.color=s.avg_bubble<0?'var(--up-text)':'var(--down)';
  if(s.max_bubble){gText('gMax',gPct(s.max_bubble.bubble)); gText('gMaxN',s.max_bubble.symbol)}
  if(s.min_bubble){gText('gMin',gPct(s.min_bubble.bubble)); gText('gMinN',s.min_bubble.symbol)}
  gText('gVal',gHemat(s.total_value));
});

/* funds table */
onGold(function(g){
  var b=document.getElementById('gBody'); if(!b) return;
  var usd=g.m.dollar?g.m.dollar.price:null;
  var rows=g.funds.slice().sort(function(x,y){return (y.value||0)-(x.value||0)});
  b.innerHTML=rows.map(function(f){
    var ok=f.last_trade&&f.nav_live;
    return '<tr><td>صندوق '+f.symbol+'</td><td>'+gNum(f.last_trade)+'</td>'+chgCells(f.change_pct,f.change)+
      '<td>'+cell(gNum(f.nav_live))+'</td>'+
      '<td>'+bubCell(f.nominal_bubble)+'</td>'+
      '<td>'+cell(ok&&usd?gNum(usd*f.last_trade/f.nav_live):'—')+'</td><td>'+gTime(f.trade_time)+'</td></tr>'}).join('');
});

/* spot gold and coins — prices in rial. Intrinsic value, bubble and
   implied dollar need validated gold-content constants (docs/gold-data-map.md) */
var SPOT=[['طلا گرم ۱۸ عیار','geram18'],['سکه امامی','sekee'],['سکه بهار آزادی','sekee_bahar'],
 ['نیم سکه','nim'],['ربع سکه','rob'],['مظنه آبشده (مثقال)','mesghal'],
 ['گواهی سکه','govahi_sekke'],['گواهی شمش','govahi_shemsh']];
onGold(function(g){
  var b=document.getElementById('sBody'); if(!b) return;
  b.innerHTML=SPOT.map(function(s){
    var r=g.m[s[1]], k=r&&r.unit==='IRT'?10:1;
    return '<tr><td>'+s[0]+'</td><td>'+gNum(goldRial(r))+'</td>'+
      chgCells(r?r.change_pct:null,r&&r.change!=null?r.change*k:null)+
      '<td>—</td><td>—</td><td>—</td></tr>'}).join('');
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

/* NAV trend — the largest fund, change against its first NAV of the day */
onGold(function(g){
  var p=document.getElementById('navLine'), ser=g.series.nav;
  if(!p||!ser||ser.points.length<2) return;
  var base=ser.points[0].value;
  var ch=ser.points.map(function(q){return (q.value/base-1)*100});
  var M=Math.max(0.1,Math.max.apply(null,ch.map(Math.abs)));
  M=Math.ceil(M*10)/10;
  p.setAttribute('d',ch.map(function(v,i){
    var x=34+i/(ch.length-1)*372, y=90-v/M*68;
    return (i?'L':'M')+x.toFixed(1)+' '+y.toFixed(1)}).join(' '));
  gText('navFund',ser.label);
  gText('navT0',gTime(ser.points[0].time));
  gText('navT1',gTime(ser.points[ser.points.length-1].time));
  gText('navTop','‎+'+fa(M.toFixed(1)).replace('.','٫')+'٪');
  gText('navBottom','‎−'+fa(M.toFixed(1)).replace('.','٫')+'٪');
  gText('navLast','آخرین NAV '+gNum(ser.points[ser.points.length-1].value)+' ریال');
});

/* asset mix — this month's reported weights, largest funds first */
onGold(function(g){
  var b=document.getElementById('mixBody'); if(!b) return;
  function w(v){return v==null?'—':fa(Math.round(v*100))+'٪'}
  var rows=g.funds.filter(function(f){return f.weights})
    .sort(function(x,y){return (y.market_cap||0)-(x.market_cap||0)});
  b.innerHTML=rows.map(function(f){
    var sk=f.weights.sekke_weight||0, sh=f.weights.shemsh_weight||0;
    return '<tr><td>'+f.symbol+'</td><td>'+w(sk)+'</td><td>'+w(sh)+'</td><td>'+w(Math.max(0,1-sk-sh))+'</td>'+
      '<td>'+cell('—')+'</td><td>'+cell('—')+'</td></tr>'}).join('');
});

(function(){
  var links=[].slice.call(document.querySelectorAll('.subnav a'));
  var secs=links.map(function(a){return document.querySelector(a.getAttribute('href'))});
  window.addEventListener('scroll',function(){
    var y=window.scrollY+180, act=0;
    secs.forEach(function(s,i){if(s&&s.offsetTop<=y)act=i});
    links.forEach(function(a,i){a.classList.toggle('on',i===act)});
  },{passive:true});
})();
"""

# ═══════════════════════════ COVERED CALL DASHBOARD ═══════════════════════════
CC = """
<div class="apphead">
<div class="wrap">
  <div>
    <h1><span class="guest">نسخه مهمان</span>داشبورد کاوردکال</h1>
    <p>آخرین روز معاملاتی: <b class="num">۱۴۰۵/۰۶/۱۶</b> · آخرین به‌روزرسانی: <b class="num" id="cClock">۱۷:۳۱:۰۴</b> · داده با تأخیر ۱۵ دقیقه</p>
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
                    p="با عضویت رایگان، دیدبان کامل با تأخیر ۱۵ دقیقه در اختیارتان است. با پلن حرفه‌ای، همان دیدبان لحظه‌ای می‌شود و استراتژی‌ساز، پرتفوی و هشدار هم اضافه می‌شود.") + """
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
  window.addEventListener('scroll',function(){
    var y=window.scrollY+180, act=0;
    secs.forEach(function(s,i){if(s&&s.offsetTop<=y)act=i});
    links.forEach(function(a,i){a.classList.toggle('on',i===act)});
  },{passive:true});
})();
"""

# ── resolve the paywall markers for the current mode ──────────────────
GOLD = paywall.apply(GOLD)
CC = paywall.apply(CC)
