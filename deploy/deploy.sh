#!/usr/bin/env bash
# ════════════════════════════════════════════════════════════════
#  انتشار نسخه جدید روی سرور
#  روی سرور اجرا کنید:   ./deploy/deploy.sh
# ════════════════════════════════════════════════════════════════
set -euo pipefail
cd "$(dirname "$0")/.."

echo "→ دریافت آخرین تغییرات"
git pull --ff-only

echo "→ ساخت سایت"
python3 site/build.py

echo "→ بررسی لینک‌ها"
python3 - <<'PY'
import sys, os
sys.path.insert(0, 'tests')
import check
bad = check.check_links()
if bad:
    print("✗ لینک شکسته:", *bad, sep="\n  ")
    sys.exit(1)
print("✓ لینک‌ها سالم")
PY

# ── وب‌سرور ──
# هر دو حالت پشتیبانی می‌شود. در هیچ‌کدام restart لازم نیست،
# چون وب‌سرور فایل‌ها را مستقیم از dist/ می‌خواند.
if systemctl is-active --quiet nginx 2>/dev/null; then
  echo "✓ nginx فعال است — مستقیم از dist/ سرو می‌کند"
elif command -v docker >/dev/null 2>&1; then
  if ! docker ps --format '{{.Names}}' | grep -q alef-caddy; then
    echo "→ بالا آوردن Caddy"
    docker compose -f deploy/docker-compose.yml up -d
  else
    echo "✓ Caddy بالاست"
  fi
else
  echo "⚠ هیچ وب‌سروری پیدا نشد — docs/DEPLOY.md بخش ۳ را ببینید"
fi

echo "✓ منتشر شد — https://alefcapital.ir"
