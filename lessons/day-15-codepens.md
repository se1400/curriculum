# Day 15 — CSS Animations & Pseudo-elements: CodePen Code Blocks

---

## CODEPEN 1 — Animation Properties Interactive Demo

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Animation Properties Demo</title>
</head>
<body>

  <h2>Animation Properties</h2>
  <p>Click a button to see each animation property in action.</p>

  <div class="controls">
    <button onclick="demo('fillNone')">fill-mode: none</button>
    <button onclick="demo('fillForwards')">fill-mode: forwards</button>
    <button onclick="demo('fillBoth')">fill-mode: both</button>
    <button onclick="demo('alternate')">direction: alternate</button>
    <button onclick="demo('infinite')">iteration: infinite</button>
    <button onclick="togglePause()">Pause / Resume</button>
  </div>

  <div class="stage">
    <div class="box" id="box">Box</div>
  </div>

  <p class="label" id="desc">Click a button above.</p>

  <script>
    const box = document.getElementById('box');
    const desc = document.getElementById('desc');

    function demo(type) {
      box.className = 'box';
      void box.offsetWidth; // force reflow to restart animation

      const configs = {
        fillNone:     { cls: 'anim-fill-none',     text: 'fill-mode: none — box snaps back after animation ends' },
        fillForwards: { cls: 'anim-fill-forwards',  text: 'fill-mode: forwards — box holds the 100% keyframe styles' },
        fillBoth:     { cls: 'anim-fill-both',      text: 'fill-mode: both — applies from 0% immediately + holds at 100%' },
        alternate:    { cls: 'anim-alternate',      text: 'direction: alternate — ping-pongs back and forth' },
        infinite:     { cls: 'anim-infinite',       text: 'iteration-count: infinite — loops forever' },
      };

      const c = configs[type];
      if (c) {
        box.classList.add(c.cls);
        desc.textContent = c.text;
      }
    }

    function togglePause() {
      const state = box.style.animationPlayState;
      box.style.animationPlayState = (state === 'paused') ? 'running' : 'paused';
      desc.textContent = (box.style.animationPlayState === 'paused')
        ? 'Animation paused — click again to resume'
        : 'Animation resumed';
    }
  </script>

</body>
</html>
```

### CSS
```css
body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #f8f9fa;
}

h2 { margin-bottom: 0.5rem; }

.controls {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

button {
  padding: 0.5rem 1rem;
  background: #4f6df5;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 0.9rem;
  cursor: pointer;
}

button:hover { background: #3451d1; }

.stage {
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  height: 120px;
  display: flex;
  align-items: center;
  padding-left: 1rem;
  margin-bottom: 1rem;
}

.box {
  width: 80px;
  height: 80px;
  background: #4f6df5;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 0.9rem;
}

.label {
  color: #64748b;
  font-size: 0.9rem;
  font-style: italic;
  min-height: 1.5em;
}

/* ---- Animation classes ---- */

@keyframes slideRight {
  from { transform: translateX(0);    opacity: 1; }
  to   { transform: translateX(300px); opacity: 0.3; }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); background: #4f6df5; }
  50%       { transform: scale(1.3); background: #ec4899; }
}

.anim-fill-none {
  animation: slideRight 1.5s ease-out none;
}

.anim-fill-forwards {
  animation: slideRight 1.5s ease-out forwards;
}

.anim-fill-both {
  animation: slideRight 1.5s ease-out 0.5s both;
  /* 0.5s delay — "both" applies from 0% during that delay */
}

.anim-alternate {
  animation: slideRight 1s ease-in-out infinite alternate;
}

.anim-infinite {
  animation: pulse 1s ease-in-out infinite;
}

@media (prefers-reduced-motion: reduce) {
  .box[class*="anim-"] {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

### JS
```js
// JS is embedded in the HTML above
```

---

## CODEPEN 2 — Layering Multiple Animations

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Multiple Animations</title>
</head>
<body>

  <h2>Layering Multiple Animations</h2>
  <p>This element has two independent animations running simultaneously:</p>
  <ul>
    <li><strong>floatUp</strong> — gentle vertical floating (3s, infinite, alternate)</li>
    <li><strong>colorCycle</strong> — color shift (6s, infinite)</li>
  </ul>

  <div class="stage">
    <div class="multi-box" id="multiBox">
      <span>✦</span>
      <p>Floating &amp; Shifting</p>
    </div>
  </div>

  <div class="controls">
    <button onclick="toggleFloat()">Toggle Float Animation</button>
    <button onclick="toggleColor()">Toggle Color Animation</button>
  </div>

  <p class="status" id="status">Both animations running</p>

  <script>
    const box = document.getElementById('multiBox');
    const status = document.getElementById('status');
    let floatOn = true;
    let colorOn = true;

    function update() {
      const names = [];
      const durations = [];
      const timings = [];
      const counts = [];
      const directions = [];

      if (floatOn) {
        names.push('floatUp');
        durations.push('3s');
        timings.push('ease-in-out');
        counts.push('infinite');
        directions.push('alternate');
      }
      if (colorOn) {
        names.push('colorCycle');
        durations.push('6s');
        timings.push('linear');
        counts.push('infinite');
        directions.push('normal');
      }

      box.style.animationName            = names.join(', ');
      box.style.animationDuration        = durations.join(', ');
      box.style.animationTimingFunction  = timings.join(', ');
      box.style.animationIterationCount  = counts.join(', ');
      box.style.animationDirection       = directions.join(', ');

      if (floatOn && colorOn) status.textContent = 'Both animations running';
      else if (floatOn)       status.textContent = 'Float only';
      else if (colorOn)       status.textContent = 'Color shift only';
      else                    status.textContent = 'Both animations paused';
    }

    function toggleFloat() { floatOn = !floatOn; update(); }
    function toggleColor() { colorOn = !colorOn; update(); }
  </script>

</body>
</html>
```

### CSS
```css
body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #f8f9fa;
  text-align: center;
}

.stage {
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 2rem 0;
}

.multi-box {
  padding: 1.5rem 2.5rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  font-weight: 700;
  font-size: 1.1rem;
  color: #4f6df5;

  /* Both animations assigned in CSS — JS just toggles them */
  animation:
    floatUp   3s ease-in-out infinite alternate,
    colorCycle 6s linear     infinite;
}

.multi-box span {
  display: block;
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.multi-box p { margin: 0; }

@keyframes floatUp {
  from { transform: translateY(0); }
  to   { transform: translateY(-20px); }
}

@keyframes colorCycle {
  0%   { color: #4f6df5; }
  25%  { color: #ec4899; }
  50%  { color: #10b981; }
  75%  { color: #f59e0b; }
  100% { color: #4f6df5; }
}

.controls {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

button {
  padding: 0.5rem 1.25rem;
  background: #4f6df5;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

button:hover { background: #3451d1; }

.status {
  margin-top: 1rem;
  color: #64748b;
  font-style: italic;
}

@media (prefers-reduced-motion: reduce) {
  .multi-box { animation: none !important; }
}
```

### JS
```js
// JS is embedded in the HTML above
```

---

## CODEPEN 3 — prefers-reduced-motion Demo

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>prefers-reduced-motion Demo</title>
</head>
<body>

  <h2>prefers-reduced-motion</h2>
  <p>
    If your OS has "Reduce Motion" enabled, the spinning circle below will show a
    static pulse instead. Use the button to simulate the preference in this demo.
  </p>

  <div class="demo-grid">
    <div class="card">
      <div class="spinner" aria-label="Loading" role="status"></div>
      <p>CSS Spinner</p>
    </div>
    <div class="card">
      <div class="bouncer">⬆</div>
      <p>Bouncing Icon</p>
    </div>
    <div class="card">
      <div class="slider-box">Sliding In</div>
      <p>Slide Entrance</p>
    </div>
  </div>

  <button id="toggleBtn" onclick="toggleReduced()">
    Simulate prefers-reduced-motion
  </button>

  <p class="note" id="note">
    Real setting: <strong id="realPref">detecting...</strong>
  </p>

  <script>
    let simulating = false;

    // Detect real OS preference
    const realPref = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    document.getElementById('realPref').textContent = realPref ? 'reduce' : 'no-preference';

    function toggleReduced() {
      simulating = !simulating;
      document.body.classList.toggle('force-reduced', simulating);
      document.getElementById('toggleBtn').textContent = simulating
        ? 'Remove Simulation'
        : 'Simulate prefers-reduced-motion';
    }

    // Restart slider animation when toggling
    const slider = document.querySelector('.slider-box');
    document.getElementById('toggleBtn').addEventListener('click', () => {
      slider.classList.remove('active');
      void slider.offsetWidth;
      slider.classList.add('active');
    });

    document.querySelector('.slider-box').classList.add('active');
  </script>

</body>
</html>
```

### CSS
```css
body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #f8f9fa;
}

.demo-grid {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  margin: 2rem 0;
}

.card {
  background: white;
  border-radius: 10px;
  padding: 2rem;
  text-align: center;
  min-width: 140px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.card p { margin: 1rem 0 0; font-size: 0.85rem; color: #64748b; }

/* --- Spinner --- */
.spinner {
  width: 48px;
  height: 48px;
  border: 4px solid #e2e8f0;
  border-top-color: #4f6df5;
  border-radius: 50%;
  margin: 0 auto;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* --- Bouncer --- */
.bouncer {
  font-size: 2rem;
  animation: bounce 0.6s ease-in-out infinite alternate;
}

@keyframes bounce {
  from { transform: translateY(0); }
  to   { transform: translateY(-20px); }
}

/* --- Slider --- */
.slider-box {
  background: #4f6df5;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-weight: 600;
  opacity: 0;
  transform: translateX(-40px);
}

.slider-box.active {
  animation: slideIn 0.6s ease-out 0.2s both;
}

@keyframes slideIn {
  from { opacity: 0; transform: translateX(-40px); }
  to   { opacity: 1; transform: translateX(0); }
}

/* --- Reduced motion overrides --- */
/* Real OS preference */
@media (prefers-reduced-motion: reduce) {
  .spinner {
    animation: none;
    border-color: #4f6df5;
    opacity: 0.7;
  }
  .bouncer { animation: none; }
  .slider-box.active {
    animation: fadeInQuick 0.2s ease both;
  }
}

/* Simulated via JS class */
body.force-reduced .spinner {
  animation: none;
  border-color: #4f6df5;
  opacity: 0.7;
}
body.force-reduced .bouncer { animation: none; }
body.force-reduced .slider-box.active {
  animation: fadeInQuick 0.2s ease both;
}

@keyframes fadeInQuick {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* --- Button --- */
button {
  padding: 0.6rem 1.25rem;
  background: #1e293b;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
}
button:hover { background: #334155; }

.note { margin-top: 1rem; color: #64748b; font-size: 0.85rem; }
```

### JS
```js
// JS is embedded in the HTML above
```

---

## CODEPEN 4 — ::before and ::after Pseudo-elements

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>::before and ::after Demo</title>
</head>
<body>

  <h2>::before and ::after</h2>

  <!-- Example 1: Animated underline link -->
  <section class="demo-block">
    <h3>Animated Underline Links</h3>
    <p>Hover the links below to see the animated underline grow from right to left on hover and shrink from left to right on mouse-out.</p>
    <nav>
      <a class="animated-link" href="#">Home</a>
      <a class="animated-link" href="#">About</a>
      <a class="animated-link" href="#">Portfolio</a>
      <a class="animated-link" href="#">Contact</a>
    </nav>
  </section>

  <!-- Example 2: Tooltip using content: attr() -->
  <section class="demo-block">
    <h3>Tooltip with <code>content: attr()</code></h3>
    <p>Hover the buttons to see a tooltip generated purely with <code>::before</code> and the element's <code>data-tooltip</code> attribute.</p>
    <div class="tooltip-row">
      <button data-tooltip="Save your current progress">Save</button>
      <button data-tooltip="Discard all unsaved changes">Cancel</button>
      <button data-tooltip="Opens your account settings">Settings</button>
    </div>
  </section>

  <!-- Example 3: Decorative blockquote -->
  <section class="demo-block">
    <h3>Decorative Quotation Marks</h3>
    <blockquote class="styled-quote">
      Design is not just what it looks like and feels like. Design is how it works.
    </blockquote>
    <p class="attribution">&mdash; Steve Jobs</p>
  </section>

  <!-- Example 4: Badge counter -->
  <section class="demo-block">
    <h3>Notification Badge</h3>
    <p>The badge number is stored in a <code>data-count</code> attribute and displayed with <code>content: attr(data-count)</code>.</p>
    <div class="badge-wrap">
      <button class="badge-btn" data-count="3">🛒 Cart</button>
      <button class="badge-btn" data-count="12">🔔 Alerts</button>
      <button class="badge-btn" data-count="0">✉️ Messages</button>
    </div>
  </section>

</body>
</html>
```

### CSS
```css
body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #f8f9fa;
  line-height: 1.6;
}

.demo-block {
  background: white;
  border-radius: 10px;
  padding: 1.5rem 2rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}

.demo-block h3 { margin: 0 0 0.5rem; }
.demo-block p  { color: #555; margin-bottom: 1rem; }

/* ---- Animated underline ---- */
nav { display: flex; gap: 1.5rem; }

.animated-link {
  position: relative;
  text-decoration: none;
  color: #1e293b;
  font-weight: 600;
  padding-bottom: 2px;
}

.animated-link::after {
  content: "";
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 2px;
  background: #4f6df5;
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 0.3s ease;
}

.animated-link:hover::after,
.animated-link:focus::after {
  transform: scaleX(1);
  transform-origin: left;
}

/* ---- Tooltips ---- */
.tooltip-row { display: flex; gap: 1rem; }

[data-tooltip] {
  position: relative;
  padding: 0.6rem 1.2rem;
  background: #4f6df5;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
}

[data-tooltip]::before {
  content: attr(data-tooltip);
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  background: #1e293b;
  color: white;
  font-size: 0.78rem;
  padding: 0.35rem 0.65rem;
  border-radius: 5px;
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s ease, transform 0.2s ease;
  transform: translateX(-50%) translateY(4px);
}

/* The little arrow pointing down */
[data-tooltip]::after {
  content: "";
  position: absolute;
  bottom: calc(100% + 2px);
  left: 50%;
  transform: translateX(-50%);
  border: 5px solid transparent;
  border-top-color: #1e293b;
  opacity: 0;
  transition: opacity 0.2s ease;
}

[data-tooltip]:hover::before,
[data-tooltip]:focus::before {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}
[data-tooltip]:hover::after,
[data-tooltip]:focus::after {
  opacity: 1;
}

/* ---- Styled blockquote ---- */
.styled-quote {
  position: relative;
  margin: 0;
  padding: 1rem 1.5rem 1rem 3.5rem;
  font-size: 1.15rem;
  font-style: italic;
  color: #334155;
  border-left: none;
  background: #f1f5f9;
  border-radius: 6px;
}

.styled-quote::before {
  content: "\201C";
  position: absolute;
  left: 0.75rem;
  top: -0.5rem;
  font-size: 5rem;
  line-height: 1;
  color: #4f6df5;
  font-style: normal;
}

.attribution { color: #64748b; font-size: 0.9rem; margin-top: 0.5rem; }

/* ---- Badge counter ---- */
.badge-wrap { display: flex; gap: 1rem; }

.badge-btn {
  position: relative;
  padding: 0.6rem 1.2rem;
  background: #f1f5f9;
  border: 1.5px solid #e2e8f0;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
}

.badge-btn[data-count]:not([data-count="0"])::after {
  content: attr(data-count);
  position: absolute;
  top: -8px;
  right: -8px;
  background: #ef4444;
  color: white;
  font-size: 0.7rem;
  font-weight: 700;
  min-width: 18px;
  height: 18px;
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 4px;
}

@media (prefers-reduced-motion: reduce) {
  .animated-link::after { transition: none; }
  [data-tooltip]::before { transition: none; transform: translateX(-50%); }
}
```

### JS
```js
// No JavaScript required for this demo
```

---

## CODEPEN 5 — Pseudo-elements Showcase (::placeholder, ::selection, ::marker, ::first-letter)

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pseudo-elements Showcase</title>
</head>
<body>

  <h2>CSS Pseudo-elements</h2>

  <!-- ::placeholder -->
  <section class="demo-block">
    <h3><code>::placeholder</code></h3>
    <p>Placeholder text styled with a custom color and italic font.</p>
    <input type="text" placeholder="Search articles...">
    <input type="email" placeholder="you@example.com">
  </section>

  <!-- ::selection -->
  <section class="demo-block">
    <h3><code>::selection</code></h3>
    <p>Click and drag to select the text below — your highlight color will match the brand blue.</p>
    <p class="selectable">The quick brown fox jumps over the lazy dog. CSS pseudo-elements make styling powerful without touching HTML. Select any portion of this text to see the custom selection color in action.</p>
  </section>

  <!-- ::marker -->
  <section class="demo-block">
    <h3><code>::marker</code></h3>
    <p>List markers styled with brand colors and custom numbering.</p>
    <ul class="styled-ul">
      <li>Unordered item one</li>
      <li>Unordered item two</li>
      <li>Unordered item three</li>
    </ul>
    <ol class="styled-ol">
      <li>Ordered item one</li>
      <li>Ordered item two</li>
      <li>Ordered item three</li>
    </ol>
  </section>

  <!-- ::first-letter drop cap -->
  <section class="demo-block">
    <h3><code>::first-letter</code> — Drop Cap</h3>
    <article class="article-body">
      <p>CSS pseudo-elements give you precise control over the details that make typography feel professional and intentional. A drop cap, for example, draws the reader's eye to the beginning of an article, a technique used in print design for centuries. With a single CSS rule, you can recreate it on the web without adding any extra markup to your HTML.</p>
      <p>The second paragraph does not get the drop cap effect, because we targeted only the first paragraph with <code>p:first-of-type::first-letter</code>.</p>
    </article>
  </section>

</body>
</html>
```

### CSS
```css
body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #f8f9fa;
  line-height: 1.7;
}

.demo-block {
  background: white;
  border-radius: 10px;
  padding: 1.5rem 2rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}

.demo-block h3 { margin: 0 0 0.5rem; }
.demo-block p, .demo-block code { color: #334155; }

/* ::placeholder */
input {
  display: block;
  width: 100%;
  max-width: 360px;
  padding: 0.6rem 0.75rem;
  border: 1.5px solid #cbd5e1;
  border-radius: 6px;
  font-size: 1rem;
  margin-bottom: 0.75rem;
  outline: none;
  transition: border-color 0.2s;
}

input:focus { border-color: #4f6df5; }

input::placeholder {
  color: #94a3b8;
  font-style: italic;
}

/* ::selection */
.selectable::selection {
  background-color: #4f6df5;
  color: white;
}

/* ::marker */
.styled-ul {
  padding-left: 1.5rem;
  margin-bottom: 1rem;
}

.styled-ul li::marker {
  color: #4f6df5;
  font-size: 1.3em;
}

.styled-ol {
  padding-left: 1.5rem;
}

.styled-ol li::marker {
  color: #ec4899;
  font-weight: 700;
}

/* ::first-letter drop cap */
.article-body p:first-of-type::first-letter {
  float: left;
  font-size: 3.8rem;
  font-weight: 700;
  line-height: 0.82;
  margin-right: 0.08em;
  margin-top: 0.05em;
  color: #4f6df5;
}
```

### JS
```js
// No JavaScript required for this demo
```

---

## CODEPEN 6 — Practical Animation Patterns

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Practical Animation Patterns</title>
</head>
<body>

  <h2>Practical CSS Animation Patterns</h2>

  <!-- Spinner -->
  <section class="demo-block">
    <h3>CSS Spinner</h3>
    <p>A pure-CSS loading spinner using only <code>border</code> and a <code>rotate</code> animation.</p>
    <div class="spinners">
      <div class="spinner sm" aria-label="Loading" role="status"></div>
      <div class="spinner md" aria-label="Loading" role="status"></div>
      <div class="spinner lg" aria-label="Loading" role="status"></div>
    </div>
    <button onclick="toggleSpinner()">Pause / Resume Spinners</button>
  </section>

  <!-- Staggered list entrance -->
  <section class="demo-block">
    <h3>Staggered List Entrance</h3>
    <p>Each item has a progressively longer <code>animation-delay</code>, creating a cascading effect.</p>
    <button onclick="restartList()">Replay Entrance</button>
    <ul class="stagger-list" id="staggerList">
      <li class="stagger-item">🎨 Design Systems</li>
      <li class="stagger-item">🔧 Component Architecture</li>
      <li class="stagger-item">⚡ Performance</li>
      <li class="stagger-item">♿ Accessibility</li>
      <li class="stagger-item">📱 Responsive Design</li>
    </ul>
  </section>

  <!-- Pulsing notification badge -->
  <section class="demo-block">
    <h3>Pulsing Notification</h3>
    <p>A combination of <code>scale</code> animation and <code>::after</code> for the ripple ring.</p>
    <div class="notif-wrap">
      <button class="notif-btn">
        🔔 Notifications
        <span class="badge pulse-badge" aria-label="3 new notifications">3</span>
      </button>
    </div>
  </section>

  <script>
    let spinnersPaused = false;
    function toggleSpinner() {
      spinnersPaused = !spinnersPaused;
      document.querySelectorAll('.spinner').forEach(s => {
        s.style.animationPlayState = spinnersPaused ? 'paused' : 'running';
      });
    }

    function restartList() {
      const list = document.getElementById('staggerList');
      list.classList.remove('visible');
      void list.offsetWidth;
      list.classList.add('visible');
    }

    // Auto-start list on load
    window.addEventListener('load', () => restartList());
  </script>

</body>
</html>
```

### CSS
```css
body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #f8f9fa;
  line-height: 1.6;
}

.demo-block {
  background: white;
  border-radius: 10px;
  padding: 1.5rem 2rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}

.demo-block h3 { margin: 0 0 0.5rem; }
.demo-block p { color: #555; margin-bottom: 1rem; }

button {
  padding: 0.5rem 1.1rem;
  background: #4f6df5;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  margin-bottom: 1rem;
}
button:hover { background: #3451d1; }

/* ---- Spinners ---- */
.spinners { display: flex; align-items: center; gap: 1.5rem; margin-bottom: 1rem; }

.spinner {
  border-style: solid;
  border-color: #e2e8f0;
  border-top-color: #4f6df5;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

.spinner.sm { width: 24px; height: 24px; border-width: 3px; }
.spinner.md { width: 40px; height: 40px; border-width: 4px; }
.spinner.lg { width: 56px; height: 56px; border-width: 5px; }

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* ---- Staggered list ---- */
.stagger-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.stagger-item {
  padding: 0.6rem 0.75rem;
  margin-bottom: 0.5rem;
  background: #f1f5f9;
  border-radius: 6px;
  font-weight: 500;
  opacity: 0;
  transform: translateX(-20px);
}

.stagger-list.visible .stagger-item {
  animation: itemSlideIn 0.4s ease-out both;
}

.stagger-list.visible .stagger-item:nth-child(1) { animation-delay: 0s; }
.stagger-list.visible .stagger-item:nth-child(2) { animation-delay: 0.07s; }
.stagger-list.visible .stagger-item:nth-child(3) { animation-delay: 0.14s; }
.stagger-list.visible .stagger-item:nth-child(4) { animation-delay: 0.21s; }
.stagger-list.visible .stagger-item:nth-child(5) { animation-delay: 0.28s; }

@keyframes itemSlideIn {
  to { opacity: 1; transform: translateX(0); }
}

/* ---- Pulsing badge ---- */
.notif-wrap { display: flex; align-items: center; }

.notif-btn {
  position: relative;
  padding: 0.7rem 1.5rem;
  margin-bottom: 0;
  font-size: 1rem;
}

.pulse-badge {
  position: absolute;
  top: -6px;
  right: -6px;
  background: #ef4444;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pulse-badge::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: #ef4444;
  animation: ripple 1.5s ease-out infinite;
}

@keyframes ripple {
  from { transform: scale(1); opacity: 0.7; }
  to   { transform: scale(2.5); opacity: 0; }
}

/* ---- Reduced motion ---- */
@media (prefers-reduced-motion: reduce) {
  .spinner { animation: none; }
  .stagger-item { animation: none !important; opacity: 1; transform: none; }
  .pulse-badge::before { animation: none; }
}
```

### JS
```js
// JS is embedded in the HTML above
```
