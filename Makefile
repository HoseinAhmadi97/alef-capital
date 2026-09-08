.PHONY: build check serve fonts deploy clean zip help
.DEFAULT_GOAL := help

help:            ## نمایش همین راهنما
	@grep -E '^[a-z]+:.*##' $(MAKEFILE_LIST) | sed 's/:.*##/  →/' | sort

build:           ## ساخت سایت در dist/
	@find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null; python3 site/build.py

check: build     ## ساخت + بررسی لینک، رندر، سرریز و منوها
	@python3 tests/check.py

serve: build     ## پیش‌نمایش محلی روی http://localhost:8000
	@echo "→ http://localhost:8000"
	@cd dist && python3 -m http.server 8000

fonts:           ## دانلود فونت Vazirmatn برای میزبانی داخلی
	@mkdir -p site/static/assets/fonts
	@for w in Regular Medium SemiBold Bold ExtraBold Black; do \
	  echo "  ↓ Vazirmatn-$$w"; \
	  curl -fsSL -o site/static/assets/fonts/Vazirmatn-$$w.woff2 \
	    "https://cdn.jsdelivr.net/npm/vazirmatn@33.0.3/fonts/webfonts/Vazirmatn-$$w.woff2" \
	  || echo "    ✗ نشد — دستی از github.com/rastikerdar/vazirmatn بگیرید"; \
	done
	@echo "→ حالا در site/config.py مقدار SELF_HOSTED_FONT را True کنید و make build بزنید"

deploy:          ## انتشار روی سرور
	@./deploy/deploy.sh

zip: build       ## بسته‌بندی dist/ برای تحویل دستی
	@cd dist && zip -qr ../alef-capital-site.zip . && echo "✓ alef-capital-site.zip"

clean:           ## پاک کردن خروجی‌ها
	@rm -rf dist alef-capital-site.zip && echo "✓ پاک شد"
