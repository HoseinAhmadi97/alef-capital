#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local preview server — the same URL rules as production.

    python tools/serve.py [port]        or      make serve

Python's plain `http.server` does not resolve /wiki to wiki.html, so with
CLEAN_URLS on every link would 404 locally while working fine on the server.
This mirrors nginx's `try_files $uri $uri.html $uri/index.html /index.html`
so what you see here is what the server does.
"""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dist")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def translate_path(self, path):
        p = super().translate_path(path)
        if os.path.isdir(p):
            index = os.path.join(p, "index.html")
            return index if os.path.exists(index) else p
        if os.path.exists(p):
            return p
        if os.path.exists(p + ".html"):          # /wiki  → wiki.html
            return p + ".html"
        return os.path.join(ROOT, "index.html")  # unknown → the 404 page

    def end_headers(self):
        # never cache during development, or you debug yesterday's build
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))


def main():
    if not os.path.isdir(ROOT):
        print("✗ dist/ does not exist. Run `make build` first.")
        sys.exit(1)
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print("→ http://localhost:%d   (Ctrl+C to stop)" % port)
    try:
        ThreadingHTTPServer(("", port), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\n✓ stopped")


if __name__ == "__main__":
    main()
