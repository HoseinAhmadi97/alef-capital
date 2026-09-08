# -*- coding: utf-8 -*-
"""صفحه اصلی — hero، دو محصول، پلن‌ها، دانشنامه، سوالات، متن سئو."""

HTML = """<!-- HERO -->
<section class="hero sec">
<div class="wrap hero-grid">
  <div>
    <span class="eyebrow"><span class="dot"></span> داشبورد آربیتراژ صندوق طلا و کاوردکال بورس تهران — داده زنده</span>
    <h1>سرمایه شما،<br><span class="grad">با دو موتور بازده کم‌ریسک</span></h1>
    <p>الف کپیتال حباب صندوق‌های طلا و فرصت‌های کاوردکال بورس تهران را لحظه‌به‌لحظه رصد می‌کند و آن‌ها را به دو داشبورد قابل استفاده تبدیل می‌کند — تا تصمیم شما بر پایه داده باشد، نه حدس.</p>
    <div class="dblaunch">
      <a class="dbtn g" href="dashboard-gold.html">
        <span class="ring">🪙</span>
        <span class="tx"><b>داشبورد طلا</b>
          <em><span class="pl"></span>۳۰ صندوق · میانگین حباب <span id="hbG">‎−۰٫۲٪</span></em></span>
        <span class="ar">←</span>
      </a>
      <a class="dbtn b" href="dashboard-covered-call.html">
        <span class="ring">📈</span>
        <span class="tx"><b>داشبورد کاوردکال</b>
          <em><span class="pl"></span><span id="hbC">۱۲</span> فرصت · تا ۶۹٪ سالانه</em></span>
        <span class="ar">←</span>
      </a>
    </div>
    <p style="font-size:13px;color:var(--slate-500);margin:16px 0 0">هر دو داشبورد بدون ثبت‌نام قابل مشاهده‌اند — ستون‌های محاسباتی با عضویت رایگان باز می‌شوند.</p>
  </div>
  <div>
    <div class="livecards">

      <div class="lcard">
        <div class="lch"><span class="lbl">حباب صندوق‌های طلا</span><span class="live"><i></i>زنده</span></div>
        <div class="lcv"><span class="big num" id="bubAvg">‎−۰٫۳۴٪</span><span class="lcu">میانگین ۳۰ صندوق</span></div>
        <div class="dist" id="dist"></div>
        <div class="lcf">
          <span>کم‌حباب‌ترین <b id="bubMin">گوهر ‎−۱٫۷۹٪</b></span>
          <span>پرحباب‌ترین <b id="bubMax">کهربا ‎+۲٫۵۰٪</b></span>
        </div>
      </div>

      <div class="lcard">
        <div class="lch"><span class="lbl">فرصت‌های کاوردکال امروز</span><span class="live"><i></i>زنده</span></div>
        <div class="lcv"><span class="big num" id="ccCount">۱۲</span><span class="lcu">موقعیت با نرخ معادل بالای ۵۰٪</span></div>
        <table class="opt"><tbody id="optBody"></tbody></table>
      </div>

      <div class="lcard">
        <div class="lch"><span class="lbl">طلای ۱۸ عیار</span><span class="live"><i></i>زنده</span></div>
        <div class="lcv"><span class="big num" id="goldPx">۱۸۲,۲۵۷,۰۰۰</span><span class="chip down" id="goldD">▼ ۰٫۱۴٪</span></div>
        <svg class="spark" id="spark" viewBox="0 0 240 44" preserveAspectRatio="none">
          <defs><linearGradient id="sg" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="rgba(240,180,41,.35)"/><stop offset="100%" stop-color="rgba(240,180,41,0)"/>
          </linearGradient></defs>
          <path id="sparkFill" fill="url(#sg)"></path>
          <path id="sparkLine" fill="none" stroke="#C9861A" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"></path>
          <circle id="sparkDot" r="3" fill="#C9861A"></circle>
        </svg>
      </div>

    </div>
    <div class="lcbar">
      <span>آخرین به‌روزرسانی <b id="clock">۱۷:۳۱:۰۴</b></span>
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
      <div class="picon g">🟡</div>
      <h3>داشبورد آربیتراژ صندوق طلا</h3>
      <p>قیمت هر صندوق طلا دقیقاً برابر ارزش واقعی‌اش (NAV) نیست؛ این اختلاف را «حباب» می‌گویند. داشبورد آربیتراژ، حباب همه صندوق‌های طلای بورس را لحظه‌ای محاسبه می‌کند و صندوق‌های ارزنده را نشان می‌دهد.</p>
      <ul class="plist">
        <li>پایش لحظه‌ای حباب و NAV همه صندوق‌ها</li>
        <li>تحلیل ترکیب دارایی (سکه، شمش، گواهی سپرده)</li>
        <li>شناسایی خودکار صندوق ارزنده برای جابه‌جایی</li>
      </ul>
      <div class="target">بازده هدف: ۵ تا ۱۰ درصد سالانه طلای اضافه</div>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-gold" href="dashboard-gold.html" style="padding:12px 24px;font-size:14.5px"><ico>🟡</ico>داشبورد طلا</a><a class="btn btn-s" href="product-gold.html" style="padding:12px 22px;font-size:14.5px">معرفی محصول</a></div>
    </div>

    <div class="pcard">
      <div class="picon b">🔵</div>
      <h3>داشبورد کاوردکال (بهره ثابت)</h3>
      <p>کاوردکال یعنی خرید سهم و هم‌زمان فروش اختیار خرید همان سهم. نتیجه، یک بازده از پیش تعیین‌شده در بازه‌ای مشخص است. داشبورد ما هزاران قرارداد را می‌سنجد و بهترین نسبت بازده به ریسک را بیرون می‌کشد.</p>
      <ul class="plist">
        <li>دیدبان کامل قراردادهای اختیار خرید</li>
        <li>محاسبه خودکار نرخ سود معادل سالانه و حاشیه ریسک</li>
        <li>پایش سررسید و نقطه سربه‌سری هر موقعیت</li>
      </ul>
      <div class="target">بازده هدف: ۶۰ تا ۱۰۰ درصد سالانه با ریسک پایین</div>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-blue" href="dashboard-covered-call.html" style="padding:12px 24px;font-size:14.5px"><ico>🔵</ico>داشبورد کاوردکال</a><a class="btn btn-s" href="product-covered-call.html" style="padding:12px 22px;font-size:14.5px">معرفی محصول</a></div>
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
        <li>داده با تأخیر ۱۵ دقیقه</li>
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

  <div class="trust">
    <span>🔒 پرداخت امن</span><span>🧾 صدور فاکتور رسمی</span><span>↩️ بازگشت وجه تا ۷ روز</span><span>✕ لغو در هر زمان</span>
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
    <details open><summary>آیا می‌توانم قبل از خرید، داشبورد را ببینم؟</summary><p>بله. صفحه «نبض بازار» بدون ثبت‌نام باز است و با ثبت‌نام رایگان به جدول کامل صندوق‌ها با تأخیر ۱۵ دقیقه دسترسی دارید. خارج از ساعات معاملاتی هم داده کامل آخرین روز معاملاتی برای همه در دسترس است.</p></details>
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
/* ===================== LIVE DATA LAYER =====================
   TODO(اتصال): این مقادیر را به API بازار وصل کنید و مهر زمان
   واقعی سرور را نمایش دهید. ساختار خروجی مورد انتظار همین است.
   =========================================================== */
function pct(v,dec){return (v<0?'‎−':'‎+')+fa(Math.abs(v).toFixed(dec||2)).replace('.','٫')+'٪'}
function flash(el,up){el.classList.remove('fu','fd');void el.offsetWidth;el.classList.add(up?'fu':'fd');
  setTimeout(function(){el.classList.remove('fu','fd')},700)}

/* ---------- 1. نوار قیمت متحرک ---------- */

document.querySelectorAll('.tab').forEach(function(t){
  t.addEventListener('click',function(){
    document.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});
    t.classList.add('on');
  });
});"""
