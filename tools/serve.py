#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local preview server — the same URL rules as production.

    python tools/serve.py [port]        or      make serve

Python's plain `http.server` does not resolve /wiki to wiki.html, so with
CLEAN_URLS on every link would 404 locally while working fine on the server.
This mirrors nginx's `try_files $uri $uri.html $uri/index.html /index.html`
so what you see here is what the server does.

It also forwards the live-data path (config.GOLD_API) to Nexus, the way
nginx does in production, so the pages show real numbers locally too:

    NEXUS_URL=http://127.0.0.1:8100 make serve      (that is the default)

Reach a remote Nexus with an SSH tunnel, e.g. `ssh -L 8100:127.0.0.1:8100 alpha`.
"""
import os
import sys
import urllib.error
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(os.path.dirname(HERE), "dist")
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "site"))
import config as C  # noqa: E402

NEXUS_URL = os.environ.get("NEXUS_URL", "http://127.0.0.1:8100").rstrip("/")
# site path → Nexus path; mirrors the nginx `location` in deploy/nginx.conf
API_ROUTES = {C.GOLD_API: "/v1/gold/snapshot"}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def do_GET(self):
        upstream = API_ROUTES.get(self.path.split("?", 1)[0])
        if upstream is None:
            return super().do_GET()
        req = urllib.request.Request(NEXUS_URL + upstream)
        if self.headers.get("If-None-Match"):
            req.add_header("If-None-Match", self.headers["If-None-Match"])
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                status, headers, body = resp.status, resp.headers, resp.read()
        except urllib.error.HTTPError as e:            # 304 arrives here too
            status, headers, body = e.code, e.headers, e.read()
        except OSError as e:
            self.send_error(502, "Nexus unreachable at %s (%s)" % (NEXUS_URL, e))
            return
        self.send_response(status)
        for name in ("Content-Type", "ETag", "Cache-Control"):
            if headers.get(name):
                self.send_header(name, headers[name])
        self.send_header("Content-Length", str(len(body)))
        self._api = True
        self.end_headers()
        self.wfile.write(body)

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
        # never cache pages during development, or you debug yesterday's
        # build — the API keeps its own caching headers
        if not getattr(self, "_api", False):
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
    print("  live data: %s → %s" % (C.GOLD_API, NEXUS_URL + API_ROUTES[C.GOLD_API]))
    try:
        ThreadingHTTPServer(("", port), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\n✓ stopped")


if __name__ == "__main__":
    main()
