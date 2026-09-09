.PHONY: build check serve fonts deploy clean zip help
.DEFAULT_GOAL := help

help:            ## show this help
	@grep -E '^[a-z]+:.*##' $(MAKEFILE_LIST) | sed 's/:.*##/  →/' | sort

build:           ## build the site into dist/
	@find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null; python3 site/build.py

check: build     ## build + check links, render, overflow and menus
	@python3 tests/check.py

serve: build     ## local preview at http://localhost:8000
	@echo "→ http://localhost:8000"
	@cd dist && python3 -m http.server 8000

fonts:           ## download the Vazirmatn font for self-hosting
	@mkdir -p site/static/assets/fonts
	@for w in Regular Medium SemiBold Bold ExtraBold Black; do \
	  echo "  ↓ Vazirmatn-$$w"; \
	  curl -fsSL -o site/static/assets/fonts/Vazirmatn-$$w.woff2 \
	    "https://cdn.jsdelivr.net/npm/vazirmatn@33.0.3/fonts/webfonts/Vazirmatn-$$w.woff2" \
	  || echo "    ✗ failed — grab it manually from github.com/rastikerdar/vazirmatn"; \
	done
	@echo "→ done. Just run make build — the fonts are picked up automatically."

deploy:          ## publish to the server
	@./deploy/deploy.sh

zip: build       ## package dist/ for manual hand-off
	@cd dist && zip -qr ../alef-capital-site.zip . && echo "✓ alef-capital-site.zip"

clean:           ## remove build outputs
	@rm -rf dist alef-capital-site.zip && echo "✓ cleaned"
