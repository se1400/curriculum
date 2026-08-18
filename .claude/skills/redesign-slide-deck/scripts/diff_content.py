#!/usr/bin/env python3
"""
Proves a redesign changed *presentation* and not *content*.

Compares an original slide deck against its redesigned version on the things
that must never drift: visible text, code sample text, button/label text,
and every identifier JS depends on (ids, onclick targets, dataset keys,
function names). Layout, classes used purely for styling, and CSS are
expected to differ and are ignored.

Usage:
    python3 diff_content.py original.html redesigned.html
"""

import re
import sys
import difflib
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    """Pulls out visible text, ignoring <style> and <script> content."""

    def __init__(self):
        super().__init__()
        self.chunks = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script"):
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in ("style", "script") and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data):
        if self._skip_depth == 0:
            text = data.strip()
            if text:
                self.chunks.append(text)


def extract_text(html):
    p = TextExtractor()
    p.feed(html)
    # Normalize whitespace so reflowed markup doesn't look like a text change.
    return [re.sub(r"\s+", " ", c).strip() for c in p.chunks if c.strip()]


def extract_identifiers(html):
    ids = set(re.findall(r"id=[\"']([^\"']+)[\"']", html))
    onclicks = set(re.findall(r"onclick=[\"']([a-zA-Z0-9_]+)\(", html))
    dataset_attrs = set(re.findall(r"data-([a-zA-Z-]+)=", html))
    script_blocks = "\n".join(re.findall(r"<script>(.*?)</script>", html, re.S))
    fn_defs = set(re.findall(r"function\s+([a-zA-Z0-9_]+)\s*\(", script_blocks))
    dom_ids = set(re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", script_blocks))
    return {
        "element id=\"\" attributes": ids,
        "onclick target functions": onclicks,
        "data-* attribute names": dataset_attrs,
        "function definitions": fn_defs,
        "getElementById targets": dom_ids,
    }


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    orig_path, new_path = sys.argv[1], sys.argv[2]
    orig = open(orig_path, encoding="utf-8").read()
    new = open(new_path, encoding="utf-8").read()

    print(f"=== Text content diff: {orig_path} -> {new_path} ===")
    orig_text = extract_text(orig)
    new_text = extract_text(new)
    diff = list(difflib.unified_diff(orig_text, new_text, lineterm="", n=0))
    if diff:
        print("TEXT CHANGED — review every line below. If any of these are the")
        print("body copy, a code sample, an analogy, or a demo label, STOP:")
        for line in diff:
            print(line)
    else:
        print("No visible text differences. Good.")
    print()

    print("=== Identifier diff ===")
    orig_ids = extract_identifiers(orig)
    new_ids = extract_identifiers(new)
    any_missing = False
    for label, orig_set in orig_ids.items():
        new_set = new_ids[label]
        missing = orig_set - new_set
        added = new_set - orig_set
        if missing:
            any_missing = True
            print(f"MISSING {label}: {sorted(missing)}")
        if added:
            print(f"(new, informational) {label}: {sorted(added)}")
    if not any_missing:
        print("Every original identifier is still present. Good.")

    if diff or any_missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
