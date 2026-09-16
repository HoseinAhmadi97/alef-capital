# -*- coding: utf-8 -*-
"""Gold-fund arbitrage dashboard — product introduction page."""
import paywall

HTML = """
<!-- HERO -->
<section class="phero">
<div class="wrap">
  <div class="crumb"><a href="index.html">خانه</a> ← <a href="index.html#products">محصولات</a> ← آربیتراژ صندوق طلا</div>
  <div class="hgrid">
    <div>
      <span class="eyebrow"><span class="dot"></span>محصول ۱ — داشبورد اشتراکی</span>
      <h1>حباب صندوق‌های طلا را<br><span class="grad">قبل از بقیه ببینید</span></h1>
      <p class="lead">قیمت هر صندوق طلا با ارزش واقعی‌اش فاصله دارد. این فاصله لحظه‌به‌لحظه عوض می‌شود و با چشم قابل ردیابی نیست. داشبورد آربیتراژ، حباب همه صندوق‌های طلای بورس تهران را هم‌زمان محاسبه می‌کند و نشان می‌دهد کدام‌ها ارزنده‌ترند.</p>
      <div class="pcta">
        <a class="btn btn-gold" href="dashboard-gold.html"><ico>🟡</ico>ورود به داشبورد طلا</a>
        <a class="btn btn-s" href="#sample">پیش‌نمایش داشبورد</a>
      </div>
    </div>
    <div class="card">
      <div class="lch"><span class="lbl">پراکندگی حباب امروز</span><span class="live"><i></i>زنده</span></div>
      <div class="lcv"><span class="big num" id="pAvg">—</span><span class="lcu">میانگین <span class="gcount">—</span> صندوق</span></div>
      <div class="dist" id="pDist"></div>
      <div class="lcf">
        <span>کم‌حباب‌ترین <b id="pMin">—</b></span>
        <span>پرحباب‌ترین <b id="pMax">—</b></span>
      </div>
      <div class="lcbar"><span>آخرین به‌روزرسانی <b class="gupdated">—</b></span></div>
    </div>
  </div>
</div>
</section>

<!-- PROBLEM -->
<section class="sec" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap split">
  <div>
    <span class="eyebrow">مسئله</span>
    <h2 class="h2">قیمت صندوق، برابر ارزش واقعی‌اش نیست</h2>
    <p class="lead">قیمت هر صندوق طلا در بورس، به‌جای تبعیت دقیق از ارزش خالص دارایی (NAV)، بیشتر تحت تأثیر عرضه و تقاضای لحظه‌ای معامله‌گران قرار می‌گیرد. همین باعث می‌شود برخی صندوق‌ها بالاتر از ارزش واقعی‌شان معامله شوند — «حباب بالا» — و برخی نزدیک‌تر یا پایین‌تر از آن.</p>
    <p class="lead" style="margin-top:16px">چون دارایی پایه همه این صندوق‌ها یکسان است (گواهی سپرده سکه و شمش طلا)، این اختلاف قیمت یک <b>فرصت آربیتراژ</b> می‌سازد: خروج از صندوق حباب‌دار و ورود به صندوق کم‌حباب، بدون خروج از بازار طلا و بدون افزودن ریسک به پرتفو.</p>
  </div>
  <div class="card">
    <h3 style="font-size:15px;margin-bottom:4px">حباب اسمی در برابر وزن سکه در صندوق</h3>
    <p style="font-size:12.5px;color:var(--slate-500);margin:0 0 14px">هر نقطه یک صندوق. صندوق‌های زیر خط روند، نسبت به ترکیب دارایی‌شان ارزنده‌ترند.</p>
    <svg viewBox="0 0 420 260" style="width:100%;height:auto;display:block">
      <rect x="46" y="14" width="358" height="196" fill="var(--surface-2)" rx="8"/>
      <line x1="46" y1="112" x2="404" y2="112" stroke="var(--border-strong)" stroke-width="1"/>
      <line x1="46" y1="14" x2="46" y2="210" stroke="var(--border-strong)" stroke-width="1"/>
      <line id="scatterFit" x1="60" y1="112" x2="392" y2="112" stroke="#DC2626" stroke-width="2" stroke-dasharray="6 5" opacity=".75" style="display:none"/>
      <g id="scatter" style="color:var(--ink-900)"></g>
      <text x="404" y="230" font-size="11" fill="#64748B" text-anchor="end">وزن سکه در صندوق ←</text>
      <text x="40" y="20" font-size="10" fill="#94A3B8" text-anchor="end" id="scatterTop"></text>
      <text x="40" y="116" font-size="10" fill="#94A3B8" text-anchor="end">۰٪</text>
      <text x="40" y="208" font-size="10" fill="#94A3B8" text-anchor="end" id="scatterBottom"></text>
    </svg>
  </div>
</div>
</section>

<!-- 4 CAPABILITIES -->
<section class="sec">
<div class="wrap">
  <span class="eyebrow">قابلیت‌ها</span>
  <h2 class="h2">چهار لایه داده، در یک صفحه</h2>
  <p class="lead">هر لایه به‌تنهایی در دسترس است؛ ارزش واقعی وقتی ساخته می‌شود که هر چهار را کنار هم ببینید.</p>
  <div class="feat4">
    <div class="fx">
      <b>لایه ۰۱</b>
      <h3>پایش قیمت و شاخص‌های کلیدی</h3>
      <p>قیمت لحظه‌ای همه دارایی‌های پایه، در یک تابلو.</p>
      <ul>
        <li>طلای ۱۸ عیار، مثقال، گواهی شمش و گواهی سکه</li>
        <li>اونس جهانی طلا و نرخ دلار</li>
        <li>شاخص لحظه‌ای صندوق‌های طلا و روند درون‌روزی آن</li>
      </ul>
    </div>
    <div class="fx">
      <b>لایه ۰۲</b>
      <h3>محاسبه و پایش حباب</h3>
      <p>فاصله قیمت هر صندوق تا ارزش خالص دارایی‌اش، لحظه‌ای.</p>
      <ul>
        <li>حباب هر صندوق نسبت به NAV، به‌صورت لحظه‌ای</li>
        <li>روند حباب در طول روز، قابل مقایسه بین صندوق‌ها</li>
        <li>هشدار وقتی حباب از آستانه دلخواه شما عبور کند</li>
      </ul>
    </div>
    <div class="fx">
      <b>لایه ۰۳</b>
      <h3>مانیتورینگ روند NAV</h3>
      <p>سه نمای مکمل از ارزش واقعی، به تفکیک هر صندوق.</p>
      <ul>
        <li><span dir="ltr">Latent NAV</span> — ارزش نهفته بر پایه آخرین معاملات</li>
        <li><span dir="ltr">Pure NAV</span> — ارزش خالص بدون اثر نقدشوندگی</li>
        <li>نسبت <span dir="ltr">Latent/Pure</span> برای مقایسه دقیق‌تر صندوق‌ها</li>
      </ul>
    </div>
    <div class="fx">
      <b>لایه ۰۴</b>
      <h3>تحلیل ترکیب دارایی</h3>
      <p>معلوم می‌کند حباب هر صندوق چقدر توجیه‌پذیر است.</p>
      <ul>
        <li>سهم سکه، شمش و سایر ابزارها در هر صندوق</li>
        <li>میزان همبستگی صندوق با قیمت سکه و دلار</li>
        <li>شناسایی صندوق ارزنده نسبت به کیفیت دارایی‌اش</li>
      </ul>
    </div>
  </div>
</div>
</section>

<!-- SAMPLE DATA -->
<section class="dark sec" id="sample">
<div class="wrap">
  <span class="eyebrow" style="background:rgba(240,180,41,.14)">پیش‌نمایش داشبورد</span>
  <h2 class="h2">این چیزی است که هر روز می‌بینید</h2>
  <p class="lead">هفت صندوق پرمعامله امروز، زنده. جدول کامل <span class="gcount">—</span> صندوق، تاریخچه و هشدار در داشبورد طلا.</p>
  <div class="panel" style="margin-top:26px">
    <div class="pbar"><i></i><i></i><i></i></div>
    <div class="tscroll">
    <table>
      <thead><tr><th>نماد</th><th>آخرین قیمت</th><th>ارزش ذاتی (NAV)</th><th>حباب</th><th>دلار محاسباتی</th><th>زمان</th></tr></thead>
      <tbody id="pSample">
        <tr><td colspan="6">در حال دریافت داده…</td></tr>
      </tbody>
    </table>
    </div>
@@IFLOCK@@    <div class="lockmsg">🔒 جدول کامل همه صندوق‌ها، تاریخچه و هشدار، با پلن طلا.</div>@@END@@
  </div>
</div>
</section>

<!-- TWO ADVANTAGES -->
<section class="sec">
<div class="wrap">
  <span class="eyebrow">نتیجه</span>
  <h2 class="h2">دو مزیتی که از این داده بیرون می‌آید</h2>
  <div class="adv">
    <div class="advc">
      <span class="big num">‎۵ تا ۱۰٪</span>
      <h3>مزیت اول — کسب سود طلایی</h3>
      <p>از محل جابه‌جایی بین صندوق‌ها، امکان کسب سود سالانه معادل ۵ تا ۱۰ درصد از ارزش طلای موجود در پرتفو وجود دارد — به‌صورت <b>طلای اضافه</b>، نه ریال.</p>
      <p style="font-size:13px;color:var(--slate-500)">بدون خروج از بازار طلا و بدون افزودن ریسک جدید به پرتفو.</p>
    </div>
    <div class="advc" style="border-inline-start-color:var(--info)">
      <span class="big num" style="color:var(--info)">‎۳۰ تا ۴۰٪</span>
      <h3>مزیت دوم — ایجاد اعتبار از گردش پرتفوی</h3>
      <p>هر جابه‌جایی، گردش معاملاتی در کارگزاری ثبت می‌کند. کارگزاری‌ها بر اساس این گردش، اعتبار با نرخ ۳۰ تا ۴۰ درصد در اختیار مشتری می‌گذارند — نرخی که در برابر تورم بالای ۶۰ درصد، مقرون‌به‌صرفه است.</p>
      <p style="font-size:13px;color:var(--slate-500)">این اعتبار داخل کارگزاری برای خرید طلا، خرید سهام یا ورود به استراتژی کاوردکال قابل استفاده است.</p>
    </div>
  </div>
  <div class="card soft" style="margin-top:20px;font-size:14px;color:var(--slate-600)">
    <b style="color:var(--ink-800)">مرز محصول:</b> آنچه با اشتراک دریافت می‌کنید، <b>داده و داشبورد</b> است — تصمیم و اجرای معامله با شماست.
    اگر اجرای خودکار روی حساب کارگزاری‌تان را می‌خواهید، آن یک خدمت جداگانه است: <a href="services.html">مدیریت پرتفوی ←</a>
  </div>
</div>
</section>

<!-- WHY GOLD FUNDS -->
<section class="sec" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <span class="eyebrow">پیش‌زمینه</span>
  <h2 class="h2">همان طلا، با ساختاری هوشمندتر</h2>
  <p class="lead">چرا صندوق‌های طلای بورس، نسبت به روش‌های سنتی نگهداری و معامله طلا مزیت دارند.</p>
  <div class="six">
    <div class="sx"><span>🏦</span><h3>امنیت بالا در نگهداری</h3><p>دارایی در مخازن بانک مرکزی و بورس کالا نگهداری می‌شود؛ احتمال سرقت عملاً منتفی است.</p></div>
    <div class="sx"><span>🔍</span><h3>شفافیت و نظارت</h3><p>تحت نظارت دقیق نهادهای ناظر بازار سرمایه؛ شفافیت به‌مراتب بالاتر از پلتفرم‌های آنلاین خرید طلا.</p></div>
    <div class="sx"><span>🧾</span><h3>معافیت مالیاتی</h3><p>خرید و فروش واحدهای صندوق طلا از مالیات معاف است.</p></div>
    <div class="sx"><span>💸</span><h3>کارمزد پایین</h3><p>کارمزد معامله زیر ۰٫۲ درصد، در حالی که این رقم در بازار فیزیکی طلا تا ۲ درصد می‌رسد.</p></div>
    <div class="sx"><span>⚡</span><h3>نقدشوندگی بالا</h3><p>خرید و فروش آنی و آسان، حتی با مبالغ کم — گزینه‌ای مناسب برای تأمین نقدینگی سریع.</p></div>
    <div class="sx"><span>🛡️</span><h3>حذف ریسک طلای تقلبی</h3><p>دارایی پشتوانه در نهادهای رسمی نگهداری و راستی‌آزمایی می‌شود.</p></div>
  </div>
</div>
</section>

<!-- FAQ -->
<section class="sec">
<div class="wrap">
  <h2 class="h2" style="text-align:center">سوالات متداول این محصول</h2>
  <div class="faq">
    <details open><summary>حباب صندوق دقیقاً چطور محاسبه می‌شود؟</summary><p>حباب، نسبت اختلاف قیمت معاملاتی هر واحد صندوق به ارزش خالص دارایی (NAV) همان واحد است. ما NAV را از ترکیب دارایی اعلامی صندوق و قیمت لحظه‌ای دارایی‌های پایه (گواهی سپرده سکه و شمش) بازسازی می‌کنیم، نه از NAV تأخیری منتشرشده.</p></details>
    <details><summary>تفاوت <span dir="ltr">Latent NAV</span> و <span dir="ltr">Pure NAV</span> چیست؟</summary><p><span dir="ltr">Pure NAV</span> ارزش خالص دارایی بر پایه قیمت دارایی‌های پایه است. <span dir="ltr">Latent NAV</span> اثر نقدشوندگی و آخرین معاملات واقعی را هم لحاظ می‌کند. نسبت این دو نشان می‌دهد قیمت‌گذاری بازار روی یک صندوق چقدر با ارزش بنیادی‌اش فاصله دارد.</p></details>
    <details><summary>داده با چه تأخیری به‌روز می‌شود؟</summary><p>داده برای همه کاربران لحظه‌ای است: قیمت‌ها و حباب صندوق‌ها هر چند ثانیه به‌روز می‌شوند و مهر زمان آخرین به‌روزرسانی روی صفحه نمایش داده می‌شود.</p></details>
    <details><summary>آیا داشبورد به‌جای من معامله می‌کند؟</summary><p>خیر. این محصول یک ابزار داده و تحلیل است؛ تصمیم و اجرای معامله با شماست. اجرای خودکار روی حساب کارگزاری، خدمت جداگانه‌ای است که در صفحه مدیریت پرتفوی توضیح داده شده.</p></details>
    <details><summary>برای استفاده باید حساب کارگزاری خاصی داشته باشم؟</summary><p>خیر. داشبورد مستقل از کارگزاری شما کار می‌کند و فقط داده بازار را نمایش می‌دهد.</p></details>
  </div>
</div>
</section>

<!-- CTA -->
<section class="sec" style="padding-top:0">
<div class="wrap">
  <div class="ctaband">
    <h2>همین حالا داشبورد را ببینید</h2>
    <p>نسخه مهمان بدون ثبت‌نام باز است؛ ستون‌های ارزش ذاتی و حباب با عضویت رایگان باز می‌شوند.</p>
    <a class="btn btn-gold" href="dashboard-gold.html"><ico>🟡</ico>ورود به داشبورد طلا</a>
    <a class="btn btn-s" href="pricing.html" style="color:#DBE6FE;border-color:#334155;margin-inline-start:8px">مقایسه پلن‌ها</a>
  </div>
</div>
</section>

<div class="riskbar"><div class="wrap">
  ارقام بازده ارائه‌شده، بازده تاریخی استراتژی آربیتراژ در صورت اجراست و تضمینی برای بازده آینده نیست. اطلاعات این صفحه صرفاً جنبه تحلیلی دارد و توصیه به خرید یا فروش هیچ اوراق بهاداری محسوب نمی‌شود.
</div></div>
"""

JS = """
/* hero card — bubble of every fund, from the gold snapshot (site/gold-data.js) */
onGold(function(g){
  var fs=g.withBubble, el=document.getElementById('pDist');
  if(el){
    var b=fs.map(function(f){return f.nominal_bubble*100});
    var mx=Math.max(0.5,Math.max.apply(null,b)), mn=Math.min(-0.5,Math.min.apply(null,b));
    el.innerHTML=fs.map(function(f,i){
      var v=b[i], h=Math.max(8,Math.round((v-mn)/(mx-mn)*100));
      var c=gBarColor(f.nominal_bubble,Math.abs(v)>1);
      return '<span title="'+f.symbol+' '+gPct(f.nominal_bubble)+'" style="height:'+h+'%;background:'+c+'"></span>'}).join('');
  }
  var s=g.summary, a=gText('pAvg',gPct(s.avg_bubble));
  if(a) a.style.color=gColor(s.avg_bubble);
  if(s.min_bubble) gText('pMin',s.min_bubble.symbol+' '+gPct(s.min_bubble.bubble));
  if(s.max_bubble) gText('pMax',s.max_bubble.symbol+' '+gPct(s.max_bubble.bubble));
});

/* bubble vs coin weight */
onGold(function(g){
  goldScatter(g,{g:'scatter',line:'scatterFit',top:'scatterTop',bottom:'scatterBottom',x0:60,x1:392,y0:112,h:90});
});

/* preview table — the seven most traded funds today */
onGold(function(g){
  var b=document.getElementById('pSample'); if(!b) return;
  var usd=g.m.dollar?g.m.dollar.price:null;
  var rows=g.funds.filter(function(f){return f.nominal_bubble!=null})
    .sort(function(x,y){return (y.value||0)-(x.value||0)}).slice(0,7);
  b.innerHTML=rows.map(function(f){
    var cls=gTone(f.nominal_bubble,'up','down','neu');
    return '<tr><td>صندوق '+f.symbol+'</td><td>'+gNum(f.last_trade)+'</td><td>'+gNum(f.nav_live)+'</td>'+
      '<td><span class="chip '+cls+'">'+gPct(f.nominal_bubble)+'</span></td>'+
      '<td>'+(usd?gNum(usd*f.last_trade/f.nav_live):'—')+'</td><td>'+gTime(f.trade_time)+'</td></tr>'}).join('');
});
"""

HTML = paywall.apply(HTML)
