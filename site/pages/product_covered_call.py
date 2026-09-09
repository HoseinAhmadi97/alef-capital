# -*- coding: utf-8 -*-
"""Covered-call dashboard — product introduction page."""
import paywall

HTML = """
<!-- HERO -->
<section class="phero">
<div class="wrap">
  <div class="crumb"><a href="index.html">خانه</a> ← <a href="index.html#products">محصولات</a> ← کاوردکال</div>
  <div class="hgrid">
    <div>
      <span class="eyebrow"><span class="dot"></span>محصول ۲ — داشبورد اشتراکی</span>
      <h1>بهره ثابت سالانه،<br><span class="grad">بدون خروج از بازار سرمایه</span></h1>
      <p class="lead">استراتژی کاوردکال امکان دستیابی به بهره ثابت سالانه ۶۰ تا ۱۰۰ درصد را با ریسک پایین فراهم می‌کند — فرصتی که در بازار سرمایه ایران کمتر شناخته شده است. داشبورد ما هزاران قرارداد اختیار خرید را می‌سنجد و بهترین نسبت بازده به ریسک را بیرون می‌کشد.</p>
      <div class="pcta">
        <a class="btn btn-blue" href="dashboard-covered-call.html"><ico>📈</ico>ورود به داشبورد کاوردکال</a>
        <a class="btn btn-s" href="#calc">دیدن مثال عددی</a>
      </div>
    </div>
    <div class="card">
      <div class="lch"><span class="lbl">بهترین فرصت‌های امروز</span><span class="live"><i></i>زنده</span></div>
      <div class="lcv"><span class="big num" id="ccN">۱۲</span><span class="lcu">موقعیت با نرخ معادل بالای ۵۰٪</span></div>
      <table class="opt"><tbody id="ccBody"></tbody></table>
      <div class="lcbar"><span>آخرین به‌روزرسانی <b id="ccClock">۱۷:۳۱:۰۴</b></span></div>
    </div>
  </div>
</div>
</section>

<!-- PROBLEM -->
<section class="sec" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap split">
  <div>
    <span class="eyebrow">مسئله</span>
    <h2 class="h2">بهره ثابت متداول، از تورم عقب می‌ماند</h2>
    <p class="lead">یکی از روش‌های متداول سرمایه‌گذاری بدون ریسک، دریافت بهره ثابت سالانه از ابزارهایی مانند سپرده بانکی، صندوق‌های درآمد ثابت قابل معامله در بورس یا اوراق اخزاست. با این حال، نرخ بهره سالانه این ابزارها معمولاً از نرخ تورم عقب می‌ماند و در نهایت به کاهش ارزش واقعی دارایی منجر می‌شود.</p>
  </div>
  <div class="card">
    <h3 style="font-size:15px;margin-bottom:16px">نرخ بهره سالانه — مقایسه</h3>
    <div style="display:grid;gap:14px">
      <div><div style="display:flex;justify-content:space-between;font-size:13.5px;margin-bottom:5px"><span>سپرده بانکی</span><b class="num">‎۲۳٪</b></div><div style="height:9px;background:var(--surface-3);border-radius:99px"><i style="display:block;height:100%;width:23%;background:var(--slate-400);border-radius:99px"></i></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:13.5px;margin-bottom:5px"><span>صندوق درآمد ثابت</span><b class="num">‎۳۰٪</b></div><div style="height:9px;background:var(--surface-3);border-radius:99px"><i style="display:block;height:100%;width:30%;background:var(--slate-400);border-radius:99px"></i></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:13.5px;margin-bottom:5px"><span>نرخ تورم</span><b class="num" style="color:var(--down)">‎۶۰٪+</b></div><div style="height:9px;background:var(--surface-3);border-radius:99px"><i style="display:block;height:100%;width:60%;background:#DC2626;border-radius:99px"></i></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:13.5px;margin-bottom:5px"><span><b>کاوردکال</b></span><b class="num" style="color:var(--gold-700)">‎۶۰ تا ۱۰۰٪</b></div><div style="height:9px;background:var(--surface-3);border-radius:99px"><i style="display:block;height:100%;width:85%;background:var(--grad-gold);border-radius:99px"></i></div></div>
    </div>
    <p style="font-size:11.5px;color:var(--slate-400);margin:16px 0 0;line-height:1.8">ارقام تقریبی و برای مقایسه مفهومی است. نرخ کاوردکال به موقعیت، سررسید و حاشیه ریسک انتخابی بستگی دارد و تضمین‌شده نیست.</p>
  </div>
</div>
</section>

<!-- WHAT IS IT -->
<section class="sec">
<div class="wrap">
  <span class="eyebrow">تعریف</span>
  <h2 class="h2">کاوردکال چیست؟</h2>
  <p class="lead" style="max-width:760px">کاوردکال به موقعیتی گفته می‌شود که با <b>خرید یک سهم</b> و هم‌زمان <b>فروش اختیار خرید (Call) همان سهم</b> ساخته می‌شود. با این کار می‌توان تا حد زیادی جلوی ضرر ناشی از ریزش سهم را گرفت و در یک بازه زمانی مشخص به سود ثابت و از پیش تعیین‌شده دست یافت.</p>

  <div class="models" style="grid-template-columns:1fr;margin-top:28px">
    <div class="model" style="grid-template-columns:44px 1fr 1fr;gap:20px">
      <div class="n">+</div>
      <div><h3>خرید سهم پایه</h3><p>سهم را در قیمت روز می‌خرید و در پرتفوی شما می‌ماند.</p></div>
      <div><h3>فروش اختیار خرید</h3><p>در ازای آن، مبلغی نقدی («پرمیوم») همین حالا دریافت می‌کنید.</p></div>
    </div>
  </div>
</div>
</section>

<!-- NUMERIC EXAMPLE -->
<section class="sec" id="calc" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <span class="eyebrow">مثال عددی</span>
  <h2 class="h2">یک موقعیت واقعی، قدم به قدم</h2>
  <p class="lead">فرض کنید موقعیتی با این شرایط باز می‌کنیم: خرید سهم به قیمت ۳٬۰۰۰ تومان و هم‌زمان فروش اختیار خرید با سررسید ۶۰ روزه و قیمت اعمال ۲٬۵۰۰ تومان، به قیمت ۷۰۰ تومان.</p>

  <div class="split" style="margin-top:30px;align-items:start">
    <div class="fbox">
      <h3>مشخصات موقعیت</h3>
      <div class="tscroll"><table class="ftab">
        <thead><tr><th style="text-align:right">مشخصه</th><th>نماد</th><th style="text-align:left">مقدار</th></tr></thead>
        <tbody>
          <tr><td>قیمت خرید سهم</td><td class="k">P</td><td style="text-align:left">۳٬۰۰۰ تومان</td></tr>
          <tr><td>قیمت اعمال</td><td class="k">K</td><td style="text-align:left">۲٬۵۰۰ تومان</td></tr>
          <tr><td>قیمت اختیار فروخته‌شده</td><td class="k">C</td><td style="text-align:left">۷۰۰ تومان</td></tr>
          <tr><td>مدت تا سررسید</td><td class="k">DTM</td><td style="text-align:left">۶۰ روز</td></tr>
        </tbody>
      </table></div>
      <div class="formula">
        <div class="lbl">نرخ سود معادل سالانه</div>
        <div class="eq">Rate = ( K / (P − C) ) <sup>365 / DTM</sup> − 1</div>
        <div class="eq">= ( 2500 / 2300 ) <sup>365 / 60</sup> − 1 = <b style="color:#4ADE80">66%</b></div>
      </div>
      <div class="formula">
        <div class="lbl">حاشیه ریسک</div>
        <div class="eq">P / K − 1 = 3000 / 2500 − 1 = <b style="color:#FFD873">20%</b></div>
      </div>
      <p style="margin:0;font-size:12.5px">نقطه سربه‌سری = P − C = <b style="color:#fff">۲٬۳۰۰ تومان</b></p>
    </div>

    <div class="scen" style="margin-top:0">
      <div style="background:rgba(22,163,74,.10);border-inline-start:3px solid #16A34A;color:var(--ink-700)">
        🟢 <b style="color:var(--ink-900)">حالت مطلوب</b> — تا زمانی که قیمت سهم در روز سررسید بالای ۲٬۵۰۰ تومان بماند (یعنی ریزشی معادل ۲۰ درصد یا بیشتر در بازه ۶۰ روزه رخ ندهد)، نرخ سود معادل <b style="color:var(--up-text)">۶۶ درصد سالانه</b> محقق می‌شود.
      </div>
      <div style="background:rgba(240,180,41,.12);border-inline-start:3px solid var(--gold-400);color:var(--ink-700)">
        🟡 <b style="color:var(--ink-900)">حالت ریزش سهم</b> — اگر قیمت سهم زیر ۲٬۵۰۰ تومان (قیمت اعمال) بیاید، خریدار اختیار سهم را با قیمت اعمال خریداری نخواهد کرد و سهم در پرتفو باقی می‌ماند.
      </div>
      <div style="background:rgba(220,38,38,.09);border-inline-start:3px solid #DC2626;color:var(--ink-700)">
        🔴 <b style="color:var(--ink-900)">نقطه سربه‌سری</b> — تا زمانی که قیمت سهم بالای <b>۲٬۳۰۰ تومان</b> (قیمت اعمال منهای قیمت اختیار فروخته‌شده) بماند، ضرری متوجه پرتفو نخواهد شد و صرفاً سود موقعیت از دست می‌رود. تنها با ریزش زیر این سطح، موقعیت وارد زیان می‌شود.
      </div>
    </div>
  </div>

  <div class="card" style="margin-top:22px">
    <h3 style="font-size:17px;margin-bottom:4px">نمودار سود و زیان در سررسید</h3>
    <p style="font-size:13px;color:var(--slate-500);margin:0 0 18px">محور افقی: قیمت سهم در روز سررسید — محور عمودی: سود یا زیان موقعیت</p>
    <svg viewBox="0 0 800 380" style="width:100%;height:auto;display:block">
      <line x1="60" y1="40" x2="60" y2="345" stroke="#CBD5E1" stroke-width="1"/>
      <line x1="60" y1="168.9" x2="770" y2="168.9" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect x="340" y="40" width="233.3" height="305" fill="rgba(240,180,41,.10)"/>
      <path d="M60 330 L246.7 168.9" stroke="#DC2626" stroke-width="3" fill="none" stroke-linecap="round"/>
      <path d="M246.7 168.9 L340 88.3" stroke="#64748B" stroke-width="3" fill="none" stroke-linecap="round"/>
      <path d="M340 88.3 L770 88.3" stroke="#16A34A" stroke-width="3.5" fill="none" stroke-linecap="round"/>
      <line x1="246.7" y1="60" x2="246.7" y2="345" stroke="#94A3B8" stroke-width="1" stroke-dasharray="4 4"/>
      <line x1="340" y1="60" x2="340" y2="345" stroke="#C9861A" stroke-width="1.5" stroke-dasharray="5 4"/>
      <line x1="573.3" y1="60" x2="573.3" y2="345" stroke="#94A3B8" stroke-width="1" stroke-dasharray="4 4"/>
      <circle cx="246.7" cy="168.9" r="6" fill="#DC2626"/>
      <circle cx="340" cy="88.3" r="7" fill="#16A34A"/>
      <text x="762" y="76" font-size="19" fill="#0F7233" font-weight="800" text-anchor="end" direction="rtl" font-family="Vazirmatn">سود سالانه ۶۶٪</text>
      <text x="246.7" y="368" font-size="16" fill="#475569" text-anchor="middle" font-family="Vazirmatn">۲٬۳۰۰</text>
      <text x="246.7" y="52" font-size="15" fill="#DC2626" text-anchor="middle" font-family="Vazirmatn">نقطه سربه‌سری</text>
      <text x="340" y="368" font-size="16" fill="#8A5A08" font-weight="700" text-anchor="middle" font-family="Vazirmatn">۲٬۵۰۰</text>
      <text x="340" y="30" font-size="15" fill="#8A5A08" text-anchor="middle" font-family="Vazirmatn">قیمت اعمال</text>
      <text x="573.3" y="368" font-size="16" fill="#475569" text-anchor="middle" font-family="Vazirmatn">۳٬۰۰۰</text>
      <text x="573.3" y="52" font-size="15" fill="#475569" text-anchor="middle" font-family="Vazirmatn">قیمت فعلی</text>
      <text x="456" y="330" font-size="15" fill="#8A5A08" text-anchor="middle" font-family="Vazirmatn">حاشیه ریسک ۲۰٪</text>
      <text x="50" y="175" font-size="15" fill="#64748B" text-anchor="end" font-family="Vazirmatn">۰</text>
      <text x="50" y="50" font-size="14" fill="#94A3B8" text-anchor="end" font-family="Vazirmatn">سود</text>
      <text x="50" y="340" font-size="14" fill="#94A3B8" text-anchor="end" font-family="Vazirmatn">زیان</text>
    </svg>
  </div>
</div>
</section>

<!-- DASHBOARD -->
<section class="dark sec">
<div class="wrap">
  <span class="eyebrow" style="background:rgba(240,180,41,.14)">پیش‌نمایش داشبورد</span>
  <h2 class="h2">دیدبان قراردادهای اختیار خرید</h2>
  <p class="lead">همه قراردادهای فعال در یک جدول، با نرخ معادل سالانه و حاشیه ریسک محاسبه‌شده. فیلتر بگذارید، مرتب کنید، هشدار تعریف کنید.</p>
  <div class="panel" style="margin-top:26px">
    <div class="pbar"><i></i><i></i><i></i></div>
    <div class="tscroll">
    <table>
      <thead><tr><th>نماد</th><th>سهم پایه</th><th>DTM</th><th>قیمت اعمال</th><th>حاشیه ریسک</th><th>سود دوره‌ای</th><th>نرخ معادل سالانه</th></tr></thead>
      <tbody>
        <tr><td>ضستا۳۰۱۰</td><td>شستا</td><td>۱۵</td><td>۱,۴۰۰</td><td><span class="chip neu">۳۳٫۸٪</span></td><td>۲٫۲٪</td><td><span class="chip up">۶۹٫۴٪</span></td></tr>
        <tr><td>ضشنا۶۰۴۹</td><td>شنا</td><td>۲۰</td><td>۶,۰۰۰</td><td><span class="chip neu">۲۸٫۱٪</span></td><td>۲٫۸٪</td><td><span class="chip up">۶۶٫۳٪</span></td></tr>
        <tr><td>ضخود۶۰۵۵</td><td>خودرو</td><td>۵۷</td><td>۳,۰۰۰</td><td><span class="chip neu">۳۴٫۶٪</span></td><td>۸٫۱٪</td><td><span class="chip up">۶۴٫۴٪</span></td></tr>
        <tr><td>ضملی۳۰۵۸</td><td>ملی</td><td>۴۳</td><td>۱,۲۶۰</td><td><span class="chip neu">۳۰٫۵٪</span></td><td>۵٫۹٪</td><td><span class="chip up">۶۲٫۴٪</span></td></tr>
        <tr><td>ضفولا۶۰۳۲</td><td>فولاد</td><td>۲۹</td><td>۴,۵۰۰</td><td><span class="chip neu">۲۶٫۲٪</span></td><td>۳٫۷٪</td><td><span class="chip up">۵۷٫۳٪</span></td></tr>
        <tr@@IFLOCK@@ class="lock"@@END@@><td>ضهرم۷۰۲۲</td><td>اهرم</td><td>۲۶</td><td>۲,۱۰۰</td><td><span class="chip neu">۲۴٫۹٪</span></td><td>۳٫۲٪</td><td><span class="chip up">۵۵٫۵٪</span></td></tr>
        <tr@@IFLOCK@@ class="lock"@@END@@><td>ضفزر۱۰۱۳</td><td>فزر</td><td>۷۱</td><td>۷,۵۰۰</td><td><span class="chip neu">۲۲٫۴٪</span></td><td>۸٫۷٪</td><td><span class="chip up">۵۳٫۹٪</span></td></tr>
      </tbody>
    </table>
    </div>
@@IFLOCK@@    <div class="lockmsg">🔒 <b>۳۶۱ قرارداد دیگر</b>، فیلتر سفارشی، هشدار و نمودار سود و زیان — با پلن حرفه‌ای.</div>@@END@@
  </div>

  <div class="feat4" style="margin-top:30px">
    <div class="fx" style="background:var(--dark-panel);border-color:var(--dark-border)">
      <b>۰۱</b><h3 style="color:#fff">دیدبان کامل قراردادها</h3>
      <p style="color:#94A3B8">همه قراردادهای فعال کال در یک جدول، با فیلتر و مرتب‌سازی آزاد روی هر ستون.</p>
    </div>
    <div class="fx" style="background:var(--dark-panel);border-color:var(--dark-border)">
      <b>۰۲</b><h3 style="color:#fff">محاسبه خودکار نرخ و ریسک</h3>
      <p style="color:#94A3B8">نرخ سود معادل سالانه و حاشیه ریسک هر قرارداد، لحظه‌ای محاسبه و رنگ‌بندی می‌شود.</p>
    </div>
    <div class="fx" style="background:var(--dark-panel);border-color:var(--dark-border)">
      <b>۰۳</b><h3 style="color:#fff">نمودار سود و زیان</h3>
      <p style="color:#94A3B8">قبل از ورود، نقطه سربه‌سری و بیشینه سود هر موقعیت را روی نمودار ببینید.</p>
    </div>
    <div class="fx" style="background:var(--dark-panel);border-color:var(--dark-border)">
      <b>۰۴</b><h3 style="color:#fff">پایش پرتفوی موجود</h3>
      <p style="color:#94A3B8">سررسید، فاصله تا نقطه سربه‌سری و وضعیت لحظه‌ای هر موقعیت باز شما.</p>
    </div>
  </div>
</div>
</section>

<!-- WHY A TOOL -->
<section class="sec">
<div class="wrap split">
  <div>
    <span class="eyebrow">چرا دستی نمی‌شود</span>
    <h2 class="h2">فرصت‌های خوب، محدود و کمیاب‌اند</h2>
    <p class="lead">تعداد قراردادهای اختیار خرید با قیمت‌های اعمال و سررسیدهای متفاوت بسیار زیاد است. موقعیت‌های جذاب در این انبوه، <b>محدود و کمیاب</b> هستند و شناسایی و ورود به‌موقع به آن‌ها به‌صورت دستی عملاً امکان‌پذیر نیست.</p>
    <p class="lead" style="margin-top:14px">شناسایی موقعیت سودساز، نیازمند ابزار جمع‌آوری و دانش تحلیل داده برای ساخت داشبوردهای مالی است؛ تا در هر لحظه بتوان بهترین موقعیت — کمترین ریسک با بالاترین نرخ بازدهی — را شناسایی کرد.</p>
  </div>
  <div class="card soft">
    <div style="display:grid;gap:18px">
      <div><div class="num" style="font-size:34px;font-weight:800;color:var(--gold-700)">۳۶۸</div><div style="font-size:14px;color:var(--slate-600)">قرارداد فعال در دیدبان</div></div>
      <div style="height:1px;background:var(--border)"></div>
      <div><div class="num" style="font-size:34px;font-weight:800;color:var(--gold-700)">۱۲</div><div style="font-size:14px;color:var(--slate-600)">موقعیت با نرخ معادل بالای ۵۰٪ — کمتر از ۴ درصد کل بازار</div></div>
      <div style="height:1px;background:var(--border)"></div>
      <div><div class="num" style="font-size:34px;font-weight:800;color:var(--gold-700)">&lt; ۱ ثانیه</div><div style="font-size:14px;color:var(--slate-600)">تأخیر به‌روزرسانی در پلن حرفه‌ای</div></div>
    </div>
  </div>
</div>
</section>

<!-- THREE MODELS -->
<section class="sec" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <span class="eyebrow">مدل‌های اجرا</span>
  <h2 class="h2">سه حالت قابل ارائه به مشتری</h2>
  <p class="lead">این استراتژی در سه حالت قابل اجراست. حالت سوم، مزیت ترکیبی دو محصول ماست.</p>
  <div class="models">
    <div class="model">
      <div class="n">۱</div>
      <div><h3>پرتفوی مستقل کاوردکال</h3><p>اجرای استراتژی به‌صورت مجزا و بدون وابستگی به پرتفوی طلا؛ مناسب برای سرمایه‌گذاری که هدفش صرفاً کسب بهره ثابت و نسبتاً تضمین‌شده از بازار سهام است.</p></div>
    </div>
    <div class="model">
      <div class="n">۲</div>
      <div><h3>ترکیبی با پرتفوی طلا</h3><p>بخشی از سرمایه در طلا (با مزایای امنیتی و پوشش تورمی) و بخشی در کاوردکال قرار می‌گیرد؛ این ترکیب باعث می‌شود ریسک کلی پرتفو کاهش و بازدهی متوازن‌تری حاصل شود.</p></div>
    </div>
    <div class="model">
      <div class="n">۳</div>
      <div><h3>اجرا از محل اعتبار حاصل از گردش طلا</h3><p>بدون نیاز به سرمایه نقدی جدید: اعتباری که از محل آربیتراژ و گردش صندوق‌های طلا به دست می‌آید، مستقیماً وارد استراتژی کاوردکال می‌شود. این حالت عملاً بازدهی را بدون درگیر کردن اصل سرمایه مشتری ایجاد می‌کند. <a href="product-gold.html">درباره داشبورد آربیتراژ ←</a></p></div>
    </div>
  </div>
  <div class="card" style="margin-top:20px;font-size:14px;color:var(--slate-600)">
    <b style="color:var(--ink-800)">مرز محصول:</b> اشتراک این محصول، <b>داشبورد و داده</b> در اختیار شما می‌گذارد؛ ساخت و مدیریت موقعیت با خودتان است.
    اجرای این سه مدل روی حساب کارگزاری، خدمت جداگانه است: <a href="services.html">مدیریت پرتفوی ←</a>
  </div>
</div>
</section>

<!-- FAQ -->
<section class="sec">
<div class="wrap">
  <h2 class="h2" style="text-align:center">سوالات متداول این محصول</h2>
  <div class="faq">
    <details open><summary>نرخ سود معادل سالانه یعنی چه؟</summary><p>شاخصی است که نشان می‌دهد اگر نرخ سود به‌دست‌آمده در یک بازه زمانی کوتاه (مثلاً ۱۵ روز)، دقیقاً به همان صورت و پیوسته در طول یک سال کامل تکرار شود، در نهایت چه میزان بازدهی سالانه محقق خواهد شد. این عدد برای <b>مقایسه</b> موقعیت‌ها با سررسیدهای متفاوت است، نه یک وعده بازده.</p></details>
    <details><summary>حاشیه ریسک دقیقاً چه چیزی را می‌گوید؟</summary><p>حاشیه ریسک برابر <span dir="ltr">P/K − 1</span> است: یعنی قیمت سهم تا چه درصدی می‌تواند ریزش کند و سود موقعیت همچنان قطعی و تضمین‌شده باقی بماند. در مثال صفحه، تا ۲۰ درصد ریزش، نرخ ۶۶ درصد محقق می‌شود.</p></details>
    <details><summary>اگر سهم بیش از حاشیه ریسک ریزش کند چه می‌شود؟</summary><p>سهم در پرتفوی شما باقی می‌ماند و پرمیوم دریافتی هم مال شماست. تا زمانی که قیمت بالای نقطه سربه‌سری (قیمت خرید منهای پرمیوم) بماند، ضرری متوجه پرتفو نیست؛ فقط سود موقعیت از دست می‌رود. زیر آن سطح، موقعیت وارد زیان می‌شود.</p></details>
    <details><summary>برای استفاده باید با اختیار معامله آشنا باشم؟</summary><p>آشنایی پایه لازم است. دانشنامه ما مفاهیم قیمت اعمال، سررسید، حاشیه ریسک و نقطه سربه‌سری را از صفر توضیح می‌دهد و ماشین‌حساب کاوردکال به شما اجازه می‌دهد اعداد خودتان را وارد کنید.</p></details>
    <details><summary>داشبورد به من می‌گوید کدام موقعیت را بخرم؟</summary><p>خیر. داشبورد موقعیت‌ها را بر اساس نرخ و ریسک مرتب و رنگ‌بندی می‌کند، اما توصیه خرید یا فروش نمی‌دهد. انتخاب و اجرای معامله با شماست.</p></details>
  </div>
</div>
</section>

<!-- CTA -->
<section class="sec" style="padding-top:0">
<div class="wrap">
  <div class="ctaband">
    <h2>همین حالا دیدبان را ببینید</h2>
    <p>نسخه مهمان بدون ثبت‌نام باز است؛ ستون‌های نرخ و حاشیه ریسک با عضویت رایگان باز می‌شوند.</p>
    <a class="btn btn-blue" href="dashboard-covered-call.html"><ico>📈</ico>ورود به داشبورد کاوردکال</a>
    <a class="btn btn-s" href="tools-covered-call.html" style="color:#DBE6FE;border-color:#334155;margin-inline-start:8px">ماشین‌حساب کاوردکال</a>
  </div>
</div>
</section>

<div class="riskbar"><div class="wrap">
  بازده اعلام‌شده در صورت تحقق سناریوی مطلوب و تا سقف حاشیه ریسک محاسبه‌شده است. در صورت ریزش قیمت سهم به زیر نقطه سربه‌سری، موقعیت وارد زیان می‌شود. اطلاعات این صفحه صرفاً جنبه تحلیلی دارد و توصیه به خرید یا فروش هیچ اوراق بهاداری محسوب نمی‌شود.
</div></div>
"""

JS = """
var OPTS=[
 {s:'ضستا۳۰۱۰',dtm:15,r:69.4},
 {s:'ضشنا۶۰۴۹',dtm:20,r:66.3},
 {s:'ضخود۶۰۵۵',dtm:57,r:64.4},
 {s:'ضملی۳۰۵۸',dtm:43,r:62.4},
 {s:'ضفولا۶۰۳۲',dtm:29,r:57.3},
 {s:'ضهرم۷۰۲۲',dtm:26,r:55.5},
 {s:'ضفزر۱۰۱۳',dtm:71,r:53.9}];
var oi=0;
function drawOpts(first){
  var b=document.getElementById('ccBody'); if(!b) return;
  var rows=[0,1,2].map(function(k){return OPTS[(oi+k)%OPTS.length]});
  if(!first) b.querySelectorAll('tr').forEach(function(t){t.classList.add('out')});
  setTimeout(function(){
    b.innerHTML=rows.map(function(o){
      return '<tr><td class="sym">'+o.s+'</td><td class="dtm">'+fa(o.dtm)+' روز</td>'+
             '<td class="rt">'+fa(o.r.toFixed(1)).replace('.','٫')+'٪ <em>سالانه</em></td></tr>'}).join('');
  }, first?0:340);
}
var t0=new Date(); t0.setHours(17,31,4,0);
function clk(){t0=new Date(t0.getTime()+1000);
  var c=document.getElementById('ccClock'); if(!c) return;
  c.textContent=fa(('0'+t0.getHours()).slice(-2)+':'+('0'+t0.getMinutes()).slice(-2)+':'+('0'+t0.getSeconds()).slice(-2))}
drawOpts(true);
if(!(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches)){
  setInterval(clk,1000);
  setInterval(function(){
    oi=(oi+1)%OPTS.length; drawOpts(false);
    var n=document.getElementById('ccN'), v=10+Math.floor(Math.random()*6);
    if(fa(v)!==n.textContent){n.textContent=fa(v);
      n.classList.add('fu');setTimeout(function(){n.classList.remove('fu')},700)}
  },4200);
}
"""

HTML = paywall.apply(HTML)
