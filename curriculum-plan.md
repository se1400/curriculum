# Complete 28-Day Curriculum: HTML / CSS / JavaScript Introduction Course

---

## DAYS 1–12: EXISTING LESSONS (Already Built)

### Day 1: Understanding How the Web Works
**Topics & Concepts:**
- History of HTML and the World Wide Web (Tim Berners-Lee, 1990)
- What "web content" means vs. web pages
- The three core technologies: HTML (structure), CSS (presentation), JavaScript (behavior)
- How content travels from server to browser: the request/response cycle
- Local file viewing vs. remote hosting
- Selecting a web hosting provider
- Testing across multiple browsers (Safari, Chrome, Firefox, Edge, Opera)
- Why cross-browser testing matters
- Choosing and using a code editor (VS Code)
- Using FTP/SFTP to transfer files (FileZilla, Cyberduck)
- Understanding the document root and file organization
- The index.html file and default pages
- Modern deployment with Git and GitHub
- Blog and site publishing platforms (WordPress, Wix, Squarespace)

**Skills:**
- Understanding the web as a client/server system
- Setting up a local development environment
- Organizing project files and folders
- Uploading files to a web server

---

### Day 2: Structuring an HTML Document
**Topics & Concepts:**
- DOCTYPE declaration and why it matters
- Core document structure: `<html>`, `<head>`, `<body>`
- Tags every page must have (`<meta charset>`, `<title>`, viewport meta)
- Three types of HTML tags: container, void (self-closing), inline
- Using browser developer tools
- Paragraphs `<p>`, line breaks `<br>`, horizontal rules `<hr>`
- Headings `<h1>`–`<h6>` and document hierarchy
- The generic container `<div>`
- What semantic HTML means and why it matters (accessibility, SEO, readability)
- Semantic page layout elements: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`
- Nesting semantic elements correctly
- `<div>` vs. semantic elements — when to use each

**Skills:**
- Writing a valid, well-structured HTML document from scratch
- Choosing the right semantic element for content
- Reading HTML in browser DevTools

---

### Day 3: Text Formatting, Lists, and Tables
**Topics & Concepts:**
- HTML entities and special characters (`&copy;`, `&trade;`, `&amp;`, etc.)
- Bold and italic: `<b>` vs `<strong>`, `<i>` vs `<em>` — semantic difference
- Using web fonts and Google Fonts (`<link>` in head)
- Variable fonts
- Text alignment in CSS
- Unordered lists `<ul>` and `<li>`
- Ordered lists `<ol>` and list type attributes
- Description lists `<dl>`, `<dt>`, `<dd>`
- Nesting lists
- CSS list styling: `list-style-type`, `list-style-image`, `list-style-position`
- HTML tables: `<table>`, `<tr>`, `<td>`, `<th>`
- Table structure: `<thead>`, `<tbody>`, `<tfoot>`
- Spanning cells: `colspan`, `rowspan`
- Table styling with CSS
- CSS multi-column layout: `column-count`, `column-gap`, `column-rule`

**Skills:**
- Marking up content with the correct text-level elements
- Building accessible, well-structured lists
- Creating and styling data tables
- Using Google Fonts in a project

---

### Day 4: Introduction to JavaScript
**Topics & Concepts:**
- What scripts are vs. compiled programs
- How JavaScript fits into a web page
- Placing scripts in `<body>` vs `<head>` — and why `defer` matters
- Inline event handlers (onclick, onmouseover) — the old way
- Using separate `.js` files — the right way
- Understanding JavaScript events
- Mouse events, keyboard events, page events, form events
- JavaScript variables: `let`, `const`, `var` — brief introduction
- The `Date` object and its methods (`getFullYear`, `getMonth`, `getDate`, `getHours`)
- Displaying and formatting time with JavaScript
- Introduction to browser developer tools for JavaScript
- `console.log()` for debugging
- `console.table()`, `console.warn()`, `console.error()`, `console.time()`
- Types of JavaScript errors: SyntaxError, ReferenceError, TypeError
- Reading error messages: type, description, file, line number
- Handling errors with `try`/`catch` blocks
- JavaScript best practices overview

**Skills:**
- Linking a JavaScript file to an HTML page
- Using the console to test and debug code
- Reading and interpreting error messages
- Writing a basic event handler

---

### Day 5: Validating and Debugging Your Code
**Topics & Concepts:**
- Why validation matters: catching errors, enforcing standards
- W3C HTML Validation Service (by URI, file upload, direct input)
- W3C CSS Validation Service
- Modern linting tools: ESLint, Stylelint
- Accessibility validation: WAVE, WebAIM Contrast Checker
- Browser DevTools: opening and navigating panels
- The Elements/Inspector panel: viewing and editing live HTML and CSS
- Common HTML errors: unclosed tags, mismatched tags, typos
- Debugging CSS with computed styles, box model view
- Grid Inspector and Flexbox Inspector
- The Console panel: errors, warnings, info, logs
- Understanding stack traces
- The Sources/Debugger panel
- Setting breakpoints and stepping through code (Step Over, Step Into, Step Out)
- Watching variables and inspecting scope (local, closure, global)
- The Network panel: finding 404 errors, slow resources, API calls
- Understanding source maps, minified and transpiled code

**Skills:**
- Validating HTML and CSS against W3C standards
- Using DevTools to inspect and fix layout issues
- Setting breakpoints and stepping through JavaScript
- Diagnosing network errors and 404s

---

### Day 6: Understanding Style Sheets (CSS)
**Topics & Concepts:**
- What CSS is and how it works
- Internal styles (`<style>` in `<head>`) vs. external stylesheets (`<link>`)
- The Cascade: specificity, source order, `!important`
- Specificity scoring: inline > ID > class > element
- Basic CSS rule syntax: selector, property, value
- Element selectors, class selectors (`.`), ID selectors (`#`)
- Grouping selectors with commas
- Descendant, child (`>`), adjacent sibling (`+`), general sibling (`~`) combinators
- `display` property: `block`, `inline`, `inline-block`, `none`
- Absolute units: `px`, `pt`, `in`, `cm`
- Relative units: `em`, `rem`, `%`, `vw`, `vh`, `ch`
- Border properties: `border-width`, `border-color`, `border-style`, `border-radius`
- Border styles: solid, dashed, dotted, double, groove, ridge, inset, outset
- Color properties: `color`, `background-color`
- Color formats: named colors, hexadecimal, RGB, RGBa
- Font properties: `font-family`, `font-size`, `font-weight`, `font-style`, `line-height`, `letter-spacing`
- CSS Custom Properties (variables): `--property-name` and `var()`
- Logical properties: `margin-inline-start`, `padding-block-end`
- Introduction to responsive design: relative units, media queries, flexible layouts

**Skills:**
- Writing CSS rules with correct syntax
- Understanding and calculating specificity
- Using relative units for responsive sizing
- Defining and using CSS custom properties

---

### Day 7: Colors, Graphics, and Multimedia
**Topics & Concepts:**
- Choosing colors: natural palettes, accessible combinations
- WCAG 2.1 contrast requirements: 4.5:1 for normal text, 3:1 for large text
- Building small, cohesive color palettes (3–4 main + 1–2 accent)
- Dark mode consideration: `prefers-color-scheme`
- Color tools: Paletton, Adobe Color
- Hexadecimal color values and shorthand (`#fff` vs `#ffffff`)
- RGB and RGBa color values
- HSL and HSLa: Hue (0–360), Saturation (0–100%), Lightness (0–100%)
- CSS Custom Properties for color theming
- Graphics software: Photoshop, Illustrator, GIMP, Figma, Canva
- Raster image formats: JPEG (photos, lossy), PNG (transparency, lossless), GIF (animation, 256 colors)
- Modern image formats: WebP (25–35% smaller than JPEG), AVIF (50% smaller), SVG (vector, scalable)
- Image optimization: file size, resolution, compression
- Composition: rule of thirds, cropping, resizing (never upscale)
- The `<img>` tag: `src`, `alt`, `width`, `height`, `loading="lazy"`
- Writing meaningful alt text for accessibility
- Responsive images: `srcset`, `sizes`, the `<picture>` element
- HTML audio: `<audio>` element, `controls`, `autoplay`, `loop`, file formats (MP3, OGG, WAV)
- HTML video: `<video>` element, `controls`, `poster`, `muted`, `autoplay`, `loop`, file formats (MP4, WebM)
- Closed captions and accessibility for media

**Skills:**
- Choosing accessible color combinations that meet WCAG
- Selecting the right image format for each use case
- Optimizing images for the web
- Writing descriptive alt text
- Embedding audio and video with fallbacks

---

### Day 8: CSS Backgrounds and Borders
**Topics & Concepts:**
- The `background` shorthand property
- `background-color`, `background-image`, `background-repeat`, `background-position`, `background-size`
- `background-size` values: `cover`, `contain`, exact values
- `background-attachment`: `scroll`, `fixed` (parallax effect), `local`
- `background-clip`: `border-box`, `padding-box`, `content-box`, `text` (gradient text)
- `background-origin`: controlling where background starts
- Layering multiple backgrounds with comma-separated values
- Blending backgrounds: `background-blend-mode`, `mix-blend-mode`
- Frosted glass effect: `backdrop-filter: blur()`
- CSS Linear gradients: direction, angles, color stops
- Repeating linear gradients for patterns
- CSS Radial gradients: shape, size keywords (`closest-side`, `farthest-corner`)
- CSS Conic gradients: color wheel effects, pie charts
- Border shorthand and individual side properties
- Border styles in depth: solid, dashed, dotted, double, groove, ridge
- Faking multiple borders with `box-shadow`
- `border-radius`: rounded corners, circles, ellipses, individual corners
- `border-image`: using images as borders
- Outlines vs. borders: `outline` does not affect layout
- `:focus-visible` for accessible keyboard focus styles
- `:nth-child()` selectors: `even`, `odd`, formulas like `3n+1`
- Zebra-stripe tables with `:nth-child()`

**Skills:**
- Building complex background treatments with layered images and gradients
- Creating decorative effects with `backdrop-filter` and blend modes
- Using `border-image` and `border-radius` for styled elements
- Writing accessible focus styles

---

### Day 9: Margins, Padding, Alignment, and Floats
**Topics & Concepts:**
- Margins: space outside an element
- Margin shorthand: TRBL — Top, Right, Bottom, Left
- One value (all sides), two values (top/bottom, left/right), three values, four values
- Negative margins and their uses
- `margin: auto` for horizontal centering
- Removing default browser margins on `<body>`
- Margin collapse: when vertical margins merge — and when they don't
- Why `rem` and `em` are preferred over `px` for spacing
- Padding: space inside an element between content and border
- Padding shorthand (same TRBL pattern as margin)
- Visual impact of padding on element size (default `content-box` model)
- Margin vs. padding decision guide: outside vs. inside spacing
- The `float` property: `left`, `right`, `none`
- Float behavior: text wrapping around floated elements
- The `clear` property: `left`, `right`, `both`
- Clearfix technique for containing floated children
- When to use float today (text wrap around images — its original purpose)
- Modern centering techniques: Flexbox, Grid, `margin: auto`

**Skills:**
- Controlling spacing inside and outside elements with precision
- Using margin shorthand fluently
- Understanding and preventing margin collapse
- Floating images with wrapped text

---

### Day 10: Box Model, Positioning, and Flexbox
**Topics & Concepts:**
- The CSS Box Model: content → padding → border → margin
- How element size is calculated in `content-box` (default)
- `box-sizing: border-box` — padding and border included in width
- Universal `box-sizing` reset: `*, *::before, *::after { box-sizing: border-box }`
- Borders vs. outlines: outlines don't affect layout
- CSS positioning: `static` (default), `relative`, `absolute`, `fixed`, `sticky`
- Relative positioning: offset from normal position, still in flow
- Absolute positioning: removed from flow, positioned to nearest positioned ancestor
- Fixed positioning: relative to viewport, stays on scroll
- Sticky positioning: hybrid — in flow until threshold, then fixed
- Stacking context and `z-index`: controlling which elements appear on top
- Why flexbox? Problems it solves over floats
- `display: flex` and the flex container
- Main axis vs. cross axis
- `flex-direction`: `row`, `column`, `row-reverse`, `column-reverse`
- `justify-content`: `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly`
- `align-items`: `stretch`, `flex-start`, `flex-end`, `center`, `baseline`
- `flex-wrap` and the `gap` property
- Flex item properties: `flex-grow`, `flex-shrink`, `flex-basis`
- The `flex` shorthand: `flex: 1`, `flex: 0 0 200px`
- `order` property and individual alignment with `align-self`
- Practical Flexbox patterns: navigation bars, card rows, centering
- Common Flexbox pitfalls and fixes
- Flexbox vs. Grid vs. positioning: when to use which

**Skills:**
- Using `border-box` sizing throughout a project
- Positioning elements with `absolute`/`fixed`/`sticky` confidently
- Managing z-index stacking
- Building responsive layouts with Flexbox

---

### Day 11: Hyperlinks and Navigation
**Topics & Concepts:**
- Anchor tag `<a>`: `href`, `target`, `rel="noopener noreferrer"` for security
- Absolute vs. relative URLs
- Linking to sections with ID anchors (`href="#section-id"`)
- `mailto:` and `tel:` links
- Link pseudo-classes: `:link`, `:visited`, `:hover`, `:focus`, `:active` — and LVHFA order
- Why lists are the semantic foundation of navigation
- Stripping default list styles: `list-style: none`, `margin: 0`, `padding: 0`
- `display: block` on links for larger click targets
- Styling hover and focus states: visual feedback for keyboard users
- Building vertical (sidebar) navigation with block links
- Building horizontal navigation with Flexbox
- Creating dropdown menus with CSS `position: absolute` + `:hover`/`:focus-within`
- Multi-level (fly-out) dropdowns
- Fixed navigation bars: stays at top on scroll
- Sticky navigation: in flow until scroll threshold
- Polished hover effects: animated underlines with `::after` and transitions
- Accessible navigation: `aria-label` on `<nav>`, `aria-current="page"` for active links

**Skills:**
- Building accessible navigation from semantic HTML
- Creating dropdown menus with CSS only
- Styling link states in the correct order
- Making navigation keyboard-accessible

---

### Day 12: CSS Grid Layout
**Topics & Concepts:**
- The history: fixed vs. liquid layouts, floats, then Flexbox, then Grid
- What CSS Grid is: a two-dimensional layout system
- `display: grid` activating a grid container
- Implicit vs. explicit grids
- `grid-template-columns` and `grid-template-rows`
- Pixel, percentage, and `fr` (fractional) unit
- The `repeat()` function: `repeat(3, 1fr)`
- `minmax()` function: `minmax(200px, 1fr)`
- `auto-fill` vs. `auto-fit` with `minmax()` for intrinsic responsive grids
- `gap`, `row-gap`, `column-gap`
- Auto-placement and `grid-auto-flow`: `row` vs. `column`
- Line-based placement: `grid-column: 1 / 3`, `grid-row: 2 / 4`
- `span` keyword: `grid-column: span 2`
- Named grid areas: `grid-template-areas` as a visual layout map
- `grid-area` on items to place them by name
- Layout rearrangement with named areas at different breakpoints
- Grid alignment: `justify-items`, `align-items`, `justify-content`, `align-content`
- Individual item alignment: `justify-self`, `align-self`
- Overlapping grid items with `z-index`
- Subgrid: nested grids that align to the parent grid's tracks
- Grid vs. Flexbox decision guide: 2D vs. 1D

**Skills:**
- Creating responsive grid layouts without media queries using `auto-fill`/`minmax()`
- Placing items precisely using line numbers and named areas
- Rearranging layout at different screen sizes with named areas
- Choosing between Grid and Flexbox for a given layout

---

## DAYS 13–17: HTML/CSS COMPLETION (New Lessons)

### Day 13: HTML Forms & Form Accessibility
**Topics & Concepts:**
- Why forms are critical — the primary way users send data
- The `<form>` element: `action`, `method` (GET vs. POST)
- Always pairing `<label>` with `<input>`: `for`/`id` association or wrapping
- Text-type inputs: `text`, `email`, `password`, `url`, `tel`, `search`, `number`
- Date and time inputs: `date`, `time`, `datetime-local`, `month`, `week`
- Selection inputs: `checkbox`, `radio`, `range`, `color`
- The `<select>` element with `<option>` and `<optgroup>`
- The `<textarea>` element: `rows`, `cols`, CSS `resize`
- The `<datalist>` element for autocomplete suggestions
- `<fieldset>` and `<legend>` for grouping related fields
- Hidden inputs: `<input type="hidden">`
- The `<output>` element for calculated results
- `<button>` element vs. `<input type="submit">` — when and why
- HTML5 validation attributes: `required`, `minlength`, `maxlength`, `min`, `max`, `pattern`, `step`
- The `placeholder` attribute — hints, not labels
- The `autocomplete` attribute for improved UX
- Form-related pseudo-classes: `:valid`, `:invalid`, `:required`, `:optional`, `:placeholder-shown`, `:focus`
- Form accessibility: `aria-describedby` for help text, `aria-invalid` for errors, logical tab order
- The `novalidate` attribute for custom JS validation

**Skills:**
- Building complete, accessible HTML forms
- Using HTML5 built-in validation attributes
- Grouping related form controls with `fieldset` and `legend`
- Associating labels with inputs correctly

---

### Day 14: CSS Transitions & Transforms
**Topics & Concepts:**

**Transitions:**
- What CSS transitions are — smoothly animating between two property states
- `transition-property`: which property to animate
- `transition-duration`: how long the transition takes
- `transition-timing-function`: the speed curve
- `transition-delay`: waiting before starting
- The `transition` shorthand: `property duration timing-function delay`
- Timing function values: `ease`, `linear`, `ease-in`, `ease-out`, `ease-in-out`
- `cubic-bezier()` for custom easing curves
- `steps()` function for discrete (non-smooth) animation
- Which properties can and cannot be transitioned (animatable properties)
- Performance: `transform` and `opacity` are GPU-accelerated — prefer them
- Transitioning on `:hover`, `:focus`, class additions via JS

**2D Transforms:**
- `translate(x, y)`, `translateX()`, `translateY()` — moving elements
- `rotate(deg)` — spinning elements
- `scale(x, y)`, `scaleX()`, `scaleY()` — resizing
- `skew(x, y)`, `skewX()`, `skewY()` — shearing/distorting
- `transform-origin` — the pivot point (default: center)
- Combining multiple transforms in one declaration
- `transform: translateX(-50%) translateY(-50%)` for centering trick

**3D Transforms:**
- `perspective` property — establishing depth on a parent
- `rotateX()`, `rotateY()`, `rotateZ()`, `rotate3d()`
- `translateZ()`, `translate3d()`
- `transform-style: preserve-3d` — maintaining 3D context for children
- `backface-visibility` — hiding the back of a flipped element

**Skills:**
- Applying smooth hover transitions to interactive elements
- Moving, rotating, and scaling elements with transforms
- Building a CSS card flip effect with 3D transforms
- Understanding performance implications of different animatable properties

---

### Day 15: CSS Animations & Pseudo-elements
**Topics & Concepts:**

**CSS Animations:**
- `@keyframes` — defining multi-step animation sequences
- `from` / `to` vs. percentage-based keyframes (`0%`, `50%`, `100%`)
- `animation-name` — referencing a `@keyframes` block
- `animation-duration` — how long one cycle takes
- `animation-timing-function` — easing across the animation
- `animation-delay` — waiting before starting
- `animation-iteration-count`: a number or `infinite`
- `animation-direction`: `normal`, `reverse`, `alternate`, `alternate-reverse`
- `animation-fill-mode`: `none`, `forwards`, `backwards`, `both`
- `animation-play-state`: `running`, `paused` (toggle with JS)
- The `animation` shorthand
- Combining animations with transforms for rich motion
- Layering multiple animations on one element (comma-separated)
- Performance: prefer `transform` and `opacity`, avoid animating layout properties
- `will-change` property — use sparingly as a hint to the browser
- Modern: Scroll-driven animations with `animation-timeline: scroll()`

**Pseudo-elements:**
- `::before` and `::after` — inserting generated content before/after an element
- The `content` property: string, `attr()`, `counter()`, empty string `""`
- Pseudo-elements must have `content` to appear
- Positioning pseudo-elements with `position: absolute`
- Using pseudo-elements for decorative shapes and overlays
- `::placeholder` — styling placeholder text in form inputs
- `::selection` — styling highlighted/selected text
- `::marker` — styling list item markers (bullets, numbers)
- `::first-line` — styling the first line of a paragraph
- `::first-letter` — styling the first letter (drop caps)
- Practical patterns: tooltip arrows, quotation marks, decorative dividers, badge counters

**Skills:**
- Writing multi-step `@keyframes` animations
- Controlling animation direction, fill mode, and play state
- Using `::before` and `::after` for decorative CSS effects
- Styling form placeholder text and selected text

---

### Day 16: Responsive Web Design
**Topics & Concepts:**
- What responsive design is and the problem it solves
- Mobile-first design philosophy: start simple, add complexity upward
- The viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- Why the viewport meta tag is required
- CSS `@media` queries syntax: `@media (min-width: 768px) { }`
- `min-width` (mobile-first) vs. `max-width` (desktop-first) — why `min-width` wins
- Common breakpoint strategies: based on content, not specific device sizes
- Typical breakpoint ranges: small (< 640px), medium (640–1024px), large (> 1024px)
- Responsive typography with `clamp()`: `font-size: clamp(1rem, 2.5vw, 2rem)`
- Fluid spacing with `clamp()` for margins and padding
- Responsive images review: `srcset`, `sizes`, `<picture>` element
- `max-width: 100%` on images to prevent overflow
- `object-fit`: `cover`, `contain`, `fill` for image sizing within a container
- Responsive layout patterns: single column → two column → three column
- Stack-to-row pattern with Flexbox: wrapping at breakpoints
- Grid with `auto-fill` / `minmax()`: intrinsically responsive without media queries
- Responsive navigation: hamburger menus, priority+ navigation
- Hiding/showing elements at breakpoints with `display: none`
- `aspect-ratio` property for maintaining proportions of media
- Testing responsive designs with browser DevTools device emulation
- Container queries: `@container` — responsive to the element's parent, not the viewport
- Container query syntax: `container-type`, `container-name`, `@container (min-width:)`
- When to use container queries vs. media queries

**Skills:**
- Writing mobile-first CSS with `@media (min-width)` queries
- Using `clamp()` for fluid typography and spacing
- Building intrinsically responsive grids with `auto-fill` + `minmax()`
- Using container queries for component-level responsiveness

---

### Day 17: Modern CSS & Accessibility (Dense Day)
**Topics & Concepts:**

**Modern CSS Features:**
- CSS Nesting — writing nested selectors natively without a preprocessor
- Nesting syntax: `&` represents the parent selector
- Nesting pseudo-classes: `&:hover`, `&:focus-within`
- Nesting media queries inside a rule: `@media` inside a selector block
- `:has()` — the "parent selector": style a parent based on its children
- Practical `:has()` use cases: `form:has(:invalid)`, `li:has(img)`
- `:is()` — matching any selector in a list, takes the highest specificity of its arguments
- `:where()` — same as `:is()` but always zero specificity (safe for overriding)
- Using `:is()` and `:where()` to reduce repetitive selectors
- `@layer` — CSS Cascade Layers for managing specificity at scale
- Declaring layers: `@layer base, components, utilities`
- Styles in lower layers lose to styles in higher layers regardless of specificity
- `color-mix()` — mixing two colors in a given color space: `color-mix(in srgb, red 30%, blue)`
- `light-dark()` — returns different values based on the user's color scheme
- `prefers-color-scheme` media query: `@media (prefers-color-scheme: dark)`
- `prefers-reduced-motion` media query — respecting user motion preferences
- `@supports` — feature queries for progressive enhancement: `@supports (display: grid)`
- Recap of modern features already covered: CSS variables, logical properties, container queries, subgrid

**Accessibility Deep Dive:**
- Why accessibility matters: legal (ADA, Section 508, WCAG), ethical, and business case
- The Web Content Accessibility Guidelines (WCAG): levels A, AA, AAA
- The accessibility tree — how browsers expose content to assistive technology
- Semantic HTML as the #1 accessibility tool
- ARIA roles: `role="navigation"`, `role="dialog"`, `role="alert"`, `role="tab"`, `role="tabpanel"`, `role="banner"`, `role="complementary"`, `role="contentinfo"`
- The first rule of ARIA: don't use ARIA if native HTML can do it
- ARIA labels: `aria-label`, `aria-labelledby`, `aria-describedby`
- ARIA states: `aria-expanded`, `aria-hidden`, `aria-live`, `aria-current`, `aria-selected`, `aria-checked`, `aria-disabled`
- Live regions: `aria-live="polite"` vs. `aria-live="assertive"` for dynamic content announcements
- Focus management: `tabindex="0"` (in tab order), `tabindex="-1"` (programmatic focus only)
- Avoid positive `tabindex` values — they break natural tab order
- Focus trapping for modals and dialogs
- Skip navigation links for keyboard users
- Keyboard navigation: all interactive elements must be reachable and operable by keyboard
- Screen reader testing: VoiceOver (Mac/iOS), NVDA (Windows), TalkBack (Android)
- Accessible color contrast review (building on Day 7's WCAG coverage)
- Accessible forms review (building on Day 13 — error association, required indicators)
- Accessible images: meaningful alt text vs. decorative `alt=""`
- Common accessibility mistakes: missing alt text, low contrast, inaccessible modals, keyboard traps, auto-playing media
- Accessibility testing tools: browser Lighthouse audit, axe DevTools extension, WAVE

**Skills:**
- Writing nested CSS without a preprocessor
- Using `:has()` to style parent elements based on their contents
- Implementing system dark mode with `prefers-color-scheme` and `light-dark()`
- Auditing a page with Lighthouse and axe for accessibility violations
- Adding ARIA attributes correctly to custom interactive components

---

## DAYS 18–28: JAVASCRIPT FUNDAMENTALS (New Lessons — DOM-First, Visual Approach)

### Day 18: JavaScript Foundations — Variables & Values for the Browser
**Visual-First Approach:** Every code example produces visible output on screen — no console.log-only examples. Frame the lesson around: "Variables are tools for controlling what users see on the page."
**Topics & Concepts:**
- Opening: "Variables in the Browser" — show `document.querySelector('h1').textContent = "Hello, " + name;` before any theory
- `let` — block-scoped, can be reassigned
- `const` — block-scoped, cannot be reassigned (but object/array contents can change)
- `var` — legacy (function scoping, hoisting, no block scope) — avoid
- Block scope and Temporal Dead Zone (brief — one sentence on TDZ)
- The five core primitives: `string`, `number`, `boolean`, `null`, `undefined`
- BigInt — one sentence only: represents integers larger than JS can handle — rarely needed
- Symbol — one sentence only: used inside frameworks — not needed as a beginner
- Template literals: `${expression}` interpolation, multiline strings
- String concatenation with `+`
- Numbers: integers, floats, `NaN`, `Infinity`
- The `Math` object: `Math.floor()`, `Math.ceil()`, `Math.round()`, `Math.random()`
- Truthy and falsy values: `0`, `""`, `null`, `undefined`, `NaN`, `false` are falsy
- `===` vs `==` — strict equality always; DOM bug examples showing why `==` causes problems
- Type coercion: keep `===` vs `==` — do not cover exotic coercion tables
- The `typeof` operator
- Converting between types: `Number()`, `String()`, `Boolean()`, `parseInt()`, `parseFloat()`

**Changes from original:** Cut BigInt section, cut Symbol section, reduce hoisting coverage, cut exotic coercion tables, remove structuredClone (moved to Day 25 Objects), replace all console.log with DOM output examples.

**Skills:**
- Declaring variables correctly with `let` and `const`
- Identifying data types with `typeof`
- Using template literals for string construction
- Generating random numbers with `Math.random()`
- Avoiding type coercion bugs with strict equality
- Updating DOM elements to display variable values on screen

---

### Day 19: The DOM — Selecting & Manipulating Elements
**Visual-First Approach:** Already strong (4/5). Minor cleanup only.
**Topics & Concepts:**
- What the DOM is: the browser's live, object-based representation of the HTML document
- The DOM tree: `document` → `html` → `head` / `body` → elements → text nodes
- Why the DOM is the bridge between HTML/CSS and JavaScript
- `document.querySelector(selector)` — select the first matching element (uses CSS selector syntax)
- `document.querySelectorAll(selector)` — select all matching elements (returns a NodeList)
- NodeList vs array (simplified): `querySelectorAll` + `forEach` covers 95% of use cases; use `Array.from()` only when you need `filter`/`map`
- Legacy selectors for awareness: `getElementById()`, `getElementsByClassName()`, `getElementsByTagName()`
- Reading text content: `element.textContent` (plain text), `element.innerHTML` (HTML markup), `element.innerText` (rendered text)
- Setting content: `element.textContent = "..."`, `element.innerHTML = "<strong>...</strong>"`
- Security warning: never set `innerHTML` from user input (XSS risk)
- Reading and writing attributes: `getAttribute()`, `setAttribute()`, `removeAttribute()`, `hasAttribute()`
- `data-*` attributes and the `dataset` property: `element.dataset.userId`
- Modifying inline styles: `element.style.color = "red"` (camelCase properties)
- The `classList` API: `classList.add()`, `classList.remove()`, `classList.toggle()`, `classList.contains()`, `classList.replace()`
- Why `classList` is preferred over `className` string manipulation
- Creating new elements: `document.createElement("div")`
- Setting content/attributes on a new element before inserting
- Inserting elements: `parent.appendChild(child)`, `parent.prepend(child)`, `element.before()`, `element.after()`, `parent.insertAdjacentHTML(position, html)`
- `insertAdjacentHTML` positions: `"beforebegin"`, `"afterbegin"`, `"beforeend"`, `"afterend"`
- Removing elements: `element.remove()`
- DOM traversal: `element.parentElement`, `element.children`, `element.firstElementChild`, `element.lastElementChild`, `element.nextElementSibling`, `element.previousElementSibling`

**Changes from original:** Simplify NodeList/Array conversion message; audit any console.log-only examples.

**Skills:**
- Selecting elements by tag, class, ID, attribute, and complex CSS selectors
- Reading and updating text, HTML, and attributes on the page
- Using `classList` to add/remove CSS classes from elements
- Creating elements and inserting them into the DOM
- Traversing the DOM tree to find related elements

---

### Day 20: DOM Events & Event Handling
**Visual-First Approach:** Moderate revision — cut advanced APIs that distract beginners.
**Topics & Concepts:**
- What events are: signals from the browser that something happened
- The modern approach: `element.addEventListener(type, handler)` — preferred over inline HTML handlers
- Why `addEventListener` is better than `onclick = function(){}`: multiple listeners, separation of concerns
- Common events: `click`, `submit` (with `preventDefault`), `change`, `input`, `keydown`, `keyup`, `focus`, `blur`, `mouseover`, `mouseout`
- The event object: `event.target`, `event.type`, `event.key`, `event.preventDefault()`
- `event.target` — the element that was actually clicked/interacted with
- `event.currentTarget` — the element the listener is attached to
- `input` vs `change`: `input` fires on every keystroke, `change` fires on blur/commit
- Window events: `DOMContentLoaded`, `load`, `resize`, `scroll`
- `DOMContentLoaded` vs `load`: DOM ready vs all assets loaded
- Event bubbling: events propagate up from child to parent
- Event capturing: ONE paragraph — events travel down then bubble up; you almost always use bubbling (third arg `true` to addEventListener)
- `event.stopPropagation()` — preventing an event from bubbling further
- Event delegation: attaching one listener to a parent instead of many listeners on children
- Why delegation matters: works for dynamically added elements, better performance
- Pattern for delegation: check `event.target.matches(selector)` inside the handler
- Removing event listeners: `element.removeEventListener(type, handler)` — requires named function reference
- Pointer Events: ONE paragraph + one snippet — modern way to handle mouse AND touch input
- AbortController: ONE paragraph — cancel multiple listeners at once; `removeEventListener` covers most needs

**Changes from original:** Reduce Pointer Events, event capture, AbortController to brief paragraphs; expand practical events coverage.

**Skills:**
- Adding and removing event listeners correctly
- Using the event object to get information about what happened
- Preventing default browser behavior with `event.preventDefault()`
- Distinguishing between different event types and when to use each
- Implementing event delegation for dynamic lists

---

### Day 21: Control Flow
**Visual-First Approach:** Substantial revision — DOM context for all examples.
**Topics & Concepts:**
- Opening: shipping calculator (or simpler version) shown FIRST as motivation — the visual payoff before the theory
- `if` / `else if` / `else`
- Truthy and falsy recap
- Comparison operators: `===`, `!==`, `>`, `<`, `>=`, `<=`
- Logical operators: `&&`, `||`, `!` — with DOM examples: `if (username && password) { loginBtn.disabled = false; }`
- Short-circuit evaluation: `&&` returns first falsy, `||` returns first truthy
- Nullish coalescing operator `??`: returns right side only if left is `null` or `undefined`
- Optional chaining `?.`: safely accessing nested properties — `object?.property`, `object?.method?.()`
- The ternary operator: shown updating `textContent` — `isValid ? "✓ Valid" : "✗ Invalid"`
- Logical assignment operators `&&=`, `||=`, `??=` — brief, one DOM example each
- The `switch` statement: reframed around visible UI — a theme switcher changing a CSS class

**Changes from original:** Move shipping calculator up to opening; replace console.log examples with DOM scenarios; remove Object.groupBy() (students don't know objects yet — moved to Day 27).

**Skills:**
- Writing if/else chains to handle multiple cases
- Using the ternary operator for concise conditional expressions
- Using switch statements for multi-case decisions
- Safely accessing nested data with optional chaining
- Using `??` and logical assignment operators in real DOM scenarios

---

### Day 22: Functions
**Visual-First Approach:** Substantial revision — cut advanced patterns, add DOM context.
**Topics & Concepts:**
- What functions are: named, reusable blocks of code
- Why functions matter: DRY (Don't Repeat Yourself), organization, readability
- Function declarations: `function name(params) { body }` — hoisted
- Function expressions: `const name = function(params) { body }` — not hoisted
- Arrow functions: `const name = (params) => { body }` — concise syntax
- Arrow function shorthand: single parameter needs no parens `x => x * 2`
- Arrow function implicit return: no curly braces returns the expression `x => x * 2`
- Parameters vs. arguments: the difference between definition and call
- Default parameters: `function greet(name = "World") { }`
- Rest parameters: `function sum(...numbers) { }` — collects remaining args into array
- The `return` keyword — exiting a function and passing back a value
- Scope: global, function, block — with a DOM example showing outer scope access
- The scope chain: how JS looks up variable names outward through nested scopes
- Closures — with a VISIBLE DOM counter example:
  ```js
  function createCounter(buttonEl, displayEl) {
    let count = 0;
    buttonEl.addEventListener('click', () => { count++; displayEl.textContent = count; });
  }
  ```
- Callbacks — explicitly connected to event listeners: "Every addEventListener callback is a function callback"
- Named function expressions — brief, framed as a debugging tip
- IIFE (immediately invoked function expression) — brief
- Higher-order functions preview

**Changes from original:** Delete "A Taste of Advanced Patterns" section entirely (currying, generators, top-level await); add DOM closure example; connect callbacks to event handlers; add DOM example to scope section.

**Skills:**
- Writing functions with declarations, expressions, and arrow syntax
- Using default and rest parameters
- Understanding the difference between parameters and arguments
- Explaining and navigating scope in a program
- Passing functions as callbacks
- Using closures to maintain state across DOM interactions

---

### Day 23: Loops & Generating HTML
**Visual-First Approach:** Already excellent (5/5). Minor restructure only.
**Topics & Concepts:**
- Opening: Show the HTML-generation payoff FIRST — a 5-line snippet turning a products array into rendered cards — BEFORE teaching loop syntax
- The `for` loop: `for (initialization; condition; increment)`
- Loop counter variables by convention: `i`, `j`, `k`
- Counting up, counting down, custom increments
- The `while` loop: `while (condition)` — for when the number of iterations is unknown
- The `do...while` loop: one paragraph + one example only — always runs at least once
- The `for...of` loop: the modern loop for arrays and iterables
- `for...in` REMOVED — replaced with: "`for...in` iterates object keys — don't use it on arrays. Use `Object.entries()` for objects, `for...of` for arrays." (one sentence)
- `break` — exit the loop immediately
- `continue` — skip the rest of this iteration, go to the next
- Labels with `break`/`continue` for nested loops (brief)
- Accumulator pattern (trimmed 20% from original)
- Nested loops: a loop inside a loop (use sparingly)
- Generating HTML with loops — the visual payoff (expanded): template literals inside loops, inserting with `innerHTML`

**Changes from original:** Add payoff preview at top; trim console.log patterns ~20%; remove `for...in` section; reduce `do...while` coverage.

**Skills:**
- Writing `for`, `while`, and `for...of` loops correctly
- Using `break` and `continue` strategically
- Generating HTML markup dynamically with a loop
- Inserting loop-generated HTML into the DOM

---

### Day 24: Arrays — Core Methods
**Visual Frame:** Interactive to-do list where every method has a visible effect on screen.
**Topics & Concepts:**
- What arrays are: ordered, zero-indexed collections
- Creating: `[]` literal, `Array.of()`, `Array.from()`
- Reading: `array[0]`, `array.at(-1)` (negative indexing), `array.length`
- **Mutating methods (change original array):**
  - `push(item)` — add to end, returns new length
  - `pop()` — remove from end, returns removed item
  - `unshift(item)` — add to beginning
  - `shift()` — remove from beginning
  - `splice(start, deleteCount, ...items)` — remove, replace, or insert at a position
  - `reverse()` — reverse in place
  - `sort(compareFn)` — sort in place (numeric needs comparator)
- **Non-mutating methods (return new array, don't change original):**
  - `slice(start, end)` — extract a portion into a new array
  - `concat(...arrays)` — merge arrays
  - `toReversed()`, `toSorted()`, `toSpliced()`, `with()` — ES2023 non-mutating versions
- Finding: `indexOf()`, `lastIndexOf()`, `includes()`, `findLast()`, `findLastIndex()`
- `join(separator)` — array to string
- Spread operator: `[...arr]` copy, `[...arr1, ...arr2]` merge
- Array destructuring: `const [first, second, ...rest] = array`
- `Array.isArray()` — reliable type check
- The mutation trap: `const arr2 = arr1` is NOT a copy — both point to the same array

**CodePens (5 visual):**
1. Interactive to-do list (push adds, pop removes, list updates visually)
2. Sort demo (name/price cards reorder on button click)
3. Mutation trap visualizer (two variables → same array, side-by-side)
4. `at()` and `findLast()` explorer
5. Spread & destructuring lab

**Skills:**
- Creating and modifying arrays with mutating and non-mutating methods
- Sorting arrays of strings and numbers correctly
- Using the spread operator to copy and merge arrays
- Destructuring arrays to extract values
- Recognizing and avoiding the mutation trap

---

### Day 25: Objects & JSON
**Visual Frame:** One object = one rendered card. Array of objects = full rendered grid.
**Topics & Concepts:**
- What objects are: key-value pairs for grouping related data
- Object literal `{}`
- Dot notation vs bracket notation — when to use each (dynamic keys, keys with special chars)
- Adding, modifying, deleting properties
- Checking existence: `"key" in object`, `Object.hasOwn(obj, key)` (modern)
- Property shorthand: `{ x, y }`
- Computed property names: `{ [key]: value }`
- Methods and method shorthand
- `this` in methods; arrow functions and `this`
- `Object.keys()`, `Object.values()`, `Object.entries()`, `Object.fromEntries()`
- `Object.assign()` — merging objects
- Spread with objects: `{ ...obj }` shallow copy, `{ ...obj, key: newVal }` override
- `structuredClone()` — modern deep copy (moved here from Day 18)
- Object destructuring with rename and defaults
- Nested objects and optional chaining `?.`
- Arrays of objects — the most common real-world data structure

**JSON (dedicated section):**
- What JSON is: language-agnostic data format
- JSON vs JavaScript object: keys must be quoted, no functions, no `undefined`
- `JSON.stringify(obj, null, 2)` — with pretty-print
- `JSON.parse(jsonString)`
- Null guard: `JSON.parse(localStorage.getItem(key) || "[]")`
- Real-world context: APIs respond with JSON strings

- `Object.freeze()` — brief

**CodePens (5 visual):**
1. Object-to-card renderer (edit form → card updates live)
2. Array of objects → rendered card grid
3. `Object.entries()` settings panel
4. Destructuring lab (with rename/defaults)
5. `structuredClone()` deep copy demo

**Skills:**
- Creating, reading, and modifying objects with dot and bracket notation
- Writing methods and understanding `this` in context
- Using `Object.keys/values/entries` to iterate over objects
- Destructuring objects to extract values cleanly
- Working with arrays of objects as data structures
- Serializing and parsing JSON

---

### Day 26: Strings & Numbers In Depth + Timers
**Visual Frame:** Format object data for display (prices, names, dates). Live clock and countdown.
**Topics & Concepts:**

**Strings:**
- Strings are immutable — methods return new strings, never modify the original
- `length`, `at(-1)`, `toUpperCase()`, `toLowerCase()`
- `includes()`, `startsWith()`, `endsWith()`
- `indexOf()`, `lastIndexOf()`
- `slice()` — excerpts, truncation
- `substring()` — historical context only
- `replace()`, `replaceAll()` — also accepts regex
- `trim()`, `trimStart()`, `trimEnd()` — form input cleaning
- `padStart()`, `padEnd()` — zero-padding
- `repeat()` — star ratings, progress bars
- `split(delimiter)`
- Chaining: `trim().toLowerCase().replace()` — URL slug example
- Brief regex: `/pattern/.test(str)`, `str.match(/pattern/)`
- `matchAll()`

**Numbers:**
- `Number.isInteger()`, `Number.isFinite()`, `Number.isNaN()`
- `Number.parseInt()`, `Number.parseFloat()`
- `.toFixed(digits)` — format decimal places (returns a string)
- `.toString(radix)` — convert to other bases
- Floating point: `0.1 + 0.2 !== 0.3` — why and how to handle
- `Intl.NumberFormat` — locale-aware currency, percentages, compact notation
- `Intl.DateTimeFormat` — brief

**Timers:**
- `setTimeout(callback, delay)` — run once after a delay in milliseconds
- `setInterval(callback, interval)` — run repeatedly at an interval
- `clearTimeout(id)` and `clearInterval(id)` — stopping timers
- Practical uses: live clock, countdown timer, toast notification
- Debounce pattern — real-world `setTimeout` use

**CodePens (5 visual):**
1. String method playground
2. Price/number formatter (`Intl.NumberFormat` as USD, EUR, GBP, percent, compact)
3. Live clock + countdown timer
4. Debounce demo (unthrottled vs debounced side by side)
5. URL slug generator

**Skills:**
- Using string methods to search, extract, and transform text
- Formatting numbers for display with `toFixed()` and `Intl.NumberFormat`
- Building timers with `setTimeout` and `setInterval`
- Chaining string methods for clean transformations

---

### Day 27: Array Iteration Methods
**Visual Frame:** THE big payoff day. `map()` renders a card grid. `filter()` hides/shows cards live. `reduce()` shows running cart total. Everything from Days 18-26 converges here.
**Topics & Concepts:**
- Higher-order functions that take a callback: `(element, index, array) => {}`
- Why they exist: cleaner than writing loops manually
- Decision guide table: which method does what
- `forEach(cb)` — side effects, returns `undefined`
- `map(cb)` — transforms, returns new array of same length
- `filter(cb)` — keeps elements where callback returns `true`
- `find(cb)` — first matching element
- `findIndex(cb)` — index of first match
- `findLast(cb)`, `findLastIndex(cb)` — ES2023
- `some(cb)` — `true` if ANY element passes (form validation)
- `every(cb)` — `true` if ALL elements pass
- `reduce(cb, initialValue)` — accumulate into single result
  - Callback receives: `(accumulator, currentValue, index, array)`
  - Common uses: summing, counting, building objects from arrays
- `flat(depth)` — flatten nested arrays
- `flatMap(cb)` — map then flatten one level
- Chaining: `filter().map().sort()`
- `forEach` vs `map`: when to use which
- Rendering HTML: `map()` + `join("")` + `innerHTML`
- `Object.groupBy()` — ES2024, group items into categories (moved here from Day 21)

**CodePens (5 visual):**
1. `map()` card renderer (array of objects → grid, edit data → grid rebuilds)
2. `filter()` category toggle (click buttons, cards show/hide with transition)
3. `reduce()` shopping cart (add items, running total updates)
4. Method decision lab (6 buttons, same dataset, different method each)
5. Full pipeline: filterable + sortable product grid (`filter` + `sort` + `map` + `join` + `innerHTML`)

**Skills:**
- Using `forEach`, `map`, and `filter` to work with arrays
- Finding elements with `find` and `findIndex`
- Testing arrays with `some` and `every`
- Using `reduce` for accumulation
- Chaining methods to transform data in multiple steps
- Rendering lists and cards from arrays using `map()` and `innerHTML`

---

### Day 28: Local Storage & Practical Patterns
**Visual Frame:** Everything persists across page refreshes. Error states have visible UI. Course wrap-up with "what's next."
**Topics & Concepts:**

**Local Storage:**
- What it is: browser API, key-value string storage, ~5MB, persists, domain-specific
- `localStorage.setItem(key, value)` — store a string value
- `localStorage.getItem(key)` — retrieve a string value (returns `null` if key doesn't exist)
- `localStorage.removeItem(key)` — delete a specific item
- `localStorage.clear()` — clear all stored items for the domain
- Storing objects: `JSON.stringify()` before `setItem()`
- Retrieving objects: `JSON.parse()` after `getItem()`
- Null guard pattern: `JSON.parse(localStorage.getItem(key) || "[]")`
- `sessionStorage` vs `localStorage` — `sessionStorage` cleared when tab closes
- Web Storage `storage` event — detect changes from another tab
- `navigator.onLine` — show offline UI
- `localStorage` vs `sessionStorage` vs cookies vs IndexedDB — comparison
- When NOT to use: passwords, tokens, sensitive data

**Error Handling:**
- `try` / `catch` / `finally`
- The `catch(error)` parameter: `error.message`, `error.name`, `error.stack`
- `throw new Error()`, `TypeError`, `RangeError`
- Wrapping `localStorage` in `try`/`catch` (can fail in private browsing)
- Defensive coding with `?.` and `??`

**Code Organization:**
- Naming conventions: `camelCase` for variables/functions, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants
- Single responsibility principle: one function does one thing
- Separating concerns: data / rendering / events
- ES Modules preview: `import` / `export`

**Bringing It Together:**
- Data → Logic → Display → Persistence → Interaction
- Common JS pitfalls review
- What's next: Promises & async/await, Fetch API, frameworks (React, Vue, Svelte), Node.js

**CodePens (5 visual):**
1. Theme switcher persisting to `localStorage`
2. Persistent to-do list (full CRUD, survives refresh)
3. Shopping cart with storage
4. Offline-aware app (`navigator.onLine` banner)
5. Error handling showcase with visible error UI

**Skills:**
- Saving and loading data with Local Storage
- Serializing and deserializing objects with JSON
- Using try/catch for defensive error handling
- Organizing JavaScript code by responsibility
- Connecting events, DOM, arrays, objects, and local storage into a complete interactive feature

---

## IFRAME RECOMMENDATION (Retroactive Addition to Existing Lesson)
**Insert into Lesson 7 (Colors, Graphics, Multimedia):**
- The `<iframe>` element: purpose and use cases (embedding external content)
- Core attributes: `src`, `width`, `height`, `title` (required for accessibility)
- The `loading="lazy"` attribute for performance
- The `sandbox` attribute and security (prevents scripts, forms, etc. from embedded content)
- Common `sandbox` values: `allow-scripts`, `allow-same-origin`, `allow-forms`
- Embedding YouTube videos (using embed URL format)
- Embedding Google Maps
- Responsive iframes: using `aspect-ratio` + `width: 100%` instead of fixed dimensions
- `<iframe>` limitations: some sites block embedding with `X-Frame-Options`
