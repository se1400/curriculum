# Day 17 — Modern CSS & Accessibility: CodePen Code Blocks

Each numbered section corresponds to the `[CODEPEN #]` placeholder in the article.

---

## CODEPEN 1 — :has() Selector Demo

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>:has() Selector Demo</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <header>
    <h1>:has() — The Parent Selector</h1>
    <p class="subtitle">Style a parent based on what it contains — no JavaScript required.</p>
  </header>

  <main>

    <!-- Demo 1: Cards with and without images -->
    <section class="demo-section">
      <h2>Demo 1: Card Styling Based on Contents</h2>
      <p class="demo-note">Cards containing an image get a different top treatment. Cards without an image get a blue top border. This uses <code>.card:has(img)</code> and <code>.card:not(:has(img))</code>.</p>
      <div class="card-row">
        <article class="card">
          <img src="https://picsum.photos/seed/css1/400/200" alt="A random nature photo" width="400" height="200">
          <div class="card-body">
            <h3>Card With Image</h3>
            <p>This card contains an &lt;img&gt; element, so <code>.card:has(img)</code> matches it — removing the padding-top so the image sits flush at the top.</p>
          </div>
        </article>
        <article class="card">
          <div class="card-body">
            <h3>Card Without Image</h3>
            <p>No image here, so <code>.card:not(:has(img))</code> matches this card, applying a blue top border and keeping standard padding.</p>
          </div>
        </article>
        <article class="card">
          <img src="https://picsum.photos/seed/css2/400/200" alt="Another random photo" width="400" height="200">
          <div class="card-body">
            <h3>Another Image Card</h3>
            <p>Same as the first card — the image removes padding-top so the photo bleeds to the top edge of the card.</p>
          </div>
        </article>
      </div>
    </section>

    <!-- Demo 2: Form parent reacts to invalid children -->
    <section class="demo-section">
      <h2>Demo 2: Form Reacts to Validation</h2>
      <p class="demo-note">The form border turns red when it contains an invalid input. The submit button becomes disabled when the form has any invalid fields. This uses <code>form:has(:invalid)</code>.</p>
      <form id="contactForm" novalidate>
        <div class="field">
          <label for="name">Name <span aria-hidden="true">*</span></label>
          <input type="text" id="name" required placeholder="Your full name">
        </div>
        <div class="field">
          <label for="email">Email <span aria-hidden="true">*</span></label>
          <input type="email" id="email" required placeholder="you@example.com">
        </div>
        <div class="field">
          <label for="message">Message</label>
          <textarea id="message" rows="3" placeholder="Optional message"></textarea>
        </div>
        <button type="submit">Send Message</button>
        <p class="form-hint">Fill in Name and Email to see the form state change.</p>
      </form>
    </section>

    <!-- Demo 3: Label styling on focused input -->
    <section class="demo-section">
      <h2>Demo 3: Label Highlights When Input Is Focused</h2>
      <p class="demo-note">Click inside each field. The label turns blue and the field wrapper gets a subtle highlight. This uses <code>.field:has(input:focus) label</code> and <code>.field:has(textarea:focus) label</code>.</p>
      <div class="field-group">
        <div class="field has-label-demo">
          <label for="f-name">Full Name</label>
          <input type="text" id="f-name" placeholder="Click to focus">
        </div>
        <div class="field has-label-demo">
          <label for="f-email">Email Address</label>
          <input type="email" id="f-email" placeholder="Click to focus">
        </div>
        <div class="field has-label-demo">
          <label for="f-notes">Notes</label>
          <textarea id="f-notes" rows="2" placeholder="Click to focus"></textarea>
        </div>
      </div>
    </section>

    <!-- Demo 4: List items with nested lists -->
    <section class="demo-section">
      <h2>Demo 4: List Items With Nested Lists Get a Marker</h2>
      <p class="demo-note">List items that contain a nested <code>&lt;ul&gt;</code> automatically get a "▸" arrow marker. Plain list items keep the default bullet. This uses <code>li:has(ul)</code>.</p>
      <ul class="nested-demo-list">
        <li>HTML Fundamentals</li>
        <li>
          CSS Techniques
          <ul>
            <li>Box Model</li>
            <li>Flexbox</li>
            <li>Grid</li>
          </ul>
        </li>
        <li>JavaScript Basics</li>
        <li>
          Accessibility
          <ul>
            <li>ARIA</li>
            <li>Keyboard Navigation</li>
            <li>Color Contrast</li>
          </ul>
        </li>
        <li>Responsive Design</li>
      </ul>
    </section>

  </main>

  <script src="script.js"></script>
</body>
</html>
```

### CSS
```css
/* ─── Reset ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; }

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #f8fafc;
  color: #1e293b;
  line-height: 1.6;
  padding: 2rem 1rem;
}

/* ─── Layout ─── */
header {
  max-width: 900px;
  margin: 0 auto 2.5rem;
}

h1 {
  font-size: 1.75rem;
  margin-bottom: 0.25rem;
}

.subtitle {
  color: #64748b;
  font-size: 1rem;
}

main {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 3rem;
}

/* ─── Demo Section ─── */
.demo-section {
  background: white;
  border-radius: 12px;
  padding: 1.75rem;
  box-shadow: 0 1px 4px rgba(0,0,0,.06), 0 4px 16px rgba(0,0,0,.04);
}

.demo-section h2 {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  color: #0f172a;
}

.demo-note {
  font-size: 0.875rem;
  color: #64748b;
  background: #f1f5f9;
  padding: 0.6rem 0.9rem;
  border-radius: 6px;
  margin-bottom: 1.25rem;
}

.demo-note code {
  background: #e2e8f0;
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
  font-size: 0.8rem;
  color: #334155;
}

/* ─── Demo 1: Cards ─── */
.card-row {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1rem;
}

.card {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  overflow: hidden;
  background: white;
  /* Default padding-top */
  padding-top: 1.25rem;
}

/* KEY :has() RULE — card with image gets no padding-top */
.card:has(img) {
  padding-top: 0;
}

/* Card without image gets a colored top border */
.card:not(:has(img)) {
  border-top: 4px solid #4f6df5;
}

.card img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  display: block;
}

.card-body {
  padding: 1rem;
}

.card-body h3 {
  font-size: 1rem;
  margin-bottom: 0.5rem;
  color: #0f172a;
}

.card-body p {
  font-size: 0.85rem;
  color: #64748b;
}

.card-body code {
  background: #e8ecff;
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
  font-size: 0.8rem;
}

/* ─── Demo 2: Form with :has(:invalid) ─── */
form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  padding: 1.25rem;
  transition: border-color 0.2s;
}

/* KEY :has() RULE — form turns red when it has invalid fields */
form:has(:invalid) {
  border-color: #ef4444;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.field label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #374151;
}

.field span[aria-hidden="true"] {
  color: #ef4444;
}

input, textarea {
  width: 100%;
  padding: 0.6rem 0.8rem;
  border: 1.5px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.95rem;
  font-family: inherit;
  outline: none;
  transition: border-color 0.15s;
}

input:focus, textarea:focus {
  border-color: #4f6df5;
  box-shadow: 0 0 0 3px rgba(79, 109, 245, 0.15);
}

input:invalid:not(:placeholder-shown) {
  border-color: #ef4444;
}

button[type="submit"] {
  align-self: flex-start;
  background: #4f6df5;
  color: white;
  border: none;
  padding: 0.65rem 1.5rem;
  border-radius: 6px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s, opacity 0.15s;
}

button[type="submit"]:hover {
  background: #3451d1;
}

/* KEY :has() RULE — submit button dims when form has invalid fields */
form:has(:invalid) button[type="submit"] {
  opacity: 0.5;
  cursor: not-allowed;
}

.form-hint {
  font-size: 0.8rem;
  color: #9ca3af;
}

/* ─── Demo 3: Label highlights on focused field ─── */
.field-group {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.has-label-demo {
  padding: 0.75rem 1rem;
  border: 1.5px solid #e2e8f0;
  border-radius: 8px;
  transition: background 0.15s, border-color 0.15s;
}

/* KEY :has() RULE — highlight the wrapper when input is focused */
.has-label-demo:has(input:focus),
.has-label-demo:has(textarea:focus) {
  background: #eff3ff;
  border-color: #4f6df5;
}

/* KEY :has() RULE — highlight the label when sibling input is focused */
.has-label-demo:has(input:focus) label,
.has-label-demo:has(textarea:focus) label {
  color: #4f6df5;
  font-weight: 700;
}

/* ─── Demo 4: Nested list markers ─── */
.nested-demo-list {
  padding-left: 1.5rem;
  font-size: 0.95rem;
}

.nested-demo-list li {
  padding: 0.3rem 0;
}

/* KEY :has() RULE — list items containing a nested list get a ▸ marker */
.nested-demo-list li:has(ul) {
  list-style-type: "▸ ";
  font-weight: 600;
  color: #4f6df5;
}

.nested-demo-list ul {
  padding-left: 1.25rem;
  margin-top: 0.25rem;
  font-weight: 400;
  color: #374151;
}

.nested-demo-list ul li {
  list-style-type: disc;
}
```

### JS
```js
// Demo 2: Prevent default form submission (just for demo)
document.getElementById('contactForm').addEventListener('submit', e => {
  e.preventDefault();
  alert('Form submitted! (Demo only)');
});
```

---

## CODEPEN 2 — @layer Cascade Layers Demo

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>@layer Cascade Layers Demo</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <header>
    <h1>@layer — CSS Cascade Layers</h1>
    <p class="subtitle">Layers give you explicit control over which styles win — regardless of specificity.</p>
  </header>

  <main>

    <!-- Layer Order Visualization -->
    <section class="demo-section">
      <h2>Layer Order</h2>
      <p class="demo-note">This stylesheet declares three layers in priority order. Styles in later-declared layers beat styles in earlier layers, even if earlier layers have higher specificity selectors.</p>
      <div class="layer-diagram">
        <div class="layer-box layer-base">
          <span class="layer-tag">@layer base</span>
          <strong>Lowest Priority</strong>
          <p>Resets, default typography, body styles</p>
          <code>@layer base, components, utilities;</code>
        </div>
        <div class="layer-arrow">↑ wins over</div>
        <div class="layer-box layer-components">
          <span class="layer-tag">@layer components</span>
          <strong>Medium Priority</strong>
          <p>Reusable UI patterns: cards, buttons, nav</p>
        </div>
        <div class="layer-arrow">↑ wins over</div>
        <div class="layer-box layer-utilities">
          <span class="layer-tag">@layer utilities</span>
          <strong>Highest Priority</strong>
          <p>Single-purpose utility classes: .hidden, .p-0</p>
        </div>
        <div class="layer-arrow">↑ wins over</div>
        <div class="layer-box layer-unlayered">
          <span class="layer-tag">Unlayered CSS</span>
          <strong>Always Wins Over Layered Styles</strong>
          <p>Rules outside any @layer beat all layered rules</p>
        </div>
      </div>
    </section>

    <!-- Button Demo -->
    <section class="demo-section">
      <h2>Button: base → components → utilities</h2>
      <p class="demo-note">Each button shows how layers interact. The buttons below demonstrate layer priority: the <code>@layer utilities</code> color always overrides the <code>@layer components</code> color, even if the components selector is more specific.</p>

      <div class="button-grid">

        <div class="demo-card">
          <h3>Base Layer Style</h3>
          <p class="demo-sub">Only @layer base is applied.</p>
          <button class="btn base-only">Base Button</button>
          <pre class="code-snippet">@layer base {
  .btn { padding: 0.6rem 1.2rem; }
}</pre>
        </div>

        <div class="demo-card">
          <h3>Component Layer Override</h3>
          <p class="demo-sub">@layer components overrides base.</p>
          <button class="btn component-styled">Component Button</button>
          <pre class="code-snippet">@layer components {
  .btn { background: #4f6df5; color: white; }
}</pre>
        </div>

        <div class="demo-card">
          <h3>Utility Wins Over Component</h3>
          <p class="demo-sub">Even a less-specific utility class wins.</p>
          <button class="btn component-styled utility-override">Utility Override</button>
          <pre class="code-snippet">@layer utilities {
  /* .utility-override has lower specificity
     than .component-styled, yet it wins
     because utilities layer > components layer */
  .utility-override { background: #10b981; }
}</pre>
        </div>

        <div class="demo-card">
          <h3>Unlayered Always Wins</h3>
          <p class="demo-sub">Styles outside @layer beat all layers.</p>
          <button class="btn component-styled unlayered-btn">Unlayered</button>
          <pre class="code-snippet">/* Outside any @layer */
.unlayered-btn {
  background: #ef4444; /* beats everything */
}</pre>
        </div>

      </div>
    </section>

    <!-- Specificity paradox demo -->
    <section class="demo-section">
      <h2>The Specificity Paradox — Solved by Layers</h2>
      <p class="demo-note">Without layers, a high-specificity selector in a vendor library prevents you from overriding it without writing an even more specific selector. With layers, you wrap the library in a <code>layer(vendor)</code> layer, and all your component styles automatically win — no specificity arms race needed.</p>
      <div class="paradox-demo">
        <div class="paradox-card bad-example">
          <h3>Without @layer (Problem)</h3>
          <ul>
            <li>Library uses: <code>div.card.featured h2.title</code></li>
            <li>Your override: <code>.title</code> — loses, not specific enough</li>
            <li>You must escalate to <code>div.card.featured h2.title</code> or add <code>!important</code></li>
            <li>Results in specificity arms race 🔥</li>
          </ul>
        </div>
        <div class="paradox-card good-example">
          <h3>With @layer (Solution)</h3>
          <ul>
            <li>Library is wrapped: <code>@import url("lib.css") layer(vendor);</code></li>
            <li>Your layers: <code>@layer vendor, base, components, utilities;</code></li>
            <li>Your <code>.title</code> style is in <code>components</code> layer — after vendor</li>
            <li>Your style wins automatically, regardless of specificity ✓</li>
          </ul>
        </div>
      </div>
    </section>

  </main>

</body>
</html>
```

### CSS
```css
/* ─── Layer Order Declaration ─── */
/* The ORDER here determines priority: later = higher priority */
@layer base, components, utilities;

/* ─── @layer base ─── */
@layer base {
  *, *::before, *::after { box-sizing: border-box; margin: 0; }

  body {
    font-family: system-ui, -apple-system, sans-serif;
    background: #f8fafc;
    color: #1e293b;
    line-height: 1.6;
    padding: 2rem 1rem;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    padding: 0.6rem 1.2rem;
    border: none;
    border-radius: 6px;
    font-size: 0.95rem;
    font-family: inherit;
    cursor: pointer;
    /* Base gives it a plain gray look */
    background: #e2e8f0;
    color: #374151;
  }
}

/* ─── @layer components ─── */
@layer components {
  /* Components adds the brand color treatment */
  .btn.component-styled {
    background: #4f6df5;
    color: white;
    font-weight: 600;
    box-shadow: 0 2px 8px rgba(79, 109, 245, 0.3);
    transition: background 0.15s;
  }

  .btn.component-styled:hover {
    background: #3451d1;
  }
}

/* ─── @layer utilities ─── */
@layer utilities {
  /* Even though .utility-override has lower specificity than
     .btn.component-styled, this wins because utilities layer > components layer */
  .utility-override {
    background: #10b981 !important;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
  }
}

/* ─── Unlayered CSS (outside all layers) — always beats layered styles ─── */
.unlayered-btn {
  background: #ef4444;
  box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3);
}


/* ─── Page Layout (unlayered, structural) ─── */
header {
  max-width: 900px;
  margin: 0 auto 2.5rem;
}

h1 {
  font-size: 1.75rem;
  margin-bottom: 0.25rem;
}

.subtitle {
  color: #64748b;
}

main {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 3rem;
}

.demo-section {
  background: white;
  border-radius: 12px;
  padding: 1.75rem;
  box-shadow: 0 1px 4px rgba(0,0,0,.06), 0 4px 16px rgba(0,0,0,.04);
}

.demo-section h2 {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  color: #0f172a;
}

.demo-note {
  font-size: 0.875rem;
  color: #64748b;
  background: #f1f5f9;
  padding: 0.6rem 0.9rem;
  border-radius: 6px;
  margin-bottom: 1.25rem;
}

.demo-note code, .demo-sub code {
  background: #e2e8f0;
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
  font-size: 0.8rem;
  color: #334155;
}

/* ─── Layer Diagram ─── */
.layer-diagram {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.layer-box {
  border: 2px solid;
  border-radius: 8px;
  padding: 0.75rem 1rem;
  position: relative;
}

.layer-tag {
  display: inline-block;
  font-family: monospace;
  font-size: 0.8rem;
  background: rgba(0,0,0,0.1);
  padding: 0.1rem 0.5rem;
  border-radius: 4px;
  margin-bottom: 0.3rem;
}

.layer-box strong { display: block; margin-bottom: 0.2rem; }
.layer-box p { font-size: 0.85rem; color: #64748b; }
.layer-box code { font-size: 0.8rem; background: rgba(0,0,0,0.08); padding: 0.15rem 0.4rem; border-radius: 3px; }

.layer-base     { border-color: #94a3b8; background: #f8fafc; }
.layer-components { border-color: #4f6df5; background: #eff3ff; }
.layer-utilities  { border-color: #10b981; background: #ecfdf5; }
.layer-unlayered  { border-color: #f59e0b; background: #fffbeb; }

.layer-arrow {
  text-align: center;
  font-size: 0.85rem;
  color: #94a3b8;
  font-style: italic;
}

/* ─── Button Grid ─── */
.button-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.demo-card {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.demo-card h3 { font-size: 0.9rem; color: #0f172a; }

.demo-sub {
  font-size: 0.8rem;
  color: #64748b;
}

.code-snippet {
  font-size: 0.72rem;
  background: #1e293b;
  color: #94a3b8;
  padding: 0.6rem;
  border-radius: 6px;
  overflow-x: auto;
  white-space: pre-wrap;
  line-height: 1.5;
}

/* ─── Specificity Paradox Demo ─── */
.paradox-demo {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.paradox-card {
  padding: 1rem;
  border-radius: 8px;
}

.paradox-card h3 {
  font-size: 0.95rem;
  margin-bottom: 0.75rem;
}

.paradox-card ul {
  padding-left: 1.2rem;
  font-size: 0.85rem;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.paradox-card code {
  background: rgba(0,0,0,0.1);
  padding: 0.1rem 0.3rem;
  border-radius: 3px;
  font-size: 0.78rem;
}

.bad-example  { background: #fef2f2; border: 1.5px solid #fecaca; color: #991b1b; }
.good-example { background: #f0fdf4; border: 1.5px solid #bbf7d0; color: #166534; }

@media (max-width: 600px) {
  .paradox-demo { grid-template-columns: 1fr; }
}
```

### JS
```js
// No JavaScript required for this demo.
// @layer is a pure CSS feature.
```

---

## CODEPEN 3 — Dark Mode: prefers-color-scheme, light-dark(), and color-mix()

### HTML
```html
<!DOCTYPE html>
<html lang="en" data-theme="auto">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dark Mode Demo</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- Skip link -->
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="header-inner">
      <span class="site-logo">🎨 ThemeKit</span>
      <div class="theme-controls">
        <span class="theme-label">Theme:</span>
        <div class="theme-toggle-group" role="group" aria-label="Theme preference">
          <button class="theme-btn active" data-theme-value="auto" aria-pressed="true">
            🖥 Auto
          </button>
          <button class="theme-btn" data-theme-value="light" aria-pressed="false">
            ☀️ Light
          </button>
          <button class="theme-btn" data-theme-value="dark" aria-pressed="false">
            🌙 Dark
          </button>
        </div>
      </div>
    </div>
  </header>

  <main id="main">

    <section class="hero">
      <h1>Dark Mode Theming</h1>
      <p>Three modern CSS techniques working together: <strong>CSS custom properties</strong> + <strong>prefers-color-scheme</strong>, the <strong>light-dark()</strong> function, and <strong>color-mix()</strong> for automatic tints.</p>
    </section>

    <!-- Cards -->
    <section class="section">
      <h2>Component Cards</h2>
      <p class="section-desc">These cards adapt automatically. The colors are defined as tokens; the cards only reference tokens — they never hardcode a color value.</p>
      <div class="card-grid">
        <article class="card">
          <div class="card-badge">New</div>
          <h3>CSS Custom Properties</h3>
          <p>Define color tokens once. Override them for dark mode. Every component that references the token automatically updates.</p>
          <a href="#" class="card-link">Learn more →</a>
        </article>
        <article class="card">
          <div class="card-badge card-badge--accent">Feature</div>
          <h3>light-dark() Function</h3>
          <p>Specify light and dark values in a single property declaration without a media query block. Cleaner than two <code>:root</code> rule sets.</p>
          <a href="#" class="card-link">Learn more →</a>
        </article>
        <article class="card">
          <div class="card-badge card-badge--success">Modern</div>
          <h3>color-mix()</h3>
          <p>Generate tints, shades, and transparency values from a single brand color. No more maintaining 10 hex values per color.</p>
          <a href="#" class="card-link">Learn more →</a>
        </article>
      </div>
    </section>

    <!-- color-mix() palette demo -->
    <section class="section">
      <h2>color-mix() in Action</h2>
      <p class="section-desc">All swatches below are generated from a single brand color using <code>color-mix()</code>. No hardcoded hex values — just one variable and math.</p>
      <div class="palette">
        <div class="swatch swatch-100"><span>10% brand</span></div>
        <div class="swatch swatch-200"><span>25% brand</span></div>
        <div class="swatch swatch-300"><span>50% brand</span></div>
        <div class="swatch swatch-400"><span>75% brand</span></div>
        <div class="swatch swatch-500"><span>Brand</span></div>
        <div class="swatch swatch-600"><span>+20% dark</span></div>
        <div class="swatch swatch-700"><span>+40% dark</span></div>
      </div>
    </section>

    <!-- Technique comparison -->
    <section class="section">
      <h2>Technique Comparison</h2>
      <div class="comparison-grid">
        <div class="comparison-card">
          <h3>Custom Properties + Media Query</h3>
          <pre>:root { --bg: #fff; }
@media (prefers-color-scheme: dark) {
  :root { --bg: #0f172a; }
}
body { background: var(--bg); }</pre>
          <ul class="pro-con-list">
            <li class="pro">✓ Works in all browsers</li>
            <li class="pro">✓ Easy manual toggle with data-theme</li>
            <li class="pro">✓ Explicit and readable</li>
          </ul>
        </div>
        <div class="comparison-card">
          <h3>light-dark() Function</h3>
          <pre>:root { color-scheme: light dark; }
body {
  background: light-dark(#fff, #0f172a);
  color: light-dark(#0f172a, #f1f5f9);
}</pre>
          <ul class="pro-con-list">
            <li class="pro">✓ More concise syntax</li>
            <li class="pro">✓ No separate media query block</li>
            <li class="con">✗ No easy manual toggle override</li>
            <li class="con">✗ Requires 2024+ browser</li>
          </ul>
        </div>
      </div>
    </section>

  </main>

  <script src="script.js"></script>
</body>
</html>
```

### CSS
```css
/* ─── Color Tokens ─── */
/* Approach 1: Custom Properties + prefers-color-scheme (recommended) */
:root {
  --brand:           #4f6df5;

  /* Light mode defaults */
  --color-bg:        #f8fafc;
  --color-surface:   #ffffff;
  --color-surface-2: #f1f5f9;
  --color-border:    #e2e8f0;
  --color-text:      #0f172a;
  --color-text-muted:#64748b;
  --color-accent:    #4f6df5;

  /* Also enable light-dark() function (Approach 2) */
  color-scheme: light dark;
}

/* Dark mode via OS preference */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --color-bg:        #0f172a;
    --color-surface:   #1e293b;
    --color-surface-2: #334155;
    --color-border:    #334155;
    --color-text:      #f1f5f9;
    --color-text-muted:#94a3b8;
    --color-accent:    #7c9bff;
  }
}

/* Dark mode via manual toggle */
[data-theme="dark"] {
  --color-bg:        #0f172a;
  --color-surface:   #1e293b;
  --color-surface-2: #334155;
  --color-border:    #334155;
  --color-text:      #f1f5f9;
  --color-text-muted:#94a3b8;
  --color-accent:    #7c9bff;
}

/* ─── Reset ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; }

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--color-bg);
  color: var(--color-text);
  line-height: 1.6;
  transition: background 0.3s, color 0.3s;
}

/* ─── Skip Link ─── */
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  background: var(--brand);
  color: white;
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  text-decoration: none;
  z-index: 9999;
  transition: top 0.1s;
}
.skip-link:focus { top: 0; }

/* ─── Header ─── */
.site-header {
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
  position: sticky;
  top: 0;
  z-index: 100;
  transition: background 0.3s;
}

.header-inner {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0.75rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.site-logo {
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--color-text);
}

.theme-controls {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.theme-label {
  font-size: 0.875rem;
  color: var(--color-text-muted);
}

.theme-toggle-group {
  display: flex;
  gap: 0.25rem;
  background: var(--color-surface-2);
  padding: 0.25rem;
  border-radius: 8px;
}

.theme-btn {
  background: transparent;
  border: none;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.8rem;
  cursor: pointer;
  color: var(--color-text-muted);
  transition: background 0.15s, color 0.15s;
}

.theme-btn:hover {
  background: var(--color-surface);
  color: var(--color-text);
}

.theme-btn.active {
  background: var(--color-surface);
  color: var(--color-accent);
  font-weight: 600;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

/* ─── Layout ─── */
main {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 3rem;
}

/* ─── Hero ─── */
.hero {
  text-align: center;
  padding: 2rem 0 1rem;
}

.hero h1 {
  font-size: clamp(1.5rem, 4vw, 2.5rem);
  margin-bottom: 0.75rem;
}

.hero p {
  color: var(--color-text-muted);
  max-width: 600px;
  margin: 0 auto;
  font-size: 1.05rem;
}

.hero strong {
  color: var(--color-accent);
}

/* ─── Section ─── */
.section h2 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.section-desc {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  margin-bottom: 1.25rem;
}

.section-desc code {
  background: var(--color-surface-2);
  padding: 0.1rem 0.4rem;
  border-radius: 3px;
  font-size: 0.85rem;
  color: var(--color-accent);
}

/* ─── Card Grid ─── */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1rem;
}

.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 12px;
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  transition: background 0.3s, border-color 0.3s;
}

.card-badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.2rem 0.6rem;
  border-radius: 100px;
  background: color-mix(in srgb, var(--brand), transparent 85%);
  color: var(--color-accent);
  align-self: flex-start;
}

.card-badge--accent {
  background: color-mix(in srgb, #8b5cf6, transparent 85%);
  color: #8b5cf6;
}

.card-badge--success {
  background: color-mix(in srgb, #10b981, transparent 85%);
  color: #10b981;
}

.card h3 {
  font-size: 1rem;
  color: var(--color-text);
}

.card p {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  flex: 1;
}

.card p code {
  background: var(--color-surface-2);
  padding: 0.1rem 0.3rem;
  border-radius: 3px;
  font-size: 0.8rem;
}

.card-link {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--color-accent);
  text-decoration: none;
  align-self: flex-start;
}

.card-link:hover { text-decoration: underline; }

/* ─── color-mix() Palette ─── */
.palette {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.swatch {
  flex: 1 1 80px;
  height: 80px;
  border-radius: 8px;
  display: flex;
  align-items: flex-end;
  padding: 0.4rem 0.5rem;
  min-width: 70px;
}

.swatch span {
  font-size: 0.7rem;
  font-weight: 600;
  color: white;
  text-shadow: 0 1px 2px rgba(0,0,0,0.5);
  line-height: 1.2;
}

/* Generated from a single --brand variable */
.swatch-100 { background: color-mix(in srgb, var(--brand), white 90%); }
.swatch-200 { background: color-mix(in srgb, var(--brand), white 75%); }
.swatch-300 { background: color-mix(in srgb, var(--brand), white 50%); }
.swatch-400 { background: color-mix(in srgb, var(--brand), white 25%); }
.swatch-500 { background: var(--brand); }
.swatch-600 { background: color-mix(in srgb, var(--brand), black 20%); }
.swatch-700 { background: color-mix(in srgb, var(--brand), black 40%); }

/* ─── Comparison Grid ─── */
.comparison-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.comparison-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 10px;
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.comparison-card h3 {
  font-size: 0.95rem;
  color: var(--color-text);
}

.comparison-card pre {
  background: #1e293b;
  color: #94a3b8;
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 0.75rem;
  overflow-x: auto;
  white-space: pre-wrap;
  line-height: 1.5;
}

.pro-con-list {
  list-style: none;
  padding: 0;
  font-size: 0.85rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.pro { color: #10b981; }
.con { color: #ef4444; }

@media (max-width: 600px) {
  .comparison-grid { grid-template-columns: 1fr; }
}
```

### JS
```js
// Theme toggle: Auto / Light / Dark
const html       = document.documentElement;
const themeBtns  = document.querySelectorAll('.theme-btn');
const STORAGE_KEY = 'day17-theme';

// Restore saved preference
const savedTheme = localStorage.getItem(STORAGE_KEY) || 'auto';
applyTheme(savedTheme);

themeBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const value = btn.dataset.themeValue;
    applyTheme(value);
    localStorage.setItem(STORAGE_KEY, value);
  });
});

function applyTheme(value) {
  // Set the data-theme attribute which CSS reads
  html.dataset.theme = value;

  // Update button pressed states
  themeBtns.forEach(btn => {
    const isActive = btn.dataset.themeValue === value;
    btn.classList.toggle('active', isActive);
    btn.setAttribute('aria-pressed', String(isActive));
  });
}
```

---

## CODEPEN 4 — Native &lt;dialog&gt; Element: Accessible Modal

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Native &lt;dialog&gt; Demo</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <header>
    <h1>Native &lt;dialog&gt; Element</h1>
    <p class="subtitle">Accessible modals with zero JavaScript boilerplate for focus trapping, Escape key, and backdrop.</p>
  </header>

  <main id="main-content">

    <section class="demo-section">
      <h2>Three Dialog Types</h2>
      <p class="demo-note">Click each button to open a different dialog. All three use the native <code>&lt;dialog&gt;</code> element. Notice: Escape always closes them, focus is trapped inside, and focus returns to the trigger button when closed.</p>

      <div class="button-row">
        <button class="btn btn-primary" id="openConfirmBtn">
          Open Confirm Dialog
        </button>
        <button class="btn btn-warning" id="openDeleteBtn">
          Open Delete Dialog
        </button>
        <button class="btn btn-neutral" id="openInfoBtn">
          Open Info Dialog (non-modal)
        </button>
      </div>
    </section>

    <section class="demo-section">
      <h2>How It Works</h2>
      <div class="code-compare">
        <div class="compare-col">
          <h3>showModal() — True Modal</h3>
          <pre>dialog.showModal()
// ✓ Focus is trapped inside
// ✓ Escape key closes it
// ✓ Adds ::backdrop
// ✓ Returns focus to trigger on close
// ✓ Scrolling locked on background</pre>
        </div>
        <div class="compare-col">
          <h3>show() — Non-Modal</h3>
          <pre>dialog.show()
// ✗ Focus is NOT trapped
// ✓ Still has ARIA dialog role
// ✗ No ::backdrop pseudo-element
// ✓ Background remains interactive
// Use for: tooltips, sidebars</pre>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>Event Log</h2>
      <p class="demo-note">Dialog events are logged here. Notice the <code>returnValue</code> property — it tells you which button closed the dialog.</p>
      <div class="event-log" id="eventLog" aria-live="polite" aria-label="Event log">
        <p class="log-empty">Open a dialog to see events logged here.</p>
      </div>
    </section>

  </main>

  <!-- ── Dialog 1: Confirm ── -->
  <dialog class="modal" id="confirmDialog" aria-labelledby="confirmTitle" aria-describedby="confirmDesc">
    <div class="modal-header">
      <h2 id="confirmTitle">Confirm Action</h2>
      <button class="modal-close" aria-label="Close dialog" data-close="cancel">✕</button>
    </div>
    <div class="modal-body">
      <p id="confirmDesc">Are you sure you want to publish this article? It will be visible to all users immediately.</p>
    </div>
    <div class="modal-footer">
      <button class="btn btn-neutral" value="cancel" data-close="cancel">Cancel</button>
      <button class="btn btn-primary" value="confirmed" data-close="confirmed">Yes, Publish</button>
    </div>
  </dialog>

  <!-- ── Dialog 2: Destructive Confirm ── -->
  <dialog class="modal modal--danger" id="deleteDialog" aria-labelledby="deleteTitle" aria-describedby="deleteDesc">
    <div class="modal-header">
      <h2 id="deleteTitle">Delete Permanently?</h2>
      <button class="modal-close" aria-label="Close dialog" data-close="cancel">✕</button>
    </div>
    <div class="modal-body">
      <div class="modal-icon">⚠️</div>
      <p id="deleteDesc">This will permanently delete <strong>"My Project"</strong> and all associated files. This action <strong>cannot be undone</strong>.</p>
    </div>
    <div class="modal-footer">
      <button class="btn btn-neutral" value="cancel" data-close="cancel">Cancel</button>
      <button class="btn btn-danger" value="deleted" data-close="deleted">Delete Forever</button>
    </div>
  </dialog>

  <!-- ── Dialog 3: Info (non-modal) ── -->
  <dialog class="modal modal--info" id="infoDialog" aria-labelledby="infoTitle">
    <div class="modal-header">
      <h2 id="infoTitle">Keyboard Shortcuts</h2>
      <button class="modal-close" aria-label="Close dialog" data-close="closed">✕</button>
    </div>
    <div class="modal-body">
      <p>This is a <strong>non-modal</strong> dialog opened with <code>dialog.show()</code> — the background remains interactive. Useful for side panels, popovers, and non-blocking info.</p>
      <table class="shortcut-table">
        <thead><tr><th>Key</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td><kbd>Ctrl+S</kbd></td><td>Save document</td></tr>
          <tr><td><kbd>Ctrl+Z</kbd></td><td>Undo</td></tr>
          <tr><td><kbd>Ctrl+Shift+P</kbd></td><td>Command palette</td></tr>
          <tr><td><kbd>Esc</kbd></td><td>Close this panel</td></tr>
        </tbody>
      </table>
    </div>
    <div class="modal-footer">
      <button class="btn btn-neutral" value="closed" data-close="closed">Close</button>
    </div>
  </dialog>

  <script src="script.js"></script>
</body>
</html>
```

### CSS
```css
/* ─── Reset ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; }

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #f8fafc;
  color: #1e293b;
  line-height: 1.6;
  padding: 2rem 1rem;
}

/* ─── Layout ─── */
header {
  max-width: 860px;
  margin: 0 auto 2.5rem;
}

h1 { font-size: 1.75rem; margin-bottom: 0.25rem; }
.subtitle { color: #64748b; }

main {
  max-width: 860px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.demo-section {
  background: white;
  border-radius: 12px;
  padding: 1.75rem;
  box-shadow: 0 1px 4px rgba(0,0,0,.06), 0 4px 16px rgba(0,0,0,.04);
}

.demo-section h2 { font-size: 1.1rem; margin-bottom: 0.5rem; }

.demo-note {
  font-size: 0.875rem;
  color: #64748b;
  background: #f1f5f9;
  padding: 0.6rem 0.9rem;
  border-radius: 6px;
  margin-bottom: 1.25rem;
}

.demo-note code {
  background: #e2e8f0;
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
  font-size: 0.8rem;
}

/* ─── Buttons ─── */
.button-row {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.btn {
  padding: 0.65rem 1.25rem;
  border: none;
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: background 0.15s, transform 0.1s, box-shadow 0.15s;
}

.btn:hover { transform: translateY(-1px); }
.btn:active { transform: translateY(0); }

.btn-primary {
  background: #4f6df5;
  color: white;
  box-shadow: 0 2px 8px rgba(79,109,245,.3);
}
.btn-primary:hover { background: #3451d1; }

.btn-warning {
  background: #f59e0b;
  color: white;
  box-shadow: 0 2px 8px rgba(245,158,11,.3);
}
.btn-warning:hover { background: #d97706; }

.btn-danger {
  background: #ef4444;
  color: white;
  box-shadow: 0 2px 8px rgba(239,68,68,.3);
}
.btn-danger:hover { background: #dc2626; }

.btn-neutral {
  background: #e2e8f0;
  color: #374151;
}
.btn-neutral:hover { background: #cbd5e1; }

/* ─── Dialog / Modal ─── */
dialog.modal {
  border: none;
  border-radius: 16px;
  padding: 0;
  width: min(480px, calc(100vw - 2rem));
  box-shadow: 0 20px 60px rgba(0,0,0,.25), 0 4px 16px rgba(0,0,0,.15);
  /* Animate in */
  animation: modal-in 0.2s ease;
}

@keyframes modal-in {
  from { opacity: 0; transform: translateY(-16px) scale(0.97); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}

/* ::backdrop — the overlay behind the modal */
dialog.modal::backdrop {
  background: rgba(15, 23, 42, 0.65);
  backdrop-filter: blur(3px);
}

.modal--danger {
  border-top: 4px solid #ef4444;
}

.modal--info {
  /* Non-modal: positioned at bottom-right */
  position: fixed;
  bottom: 1.5rem;
  right: 1.5rem;
  margin: 0;
  width: min(400px, calc(100vw - 2rem));
  box-shadow: 0 8px 32px rgba(0,0,0,.2);
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem 1.5rem 1rem;
  border-bottom: 1px solid #e2e8f0;
}

.modal-header h2 { font-size: 1.1rem; color: #0f172a; }

.modal-close {
  background: none;
  border: none;
  font-size: 1rem;
  color: #94a3b8;
  cursor: pointer;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  transition: color 0.15s, background 0.15s;
  line-height: 1;
}

.modal-close:hover { color: #1e293b; background: #f1f5f9; }

.modal-body {
  padding: 1.25rem 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.modal-icon { font-size: 2rem; text-align: center; }

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  padding: 1rem 1.5rem 1.25rem;
  border-top: 1px solid #e2e8f0;
}

/* ─── Code Compare ─── */
.code-compare {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.compare-col h3 {
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
  color: #374151;
}

.compare-col pre {
  background: #1e293b;
  color: #94a3b8;
  padding: 1rem;
  border-radius: 8px;
  font-size: 0.78rem;
  line-height: 1.7;
  white-space: pre-wrap;
}

/* ─── Event Log ─── */
.event-log {
  background: #0f172a;
  border-radius: 8px;
  padding: 1rem;
  min-height: 120px;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  font-family: monospace;
  font-size: 0.8rem;
}

.log-empty { color: #475569; font-style: italic; }

.log-entry {
  color: #94a3b8;
  display: flex;
  gap: 0.75rem;
}

.log-time { color: #475569; flex-shrink: 0; }
.log-event { color: #7c9bff; }
.log-value { color: #6ee7b7; }

/* ─── Shortcut Table ─── */
.shortcut-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.875rem;
}

.shortcut-table th,
.shortcut-table td {
  text-align: left;
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid #e2e8f0;
}

.shortcut-table th { background: #f8fafc; font-weight: 600; }

kbd {
  background: #e2e8f0;
  border: 1px solid #cbd5e1;
  border-radius: 4px;
  padding: 0.1rem 0.4rem;
  font-size: 0.78rem;
  font-family: monospace;
}

@media (max-width: 540px) {
  .code-compare { grid-template-columns: 1fr; }
}
```

### JS
```js
// ─── Dialog openers ───
const confirmDialog = document.getElementById('confirmDialog');
const deleteDialog  = document.getElementById('deleteDialog');
const infoDialog    = document.getElementById('infoDialog');
const mainContent   = document.getElementById('main-content');

document.getElementById('openConfirmBtn').addEventListener('click', () => {
  confirmDialog.showModal(); // True modal
  mainContent.inert = true;  // Prevent background interaction (inert attribute)
  logEvent('confirmDialog', 'showModal() called', '—');
});

document.getElementById('openDeleteBtn').addEventListener('click', () => {
  deleteDialog.showModal();
  mainContent.inert = true;
  logEvent('deleteDialog', 'showModal() called', '—');
});

document.getElementById('openInfoBtn').addEventListener('click', () => {
  infoDialog.show(); // Non-modal
  // Note: we do NOT set inert for non-modal dialogs
  logEvent('infoDialog', 'show() called (non-modal)', '—');
});

// ─── Close buttons (via data-close attribute) ───
document.querySelectorAll('[data-close]').forEach(btn => {
  btn.addEventListener('click', () => {
    const returnValue = btn.dataset.close;
    const dialog = btn.closest('dialog');
    dialog.close(returnValue); // Pass returnValue to dialog.returnValue
  });
});

// ─── Listen for close events on all dialogs ───
document.querySelectorAll('dialog').forEach(dialog => {
  dialog.addEventListener('close', () => {
    // Remove inert from background (modal dialogs only)
    if (dialog.id !== 'infoDialog') {
      mainContent.inert = false;
    }
    logEvent(dialog.id, 'close event fired', `returnValue: "${dialog.returnValue}"`);
  });
});

// ─── Event Logger ───
const eventLog = document.getElementById('eventLog');

function logEvent(dialogId, eventName, value) {
  // Remove empty state message
  const empty = eventLog.querySelector('.log-empty');
  if (empty) empty.remove();

  const now = new Date();
  const time = now.toLocaleTimeString([], { hour: '2-digit', minute:'2-digit', second:'2-digit' });

  const entry = document.createElement('div');
  entry.className = 'log-entry';
  entry.innerHTML = `
    <span class="log-time">${time}</span>
    <span class="log-event">${dialogId}</span>
    <span>${eventName}</span>
    <span class="log-value">${value}</span>
  `;

  eventLog.appendChild(entry);
  eventLog.scrollTop = eventLog.scrollHeight;
}
```

---

## CODEPEN 5 — Accessibility Showcase: ARIA States, Live Regions, Skip Nav, Focus Management

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Accessibility Showcase</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- ── DEMO 1: Skip Navigation Link ── -->
  <!-- First element in body — keyboard users press Tab to reveal it -->
  <a class="skip-link" href="#main-content">Skip to main content</a>

  <!-- Simulated navigation with many links -->
  <nav aria-label="Main navigation">
    <ul class="nav-list">
      <li><a href="#" aria-current="page">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Services</a></li>
      <li><a href="#">Portfolio</a></li>
      <li><a href="#">Blog</a></li>
      <li><a href="#">Team</a></li>
      <li><a href="#">Careers</a></li>
      <li><a href="#">Press</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>

  <main id="main-content" tabindex="-1">

    <header class="page-header">
      <h1>Accessibility Patterns</h1>
      <p class="lead">Press <kbd>Tab</kbd> to navigate with the keyboard. Each section demonstrates a key accessibility pattern.</p>
    </header>

    <!-- ── DEMO 2: ARIA States on an Accordion ── -->
    <section class="demo-box" aria-labelledby="accordion-heading">
      <h2 id="accordion-heading">Demo 2: ARIA States — Accordion</h2>
      <p class="demo-desc">The buttons use <code>aria-expanded</code> and <code>aria-controls</code>. Screen readers announce "expanded" or "collapsed" for each panel.</p>

      <div class="accordion" id="faq">

        <div class="accordion-item">
          <h3>
            <button
              class="accordion-trigger"
              aria-expanded="false"
              aria-controls="faq-1-panel"
              id="faq-1-btn"
            >
              What is the accessibility tree?
              <span class="accordion-icon" aria-hidden="true">▸</span>
            </button>
          </h3>
          <div
            id="faq-1-panel"
            role="region"
            aria-labelledby="faq-1-btn"
            class="accordion-panel"
            hidden
          >
            <p>The accessibility tree is a parallel structure to the DOM that browsers expose to screen readers and other assistive technologies. It represents elements as semantic roles — "button," "heading," "list" — rather than raw HTML tags.</p>
          </div>
        </div>

        <div class="accordion-item">
          <h3>
            <button
              class="accordion-trigger"
              aria-expanded="false"
              aria-controls="faq-2-panel"
              id="faq-2-btn"
            >
              What is the first rule of ARIA?
              <span class="accordion-icon" aria-hidden="true">▸</span>
            </button>
          </h3>
          <div
            id="faq-2-panel"
            role="region"
            aria-labelledby="faq-2-btn"
            class="accordion-panel"
            hidden
          >
            <p>Don't use ARIA if a native HTML element can do the same thing. A <code>&lt;button&gt;</code> is always better than <code>&lt;div role="button"&gt;</code> because native elements come with keyboard behavior and semantics built in — ARIA only adds to the accessibility tree.</p>
          </div>
        </div>

        <div class="accordion-item">
          <h3>
            <button
              class="accordion-trigger"
              aria-expanded="false"
              aria-controls="faq-3-panel"
              id="faq-3-btn"
            >
              When should I use tabindex?
              <span class="accordion-icon" aria-hidden="true">▸</span>
            </button>
          </h3>
          <div
            id="faq-3-panel"
            role="region"
            aria-labelledby="faq-3-btn"
            class="accordion-panel"
            hidden
          >
            <p>Use <code>tabindex="0"</code> to add a non-interactive element to the tab order when you must build a custom widget. Use <code>tabindex="-1"</code> to allow programmatic focus via JavaScript (used in focus management for modals and skip links). Never use positive values like <code>tabindex="2"</code> — they override document order and confuse keyboard users.</p>
          </div>
        </div>

      </div>
    </section>

    <!-- ── DEMO 3: aria-live Regions ── -->
    <section class="demo-box" aria-labelledby="live-heading">
      <h2 id="live-heading">Demo 3: aria-live Regions</h2>
      <p class="demo-desc">Click the buttons to trigger announcements. Screen readers will announce updates to <code>aria-live="polite"</code> regions when you pause. <code>role="alert"</code> interrupts immediately.</p>

      <div class="live-demo">
        <div class="live-controls">
          <button class="btn btn-blue" id="saveBtn">💾 Save Document</button>
          <button class="btn btn-green" id="successBtn">✓ Mark Complete</button>
          <button class="btn btn-red" id="errorBtn">⚠ Trigger Error</button>
          <button class="btn btn-gray" id="clearBtn">✕ Clear</button>
        </div>

        <!-- Polite region: waits for user to stop interacting -->
        <div class="live-region-wrapper">
          <h3 class="live-region-label">
            <code>aria-live="polite"</code> — Status Messages
          </h3>
          <div
            class="live-region polite-region"
            aria-live="polite"
            aria-atomic="true"
            id="statusRegion"
          >
            <p id="statusMsg" class="live-placeholder">Status messages appear here.</p>
          </div>
        </div>

        <!-- Assertive region: interrupts immediately -->
        <div class="live-region-wrapper">
          <h3 class="live-region-label">
            <code>role="alert"</code> (assertive) — Error Messages
          </h3>
          <div
            class="live-region alert-region"
            role="alert"
            id="errorRegion"
          >
            <p id="errorMsg" class="live-placeholder">Error alerts appear here.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ── DEMO 4: ARIA-invalid + ARIA-describedby ── -->
    <section class="demo-box" aria-labelledby="form-heading">
      <h2 id="form-heading">Demo 4: Accessible Form Validation</h2>
      <p class="demo-desc">Submit the form with invalid data. Watch how <code>aria-invalid</code>, <code>aria-describedby</code>, and <code>role="alert"</code> work together to communicate errors to assistive technology.</p>

      <form id="demoForm" novalidate>
        <div class="form-field" id="field-username">
          <label for="username">Username <span class="required" aria-hidden="true">*</span></label>
          <input
            type="text"
            id="username"
            name="username"
            required
            minlength="3"
            maxlength="20"
            autocomplete="username"
            aria-required="true"
            aria-describedby="username-hint username-error"
          >
          <p id="username-hint" class="field-hint">3–20 characters. Letters and numbers only.</p>
          <p id="username-error" class="field-error" role="alert" aria-live="assertive" hidden></p>
        </div>

        <div class="form-field" id="field-email">
          <label for="email-input">Email Address <span class="required" aria-hidden="true">*</span></label>
          <input
            type="email"
            id="email-input"
            name="email"
            required
            autocomplete="email"
            aria-required="true"
            aria-describedby="email-error"
          >
          <p id="email-error" class="field-error" role="alert" aria-live="assertive" hidden></p>
        </div>

        <div class="form-actions">
          <button type="submit" class="btn btn-blue">Submit</button>
          <button type="reset" class="btn btn-gray">Reset</button>
        </div>
      </form>
    </section>

    <!-- ── DEMO 5: aria-hidden and visually hidden ── -->
    <section class="demo-box" aria-labelledby="hidden-heading">
      <h2 id="hidden-heading">Demo 5: aria-hidden vs. Visually Hidden</h2>
      <p class="demo-desc">Two techniques for managing what screen readers see — sometimes you want to hide <em>from</em> screen readers; other times you want to hide <em>visually</em> while keeping content available to screen readers.</p>

      <div class="hidden-demo">
        <div class="hidden-example">
          <h3>Decorative Icon — aria-hidden="true"</h3>
          <p>The star icon below is decorative. Screen readers skip it because of <code>aria-hidden="true"</code>. The <code>.sr-only</code> span provides the accessible name instead.</p>
          <div class="star-rating" aria-label="Product rating">
            <span aria-hidden="true">★★★★☆</span>
            <span class="sr-only">4 out of 5 stars</span>
          </div>
        </div>

        <div class="hidden-example">
          <h3>Visually Hidden — .sr-only</h3>
          <p>Buttons with icon-only visuals need accessible names. The text below is visually hidden but read by screen readers.</p>
          <div class="icon-buttons">
            <button class="icon-btn" aria-label="Search">
              🔍
              <span class="sr-only">Search</span>
            </button>
            <button class="icon-btn" aria-label="Notifications">
              🔔
              <span class="sr-only">Notifications</span>
            </button>
            <button class="icon-btn" aria-label="Settings">
              ⚙️
              <span class="sr-only">Settings</span>
            </button>
          </div>
        </div>
      </div>
    </section>

  </main>

  <script src="script.js"></script>
</body>
</html>
```

### CSS
```css
/* ─── Reset ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; }

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #f8fafc;
  color: #1e293b;
  line-height: 1.6;
}

/* ─── Focus styles (keyboard users) ─── */
:focus:not(:focus-visible) { outline: none; }

:focus-visible {
  outline: 3px solid #4f6df5;
  outline-offset: 3px;
  border-radius: 3px;
}

/* ─── Visually hidden (accessible to screen readers) ─── */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* ─── Skip Link ─── */
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  z-index: 9999;
  background: #4f6df5;
  color: white;
  padding: 0.75rem 1.5rem;
  font-weight: 700;
  font-size: 0.95rem;
  text-decoration: none;
  border-radius: 0 0 6px 0;
  transition: top 0.1s ease;
}

.skip-link:focus {
  top: 0; /* Slides into view on focus */
}

/* ─── Navigation ─── */
nav {
  background: #0f172a;
  padding: 0.75rem 1.5rem;
  position: sticky;
  top: 0;
  z-index: 10;
}

.nav-list {
  list-style: none;
  padding: 0;
  display: flex;
  gap: 0.25rem;
  flex-wrap: wrap;
}

.nav-list a {
  color: #94a3b8;
  text-decoration: none;
  padding: 0.4rem 0.75rem;
  border-radius: 4px;
  font-size: 0.875rem;
  transition: color 0.15s, background 0.15s;
}

.nav-list a:hover {
  color: white;
  background: rgba(255,255,255,0.08);
}

/* aria-current="page" — active link */
.nav-list a[aria-current="page"] {
  color: white;
  background: rgba(79,109,245,0.3);
  font-weight: 600;
}

/* ─── Main content ─── */
main {
  max-width: 900px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
}

/* tabindex="-1" target: allow programmatic focus from skip link */
main:focus { outline: none; }

.page-header h1 { font-size: clamp(1.5rem, 4vw, 2rem); margin-bottom: 0.5rem; }
.lead { color: #64748b; font-size: 1rem; }
.lead kbd { background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 4px; padding: 0.1rem 0.4rem; font-size: 0.85rem; }

/* ─── Demo sections ─── */
.demo-box {
  background: white;
  border-radius: 12px;
  padding: 1.75rem;
  box-shadow: 0 1px 4px rgba(0,0,0,.06), 0 4px 16px rgba(0,0,0,.04);
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.demo-box h2 { font-size: 1.1rem; color: #0f172a; }

.demo-desc {
  font-size: 0.875rem;
  color: #64748b;
  background: #f1f5f9;
  padding: 0.6rem 0.9rem;
  border-radius: 6px;
}

.demo-desc code {
  background: #e2e8f0;
  padding: 0.1rem 0.3rem;
  border-radius: 3px;
  font-size: 0.8rem;
  color: #334155;
}

/* ─── Accordion ─── */
.accordion { display: flex; flex-direction: column; gap: 0; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; }

.accordion-item + .accordion-item { border-top: 1px solid #e2e8f0; }

.accordion-trigger {
  width: 100%;
  background: white;
  border: none;
  padding: 1rem 1.25rem;
  text-align: left;
  font-size: 0.95rem;
  font-weight: 600;
  color: #0f172a;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  transition: background 0.15s;
  font-family: inherit;
}

.accordion-trigger:hover { background: #f8fafc; }

.accordion-trigger[aria-expanded="true"] { color: #4f6df5; background: #eff3ff; }

.accordion-icon {
  font-size: 0.8rem;
  transition: transform 0.2s;
  flex-shrink: 0;
}

.accordion-trigger[aria-expanded="true"] .accordion-icon {
  transform: rotate(90deg);
}

.accordion-panel {
  padding: 1rem 1.25rem;
  background: #f8fafc;
  font-size: 0.9rem;
  color: #475569;
  border-top: 1px solid #e2e8f0;
}

.accordion-panel code {
  background: #e2e8f0;
  padding: 0.1rem 0.3rem;
  border-radius: 3px;
  font-size: 0.8rem;
}

/* ─── Live Region Demo ─── */
.live-demo { display: flex; flex-direction: column; gap: 1rem; }

.live-controls {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.live-region-wrapper { display: flex; flex-direction: column; gap: 0.4rem; }

.live-region-label {
  font-size: 0.8rem;
  font-weight: 600;
  color: #64748b;
}

.live-region-label code {
  background: #e2e8f0;
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
}

.live-region {
  padding: 0.75rem 1rem;
  border-radius: 8px;
  min-height: 56px;
  font-size: 0.9rem;
  transition: all 0.2s;
}

.polite-region {
  background: #eff3ff;
  border: 1.5px solid #c7d2fe;
  color: #3730a3;
}

.alert-region {
  background: #fef2f2;
  border: 1.5px solid #fecaca;
  color: #991b1b;
}

.live-placeholder { color: #94a3b8; font-style: italic; font-size: 0.85rem; }

/* ─── Buttons ─── */
.btn {
  padding: 0.55rem 1rem;
  border: none;
  border-radius: 7px;
  font-size: 0.875rem;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: background 0.15s;
}

.btn-blue  { background: #4f6df5; color: white; }
.btn-blue:hover { background: #3451d1; }
.btn-green { background: #10b981; color: white; }
.btn-green:hover { background: #059669; }
.btn-red   { background: #ef4444; color: white; }
.btn-red:hover { background: #dc2626; }
.btn-gray  { background: #e2e8f0; color: #374151; }
.btn-gray:hover { background: #cbd5e1; }

/* ─── Accessible Form ─── */
form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.form-field {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #374151;
}

.required { color: #ef4444; }

input[type="text"],
input[type="email"] {
  padding: 0.65rem 0.9rem;
  border: 1.5px solid #d1d5db;
  border-radius: 7px;
  font-size: 0.95rem;
  font-family: inherit;
  outline: none;
  transition: border-color 0.15s;
}

input:focus {
  border-color: #4f6df5;
  box-shadow: 0 0 0 3px rgba(79,109,245,.15);
}

input[aria-invalid="true"] {
  border-color: #ef4444;
  box-shadow: 0 0 0 3px rgba(239,68,68,.1);
}

.field-hint {
  font-size: 0.8rem;
  color: #94a3b8;
}

.field-error {
  font-size: 0.8rem;
  color: #dc2626;
  font-weight: 600;
}

.field-error:not([hidden]) { display: block; }

.form-actions { display: flex; gap: 0.75rem; }

/* ─── aria-hidden / sr-only demo ─── */
.hidden-demo {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.hidden-example {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.hidden-example h3 { font-size: 0.9rem; color: #374151; }
.hidden-example p { font-size: 0.8rem; color: #64748b; }
.hidden-example code { background: #e2e8f0; padding: 0.1rem 0.3rem; border-radius: 3px; font-size: 0.75rem; }

.star-rating { font-size: 1.5rem; color: #f59e0b; }

.icon-buttons { display: flex; gap: 0.5rem; }

.icon-btn {
  width: 44px;
  height: 44px;
  border: 1.5px solid #e2e8f0;
  border-radius: 8px;
  background: white;
  font-size: 1.2rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s;
}

.icon-btn:hover { background: #f1f5f9; }

@media (max-width: 600px) {
  .hidden-demo { grid-template-columns: 1fr; }
}
```

### JS
```js
// ─── Demo 2: Accordion ───
document.querySelectorAll('.accordion-trigger').forEach(trigger => {
  trigger.addEventListener('click', () => {
    const panelId = trigger.getAttribute('aria-controls');
    const panel   = document.getElementById(panelId);
    const isOpen  = trigger.getAttribute('aria-expanded') === 'true';

    // Toggle this panel
    trigger.setAttribute('aria-expanded', String(!isOpen));
    panel.hidden = isOpen;
  });
});

// ─── Demo 3: aria-live Regions ───
const statusMsg = document.getElementById('statusMsg');
const errorMsg  = document.getElementById('errorMsg');

document.getElementById('saveBtn').addEventListener('click', () => {
  setStatus('✓ Document saved successfully at ' + new Date().toLocaleTimeString());
  clearError();
});

document.getElementById('successBtn').addEventListener('click', () => {
  setStatus('✓ Item marked as complete.');
  clearError();
});

document.getElementById('errorBtn').addEventListener('click', () => {
  setError('⚠ Error: Could not connect to server. Check your internet connection and try again.');
  clearStatus();
});

document.getElementById('clearBtn').addEventListener('click', () => {
  clearStatus();
  clearError();
});

function setStatus(msg) {
  statusMsg.textContent = msg;
  statusMsg.classList.remove('live-placeholder');
}

function setError(msg) {
  errorMsg.textContent = msg;
  errorMsg.classList.remove('live-placeholder');
}

function clearStatus() {
  statusMsg.textContent = 'Status messages appear here.';
  statusMsg.classList.add('live-placeholder');
}

function clearError() {
  errorMsg.textContent = 'Error alerts appear here.';
  errorMsg.classList.add('live-placeholder');
}

// ─── Demo 4: Accessible Form Validation ───
const form = document.getElementById('demoForm');

form.addEventListener('submit', e => {
  e.preventDefault();
  let firstError = null;

  // Validate username
  const username      = form.elements['username'];
  const usernameError = document.getElementById('username-error');
  const usernameValid = username.value.trim().length >= 3 &&
                        /^[a-zA-Z0-9]+$/.test(username.value.trim());

  if (!usernameValid) {
    setFieldError(username, usernameError, 'Username must be 3–20 letters and numbers only.');
    firstError = firstError || username;
  } else {
    clearFieldError(username, usernameError);
  }

  // Validate email
  const email      = form.elements['email'];
  const emailError = document.getElementById('email-error');
  const emailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim());

  if (!emailValid) {
    setFieldError(email, emailError, 'Please enter a valid email address.');
    firstError = firstError || email;
  } else {
    clearFieldError(email, emailError);
  }

  // Move focus to first error field
  if (firstError) {
    firstError.focus();
  } else {
    setStatus('✓ Form submitted successfully!');
  }
});

form.addEventListener('reset', () => {
  form.querySelectorAll('input').forEach(input => {
    clearFieldError(input, document.getElementById(input.id + '-error'));
  });
});

function setFieldError(input, errorEl, message) {
  input.setAttribute('aria-invalid', 'true');
  errorEl.textContent = message;
  errorEl.hidden = false;
}

function clearFieldError(input, errorEl) {
  if (!errorEl) return;
  input.setAttribute('aria-invalid', 'false');
  errorEl.textContent = '';
  errorEl.hidden = true;
}

// ─── Skip Link: move focus to main content ───
document.querySelector('.skip-link').addEventListener('click', e => {
  e.preventDefault();
  const target = document.getElementById('main-content');
  target.focus(); // tabindex="-1" on <main> makes this possible
});
```
