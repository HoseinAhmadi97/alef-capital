#!/usr/bin/env bash
# ════════════════════════════════════════════════════════════════
#  Publish a new version on the server
#  Run this on the server:   ./deploy/deploy.sh
# ════════════════════════════════════════════════════════════════
set -euo pipefail
cd "$(dirname "$0")/.."

echo "→ pulling latest changes"
git pull --ff-only

echo "→ building the site"
python3 site/build.py

echo "→ checking links"
python3 - <<'PY'
import sys, os
sys.path.insert(0, 'tests')
import check
bad = check.check_links()
if bad:
    print("✗ broken links:", *bad, sep="\n  ")
    sys.exit(1)
print("✓ links are healthy")
PY

# ── web server ──
# Both setups are supported. Neither needs a restart, because the
# web server reads the files straight out of dist/.
if systemctl is-active --quiet nginx 2>/dev/null; then
  echo "✓ nginx is active — serving straight from dist/"
elif command -v docker >/dev/null 2>&1; then
  if ! docker ps --format '{{.Names}}' | grep -q alef-caddy; then
    echo "→ bringing Caddy up"
    docker compose -f deploy/docker-compose.yml up -d
  else
    echo "✓ Caddy is already up"
  fi
else
  echo "⚠ no web server found — see docs/DEPLOY.md section 3"
fi

echo "✓ published — https://alefcapital.ir"
