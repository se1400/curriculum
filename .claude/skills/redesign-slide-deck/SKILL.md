---
name: redesign-slide-deck
description: Redesigns the interactive HTML slideshow decks in slides/ away from the generic "AI dashboard" look (gradient-clipped headlines, four-color violet/mint/amber/red palette, rounded cards for everything) into a consistent editorial system — Fraunces/Inter/JetBrains Mono, a warm dark palette, a single terracotta accent, a left margin rail, and slides that never scroll or clip. Use this whenever the user asks to redesign, restyle, reskin, modernize, unify, or "fix the look" of a deck in slides/, mentions a specific deck by name, or says the slides look like AI slop / look generic / need a facelift. Always work on exactly one deck at a time and stop for the user's explicit approval before starting the next one — never batch-apply across multiple files in the same pass, even if asked to "just do all of them," without confirming that's really what they want.
---

# Redesign Slide Deck

## Why this is riskier than it looks

These decks are single self-contained HTML files: markup, CSS, and JS all
inline, no shared stylesheet between files. That independence is exactly
what makes this dangerous to automate carelessly — every deck was hand-built
at a different time, so **no two decks necessarily share the same CSS
variable names, the same navigation engine, or the same component classes.**
A change that's safe in one file can silently break another.

Two concrete failure modes already found in this codebase:

1. **Interactive demos generate inline styles that hard-code CSS variable
   names** — e.g. `'<span style="color:var(--accent2)">'` built inside a
   `<script>` block. Rename `--accent2` while restyling the page and that
   demo's output silently renders with no color. No error, no console
   warning — it just looks wrong, and only if someone happens to click it.
2. **A handful of decks mutate CSS custom properties live** (`javascript-dom-foundations.html`
   drives an actual `--hue`/`--saturation` demo via `documentElement.style.setProperty`).
   Those variables are the lesson content, not decoration.

The rule that avoids both: **never rename an existing CSS custom property.**
Repoint its hex value to the new palette; never touch its name. This means
the `<script>` block of a deck almost never needs to be opened for editing —
only read, during the preflight step below.

## Before touching any file: run the preflight

```
.claude/skills/redesign-slide-deck/scripts/inventory_slide.sh slides/<file>.html
```

This prints, for that specific file:
- its own `:root` custom property names and current values
- which of those variables the `<script>` block reads dynamically (these
  names are locked — repoint values only)
- every id / class / dataset key JS depends on (`getElementById`,
  `querySelector`, `classList`, `data-*`) — these must not be renamed
- every `onclick`-invoked function name — same rule
- any live `style.setProperty` / `documentElement.style` usage — if this
  fires, stop and read that part of the script by hand before deciding
  anything about the palette; the variable being mutated is probably load-bearing
  content, not styling
- whether the deck uses the standard `showSlide`/`changeSlide` engine and the
  standard nav ids (`#slide-counter`, `#prevBtn`, `#nextBtn`, `#progress-bar`).
  **Three decks in this repo don't**: `responsive-design.html`,
  `ux-design-usability.html`, `visual-design-theory.html`. If the script
  reports the standard engine missing, read the whole `<script>` block before
  assuming the rail/fit-to-screen scaffold in this skill applies as-is.
- how many CodePen/iframe embeds it has, and what recurring component
  classes (`.card`, `.two-col`, `.demo-box`, etc.) it already uses

Do this for every deck, even ones that look similar to one you've already
done. Don't assume; the whole point of this step is that assumptions are
what break a demo three lessons later.

## The design system

Full token values, font setup, and CSS for every recurring component are in
[references/design-system.md](references/design-system.md) — read it before
writing any CSS. The short version, approved by the user across two rounds
of real rendered review:

- **Typefaces**: Fraunces (headlines, display numerals) + Inter (body/UI) +
  JetBrains Mono (code) via Google Fonts. Disable ligatures on `code`
  (`font-variant-ligatures: none`) — JetBrains Mono renders `===` as a
  squashed glyph otherwise.
- **Palette**: warm near-black background, warm ivory text, one terracotta
  accent used sparingly (current page number, cautions, interactive
  affordances) rather than smeared across four unrelated hues. Exact hex
  values are in the reference doc, keyed to whatever variable names *that
  file* already uses per the preflight step — don't invent new variable
  names for colors that already have a name.
- **Layout**: a persistent left rail (deck kicker, big italic slide number,
  rotated section tag) replaces the old centered 860px column. Content uses
  the freed-up width instead of floating in empty space.
- **Components, not cards**: analogies become a typographic pull-quote
  (serif italic, big opening quote mark), notes/best-practices become
  numbered or ruled lists instead of identically-styled colored boxes.
  Reserve color for things that need attention (cautions, live output),
  not decoration.

## The no-scroll rule

A slide must never require scrolling, and must never silently clip content
either. The fix is a fit-to-screen scale, not `overflow: auto`: measure each
slide's natural content height; if it's taller than the available space,
scale the whole content block down just enough to fit (`transform: scale()`
on a wrapper, anchored top-left, width compensated so it still spans full
width after scaling). Dense slides zoom out a hair; simple slides render at
full size. The JS for this is short and reusable — copy it from
[references/design-system.md](references/design-system.md) rather than
rederiving it each time.

Set a floor on the scale (around `0.72`). If a slide would need to shrink
past that to fit, that's a signal the slide has too much content and should
be **split into two slides**, not shrunk further — flag this to the user
rather than silently letting text get too small to read on a classroom
projector.

Also drop `overflow-x: auto` on code blocks in favor of `white-space:
pre-wrap; overflow-wrap: anywhere`, and widen `pre` (`max-width: 82ch` or so)
since the new layout has far more horizontal room than the old narrow
column — this avoids most wrapping before it starts.

## What must never change, ever

- Visible text: headings, body copy, analogies, list items, table cells,
  best-practice descriptions, link text and hrefs.
- Code sample content (the actual code being taught) and its syntax
  highlighting markup (`<span class="kw">` etc.) — restyle the CSS rule for
  `.kw`/`.fn`/`.str`/etc., never touch which spans wrap which tokens.
- Anything inside `<script>` — logic, function bodies, data objects, event
  wiring — except the one narrow, mechanical case of a CSS variable *value*
  changing while its *name* stays put (which requires no script edit at
  all).
- Any element id, class name, or `data-*` key that the preflight step
  flagged as JS-dependent.
- iframe `src` URLs, and everything else about a CodePen/iframe embed —
  see the special case below. Don't invent bespoke layout for these slides;
  it's exactly how the one real bug so far happened.

What's expected and fine to change: CSS rule bodies (colors, fonts, spacing,
radius, shadows), the wrapping DOM structure around content (adding the rail,
the fit-to-screen scaling wrapper), and which existing component pattern a
slide uses (e.g. a `dl.qa` card list becoming a numbered index) — as long as
the text inside is carried over verbatim and no JS-referenced identifier
inside that block is touched.

## Verify before presenting a file as done

1. Run the preflight script's identifier list again against the finished
   file and confirm every id/class/onclick target/function name is still
   there.
2. Run the diff script:
   ```
   python3 .claude/skills/redesign-slide-deck/scripts/diff_content.py \
     slides/<file>.html.orig slides/<file>.html
   ```
   (keep a `.orig` copy — or just use `git show HEAD:slides/<file>.html` — as
   the "before" side). A clean run prints "No visible text differences" and
   "Every original identifier is still present." Anything else needs to be
   understood before moving on, not explained away.
3. Actually open the file in a browser and **click every interactive
   control** — every demo button, every input, every sortable/filterable
   grid — and check the output is correct, not just that it looks styled
   correctly at rest. A static screenshot of the resting state proves
   nothing about whether the demo still works.
4. Screenshot 3–4 representative slides (title, a dense content slide, any
   interactive demo, and any distinctive component like a table or two-col
   comparison) for the user to review.

## Workflow

Work on exactly one file per pass:

1. Preflight (script above).
2. Redesign: apply the design system, wrap slides in the rail/fit-to-screen
   scaffold, restyle existing component classes in place.
3. Verify (four checks above).
4. Edit the real file in place — this repo is git-tracked, so `git diff` /
   `git checkout` is the undo button. Don't create a scratch copy in
   `slides/` for review; that was only useful while the design system itself
   was still being decided.
5. Present screenshots + a one-line summary of what changed to the user and
   **wait for explicit approval** before starting the next file.

Never move to the next file on your own initiative, even if the previous one
went smoothly. Decks vary enough (see preflight rationale above) that a clean
run on one file is not evidence the next one will be as straightforward.

## Known special cases — read the file by hand before applying anything generic

- `javascript-dom-foundations.html`, `css-animations-pseudo-elements.html`,
  `css-transitions-transforms.html`, `functions-loops-generating-html.html`,
  `javascript-events-decisions.html` — these mutate CSS custom properties
  live via JS. Understand exactly what each mutated property drives before
  touching that file's palette.
- `responsive-design.html`, `ux-design-usability.html`,
  `visual-design-theory.html` — don't use the standard `showSlide`/
  `changeSlide` engine. Read their actual navigation mechanism first.
- 19 of 25 decks embed CodePen iframes. Give these slides the standard rail
  scaffold and restyle their heading/paragraph text like any other slide —
  **but leave `.codepen-container`, the iframe, and its attributes
  completely untouched.** An earlier attempt at a special "full-bleed"
  treatment for these silently dropped a slide's actual heading and intro
  paragraph, on the unchecked assumption that a CodePen slide has no other
  content. See
  [references/design-system.md](references/design-system.md) for the full
  rule — there's no case where inventing bespoke embed styling is worth the
  risk, especially at this volume.
- Every deck also has bespoke, lesson-specific interactive widgets (a
  box-model visualizer, a flexbox playground, "gestalt cards," etc.) with
  their own custom classes. There's no generic template for these — restyle
  each on its own terms, guided by the same design-system principles, and
  show the user before assuming it lands.
