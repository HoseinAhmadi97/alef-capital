# -*- coding: utf-8 -*-
"""Home page — hero, the two products, plans, wiki, FAQ, SEO copy."""

HTML = """<!-- HERO -->
<section class="hero sec">
<div class="wrap hero-grid">
  <div>
    <div class="tw"><span class="dot"></span><span class="txt" id="tw"></span><span class="car"></span></div>
    <h1>سرمایه شما،<br><span class="grad">با دو موتور بازده کم‌ریسک</span></h1>
    <p>الف کپیتال حباب صندوق‌های طلا و فرصت‌های کاوردکال بورس تهران را لحظه‌به‌لحظه رصد می‌کند و آن‌ها را به دو داشبورد قابل استفاده تبدیل می‌کند — تا تصمیم شما بر پایه داده باشد، نه حدس.</p>
    <div class="dblaunch">
      <a class="dbtn g" href="dashboard-gold.html">
        <span class="tx"><b>داشبورد طلا</b>
          <em><span class="pl"></span><span class="gcount">—</span> صندوق · میانگین حباب <span id="hbG">—</span></em></span>
        <span class="ar">←</span>
      </a>
      <a class="dbtn b" href="dashboard-covered-call.html">
        <span class="tx"><b>داشبورد کاوردکال</b>
          <em><span class="pl"></span><span id="hbC">۱۲</span> فرصت · تا ۶۹٪ سالانه</em></span>
        <span class="ar">←</span>
      </a>
    </div>
    <p style="font-size:13px;color:var(--slate-500);margin:16px 0 0">هر دو داشبورد کامل و بدون ثبت‌نام باز است — همه ستون‌های محاسباتی، همین حالا.</p>
  </div>
  <div>
    <div class="livecards">

      <div class="lcard">
        <div class="lch"><span class="lbl">حباب صندوق‌های طلا</span><span class="live" data-session="funds"><i></i><span>زنده</span></span></div>
        <div class="lcv"><span class="big num" id="bubAvg">—</span><span class="lcu">میانگین <span class="gcount">—</span> صندوق</span></div>
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
          <span>کم‌حباب‌ترین <b id="bubMin">—</b></span>
          <span>پرحباب‌ترین <b id="bubMax">—</b></span>
        </div>
      </div>

      <div class="lcard">
        <div class="lch"><span class="lbl">فرصت‌های کاوردکال امروز</span><span class="live"><i></i>زنده</span></div>
        <div class="lcv"><span class="big num" id="ccCount">۱۲</span><span class="lcu">موقعیت با نرخ معادل بالای ۵۰٪</span></div>
        <table class="opt"><tbody id="optBody"></tbody></table>
      </div>


    </div>
    <div class="lcbar">
      <span>آخرین به‌روزرسانی <b class="gupdated">—</b></span>
      <span class="prog"><i id="prog"></i></span>
    </div>
  </div>
</div>
</section>

<!-- KPI -->
<section class="kpis sec" style="padding-block:44px">
<div class="wrap kpi-grid">
  <div class="kpi"><b class="num">۳۰+</b><span>صندوق طلای تحت پایش</span></div>
  <div class="kpi"><b class="num">۳۶۸</b><span>قرارداد اختیار در دیدبان</span></div>
  <div class="kpi"><b class="num">‎۵–۱۰٪</b><span>بازده هدف آربیتراژ سالانه</span></div>
  <div class="kpi"><b class="num">۲۴/۷</b><span>رصد در ساعات معاملاتی</span></div>
</div>
</section>

<!-- PRODUCTS -->
<section class="sec" id="products">
<div class="wrap">
  <span class="eyebrow">محصولات</span>
  <h2 class="h2">دو محصول، دو مسیر کسب بازده</h2>
  <p class="lead">هر دو بر یک اصل استوارند: فرصت‌هایی که با چشم و به‌صورت دستی قابل شناسایی نیستند، اما الگوریتم آن‌ها را لحظه‌ای پیدا می‌کند.</p>

  <div class="two">
    <div class="pcard">
      <h3>داشبورد آربیتراژ صندوق طلا</h3>
      <p>قیمت هر صندوق طلا دقیقاً برابر ارزش واقعی‌اش (NAV) نیست؛ این اختلاف را «حباب» می‌گویند. داشبورد آربیتراژ، حباب همه صندوق‌های طلای بورس را لحظه‌ای محاسبه می‌کند و صندوق‌های ارزنده را نشان می‌دهد.</p>
      <ul class="plist">
        <li>پایش لحظه‌ای حباب و NAV همه صندوق‌ها</li>
        <li>تحلیل ترکیب دارایی (سکه، شمش، گواهی سپرده)</li>
        <li>شناسایی خودکار صندوق ارزنده برای جابه‌جایی</li>
      </ul>
      <div class="target">بازده هدف: ۵ تا ۱۰ درصد سالانه طلای اضافه</div>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-gold" href="dashboard-gold.html" style="padding:12px 24px;font-size:14.5px"><ico>🪙</ico>داشبورد طلا</a><a class="btn btn-s" href="product-gold.html" style="padding:12px 22px;font-size:14.5px">معرفی محصول</a></div>
    </div>

    <div class="pcard">
      <h3>داشبورد کاوردکال (بهره ثابت)</h3>
      <p>کاوردکال یعنی خرید سهم و هم‌زمان فروش اختیار خرید همان سهم. نتیجه، یک بازده از پیش تعیین‌شده در بازه‌ای مشخص است. داشبورد ما هزاران قرارداد را می‌سنجد و بهترین نسبت بازده به ریسک را بیرون می‌کشد.</p>
      <ul class="plist">
        <li>دیدبان کامل قراردادهای اختیار خرید</li>
        <li>محاسبه خودکار نرخ سود معادل سالانه و حاشیه ریسک</li>
        <li>پایش سررسید و نقطه سربه‌سری هر موقعیت</li>
      </ul>
      <div class="target">بازده هدف: ۶۰ تا ۱۰۰ درصد سالانه با ریسک پایین</div>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-blue" href="dashboard-covered-call.html" style="padding:12px 24px;font-size:14.5px"><ico>📈</ico>داشبورد کاوردکال</a><a class="btn btn-s" href="product-covered-call.html" style="padding:12px 22px;font-size:14.5px">معرفی محصول</a></div>
    </div>
  </div>
</div>
</section>

<!-- PRICING -->
<section class="sec" id="pricing" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap" style="text-align:center">
  <span class="eyebrow">اشتراک</span>
  <h2 class="h2">پلن مناسب خود را انتخاب کنید</h2>
  <p class="lead" style="margin-inline:auto">همه پلن‌ها ۷ روز رایگان، بدون نیاز به کارت بانکی. هر زمان بخواهید لغو کنید.</p>

  <div>
    <div class="toggle">
      <button id="bm" class="on" onclick="setP('m')">ماهانه</button>
      <button id="bq" onclick="setP('q')">۳ ماهه</button>
      <button id="by" onclick="setP('y')">سالانه</button>
    </div>
    <span class="saveband">تا ۳۰٪ تخفیف با پرداخت سالانه</span>
  </div>

  <div class="plans" style="text-align:right">
    <div class="plan">
      <h3>پایه</h3>
      <div class="who">آشنایی با پلتفرم و داده بازار</div>
      <div class="price">رایگان</div>
      <div class="per">همیشه رایگان</div>
      <a class="btn btn-s" href="pricing.html">شروع رایگان</a>
      <ul class="feat">
        <li>۵ صندوق برتر</li>
        <li>داده لحظه‌ای</li>
        <li>۱ هشدار</li>
        <li class="no">داشبورد کاوردکال</li>
        <li class="no">تاریخچه و خروجی اکسل</li>
      </ul>
    </div>

    <div class="plan hot">
      <span class="badge">محبوب‌ترین</span>
      <h3>طلا</h3>
      <div class="who">دارندگان صندوق طلا که دنبال بازده اضافه‌اند</div>
      <div class="price"><span class="num" id="p-gold">۱,۹۰۰,۰۰۰</span> <small>تومان</small></div>
      <div class="per" id="u-gold">ماهانه</div>
      <a class="btn btn-p" href="pricing.html">خرید اشتراک طلا</a>
      <ul class="feat">
        <li>همه صندوق‌های طلا، لحظه‌ای</li>
        <li>تحلیل ترکیب دارایی صندوق‌ها</li>
        <li>مانیتورینگ NAV (Latent / Pure)</li>
        <li>۲۰ هشدار حباب + تاریخچه ۶ ماه</li>
        <li>خروجی اکسل · پشتیبانی تیکت</li>
        <li class="no">داشبورد کاوردکال</li>
      </ul>
    </div>

    <div class="plan">
      <h3>حرفه‌ای</h3>
      <div class="who">معامله‌گران اختیار معامله و پرتفوهای ترکیبی</div>
      <div class="price"><span class="num" id="p-pro">۳,۹۰۰,۰۰۰</span> <small>تومان</small></div>
      <div class="per" id="u-pro">ماهانه</div>
      <a class="btn btn-s" href="pricing.html">خرید اشتراک حرفه‌ای</a>
      <ul class="feat">
        <li>همه امکانات پلن طلا</li>
        <li>دیدبان کامل کاوردکال</li>
        <li>نمودار سود و زیان و نقطه سربه‌سری</li>
        <li>هشدار نامحدود · تاریخچه نامحدود</li>
        <li>دسترسی API</li>
        <li>پشتیبانی تلفنی اختصاصی</li>
      </ul>
    </div>
  </div>

  <div class="entband" style="text-align:right">
    <div>
      <h3>پلن سازمانی و مدیریت پرتفوی</h3>
      <p>اجرای خودکار الگوریتم روی حساب کارگزاری شما، گزارش اختصاصی، و دسترسی چندکاربره برای تیم‌های سرمایه‌گذاری.</p>
    </div>
    <a class="btn btn-p" href="services.html">درخواست مشاوره</a>
  </div>
</div>
</section>

<!-- WIKI -->
<section class="sec" id="wiki">
<div class="wrap">
  <span class="eyebrow">دانشنامه</span>
  <h2 class="h2">قبل از سرمایه‌گذاری، بدانید چه می‌کنید</h2>
  <p class="lead">مرجع آموزشی صندوق‌های طلا، حباب و NAV، و استراتژی‌های اختیار معامله — با مثال عددی و داده واقعی بازار ایران.</p>

  <div class="wgrid">
    <a class="wcard feature" href="wiki-covered-call.html">
      <span style="color:var(--gold-700);font-weight:800;font-size:13px">✨ پیشنهاد مطالعه</span>
      <h3 style="margin-top:8px">کاوردکال چیست؟ راهنمای کامل با مثال عددی</h3>
      <span>خرید سهم ۳٬۰۰۰ تومانی و فروش اختیار خرید ۲٬۵۰۰ تومانی به قیمت ۷۰۰ تومان با سررسید ۶۰ روزه، یعنی نرخ سود معادل سالانه ۶۶ درصد و حاشیه ریسک ۲۰ درصد. در این مقاله فرمول، نقطه سربه‌سری و سه سناریوی سررسید را قدم‌به‌قدم می‌بینید — به‌همراه ماشین‌حساب تعاملی.</span>
      <div style="margin-top:12px;color:var(--gold-700);font-weight:700;font-size:14px">مشاهده مقاله ←</div>
    </a>
    <a class="wcard" href="wiki.html"><h3>🥇 صندوق‌های طلا و ETF</h3><span>۵ مقاله — از مبانی تا مقایسه صندوق‌ها</span></a>
    <a class="wcard" href="wiki.html"><h3>📊 آربیتراژ، حباب و NAV</h3><span>۶ مقاله — قلب محصول اول</span></a>
    <a class="wcard" href="wiki.html"><h3>📈 اختیار معامله و کاوردکال</h3><span>۷ مقاله — با ماشین‌حساب تعاملی</span></a>
    <a class="wcard" href="wiki.html"><h3>🛡️ مدیریت ریسک و سرمایه</h3><span>۴ مقاله</span></a>
    <a class="wcard" href="wiki.html"><h3>📖 راهنمای داشبوردها</h3><span>۲ راهنمای گام‌به‌گام</span></a>
  </div>
</div>
</section>

<!-- FAQ -->
<section class="sec" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <h2 class="h2" style="text-align:center">سوالات متداول خرید</h2>
  <div class="faq">
    <details open><summary>آیا می‌توانم قبل از خرید، داشبورد را ببینم؟</summary><p>بله. صفحه «نبض بازار» و داشبورد طلا بدون ثبت‌نام باز هستند و داده لحظه‌ای همه صندوق‌ها را نشان می‌دهند. خارج از ساعات معاملاتی هم داده کامل آخرین روز معاملاتی برای همه در دسترس است.</p></details>
    <details><summary>تفاوت پلن طلا و حرفه‌ای در عمل چیست؟</summary><p>پلن طلا فقط حوزه صندوق‌های طلا را پوشش می‌دهد: حباب، NAV و ترکیب دارایی. پلن حرفه‌ای علاوه بر آن، دیدبان کامل قراردادهای اختیار خرید، محاسبه نرخ سود معادل سالانه، نمودار سود و زیان و دسترسی API را اضافه می‌کند.</p></details>
    <details><summary>داده‌ها از چه منبعی و با چه تأخیری می‌آیند؟</summary><p>داده مستقیماً از تابلوی معاملات بورس تهران و بورس کالا خوانده می‌شود. در پلن‌های پولی تأخیر عملی زیر یک ثانیه است و مهر زمان هر داده روی صفحه نمایش داده می‌شود.</p></details>
    <details><summary>امکان ارتقای پلن در میانه دوره وجود دارد؟</summary><p>بله. هزینه باقی‌مانده پلن فعلی به‌صورت اعتبار محاسبه و از مبلغ پلن جدید کسر می‌شود.</p></details>
    <details><summary>اگر اشتراکم تمام شود، هشدارها و تنظیماتم را از دست می‌دهم؟</summary><p>خیر. تنظیمات، هشدارها و لیست‌های ذخیره‌شده حفظ می‌شوند و با تمدید اشتراک دوباره فعال می‌گردند.</p></details>
  </div>
</div>
</section>

<!-- SEO PROSE -->
<section class="prose sec">
<div class="wrap">
  <h2 class="h2">الف کپیتال چه ابزارهایی برای بازار طلا و اختیار معامله دارد؟</h2>
  <p style="margin-top:14px">الف کپیتال دو خانواده ابزار برای سرمایه‌گذاران بورس تهران فراهم می‌کند: یکی برای بازار صندوق‌های طلا و دیگری برای بازار اختیار معامله. داده هر صندوق طلا — قیمت لحظه‌ای، ارزش خالص دارایی، ترکیب دارایی و حباب — در یک جا جمع می‌شود، و روی همان داده، محاسبات آربیتراژ و شناسایی صندوق ارزنده انجام می‌گیرد.</p>
  <h3>حباب صندوق‌های طلا: چرا قیمت با ارزش واقعی فرق می‌کند</h3>
  <p>قیمت هر صندوق طلا در بورس، به‌جای تبعیت دقیق از ارزش خالص دارایی، بیشتر تحت تأثیر عرضه و تقاضای لحظه‌ای معامله‌گران قرار می‌گیرد. همین موضوع باعث می‌شود برخی صندوق‌ها بالاتر از ارزش واقعی‌شان معامله شوند و برخی دیگر نزدیک‌تر یا پایین‌تر از آن. چون دارایی پایه همه این صندوق‌ها یکسان است — گواهی سپرده سکه و شمش طلا — این اختلاف قیمت یک فرصت آربیتراژ می‌سازد.</p>
  <h3>داشبورد آربیتراژ: چه چیزی را لحظه‌ای می‌بینید</h3>
  <p>داشبورد آربیتراژ چهار لایه داده را کنار هم می‌گذارد: قیمت پایه (طلای ۱۸ عیار، شمش، سکه، اونس جهانی و دلار)، حباب لحظه‌ای هر صندوق نسبت به ارزش خالص دارایی، روند ارزش خالص دارایی به تفکیک هر صندوق، و ترکیب دارایی صندوق‌ها. خروجی این چهار لایه، شناسایی صندوق‌هایی است که نسبت به کیفیت دارایی‌شان ارزنده‌تر معامله می‌شوند.</p>
  <h3>کاوردکال: بهره ثابت از بازار سهام</h3>
  <p>کاوردکال به موقعیتی گفته می‌شود که با خرید یک سهم و فروش اختیار خرید همان سهم ساخته می‌شود. با این کار می‌توان تا حد زیادی جلوی ضرر ناشی از ریزش سهم را گرفت و در یک بازه زمانی مشخص به سود ثابت و از پیش تعیین‌شده دست یافت. موقعیت‌های جذاب در میان انبوه قراردادهای موجود محدود و کمیاب هستند و شناسایی و ورود به‌موقع به آن‌ها به‌صورت دستی عملاً امکان‌پذیر نیست.</p>
  <h3>اگر تازه با صندوق‌های طلا آشنا می‌شوید</h3>
  <p>پیش از باز کردن جدول‌ها، دانشنامه الف کپیتال از صفر شروع می‌کند: صندوق طلا چیست، ارزش خالص دارایی چطور محاسبه می‌شود، حباب یعنی چه و ریسک هر استراتژی کجاست. بیرون از ساعت معاملات، نبض بازار برای همه باز است و می‌توانید بدون اشتراک با داده آخرین روز معاملاتی کار کنید.</p>
</div>
</section>"""

JS = """var PRICES={
  m:{gold:'۱,۹۰۰,۰۰۰',pro:'۳,۹۰۰,۰۰۰',u:'ماهانه'},
  q:{gold:'۱,۶۱۵,۰۰۰',pro:'۳,۳۱۵,۰۰۰',u:'ماهانه، با پرداخت ۳ ماهه (۱۵٪ تخفیف)'},
  y:{gold:'۱,۳۳۰,۰۰۰',pro:'۲,۷۳۰,۰۰۰',u:'ماهانه، با پرداخت سالانه (۳۰٪ تخفیف)'}
};
function setP(k){
  var p=PRICES[k];
  document.getElementById('p-gold').textContent=p.gold;
  document.getElementById('p-pro').textContent=p.pro;
  document.getElementById('u-gold').textContent=p.u;
  document.getElementById('u-pro').textContent=p.u;
  ['m','q','y'].forEach(function(x){document.getElementById('b'+x).className=(x===k?'on':'')});
}
/* Gold numbers come from the gold snapshot (site/gold-data.js); the
   covered-call card below is still sample data — no options source yet. */
function flash(el,up){el.classList.remove('fu','fd');void el.offsetWidth;el.classList.add(up?'fu':'fd');
  setTimeout(function(){el.classList.remove('fu','fd')},700)}
var CALM=window.matchMedia('(prefers-reduced-motion:reduce)').matches;

/* ---------- 1. bubble spectrum — every fund as a dot on one axis ----------
   x = bubble (price vs farabi NAV), stacked beeswarm-style so funds with
   nearly the same bubble sit above/below each other instead of on top.
   The track shades red → green; the dashed tick is NAV (0%), the gold
   marker the average. Colours follow the site rule: negative red, positive green. */
(function(){
  var svg=document.getElementById('bSpec'); if(!svg) return;
  var X0=8, X1=292, MID=46, R=4.6, GAP=10.4;
  var tip=document.getElementById('bTip'), box=svg.parentNode;
  onGold(function(g){
    var fs=g.withBubble.slice().sort(function(a,b){return a.nominal_bubble-b.nominal_bubble});
    if(!fs.length) return;
    var vals=fs.map(function(f){return f.nominal_bubble*100});
    /* a symmetric-enough domain that always includes 0 and has 10% headroom */
    var lo=Math.min(0,vals[0]), hi=Math.max(0,vals[vals.length-1]), pad=Math.max(0.15,(hi-lo)*0.1);
    lo-=pad; hi+=pad;
    function X(v){return X0+(v-lo)/(hi-lo)*(X1-X0)}

    /* beeswarm: place each dot on the lowest free lane (0, +1, −1, +2, …) */
    var lanes=[], placed=fs.map(function(f,i){
      var x=X(vals[i]), lane=0;
      for(var k=0;k<12;k++){
        var l=k===0?0:(k%2?(k+1)/2:-k/2);
        if(!(lanes[l]||[]).some(function(px){return Math.abs(px-x)<R*2+0.6})){lane=l;break}
      }
      (lanes[lane]=lanes[lane]||[]).push(x);
      return {f:f,x:x,lane:lane,v:vals[i]};
    });
    /* keep the swarm inside the card: squeeze lanes if a cluster runs deep */
    var deepest=Math.max.apply(null,placed.map(function(p){return Math.abs(p.lane)}));
    var gap=deepest>3?GAP*3/deepest:GAP;
    placed.forEach(function(p){p.y=MID+p.lane*gap});

    document.getElementById('bDots').innerHTML=placed.map(function(p,i){
      return '<circle data-i="'+i+'" cx="'+p.x.toFixed(1)+'" cy="'+p.y.toFixed(1)+'" r="'+R+'" fill="'+
        gBarColor(p.f.nominal_bubble,true).replace('.75','.9')+'" stroke="var(--surface)" stroke-width="1.2"/>'}).join('');

    var zx=X(0).toFixed(1);
    document.getElementById('bZero').innerHTML=
      '<line x1="'+zx+'" x2="'+zx+'" y1="8" y2="84" stroke="var(--slate-400)" stroke-dasharray="2 3"/>';
    var s=g.summary, ax=X(s.avg_bubble*100).toFixed(1);
    document.getElementById('bAvgMark').innerHTML=
      '<path d="M'+ax+' 91 l-5 -7 h10 z" fill="var(--gold-600)"/>';
    document.getElementById('bAxis').innerHTML=
      '<text x="'+X0+'" y="8">'+gPct(lo/100,1)+'</text>'+
      '<text x="'+zx+'" y="8" text-anchor="middle" font-weight="700">NAV</text>'+
      '<text x="'+X1+'" y="8" text-anchor="end">'+gPct(hi/100,1)+'</text>';

    var below=fs.filter(function(f){return f.nominal_bubble<0}).length, above=fs.length-below;
    gText('bBelow',fa(below)); gText('bAbove',fa(above));
    document.getElementById('bBelowBar').style.width=(below/fs.length*100)+'%';
    document.getElementById('bAboveBar').style.width=(above/fs.length*100)+'%';

    svg._placed=placed;
  });

  /* hover / tap a dot to name it */
  function show(ev){
    var c=ev.target.closest&&ev.target.closest('circle[data-i]');
    if(!c||!svg._placed){tip.hidden=true; return}
    var p=svg._placed[+c.getAttribute('data-i')], r=svg.getBoundingClientRect();
    tip.innerHTML='صندوق '+p.f.symbol+' <b style="color:'+gColor(p.f.nominal_bubble)+'">'+gPct(p.f.nominal_bubble)+'</b>';
    tip.style.left=(p.x/300*r.width)+'px'; tip.style.top=(p.y/92*r.height)+'px';
    tip.hidden=false;
  }
  svg.addEventListener('mousemove',show);
  svg.addEventListener('click',show);
  svg.addEventListener('mouseleave',function(){tip.hidden=true});
})();

onGold(function(g){
  var s=g.summary, el=document.getElementById('bubAvg');
  if(el){var prev=el.textContent; el.textContent=gPct(s.avg_bubble); el.style.color=gColor(s.avg_bubble);
    if(prev!=='—'&&prev!==el.textContent) flash(el,s.avg_bubble>=0)}
  if(s.min_bubble) gText('bubMin',s.min_bubble.symbol+' '+gPct(s.min_bubble.bubble));
  if(s.max_bubble) gText('bubMax',s.max_bubble.symbol+' '+gPct(s.max_bubble.bubble));
  gText('hbG',gPct(s.avg_bubble,1));
});

/* ---------- 2. covered-call opportunities ---------- */
/* [نماد, C, DTM, K, P] — the same rows and the same formula as the dashboard
   and the calculator, so the three pages can never disagree by a decimal */
var OPTS=[['ضستا۳۰۱۰',503,15,1400,1873],['ضشنا۶۰۴۹',1851,20,6000,7696],
          ['ضخود۶۰۵۵',1262,57,3000,4082],['ضملی۳۰۵۸',454,43,1260,1663]];
function annual(o){return (Math.pow(o[3]/(o[4]-o[1]),365/o[2])-1)*100}
function drawOpts(){
  var b=document.getElementById('optBody'); if(!b) return;
  b.innerHTML=OPTS.map(function(o){
    return '<tr><td class="sym">'+o[0]+'</td>'+
           '<td class="dtm">'+fa(o[2])+' روز</td>'+
           '<td class="rt">'+fa(annual(o).toFixed(1)).replace('.','٫')+'٪ <em>سالانه</em></td></tr>'}).join('');
  var c=document.getElementById('ccCount'); if(c) c.textContent=fa(OPTS.length+8);
  var h=document.getElementById('hbC'); if(h) h.textContent=fa(OPTS.length+8);
}

/* ---------- 3. progress bar: time until the next data poll ---------- */
(function(){
  drawOpts();
  var prog=document.getElementById('prog'); if(!prog||CALM) return;
  var t0=Date.now();
  onGold(function(){t0=Date.now()});
  setInterval(function(){
    prog.style.width=Math.min(100,(Date.now()-t0)/GOLD_POLL_MS*100)+'%';
  },250);
})();

/* ---------- 5. typewriter line in the hero ---------- */
var TW=[
 'حباب هر ۳۰ صندوق طلا، هر ثانیه بازمحاسبه می‌شود.',
 '۳۶۸ قرارداد اختیار، زیر ذره‌بین یک الگوریتم.',
 'فاصله قیمت تا ارزش — همان چیزی که شکار می‌کنیم.',
 'فرصتی که با چشم پیدا نمی‌شود، با محاسبه پیدا می‌شود.',
 'تصمیم بر پایه داده، نه بر پایه حدس.'];
(function(){
  var el=document.getElementById('tw'); if(!el) return;
  if(CALM){el.textContent=TW[0]; return}          /* no animation when asked */
  var i=0,j=0,del=false;
  (function step(){
    var full=TW[i];
    j += del ? -1 : 1;
    el.textContent=full.slice(0,j);
    var wait=del?26:58;
    if(!del && j===full.length){del=true; wait=2100}
    else if(del && j===0){del=false; i=(i+1)%TW.length; wait=320}
    setTimeout(step,wait);
  })();
})();

/* ---------- 6. tabs ---------- */
document.querySelectorAll('.tab').forEach(function(t){
  t.addEventListener('click',function(){
    document.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});
    t.classList.add('on');
  });
});"""
