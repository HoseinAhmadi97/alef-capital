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
      <div>آخرین روز معاملاتی: <b class="num" style="color:var(--ink-800)">۱۴۰۵/۰۶/۱۶</b></div>
      <div>آخرین به‌روزرسانی: <b class="num" id="mClock" style="color:var(--ink-800)">۱۷:۳۱:۰۴</b></div>
    </div>
  </div>
</div>
</section>

<!-- KPI -->
<section class="sec" style="padding-block:32px;background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <div class="kpirow">
    <div class="kc"><small>میانگین حباب صندوق‌ها</small><b class="num" id="kAvg">‎−۰٫۳۴٪</b><span class="d d-up" style="font-size:12px">نسبت به دیروز ▼ ۰٫۱۲</span></div>
    <div class="kc"><small>پرحباب‌ترین صندوق</small><b class="num" id="kMax" style="color:var(--down)">‎+۲٫۵۰٪</b><span style="font-size:12px;color:var(--slate-500)" id="kMaxN">کهربا</span></div>
    <div class="kc"><small>کم‌حباب‌ترین صندوق</small><b class="num" id="kMin" style="color:var(--up-text)">‎−۱٫۷۹٪</b><span style="font-size:12px;color:var(--slate-500)" id="kMinN">گوهر</span></div>
    <div class="kc"><small>ارزش معاملات صندوق‌های طلا</small><b class="num">۴٫۲ همت</b><span style="font-size:12px;color:var(--slate-500)">▲ ۸٫۳٪ نسبت به میانگین هفته</span></div>
  </div>
</div>
</section>

<!-- FUNDS TABLE -->
<section class="sec">
<div class="wrap">
  <h2 class="h2">جدول حباب صندوق‌های طلا</h2>
  <p class="lead">پنج ردیف اول برای مهمان باز است. جدول کامل ۳۰ صندوق با ثبت‌نام رایگان، و نسخه لحظه‌ای با پلن طلا.</p>
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
  <p class="lead">همان قیمت‌هایی که ارزش ذاتی هر صندوق از روی آن‌ها بازسازی می‌شود.</p>
  <div class="six six4">
    <div class="sx"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">طلای ۱۸ عیار</span><b class="num" style="font-size:21px;font-weight:800">۱۸۲,۲۵۷,۰۰۰</b><div class="d d-dn" style="margin-top:8px">▼ ۰٫۱۴٪</div></div>
    <div class="sx"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">مثقال طلا</span><b class="num" style="font-size:21px;font-weight:800">۷۸۹,۵۰۰,۰۰۰</b><div class="d d-dn" style="margin-top:8px">▼ ۰٫۱۴٪</div></div>
    <div class="sx"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">گواهی شمش</span><b class="num" style="font-size:21px;font-weight:800">۲۳,۹۰۰,۵۵۰</b><div class="d d-dn" style="margin-top:8px">▼ ۱٫۷۹٪</div></div>
    <div class="sx"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">گواهی سکه</span><b class="num" style="font-size:21px;font-weight:800">۱,۸۱۶,۰۰۰,۰۰۰</b><div class="d d-up" style="margin-top:8px">▲ ۱٫۹۴٪</div></div>
    <div class="sx"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">سکه امامی</span><b class="num" style="font-size:21px;font-weight:800">۱,۸۲۶,۰۰۰,۰۰۰</b><div class="d d-up" style="margin-top:8px">▲ ۲٫۵۰٪</div></div>
    <div class="sx"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">اونس جهانی طلا</span><b class="num" style="font-size:21px;font-weight:800">۴,۰۰۵</b><div class="d" style="margin-top:8px;background:var(--surface-3);color:var(--slate-600)">— ۰٫۰۰٪</div></div>
    <div class="sx"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">دلار</span><b class="num" style="font-size:21px;font-weight:800">۱۸۹,۰۰۰</b><div class="d" style="margin-top:8px;background:var(--surface-3);color:var(--slate-600)">— ۰٫۰۰٪</div></div>
    <div class="sx"><span style="font-size:13px;color:var(--slate-500);display:block;margin-bottom:6px">شاخص صندوق‌های طلا</span><b class="num" style="font-size:21px;font-weight:800">۲۳,۴۱۸</b><div class="d d-up" style="margin-top:8px">▲ ۰٫۶۲٪</div></div>
  </div>
</div>
</section>

<!-- CHARTS -->
<section class="sec">
<div class="wrap split" style="align-items:start">
  <div class="card">
    <h3 style="font-size:16px;margin-bottom:4px">حباب اسمی در برابر وزن سکه در صندوق</h3>
    <p style="font-size:12.5px;color:var(--slate-500);margin:0 0 16px">هر نقطه یک صندوق. نقاط زیر خط روند، نسبت به ترکیب دارایی‌شان ارزنده‌ترند.</p>
    <svg viewBox="0 0 420 260" style="width:100%;height:auto;display:block">
      <rect x="46" y="14" width="358" height="196" fill="var(--surface-2)" rx="8"/>
      <line x1="46" y1="112" x2="404" y2="112" stroke="var(--border-strong)"/>
      <line x1="46" y1="14" x2="46" y2="210" stroke="var(--border-strong)"/>
      <line x1="60" y1="150" x2="392" y2="70" stroke="#DC2626" stroke-width="2" stroke-dasharray="6 5" opacity=".75"/>
      <g id="scatter"></g>
      <text x="404" y="232" font-size="11" fill="#64748B" text-anchor="end">وزن سکه در صندوق ←</text>
      <text x="40" y="20" font-size="11" fill="#64748B" text-anchor="end">حباب</text>
      <text x="40" y="116" font-size="10" fill="#94A3B8" text-anchor="end">۰٪</text>
    </svg>
  </div>
  <div class="card">
    <h3 style="font-size:16px;margin-bottom:4px">روند حباب در طول روز</h3>
    <p style="font-size:12.5px;color:var(--slate-500);margin:0 0 16px">پنج صندوق پرگردش، از بازگشایی تا پایان معاملات.</p>
    <svg viewBox="0 0 420 260" style="width:100%;height:auto;display:block">
      <rect x="40" y="14" width="364" height="196" fill="var(--surface-2)" rx="8"/>
      <line x1="40" y1="112" x2="404" y2="112" stroke="var(--border-strong)" stroke-dasharray="3 3"/>
      <g id="lines" fill="none" stroke-width="2" stroke-linejoin="round"></g>
      <text x="40" y="232" font-size="11" fill="#64748B">۰۹:۰۰</text>
      <text x="404" y="232" font-size="11" fill="#64748B" text-anchor="end">۱۲:۳۰</text>
      <text x="34" y="116" font-size="10" fill="#94A3B8" text-anchor="end">۰٪</text>
    </svg>
    <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:12px;font-size:12px;color:var(--slate-600)">
      <span><i style="width:10px;height:10px;border-radius:3px;background:#B4790F;display:inline-block;margin-inline-end:5px"></i>طلا</span>
      <span><i style="width:10px;height:10px;border-radius:3px;background:#2E5FE0;display:inline-block;margin-inline-end:5px"></i>کهربا</span>
      <span><i style="width:10px;height:10px;border-radius:3px;background:#D9482B;display:inline-block;margin-inline-end:5px"></i>گوهر</span>
      <span><i style="width:10px;height:10px;border-radius:3px;background:#0E9CAD;display:inline-block;margin-inline-end:5px"></i>زر</span>
      <span><i style="width:10px;height:10px;border-radius:3px;background:#9333EA;display:inline-block;margin-inline-end:5px"></i>عیار</span>
    </div>
  </div>
</div>
</section>

<!-- UPGRADE -->
<section class="sec" style="padding-top:0">
<div class="wrap">
  <div class="ctaband">
    <h2>این جدول با تأخیر ۱۵ دقیقه است</h2>
    <p>نسخه لحظه‌ای، تاریخچه ۶ ماهه و هشدار عبور حباب از آستانه، در پلن طلا.</p>
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
var FUNDS=[['طلا',172900,172835],['کهربا',18420,18221],['گوهر',24160,24600],['زر',15630,15702],
 ['عیار',9840,9795],['مثقال',31250,31410],['آلتون',12480,12390],['ناب',8720,8801],
 ['نفیس',21340,21180],['تابش',7650,7712]];
var TIMES=['۱۷:۳۱','۱۷:۲۹','۱۷:۳۰','۱۷:۲۶','۱۷:۳۱','۱۷:۲۸','۱۷:۲۵','۱۷:۳۰','۱۷:۲۷','۱۷:۳۱'];
var VOLS=['۸۴۰ میلیارد','۶۱۲ میلیارد','۵۰۸ میلیارد','۴۳۹ میلیارد','۳۸۷ میلیارد','۳۱۲ میلیارد','۲۷۴ میلیارد','۲۱۰ میلیارد','۱۸۶ میلیارد','۱۴۹ میلیارد'];
function pct(v){return (v<0?'‎−':'‎+')+fa(Math.abs(v).toFixed(2)).replace('.','٫')+'٪'}
function drawFunds(){
  var b=document.getElementById('fundBody'); if(!b) return;
  b.innerHTML=FUNDS.map(function(f,i){
    var bub=(f[1]/f[2]-1)*100;
    var cls=bub<0?'up':(bub>0?'down':'neu');
    return '<tr'+(PAYWALL&&i>=5?' class="lock"':'')+' style="border-color:var(--border)">'+
      '<td style="border-color:var(--border)">صندوق '+f[0]+'</td>'+
      '<td style="border-color:var(--border)">'+fa(grp(f[1]))+'</td>'+
      '<td style="border-color:var(--border)">'+fa(grp(f[2]))+'</td>'+
      '<td style="border-color:var(--border)"><span class="chip '+cls+'">'+pct(bub)+'</span></td>'+
      '<td style="border-color:var(--border)">'+VOLS[i]+'</td>'+
      '<td style="border-color:var(--border)">'+TIMES[i]+'</td></tr>'}).join('');
  var bs=FUNDS.map(function(f){return (f[1]/f[2]-1)*100});
  var lo=0,hi=0; bs.forEach(function(v,i){if(v<bs[lo])lo=i;if(v>bs[hi])hi=i});
  var avg=bs.reduce(function(a,c){return a+c},0)/bs.length;
  document.getElementById('kAvg').textContent=pct(avg);
  document.getElementById('kAvg').style.color=avg<0?'var(--up-text)':'var(--down)';
  document.getElementById('kMax').textContent=pct(bs[hi]);
  document.getElementById('kMaxN').textContent=FUNDS[hi][0];
  document.getElementById('kMin').textContent=pct(bs[lo]);
  document.getElementById('kMinN').textContent=FUNDS[lo][0];
}
(function(){
  var g=document.getElementById('scatter'); if(!g) return; var s='';
  for(var i=0;i<28;i++){var w=Math.random(),x=60+w*332,y=150-w*80+(Math.random()-0.5)*46;
    var big=i===3;
    s+='<circle cx="'+x.toFixed(1)+'" cy="'+Math.max(24,Math.min(202,y)).toFixed(1)+'" r="'+(big?7:4)+
       '" fill="'+(big?'#0891B2':'#0F172A')+'" opacity="'+(big?'.95':'.55')+'"/>'}
  g.innerHTML=s;
})();
(function(){
  var g=document.getElementById('lines'); if(!g) return;
  var C=['#B4790F','#2E5FE0','#D9482B','#0E9CAD','#9333EA'],s='';
  for(var k=0;k<5;k++){var d='',y=112+(k-2)*16;
    for(var i=0;i<=28;i++){var x=40+i*13; y+=(Math.random()-0.5)*11;
      y=Math.max(30,Math.min(196,y)); d+=(i?'L':'M')+x+' '+y.toFixed(1)+' '}
    s+='<path d="'+d+'" stroke="'+C[k]+'" opacity=".85"/>'}
  g.innerHTML=s;
})();
var t0=new Date(); t0.setHours(17,31,4,0);
drawFunds();
if(!(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches)){
  setInterval(function(){t0=new Date(t0.getTime()+1000);
    var c=document.getElementById('mClock'); if(c) c.textContent=
      fa(('0'+t0.getHours()).slice(-2)+':'+('0'+t0.getMinutes()).slice(-2)+':'+('0'+t0.getSeconds()).slice(-2))},1000);
  setInterval(function(){
    FUNDS=FUNDS.map(function(f){return [f[0], Math.round(f[1]*(1+(Math.random()-0.5)*0.003)), f[2]]});
    drawFunds();},4000);
}
"""

HTML = paywall.apply(HTML)
JS = paywall.js_flag() + JS
