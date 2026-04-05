# Day 19 — CodePen Examples
## Click, Type, Submit: Events, Decisions, and Live Feedback

---

## CodePen 1 — Live Theme Customizer

**Placement:** After the "addEventListener — The Right Way" section.
**Demonstrates:** `addEventListener('input')`, `event.target.value`, `style.setProperty()` — three range sliders controlling CSS custom properties in real time.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Live Theme Customizer</title>
  <style>
    :root {
      --hue: 262;
      --saturation: 70%;
      --lightness: 55%;
      --accent: hsl(var(--hue), var(--saturation), var(--lightness));
      --bg:     hsl(var(--hue), 30%, 10%);
      --card:   hsl(var(--hue), 30%, 16%);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: var(--bg);
      color: #eee;
      min-height: 100vh;
      display: grid;
      grid-template-columns: 280px 1fr;
      transition: background 0.2s;
    }

    /* ── Control Panel ───────────────────────────────────── */
    .panel {
      background: rgba(0,0,0,0.3);
      padding: 2rem 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.75rem;
    }

    .panel h2 {
      font-size: 1rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.25rem;
    }

    .control {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .control label {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      opacity: 0.65;
      display: flex;
      justify-content: space-between;
    }

    .control label span {
      color: var(--accent);
      font-weight: 700;
      font-family: 'Courier New', monospace;
    }

    input[type="range"] {
      width: 100%;
      accent-color: var(--accent);
      cursor: pointer;
    }

    /* ── Preview Area ─────────────────────────────────────── */
    .preview {
      padding: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      justify-content: center;
    }

    .preview h1 {
      font-size: 1.6rem;
      color: var(--accent);
      transition: color 0.2s;
    }

    .card {
      background: var(--card);
      border: 2px solid var(--accent);
      border-radius: 12px;
      padding: 1.25rem 1.5rem;
      transition: background 0.2s, border-color 0.2s;
    }

    .card p { font-size: 0.9rem; opacity: 0.75; line-height: 1.6; }

    .pill-row {
      display: flex;
      gap: 0.6rem;
      flex-wrap: wrap;
    }

    .pill {
      padding: 0.35rem 0.9rem;
      border-radius: 100px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: default;
    }

    .pill.filled  { background: var(--accent); color: #fff; }
    .pill.outline { border: 2px solid var(--accent); color: var(--accent); }

    .code-line {
      background: #0d1117;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      color: #aaa;
      line-height: 1.8;
    }
    .hl { color: #55efc4; }
  </style>
</head>
<body>

  <div class="panel">
    <div>
      <h2>Theme Customizer</h2>
      <p style="font-size:0.8rem;opacity:0.5;margin-top:0.25rem;">Drag the sliders — the page updates live.</p>
    </div>

    <div class="control">
      <label>Hue <span id="hue-val">262</span></label>
      <input type="range" id="hue" min="0" max="360" value="262">
    </div>

    <div class="control">
      <label>Saturation <span id="sat-val">70%</span></label>
      <input type="range" id="saturation" min="20" max="100" value="70">
    </div>

    <div class="control">
      <label>Lightness <span id="light-val">55%</span></label>
      <input type="range" id="lightness" min="30" max="75" value="55">
    </div>

    <div class="code-line" id="code-output">
      --hue: <span class="hl" id="code-hue">262</span><br>
      --saturation: <span class="hl" id="code-sat">70%</span><br>
      --lightness: <span class="hl" id="code-light">55%</span>
    </div>
  </div>

  <div class="preview">
    <h1>Live Theme Preview</h1>
    <div class="card">
      <p>Every element using <code>var(--accent)</code> updates instantly. One CSS custom property, changed by JavaScript, cascades to everything.</p>
    </div>
    <div class="pill-row">
      <span class="pill filled">Primary Button</span>
      <span class="pill outline">Outline Button</span>
      <span class="pill filled">Badge</span>
    </div>
  </div>

  <script>
    const hueSlider   = document.querySelector('#hue');
    const satSlider   = document.querySelector('#saturation');
    const lightSlider = document.querySelector('#lightness');

    function updateTheme() {
      const hue   = hueSlider.value;
      const sat   = satSlider.value + '%';
      const light = lightSlider.value + '%';

      // Each setProperty() call updates one CSS custom property
      // Every element using var(--accent), var(--bg), or var(--card) reacts
      document.documentElement.style.setProperty('--hue',       hue);
      document.documentElement.style.setProperty('--saturation', sat);
      document.documentElement.style.setProperty('--lightness',  light);

      // Update the display labels
      document.querySelector('#hue-val').textContent   = hue;
      document.querySelector('#sat-val').textContent   = sat;
      document.querySelector('#light-val').textContent = light;

      // Update the code reference panel
      document.querySelector('#code-hue').textContent   = hue;
      document.querySelector('#code-sat').textContent   = sat;
      document.querySelector('#code-light').textContent = light;
    }

    // addEventListener('input') fires on EVERY change while dragging
    hueSlider.addEventListener('input',   function() { updateTheme(); });
    satSlider.addEventListener('input',   function() { updateTheme(); });
    lightSlider.addEventListener('input', function() { updateTheme(); });
  </script>

</body>
</html>
```

---

## CodePen 2 — Form Value Inspector

**Placement:** After the "Reading Form Values" section.
**Demonstrates:** Reading `.value`, `.checked`, `Number()` conversion from every common form element type. On submit with `event.preventDefault()`, all values display in a results panel.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Form Value Inspector</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      padding: 2rem;
      align-items: start;
      max-width: 860px;
      margin: 0 auto;
    }

    h2 {
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #74b9ff;
      margin-bottom: 1rem;
      grid-column: 1 / -1;
    }

    .form-col h2, .results-col h2 { grid-column: auto; }

    .form-col, .results-col {
      background: #16213e;
      border-radius: 12px;
      padding: 1.5rem;
    }

    .field {
      margin-bottom: 1.25rem;
    }

    label {
      display: block;
      font-size: 0.8rem;
      opacity: 0.6;
      margin-bottom: 0.35rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    input[type="text"],
    input[type="email"],
    input[type="number"],
    select,
    textarea {
      width: 100%;
      padding: 0.5rem 0.75rem;
      background: #0d1117;
      border: 1px solid #2d3561;
      border-radius: 6px;
      color: #eee;
      font-size: 0.9rem;
      font-family: inherit;
      outline: none;
    }

    input[type="text"]:focus,
    input[type="email"]:focus,
    select:focus { border-color: #6c5ce7; }

    .checkbox-row {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.9rem;
    }

    input[type="range"] {
      width: 100%;
      accent-color: #6c5ce7;
      margin-top: 0.35rem;
    }

    input[type="color"] {
      width: 3rem;
      height: 2rem;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      background: none;
    }

    .submit-btn {
      width: 100%;
      padding: 0.65rem;
      background: #6c5ce7;
      color: #fff;
      border: none;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      margin-top: 0.5rem;
    }

    .results-col h2 { margin-bottom: 1rem; }

    .result-row {
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
      padding: 0.6rem 0;
      border-bottom: 1px solid #2d3561;
      font-size: 0.85rem;
    }

    .result-row:last-child { border-bottom: none; }

    .result-label {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      opacity: 0.5;
    }

    .result-value {
      font-family: 'Courier New', monospace;
      color: #55efc4;
    }

    .result-type {
      font-size: 0.72rem;
      color: #a29bfe;
      opacity: 0.8;
    }

    .empty-state {
      text-align: center;
      opacity: 0.35;
      font-size: 0.85rem;
      padding: 2rem 0;
    }
  </style>
</head>
<body>

  <div class="form-col">
    <h2>Form Inputs</h2>
    <form id="inspector-form">

      <div class="field">
        <label>Text Input</label>
        <input type="text" id="name" placeholder="Your name">
      </div>

      <div class="field">
        <label>Dropdown (select)</label>
        <select id="role">
          <option value="student">Student</option>
          <option value="designer">Designer</option>
          <option value="developer">Developer</option>
        </select>
      </div>

      <div class="field">
        <label>Number Input</label>
        <input type="number" id="age" value="25" min="1" max="120">
      </div>

      <div class="field">
        <label>Range Slider</label>
        <input type="range" id="score" min="0" max="100" value="72">
      </div>

      <div class="field">
        <label>Color Picker</label>
        <input type="color" id="fav-color" value="#6c5ce7">
      </div>

      <div class="field">
        <div class="checkbox-row">
          <input type="checkbox" id="agree" checked>
          <label style="margin:0;opacity:1;">I agree to the terms</label>
        </div>
      </div>

      <button type="submit" class="submit-btn">Inspect Values</button>
    </form>
  </div>

  <div class="results-col">
    <h2>Values Read by JS</h2>
    <div id="results">
      <p class="empty-state">Submit the form to see<br>how JavaScript reads each value.</p>
    </div>
  </div>

  <script>
    const form = document.querySelector('#inspector-form');

    form.addEventListener('submit', function(event) {
      event.preventDefault();  // Stop the page from refreshing

      // Read each form element
      const nameVal  = document.querySelector('#name').value;
      const roleVal  = document.querySelector('#role').value;
      const ageStr   = document.querySelector('#age').value;
      const ageNum   = Number(document.querySelector('#age').value);  // string → number
      const score    = document.querySelector('#score').value;
      const color    = document.querySelector('#fav-color').value;
      const isAgreed = document.querySelector('#agree').checked;

      const results = [
        { label: 'Text Input',         value: '"' + nameVal + '"',    type: 'string — input.value' },
        { label: 'Dropdown',           value: '"' + roleVal + '"',    type: 'string — select.value' },
        { label: 'Number (raw)',        value: '"' + ageStr + '"',     type: 'string — input.value (always!)' },
        { label: 'Number (converted)', value: ageNum,                  type: 'number — Number(input.value)' },
        { label: 'Range Slider',       value: '"' + score + '"',      type: 'string — input.value' },
        { label: 'Color Picker',       value: '"' + color + '"',      type: 'string — input.value (hex)' },
        { label: 'Checkbox',           value: isAgreed,               type: 'boolean — input.checked' }
      ];

      const container = document.querySelector('#results');
      container.innerHTML = '';

      for (let i = 0; i < results.length; i++) {
        const r   = results[i];
        const row = document.createElement('div');
        row.classList.add('result-row');
        row.innerHTML =
          '<span class="result-label">' + r.label + '</span>' +
          '<span class="result-value">' + r.value + '</span>' +
          '<span class="result-type">' + r.type + '</span>';
        container.appendChild(row);
      }
    });
  </script>

</body>
</html>
```

---

## CodePen 3 — Click Counter with Conditional Feedback

**Placement:** After the "Making Decisions: if, else if, else" section.
**Demonstrates:** `addEventListener('click')`, incrementing a `let` variable, `if/else if/else` with multiple branches, `classList` for visual state changes.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Click Counter</title>
  <style>
    :root { --accent: #6c5ce7; }

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
      gap: 1.5rem;
      padding: 2rem;
    }

    .counter-display {
      font-size: 5rem;
      font-weight: 800;
      color: var(--accent);
      font-variant-numeric: tabular-nums;
      transition: color 0.3s, transform 0.15s;
      line-height: 1;
    }

    .counter-display.bump {
      transform: scale(1.15);
    }

    .message {
      font-size: 1.1rem;
      font-weight: 600;
      min-height: 1.5rem;
      text-align: center;
      transition: color 0.3s;
    }

    .message.grey   { color: #636e72; }
    .message.blue   { color: #74b9ff; }
    .message.green  { color: #55efc4; }
    .message.gold   { color: #fdcb6e; }
    .message.purple { color: #a29bfe; }

    .progress-bar {
      width: 280px;
      height: 8px;
      background: #2d3561;
      border-radius: 100px;
      overflow: hidden;
    }

    .progress-fill {
      height: 100%;
      background: var(--accent);
      border-radius: 100px;
      width: 0%;
      transition: width 0.3s, background 0.3s;
    }

    .btn-row {
      display: flex;
      gap: 0.75rem;
    }

    .click-btn {
      padding: 0.75rem 2rem;
      background: var(--accent);
      color: #fff;
      border: none;
      border-radius: 10px;
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
      transition: transform 0.1s, background 0.3s;
    }

    .click-btn:active { transform: scale(0.95); }

    .reset-btn {
      padding: 0.75rem 1.25rem;
      background: transparent;
      color: #636e72;
      border: 2px solid #2d3561;
      border-radius: 10px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
    }

    .stage-list {
      background: #16213e;
      border-radius: 10px;
      padding: 1rem 1.25rem;
      font-size: 0.8rem;
      width: 280px;
    }

    .stage-list p {
      padding: 0.3rem 0;
      border-bottom: 1px solid #2d3561;
      opacity: 0.55;
      transition: opacity 0.3s, color 0.3s;
    }

    .stage-list p:last-child { border-bottom: none; }
    .stage-list p.active { opacity: 1; color: var(--accent); }
  </style>
</head>
<body>

  <p class="counter-display" id="count">0</p>
  <p class="message grey" id="message">Start clicking!</p>

  <div class="progress-bar">
    <div class="progress-fill" id="progress"></div>
  </div>

  <div class="btn-row">
    <button class="click-btn" id="click-btn">Click Me</button>
    <button class="reset-btn" id="reset-btn">Reset</button>
  </div>

  <div class="stage-list">
    <p id="stage-0" class="active">0 clicks — waiting...</p>
    <p id="stage-1">1–4 — warming up</p>
    <p id="stage-2">5–9 — getting there</p>
    <p id="stage-3">10–19 — on a roll!</p>
    <p id="stage-4">20+ — unstoppable!</p>
  </div>

  <script>
    let clicks = 0;

    const countDisplay = document.querySelector('#count');
    const message      = document.querySelector('#message');
    const progress     = document.querySelector('#progress');
    const stages       = document.querySelectorAll('.stage-list p');

    function updateUI() {
      // Update the number
      countDisplay.textContent = clicks;

      // Animate the number on click
      countDisplay.classList.add('bump');
      setTimeout(function() { countDisplay.classList.remove('bump'); }, 150);

      // if / else if / else — branches based on click count
      if (clicks === 0) {
        message.textContent = 'Start clicking!';
        message.className   = 'message grey';
        document.documentElement.style.setProperty('--accent', '#6c5ce7');
        progress.style.width = '0%';
        progress.style.background = '#6c5ce7';

      } else if (clicks < 5) {
        message.textContent = 'Warming up... keep going!';
        message.className   = 'message blue';
        document.documentElement.style.setProperty('--accent', '#74b9ff');
        progress.style.width = (clicks / 20 * 100) + '%';
        progress.style.background = '#74b9ff';

      } else if (clicks < 10) {
        message.textContent = 'Getting there! Almost halfway.';
        message.className   = 'message green';
        document.documentElement.style.setProperty('--accent', '#00b894');
        progress.style.width = (clicks / 20 * 100) + '%';
        progress.style.background = '#00b894';

      } else if (clicks < 20) {
        message.textContent = "On a roll! Don't stop now.";
        message.className   = 'message gold';
        document.documentElement.style.setProperty('--accent', '#fdcb6e');
        progress.style.width = (clicks / 20 * 100) + '%';
        progress.style.background = '#fdcb6e';

      } else {
        message.textContent = 'Unstoppable! ' + clicks + ' clicks!';
        message.className   = 'message purple';
        document.documentElement.style.setProperty('--accent', '#fd79a8');
        progress.style.width = '100%';
        progress.style.background = '#fd79a8';
      }

      // Update active stage in the list
      for (let i = 0; i < stages.length; i++) {
        stages[i].classList.remove('active');
      }

      if      (clicks === 0)  { stages[0].classList.add('active'); }
      else if (clicks < 5)    { stages[1].classList.add('active'); }
      else if (clicks < 10)   { stages[2].classList.add('active'); }
      else if (clicks < 20)   { stages[3].classList.add('active'); }
      else                    { stages[4].classList.add('active'); }
    }

    document.querySelector('#click-btn').addEventListener('click', function() {
      clicks = clicks + 1;
      updateUI();
    });

    document.querySelector('#reset-btn').addEventListener('click', function() {
      clicks = 0;
      updateUI();
    });
  </script>

</body>
</html>
```

---

## CodePen 4 — Password Strength Indicator

**Placement:** After the "Truthy and Falsy" / "Ternary Operator" sections.
**Demonstrates:** `addEventListener('input')`, truthy/falsy checks, multiple `if/else if` conditions, live visual feedback with colored bar and label. Pays off form knowledge from Day 14.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Password Strength</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }

    .card {
      background: #16213e;
      border-radius: 16px;
      padding: 2rem 2.5rem;
      width: 100%;
      max-width: 420px;
    }

    h2 {
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
    }

    .subtitle {
      font-size: 0.85rem;
      opacity: 0.55;
      margin-bottom: 1.75rem;
    }

    .field {
      margin-bottom: 1rem;
    }

    label {
      display: block;
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      opacity: 0.6;
      margin-bottom: 0.4rem;
    }

    .input-wrap {
      position: relative;
    }

    input[type="password"],
    input[type="text"] {
      width: 100%;
      padding: 0.65rem 2.75rem 0.65rem 0.9rem;
      background: #0d1117;
      border: 2px solid #2d3561;
      border-radius: 8px;
      color: #eee;
      font-size: 1rem;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s;
    }

    input:focus { border-color: #6c5ce7; }

    .toggle-vis {
      position: absolute;
      right: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      color: #636e72;
      cursor: pointer;
      font-size: 1rem;
      padding: 0;
    }

    /* ── Strength Bar ─────────────────────────────────────── */
    .strength-bar {
      height: 6px;
      background: #2d3561;
      border-radius: 100px;
      margin: 0.75rem 0 0.5rem;
      overflow: hidden;
    }

    .strength-fill {
      height: 100%;
      border-radius: 100px;
      width: 0%;
      transition: width 0.3s ease, background 0.3s ease;
    }

    .strength-label {
      font-size: 0.8rem;
      font-weight: 600;
      min-height: 1.2rem;
    }

    /* ── Requirements Checklist ───────────────────────────── */
    .requirements {
      margin-top: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }

    .req {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.82rem;
      opacity: 0.45;
      transition: opacity 0.2s, color 0.2s;
    }

    .req.met {
      opacity: 1;
      color: #55efc4;
    }

    .req .icon {
      font-size: 0.8rem;
      width: 1rem;
      text-align: center;
    }
  </style>
</head>
<body>

  <div class="card">
    <h2>Create a Password</h2>
    <p class="subtitle">Strength updates as you type.</p>

    <div class="field">
      <label>Password</label>
      <div class="input-wrap">
        <input type="password" id="password-input" placeholder="Enter a password…" autocomplete="new-password">
        <button class="toggle-vis" id="toggle-vis" title="Show/hide password">&#128065;</button>
      </div>
      <div class="strength-bar">
        <div class="strength-fill" id="strength-fill"></div>
      </div>
      <p class="strength-label" id="strength-label" style="color:#636e72;">Start typing…</p>
    </div>

    <div class="requirements">
      <p class="req" id="req-length"><span class="icon">○</span> At least 8 characters</p>
      <p class="req" id="req-upper"> <span class="icon">○</span> One uppercase letter (A–Z)</p>
      <p class="req" id="req-number"><span class="icon">○</span> One number (0–9)</p>
      <p class="req" id="req-symbol"><span class="icon">○</span> One symbol (!@#$%…)</p>
    </div>
  </div>

  <script>
    const input    = document.querySelector('#password-input');
    const fill     = document.querySelector('#strength-fill');
    const label    = document.querySelector('#strength-label');
    const toggleBtn = document.querySelector('#toggle-vis');

    // Show/hide toggle
    toggleBtn.addEventListener('click', function() {
      if (input.type === 'password') {
        input.type = 'text';
      } else {
        input.type = 'password';
      }
    });

    // Live strength check — fires on every keystroke
    input.addEventListener('input', function() {
      const pw = input.value;

      // Check each requirement
      const hasLength = pw.length >= 8;
      const hasUpper  = /[A-Z]/.test(pw);
      const hasNumber = /[0-9]/.test(pw);
      const hasSymbol = /[^A-Za-z0-9]/.test(pw);

      // Update requirement indicators using ternary
      updateReq('req-length', hasLength);
      updateReq('req-upper',  hasUpper);
      updateReq('req-number', hasNumber);
      updateReq('req-symbol', hasSymbol);

      // Count how many requirements are met
      const score = (hasLength ? 1 : 0) + (hasUpper ? 1 : 0) +
                    (hasNumber ? 1 : 0) + (hasSymbol ? 1 : 0);

      // Truthy/falsy: if pw is empty string (''), it's falsy
      if (!pw) {
        fill.style.width      = '0%';
        fill.style.background = '#2d3561';
        label.textContent     = 'Start typing…';
        label.style.color     = '#636e72';

      } else if (score === 1) {
        fill.style.width      = '25%';
        fill.style.background = '#d63031';
        label.textContent     = 'Weak';
        label.style.color     = '#d63031';

      } else if (score === 2) {
        fill.style.width      = '50%';
        fill.style.background = '#fdcb6e';
        label.textContent     = 'Fair';
        label.style.color     = '#fdcb6e';

      } else if (score === 3) {
        fill.style.width      = '75%';
        fill.style.background = '#74b9ff';
        label.textContent     = 'Good';
        label.style.color     = '#74b9ff';

      } else {
        fill.style.width      = '100%';
        fill.style.background = '#00b894';
        label.textContent     = 'Strong ✓';
        label.style.color     = '#00b894';
      }
    });

    function updateReq(id, isMet) {
      const el   = document.querySelector('#' + id);
      const icon = el.querySelector('.icon');

      // Ternary: isMet is truthy → 'met' class, falsy → remove it
      if (isMet) {
        el.classList.add('met');
        icon.textContent = '✓';
      } else {
        el.classList.remove('met');
        icon.textContent = '○';
      }
    }
  </script>

</body>
</html>
```

---

## CodePen 5 — Color Picker Page Theming

**Placement:** After the "Live CSS Updates with Events" section.
**Demonstrates:** `<input type="color">` and `<input type="range">` combined to update multiple CSS custom properties. The most visual demo of events + CSS variables working together.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Color Picker Theming</title>
  <style>
    :root {
      --primary: #6c5ce7;
      --bg:      #1a1a2e;
      --card:    #16213e;
      --radius:  12px;
      --size:    1rem;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: var(--bg);
      color: #eee;
      min-height: 100vh;
      display: grid;
      grid-template-columns: 260px 1fr;
      transition: background 0.3s;
    }

    /* ── Controls sidebar ─────────────────────────────────── */
    .controls {
      padding: 2rem 1.5rem;
      background: rgba(0,0,0,0.25);
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .controls h2 {
      font-size: 1rem;
      font-weight: 700;
      color: var(--primary);
      transition: color 0.3s;
    }

    .control-group {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .control-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
    }

    .control-row label {
      font-size: 0.8rem;
      opacity: 0.65;
      white-space: nowrap;
    }

    input[type="color"] {
      width: 2.5rem;
      height: 1.75rem;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      background: none;
      padding: 0;
    }

    input[type="range"] {
      width: 100%;
      accent-color: var(--primary);
    }

    .range-row {
      display: flex;
      flex-direction: column;
      gap: 0.3rem;
    }

    .range-label {
      display: flex;
      justify-content: space-between;
      font-size: 0.78rem;
      opacity: 0.55;
    }

    .range-label span {
      color: var(--primary);
      font-family: 'Courier New', monospace;
      transition: color 0.3s;
    }

    .reset-btn {
      padding: 0.5rem;
      background: transparent;
      border: 1px solid #2d3561;
      border-radius: 6px;
      color: #636e72;
      font-size: 0.8rem;
      cursor: pointer;
      text-align: center;
    }

    /* ── Page preview ─────────────────────────────────────── */
    .page-preview {
      padding: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .page-preview h1 {
      font-size: calc(var(--size) * 1.6);
      color: var(--primary);
      transition: color 0.3s, font-size 0.3s;
    }

    .preview-card {
      background: var(--card);
      border: 2px solid var(--primary);
      border-radius: var(--radius);
      padding: 1.5rem;
      transition: background 0.3s, border-color 0.3s, border-radius 0.3s;
    }

    .preview-card h3 {
      color: var(--primary);
      margin-bottom: 0.5rem;
      font-size: calc(var(--size) * 1.1);
      transition: color 0.3s, font-size 0.3s;
    }

    .preview-card p {
      font-size: var(--size);
      opacity: 0.75;
      line-height: 1.6;
      transition: font-size 0.3s;
    }

    .btn-demo {
      display: inline-flex;
      gap: 0.75rem;
      flex-wrap: wrap;
      margin-top: 0.75rem;
    }

    .btn-filled {
      padding: 0.5rem 1.25rem;
      background: var(--primary);
      color: #fff;
      border: none;
      border-radius: calc(var(--radius) * 0.6);
      font-size: var(--size);
      cursor: default;
      transition: background 0.3s, border-radius 0.3s, font-size 0.3s;
    }

    .btn-outline {
      padding: 0.5rem 1.25rem;
      background: transparent;
      color: var(--primary);
      border: 2px solid var(--primary);
      border-radius: calc(var(--radius) * 0.6);
      font-size: var(--size);
      cursor: default;
      transition: color 0.3s, border-color 0.3s, border-radius 0.3s, font-size 0.3s;
    }
  </style>
</head>
<body>

  <div class="controls">
    <h2>Design Controls</h2>

    <div class="control-group">
      <div class="control-row">
        <label>Primary Color</label>
        <input type="color" id="primary-color" value="#6c5ce7">
      </div>
      <div class="control-row">
        <label>Background</label>
        <input type="color" id="bg-color" value="#1a1a2e">
      </div>
      <div class="control-row">
        <label>Card Color</label>
        <input type="color" id="card-color" value="#16213e">
      </div>
    </div>

    <div class="control-group">
      <div class="range-row">
        <div class="range-label">Border Radius <span id="radius-val">12px</span></div>
        <input type="range" id="radius-slider" min="0" max="32" value="12">
      </div>
      <div class="range-row">
        <div class="range-label">Font Size <span id="size-val">1rem</span></div>
        <input type="range" id="size-slider" min="12" max="22" value="16">
      </div>
    </div>

    <button class="reset-btn" id="reset-btn">Reset to Default</button>
  </div>

  <div class="page-preview">
    <h1>Page Preview</h1>

    <div class="preview-card">
      <h3>Design Card</h3>
      <p>Every property you see &mdash; color, border radius, font size &mdash; is controlled by a CSS custom property. JavaScript reads the control value and calls <code>style.setProperty()</code>. No inline styles on any element.</p>
      <div class="btn-demo">
        <button class="btn-filled">Primary Action</button>
        <button class="btn-outline">Secondary</button>
      </div>
    </div>

    <div class="preview-card">
      <h3>Second Card</h3>
      <p>Both cards share the same CSS variables. Change the primary color once &mdash; it updates everywhere at the same time.</p>
    </div>
  </div>

  <script>
    // Color pickers — 'input' fires on every change
    document.querySelector('#primary-color').addEventListener('input', function(event) {
      document.documentElement.style.setProperty('--primary', event.target.value);
    });

    document.querySelector('#bg-color').addEventListener('input', function(event) {
      document.documentElement.style.setProperty('--bg', event.target.value);
    });

    document.querySelector('#card-color').addEventListener('input', function(event) {
      document.documentElement.style.setProperty('--card', event.target.value);
    });

    // Range sliders
    document.querySelector('#radius-slider').addEventListener('input', function(event) {
      const val = event.target.value + 'px';
      document.documentElement.style.setProperty('--radius', val);
      document.querySelector('#radius-val').textContent = val;
    });

    document.querySelector('#size-slider').addEventListener('input', function(event) {
      const px  = Number(event.target.value);
      const rem = (px / 16).toFixed(2) + 'rem';
      document.documentElement.style.setProperty('--size', rem);
      document.querySelector('#size-val').textContent = rem;
    });

    // Reset to defaults
    document.querySelector('#reset-btn').addEventListener('click', function() {
      document.querySelector('#primary-color').value = '#6c5ce7';
      document.querySelector('#bg-color').value      = '#1a1a2e';
      document.querySelector('#card-color').value    = '#16213e';
      document.querySelector('#radius-slider').value = '12';
      document.querySelector('#size-slider').value   = '16';

      document.documentElement.style.setProperty('--primary', '#6c5ce7');
      document.documentElement.style.setProperty('--bg',      '#1a1a2e');
      document.documentElement.style.setProperty('--card',    '#16213e');
      document.documentElement.style.setProperty('--radius',  '12px');
      document.documentElement.style.setProperty('--size',    '1rem');

      document.querySelector('#radius-val').textContent = '12px';
      document.querySelector('#size-val').textContent   = '1rem';
    });
  </script>

</body>
</html>
```
