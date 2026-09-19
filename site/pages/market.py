# -*- coding: utf-8 -*-
"""Market pulse — free live gold/fund table, no sign-up required."""
import paywall

HTML = """
<section class="phero" style="padding-block:clamp(36px,4vw,56px)">
<div class="wrap">
  <div class="crumb"><a href="index.html">خانه</a> ← نبض بازار</div>
  <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap">
    <div>
      <span class="eyebrow"><span class="dot"></span>رایگان — بدون ثبت‌نام</span>
      <h1 style="font-size:clamp(28px,3.6vw,44px)">نبض بازار طلا</h1>
      <p class="lead">حباب لحظه‌ای صندوق‌های طلای بورس تهران، قیمت دارایی‌های پایه و روند درون‌روزی — همه در یک صفحه.</p>
    </div>
    <div style="text-align:left;font-size:13px;color:var(--slate-500);line-height:2">
      <div>آخرین روز معاملاتی: <b class="num gdate" style="color:var(--ink-800)">—</b></div>
      <div>آخرین به‌روزرسانی: <b class="num gupdated" style="color:var(--ink-800)">—</b></div>
      <div><b data-session="funds" style="color:var(--ink-800)">—</b></div>
    </div>
  </div>
</div>
</section>

<!-- KPI -->
<section class="sec" style="padding-block:32px;background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <div class="kpirow">
    <div class="kc"><small>میانگین حباب صندوق‌ها</small><b class="num" id="kAvg">—</b><span style="font-size:12px;color:var(--slate-500)"><span class="gcount">—</span> صندوق تحت پایش</span></div>
    <div class="kc"><small>پرحباب‌ترین صندوق</small><b class="num" id="kMax">—</b><span style="font-size:12px;color:var(--slate-500)" id="kMaxN">—</span></div>
    <div class="kc"><small>کم‌حباب‌ترین صندوق</small><b class="num" id="kMin">—</b><span style="font-size:12px;color:var(--slate-500)" id="kMinN">—</span></div>
    <div class="kc"><small>ارزش معاملات صندوق‌های طلا</small><b class="num" id="kVal">—</b><span style="font-size:12px;color:var(--slate-500)">مجموع امروز</span></div>
  </div>
</div>
</section>

<!-- FUNDS TABLE -->
<section class="sec">
<div class="wrap">
  <h2 class="h2">جدول حباب صندوق‌های طلا</h2>
  <p class="lead">همه <span class="gcount">—</span> صندوق طلای بورس، به ترتیب ارزش معاملات امروز. قیمت و NAV به تومان.</p>
  <div class="panel" style="margin-top:24px;background:var(--surface);border-color:var(--border)">
    <div class="tscroll">
    <table style="color:var(--ink-800)">
      <thead><tr>
        <th style="background:var(--surface-3);color:var(--slate-600)">نماد</th>
        <th style="background:var(--surface-3);color:var(--slate-600)">آخرین قیمت</th>
        <th style="background:var(--surface-3);color:var(--slate-600)">ارزش ذاتی (NAV)</th>
        <th style="background:var(--surface-3);color:var(--slate-600)">حباب</th>
        <th style="background:var(--surface-3);color:var(--slate-600)">ارزش معاملات</th>
        <th style="background:var(--surface-3);color:var(--slate-600)">زمان</th>
      </tr></thead>
      <tbody id="fundBody" style="border-color:var(--border)"></tbody>
    </table>
    </div>
@@IFLOCK@@    <div class="lockmsg" style="background:rgba(240,180,41,.08);color:var(--ink-700);border-color:var(--border)">
      🔒 <b style="color:var(--gold-700)">۲۵ صندوق دیگر</b> با ثبت‌نام رایگان — داده لحظه‌ای، تاریخچه و هشدار با <a href="pricing.html">پلن طلا</a>.
    </div>@@END@@
  </div>
</div>
</section>

<!-- BASE PRICES -->
<section class="sec" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <h2 class="h2">قیمت دارایی‌های پایه</h2>
  <p class="lead">همان قیمت‌هایی که ارزش ذاتی هر صندوق از روی آن‌ها بازسازی می‌شود. همه قیمت‌ها به تومان، انس جهانی به دلار.</p>
  <div class="six six4" id="basePrices">
    <div class="sx" data-sym="geram18"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">طلای ۱۸ عیار</span><b class="num" style="font-size:21px;font-weight:800">—</b><div class="d" style="margin-top:8px">—</div></div>
    <div class="sx" data-sym="mesghal"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">مظنه آبشده (مثقال)</span><b class="num" style="font-size:21px;font-weight:800">—</b><div class="d" style="margin-top:8px">—</div></div>
    <div class="sx" data-sym="govahi_shemsh"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">گواهی شمش</span><b class="num" style="font-size:21px;font-weight:800">—</b><div class="d" style="margin-top:8px">—</div></div>
    <div class="sx" data-sym="govahi_sekke"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">گواهی سکه</span><b class="num" style="font-size:21px;font-weight:800">—</b><div class="d" style="margin-top:8px">—</div></div>
    <div class="sx" data-sym="sekee"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">سکه امامی</span><b class="num" style="font-size:21px;font-weight:800">—</b><div class="d" style="margin-top:8px">—</div></div>
    <div class="sx" data-sym="ons"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">اونس جهانی طلا</span><b class="num" style="font-size:21px;font-weight:800">—</b><div class="d" style="margin-top:8px">—</div></div>
    <div class="sx" data-sym="dollar"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">دلار</span><b class="num" style="font-size:21px;font-weight:800">—</b><div class="d" style="margin-top:8px">—</div></div>
    <div class="sx" data-sym="funds"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">میانگین تغییر صندوق‌های طلا</span><b class="num" style="font-size:21px;font-weight:800">—</b><div class="d" style="margin-top:8px">امروز</div></div>
  </div>
</div>
</section>

<!-- CHARTS -->
<section class="sec">
<div class="wrap split" style="align-items:start">
  <div class="card">
    <h3 style="font-size:16px;margin-bottom:4px">حباب و وزن گواهی سکه</h3>
    <p style="font-size:12.5px;color:var(--slate-500);margin:0 0 12px">هر دایره یک صندوق. صندوق‌های زیر خط روند، نسبت به ترکیب دارایی‌شان ارزنده‌ترند.</p>
    <div class="bmix" data-bmix></div>
  </div>
  <div class="card">
    <h3 style="font-size:16px;margin-bottom:4px">روند حباب در طول روز</h3>
    <p style="font-size:12.5px;color:var(--slate-500);margin:0 0 16px">پنج صندوق پرگردش، از بازگشایی تا پایان معاملات.</p>
    <div class="lockpanel" style="min-height:220px;padding:30px 20px">
      <div class="ic">📈</div>
      <h3>به‌زودی</h3>
      <p>نمودار درون‌روزی حباب به تاریخچه قیمت صندوق‌ها نیاز دارد که در حال آماده‌سازی است. حباب لحظه‌ای همه صندوق‌ها در جدول بالا در دسترس است.</p>
    </div>
  </div>
</div>
</section>

<!-- UPGRADE -->
<section class="sec" style="padding-top:0">
<div class="wrap">
  <div class="ctaband">
    <h2>این جدول زنده است و هر چند ثانیه به‌روز می‌شود</h2>
    <p>نقشه بازار، روند NAV همه صندوق‌ها و ترکیب دارایی هر صندوق، در داشبورد طلا.</p>
    <a class="btn btn-gold" href="dashboard-gold.html"><ico>🪙</ico>داشبورد طلا</a>
    <a class="btn btn-s" href="pricing.html" style="color:#DBE6FE;border-color:#334155;margin-inline-start:8px">مشاهده پلن‌ها</a>
  </div>
</div>
</section>

<!-- SEO PROSE -->
<section class="prose sec" style="background:var(--surface-2);border-top:1px solid var(--border)">
<div class="wrap" style="max-width:820px">
  <h2 class="h2">حباب صندوق طلا چیست و چطور محاسبه می‌شود؟</h2>
  <p style="margin-top:14px;color:var(--slate-600);font-size:15px;line-height:2.1">حباب صندوق طلا، اختلاف بین قیمت معاملاتی هر واحد صندوق و ارزش خالص دارایی (NAV) همان واحد است. وقتی قیمت بازار بالاتر از ارزش ذاتی باشد، صندوق «حباب مثبت» دارد؛ و وقتی پایین‌تر باشد، «حباب منفی». برای خریدار، حباب منفی یعنی خرید همان مقدار طلا با قیمتی کمتر از ارزش واقعی‌اش.</p>
  <h3 style="font-size:18px;margin:26px 0 8px">چرا حباب صندوق‌ها با هم فرق دارد؟</h3>
  <p style="margin:0;color:var(--slate-600);font-size:15px;line-height:2.1">دارایی پایه همه صندوق‌های طلای بورس تهران تقریباً یکسان است — گواهی سپرده سکه و شمش طلا — اما نسبت این دو در هر صندوق متفاوت است. صندوقی که سهم بیشتری از سکه دارد، بیشتر تحت تأثیر حباب سکه قرار می‌گیرد. به همین دلیل مقایسه حباب دو صندوق بدون در نظر گرفتن ترکیب دارایی‌شان گمراه‌کننده است.</p>
  <h3 style="font-size:18px;margin:26px 0 8px">این اختلاف چطور به فرصت تبدیل می‌شود؟</h3>
  <p style="margin:0;color:var(--slate-600);font-size:15px;line-height:2.1">چون دارایی پایه یکسان است، خروج از صندوقی که حباب بالایی دارد و ورود به صندوقی با حباب کمتر، مقدار طلای در اختیار سرمایه‌گذار را افزایش می‌دهد — بدون اینکه از بازار طلا خارج شود یا ریسک جدیدی به پرتفو اضافه کند. تکرار این جابه‌جایی در طول سال، همان چیزی است که <a href="product-gold.html">داشبورد آربیتراژ</a> برای شناسایی‌اش ساخته شده. برای آشنایی بیشتر با مفاهیم، <a href="wiki.html">دانشنامه</a> را ببینید.</p>
</div>
</section>
"""

JS = """
/* every number below comes from the gold snapshot (site/gold-data.js) */
var TD=' style="border-color:var(--border)"';

/* KPIs */
onGold(function(g){
  var s=g.summary, a=gText('kAvg',gPct(s.avg_bubble));
  if(a) a.style.color=gColor(s.avg_bubble);
  if(s.max_bubble){gText('kMax',gPct(s.max_bubble.bubble)).style.color=gColor(s.max_bubble.bubble); gText('kMaxN',s.max_bubble.symbol)}
  if(s.min_bubble){gText('kMin',gPct(s.min_bubble.bubble)).style.color=gColor(s.min_bubble.bubble); gText('kMinN',s.min_bubble.symbol)}
  gText('kVal',gHemat(s.total_value));
});

/* funds table — every fund, most traded first */
onGold(function(g){
  var b=document.getElementById('fundBody'); if(!b) return;
  var rows=g.funds.slice().sort(function(x,y){return (y.value||0)-(x.value||0)});
  b.innerHTML=rows.map(function(f,i){
    var cls=gTone(f.nominal_bubble,'up','down','neu');
    return '<tr'+(PAYWALL&&i>=5?' class="lock"':'')+TD+'>'+
      '<td'+TD+'><b>'+f.symbol+'</b></td>'+
      '<td'+TD+'>'+gNum(gToman(f.last_trade))+'</td>'+
      '<td'+TD+'>'+gNum(gToman(f.nav))+'</td>'+
      '<td'+TD+'><span class="chip '+cls+'">'+gPct(f.nominal_bubble)+'</span></td>'+
      '<td'+TD+'>'+gBillion(f.value)+'</td>'+
      '<td'+TD+'>'+gTime(f.trade_time)+'</td></tr>'}).join('');
});

/* base prices */
onGold(function(g){
  document.querySelectorAll('#basePrices [data-sym]').forEach(function(box){
    var k=box.getAttribute('data-sym'), val=box.querySelector('b'), chg=box.querySelector('.d');
    var price, f;
    if(k==='funds'){price=null; f=g.summary.avg_change_pct}
    else{var r=g.m[k]; price=goldShown(r); f=r?r.change_pct:null}
    if(k==='funds'){val.textContent=gPct(f); val.style.color=gColor(f)}
    else{val.textContent=gNum(price); chg.textContent=gArrow(f)}
    chg.className='d '+gTone(f,'d-up','d-dn');
  });
});

/* bubble vs coin weight: <div data-bmix> renders itself (site/gold-data.js) */
"""

HTML = paywall.apply(HTML)
JS = paywall.js_flag() + JS
