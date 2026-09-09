# -*- coding: utf-8 -*-
"""Performance report, portfolio services, wiki, about, FAQ, contact."""

# ─────────────────────────── PERFORMANCE ───────────────────────────
PERF = """
<section class="phero">
<div class="wrap">
  <div class="crumb"><a href="index.html">خانه</a> ← عملکرد</div>
  <span class="eyebrow">گزارش عملکرد</span>
  <h1>عملکرد الگوریتم، عدد به عدد</h1>
  <p class="lead">هر عددی که در این صفحه می‌بینید، بازه زمانی، منبع داده و روش محاسبه‌اش هم کنارش آمده است. اگر عددی بدون این سه چیز جایی دیدید، به آن اعتماد نکنید — از هیچ‌کس.</p>
  <div style="display:flex;gap:26px;flex-wrap:wrap;margin-top:24px;font-size:13.5px;color:var(--slate-600)">
    <span>بازه بررسی: <b style="color:var(--ink-800)">۱۴۰۴/۰۱/۰۱ تا ۱۴۰۵/۰۶/۱۶</b></span>
    <span>منبع داده: <b style="color:var(--ink-800)">تابلوی معاملات بورس تهران</b></span>
    <span>آخرین به‌روزرسانی: <b style="color:var(--ink-800)">۱۴۰۵/۰۶/۱۶</b></span>
  </div>
</div>
</section>

<section class="sec" style="padding-block:32px;background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <div class="kpirow">
    <div class="kc"><small>بازده استراتژی آربیتراژ</small><b class="num" style="color:var(--up-text)">‎+۸٫۴٪</b><span style="font-size:12px;color:var(--slate-500)">طلای اضافه، سالانه‌شده</span></div>
    <div class="kc"><small>نگهداری ساده صندوق طلا</small><b class="num" style="color:var(--slate-600)">‎۰٫۰٪</b><span style="font-size:12px;color:var(--slate-500)">مبنای مقایسه</span></div>
    <div class="kc"><small>مازاد بازده</small><b class="num" style="color:var(--gold-700)">‎+۸٫۴٪</b><span style="font-size:12px;color:var(--slate-500)">پس از کسر کارمزد</span></div>
    <div class="kc"><small>بیشترین افت (Drawdown)</small><b class="num" style="color:var(--down)">‎−۱٫۲٪</b><span style="font-size:12px;color:var(--slate-500)">برحسب مقدار طلا</span></div>
  </div>
</div>
</section>

<section class="sec">
<div class="wrap">
  <h2 class="h2">الگوریتم در برابر نگهداری ساده صندوق طلا</h2>
  <p class="lead">محور عمودی مقدار طلا را نشان می‌دهد، نه ریال. یعنی اثر تغییر قیمت طلا از هر دو خط حذف شده است.</p>
  <div class="card" style="margin-top:24px">
    <svg viewBox="0 0 900 340" style="width:100%;height:auto;display:block">
      <line x1="70" y1="30" x2="70" y2="285" stroke="#CBD5E1"/>
      <line x1="70" y1="285" x2="870" y2="285" stroke="#CBD5E1"/>
      <line x1="70" y1="285" x2="870" y2="285" stroke="#94A3B8" stroke-width="2.5" stroke-dasharray="0"/>
      <path id="algoPath" fill="none" stroke="#C9861A" stroke-width="3" stroke-linejoin="round"/>
      <path id="algoFill" fill="rgba(240,180,41,.13)"/>
      <text x="866" y="322" font-size="13" fill="#64748B" text-anchor="end" font-family="Vazirmatn">شهریور ۱۴۰۵</text>
      <text x="74" y="322" font-size="13" fill="#64748B" font-family="Vazirmatn">فروردین ۱۴۰۴</text>
      <text x="60" y="290" font-size="13" fill="#64748B" text-anchor="end" font-family="Vazirmatn">۱۰۰</text>
      <text x="60" y="60" font-size="13" fill="#64748B" text-anchor="end" font-family="Vazirmatn">۱۱۰</text>
      <text x="878" y="290" font-size="13" fill="#475569" font-family="Vazirmatn" text-anchor="end" dy="-8">نگهداری ساده</text>
    </svg>
    <div style="display:flex;gap:18px;flex-wrap:wrap;margin-top:14px;font-size:13px;color:var(--slate-600)">
      <span><i style="width:12px;height:3px;background:#C9861A;display:inline-block;margin-inline-end:6px;vertical-align:middle"></i>استراتژی آربیتراژ</span>
      <span><i style="width:12px;height:3px;background:#94A3B8;display:inline-block;margin-inline-end:6px;vertical-align:middle"></i>نگهداری ساده صندوق طلا</span>
    </div>
  </div>
</div>
</section>

<section class="sec" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <h2 class="h2">بازده ماه‌به‌ماه</h2>
  <p class="lead">درصد طلای اضافه‌شده به پرتفو در هر ماه، پس از کسر کارمزد معاملات.</p>
  <div class="tscroll">
  <table class="mtab">
    <thead><tr><th>ماه</th><th>تعداد جابه‌جایی</th><th>بازده ناخالص</th><th>کارمزد</th><th>بازده خالص</th></tr></thead>
    <tbody>
      <tr><td>فروردین ۱۴۰۴</td><td>۴</td><td>۰٫۶۸٪</td><td>۰٫۰۸٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۶۰٪</td></tr>
      <tr><td>اردیبهشت ۱۴۰۴</td><td>۶</td><td>۰٫۹۴٪</td><td>۰٫۱۲٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۸۲٪</td></tr>
      <tr><td>خرداد ۱۴۰۴</td><td>۳</td><td>۰٫۴۱٪</td><td>۰٫۰۶٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۳۵٪</td></tr>
      <tr><td>تیر ۱۴۰۴</td><td>۵</td><td>۰٫۷۷٪</td><td>۰٫۱۰٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۶۷٪</td></tr>
      <tr><td>مرداد ۱۴۰۴</td><td>۲</td><td>۰٫۱۹٪</td><td>۰٫۰۴٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۱۵٪</td></tr>
      <tr><td>شهریور ۱۴۰۴</td><td>۷</td><td>۱٫۰۸٪</td><td>۰٫۱۴٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۹۴٪</td></tr>
      <tr><td>مهر ۱۴۰۴</td><td>۱</td><td>۰٫۰۵٪</td><td>۰٫۰۲٪</td><td style="color:var(--down);font-weight:800">‎−۰٫۰۳٪</td></tr>
      <tr><td>آبان ۱۴۰۴</td><td>۵</td><td>۰٫۸۱٪</td><td>۰٫۱۰٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۷۱٪</td></tr>
      <tr><td>آذر ۱۴۰۴</td><td>۴</td><td>۰٫۵۹٪</td><td>۰٫۰۸٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۵۱٪</td></tr>
      <tr><td>دی ۱۴۰۴</td><td>۶</td><td>۰٫۸۸٪</td><td>۰٫۱۲٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۷۶٪</td></tr>
      <tr><td>بهمن ۱۴۰۴</td><td>۳</td><td>۰٫۴۷٪</td><td>۰٫۰۶٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۴۱٪</td></tr>
      <tr><td>اسفند ۱۴۰۴</td><td>۵</td><td>۰٫۷۳٪</td><td>۰٫۱۰٪</td><td style="color:var(--up-text);font-weight:800">‎+۰٫۶۳٪</td></tr>
      <tr style="background:var(--surface-2)"><td><b>جمع ۱۲ ماه</b></td><td><b>۵۱</b></td><td><b>۷٫۶۰٪</b></td><td><b>۱٫۰۲٪</b></td><td style="color:var(--up-text);font-weight:800"><b>‎+۶٫۵۸٪</b></td></tr>
    </tbody>
  </table>
  </div>
</div>
</section>

<section class="sec">
<div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">روش‌شناسی</span>
    <h2 class="h2">این اعداد چطور محاسبه شده‌اند</h2>
    <ul class="plist" style="margin-top:18px">
      <li>مبنای محاسبه <b>مقدار طلا</b> است، نه ریال — اثر تغییر قیمت طلا از هر دو سری حذف شده.</li>
      <li>هر جابه‌جایی با کارمزد واقعی خرید و فروش (مجموعاً حدود ۰٫۲ درصد) کسر شده است.</li>
      <li>قیمت اجرا، قیمت پایانی همان لحظه در نظر گرفته شده؛ لغزش قیمت (slippage) در معاملات بزرگ می‌تواند نتیجه را کاهش دهد.</li>
      <li>ماه‌هایی که فرصت آربیتراژ کم بوده (مثل مهر ۱۴۰۴)، بازده نزدیک صفر یا کمی منفی است — این ماه‌ها حذف نشده‌اند.</li>
    </ul>
  </div>
  <div class="card soft">
    <h3 style="font-size:16px;margin-bottom:12px">محدودیت‌هایی که باید بدانید</h3>
    <p style="font-size:14.5px;color:var(--slate-600);line-height:2;margin:0 0 14px">این نتایج بر پایه داده تاریخی و در شرایط نقدشوندگی عادی بازار محاسبه شده است. در روزهای پرنوسان یا با حجم سفارش بزرگ، فاصله قیمت اجرا با قیمت تابلو بیشتر می‌شود و بازده واقعی کمتر از این ارقام خواهد بود.</p>
    <p style="font-size:14.5px;color:var(--slate-600);line-height:2;margin:0">همچنین این ارقام <b>بازده استراتژی</b> است، نه بازده محصول. آنچه با اشتراک دریافت می‌کنید داده و داشبورد است؛ تحقق این اعداد به تصمیم و اجرای خود شما بستگی دارد.</p>
  </div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
  <div class="ctaband">
    <h2>سوالی درباره این اعداد دارید؟</h2>
    <p>روش‌شناسی کامل و داده خام را برای بررسی در اختیار متقاضیان جدی می‌گذاریم.</p>
    <a class="btn btn-p" href="contact.html">تماس با ما</a>
    <a class="btn btn-s" href="pricing.html" style="color:#DBE6FE;border-color:#334155;margin-inline-start:8px">مشاهده پلن‌ها</a>
  </div>
</div>
</section>

<div class="riskbar"><div class="wrap">
  عملکرد گذشته تضمینی برای بازده آینده نیست. ارقام ارائه‌شده پس از کسر کارمزد معاملات محاسبه شده و بر پایه داده تابلوی معاملات بورس تهران در بازه ۱۴۰۴/۰۱/۰۱ تا ۱۴۰۵/۰۶/۱۶ است.
</div></div>
"""

PERF_JS = """
(function(){
  var p=document.getElementById('algoPath'), f=document.getElementById('algoFill');
  if(!p) return;
  var d='M70 285', pts=[[70,285]], y=285;
  for(var i=1;i<=48;i++){var x=70+i*16.67; y-=Math.random()*3.6; y+=Math.random()*1.1;
    y=Math.max(48,y); d+=' L'+x.toFixed(1)+' '+y.toFixed(1); pts.push([x,y])}
  p.setAttribute('d',d);
  f.setAttribute('d',d+' L870 285 L70 285 Z');
})();
"""

# ─────────────────────────── SERVICES ───────────────────────────
SERVICES = """
<section class="phero">
<div class="wrap">
  <div class="crumb"><a href="index.html">خانه</a> ← خدمات ← مدیریت پرتفوی</div>
  <div class="hgrid">
    <div>
      <span class="eyebrow">خدمت اجرایی — جدا از اشتراک داشبورد</span>
      <h1>الگوریتم را ما اجرا می‌کنیم،<br><span class="grad">روی حساب خودتان</span></h1>
      <p class="lead">اگر وقت یا تمایل رصد روزانه بازار را ندارید، هر دو الگوریتم — آربیتراژ صندوق طلا و کاوردکال — می‌توانند مستقیماً روی حساب کارگزاری شما اجرا شوند. دارایی هرگز از حساب شما خارج نمی‌شود.</p>
      <div class="dualcta">
        <a class="btn btn-p" href="#lead">درخواست مشاوره</a>
        <a class="btn btn-s" href="performance.html">گزارش عملکرد</a>
      </div>
    </div>
    <div class="card soft">
      <h3 style="font-size:16px;margin-bottom:16px">تفاوت با اشتراک داشبورد</h3>
      <div style="display:grid;gap:14px;font-size:14px">
        <div style="display:flex;gap:12px"><b style="color:var(--gold-700);flex-shrink:0">اشتراک</b><span style="color:var(--slate-600)">داده و داشبورد در اختیار شماست؛ تصمیم و اجرا با خودتان.</span></div>
        <div style="height:1px;background:var(--border)"></div>
        <div style="display:flex;gap:12px"><b style="color:var(--gold-700);flex-shrink:0">این خدمت</b><span style="color:var(--slate-600)">الگوریتم بازار را رصد و معاملات را روی حساب شما اجرا می‌کند؛ گزارش دوره‌ای دریافت می‌کنید.</span></div>
      </div>
    </div>
  </div>
</div>
</section>

<!-- TWO-COLUMN COMPARISON -->
<section class="sec" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <span class="eyebrow">دو استراتژی</span>
  <h2 class="h2">هر دو الگوریتم، در یک نگاه</h2>
  <p class="lead">می‌توانید یکی را انتخاب کنید یا هر دو را با هم اجرا کنید. حالت سوم آربیتراژ طلا، خودش سوخت لازم برای کاوردکال را می‌سازد.</p>

  <div class="vs">
  <div class="tscroll">
  <table class="vstab">
    <thead>
      <tr>
        <th></th>
        <th class="g"><span class="ic">🟡</span>آربیتراژ صندوق طلا<span class="sb">جابه‌جایی بین صندوق‌های طلا</span></th>
        <th class="b"><span class="ic">🔵</span>کاوردکال<span class="sb">فروش اختیار خرید روی سهام پایه</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>هدف</td>
        <td class="g">افزایش <b>مقدار طلای</b> پرتفو، بدون خروج از بازار طلا</td>
        <td class="b">کسب <b>بهره ثابت</b> از بازار سهام در بازه‌ای مشخص</td>
      </tr>
      <tr>
        <td>بازده هدف</td>
        <td class="g"><span class="kv">۵ تا ۱۰٪ سالانه</span><br><span style="font-size:12.5px;color:var(--slate-500)">به‌صورت طلای اضافه، نه ریال</span></td>
        <td class="b"><span class="kv">۶۰ تا ۱۰۰٪ سالانه</span><br><span style="font-size:12.5px;color:var(--slate-500)">تا سقف حاشیه ریسک هر موقعیت</span></td>
      </tr>
      <tr>
        <td>مناسب برای</td>
        <td class="g">دارنده پرتفوی طلا که نمی‌خواهد از بازار طلا خارج شود</td>
        <td class="b">سرمایه‌گذاری که دنبال جایگزین سپرده و صندوق درآمد ثابت است</td>
      </tr>
      <tr>
        <td><span class="stepn">۱</span>رصد</td>
        <td class="g">قیمت، NAV و حباب همه صندوق‌های طلا لحظه‌ای خوانده می‌شود.</td>
        <td class="b">همه قراردادهای اختیار خرید فعال بازار، لحظه‌ای پایش می‌شوند.</td>
      </tr>
      <tr>
        <td><span class="stepn">۲</span>تحلیل</td>
        <td class="g">حباب هر صندوق نسبت به ترکیب دارایی‌اش سنجیده می‌شود.</td>
        <td class="b">نرخ سود معادل سالانه و حاشیه ریسک هر قرارداد محاسبه می‌شود.</td>
      </tr>
      <tr>
        <td><span class="stepn">۳</span>شناسایی</td>
        <td class="g">صندوق حباب‌دار و صندوق ارزنده مشخص می‌شوند.</td>
        <td class="b">موقعیت‌هایی با بهترین نسبت بازده به ریسک انتخاب می‌شوند.</td>
      </tr>
      <tr>
        <td><span class="stepn">۴</span>اجرا</td>
        <td class="g">سفارش جابه‌جایی بین دو صندوق روی حساب شما ثبت می‌شود.</td>
        <td class="b">خرید سهم و فروش هم‌زمان اختیار خرید روی حساب شما اجرا می‌شود.</td>
      </tr>
      <tr>
        <td>ریسک اصلی</td>
        <td class="g">ریسک بازار طلا حذف نمی‌شود؛ افت قیمت طلا، ارزش ریالی پرتفو را کم می‌کند.</td>
        <td class="b">ریزش سهم پایه به زیر نقطه سربه‌سری، موقعیت را وارد زیان می‌کند.</td>
      </tr>
      <tr>
        <td>افق زمانی</td>
        <td class="g">پیوسته — چند جابه‌جایی در ماه، بسته به فرصت‌های بازار</td>
        <td class="b">دوره‌ای — هر موقعیت با سررسید مشخص، معمولاً ۱۵ تا ۷۰ روز</td>
      </tr>
      <tr>
        <td>سرمایه لازم</td>
        <td class="g">پرتفوی طلای موجود کافی است؛ سرمایه نقدی جدید لازم نیست.</td>
        <td class="b">سرمایه نقدی، یا اعتبار حاصل از گردش پرتفوی طلا (حالت سوم).</td>
      </tr>
      <tr>
        <td>داشبورد مرتبط</td>
        <td class="g"><a class="btn btn-s" href="dashboard-gold.html" style="padding:9px 18px;font-size:13.5px">داشبورد طلا</a></td>
        <td class="b"><a class="btn btn-s" href="dashboard-covered-call.html" style="padding:9px 18px;font-size:13.5px">داشبورد کاوردکال</a></td>
      </tr>
    </tbody>
  </table>
  </div>
  </div>
</div>
</section>

<!-- THREE MODELS -->
<section class="sec">
<div class="wrap">
  <span class="eyebrow">مدل‌های ارائه</span>
  <h2 class="h2">سه حالت اجرا</h2>
  <p class="lead">حالت سوم، همان جایی است که دو محصول به هم وصل می‌شوند.</p>
  <div class="models">
    <div class="model"><div class="n">۱</div><div><h3>پرتفوی مستقل کاوردکال</h3><p>اجرای استراتژی به‌صورت مجزا و بدون وابستگی به پرتفوی طلا؛ مناسب برای سرمایه‌گذاری که هدفش صرفاً کسب بهره ثابت و نسبتاً تضمین‌شده از بازار سهام است.</p></div></div>
    <div class="model"><div class="n">۲</div><div><h3>ترکیبی با پرتفوی طلا</h3><p>بخشی از سرمایه در طلا (با مزایای امنیتی و پوشش تورمی) و بخشی در کاوردکال قرار می‌گیرد؛ این ترکیب باعث می‌شود ریسک کلی پرتفو کاهش و بازدهی متوازن‌تری حاصل شود.</p></div></div>
    <div class="model" style="border-inline-start:4px solid var(--gold-400)"><div class="n">۳</div><div><h3>اجرا از محل اعتبار حاصل از گردش طلا</h3><p>بدون نیاز به سرمایه نقدی جدید: اعتباری که از محل آربیتراژ و گردش صندوق‌های طلا به دست می‌آید (با نرخ ۳۰ تا ۴۰ درصد، در برابر تورم بالای ۶۰ درصد)، مستقیماً وارد استراتژی کاوردکال می‌شود. این حالت عملاً بازدهی را بدون درگیر کردن اصل سرمایه مشتری ایجاد می‌کند.</p></div></div>
  </div>
</div>
</section>

<!-- ONBOARDING -->
<section class="sec" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">شروع همکاری</span>
    <h2 class="h2">از تماس تا اجرا</h2>
    <div class="tl">
      <div class="tli"><b>گام ۱ — جلسه شناخت</b><p>حجم پرتفو، افق زمانی و میزان ریسک‌پذیری شما بررسی می‌شود. رایگان و بدون تعهد.</p></div>
      <div class="tli"><b>گام ۲ — انتخاب استراتژی و مدل</b><p>یکی از دو استراتژی (یا ترکیب هر دو) و یکی از سه مدل بالا انتخاب و پارامترهای اجرا تنظیم می‌شود.</p></div>
      <div class="tli"><b>گام ۳ — اتصال به کارگزاری</b><p>دسترسی معاملاتی محدود روی حساب خودتان تعریف می‌شود. برداشت وجه در این دسترسی وجود ندارد.</p></div>
      <div class="tli" style="padding-bottom:0"><b>گام ۴ — اجرا و گزارش</b><p>الگوریتم فعال می‌شود و گزارش عملکرد ماهانه دریافت می‌کنید. توقف در هر زمان ممکن است.</p></div>
    </div>
  </div>
  <div class="card">
    <h3 style="font-size:16px;margin-bottom:14px">شرایط و نکات</h3>
    <ul class="plist">
      <li>حداقل سرمایه پیشنهادی: <b>{{ مبلغ }}</b> — برای اینکه کارمزد جابه‌جایی‌ها منطقی بماند</li>
      <li>دارایی در حساب کارگزاری خودتان می‌ماند و به حساب ما منتقل نمی‌شود</li>
      <li>دسترسی داده‌شده فقط معاملاتی است؛ امکان برداشت وجه ندارد</li>
      <li>گزارش عملکرد ماهانه با تفکیک هر معامله</li>
      <li>توقف خدمت در هر زمان، بدون جریمه</li>
    </ul>
    <p style="font-size:12.5px;color:var(--slate-500);margin:18px 0 0;line-height:1.9">این خدمت مشمول ضوابط نهاد ناظر بازار سرمایه است. جزئیات قرارداد و مجوزهای مربوطه در جلسه شناخت ارائه می‌شود.</p>
  </div>
</div>
</section>

<!-- LEAD FORM -->
<section class="sec" id="lead">
<div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">درخواست مشاوره</span>
    <h2 class="h2">یک تماس کوتاه، بدون تعهد</h2>
    <p class="lead">فرم را پر کنید؛ در اولین فرصت کاری تماس می‌گیریم و بدون فروش تحت فشار، توضیح می‌دهیم که این خدمت برای شرایط شما مناسب هست یا نه.</p>
    <div style="margin-top:24px;display:grid;gap:12px;font-size:14px;color:var(--slate-600)">
      <div>📞 <b style="color:var(--ink-800)" dir="ltr">۰۲۱-۹۱۰۰۱۲۳۴</b> — شنبه تا چهارشنبه، ۹ تا ۱۷</div>
      <div>✉️ <b style="color:var(--ink-800)" dir="ltr">info@alefcapital.ir</b></div>
    </div>
    <div class="card soft" style="margin-top:24px">
      <h3 style="font-size:15px;margin-bottom:10px">اول داشبوردها را ببینید</h3>
      <p style="font-size:13.5px;color:var(--slate-600);margin:0 0 14px">همان داده‌ای که الگوریتم روی آن تصمیم می‌گیرد، در نسخه مهمان قابل مشاهده است.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <a class="btn btn-gold" href="dashboard-gold.html" style="padding:10px 20px;font-size:13.5px"><ico>🟡</ico>داشبورد طلا</a>
        <a class="btn btn-blue" href="dashboard-covered-call.html" style="padding:10px 20px;font-size:13.5px"><ico>🔵</ico>داشبورد کاوردکال</a>
      </div>
    </div>
  </div>
  <div class="card">
    <form class="form" style="max-width:none" onsubmit="event.preventDefault();this.style.display='none';document.getElementById('done').style.display='block'">
      <div class="fld"><label for="nm">نام و نام خانوادگی</label><input id="nm" type="text" required placeholder="مثلاً حسین احمدی"></div>
      <div class="fld"><label for="ph">شماره موبایل</label><input id="ph" type="tel" required dir="ltr" pattern="09[0-9]{9}" placeholder="09121234567"><div class="hint">فقط برای تماس مشاوره استفاده می‌شود.</div></div>
      <div class="fld"><label for="st">استراتژی مورد نظر</label>
        <select id="st">
          <option>هنوز مطمئن نیستم — راهنمایی می‌خواهم</option>
          <option>آربیتراژ صندوق طلا</option>
          <option>کاوردکال</option>
          <option>ترکیب هر دو</option>
        </select></div>
      <div class="fld"><label for="vol">حجم تقریبی پرتفو (اختیاری)</label>
        <select id="vol">
          <option value="">ترجیح می‌دهم نگویم</option>
          <option>زیر ۱ میلیارد تومان</option>
          <option>۱ تا ۵ میلیارد تومان</option>
          <option>۵ تا ۲۰ میلیارد تومان</option>
          <option>بالای ۲۰ میلیارد تومان</option>
        </select></div>
      <div class="fld"><label for="ms">توضیح کوتاه (اختیاری)</label><textarea id="ms" rows="3" placeholder="مثلاً: پرتفوی طلا دارم و دنبال بازده اضافه هستم"></textarea></div>
      <label class="chk"><input type="checkbox" required> <span><a href="legal-terms.html">شرایط استفاده</a> و <a href="legal-risk.html">افشای ریسک</a> را خوانده‌ام و می‌پذیرم.</span></label>
      <button class="btn btn-p" type="submit">ارسال درخواست</button>
    </form>
    <div id="done" style="display:none;text-align:center;padding:30px 0">
      <div style="font-size:40px;margin-bottom:12px">✓</div>
      <h3 style="font-size:19px;margin-bottom:8px">درخواست شما ثبت شد</h3>
      <p style="color:var(--slate-600);font-size:14.5px;margin:0">در اولین فرصت کاری با شما تماس می‌گیریم.</p>
    </div>
  </div>
</div>
</section>

<div class="riskbar"><div class="wrap">
  ارائه این خدمت مشمول ضوابط و مقررات نهاد ناظر بازار سرمایه است. عملکرد گذشته تضمینی برای بازده آینده نیست و سرمایه‌گذاری در بازار سرمایه با ریسک همراه است.
</div></div>
"""

# ─────────────────────────── WIKI HUB ───────────────────────────
WIKI = """
<section class="phero" style="padding-block:clamp(40px,5vw,68px)">
<div class="wrap">
  <div class="crumb"><a href="index.html">خانه</a> ← دانشنامه</div>
  <span class="eyebrow">دانشنامه</span>
  <h1>مرجع صندوق طلا، آربیتراژ و اختیار معامله</h1>
  <p class="lead">مفاهیم بازار سرمایه ایران، با مثال عددی و داده واقعی. همه مقالات رایگان و بدون نیاز به ثبت‌نام.</p>
  <div class="fld" style="max-width:440px;margin-top:24px"><input type="search" placeholder="🔎 جستجو در دانشنامه…"></div>
</div>
</section>

<section class="sec">
<div class="wrap">
  <div class="wcat" style="grid-template-columns:2fr 1fr">
    <a class="wc" href="wiki-covered-call.html" style="background:var(--surface-2)">
      <em>✨ پیشنهاد مطالعه</em>
      <h3 style="font-size:21px;margin-top:8px">کاوردکال چیست؟ راهنمای کامل با مثال عددی</h3>
      <p style="font-size:14.5px;line-height:2">خرید سهم ۳٬۰۰۰ تومانی و فروش اختیار خرید ۲٬۵۰۰ تومانی به قیمت ۷۰۰ تومان با سررسید ۶۰ روزه، یعنی نرخ سود معادل سالانه ۶۶ درصد و حاشیه ریسک ۲۰ درصد. در این مقاله فرمول، نقطه سربه‌سری و سه سناریوی سررسید را قدم‌به‌قدم می‌بینید — به‌همراه ماشین‌حساب تعاملی.</p>
      <em>مشاهده مقاله ←</em>
    </a>
    <div class="wc" style="background:var(--ink-900);border-color:var(--ink-900)">
      <span class="ic">🧮</span>
      <h3 style="color:#fff">ماشین‌حساب کاوردکال</h3>
      <p style="color:#94A3B8">عدد خودتان را وارد کنید و نرخ معادل سالانه، حاشیه ریسک و نقطه سربه‌سری را ببینید.</p>
      <a class="btn btn-p" href="tools-covered-call.html" style="padding:11px 22px;font-size:14px">باز کردن ابزار</a>
    </div>
  </div>

  <h2 class="h2" style="margin-top:52px">دسته‌بندی موضوعی</h2>
  <div class="wcat">
    <div class="wc">
      <span class="ic">🥇</span>
      <h3>صندوق‌های طلا و ETF</h3>
      <p>از مبانی تا مقایسه صندوق‌ها — ۵ مقاله</p>
      <ul class="wlist">
        <li><a href="#">صندوق طلا چیست و چطور کار می‌کند؟</a></li>
        <li><a href="#">مقایسه کامل صندوق‌های طلای بورس تهران</a></li>
        <li><a href="#">صندوق طلا یا طلای فیزیکی؟ مقایسه شش‌بعدی</a></li>
        <li><a href="#">معافیت مالیاتی و کارمزد صندوق‌های طلا</a></li>
        <li><a href="#">گواهی سپرده سکه و شمش طلا چیست؟</a></li>
      </ul>
    </div>
    <div class="wc">
      <span class="ic">📊</span>
      <h3>آربیتراژ، حباب و NAV</h3>
      <p>قلب محصول اول — ۶ مقاله</p>
      <ul class="wlist">
        <li><a href="#">حباب صندوق طلا چیست و چگونه محاسبه می‌شود؟</a></li>
        <li><a href="#">NAV چیست؟ تفاوت NAV ابطال، صدور و لحظه‌ای</a></li>
        <li><a href="#">آربیتراژ بین صندوق‌های طلا چگونه سود می‌سازد؟</a></li>
        <li><a href="#">چرا حباب صندوق‌ها با هم فرق دارد؟</a></li>
        <li><a href="#">اعتبار کارگزاری از محل گردش معاملاتی</a></li>
        <li><a href="#">Latent NAV و Pure NAV — دو نگاه به ارزش واقعی</a></li>
      </ul>
    </div>
    <div class="wc">
      <span class="ic">📈</span>
      <h3>اختیار معامله و کاوردکال</h3>
      <p>با ماشین‌حساب تعاملی — ۷ مقاله</p>
      <ul class="wlist">
        <li><a href="wiki-covered-call.html">کاوردکال چیست؟ راهنمای کامل</a></li>
        <li><a href="#">نرخ سود معادل سالانه چطور محاسبه می‌شود؟</a></li>
        <li><a href="#">نقطه سربه‌سری — کجا وارد ضرر می‌شویم؟</a></li>
        <li><a href="#">حاشیه ریسک (ITM) در اختیار خرید یعنی چه؟</a></li>
        <li><a href="#">DTM، قیمت اعمال و سررسید</a></li>
        <li><a href="#">چرا شناسایی دستی فرصت‌ها شکست می‌خورد</a></li>
        <li><a href="#">کاوردکال در برابر سپرده بانکی</a></li>
      </ul>
    </div>
    <div class="wc">
      <span class="ic">🛡️</span>
      <h3>مدیریت ریسک و سرمایه</h3>
      <p>۴ مقاله</p>
      <ul class="wlist">
        <li><a href="#">تورم و ارزش واقعی دارایی</a></li>
        <li><a href="#">چگونه پرتفوی طلا و سهام را متوازن کنیم؟</a></li>
        <li><a href="#">ریسک‌های کاوردکال که کمتر گفته می‌شود</a></li>
        <li><a href="#">معاملات الگوریتمی در بورس ایران</a></li>
      </ul>
    </div>
    <div class="wc">
      <span class="ic">📖</span>
      <h3>راهنمای داشبوردها</h3>
      <p>۲ راهنمای گام‌به‌گام</p>
      <ul class="wlist">
        <li><a href="#">راهنمای داشبورد آربیتراژ: از باز کردن تا اولین سیگنال</a></li>
        <li><a href="#">راهنمای دیدبان کاوردکال: فیلترها، ستون‌ها و هشدارها</a></li>
      </ul>
    </div>
    <div class="wc">
      <span class="ic">📰</span>
      <h3>گزارش‌های دوره‌ای</h3>
      <p>تحلیل ماهانه بازار طلا</p>
      <ul class="wlist">
        <li><a href="#">گزارش شهریور ۱۴۰۵ — بازار صندوق‌های طلا</a></li>
        <li><a href="#">گزارش مرداد ۱۴۰۵ — بازار صندوق‌های طلا</a></li>
        <li><a href="#">آرشیو گزارش‌ها</a></li>
      </ul>
    </div>
  </div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
  <div class="ctaband">
    <h2>مفاهیم را یاد گرفتید؟ حالا داده واقعی</h2>
    <p>نبض بازار طلا رایگان و بدون ثبت‌نام باز است.</p>
    <a class="btn btn-gold" href="dashboard-gold.html"><ico>🟡</ico>داشبورد طلا</a>
    <a class="btn btn-blue" href="dashboard-covered-call.html" style="margin-inline-start:8px"><ico>🔵</ico>داشبورد کاوردکال</a>
  </div>
</div>
</section>
"""

# ─────────────────────────── ABOUT ───────────────────────────
ABOUT = """
<section class="phero">
<div class="wrap">
  <div class="crumb"><a href="index.html">خانه</a> ← درباره ما</div>
  <span class="eyebrow">درباره ما</span>
  <h1>تیمی از دانشگاه،<br><span class="grad">پشت یک الگوریتم</span></h1>
  <p class="lead">ما از سمت داده به بازار سرمایه رسیدیم، نه از سمت معامله‌گری. همین باعث شده محصولمان به‌جای وعده سود، ابزار تصمیم بسازد.</p>
</div>
</section>

<section class="sec">
<div class="wrap split" style="align-items:start">
  <div>
    <h2 class="h2">از یک مشاهده ساده شروع شد</h2>
    <p class="lead" style="margin-top:16px">در حال بررسی داده معاملات صندوق‌های طلای بورس تهران بودیم که چیز عجیبی دیدیم: دو صندوق با دارایی پایه تقریباً یکسان، در یک لحظه، با اختلاف قیمتی معنادار معامله می‌شدند. این اختلاف پایدار نبود — باز و بسته می‌شد، گاهی در چند دقیقه.</p>
    <p class="lead" style="margin-top:14px">سوال ساده بود: اگر بشود این اختلاف را لحظه‌ای اندازه گرفت، می‌شود از آن استفاده کرد؟ پاسخ دادن به این سوال، دو سال داده‌کاوی و ساخت زیرساخت لازم داشت. نتیجه‌اش دو داشبوردی است که امروز می‌بینید.</p>
  </div>
  <div class="card soft">
    <h3 style="font-size:16px;margin-bottom:16px">اصولی که به آن پایبندیم</h3>
    <ul class="plist">
      <li><b>هر عدد، یک منبع دارد.</b> بازه زمانی و روش محاسبه هر رقم را منتشر می‌کنیم.</li>
      <li><b>ریسک را پنهان نمی‌کنیم.</b> نقطه سربه‌سری و حاشیه ریسک، به‌اندازه نرخ بازده برجسته‌اند.</li>
      <li><b>توصیه معاملاتی نمی‌دهیم.</b> ابزار می‌سازیم؛ تصمیم با شماست.</li>
      <li><b>محتوای آموزشی پشت دیوار پرداخت نمی‌رود.</b> دانشنامه برای همه باز است.</li>
      <li><b>کلمه «تضمین» را به کار نمی‌بریم.</b> در بازار سرمایه چیزی تضمین‌شده نیست.</li>
    </ul>
  </div>
</div>
</section>

<section class="sec" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <h2 class="h2" style="text-align:center">دو تخصص، یک محصول</h2>
  <p class="lead" style="margin-inline:auto;text-align:center">تیم کوچکی هستیم در تقاطع مهندسی داده و مالی کمّی.</p>
  <div class="team">
    <div class="tm"><div class="av">ح‌ا</div><h3>{{ نام }}</h3><span>مالی کمّی و استراتژی</span><p>طراحی منطق آربیتراژ و مدل‌سازی حباب و ارزش ذاتی صندوق‌ها.</p></div>
    <div class="tm"><div class="av">؟</div><h3>{{ نام }}</h3><span>مهندسی داده</span><p>زیرساخت داده لحظه‌ای، پایگاه داده سری‌زمانی و خط لوله پردازش.</p></div>
    <div class="tm"><div class="av">؟</div><h3>{{ نام }}</h3><span>محصول و تجربه کاربری</span><p>تبدیل خروجی مدل‌ها به داشبوردی که بشود در چند ثانیه خواند.</p></div>
  </div>
  <p style="text-align:center;font-size:12.5px;color:var(--slate-500);margin-top:20px">نام‌ها و عکس‌های واقعی تیم را قبل از انتشار جایگزین کنید — گرید تیم بدون چهره واقعی، اثر معکوس دارد.</p>
</div>
</section>

<section class="sec">
<div class="wrap split" style="align-items:start">
  <div>
    <h2 class="h2">مسیری که آمده‌ایم</h2>
    <div class="tl">
      <div class="tli"><b>۱۴۰۲</b><p>شروع تحلیل داده معاملات صندوق‌های طلای بورس تهران و مشاهده اولین الگوهای اختلاف قیمت.</p></div>
      <div class="tli"><b>۱۴۰۳</b><p>ساخت زیرساخت داده لحظه‌ای و اولین نسخه محاسبه‌گر حباب و ارزش ذاتی.</p></div>
      <div class="tli"><b>۱۴۰۴</b><p>اجرای آزمایشی الگوریتم آربیتراژ روی حساب‌های واقعی و انتشار اولین گزارش عملکرد.</p></div>
      <div class="tli" style="padding-bottom:0"><b>۱۴۰۵</b><p>افزودن داشبورد کاوردکال و عرضه عمومی هر دو محصول به‌صورت اشتراکی.</p></div>
    </div>
  </div>
  <div class="card">
    <h3 style="font-size:16px;margin-bottom:14px">مجوزها و شفافیت</h3>
    <p style="font-size:14.5px;color:var(--slate-600);line-height:2;margin:0 0 14px">الف کپیتال یک ارائه‌دهنده ابزار تحلیلی است. محصولات اشتراکی ما داده و داشبورد ارائه می‌کنند و توصیه سرمایه‌گذاری محسوب نمی‌شوند.</p>
      <p style="font-size:14.5px;color:var(--slate-600);line-height:2;margin:0">خدمت مدیریت پرتفوی، که در آن الگوریتم روی حساب مشتری اجرا می‌شود، مشمول ضوابط نهاد ناظر بازار سرمایه است و جزئیات مجوزهای مربوطه در جلسه شناخت ارائه می‌شود.</p>
    <div style="margin-top:18px;padding-top:18px;border-top:1px solid var(--border);font-size:13.5px;color:var(--slate-600);line-height:2">
      شماره ثبت: <b>{{ شماره }}</b><br>
      شناسه ملی: <b>{{ شناسه }}</b><br>
      نشانی: <b>{{ نشانی }}</b>
    </div>
  </div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
  <div class="ctaband">
    <h2>می‌خواهید بیشتر بدانید؟</h2>
    <p>سوالتان درباره روش‌شناسی، داده یا محصول را بپرسید.</p>
    <a class="btn btn-p" href="contact.html">تماس با ما</a>
    <a class="btn btn-s" href="performance.html" style="color:#DBE6FE;border-color:#334155;margin-inline-start:8px">گزارش عملکرد</a>
  </div>
</div>
</section>
"""

# ─────────────────────────── FAQ ───────────────────────────
FAQ = """
<section class="phero">
<div class="wrap">
  <div class="crumb"><a href="index.html">خانه</a> ← سوالات متداول</div>
  <span class="eyebrow">راهنما</span>
  <h1>آنچه بیشتر از ما می‌پرسند</h1>
  <p class="lead">اگر پاسخ سوالتان اینجا نبود، از <a href="contact.html">صفحه تماس</a> بپرسید.</p>
</div>
</section>

<section class="sec">
<div class="wrap" style="max-width:880px">
  <h2 class="h2" style="font-size:20px;margin-bottom:16px">🧩 محصول و قابلیت‌ها</h2>
  <div class="faq" style="margin:0 0 40px">
    <details open><summary>الف کپیتال دقیقاً چه چیزی می‌فروشد؟</summary><p>دو داشبورد اشتراکی: یکی برای پایش حباب و NAV صندوق‌های طلای بورس تهران، و یکی برای پایش فرصت‌های کاوردکال در بازار اختیار معامله. آنچه دریافت می‌کنید داده و ابزار تحلیل است؛ تصمیم و اجرای معامله با خودتان.</p></details>
    <details><summary>آیا داشبورد به‌جای من معامله می‌کند؟</summary><p>خیر. اجرای خودکار روی حساب کارگزاری، یک <a href="services.html">خدمت جداگانه</a> است و بخشی از اشتراک نیست.</p></details>
    <details><summary>آیا سیگنال خرید و فروش می‌دهید؟</summary><p>خیر. ما موقعیت‌ها را بر اساس معیارهای عددی (حباب، نرخ معادل سالانه، حاشیه ریسک) مرتب و رنگ‌بندی می‌کنیم، اما توصیه خرید یا فروش نماد مشخصی نمی‌دهیم.</p></details>
    <details><summary>برای استفاده باید حساب کارگزاری خاصی داشته باشم؟</summary><p>خیر. داشبوردها مستقل از کارگزاری شما کار می‌کنند و فقط داده بازار را نمایش می‌دهند.</p></details>
    <details><summary>روی موبایل هم کار می‌کند؟</summary><p>بله. هر دو داشبورد برای موبایل بهینه شده‌اند، هرچند جدول‌های بزرگ روی صفحه بزرگ‌تر راحت‌تر خوانده می‌شوند.</p></details>
  </div>

  <h2 class="h2" style="font-size:20px;margin-bottom:16px">📊 داده و دقت</h2>
  <div class="faq" style="margin:0 0 40px">
    <details><summary>داده از کجا می‌آید؟</summary><p>مستقیماً از تابلوی معاملات بورس تهران و بورس کالا. ارزش ذاتی صندوق‌ها را از ترکیب دارایی اعلامی و قیمت لحظه‌ای دارایی‌های پایه بازسازی می‌کنیم، نه از NAV تأخیری منتشرشده.</p></details>
    <details><summary>تأخیر داده چقدر است؟</summary><p>در پلن‌های پولی، زیر یک ثانیه. برای کاربر مهمان و پلن رایگان، ۱۵ دقیقه. مهر زمان هر داده همیشه روی صفحه نمایش داده می‌شود.</p></details>
    <details><summary>خارج از ساعت معاملات چه می‌بینم؟</summary><p>داده کامل آخرین روز معاملاتی، برای همه کاربران و بدون محدودیت. نشان «زنده» در این حالت به «آخرین داده معاملاتی» تغییر می‌کند.</p></details>
    <details><summary>اگر داده اشتباه باشد چه؟</summary><p>اگر مغایرتی دیدید به ما اطلاع دهید. ما داده را از منبع رسمی می‌خوانیم، اما مسئولیت تصمیم‌های معاملاتی بر پایه آن با کاربر است — این در <a href="legal-terms.html">شرایط استفاده</a> تصریح شده.</p></details>
  </div>

  <h2 class="h2" style="font-size:20px;margin-bottom:16px">💳 اشتراک و پرداخت</h2>
  <div class="faq" style="margin:0 0 40px">
    <details><summary>دوره رایگان چطور کار می‌کند؟</summary><p>۷ روز، بدون نیاز به کارت بانکی. در پایان دوره، اگر اشتراک نخرید، حساب شما به پلن پایه رایگان برمی‌گردد و هیچ مبلغی کسر نمی‌شود.</p></details>
    <details><summary>امکان ارتقا یا تنزل پلن هست؟</summary><p>بله. ارتقا فوری اعمال می‌شود و مبلغ باقی‌مانده پلن قبلی به‌صورت اعتبار کسر می‌گردد. تنزل در پایان دوره جاری اعمال می‌شود.</p></details>
    <details><summary>فاکتور رسمی صادر می‌شود؟</summary><p>بله، برای همه پلن‌ها. در بخش «اشتراک و فاکتورها» در حساب کاربری قابل دانلود است.</p></details>
    <details><summary>امکان بازگشت وجه وجود دارد؟</summary><p>تا ۷ روز پس از خرید، در صورت عدم استفاده مؤثر، مبلغ بازگردانده می‌شود.</p></details>
    <details><summary>برای تیم و سازمان چه گزینه‌ای دارید؟</summary><p>دسترسی چندکاربره و گزارش اختصاصی. از <a href="services.html">صفحه خدمات</a> درخواست مشاوره ثبت کنید.</p></details>
  </div>

  <h2 class="h2" style="font-size:20px;margin-bottom:16px">⚠️ ریسک</h2>
  <div class="faq">
    <details><summary>آیا این استراتژی‌ها بدون ریسک هستند؟</summary><p>خیر. هیچ استراتژی در بازار سرمایه بدون ریسک نیست. آربیتراژ صندوق طلا ریسک بازار طلا را حذف نمی‌کند و کاوردکال در صورت ریزش سهم به زیر نقطه سربه‌سری وارد زیان می‌شود. <a href="legal-risk.html">افشای کامل ریسک</a> را بخوانید.</p></details>
    <details><summary>ارقام بازده اعلام‌شده تضمین‌شده‌اند؟</summary><p>خیر. این ارقام بازده تاریخی استراتژی در بازه‌ای مشخص است و تضمینی برای آینده نیست. روش محاسبه و محدودیت‌ها در <a href="performance.html">صفحه عملکرد</a> آمده.</p></details>
    <details><summary>اگر بازار طلا ریزش کند چه می‌شود؟</summary><p>استراتژی آربیتراژ، مقدار طلای شما را افزایش می‌دهد، نه ارزش ریالی آن را. اگر قیمت طلا افت کند، ارزش پرتفوی شما هم افت می‌کند — این ریسک با آربیتراژ حذف نمی‌شود.</p></details>
  </div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
  <div class="ctaband">
    <h2>سوال دیگری دارید؟</h2>
    <p>بپرسید — معمولاً در کمتر از یک روز کاری پاسخ می‌دهیم.</p>
    <a class="btn btn-p" href="contact.html">تماس با ما</a>
  </div>
</div>
</section>
"""

# ─────────────────────────── CONTACT ───────────────────────────
CONTACT = """
<section class="phero">
<div class="wrap">
  <div class="crumb"><a href="index.html">خانه</a> ← تماس با ما</div>
  <span class="eyebrow">تماس</span>
  <h1>سریع‌ترین راه، یک تماس تلفنی است</h1>
  <p class="lead">شنبه تا چهارشنبه، ۹ تا ۱۷. اگر ترجیح می‌دهید ما تماس بگیریم، فرم پایین را پر کنید.</p>
  <div class="cchan">
    <div class="cc2"><span>📞</span><h3>تلفن</h3><p>پاسخگویی مستقیم در ساعات کاری</p><a href="tel:+982191001234" dir="ltr">۰۲۱-۹۱۰۰۱۲۳۴</a></div>
    <div class="cc2"><span>✉️</span><h3>ایمیل</h3><p>برای سوالات فنی و پشتیبانی</p><a href="mailto:info@alefcapital.ir" dir="ltr">info@alefcapital.ir</a></div>
    <div class="cc2"><span>💬</span><h3>تلگرام</h3><p>کانال تحلیل و اطلاعیه‌های بازار</p><a href="#" dir="ltr">@alefcapital</a></div>
  </div>
</div>
</section>

<section class="sec">
<div class="wrap split" style="align-items:start">
  <div class="card">
    <h3 style="font-size:18px;margin-bottom:16px">ما تماس بگیریم</h3>
    <form class="form" style="max-width:none" onsubmit="event.preventDefault();this.style.display='none';document.getElementById('cdone').style.display='block'">
      <div class="fld"><label for="cn">نام و نام خانوادگی</label><input id="cn" type="text" required></div>
      <div class="fld"><label for="cp">شماره موبایل</label><input id="cp" type="tel" required dir="ltr" pattern="09[0-9]{9}" placeholder="09121234567"></div>
      <div class="fld"><label for="ct">موضوع</label>
        <select id="ct">
          <option>سوال درباره محصول و اشتراک</option>
          <option>پشتیبانی فنی</option>
          <option>خرید سازمانی / مدیریت پرتفوی</option>
          <option>همکاری و رسانه</option>
          <option>سایر</option>
        </select></div>
      <div class="fld"><label for="cm">پیام</label><textarea id="cm" rows="4" required></textarea></div>
      <label class="chk"><input type="checkbox" required> <span><a href="legal-privacy.html">حریم خصوصی</a> را خوانده‌ام و می‌پذیرم.</span></label>
      <button class="btn btn-p" type="submit">ارسال پیام</button>
    </form>
    <div id="cdone" style="display:none;text-align:center;padding:30px 0">
      <div style="font-size:40px;margin-bottom:12px">✓</div>
      <h3 style="font-size:19px;margin-bottom:8px">پیام شما ثبت شد</h3>
      <p style="color:var(--slate-600);font-size:14.5px;margin:0">معمولاً در کمتر از یک روز کاری پاسخ می‌دهیم.</p>
    </div>
  </div>
  <div>
    <h2 class="h2">قبل از تماس، شاید اینجا باشد</h2>
    <p class="lead" style="margin-top:14px">بیشتر سوالات رایج در صفحه سوالات متداول پاسخ داده شده — از تأخیر داده و تفاوت پلن‌ها تا شرایط بازگشت وجه.</p>
    <a class="btn btn-s" href="faq.html" style="margin-top:20px">سوالات متداول</a>

    <div class="card soft" style="margin-top:28px">
      <h3 style="font-size:16px;margin-bottom:12px">نشانی دفتر</h3>
      <p style="font-size:14.5px;color:var(--slate-600);line-height:2;margin:0">{{ نشانی کامل }}</p>
      <div style="margin-top:16px;height:180px;border-radius:12px;background:var(--surface-3);display:grid;place-items:center;color:var(--slate-400);font-size:13.5px">جای نقشه</div>
    </div>
  </div>
</div>
</section>
"""
