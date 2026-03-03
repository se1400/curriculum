# Day 16 — Responsive Web Design: CodePen Code Blocks

---

## CODEPEN 1 — Media Queries: Mobile-First Layout

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Media Queries Demo</title>
</head>
<body>

  <header class="site-header">
    <span class="logo">Brand</span>
    <nav class="nav">
      <a href="#">Home</a>
      <a href="#">About</a>
      <a href="#">Work</a>
      <a href="#">Contact</a>
    </nav>
  </header>

  <main class="layout">
    <section class="content">
      <h1>Responsive Layout</h1>
      <p>Resize this window to see the layout change at different breakpoints. On small screens, everything stacks vertically. On medium screens (640px+), the grid activates. On large screens (1024px+), the sidebar appears.</p>
      <div class="card-grid">
        <div class="card">Card 1</div>
        <div class="card">Card 2</div>
        <div class="card">Card 3</div>
        <div class="card">Card 4</div>
      </div>
    </section>
    <aside class="sidebar">
      <h2>Sidebar</h2>
      <p>Only visible at 1024px+</p>
      <ul>
        <li>Link One</li>
        <li>Link Two</li>
        <li>Link Three</li>
      </ul>
    </aside>
  </main>

  <div class="breakpoint-indicator" aria-hidden="true"></div>

</body>
</html>
```

### CSS
```css
/* ---- Reset & Base ---- */
*, *::before, *::after { box-sizing: border-box; }
body {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  background: #f8f9fa;
  color: #1e293b;
}

/* ---- Header — mobile first ---- */
.site-header {
  background: #1e293b;
  color: white;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.logo { font-weight: 700; font-size: 1.25rem; }

.nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.nav a {
  color: #cbd5e1;
  text-decoration: none;
  padding: 0.35rem 0;
}

.nav a:hover { color: white; }

/* ---- Main layout — mobile: single column ---- */
.layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  max-width: 1280px;
  margin: 0 auto;
  padding: 1.5rem 1rem;
}

.sidebar { display: none; } /* hidden on mobile */

/* ---- Card grid — mobile: 1 column ---- */
.card-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin-top: 1.5rem;
}

.card {
  background: white;
  border: 1.5px solid #e2e8f0;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  font-weight: 600;
  color: #4f6df5;
}

/* ---- Medium breakpoint: 640px ---- */
@media (min-width: 640px) {
  .site-header {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 2rem;
  }

  .nav { flex-direction: row; gap: 1.5rem; }

  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* ---- Large breakpoint: 1024px ---- */
@media (min-width: 1024px) {
  .layout {
    grid-template-columns: 1fr 280px;
    padding: 2rem;
  }

  .sidebar {
    display: block;
    background: white;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    padding: 1.5rem;
  }

  .sidebar h2 { margin-top: 0; }

  .sidebar ul { padding-left: 1rem; }

  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* ---- Breakpoint indicator ---- */
.breakpoint-indicator {
  position: fixed;
  bottom: 1rem;
  right: 1rem;
  background: #1e293b;
  color: white;
  font-size: 0.8rem;
  font-weight: 600;
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  z-index: 100;
}

.breakpoint-indicator::after { content: "< 640px (mobile)"; }

@media (min-width: 640px) {
  .breakpoint-indicator::after { content: "≥ 640px (medium)"; }
}

@media (min-width: 1024px) {
  .breakpoint-indicator::after { content: "≥ 1024px (large)"; }
}
```

### JS
```js
// No JavaScript required for this demo
```

---

## CODEPEN 2 — clamp() Fluid Typography & Spacing

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>clamp() Fluid Typography</title>
</head>
<body>

  <div class="demo-container">

    <section class="demo-section">
      <h2>Fluid Typography with <code>clamp()</code></h2>
      <p>Resize the browser window. The text below scales fluidly between a minimum and maximum size — no media query jumps.</p>

      <div class="type-showcase">
        <p class="t-h1">Fluid Heading 1</p>
        <p class="t-h2">Fluid Heading 2</p>
        <p class="t-body">This body paragraph scales from 1rem on small screens to 1.25rem on wide screens. The line-length and line-height also adapt to maintain comfortable readability at any size.</p>
      </div>
    </section>

    <section class="demo-section">
      <h2>Fluid Spacing</h2>
      <p>The padding and gaps in this page also use <code>clamp()</code> — they grow larger on wider screens for a more open, breathable layout.</p>

      <div class="spacing-demo">
        <div class="box">Box 1</div>
        <div class="box">Box 2</div>
        <div class="box">Box 3</div>
      </div>

      <div class="formula-card">
        <h3>The Formula</h3>
        <pre><code>clamp(minimum, preferred, maximum)

/* Example: scales h1 from 1.75rem to 3.5rem */
font-size: clamp(1.75rem, 4vw + 1rem, 3.5rem);

/* 4vw + 1rem at 320px viewport = 1.08rem + 1rem = ~2rem (clamped to min) */
/* 4vw + 1rem at 1280px viewport = 3.2rem + 1rem = 4.2rem (clamped to max) */</code></pre>
      </div>
    </section>

  </div>

</body>
</html>
```

### CSS
```css
*, *::before, *::after { box-sizing: border-box; }

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  background: #f8f9fa;
  color: #1e293b;
}

.demo-container {
  max-width: 900px;
  margin: 0 auto;
  /* Fluid padding — scales from 1rem to 3rem */
  padding: clamp(1rem, 5vw, 3rem);
}

.demo-section {
  background: white;
  border-radius: 10px;
  padding: clamp(1rem, 4vw, 2.5rem);
  margin-bottom: clamp(1rem, 3vw, 2rem);
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}

.demo-section h2 {
  font-size: clamp(1.1rem, 2.5vw, 1.5rem);
  margin-top: 0;
}

.demo-section p {
  font-size: clamp(0.95rem, 1.5vw + 0.5rem, 1.1rem);
  color: #475569;
}

/* ---- Fluid type showcase ---- */
.type-showcase {
  background: #f1f5f9;
  border-radius: 8px;
  padding: clamp(1rem, 3vw, 2rem);
}

.t-h1 {
  font-size: clamp(1.75rem, 4vw + 1rem, 3.5rem);
  font-weight: 800;
  margin: 0 0 0.5rem;
  color: #0f172a;
}

.t-h2 {
  font-size: clamp(1.25rem, 3vw + 0.5rem, 2.25rem);
  font-weight: 700;
  margin: 0 0 0.75rem;
  color: #1e293b;
}

.t-body {
  font-size: clamp(1rem, 1.5vw + 0.5rem, 1.25rem);
  line-height: clamp(1.5, 1.5 + 0.3vw, 1.8);
  max-width: 65ch;
  color: #334155;
  margin: 0;
}

/* ---- Spacing demo ---- */
.spacing-demo {
  display: flex;
  gap: clamp(0.5rem, 2vw, 1.5rem);
  flex-wrap: wrap;
  margin: clamp(1rem, 2vw, 1.5rem) 0;
}

.box {
  flex: 1 1 100px;
  background: #4f6df5;
  color: white;
  border-radius: 8px;
  padding: clamp(0.75rem, 2vw, 1.5rem);
  text-align: center;
  font-weight: 600;
}

/* ---- Formula card ---- */
.formula-card {
  background: #1e293b;
  color: #e2e8f0;
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
}

.formula-card h3 {
  color: #94a3b8;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin: 0 0 0.75rem;
}

.formula-card pre {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.7;
  white-space: pre-wrap;
}

.formula-card code { color: #7c9bff; }
```

### JS
```js
// No JavaScript required for this demo
```

---

## CODEPEN 3 — Intrinsic Grid (auto-fill + minmax, no media queries)

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Intrinsic Responsive Grid</title>
</head>
<body>

  <div class="page">
    <h1>Intrinsic Grid — No Media Queries</h1>
    <p>Resize this window. The grid automatically adds and removes columns to fit cards of at least 260px each — with zero media queries.</p>

    <div class="controls">
      <label>Min card width:
        <input type="range" id="minWidth" min="150" max="400" value="260">
        <output id="widthOutput">260px</output>
      </label>
    </div>

    <div class="card-grid" id="cardGrid">
      <article class="card">
        <div class="card-img" style="background:#4f6df5"></div>
        <div class="card-body">
          <h3>Responsive Design</h3>
          <p>Adapts to any screen size with a single layout definition.</p>
        </div>
      </article>
      <article class="card">
        <div class="card-img" style="background:#10b981"></div>
        <div class="card-body">
          <h3>Flexbox</h3>
          <p>One-dimensional layout: rows or columns.</p>
        </div>
      </article>
      <article class="card">
        <div class="card-img" style="background:#f59e0b"></div>
        <div class="card-body">
          <h3>CSS Grid</h3>
          <p>Two-dimensional layout: rows and columns together.</p>
        </div>
      </article>
      <article class="card">
        <div class="card-img" style="background:#ef4444"></div>
        <div class="card-body">
          <h3>Container Queries</h3>
          <p>Respond to a component's container width, not the viewport.</p>
        </div>
      </article>
      <article class="card">
        <div class="card-img" style="background:#8b5cf6"></div>
        <div class="card-body">
          <h3>clamp()</h3>
          <p>Fluid values between a minimum and maximum.</p>
        </div>
      </article>
      <article class="card">
        <div class="card-img" style="background:#ec4899"></div>
        <div class="card-body">
          <h3>Media Queries</h3>
          <p>Apply styles based on viewport width breakpoints.</p>
        </div>
      </article>
    </div>
  </div>

  <script>
    const slider = document.getElementById('minWidth');
    const output = document.getElementById('widthOutput');
    const grid   = document.getElementById('cardGrid');

    slider.addEventListener('input', () => {
      const val = slider.value;
      output.textContent = val + 'px';
      grid.style.gridTemplateColumns = `repeat(auto-fill, minmax(${val}px, 1fr))`;
    });
  </script>

</body>
</html>
```

### CSS
```css
*, *::before, *::after { box-sizing: border-box; }

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  background: #f8f9fa;
  color: #1e293b;
}

.page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

h1 { font-size: 1.6rem; margin-bottom: 0.5rem; }
p  { color: #475569; }

/* ---- Controls ---- */
.controls {
  background: #1e293b;
  color: white;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  margin: 1.5rem 0;
  display: flex;
  align-items: center;
  gap: 1rem;
  font-size: 0.9rem;
}

.controls label { display: flex; align-items: center; gap: 0.5rem; }
.controls input[type=range] { cursor: pointer; }
output { font-weight: 700; color: #7c9bff; min-width: 3.5rem; display: inline-block; }

/* ---- The magic: intrinsic grid ---- */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.25rem;
}

/* ---- Cards ---- */
.card {
  background: white;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}

.card-img {
  height: 120px;
  opacity: 0.85;
}

.card-body { padding: 1rem 1.25rem 1.25rem; }

.card-body h3 { margin: 0 0 0.4rem; font-size: 1rem; color: #0f172a; }
.card-body p  { margin: 0; font-size: 0.9rem; color: #64748b; }
```

### JS
```js
// JS is embedded in the HTML above
```

---

## CODEPEN 4 — Container Queries Demo

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Container Queries</title>
</head>
<body>

  <h1>Container Queries</h1>
  <p>The same card component adapts based on its <em>container's</em> width — not the viewport. Drag the dividers to resize each column.</p>

  <div class="columns" id="cols">
    <div class="col col-narrow" id="colA">
      <p class="col-label">Narrow Context (drag to resize →)</p>
      <div class="card-wrapper">
        <article class="card">
          <img class="card-img" src="https://picsum.photos/seed/a/400/250" alt="Sample image">
          <div class="card-body">
            <h2 class="card-title">Article Title</h2>
            <p class="card-text">A short description that adjusts its layout depending on the available container width.</p>
            <a class="card-link" href="#">Read more</a>
          </div>
        </article>
      </div>
    </div>

    <div class="col col-wide" id="colB">
      <p class="col-label">Wide Context</p>
      <div class="card-wrapper">
        <article class="card">
          <img class="card-img" src="https://picsum.photos/seed/b/400/250" alt="Sample image">
          <div class="card-body">
            <h2 class="card-title">Article Title</h2>
            <p class="card-text">The same card HTML and CSS. When the container is wide enough, it switches to a side-by-side layout automatically.</p>
            <a class="card-link" href="#">Read more</a>
          </div>
        </article>
      </div>
    </div>
  </div>

  <div class="code-note">
    <strong>The key CSS:</strong>
    <pre>.card-wrapper { container-type: inline-size; }

/* Card: stacked by default */
.card { display: flex; flex-direction: column; }

/* Switch to side-by-side when container ≥ 420px */
@container (min-width: 420px) {
  .card { flex-direction: row; }
  .card-img { width: 200px; flex-shrink: 0; }
}</pre>
  </div>

</body>
</html>
```

### CSS
```css
*, *::before, *::after { box-sizing: border-box; }

body {
  font-family: system-ui, sans-serif;
  padding: 1.5rem;
  background: #f8f9fa;
  color: #1e293b;
  line-height: 1.6;
}

h1 { font-size: 1.5rem; margin-bottom: 0.5rem; }
p  { color: #475569; }

/* ---- Two-column layout ---- */
.columns {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
  align-items: flex-start;
}

.col {
  background: white;
  border-radius: 10px;
  padding: 1rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  resize: horizontal;
  overflow: auto;
  min-width: 200px;
}

.col-narrow { flex: 0 0 260px; }
.col-wide   { flex: 1; }

.col-label {
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: #94a3b8;
  font-weight: 600;
  margin: 0 0 0.75rem;
}

/* ---- Container context ---- */
.card-wrapper {
  container-type: inline-size;
}

/* ---- Card: default (stacked) ---- */
.card {
  display: flex;
  flex-direction: column;
  border-radius: 8px;
  overflow: hidden;
  border: 1.5px solid #e2e8f0;
}

.card-img {
  width: 100%;
  height: 160px;
  object-fit: cover;
  display: block;
}

.card-body {
  padding: 0.75rem 1rem;
}

.card-title {
  font-size: 1rem;
  margin: 0 0 0.4rem;
  color: #0f172a;
}

.card-text {
  font-size: 0.875rem;
  color: #64748b;
  margin: 0 0 0.75rem;
}

.card-link {
  font-size: 0.85rem;
  font-weight: 600;
  color: #4f6df5;
  text-decoration: none;
}

.card-link:hover { text-decoration: underline; }

/* ---- Container query: side-by-side when wide enough ---- */
@container (min-width: 420px) {
  .card {
    flex-direction: row;
  }

  .card-img {
    width: 180px;
    height: auto;
    flex-shrink: 0;
  }
}

/* ---- Code note ---- */
.code-note {
  margin-top: 1.5rem;
  background: #1e293b;
  color: #e2e8f0;
  border-radius: 8px;
  padding: 1rem 1.25rem;
  font-size: 0.85rem;
}

.code-note strong { color: #7c9bff; }
.code-note pre { margin: 0.5rem 0 0; line-height: 1.6; color: #94a3b8; }
```

### JS
```js
// No JavaScript required — the columns have resize: horizontal
// so the user can drag them to see the container query fire
```

---

## CODEPEN 5 — Responsive Navigation with Hamburger Menu

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Navigation</title>
</head>
<body>

  <header class="site-header">
    <a href="#" class="logo">Brand</a>

    <button
      class="menu-toggle"
      aria-expanded="false"
      aria-controls="main-nav"
      aria-label="Toggle navigation menu"
    >
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </button>

    <nav id="main-nav" class="main-nav" hidden>
      <a href="#" class="nav-link">Home</a>
      <a href="#" class="nav-link">About</a>
      <a href="#" class="nav-link">Services</a>
      <a href="#" class="nav-link">Portfolio</a>
      <a href="#" class="nav-link nav-cta">Contact Us</a>
    </nav>
  </header>

  <main class="page-content">
    <h1>Responsive Navigation Demo</h1>
    <p>On small screens, the nav collapses into a hamburger button. On screens 768px and wider, the nav displays inline in the header.</p>
    <p>Try clicking the hamburger icon (☰) if you are on a small screen or have a narrow window.</p>
    <p><strong>Accessibility notes:</strong></p>
    <ul>
      <li>The toggle button has <code>aria-expanded</code> and <code>aria-controls</code></li>
      <li>The nav uses the HTML <code>hidden</code> attribute (not just CSS) when collapsed</li>
      <li>An <code>aria-label</code> names the navigation region for screen readers</li>
    </ul>
  </main>

  <script>
    const toggle = document.querySelector('.menu-toggle');
    const nav    = document.querySelector('.main-nav');

    toggle.addEventListener('click', () => {
      const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!isExpanded));
      nav.hidden = isExpanded;
      nav.classList.toggle('is-open', !isExpanded);
    });

    // Close menu when a nav link is clicked on mobile
    nav.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth < 768) {
          nav.hidden = true;
          nav.classList.remove('is-open');
          toggle.setAttribute('aria-expanded', 'false');
        }
      });
    });
  </script>

</body>
</html>
```

### CSS
```css
*, *::before, *::after { box-sizing: border-box; }

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  background: #f8f9fa;
  color: #1e293b;
  line-height: 1.6;
}

/* ---- Header ---- */
.site-header {
  background: #0f172a;
  padding: 0.75rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  position: relative;
}

.logo {
  color: white;
  font-weight: 800;
  font-size: 1.3rem;
  text-decoration: none;
  letter-spacing: -0.02em;
}

/* ---- Hamburger button ---- */
.menu-toggle {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.4rem;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.bar {
  display: block;
  width: 24px;
  height: 2px;
  background: white;
  border-radius: 2px;
  transition: transform 0.25s ease, opacity 0.25s ease;
}

/* Animate to X when open */
.menu-toggle[aria-expanded="true"] .bar:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}
.menu-toggle[aria-expanded="true"] .bar:nth-child(2) {
  opacity: 0;
}
.menu-toggle[aria-expanded="true"] .bar:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

/* ---- Nav menu — mobile ---- */
.main-nav {
  width: 100%;
  display: flex;
  flex-direction: column;
  padding: 0.5rem 0 1rem;
  gap: 0;
}

.main-nav[hidden] { display: none; }

.main-nav.is-open { display: flex; }

.nav-link {
  color: #cbd5e1;
  text-decoration: none;
  padding: 0.6rem 0;
  font-size: 0.95rem;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  transition: color 0.2s;
}

.nav-link:hover, .nav-link:focus { color: white; outline: 2px solid #4f6df5; outline-offset: 2px; }

.nav-cta {
  margin-top: 0.5rem;
  background: #4f6df5;
  color: white;
  padding: 0.55rem 1.25rem;
  border-radius: 6px;
  text-align: center;
  border-bottom: none;
  font-weight: 600;
}

.nav-cta:hover { background: #3451d1; color: white; }

/* ---- Desktop nav: 768px+ ---- */
@media (min-width: 768px) {
  .menu-toggle { display: none; }

  .main-nav,
  .main-nav[hidden],
  .main-nav.is-open {
    display: flex !important;
    flex-direction: row;
    align-items: center;
    gap: 0.25rem;
    width: auto;
    padding: 0;
  }

  .nav-link {
    padding: 0.4rem 0.75rem;
    border-bottom: none;
    border-radius: 6px;
    color: #94a3b8;
  }

  .nav-link:hover { background: rgba(255,255,255,0.07); color: white; }

  .nav-cta { margin-top: 0; }
}

/* ---- Page content ---- */
.page-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

ul li { margin-bottom: 0.4rem; }
code { background: #e2e8f0; padding: 0.1rem 0.35rem; border-radius: 3px; font-size: 0.88em; }
```

### JS
```js
// JS is embedded in the HTML above
```

---

## CODEPEN 6 — Responsive Design Playground (resize + inspect)

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Playground</title>
</head>
<body>

  <div class="page">
    <header class="hero">
      <h1>Responsive Design Playground</h1>
      <p>This demo combines fluid typography, auto-fill grid, aspect-ratio, and media queries. Resize your browser to see everything adapt.</p>
    </header>

    <section class="features">
      <div class="feature-card">
        <div class="icon-box" style="background:#4f6df5">📐</div>
        <h3>Fluid Grid</h3>
        <p>auto-fill + minmax — no media queries needed for the grid itself.</p>
      </div>
      <div class="feature-card">
        <div class="icon-box" style="background:#10b981">✦</div>
        <h3>clamp() Type</h3>
        <p>Headlines scale smoothly between min and max values.</p>
      </div>
      <div class="feature-card">
        <div class="icon-box" style="background:#f59e0b">⬛</div>
        <h3>aspect-ratio</h3>
        <p>Icon boxes maintain their square shape at any size.</p>
      </div>
      <div class="feature-card">
        <div class="icon-box" style="background:#ec4899">📱</div>
        <h3>Mobile First</h3>
        <p>All styles build up from the smallest screen.</p>
      </div>
      <div class="feature-card">
        <div class="icon-box" style="background:#8b5cf6">🔲</div>
        <h3>Container Queries</h3>
        <p>Cards adapt to their context, not just the viewport.</p>
      </div>
      <div class="feature-card">
        <div class="icon-box" style="background:#ef4444">📏</div>
        <h3>Dynamic vh</h3>
        <p>The hero uses dvh to always fill the visible screen.</p>
      </div>
    </section>

    <div class="breakpoint-badge" aria-hidden="true"></div>
  </div>

</body>
</html>
```

### CSS
```css
*, *::before, *::after { box-sizing: border-box; }

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  background: #f1f5f9;
  color: #1e293b;
}

.page {
  max-width: 1200px;
  margin: 0 auto;
  padding: clamp(1rem, 4vw, 2.5rem);
}

/* ---- Hero ---- */
.hero {
  background: linear-gradient(135deg, #0f172a, #1e3a5f);
  color: white;
  border-radius: 12px;
  padding: clamp(2rem, 6vw, 5rem) clamp(1.5rem, 5vw, 4rem);
  margin-bottom: clamp(1.5rem, 3vw, 2.5rem);
  min-height: 30dvh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hero h1 {
  font-size: clamp(1.5rem, 4vw + 1rem, 3.5rem);
  line-height: 1.2;
  margin: 0 0 0.75rem;
}

.hero p {
  font-size: clamp(1rem, 1.5vw + 0.5rem, 1.25rem);
  color: #94a3b8;
  margin: 0;
  max-width: 60ch;
}

/* ---- Feature grid ---- */
.features {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: clamp(0.75rem, 2vw, 1.5rem);
}

.feature-card {
  container-type: inline-size;
  background: white;
  border-radius: 10px;
  padding: 1.25rem;
  box-shadow: 0 2px 6px rgba(0,0,0,0.07);
  transition: transform 0.2s, box-shadow 0.2s;
}

.feature-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.1);
}

.icon-box {
  width: 52px;
  aspect-ratio: 1;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 0.75rem;
  opacity: 0.9;
}

.feature-card h3 {
  font-size: 1rem;
  margin: 0 0 0.4rem;
}

.feature-card p {
  font-size: 0.875rem;
  color: #64748b;
  margin: 0;
  line-height: 1.5;
}

/* ---- Container query: wider card gets horizontal layout ---- */
@container (min-width: 280px) {
  .feature-card {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
  }
  .icon-box { flex-shrink: 0; margin-bottom: 0; }
}

/* ---- Breakpoint badge ---- */
.breakpoint-badge {
  position: fixed;
  bottom: 0.75rem;
  right: 0.75rem;
  background: rgba(15, 23, 42, 0.9);
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.65rem;
  border-radius: 999px;
  backdrop-filter: blur(4px);
}

.breakpoint-badge::after { content: "mobile"; }

@media (min-width: 640px) {
  .breakpoint-badge::after { content: "640px ➔ medium"; }
}
@media (min-width: 1024px) {
  .breakpoint-badge::after { content: "1024px ➔ large"; }
}
```

### JS
```js
// No JavaScript required for this demo
```
