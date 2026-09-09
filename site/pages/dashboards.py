# -*- coding: utf-8 -*-
"""Guest dashboards — gold arbitrage and covered call, with the per-cell paywall."""

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
    <p>آخرین روز معاملاتی: <b class="num">۱۴۰۵/۰۶/۱۶</b> · آخرین به‌روزرسانی: <b class="num" id="gClock">۱۷:۳۱:۰۴</b> · داده با تأخیر ۱۵ دقیقه</p>
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
  <div class="tiles">
    <div class="tile"><small>انس جهانی طلا (دلار)</small><b class="num">۴,۰۰۵</b><div class="sub"><span class="dn">▼ ۰٫۶۳٪</span> · ۱۷:۳۱</div></div>
    <div class="tile"><small>طلای گرمی ۱۸ عیار</small><b class="num">۱۸۲,۲۵۷,۰۰۰</b><div class="sub"><span class="dn">▼ ۰٫۱۴٪</span> · ۱۷:۲۶</div></div>
    <div class="tile"><small>شاخص صندوق‌های طلا</small><b class="num">۲۳,۴۱۸</b><div class="sub"><span class="up">▲ ۰٫۶۲٪</span> · ۱۷:۳۱</div></div>
    <div class="tile"><small>دلار محاسباتی</small><b class="num">۱۸۹,۰۰۰</b><div class="sub">— ۰٫۰۰٪ · ۱۷:۳۱</div></div>
  </div>
  <div class="tiles" style="margin-top:14px">
    <div class="tile" style="border-color:var(--gold-400);background:rgba(240,180,41,.05)"><small>میانگین حباب صندوق‌ها</small><b class="num" id="gAvg" style="color:var(--up-text)">‎−۰٫۳۴٪</b><div class="sub">۳۰ صندوق تحت پایش</div></div>
    <div class="tile"><small>پرحباب‌ترین صندوق</small><b class="num" id="gMax" style="color:var(--down)">‎+۲٫۵۰٪</b><div class="sub" id="gMaxN">کهربا</div></div>
    <div class="tile"><small>کم‌حباب‌ترین صندوق</small><b class="num" id="gMin" style="color:var(--up-text)">‎−۱٫۷۹٪</b><div class="sub" id="gMinN">گوهر</div></div>
    <div class="tile"><small>ارزش معاملات صندوق‌ها</small><b class="num">۴٫۲ همت</b><div class="sub"><span class="up">▲ ۸٫۳٪</span> نسبت به میانگین هفته</div></div>
  </div>
</div>
</section>

<!-- FUNDS TABLE -->
<section class="dsec" id="funds">
<div class="wrap">
  <div class="sh">
    <div><h2>صندوق‌های طلای بورس</h2><p>سه ستون آخر — ارزش ذاتی، حباب و دلار محاسباتی — با عضویت باز می‌شوند</p></div>
    <a class="lockcell" href="pricing.html" style="font-size:12.5px;padding:7px 14px">🔒 باز کردن همه ستون‌ها</a>
  </div>
  <div class="dwrap"><div class="tscroll">
    <table class="dt">
      <thead><tr><th>نماد</th><th>آخرین قیمت</th><th>درصد تغییر</th><th>مقدار تغییر</th>
        <th>ارزش ذاتی (NAV)</th><th>حباب</th><th>دلار محاسباتی</th><th>زمان</th></tr></thead>
      <tbody id="gBody"></tbody>
    </table>
  </div></div>
  <p style="font-size:12px;color:var(--slate-400);margin-top:10px">۳۰ صندوق در حال نمایش · مرتب‌سازی و فیلتر سفارشی با عضویت</p>
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
      <h3 style="font-size:15px;margin-bottom:4px">صندوق طلا — روند حباب درون‌روزی</h3>
      <p style="font-size:12.5px;color:var(--slate-500);margin:0 0 14px">نمونه رایگان</p>
      <svg viewBox="0 0 420 220" style="width:100%;height:auto;display:block">
        <rect x="34" y="10" width="372" height="160" fill="var(--surface-2)" rx="8"/>
        <line x1="34" y1="90" x2="406" y2="90" stroke="var(--border-strong)" stroke-dasharray="3 3"/>
        <path id="navLine" fill="none" stroke="#C9861A" stroke-width="2.5" stroke-linejoin="round"/>
        <text x="34" y="192" font-size="11" fill="#64748B" font-family="Vazirmatn">۰۹:۰۰</text>
        <text x="406" y="192" font-size="11" fill="#64748B" text-anchor="end" font-family="Vazirmatn">۱۲:۳۰</text>
        <text x="28" y="94" font-size="10" fill="#94A3B8" text-anchor="end" font-family="Vazirmatn">۰٪</text>
      </svg>
    </div>
    <div class="lockpanel">
      <div class="ic">🔒</div>
      <h3>مقایسه هم‌زمان ۳۰ صندوق</h3>
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
      <tbody>
        <tr><td>طلا</td><td>۶۲٪</td><td>۳۴٪</td><td>۴٪</td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td></tr>
        <tr><td>کهربا</td><td>۷۱٪</td><td>۲۵٪</td><td>۴٪</td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td></tr>
        <tr><td>گوهر</td><td>۴۸٪</td><td>۴۹٪</td><td>۳٪</td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td></tr>
        <tr><td>زر</td><td>۵۵٪</td><td>۴۱٪</td><td>۴٪</td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td></tr>
        <tr><td>عیار</td><td>۶۸٪</td><td>۲۹٪</td><td>۳٪</td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td></tr>
      </tbody>
    </table>
  </div></div>
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
      <a class="btn btn-p" href="pricing.html" style="padding:11px 24px;font-size:14px">ورود / عضویت</a>
    </div>
    <div class="lockpanel">
      <div class="ic">📁</div>
      <h3>ساخت سبد دارایی</h3>
      <p>صندوق‌های خودتان را وارد کنید و سود و زیان و ارزش دارایی طلای پرتفوتان را لحظه‌ای ببینید. هشدار عبور حباب از آستانه هم می‌گذارید.</p>
      <a class="btn btn-p" href="pricing.html" style="padding:11px 24px;font-size:14px">ورود / عضویت</a>
    </div>
  </div>

""" + SIGNUP.format(h="ارزش ذاتی، حباب و دلار محاسباتی را باز کنید",
                    p="با عضویت رایگان، جدول کامل ۳۰ صندوق با تأخیر ۱۵ دقیقه در اختیارتان است. با پلن طلا، همان جدول لحظه‌ای می‌شود و محاسبه‌گر، تاریخچه ۶ ماهه و هشدار هم اضافه می‌شود.") + """
</div>
</section>

<div class="riskbar"><div class="wrap">
  اطلاعات ارائه‌شده در این داشبورد صرفاً جنبه تحلیلی و اطلاع‌رسانی دارد و توصیه به خرید یا فروش هیچ اوراق بهاداری محسوب نمی‌شود. مسئولیت تصمیم‌های معاملاتی بر عهده کاربر است.
</div></div>
"""

GOLD_JS = """
var LOCK='<a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a>';
var GF=[['طلا',172900,172835,-0.62,-1080],['کهربا',18420,18221,1.09,198],['گوهر',24160,24600,-1.79,-440],
 ['زر',15630,15702,-0.46,-72],['عیار',9840,9795,0.46,45],['مثقال',31250,31410,-0.51,-160],
 ['آلتون',12480,12390,0.73,90],['ناب',8720,8801,-0.92,-81],['نفیس',21340,21180,0.76,160],
 ['تابش',7650,7712,-0.80,-62],['زرفام',14210,14118,0.65,92],['قیراط',6390,6441,-0.79,-51]];
var GT=['۱۷:۳۱','۱۷:۲۹','۱۷:۳۰','۱۷:۲۶','۱۷:۳۱','۱۷:۲۸','۱۷:۲۵','۱۷:۳۰','۱۷:۲۷','۱۷:۳۱','۱۷:۲۹','۱۷:۲۶'];
function pct(v){return (v<0?'‎−':'‎+')+fa(Math.abs(v).toFixed(2)).replace('.','٫')+'٪'}
function drawGold(){
  var b=document.getElementById('gBody'); if(!b) return;
  b.innerHTML=GF.map(function(f,i){
    var cls=f[3]<0?'dn':'up', ar=f[3]<0?'▼':'▲';
    return '<tr><td>صندوق '+f[0]+'</td><td>'+fa(grp(f[1]))+'</td>'+
      '<td class="'+cls+'">'+ar+' '+fa(Math.abs(f[3]).toFixed(2)).replace('.','٫')+'٪</td>'+
      '<td class="'+cls+'">'+fa(grp(Math.abs(f[4])))+'</td>'+
      '<td>'+LOCK+'</td><td>'+LOCK+'</td><td>'+LOCK+'</td><td>'+GT[i]+'</td></tr>'}).join('');
  var bs=GF.map(function(f){return (f[1]/f[2]-1)*100});
  var lo=0,hi=0; bs.forEach(function(v,i){if(v<bs[lo])lo=i;if(v>bs[hi])hi=i});
  var avg=bs.reduce(function(a,c){return a+c},0)/bs.length;
  var e=document.getElementById('gAvg'); e.textContent=pct(avg);
  e.style.color=avg<0?'var(--up-text)':'var(--down)';
  document.getElementById('gMax').textContent=pct(bs[hi]);
  document.getElementById('gMaxN').textContent=GF[hi][0];
  document.getElementById('gMin').textContent=pct(bs[lo]);
  document.getElementById('gMinN').textContent=GF[lo][0];
}
var SPOT=[['طلا گرم ۱۸ عیار',182257000,-0.14,-255000],['سکه امامی',1826000000,-1.42,-26000000],
 ['سکه بهار آزادی',1781000000,-1.07,-19000000],['نیم سکه',920000000,-0.85,-7900000],
 ['ربع سکه',540000000,-0.80,-4300000],['مظنه آبشده',789500000,-0.14,-1100000],
 ['گواهی سکه',1816000000,1.94,34500000],['گواهی شمش',23900550,-1.79,-435000]];
(function(){
  var b=document.getElementById('sBody'); if(!b) return;
  b.innerHTML=SPOT.map(function(r){
    var cls=r[2]<0?'dn':'up', ar=r[2]<0?'▼':'▲';
    return '<tr><td>'+r[0]+'</td><td>'+fa(grp(r[1]))+'</td>'+
      '<td class="'+cls+'">'+ar+' '+fa(Math.abs(r[2]).toFixed(2)).replace('.','٫')+'٪</td>'+
      '<td class="'+cls+'">'+fa(grp(Math.abs(r[3])))+'</td>'+
      '<td>'+LOCK+'</td><td>'+LOCK+'</td><td>'+LOCK+'</td></tr>'}).join('');
})();
(function(){
  var m=document.getElementById('tmap'); if(!m) return;
  var F=[['طلا',5,3],['کهربا',3,2],['گوهر',2,2],['زر',2,2],['عیار',2,1],['مثقال',2,1],
   ['آلتون',1,1],['ناب',1,1],['نفیس',1,1],['تابش',1,1],['زرفام',1,1],['قیراط',1,1],
   ['لطفی',1,1],['آبان',1,1],['کیان',1,1],['گنج',1,1]];
  var C=['#B91C1C','#EF4444','#94A3B8','#4ADE80','#15803D'];
  m.innerHTML=F.map(function(f){
    var r=(Math.random()*6-3), k=r<-1.5?0:(r<-0.4?1:(r<0.4?2:(r<1.5?3:4)));
    return '<div style="grid-column:span '+f[1]+';grid-row:span '+f[2]+';background:'+C[k]+'">'+
      f[0]+'<br><span style="font-size:10px;opacity:.9">'+pct(r)+'</span></div>'}).join('');
})();
(function(){
  var p=document.getElementById('navLine'); if(!p) return;
  var d='',y=90;
  for(var i=0;i<=30;i++){var x=34+i*12.4; y+=(Math.random()-0.5)*13; y=Math.max(22,Math.min(158,y));
    d+=(i?'L':'M')+x.toFixed(1)+' '+y.toFixed(1)+' '}
  p.setAttribute('d',d);
})();
var t0=new Date(); t0.setHours(17,31,4,0);
drawGold();
if(!(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches)){
  setInterval(function(){t0=new Date(t0.getTime()+1000);
    var c=document.getElementById('gClock'); if(c) c.textContent=
      fa(('0'+t0.getHours()).slice(-2)+':'+('0'+t0.getMinutes()).slice(-2)+':'+('0'+t0.getSeconds()).slice(-2))},1000);
  setInterval(function(){
    GF=GF.map(function(f){return [f[0],Math.round(f[1]*(1+(Math.random()-0.5)*0.003)),f[2],f[3],f[4]]});
    drawGold();},4500);
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
    <div><h2>دیدبان قراردادهای اختیار خرید</h2><p>سه ستون محاسباتی — حاشیه ریسک، سود دوره‌ای و نرخ معادل سالانه — با عضویت باز می‌شوند</p></div>
    <a class="lockcell" href="pricing.html" style="font-size:12.5px;padding:7px 14px">🔒 باز کردن همه ستون‌ها</a>
  </div>
  <div class="dwrap"><div class="tscroll">
    <table class="dt">
      <thead><tr><th>نماد</th><th>سهم پایه</th><th>آخرین</th><th>DTM</th><th>قیمت اعمال</th>
        <th>حاشیه ریسک</th><th>سود دوره‌ای</th><th>نرخ معادل سالانه</th></tr></thead>
      <tbody id="cBody"></tbody>
    </table>
  </div></div>
  <p style="font-size:12px;color:var(--slate-400);margin-top:10px">۱۲ قرارداد از ۳۶۸ قرارداد فعال در حال نمایش · فیلتر سفارشی، ستون محاسباتی و هشدار با عضویت</p>
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
        <tr><td>ضستا۳۰۰۸</td><td>۶۹۵</td><td>۱,۲۴۰</td><td>۸,۴۰۰</td><td>۱,۲۰۰</td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td></tr>
        <tr style="background:rgba(240,180,41,.06)"><td>ضستا۳۰۱۰</td><td>۵۰۳</td><td>۳,۸۱۰</td><td>۲۴,۶۰۰</td><td>۱,۴۰۰</td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td></tr>
        <tr><td>ضستا۳۰۱۲</td><td>۳۴۸</td><td>۲,۰۵۰</td><td>۱۵,۲۰۰</td><td>۱,۶۰۰</td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td></tr>
        <tr><td>ضستا۳۰۱۴</td><td>۲۲۱</td><td>۹۸۰</td><td>۹,۷۰۰</td><td>۱,۸۰۰</td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td></tr>
        <tr><td>ضستا۳۰۱۶</td><td>۱۳۴</td><td>۵۶۰</td><td>۶,۱۰۰</td><td>۲,۰۰۰</td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td><td><a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a></td></tr>
      </tbody>
    </table>
  </div></div>
  <p style="font-size:12px;color:var(--slate-400);margin-top:10px">در نسخه مهمان فقط زنجیره یک نماد نمایش داده می‌شود · ۴۲ نماد پایه با عضویت</p>
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

CC_JS = """
var LOCK='<a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a>';
var ROWS=[
 ['ضستا۳۰۱۰','شستا',503,15,1400],['ضشنا۶۰۴۹','شنا',1851,20,6000],
 ['ضخود۶۰۵۵','خودرو',1262,57,3000],['ضملی۳۰۵۸','ملی',454,43,1260],
 ['ضفولا۶۰۳۲','فولاد',1338,29,4500],['ضهرم۷۰۲۲','اهرم',588,26,2100],
 ['ضفزر۱۰۱۳','فزر',2283,71,7500],['ضاهرم۴۰۲۲','اهرم',412,36,1800],
 ['ضبمل۲۰۰۷','بمل',298,22,1150],['ضشپنا۵۰۳۱','شپنا',760,34,2900],
 ['ضتپکو۹۰۱۵','تپکو',195,18,880],['ضونفت۴۰۴۰','ونفت',630,49,2400]];
(function(){
  var b=document.getElementById('cBody'); if(!b) return;
  b.innerHTML=ROWS.map(function(r){
    return '<tr><td>'+r[0]+'</td><td>'+r[1]+'</td><td>'+fa(grp(r[2]))+'</td><td>'+fa(r[3])+'</td>'+
      '<td>'+fa(grp(r[4]))+'</td><td>'+LOCK+'</td><td>'+LOCK+'</td><td>'+LOCK+'</td></tr>'}).join('');
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
