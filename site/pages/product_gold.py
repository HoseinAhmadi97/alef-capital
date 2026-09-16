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
      </div>
    </div>
    <div class="card">
      <div class="lch"><span class="lbl">پراکندگی حباب امروز</span><span class="live" data-session="funds"><i></i><span>زنده</span></span></div>
      <div class="lcv"><span class="big num" id="pAvg">—</span><span class="lcu">میانگین <span class="gcount">—</span> صندوق</span></div>
      <!-- bubble spectrum: every fund is a dot on one price-vs-NAV axis -->
      <div class="bspec">
        <svg id="bSpec" viewBox="0 0 300 92" role="img" aria-label="پراکندگی حباب صندوق‌های طلا نسبت به NAV">
          <defs>
            <linearGradient id="bTrack" x1="0" x2="1" y1="0" y2="0">
              <stop offset="0%" stop-color="rgba(220,38,38,.55)"/>
              <stop offset="50%" stop-color="rgba(148,163,184,.35)"/>
              <stop offset="100%" stop-color="rgba(22,163,74,.55)"/>
            </linearGradient>
          </defs>
          <rect id="bTrackRect" x="8" y="44" width="284" height="4" rx="2" fill="url(#bTrack)"/>
          <g id="bZero"></g>
          <g id="bDots"></g>
          <g id="bAvgMark"></g>
          <g id="bAxis" font-size="9" fill="var(--slate-400)"></g>
        </svg>
        <div class="btip" id="bTip" hidden></div>
      </div>
      <div class="bsplit">
        <span class="neg"><b id="bBelow">—</b> زیر NAV</span>
        <div class="bsplit-bar" aria-hidden="true"><i id="bBelowBar"></i><i id="bAboveBar"></i></div>
        <span class="pos"><b id="bAbove">—</b> بالای NAV</span>
      </div>
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
    <h3 style="font-size:16px;margin-bottom:4px">حباب اسمی در برابر وزن سکه در صندوق</h3>
    <p style="font-size:12.5px;color:var(--slate-500);margin:0 0 12px">هر دایره یک صندوق. صندوق‌های زیر خط روند، نسبت به ترکیب دارایی‌شان ارزنده‌ترند.</p>
    <div class="bmix" data-bmix></div>
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
        <li>طلای ۱۸ عیار، مظنه آبشده، گواهی شمش و گواهی سکه</li>
        <li>انس جهانی طلا و نرخ دلار، همه به تومان</li>
        <li>نقشه بازار صندوق‌ها بر اساس ارزش معاملات و بازدهی روز</li>
      </ul>
    </div>
    <div class="fx">
      <b>لایه ۰۲</b>
      <h3>محاسبه و پایش حباب</h3>
      <p>فاصله قیمت هر صندوق تا ارزش خالص دارایی‌اش، لحظه‌ای.</p>
      <ul>
        <li>حباب هر صندوق نسبت به NAV، به‌صورت لحظه‌ای</li>
        <li>کم‌حباب‌ترین و پرحباب‌ترین صندوق در یک نگاه</li>
        <li>مرتب‌سازی همه صندوق‌ها بر اساس حباب، قیمت یا ارزش معاملات</li>
      </ul>
    </div>
    <div class="fx">
      <b>لایه ۰۳</b>
      <h3>مانیتورینگ روند NAV</h3>
      <p>حرکت ارزش خالص دارایی همه صندوق‌ها در طول روز.</p>
      <ul>
        <li>روند درون‌روزی NAV هر صندوق نسبت به دیروز</li>
        <li>مقایسه هر صندوق با میانه همه صندوق‌ها</li>
        <li>رتبه‌بندی صندوق‌ها بر اساس تغییر NAV</li>
      </ul>
    </div>
    <div class="fx">
      <b>لایه ۰۴</b>
      <h3>تحلیل ترکیب دارایی</h3>
      <p>معلوم می‌کند حباب هر صندوق چقدر توجیه‌پذیر است.</p>
      <ul>
        <li>سهم سکه، شمش و نقد در هر صندوق</li>
        <li>ترکیب کل بازار صندوق‌های طلا، وزنی با ارزش بازار</li>
        <li>حباب هر صندوق در برابر سهم سکه‌اش — کدام ارزنده‌تر است</li>
      </ul>
    </div>
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
    <details open><summary>حباب صندوق دقیقاً چطور محاسبه می‌شود؟</summary><p>حباب، فاصله قیمت آخرین معامله هر واحد صندوق از ارزش خالص دارایی (NAV) همان واحد است: قیمت ÷ NAV − ۱. NAV از فرابی گرفته می‌شود و هم‌زمان با قیمت‌ها به‌روز می‌شود. حباب منفی یعنی صندوق زیر ارزش دارایی‌اش معامله می‌شود.</p></details>
    <details><summary>چرا حباب را کنار سهم سکه صندوق می‌سنجید؟</summary><p>سکه معمولاً با حباب بیشتری از شمش معامله می‌شود، پس صندوقی که سکه بیشتری دارد طبیعتاً حباب بالاتری هم دارد. نمودار «حباب در برابر وزن سکه» این اثر را جدا می‌کند: صندوقی که زیر خط روند است، نسبت به صندوق‌های هم‌ترکیبش ارزان‌تر معامله می‌شود.</p></details>
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
    <p>داشبورد کامل بدون ثبت‌نام باز است — بازار امروز، جدول همه صندوق‌ها، روند NAV و ترکیب دارایی.</p>
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
/* hero card — the bubble spectrum renders itself (site/gold-data.js); this fills the numbers */
onGold(function(g){
  var s=g.summary, a=gText('pAvg',gPct(s.avg_bubble));
  if(a) a.style.color=gColor(s.avg_bubble);
  if(s.min_bubble) gText('pMin',s.min_bubble.symbol+' '+gPct(s.min_bubble.bubble));
  if(s.max_bubble) gText('pMax',s.max_bubble.symbol+' '+gPct(s.max_bubble.bubble));
});

/* bubble vs coin weight: <div data-bmix> renders itself (site/gold-data.js) */

"""

HTML = paywall.apply(HTML)
