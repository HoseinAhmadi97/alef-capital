# -*- coding: utf-8 -*-
"""
Pricing page.

The price numbers do not live here — they come from config.PRICING.
They appear in the markup as @@NAME@@ placeholders and are substituted
at the bottom of this file.
"""
import config as C

HTML = """
<section class="phero">
<div class="wrap" style="text-align:center">
  <div class="crumb" style="text-align:right"><a href="index.html">خانه</a> ← قیمت‌گذاری</div>
  <span class="eyebrow">اشتراک</span>
  <h1>پلن مناسب خود را انتخاب کنید</h1>
  <p class="lead" style="margin-inline:auto">همه پلن‌ها ۷ روز رایگان، بدون نیاز به کارت بانکی. هر زمان بخواهید لغو کنید.</p>

  <div style="margin-top:26px">
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
      <a class="btn btn-s" href="#">شروع رایگان</a>
      <ul class="feat">
        <li>۵ صندوق برتر</li>
        <li>داده با تأخیر ۱۵ دقیقه</li>
        <li>۱ هشدار</li>
        <li>خارج از ساعت معاملات: داده کامل روز قبل</li>
        <li class="no">داشبورد کاوردکال</li>
        <li class="no">تاریخچه و خروجی اکسل</li>
      </ul>
      <a href="#cmp" style="display:block;text-align:center;margin-top:16px;font-size:13px;font-weight:700">ویژگی‌ها و مقایسه ↓</a>
    </div>

    <div class="plan hot">
      <span class="badge">محبوب‌ترین</span>
      <h3>طلا</h3>
      <div class="who">دارندگان صندوق طلا که دنبال بازده اضافه‌اند</div>
      <div class="price"><span class="num" id="p-gold">@@M_GOLD@@</span> <small>تومان</small></div>
      <div class="per" id="u-gold">@@M_NOTE@@</div>
      <a class="btn btn-p" href="#">خرید اشتراک طلا</a>
      <ul class="feat">
        <li>همه صندوق‌های طلا، لحظه‌ای</li>
        <li>تحلیل ترکیب دارایی صندوق‌ها</li>
        <li>مانیتورینگ NAV (Latent / Pure)</li>
        <li>۲۰ هشدار حباب + تاریخچه ۶ ماه</li>
        <li>خروجی اکسل · پشتیبانی تیکت</li>
        <li class="no">داشبورد کاوردکال</li>
      </ul>
      <a href="#cmp" style="display:block;text-align:center;margin-top:16px;font-size:13px;font-weight:700">ویژگی‌ها و مقایسه ↓</a>
    </div>

    <div class="plan">
      <h3>حرفه‌ای</h3>
      <div class="who">معامله‌گران اختیار معامله و پرتفوهای ترکیبی</div>
      <div class="price"><span class="num" id="p-pro">@@M_PRO@@</span> <small>تومان</small></div>
      <div class="per" id="u-pro">@@M_NOTE@@</div>
      <a class="btn btn-s" href="#">خرید اشتراک حرفه‌ای</a>
      <ul class="feat">
        <li>همه امکانات پلن طلا</li>
        <li>دیدبان کامل کاوردکال</li>
        <li>نمودار سود و زیان و نقطه سربه‌سری</li>
        <li>هشدار نامحدود · تاریخچه نامحدود</li>
        <li>دسترسی API</li>
        <li>پشتیبانی تلفنی اختصاصی</li>
      </ul>
      <a href="#cmp" style="display:block;text-align:center;margin-top:16px;font-size:13px;font-weight:700">ویژگی‌ها و مقایسه ↓</a>
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

<!-- COMPARISON -->
<section class="sec" id="cmp" style="background:var(--surface-2);border-block:1px solid var(--border)">
<div class="wrap">
  <h2 class="h2" style="text-align:center">مقایسه کامل امکانات</h2>
  <div class="tscroll">
  <table class="cmp">
    <thead><tr><th>ویژگی</th><th>پایه</th><th class="hi">طلا</th><th>حرفه‌ای</th></tr></thead>
    <tbody>
      <tr class="grp"><td colspan="4">داشبورد آربیتراژ صندوق طلا</td></tr>
      <tr><td>تعداد صندوق قابل مشاهده</td><td>۵ صندوق</td><td class="hi">همه (۳۰+)</td><td>همه (۳۰+)</td></tr>
      <tr><td>تأخیر داده</td><td>۱۵ دقیقه</td><td class="hi">لحظه‌ای</td><td>لحظه‌ای</td></tr>
      <tr><td>محاسبه حباب نسبت به NAV</td><td class="y">✓</td><td class="hi y">✓</td><td class="y">✓</td></tr>
      <tr><td>تحلیل ترکیب دارایی صندوق‌ها</td><td class="n">—</td><td class="hi y">✓</td><td class="y">✓</td></tr>
      <tr><td>مانیتورینگ Latent / Pure NAV</td><td class="n">—</td><td class="hi y">✓</td><td class="y">✓</td></tr>
      <tr><td>شناسایی خودکار صندوق ارزنده</td><td class="n">—</td><td class="hi y">✓</td><td class="y">✓</td></tr>

      <tr class="grp"><td colspan="4">داشبورد کاوردکال</td></tr>
      <tr><td>دیدبان قراردادهای اختیار خرید</td><td class="n">—</td><td class="hi n">—</td><td class="y">✓ (۳۶۸ قرارداد)</td></tr>
      <tr><td>نرخ سود معادل سالانه و حاشیه ریسک</td><td class="n">—</td><td class="hi n">—</td><td class="y">✓</td></tr>
      <tr><td>نمودار سود و زیان و نقطه سربه‌سری</td><td class="n">—</td><td class="hi n">—</td><td class="y">✓</td></tr>
      <tr><td>پایش پرتفوی موقعیت‌های باز</td><td class="n">—</td><td class="hi n">—</td><td class="y">✓</td></tr>

      <tr class="grp"><td colspan="4">هشدار و تاریخچه</td></tr>
      <tr><td>هشدار حباب</td><td>۱</td><td class="hi">۲۰</td><td>نامحدود</td></tr>
      <tr><td>هشدار فرصت کاوردکال</td><td class="n">—</td><td class="hi n">—</td><td class="y">✓</td></tr>
      <tr><td>کانال هشدار</td><td>درون‌برنامه</td><td class="hi">درون‌برنامه + ایمیل</td><td>+ پیامک</td></tr>
      <tr><td>تاریخچه داده</td><td>۱ روز</td><td class="hi">۶ ماه</td><td>نامحدود</td></tr>
      <tr><td>خلاصه هفتگی بازار</td><td class="y">✓</td><td class="hi y">✓</td><td class="y">✓</td></tr>

      <tr class="grp"><td colspan="4">خروجی و یکپارچه‌سازی</td></tr>
      <tr><td>خروجی اکسل / CSV</td><td class="n">—</td><td class="hi y">✓</td><td class="y">✓</td></tr>
      <tr><td>دسترسی API</td><td class="n">—</td><td class="hi n">—</td><td class="y">✓</td></tr>
      <tr><td>تعداد کاربر</td><td>۱</td><td class="hi">۱</td><td>۳</td></tr>

      <tr class="grp"><td colspan="4">آموزش و پشتیبانی</td></tr>
      <tr><td>دانشنامه و راهنماها</td><td class="y">✓</td><td class="hi y">✓</td><td class="y">✓</td></tr>
      <tr><td>پشتیبانی</td><td>راهنمای آنلاین</td><td class="hi">تیکت (۲۴ ساعته)</td><td>تلفنی اختصاصی</td></tr>
      <tr><td>جلسه آنبوردینگ</td><td class="n">—</td><td class="hi n">—</td><td class="y">✓</td></tr>
    </tbody>
  </table>
  </div>
  <p style="font-size:12.5px;color:var(--slate-500);margin-top:14px">اعداد قیمت پیشنهادی است و قابل تنظیم. همه پلن‌ها شامل ۷ روز استفاده رایگان بدون نیاز به کارت بانکی هستند.</p>
</div>
</section>

<!-- FAQ -->
<section class="sec">
<div class="wrap">
  <h2 class="h2" style="text-align:center">سوالات متداول خرید</h2>
  <div class="faq">
    <details open><summary>آیا می‌توانم قبل از خرید، داشبورد را ببینم؟</summary><p>بله. صفحه <a href="market.html">نبض بازار</a> بدون ثبت‌نام باز است و با ثبت‌نام رایگان به جدول کامل صندوق‌ها با تأخیر ۱۵ دقیقه دسترسی دارید. خارج از ساعات معاملاتی هم داده کامل آخرین روز معاملاتی برای همه در دسترس است.</p></details>
    <details><summary>تفاوت پلن طلا و حرفه‌ای در عمل چیست؟</summary><p>پلن طلا فقط حوزه صندوق‌های طلا را پوشش می‌دهد: حباب، NAV و ترکیب دارایی. پلن حرفه‌ای علاوه بر آن، دیدبان کامل قراردادهای اختیار خرید، محاسبه نرخ سود معادل سالانه، نمودار سود و زیان و دسترسی API را اضافه می‌کند.</p></details>
    <details><summary>امکان ارتقای پلن در میانه دوره وجود دارد؟</summary><p>بله. هزینه باقی‌مانده پلن فعلی به‌صورت اعتبار محاسبه و از مبلغ پلن جدید کسر می‌شود. تنزل پلن هم در پایان دوره جاری اعمال می‌گردد.</p></details>
    <details><summary>داده‌ها از چه منبعی و با چه تأخیری می‌آیند؟</summary><p>داده مستقیماً از تابلوی معاملات بورس تهران و بورس کالا خوانده می‌شود. در پلن‌های پولی تأخیر عملی زیر یک ثانیه است و مهر زمان هر داده روی صفحه نمایش داده می‌شود.</p></details>
    <details><summary>اگر اشتراکم تمام شود، هشدارها و تنظیماتم را از دست می‌دهم؟</summary><p>خیر. تنظیمات، هشدارها و لیست‌های ذخیره‌شده حفظ می‌شوند و با تمدید اشتراک دوباره فعال می‌گردند. دسترسی به داده لحظه‌ای تا زمان تمدید متوقف می‌شود.</p></details>
    <details><summary>آیا فاکتور رسمی صادر می‌شود؟</summary><p>بله. برای همه پلن‌ها فاکتور رسمی صادر می‌شود و در بخش «اشتراک و فاکتورها» در حساب کاربری قابل دانلود است.</p></details>
    <details><summary>برای خرید سازمانی چطور اقدام کنم؟</summary><p>از طریق <a href="services.html">صفحه خدمات</a> فرم درخواست مشاوره را پر کنید. برای تیم‌های بالای سه کاربر، دسترسی چندکاربره و گزارش اختصاصی ارائه می‌شود.</p></details>
  </div>
</div>
</section>
"""

JS = """
var PRICES={
  m:{gold:'@@M_GOLD@@',pro:'@@M_PRO@@',u:'@@M_NOTE@@'},
  q:{gold:'@@Q_GOLD@@',pro:'@@Q_PRO@@',u:'@@Q_NOTE@@'},
  y:{gold:'@@Y_GOLD@@',pro:'@@Y_PRO@@',u:'@@Y_NOTE@@'}};
function setP(k){var p=PRICES[k];
  document.getElementById('p-gold').textContent=p.gold;
  document.getElementById('p-pro').textContent=p.pro;
  document.getElementById('u-gold').textContent=p.u;
  document.getElementById('u-pro').textContent=p.u;
  ['m','q','y'].forEach(function(x){document.getElementById('b'+x).className=(x===k?'on':'')})}
"""


# ─── substitute the numbers from config ───
_MAP = {}
for _pfx, _key in (("M", "monthly"), ("Q", "quarterly"), ("Y", "yearly")):
    _p = C.PRICING[_key]
    _MAP[f"@@{_pfx}_GOLD@@"] = _p["gold"]
    _MAP[f"@@{_pfx}_PRO@@"]  = _p["pro"]
    _MAP[f"@@{_pfx}_NOTE@@"] = _p["note"]

def _fill(t):
    for k, v in _MAP.items():
        t = t.replace(k, v)
    return t

HTML = _fill(HTML)
JS = _fill(JS)
