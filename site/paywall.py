# -*- coding: utf-8 -*-
"""
Resolve the paywall markers used inside the dashboard and product pages.

Everything is currently open to every visitor (config.PAYWALL = False). The
markers below let that be reversed with one line in config.py once the site
has traffic, instead of re-editing every table by hand.

Markers:

    @@L:value@@              the real value, or a sign-up link when locked
    @@IFLOCK@@ ... @@END@@   a block that exists only while locked

Anything outside a marker is untouched, so an unlocked page carries no trace
of the paywall — no blurred rows, no teaser text, no dead links.
"""
import re

import config as C

LOCK_CELL = '<a class="lockcell" href="pricing.html">🔒 ورود / عضویت</a>'

_L_RE = re.compile(r"@@L:(.*?)@@", re.S)
_BLOCK_RE = re.compile(r"@@IFLOCK@@(.*?)@@END@@", re.S)


def apply(html):
    """Return `html` with every paywall marker resolved for the current mode."""
    if C.PAYWALL:
        html = _L_RE.sub(lambda m: LOCK_CELL, html)
        return _BLOCK_RE.sub(lambda m: m.group(1), html)
    html = _L_RE.sub(lambda m: m.group(1), html)
    return _BLOCK_RE.sub("", html)


def js_flag():
    """The same switch, for the row builders that run in the browser."""
    return "var PAYWALL=%s;\nvar LOCK='%s';\n" % (
        "true" if C.PAYWALL else "false", LOCK_CELL)
