# Day 18 — CodePen Examples
## The DOM Is Your Paintbrush: JavaScript Foundations

---

## CodePen 1 — Console Explorer

**Placement:** After the "Browser Console" section.
**Demonstrates:** `console.log()`, `console.warn()`, `console.error()`, `console.table()` — output mirrored to a visible panel alongside DevTools.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Console Explorer</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      padding: 2rem;
      max-width: 640px;
      margin: 0 auto;
    }

    h1 {
      font-size: 1.3rem;
      font-weight: 700;
      color: #a29bfe;
      margin-bottom: 0.35rem;
    }

    .subtitle {
      font-size: 0.85rem;
      opacity: 0.6;
      margin-bottom: 1.5rem;
    }

    .btn-row {
      display: flex;
      gap: 0.6rem;
      flex-wrap: wrap;
      margin-bottom: 1.5rem;
    }

    button {
      padding: 0.45rem 1rem;
      border: none;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
    }

    .btn-log   { background: #6c5ce7; color: #fff; }
    .btn-warn  { background: #fdcb6e; color: #2d2d2d; }
    .btn-error { background: #d63031; color: #fff; }
    .btn-table { background: #00b894; color: #fff; }
    .btn-clear { background: #444; color: #ccc; }

    .panel-label {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #636e72;
      margin-bottom: 0.5rem;
    }

    .console-panel {
      background: #0d1117;
      border: 1px solid #2d2d2d;
      border-radius: 10px;
      padding: 0.75rem;
      font-family: 'Courier New', monospace;
      font-size: 0.82rem;
      min-height: 200px;
      max-height: 320px;
      overflow-y: auto;
    }

    .entry {
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
      padding: 0.35rem 0.5rem;
      border-radius: 4px;
      margin-bottom: 0.3rem;
      border-left: 3px solid transparent;
    }

    .tag {
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      min-width: 3.6rem;
      opacity: 0.8;
    }

    .entry.log   { color: #dfe6e9; border-left-color: #6c5ce7; background: rgba(108,92,231,0.08); }
    .entry.warn  { color: #fdcb6e; border-left-color: #fdcb6e; background: rgba(253,203,110,0.08); }
    .entry.error { color: #ff7675; border-left-color: #d63031; background: rgba(214,48,49,0.08); }
    .entry.table { color: #55efc4; border-left-color: #00b894; background: rgba(0,184,148,0.08); }

    .empty {
      color: #444;
      font-style: italic;
      padding: 0.5rem;
    }
  </style>
</head>
<body>

  <h1>Console Explorer</h1>
  <p class="subtitle">Click each button — output appears here AND in DevTools (F12 → Console tab).</p>

  <div class="btn-row">
    <button class="btn-log"   onclick="runLog()">console.log()</button>
    <button class="btn-warn"  onclick="runWarn()">console.warn()</button>
    <button class="btn-error" onclick="runError()">console.error()</button>
    <button class="btn-table" onclick="runTable()">console.table()</button>
    <button class="btn-clear" onclick="clearPanel()">Clear</button>
  </div>

  <p class="panel-label">Output Panel</p>
  <div class="console-panel" id="output">
    <p class="empty">Click a button to run a console method…</p>
  </div>

  <script>
    let logCount = 0;

    // Adds a styled row to the on-screen panel
    function addEntry(message, type) {
      const panel = document.querySelector('#output');

      // Remove the placeholder text on first entry
      const placeholder = panel.querySelector('.empty');
      if (placeholder) {
        placeholder.remove();
      }

      const entry = document.createElement('div');
      entry.classList.add('entry', type);

      const tag = document.createElement('span');
      tag.classList.add('tag');
      tag.textContent = type;

      const text = document.createElement('span');
      text.textContent = message;

      entry.appendChild(tag);
      entry.appendChild(text);
      panel.appendChild(entry);

      // Keep the latest entry visible
      panel.scrollTop = panel.scrollHeight;
    }

    function runLog() {
      logCount = logCount + 1;
      const message = 'Hello from console.log()  —  call #' + logCount;
      console.log(message);
      addEntry(message, 'log');
    }

    function runWarn() {
      const message = 'Something to watch out for — this is a warning!';
      console.warn(message);
      addEntry(message, 'warn');
    }

    function runError() {
      const message = 'Something went wrong — this is an error!';
      console.error(message);
      addEntry(message, 'error');
    }

    function runTable() {
      const students = [
        { name: 'Ada Lovelace', grade: 'A'  },
        { name: 'Grace Hopper', grade: 'A+' },
        { name: 'Alan Turing',  grade: 'A'  }
      ];
      console.table(students);
      addEntry('Open DevTools (F12 → Console) to see the formatted table.', 'table');
    }

    function clearPanel() {
      document.querySelector('#output').innerHTML =
        '<p class="empty">Click a button to run a console method…</p>';
    }
  </script>

</body>
</html>
```

---

## CodePen 2 — Variable Explorer

**Placement:** After the "Variables: const and let" section.
**Demonstrates:** `const`, `let`, template literals with `${}`, and `style.setProperty()` updating a CSS custom property — all wired together to populate a profile card.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Variable Explorer</title>
  <style>
    :root {
      --accent: #6c5ce7;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      gap: 1.5rem;
    }

    .hint {
      font-size: 0.8rem;
      opacity: 0.5;
      text-align: center;
      max-width: 420px;
    }

    .profile-card {
      background: #16213e;
      border: 2px solid var(--accent);
      border-radius: 16px;
      padding: 2rem 2.5rem;
      max-width: 420px;
      width: 100%;
      text-align: center;
      transition: border-color 0.4s;
    }

    .avatar {
      width: 72px;
      height: 72px;
      border-radius: 50%;
      background: var(--accent);
      color: #fff;
      font-size: 1.6rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 1rem;
      transition: background 0.4s;
    }

    .card-name {
      font-size: 1.5rem;
      font-weight: 700;
      margin-bottom: 0.3rem;
    }

    .card-role {
      font-size: 0.9rem;
      color: var(--accent);
      margin-bottom: 0.75rem;
      transition: color 0.4s;
    }

    .card-bio {
      font-size: 0.85rem;
      opacity: 0.7;
      line-height: 1.6;
    }

    .code-panel {
      background: #0d1117;
      border-radius: 10px;
      padding: 1rem 1.25rem;
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      max-width: 420px;
      width: 100%;
      line-height: 2;
    }

    .kw  { color: #a29bfe; }   /* const / let */
    .vn  { color: #74b9ff; }   /* variable name */
    .str { color: #55efc4; }   /* string value */
    .num { color: #fdcb6e; }   /* number value */
    .op  { color: #636e72; }   /* = sign */

    .palette {
      display: flex;
      gap: 0.75rem;
    }

    .palette button {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 50%;
      border: 3px solid transparent;
      cursor: pointer;
      transition: transform 0.2s, border-color 0.2s;
    }

    .palette button:hover {
      transform: scale(1.15);
      border-color: rgba(255,255,255,0.5);
    }
  </style>
</head>
<body>

  <p class="hint">Change the variables at the top of the JS panel — the card updates instantly.</p>

  <div class="profile-card" id="profile-card">
    <div class="avatar"    id="avatar"></div>
    <p  class="card-name"  id="card-name"></p>
    <p  class="card-role"  id="card-role"></p>
    <p  class="card-bio"   id="card-bio"></p>
  </div>

  <div class="code-panel" id="code-display"></div>

  <div class="palette">
    <button style="background:#6c5ce7;" onclick="updateAccent('#6c5ce7')" title="#6c5ce7 Violet"></button>
    <button style="background:#00b894;" onclick="updateAccent('#00b894')" title="#00b894 Emerald"></button>
    <button style="background:#e17055;" onclick="updateAccent('#e17055')" title="#e17055 Coral"></button>
    <button style="background:#0984e3;" onclick="updateAccent('#0984e3')" title="#0984e3 Blue"></button>
    <button style="background:#fd79a8;" onclick="updateAccent('#fd79a8')" title="#fd79a8 Rose"></button>
  </div>

  <script>
    // ── Change these variables — watch the card update ────────────────
    const firstName   = 'Ada';
    const lastName    = 'Lovelace';
    const jobTitle    = 'Mathematician & Pioneer Programmer';
    const birthYear   = 1815;
    let   accentColor = '#6c5ce7';

    // Template literal: ${} works just like CSS var() — inserts a value
    const fullName = `${firstName} ${lastName}`;
    const initials = firstName[0] + lastName[0];
    const bio      = `Born ${birthYear}. Wrote the first published algorithm — considered the world's first programmer.`;

    // ── Write the variables into the card ────────────────────────────
    document.querySelector('#avatar').textContent    = initials;
    document.querySelector('#card-name').textContent = fullName;
    document.querySelector('#card-role').textContent = jobTitle;
    document.querySelector('#card-bio').textContent  = bio;

    // ── style.setProperty() updates a CSS custom property from JS ─────
    document.documentElement.style.setProperty('--accent', accentColor);

    // ── Show the variables as a code reference ───────────────────────
    document.querySelector('#code-display').innerHTML =
      '<span class="kw">const</span> <span class="vn">firstName</span>   <span class="op">=</span> <span class="str">"' + firstName + '"</span><br>' +
      '<span class="kw">const</span> <span class="vn">lastName</span>    <span class="op">=</span> <span class="str">"' + lastName + '"</span><br>' +
      '<span class="kw">const</span> <span class="vn">jobTitle</span>    <span class="op">=</span> <span class="str">"' + jobTitle.slice(0, 24) + '…"</span><br>' +
      '<span class="kw">const</span> <span class="vn">birthYear</span>   <span class="op">=</span> <span class="num">' + birthYear + '</span><br>' +
      '<span class="kw">let</span>   <span class="vn">accentColor</span> <span class="op">=</span> <span class="str">"' + accentColor + '"</span>';

    // ── Palette buttons reassign the let variable and update CSS ──────
    function updateAccent(color) {
      accentColor = color;    // let can be reassigned — const cannot
      document.documentElement.style.setProperty('--accent', accentColor);
    }
  </script>

</body>
</html>
```

---

## CodePen 3 — querySelector in Action

**Placement:** After the "querySelector — Finding Elements" section.
**Demonstrates:** `querySelector()`, `querySelectorAll()`, `textContent`, `innerHTML`, and how CSS selector syntax transfers directly to JavaScript.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>querySelector in Action</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      padding: 2rem;
      max-width: 660px;
      margin: 0 auto;
    }

    .section {
      margin-bottom: 2rem;
    }

    .section-label {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.09em;
      color: #74b9ff;
      margin-bottom: 0.75rem;
    }

    h1 {
      font-size: 1.4rem;
      font-weight: 700;
      color: #a29bfe;
      margin-bottom: 0.35rem;
    }

    .hero-desc {
      font-size: 0.9rem;
      opacity: 0.7;
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 10px;
      padding: 1rem 1.25rem;
      margin-bottom: 0.6rem;
      font-size: 0.9rem;
    }

    .card strong { color: #a29bfe; }

    .btn-row {
      display: flex;
      gap: 0.6rem;
      flex-wrap: wrap;
      margin-top: 1rem;
    }

    button {
      padding: 0.45rem 1.1rem;
      border: none;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
    }

    .btn-purple { background: #6c5ce7; color: #fff; }
    .btn-teal   { background: #00b894; color: #fff; }
    .btn-coral  { background: #e17055; color: #fff; }

    #html-demo {
      margin-top: 0.75rem;
    }

    .badge {
      display: inline-block;
      background: #6c5ce7;
      color: #fff;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.15rem 0.55rem;
      border-radius: 100px;
      margin-left: 0.4rem;
      vertical-align: middle;
    }
  </style>
</head>
<body>

  <!-- querySelector changes these on page load -->
  <h1 id="page-heading">Waiting for JavaScript…</h1>
  <p class="hero-desc" id="page-desc">querySelector has not run yet.</p>

  <div class="section">
    <p class="section-label">querySelector — first match only</p>
    <div class="card" id="target-card">This card has <code>id="target-card"</code>.</div>

    <div class="btn-row">
      <button class="btn-purple" onclick="document.querySelector('#target-card').textContent = 'querySelector(\'#target-card\') found me by ID!'">Find by ID</button>
      <button class="btn-teal"   onclick="document.querySelector('.card').textContent = 'querySelector(\'.card\') — this is the FIRST .card on the page.'">Find First .card</button>
    </div>
  </div>

  <div class="section">
    <p class="section-label">innerHTML — inject real HTML tags</p>
    <div id="html-demo"></div>
    <div class="btn-row">
      <button class="btn-coral" onclick="injectHTML()">Inject HTML</button>
    </div>
  </div>

  <div class="section">
    <p class="section-label">querySelectorAll — every match (preview: loops covered in Lesson 21)</p>
    <div class="card team-member">Team Member</div>
    <div class="card team-member">Team Member</div>
    <div class="card team-member">Team Member</div>
  </div>

  <script>
    // ── Runs immediately on page load ────────────────────────────────

    // querySelector uses the SAME selector syntax as CSS
    const heading = document.querySelector('h1');       // element selector
    const desc    = document.querySelector('#page-desc'); // ID selector

    heading.textContent = 'querySelector Found This Heading';
    desc.textContent    = 'querySelector uses the same syntax as your CSS selectors. If you can write it in CSS, you can use it here.';

    // querySelectorAll returns ALL matching elements, not just the first
    const teamMembers = document.querySelectorAll('.team-member');

    // Preview of for loops (Lesson 21) — showing the pattern early
    const names = ['Ada Lovelace', 'Grace Hopper', 'Alan Turing'];
    for (let i = 0; i < teamMembers.length; i++) {
      teamMembers[i].textContent = names[i];
    }

    // ── Button function — injects HTML via innerHTML ──────────────────
    function injectHTML() {
      const demo = document.querySelector('#html-demo');
      // innerHTML parses tags — they become real HTML elements
      demo.innerHTML = '<div class="card"><strong>Built with innerHTML</strong> — tags are parsed as real HTML. <span class="badge">new</span></div>';
    }
  </script>

</body>
</html>
```

---

## CodePen 4 — CSS Variable Controller

**Placement:** After the "Setting CSS Custom Properties from JavaScript" section.
**Demonstrates:** `style.setProperty()` updating a CSS custom property (`--hue`) that cascades to all elements through `hsl(var(--hue), …)`. Combined with `Math.random()` and `Math.floor()` for visual randomization.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS Variable Controller</title>
  <style>
    :root {
      --hue: 262;
      --accent:    hsl(var(--hue), 70%, 62%);
      --accent-bg: hsl(var(--hue), 70%, 20%);
      --page-bg:   hsl(var(--hue), 30%, 10%);
      --card-bg:   hsl(var(--hue), 30%, 16%);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: var(--page-bg);
      color: #eee;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      gap: 1.5rem;
      transition: background 0.5s;
    }

    h1 {
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--accent);
      text-align: center;
      transition: color 0.5s;
    }

    .subtitle {
      font-size: 0.85rem;
      opacity: 0.65;
      text-align: center;
      max-width: 400px;
      line-height: 1.5;
    }

    .card {
      background: var(--card-bg);
      border: 2px solid var(--accent);
      border-radius: 16px;
      padding: 2rem 2.5rem;
      max-width: 400px;
      width: 100%;
      text-align: center;
      transition: background 0.5s, border-color 0.5s;
    }

    .card .label {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent);
      margin-bottom: 0.5rem;
      transition: color 0.5s;
    }

    .hue-number {
      font-size: 3.5rem;
      font-weight: 800;
      color: var(--accent);
      line-height: 1;
      margin-bottom: 0.5rem;
      font-variant-numeric: tabular-nums;
      transition: color 0.5s;
    }

    .card .note {
      font-size: 0.82rem;
      opacity: 0.65;
      line-height: 1.5;
    }

    .btn-row {
      display: flex;
      gap: 0.75rem;
    }

    .btn-primary {
      padding: 0.65rem 1.75rem;
      background: var(--accent);
      color: #fff;
      border: none;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.5s;
    }

    .btn-outline {
      padding: 0.65rem 1.25rem;
      background: transparent;
      color: var(--accent);
      border: 2px solid var(--accent);
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: color 0.5s, border-color 0.5s;
    }

    .code-line {
      background: #0d1117;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      max-width: 400px;
      width: 100%;
      color: #aaa;
      text-align: center;
    }

    .code-line .hl { color: #55efc4; }
  </style>
</head>
<body>

  <h1>CSS Variable Controller</h1>
  <p class="subtitle">
    One JavaScript call updates <code>--hue</code>.<br>
    Every element using <code>var(--accent)</code> shifts to the new color instantly.
  </p>

  <div class="card">
    <p class="label">Current <code>--hue</code> value</p>
    <p class="hue-number" id="hue-display">—</p>
    <p class="note">Borders, text, and buttons all read from <code>var(--accent)</code>, which is built from <code>--hue</code>. Change one variable, everything shifts.</p>
  </div>

  <div class="btn-row">
    <button class="btn-primary"  onclick="randomTheme()">New Random Theme</button>
    <button class="btn-outline"  onclick="applyTheme(262)">Reset to Default</button>
  </div>

  <div class="code-line" id="code-display">
    document.documentElement.style.setProperty(<span class="hl">'--hue'</span>, <span class="hl" id="hue-inline">…</span>);
  </div>

  <script>
    function applyTheme(hue) {
      // setProperty() updates a CSS custom property from JavaScript
      document.documentElement.style.setProperty('--hue', hue);

      // Update the display to show the new value
      document.querySelector('#hue-display').textContent  = hue;
      document.querySelector('#hue-inline').textContent   = hue;
    }

    function randomTheme() {
      // Math.random() → a decimal from 0.0 to 0.9999
      // Math.floor()  → rounds it down to a whole number
      // * 360         → gives a hue from 0 to 359
      const hue = Math.floor(Math.random() * 360);
      applyTheme(hue);
    }

    // Run immediately on page load — page arrives with a random theme
    randomTheme();
  </script>

</body>
</html>
```

---

## CodePen 5 — classList Toggle Demo

**Placement:** After the "classList — The Bridge Between JavaScript and CSS" section.
**Demonstrates:** `classList.toggle()`, `classList.contains()`, and the core principle: CSS defines two visual states, JavaScript switches between them by toggling a class — the CSS transition fires automatically.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>classList Toggle Demo</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      gap: 1.5rem;
    }

    /* ── State 1: default ─────────────────────────────────── */
    .project-card {
      background: #16213e;
      border: 2px solid #2d3561;
      border-radius: 14px;
      padding: 2rem 2.5rem;
      max-width: 380px;
      width: 100%;
      text-align: center;

      /* CSS handles all the animation — JS only toggles the class */
      transform: scale(1);
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
      transition: transform      0.3s ease,
                  box-shadow     0.3s ease,
                  border-color   0.3s ease,
                  background     0.3s ease;
    }

    /* ── State 2: .featured ──────────────────────────────── */
    .project-card.featured {
      transform: scale(1.06);
      box-shadow: 0 14px 44px rgba(108, 92, 231, 0.45);
      border-color: #6c5ce7;
      background: #1e1a3a;
    }

    .project-card h2 {
      font-size: 1.2rem;
      margin-bottom: 0.5rem;
    }

    .project-card p {
      font-size: 0.85rem;
      opacity: 0.7;
      line-height: 1.6;
    }

    /* ── Status badge ─────────────────────────────────────── */
    .status-badge {
      display: inline-block;
      background: #2d3561;
      color: #a29bfe;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      padding: 0.2rem 0.65rem;
      border-radius: 100px;
      margin-top: 1rem;
      transition: background 0.3s, color 0.3s;
    }

    .project-card.featured .status-badge {
      background: #6c5ce7;
      color: #fff;
    }

    /* ── Toggle button ─────────────────────────────────────── */
    .toggle-btn {
      padding: 0.65rem 1.75rem;
      background: #6c5ce7;
      color: #fff;
      border: none;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
    }

    /* ── Explanation panel ────────────────────────────────── */
    .explain {
      background: #0d1117;
      border-radius: 10px;
      padding: 1rem 1.25rem;
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      max-width: 380px;
      width: 100%;
      line-height: 1.8;
      color: #aaa;
      text-align: center;
    }

    .explain .hl   { color: #55efc4; }
    .explain .dim  { opacity: 0.45; }
  </style>
</head>
<body>

  <div class="project-card" id="project-card">
    <h2>Portfolio Project</h2>
    <p>CSS defines what both states look like.<br>
    JavaScript flips between them with one line.</p>
    <span class="status-badge" id="status-badge">default state</span>
  </div>

  <button class="toggle-btn" onclick="toggleFeatured()">Toggle .featured Class</button>

  <div class="explain">
    <span class="dim">card.classList.</span><span class="hl" id="method-display">toggle</span><span class="dim">('featured')</span><br>
    <span class="dim">class list: </span><span class="hl" id="class-display">card</span>
  </div>

  <script>
    function toggleFeatured() {
      const card = document.querySelector('#project-card');

      // One line — CSS transition handles all the animation
      card.classList.toggle('featured');

      // classList.contains() returns true or false
      // (if/else covered in Lesson 19 — preview below)
      if (card.classList.contains('featured')) {
        document.querySelector('#status-badge').textContent    = '.featured is active';
        document.querySelector('#class-display').textContent   = 'card featured';
        document.querySelector('#method-display').textContent  = 'toggle → added';
      } else {
        document.querySelector('#status-badge').textContent    = 'default state';
        document.querySelector('#class-display').textContent   = 'card';
        document.querySelector('#method-display').textContent  = 'toggle → removed';
      }
    }
  </script>

</body>
</html>
```

---

## CodePen 6 — Create and Remove Elements

**Placement:** After the "Creating and Removing Elements" section.
**Demonstrates:** `document.createElement()`, `classList.add()`, `textContent`, `appendChild()`, and `element.remove()` — building and tearing down real DOM elements on demand.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Create &amp; Remove Elements</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      padding: 2rem;
      max-width: 640px;
      margin: 0 auto;
    }

    h1 {
      font-size: 1.3rem;
      font-weight: 700;
      color: #a29bfe;
      margin-bottom: 0.35rem;
    }

    .subtitle {
      font-size: 0.85rem;
      opacity: 0.6;
      margin-bottom: 1.5rem;
    }

    .input-row {
      display: flex;
      gap: 0.6rem;
      margin-bottom: 1.75rem;
    }

    input[type="text"] {
      flex: 1;
      padding: 0.6rem 1rem;
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 8px;
      color: #eee;
      font-size: 0.9rem;
      font-family: inherit;
      outline: none;
    }

    input[type="text"]:focus {
      border-color: #6c5ce7;
    }

    input::placeholder { opacity: 0.45; }

    .add-btn {
      padding: 0.6rem 1.25rem;
      background: #6c5ce7;
      color: #fff;
      border: none;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
      gap: 0.75rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 10px;
      padding: 1rem;
      position: relative;
      animation: appear 0.2s ease;
    }

    @keyframes appear {
      from { opacity: 0; transform: scale(0.9); }
      to   { opacity: 1; transform: scale(1); }
    }

    .card-label {
      font-size: 0.9rem;
      font-weight: 600;
      padding-right: 1.5rem;
      word-break: break-word;
    }

    .card-id {
      font-size: 0.7rem;
      opacity: 0.4;
      font-family: 'Courier New', monospace;
      margin-top: 0.35rem;
    }

    .remove-btn {
      position: absolute;
      top: 0.5rem;
      right: 0.5rem;
      width: 1.5rem;
      height: 1.5rem;
      background: transparent;
      border: none;
      color: #636e72;
      font-size: 0.85rem;
      cursor: pointer;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s, color 0.15s;
      padding: 0;
    }

    .remove-btn:hover {
      background: #d63031;
      color: #fff;
    }

    .empty-state {
      text-align: center;
      padding: 2rem;
      opacity: 0.35;
      font-size: 0.9rem;
      display: none;
    }

    .empty-state.visible {
      display: block;
    }
  </style>
</head>
<body>

  <h1>Create &amp; Remove Elements</h1>
  <p class="subtitle">Type a name and click Add. Each card is created with JavaScript — no HTML was written for it.</p>

  <div class="input-row">
    <input type="text" id="item-input" placeholder="Enter a name or label…" maxlength="40">
    <button class="add-btn" onclick="addCard()">+ Add Card</button>
  </div>

  <div class="grid"    id="card-grid"></div>
  <p   class="empty-state visible" id="empty-state">No cards yet — add one above.</p>

  <script>
    let cardCount = 0;

    function addCard() {
      const input = document.querySelector('#item-input');
      const text  = input.value.trim();

      // Simple guard — stop if the input is empty (conditionals: Lesson 19)
      if (text === '') {
        return;
      }

      // ── Step 1: Create a new empty element ────────────────────────
      const card = document.createElement('div');

      // ── Step 2: Configure it ──────────────────────────────────────
      card.classList.add('card');
      cardCount = cardCount + 1;
      card.id = 'card-' + cardCount;

      // ── Build the label ───────────────────────────────────────────
      const label = document.createElement('p');
      label.classList.add('card-label');
      label.textContent = text;

      const idTag = document.createElement('p');
      idTag.classList.add('card-id');
      idTag.textContent = 'id="card-' + cardCount + '"';

      // ── Build the remove button ───────────────────────────────────
      const removeBtn = document.createElement('button');
      removeBtn.classList.add('remove-btn');
      removeBtn.textContent = '✕';
      removeBtn.title = 'Remove this card';

      // Store the card's id on the button as a data attribute
      // so the remove function knows which card to delete
      removeBtn.setAttribute('data-target', 'card-' + cardCount);
      removeBtn.setAttribute('onclick', 'removeCard(this)');

      // ── Step 3: Assemble and append to the page ───────────────────
      card.appendChild(label);
      card.appendChild(idTag);
      card.appendChild(removeBtn);
      document.querySelector('#card-grid').appendChild(card);

      // Clear input and hide empty state
      input.value = '';
      input.focus();
      document.querySelector('#empty-state').classList.remove('visible');
    }

    function removeCard(btn) {
      // Read the data attribute to find the right card
      const targetId = btn.dataset.target;
      document.querySelector('#' + targetId).remove();

      // Show empty state if grid is now empty
      const grid = document.querySelector('#card-grid');
      if (grid.children.length === 0) {
        document.querySelector('#empty-state').classList.add('visible');
      }
    }
  </script>

</body>
</html>
```

---

## CodePen 7 — data-* Color Swatches

**Placement:** After the "data-* Attributes and dataset" section.
**Demonstrates:** Reading `data-color` and `data-name` from HTML via `dataset.color` and `dataset.name`, setting `style.backgroundColor` from those values, and using an inline `onclick` that reads the swatch's own dataset to update a global CSS custom property.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>data-* Color Swatches</title>
  <style>
    :root {
      --selected: #6c5ce7;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      gap: 2rem;
    }

    h1 {
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--selected);
      text-align: center;
      transition: color 0.3s;
    }

    .subtitle {
      font-size: 0.85rem;
      opacity: 0.6;
      text-align: center;
      max-width: 420px;
      line-height: 1.5;
      margin-top: -1rem;
    }

    /* ── Swatch grid ───────────────────────────────────────── */
    .swatch-row {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
      justify-content: center;
    }

    /* data-color and data-name are in the HTML — JS reads them */
    .swatch {
      width: 90px;
      height: 90px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.78rem;
      font-weight: 700;
      color: #fff;
      text-shadow: 0 1px 3px rgba(0,0,0,0.4);
      cursor: pointer;
      border: 3px solid transparent;
      transition: transform 0.2s, border-color 0.2s;
    }

    .swatch:hover {
      transform: scale(1.08);
    }

    .swatch.active {
      border-color: #fff;
      transform: scale(1.1);
    }

    /* ── Selected color display ─────────────────────────────── */
    .selected-display {
      background: #16213e;
      border: 2px solid var(--selected);
      border-radius: 12px;
      padding: 1.25rem 2rem;
      text-align: center;
      max-width: 360px;
      width: 100%;
      transition: border-color 0.3s;
    }

    .color-name {
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--selected);
      transition: color 0.3s;
    }

    .color-hex {
      font-size: 0.9rem;
      font-family: 'Courier New', monospace;
      opacity: 0.65;
      margin-top: 0.25rem;
    }

    /* ── Dataset reference panel ────────────────────────────── */
    .code-panel {
      background: #0d1117;
      border-radius: 10px;
      padding: 0.85rem 1.25rem;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      max-width: 420px;
      width: 100%;
      color: #aaa;
      line-height: 1.9;
    }

    .attr  { color: #74b9ff; }
    .val   { color: #55efc4; }
    .prop  { color: #a29bfe; }
  </style>
</head>
<body>

  <h1 id="page-title">Click a Swatch</h1>
  <p class="subtitle">The color and name live in <code>data-*</code> attributes in the HTML. JavaScript reads them through <code>dataset</code>.</p>

  <!--
    The data-color and data-name values are stored here in the HTML.
    JavaScript reads them with: swatch.dataset.color and swatch.dataset.name
    Background colors are NOT set in CSS — JS applies them on page load.
  -->
  <div class="swatch-row">
    <div class="swatch" data-color="#6c5ce7" data-name="Violet"  onclick="selectSwatch(this)"></div>
    <div class="swatch" data-color="#00b894" data-name="Emerald" onclick="selectSwatch(this)"></div>
    <div class="swatch" data-color="#e17055" data-name="Coral"   onclick="selectSwatch(this)"></div>
    <div class="swatch" data-color="#0984e3" data-name="Cobalt"  onclick="selectSwatch(this)"></div>
    <div class="swatch" data-color="#fdcb6e" data-name="Gold"    onclick="selectSwatch(this)"></div>
    <div class="swatch" data-color="#fd79a8" data-name="Rose"    onclick="selectSwatch(this)"></div>
  </div>

  <div class="selected-display">
    <p class="color-name" id="color-name">—</p>
    <p class="color-hex"  id="color-hex">click a swatch to select</p>
  </div>

  <div class="code-panel" id="dataset-demo">
    Reading dataset on page load…
  </div>

  <script>
    // ── Read dataset on page load and apply background colors ─────────
    const swatches = document.querySelectorAll('.swatch');

    // Preview of for loops — covered fully in Lesson 21
    for (let i = 0; i < swatches.length; i++) {
      const swatch = swatches[i];

      // dataset.color reads the data-color attribute
      swatch.style.backgroundColor = swatch.dataset.color;

      // dataset.name reads the data-name attribute
      swatch.textContent = swatch.dataset.name;
    }

    // Show the dataset of the first swatch as a reference
    const first = swatches[0];
    document.querySelector('#dataset-demo').innerHTML =
      '&lt;div <span class="attr">data-color</span>=<span class="val">"' + first.dataset.color + '"</span><br>' +
      '     <span class="attr">data-name</span>=<span class="val">"' + first.dataset.name + '"</span>&gt;<br><br>' +
      'element.<span class="prop">dataset.color</span>  →  <span class="val">"' + first.dataset.color + '"</span><br>' +
      'element.<span class="prop">dataset.name</span>   →  <span class="val">"' + first.dataset.name + '"</span>';

    // ── onClick: read dataset from the clicked swatch ─────────────────
    function selectSwatch(el) {
      // Read data-* attributes through dataset
      const color = el.dataset.color;
      const name  = el.dataset.name;

      // Update the CSS custom property — affects everything using var(--selected)
      document.documentElement.style.setProperty('--selected', color);

      // Update the display panel
      document.querySelector('#color-name').textContent = name;
      document.querySelector('#color-hex').textContent  = color;
      document.querySelector('#page-title').textContent = name + ' selected';

      // Toggle .active class (classList covered earlier in this lesson)
      const allSwatches = document.querySelectorAll('.swatch');
      for (let i = 0; i < allSwatches.length; i++) {
        allSwatches[i].classList.remove('active');
      }
      el.classList.add('active');

      // Show this swatch's dataset in the reference panel
      document.querySelector('#dataset-demo').innerHTML =
        '&lt;div <span class="attr">data-color</span>=<span class="val">"' + color + '"</span><br>' +
        '     <span class="attr">data-name</span>=<span class="val">"' + name + '"</span>&gt;<br><br>' +
        'element.<span class="prop">dataset.color</span>  →  <span class="val">"' + color + '"</span><br>' +
        'element.<span class="prop">dataset.name</span>   →  <span class="val">"' + name + '"</span>';
    }

    // Select the first swatch on page load
    selectSwatch(swatches[0]);
  </script>

</body>
</html>
```
