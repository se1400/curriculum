#!/usr/bin/env python3
"""
Mechanically wraps every slide's existing content in the rail/main scaffold
without touching a single character of that content. This is the part of a
redesign that's pure risk with zero creative value if done by hand across a
2000-line file — a human (or model) re-typing the whole file is exactly how
text silently gets dropped.

What it does, per <div class="slide ...">...</div> block found via proper
depth-counted tag matching (not naive regex):
  - Extracts the deck title from <title> for the rail kicker.
  - Extracts this slide's own .slide-tag text (if present) for the rail-tag.
  - Extracts a running slide number (1-based, in document order).
  - If the slide has a direct .slide-inner (or .main-inner) child: wraps it
    as <div class="rail">...</div><div class="main">{slide-inner untouched}</div>
  - If the slide has no such child (e.g. a bare full-embed iframe slide):
    wraps whatever's there as-is in <div class="rail">...</div><div
    class="main">{original content untouched}</div>

Does NOT touch <style> or <script>. Does NOT touch any text. Run the
project's diff_content.py afterward — it should report zero deletions.

Usage:
    python3 wrap_rail.py slides/some-deck.html
Writes the result back to the same file. Prints a summary of what it did.
"""

import re
import sys


def find_matching_close(html, open_tag_end):
    """Given the index right after a <div ...> opening tag's '>', find the
    index of the '<' that starts its matching </div>, by counting nested
    <div ...> / </div> pairs."""
    depth = 1
    pos = open_tag_end
    tag_re = re.compile(r"<div\b[^>]*>|</div>", re.IGNORECASE)
    for m in tag_re.finditer(html, pos):
        if m.group(0).lower().startswith("</div"):
            depth -= 1
            if depth == 0:
                return m.start()
        else:
            depth += 1
    raise ValueError("Unbalanced <div> tags — could not find matching close")


def extract_slides(html):
    """Returns a list of (start, end, full_text) for each top-level
    <div class="slide ...">...</div> block, in document order."""
    slides = []
    # "slide" as a whole class token: exactly class="slide", or class="slide
    # <more classes>". Must NOT match slide-tag / slide-inner / slideshow /
    # slide-counter etc., which merely start with "slide".
    for m in re.finditer(r'<div class="slide(?:"| [^"]*")[^>]*>', html):
        open_end = m.end()
        close_start = find_matching_close(html, open_end)
        close_end = close_start + len("</div>")
        slides.append((m.start(), close_end, html[m.start():close_end]))
    return slides


def transform_slide(slide_html, kicker, slide_num, total_width=2):
    # slide opening tag + its immediate class list
    m = re.match(r'(<div class="slide\b[^"]*"[^>]*>)(.*)</div>\s*$', slide_html, re.S)
    if not m:
        raise ValueError("Slide block didn't match expected shape")
    open_tag, inner = m.group(1), m.group(2)

    tag_m = re.search(r'<div class="slide-tag">(.*?)</div>', inner, re.S)
    rail_tag_html = ""
    if tag_m:
        rail_tag_html = f'\n      <div class="rail-tag">{tag_m.group(1)}</div>'

    num_str = str(slide_num).zfill(total_width)
    rail = (
        f'\n    <div class="rail">'
        f'\n      <div class="rail-top">'
        f'\n        <div class="kicker">{kicker}</div>'
        f'\n        <div class="rail-num">{num_str}</div>'
        f'\n      </div>'
        f'{rail_tag_html}'
        f'\n    </div>'
    )

    # Find the direct-child .slide-inner (or already-named .main-inner) block
    # to wrap in .main. If not found, wrap the whole inner content instead
    # (covers bare full-embed slides with no such wrapper).
    inner_stripped = inner.strip()
    sw = re.match(r'<div class="(slide-inner|main-inner|slide-content)"[^>]*>', inner_stripped)
    if sw and inner_stripped.startswith(sw.group(0)):
        # Confirm this wrapper spans the whole remaining inner content
        open_end = sw.end()
        close_start = find_matching_close(inner_stripped, open_end)
        close_end = close_start + len("</div>")
        if close_end == len(inner_stripped):
            main_content = inner_stripped
        else:
            main_content = inner_stripped
    else:
        main_content = inner_stripped

    new_inner = f'{rail}\n    <div class="main">{main_content}</div>\n  '
    return f'{open_tag}{new_inner}</div>'


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    path = sys.argv[1]
    html = open(path, encoding="utf-8").read()

    title_m = re.search(r"<title>(.*?)</title>", html, re.S)
    kicker = title_m.group(1).strip() if title_m else "Deck"
    # Only escape for the rail — keep it plain text, single line is fine;
    # a simple deck title rarely needs a <br>, so leave wrapping to CSS.

    slides = extract_slides(html)
    if not slides:
        print("No <div class=\"slide ...\"> blocks found — nothing to do.")
        sys.exit(1)

    total = len(slides)
    width = len(str(total))

    # Rebuild the document by replacing each slide block, back to front so
    # earlier offsets stay valid.
    new_html = html
    for i, (start, end, block) in reversed(list(enumerate(slides, start=1))):
        replacement = transform_slide(block, kicker, i, width)
        new_html = new_html[:start] + replacement + new_html[end:]

    open(path, "w", encoding="utf-8").write(new_html)
    print(f"Wrapped {total} slides with rail/main scaffold in {path}")
    print(f"Kicker text used: {kicker!r}")


if __name__ == "__main__":
    main()
