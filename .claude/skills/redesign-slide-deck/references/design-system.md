# Design system reference

This is the copy-paste source of truth for restyling a deck. Read
[SKILL.md](../SKILL.md) first for the safety rules — this file is the visual
spec those rules apply to.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,900;1,9..144,500&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

- **Fraunces** — headlines (`h1`/`h2`), the big italic slide number in the
  rail, and pull-quote analogies.
- **Inter** — body text, UI labels, nav.
- **JetBrains Mono** — code. Always pair with:
  ```css
  code { font-variant-ligatures: none; font-feature-settings: "calt" 0, "liga" 0; }
  ```
  Without this, `===` and similar sequences render as a squashed ligature
  glyph instead of three characters — found and fixed during prototyping.

Classroom wifi is assumed available (this was an explicit tradeoff the user
accepted in exchange for real typographic personality over system-ui).

## Palette — values, not names

**Do not introduce these as new variable names.** Every deck already has its
own `:root` variable names (discovered via the preflight script) — repoint
*their* values to the roles below. Two examples from the actual audit:

| Role | Hex | Newer-template var (e.g. `arrays-of-objects...html`) | Older-template var (e.g. `box-model-positioning-flexbox.html`) |
|---|---|---|---|
| Page background | `#17140f` | `--bg` | `--light-bg` (check actual usage — some older decks use this name for a *lighter* panel, not the page background; verify with preflight rather than assuming) |
| Panel / card background | `#1e1a14` | `--surface` | often no equivalent — introduce as a *new* supplementary token, don't repurpose an existing one whose role is unclear |
| Hairline rules / borders | `#3a3226` | `--border` | `--secondary-color` (verify usage first) |
| Primary accent | `#cc7a4f` | `--accent` | `--accent-color` / `--primary-color` |
| Secondary accent tint (string/positive) | `#cfa77e` | `--accent2` | — |
| Tertiary accent tint (number/neutral) | `#b98a52` | `--accent3` | — |
| Quaternary accent tint (boolean-false/danger) | `#b6553c` | `--accent4` / `--danger` | — |
| Body text | `#f2ece1` | `--text` | `--text-color` |
| Muted/secondary text | `#9c9382` | `--muted` | usually no equivalent — new supplementary token |
| Code block background | `#141109` | `--code-bg` | `--code-bg` (name is consistent across almost every deck) |
| Code text | `#e4ddd0` | `--code-text` | `--code-text` (also consistent) |

The "newer-template" column matches `arrays-of-objects-and-data-driven-interfaces.html`,
`filter-search-find.html`, `functions-loops-generating-html.html`,
`javascript-dom-foundations.html`, `javascript-events-decisions.html`,
`toggle-everything.html`. Everything else in `slides/` is closer to the
"older-template" column, or has entirely bespoke names (`css-grid-layout.html`
uses `--accent-gold/--accent-green/--accent-red/--accent-teal`;
`responsive-design.html` uses `--card-bg/--card/--space-fluid`; etc.) — always
verify against that specific file's preflight output rather than assuming
either column applies.

It's fine, and expected, to add a handful of new supplementary tokens per
file for things the old template never needed (`--border-soft` for a
lower-contrast hairline, `--nav-h` for the nav bar height). New tokens are
low-risk since nothing depends on their name yet. Renaming or repurposing an
*existing* token is the risky move.

## Layout — the rail

Replaces the old centered `max-width: 860px` column.

```css
.slide{
  display:grid;
  grid-template-columns: 200px 1fr;
}
.rail{
  border-right:1px solid var(--border-soft, var(--border));
  padding:2.2rem 1.5rem;
  display:flex; flex-direction:column; justify-content:space-between;
}
.rail-top .kicker{
  font-size:.65rem; letter-spacing:.14em; text-transform:uppercase;
  color:var(--muted); font-weight:600; line-height:1.5;
}
.rail-num{
  font-family:'Fraunces',serif; font-weight:400; font-style:italic;
  font-size:3rem; color:var(--muted); opacity:.5;
  margin-top:1rem; font-variant-numeric:oldstyle-nums;
}
.rail-tag{
  font-size:.7rem; letter-spacing:.1em; text-transform:uppercase;
  color:var(--accent); font-weight:600;
  writing-mode:vertical-rl; transform:rotate(180deg);
  justify-self:start;
}
```

Markup per slide:

```html
<div class="slide">
  <div class="rail">
    <div class="rail-top">
      <div class="kicker">Deck Title<br>Line Two</div>
      <div class="rail-num">04</div>
    </div>
    <div class="rail-tag">Section Name</div>
  </div>
  <div class="main"><div class="main-inner">
    <!-- original slide-inner content goes here, unchanged -->
  </div></div>
</div>
```

The rail's slide number and section tag are cosmetic/orientational — safe to
introduce on every slide regardless of what that deck's original `.slide-tag`
said (carry the original tag text over into `.rail-tag` verbatim).

## No-scroll: fit-to-screen

```css
.main{ padding:2.6rem 4rem 2rem 3.2rem; overflow:hidden; }
.main-inner{ transform-origin: top left; }
```

```js
var MIN_SCALE = 0.72; // below this, the slide should be split instead

function fitSlide(slideEl){
  var main  = slideEl.querySelector('.main');
  var inner = slideEl.querySelector('.main-inner');
  if (!main || !inner) return; // full-embed slides have no .main-inner — skip

  inner.style.transform = 'none';
  inner.style.width = '100%';

  var cs = getComputedStyle(main);
  var available = main.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
  var natural = inner.scrollHeight;

  var scale = Math.min(1, available / natural);
  scale = Math.max(scale, MIN_SCALE);

  if (scale < 1) {
    inner.style.transform = 'scale(' + scale + ')';
    inner.style.width = (100 / scale) + '%';
  }
}
function fitCurrentSlide(){ fitSlide(slides[current]); }
```

Call `fitCurrentSlide()` at the end of the deck's existing `showSlide()`
function (add one line — this is layout, not logic, and doesn't touch any
protected identifier), and once more after fonts load:

```js
if (document.fonts && document.fonts.ready) {
  document.fonts.ready.then(fitCurrentSlide);
}
```

Also add a debounced `resize` listener that re-calls `fitCurrentSlide()`.

## Code blocks

```css
pre{
  background:var(--code-bg); border-top:1px solid var(--border); border-bottom:1px solid var(--border);
  padding:1.2rem 1.4rem; margin-bottom:1.4rem; max-width:82ch;
  font-family:'JetBrains Mono',monospace; font-size:clamp(.8rem,1.4vw,.9rem); line-height:1.7; color:var(--code-text);
  white-space:pre-wrap; overflow-wrap:anywhere;
}
```

Never touch the `<span class="kw">`/`.fn`/`.str`/`.num`/`.prop`/`.cmt` markup
around code tokens — only their color rules. Widening `pre` to `~82ch` (up
from the old `62ch`) uses the extra width the rail layout frees up, and
avoids most mid-line wraps now that horizontal scroll is gone.

## Analogies (replaces colored "highlight-box")

```css
.highlight-box{
  max-width:56ch; margin:1.4rem 0 1.6rem; padding-top:1.3rem;
  border-top:1px solid var(--border); position:relative;
  font-family:'Fraunces',serif; font-style:italic; font-weight:500;
  font-size:1.08rem; line-height:1.55; color:var(--text);
}
.highlight-box::before{
  content:'\201C'; font-family:'Fraunces',serif; font-size:2.8rem; color:var(--accent);
  position:absolute; top:.45rem; left:-2.1rem; line-height:1; opacity:.85;
}
.highlight-box strong{ font-style:normal; }
```

Keep the existing class name (`.highlight-box`, `.highlight`, or whatever
that specific deck uses) — only the rule body changes.

## Notes / cautions

```css
.note, .caution{ max-width:56ch; margin-bottom:1.4rem; padding-top:.75rem; border-top:1px solid var(--border-soft, var(--border)); font-size:.92rem; line-height:1.55; }
.caution{ background:rgba(204,122,79,.1); border-top:none; padding:.9rem 1.1rem; border-left:2px solid var(--accent); }
```

Reserve the accent-tinted background specifically for `.caution` — it's the
one place besides live demo output where color signals "pay attention."
`.note` stays quiet (just a hairline rule + text).

## Best-practices / Q&A → numbered index (replaces identical stacked cards)

```css
.index-list{ max-width:64ch; }
.index-item{ display:grid; grid-template-columns:3rem 1fr; gap:1.2rem; padding:1rem 0; border-top:1px solid var(--border-soft, var(--border)); }
.index-item:last-child{ border-bottom:1px solid var(--border-soft, var(--border)); }
.index-num{ font-family:'Fraunces',serif; font-style:italic; font-size:1.2rem; color:var(--accent); opacity:.8; }
.index-item dt{ font-family:'Fraunces',serif; font-weight:600; font-size:1.05rem; margin-bottom:.3rem; color:var(--text); }
.index-item dd{ font-size:.9rem; color:var(--muted); line-height:1.55; }
```

Only use numbering (`01`, `02`, `03`) when the list is genuinely a sequence
or the count itself is informative. A "best practices" list is really a set,
not a sequence — the numbers there are acting as a rhythm/index device, not
asserting order. If a future deck's list has a real ordinal meaning (steps in
a process), the same markup works and the numbers carry real information.
If in doubt, it's fine to drop `.index-num` and just use the ruled-list
structure without numbers.

## Demo widgets (buttons/inputs/live output)

**Keep every existing class name, id, and onclick handler untouched.** Only
these rule bodies change:

```css
.demo-box{
  background:var(--surface); border:1px solid var(--border-soft, var(--border));
  padding:1.2rem 1.4rem; margin-bottom:1.2rem; max-width:64ch;
}
.demo-box h4{
  font-size:.68rem; text-transform:uppercase; letter-spacing:.12em;
  color:var(--accent); margin-bottom:.9rem; font-weight:700;
}
.demo-btn{
  background:none; border:1px solid var(--border); color:var(--text);
  font-family:'JetBrains Mono',monospace; font-size:.82rem;
  padding:.5rem .9rem; cursor:pointer; transition:border-color .15s, background .15s, color .15s;
  margin:0 .4rem .4rem 0;
}
.demo-btn:hover{ border-color:var(--accent); }
.demo-btn:not(.secondary):not(.danger){ background:var(--accent); border-color:var(--accent); color:var(--bg); font-weight:600; }
.demo-btn.danger{ border-color:var(--accent4); color:var(--accent4); }
.demo-btn.danger:hover{ background:var(--accent4); color:var(--bg); }
.demo-output{
  background:var(--code-bg); border:1px solid var(--border-soft, var(--border));
  padding:.65rem .9rem; font-family:'JetBrains Mono',monospace; font-size:.85rem;
  min-height:2.2rem; margin-top:.5rem; display:flex; align-items:center; color:var(--muted);
}
```

This was verified against a real demo (`arrays-of-objects...html`'s "Object
Property Explorer") — clicked every button, confirmed the output text and
the JS-generated inline colors (`var(--accent2)` etc.) both resolved
correctly with zero script changes, because the variable *names* were kept
stable.

## Two-column comparisons

Used in all 25 decks — high priority to get right.

```css
.two-col{ display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-bottom:1.4rem; }
@media (max-width:600px){ .two-col{ grid-template-columns:1fr; } }
```

Style each column's heading/content using the same rules as everywhere else
(h3 treatment, pre treatment) — a two-col slide is not a special component,
just two content columns side by side. Don't add card backgrounds/borders
around each column; let the rail's left border and generous gap do the
separating.

## Reference tables

```css
.ref-table{ width:100%; border-collapse:collapse; font-size:clamp(.8rem,1.6vw,.92rem); margin-bottom:1.2rem; font-variant-numeric:tabular-nums; }
.ref-table th{ border-bottom:2px solid var(--border); padding:.6rem .9rem; text-align:left; color:var(--accent); font-weight:700; font-family:'Inter',sans-serif; }
.ref-table td{ border-bottom:1px solid var(--border-soft, var(--border)); padding:.6rem .9rem; vertical-align:top; }
```

Drop the boxed-cell look (border around every `td`) in favor of horizontal
rules only — reads closer to a printed reference table, less like a
spreadsheet grid.

## CodePen / iframe embeds (19 of 25 decks) — leave them alone

An earlier version of this doc proposed a special "full-bleed, edge to edge"
treatment for CodePen slides — no padding, iframe filling the whole frame.
Building that on `understanding-how-the-web-works.html` caused a real bug:
it was built on the unchecked assumption that a CodePen slide is *just* an
iframe, so the redesign silently dropped that slide's actual `<h1>` and
intro paragraph ("Creating a Sample File" / "Here's a simple HTML file...").
The content-diff script caught it, but it should never have been attempted
in the first place — with this many CodePen slides coming up, a special
case that requires re-deriving "does this slide also have text?" by hand
every time is exactly the kind of judgment call that quietly goes wrong.

The rule now: **a slide with a CodePen/iframe embed gets no special
treatment at all.** Wrap it in the rail + `.main`/`.slide-content` (or
`.main-inner`) scaffold exactly like every other slide, restyle its heading
and paragraph text the same as any other slide — and then stop. Do not
restyle `.codepen-container` or the iframe, do not change the iframe's
`width`/`height` attributes or inline styles, do not introduce a full-bleed
or edge-to-edge variant. Whatever CSS already governs the embed's container
stays exactly as authored; the fit-to-screen scale (if the slide needs it)
applies to the surrounding text and container the same way it would to any
other content. Always copy the iframe `src` verbatim — never regenerate or
"clean up" a CodePen URL.

If a genuinely iframe-only slide with zero heading/text ever turns up, it
still doesn't need special CSS — the standard slide padding around an
unstyled iframe is a fine, low-risk default. Design effort here is better
spent elsewhere; there's nothing to gain from a bespoke embed layout that's
worth the risk of silently eating real content again.

## Nav / progress bar

```css
#progress-bar{ position:fixed; top:0; left:0; height:2px; background:var(--accent); width:0%; transition:width .3s ease; z-index:100; }
nav{
  position:fixed; bottom:0; left:0; right:0; height:var(--nav-h, 44px);
  border-top:1px solid var(--border-soft, var(--border)); background:var(--bg);
  display:flex; align-items:center; justify-content:space-between; padding:0 1.6rem; z-index:50;
}
nav button{
  background:none; border:none; color:var(--muted);
  font-family:'Inter',sans-serif; font-size:.72rem; letter-spacing:.08em; text-transform:uppercase;
  font-weight:600; cursor:pointer; padding:.4rem 0;
}
nav button:hover:not(:disabled){ color:var(--text); }
nav button:disabled{ opacity:.25; cursor:default; }
#slide-counter{ font-size:.72rem; letter-spacing:.08em; color:var(--accent); font-variant-numeric:tabular-nums; }
```

Single-color progress bar (not the old two-color gradient) — consistent with
one restrained accent instead of a multi-hue palette.
