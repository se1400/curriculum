# Day 21 — CodePen Examples
## Write It Once: Functions, Loops, and Generating HTML

---

## CodePen 1 — Function Basics

**Placement:** After the "Function Declarations" section.
**Demonstrates:** Writing and calling functions with parameters and return values. `formatName()`, `formatPrice()`, `getDayGreeting()` — results displayed in a styled reference card.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Function Basics</title>
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

    h1 { font-size: 1.2rem; color: #a29bfe; margin-bottom: 1.5rem; }

    .fn-card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 12px;
      padding: 1.25rem 1.5rem;
      margin-bottom: 1rem;
    }

    .fn-card.active { border-color: #6c5ce7; }

    .fn-name {
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #74b9ff;
      margin-bottom: 0.35rem;
    }

    .fn-code {
      font-family: 'Courier New', monospace;
      font-size: 0.82rem;
      color: #636e72;
      margin-bottom: 0.75rem;
      padding: 0.5rem 0.75rem;
      background: #0d1117;
      border-radius: 6px;
    }

    .fn-code .kw  { color: #a29bfe; }
    .fn-code .fn  { color: #74b9ff; }
    .fn-code .str { color: #55efc4; }
    .fn-code .num { color: #fdcb6e; }

    .fn-result {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .result-label {
      font-size: 0.78rem;
      opacity: 0.5;
      white-space: nowrap;
    }

    .result-value {
      font-size: 1rem;
      font-weight: 700;
      color: #a29bfe;
    }

    .call-btn {
      margin-left: auto;
      padding: 0.35rem 0.85rem;
      background: #6c5ce7;
      color: #fff;
      border: none;
      border-radius: 6px;
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
    }
  </style>
</head>
<body>

  <h1>Function Basics — Define Once, Call Anywhere</h1>

  <!-- formatName -->
  <div class="fn-card">
    <p class="fn-name">formatName( first, last )</p>
    <div class="fn-code">
      <span class="kw">function</span> <span class="fn">formatName</span>(first, last) {<br>
      &nbsp;&nbsp;<span class="kw">return</span> last + <span class="str">', '</span> + first;<br>
      }
    </div>
    <div class="fn-result">
      <span class="result-label">formatName('Ada','Lovelace') →</span>
      <span class="result-value" id="name-result"></span>
      <button class="call-btn" onclick="callFormatName()">Call</button>
    </div>
  </div>

  <!-- formatPrice -->
  <div class="fn-card">
    <p class="fn-name">formatPrice( price )</p>
    <div class="fn-code">
      <span class="kw">function</span> <span class="fn">formatPrice</span>(price) {<br>
      &nbsp;&nbsp;<span class="kw">return</span> <span class="str">'$'</span> + price.toFixed(<span class="num">2</span>);<br>
      }
    </div>
    <div class="fn-result">
      <span class="result-label">formatPrice(9.9) →</span>
      <span class="result-value" id="price-result"></span>
      <button class="call-btn" onclick="callFormatPrice()">Call</button>
    </div>
  </div>

  <!-- greet with default -->
  <div class="fn-card">
    <p class="fn-name">greet( name = 'friend' ) &mdash; default parameter</p>
    <div class="fn-code">
      <span class="kw">function</span> <span class="fn">greet</span>(name = <span class="str">'friend'</span>) {<br>
      &nbsp;&nbsp;<span class="kw">return</span> <span class="str">`Hello, ${name}!`</span>;<br>
      }
    </div>
    <div class="fn-result">
      <span class="result-label">greet() →</span>
      <span class="result-value" id="greet-result"></span>
      <button class="call-btn" onclick="callGreet()">Call (no arg)</button>
    </div>
  </div>

  <!-- getDayGreeting -->
  <div class="fn-card">
    <p class="fn-name">getDayGreeting() &mdash; no parameters</p>
    <div class="fn-code">
      <span class="kw">function</span> <span class="fn">getDayGreeting</span>() {<br>
      &nbsp;&nbsp;<span class="kw">const</span> hour = <span class="kw">new</span> Date().getHours();<br>
      &nbsp;&nbsp;<span class="kw">if</span> (hour &lt; 12) <span class="kw">return</span> <span class="str">'Good morning!'</span>;<br>
      &nbsp;&nbsp;<span class="kw">if</span> (hour &lt; 18) <span class="kw">return</span> <span class="str">'Good afternoon!'</span>;<br>
      &nbsp;&nbsp;<span class="kw">return</span> <span class="str">'Good evening!'</span>;<br>
      }
    </div>
    <div class="fn-result">
      <span class="result-label">getDayGreeting() →</span>
      <span class="result-value" id="greeting-result"></span>
      <button class="call-btn" onclick="callGreeting()">Call</button>
    </div>
  </div>

  <script>
    // ── Function definitions ──────────────────────────────────

    function formatName(first, last) {
      return last + ', ' + first;
    }

    function formatPrice(price) {
      return '$' + price.toFixed(2);
    }

    function greet(name = 'friend') {
      return `Hello, ${name}!`;
    }

    function getDayGreeting() {
      const hour = new Date().getHours();
      if (hour < 12) return 'Good morning!';
      if (hour < 18) return 'Good afternoon!';
      return 'Good evening!';
    }

    // ── Call handlers ─────────────────────────────────────────

    function callFormatName() {
      document.querySelector('#name-result').textContent = formatName('Ada', 'Lovelace');
      document.querySelector('#name-result').closest('.fn-card').classList.add('active');
    }

    function callFormatPrice() {
      document.querySelector('#price-result').textContent = formatPrice(9.9);
      document.querySelector('#price-result').closest('.fn-card').classList.add('active');
    }

    function callGreet() {
      document.querySelector('#greet-result').textContent = greet();
      document.querySelector('#greet-result').closest('.fn-card').classList.add('active');
    }

    function callGreeting() {
      document.querySelector('#greeting-result').textContent = getDayGreeting();
      document.querySelector('#greeting-result').closest('.fn-card').classList.add('active');
    }

    // Run all on page load so the results are visible immediately
    callFormatName();
    callFormatPrice();
    callGreet();
    callGreeting();
  </script>

</body>
</html>
```

---

## CodePen 2 — Card Grid from Array

**Placement:** After the "Generating HTML with Loops" section.
**Demonstrates:** `for...of` loop building HTML string, `innerHTML` injection, CSS card grid styles applied automatically. An array of strings → a full styled flexbox card grid.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Card Grid from Array</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      padding: 2rem;
      max-width: 820px;
      margin: 0 auto;
    }

    .header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 1.5rem;
    }

    h1 { font-size: 1.2rem; color: #a29bfe; }

    .count {
      font-size: 0.8rem;
      color: #636e72;
    }

    /* ── The CSS grid layout — unchanged by JS ─────────────── */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 1rem;
      margin-bottom: 1.5rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 12px;
      padding: 1.25rem;
      transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    }

    .card:hover {
      transform: translateY(-4px);
      border-color: #6c5ce7;
      box-shadow: 0 8px 24px rgba(108,92,231,0.25);
    }

    .card-number {
      font-size: 0.68rem;
      color: #6c5ce7;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 0.4rem;
    }

    .card-title {
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
    }

    .card-sub {
      font-size: 0.78rem;
      color: #636e72;
    }

    /* ── Controls ─────────────────────────────────────────── */
    .btn-row { display: flex; gap: 0.6rem; flex-wrap: wrap; }

    .btn {
      padding: 0.45rem 1rem;
      border: none;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
    }

    .btn-primary { background: #6c5ce7; color: #fff; }
    .btn-outline { background: transparent; border: 2px solid #2d3561; color: #aaa; }
  </style>
</head>
<body>

  <div class="header">
    <h1>Destinations</h1>
    <span class="count" id="card-count"></span>
  </div>

  <!-- JS fills this grid — no cards are written in HTML -->
  <div class="card-grid" id="card-grid"></div>

  <div class="btn-row">
    <button class="btn btn-primary" id="shuffle-btn">Shuffle</button>
    <button class="btn btn-outline" id="reverse-btn">Reverse</button>
    <button class="btn btn-outline" id="reset-btn">Reset</button>
  </div>

  <script>
    // ── The data — an array of strings ────────────────────────
    const destinations = [
      'Tokyo', 'Lisbon', 'Chicago', 'Nairobi',
      'Sydney', 'Reykjavik', 'Medellín', 'Kyoto'
    ];

    // Keep a working copy so we can reset
    let current = [...destinations];

    const grid = document.querySelector('#card-grid');

    // ── renderCards() — the core pattern ──────────────────────
    function renderCards(items) {
      let html = '';

      // for...of loop: do something for each item in the array
      for (const item of items) {
        const index = items.indexOf(item) + 1;
        html += `
          <div class="card">
            <p class="card-number">Destination ${index}</p>
            <h3 class="card-title">${item}</h3>
            <p class="card-sub">Explore the city</p>
          </div>
        `;
      }

      grid.innerHTML = html;
      document.querySelector('#card-count').textContent = items.length + ' cities';
    }

    // ── Shuffle helper (Fisher-Yates) ─────────────────────────
    function shuffle(arr) {
      const copy = [...arr];
      for (let i = copy.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const temp = copy[i];
        copy[i] = copy[j];
        copy[j] = temp;
      }
      return copy;
    }

    // ── Button events ─────────────────────────────────────────
    document.querySelector('#shuffle-btn').addEventListener('click', function() {
      current = shuffle(current);
      renderCards(current);
    });

    document.querySelector('#reverse-btn').addEventListener('click', function() {
      current = [...current].reverse();
      renderCards(current);
    });

    document.querySelector('#reset-btn').addEventListener('click', function() {
      current = [...destinations];
      renderCards(current);
    });

    // Initial render on page load
    renderCards(current);
  </script>

</body>
</html>
```

---

## CodePen 3 — Greeting Card Generator

**Placement:** After the "Arrow Functions" section.
**Demonstrates:** Arrow functions, function with multiple parameters, combining select dropdowns + a render function to generate a styled card. Shows functions as composable units producing visual output.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Greeting Card Generator</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 2rem;
      padding: 2rem;
      align-items: start;
    }

    /* ── Controls ─────────────────────────────────────────── */
    .controls { display: flex; flex-direction: column; gap: 1rem; }

    .controls h2 { font-size: 1rem; color: #a29bfe; margin-bottom: 0.25rem; }

    .field { display: flex; flex-direction: column; gap: 0.35rem; }

    label {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      opacity: 0.55;
    }

    select, input[type="text"] {
      padding: 0.55rem 0.75rem;
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 8px;
      color: #eee;
      font-size: 0.9rem;
      font-family: inherit;
      outline: none;
    }

    select:focus, input:focus { border-color: #6c5ce7; }

    /* ── Card preview ─────────────────────────────────────── */
    .preview { display: flex; flex-direction: column; gap: 0.5rem; }

    .preview h2 {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      opacity: 0.35;
      margin-bottom: 0.25rem;
    }

    .greeting-card {
      border-radius: 20px;
      padding: 3rem 2.5rem;
      text-align: center;
      min-height: 240px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
      transition: all 0.4s ease;
    }

    .greeting-card .emoji  { font-size: 3rem; line-height: 1; }
    .greeting-card .to     { font-size: 0.85rem; opacity: 0.75; }
    .greeting-card .title  { font-size: 1.6rem; font-weight: 800; line-height: 1.2; }
    .greeting-card .msg    { font-size: 0.9rem; opacity: 0.8; line-height: 1.6; max-width: 300px; }
    .greeting-card .sig    { font-size: 0.8rem; opacity: 0.6; margin-top: 0.5rem; font-style: italic; }

    /* Theme: birthday */
    .theme-birthday {
      background: linear-gradient(135deg, #fdcb6e, #e17055);
      color: #2d1b00;
    }

    /* Theme: congrats */
    .theme-congrats {
      background: linear-gradient(135deg, #55efc4, #0984e3);
      color: #001a2e;
    }

    /* Theme: thanks */
    .theme-thanks {
      background: linear-gradient(135deg, #a29bfe, #6c5ce7);
      color: #fff;
    }

    /* Theme: holiday */
    .theme-holiday {
      background: linear-gradient(135deg, #d63031, #00b894);
      color: #fff;
    }
  </style>
</head>
<body>

  <div class="controls">
    <h2>Card Builder</h2>

    <div class="field">
      <label>Occasion</label>
      <select id="occasion">
        <option value="birthday">Birthday</option>
        <option value="congrats">Congratulations</option>
        <option value="thanks">Thank You</option>
        <option value="holiday">Holiday</option>
      </select>
    </div>

    <div class="field">
      <label>Recipient Name</label>
      <input type="text" id="recipient" value="Ada" placeholder="Enter a name…">
    </div>

    <div class="field">
      <label>Tone</label>
      <select id="tone">
        <option value="warm">Warm</option>
        <option value="funny">Funny</option>
        <option value="formal">Formal</option>
      </select>
    </div>

    <div class="field">
      <label>From</label>
      <input type="text" id="sender" value="The Team" placeholder="Your name…">
    </div>
  </div>

  <div class="preview">
    <h2>Preview</h2>
    <div id="card-preview"></div>
  </div>

  <script>
    // ── Data: each occasion has content for each tone ─────────
    const content = {
      birthday: {
        emoji: '🎂',
        title: 'Happy Birthday!',
        warm:   'Wishing you a day full of joy, laughter, and everything you love.',
        funny:  'Another year older, but still younger than you'll be tomorrow!',
        formal: 'Please accept our warmest congratulations on this auspicious occasion.'
      },
      congrats: {
        emoji: '🏆',
        title: 'Congratulations!',
        warm:   'You worked so hard for this — every bit of it was deserved.',
        funny:  'You did it! Time to update that resume with "achieved greatness."',
        formal: 'We extend our sincere congratulations on this significant achievement.'
      },
      thanks: {
        emoji: '💜',
        title: 'Thank You',
        warm:   'Your kindness made a real difference. We are so grateful for you.',
        funny:  'We would thank you in person, but you've already done too much!',
        formal: 'We wish to express our sincere gratitude for your generous contribution.'
      },
      holiday: {
        emoji: '🌟',
        title: 'Happy Holidays!',
        warm:   'Warmest wishes for a joyful season and a wonderful new year.',
        funny:  'May your holidays be merry, bright, and involve a lot of snacks.',
        formal: 'We wish you a prosperous holiday season and a happy new year.'
      }
    };

    // ── buildCard — arrow function with multiple parameters ────
    const buildCard = (occasion, recipient, tone, sender) => {
      const c = content[occasion];
      return `
        <div class="greeting-card theme-${occasion}">
          <span class="emoji">${c.emoji}</span>
          <p class="to">To: <strong>${recipient}</strong></p>
          <h2 class="title">${c.title}</h2>
          <p class="msg">${c[tone]}</p>
          <p class="sig">— ${sender}</p>
        </div>
      `;
    };

    // ── renderCard — reads all inputs and calls buildCard ──────
    function renderCard() {
      const occasion  = document.querySelector('#occasion').value;
      const recipient = document.querySelector('#recipient').value || 'Friend';
      const tone      = document.querySelector('#tone').value;
      const sender    = document.querySelector('#sender').value || 'Someone who cares';

      document.querySelector('#card-preview').innerHTML = buildCard(occasion, recipient, tone, sender);
    }

    // Re-render whenever anything changes
    document.querySelector('#occasion').addEventListener('change', renderCard);
    document.querySelector('#recipient').addEventListener('input',  renderCard);
    document.querySelector('#tone').addEventListener('change',      renderCard);
    document.querySelector('#sender').addEventListener('input',     renderCard);

    // Initial render
    renderCard();
  </script>

</body>
</html>
```

---

## CodePen 4 — Dynamic List Builder

**Placement:** After the "Putting It Together" section.
**Demonstrates:** Adding items to an array, calling a render function to update the display, the pattern of "change the data → re-render." Text input + Add button builds a list of styled cards.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dynamic List Builder</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      padding: 2rem;
      max-width: 600px;
      margin: 0 auto;
    }

    h1 { font-size: 1.2rem; color: #a29bfe; margin-bottom: 0.25rem; }
    .subtitle { font-size: 0.82rem; opacity: 0.5; margin-bottom: 1.5rem; }

    .input-row {
      display: flex;
      gap: 0.6rem;
      margin-bottom: 1.5rem;
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

    input:focus { border-color: #6c5ce7; }
    input::placeholder { opacity: 0.4; }

    .add-btn {
      padding: 0.6rem 1.25rem;
      background: #6c5ce7;
      color: #fff;
      border: none;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
    }

    /* ── Skill cards ───────────────────────────────────────── */
    .skill-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-bottom: 1rem;
    }

    .skill-card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 100px;
      padding: 0.45rem 1rem;
      font-size: 0.85rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      animation: pop 0.2s ease;
    }

    @keyframes pop {
      from { opacity: 0; transform: scale(0.8); }
      to   { opacity: 1; transform: scale(1); }
    }

    .skill-card .remove {
      background: none;
      border: none;
      color: #636e72;
      cursor: pointer;
      font-size: 0.85rem;
      padding: 0;
      line-height: 1;
      transition: color 0.15s;
    }

    .skill-card .remove:hover { color: #d63031; }

    .empty-state {
      text-align: center;
      opacity: 0.3;
      font-size: 0.88rem;
      padding: 2rem;
    }

    .meta {
      font-size: 0.78rem;
      color: #636e72;
    }

    /* ── Code panel ────────────────────────────────────────── */
    .code-panel {
      background: #0d1117;
      border-radius: 10px;
      padding: 0.85rem 1.1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      color: #636e72;
      margin-top: 1.5rem;
      line-height: 1.8;
    }

    .code-panel .hl  { color: #55efc4; }
    .code-panel .arr { color: #fdcb6e; }
  </style>
</head>
<body>

  <h1>Skill Tracker</h1>
  <p class="subtitle">Add skills to the array — the render function rebuilds the list each time.</p>

  <div class="input-row">
    <input type="text" id="skill-input" placeholder="Add a skill (e.g. CSS Grid, Figma…)" maxlength="40">
    <button class="add-btn" id="add-btn">+ Add</button>
  </div>

  <div class="skill-grid" id="skill-grid">
    <p class="empty-state" id="empty">No skills yet — add one above.</p>
  </div>

  <p class="meta" id="meta"></p>

  <div class="code-panel">
    skills = [<span class="hl" id="array-display"></span>]<br>
    <span class="arr">renderSkills</span>(skills)  &larr;  called every time the array changes
  </div>

  <script>
    // ── The data array — renderSkills() reads this ────────────
    let skills = ['HTML', 'CSS', 'JavaScript'];

    const grid = document.querySelector('#skill-grid');

    // ── renderSkills — called every time skills changes ───────
    function renderSkills(items) {
      if (items.length === 0) {
        grid.innerHTML = '<p class="empty-state" id="empty">No skills yet — add one above.</p>';
        document.querySelector('#meta').textContent = '';
        document.querySelector('#array-display').textContent = '';
        return;
      }

      grid.innerHTML = items.map(function(skill, index) {
        return `
          <div class="skill-card">
            <span>${skill}</span>
            <button class="remove" onclick="removeSkill(${index})" title="Remove">&times;</button>
          </div>
        `;
      }).join('');

      document.querySelector('#meta').textContent = items.length + ' skills tracked';
      document.querySelector('#array-display').textContent =
        items.map(s => '"' + s + '"').join(', ');
    }

    // ── addSkill — pushes to array, re-renders ────────────────
    function addSkill() {
      const input = document.querySelector('#skill-input');
      const text  = input.value.trim();

      if (!text) return;
      if (skills.includes(text)) {
        input.value = '';
        return;
      }

      skills.push(text);
      renderSkills(skills);
      input.value = '';
      input.focus();
    }

    // ── removeSkill — splices from array, re-renders ──────────
    function removeSkill(index) {
      skills.splice(index, 1);
      renderSkills(skills);
    }

    document.querySelector('#add-btn').addEventListener('click', addSkill);
    document.querySelector('#skill-input').addEventListener('keydown', function(event) {
      if (event.key === 'Enter') addSkill();
    });

    // Initial render
    renderSkills(skills);
  </script>

</body>
</html>
```

---

## CodePen 5 — Reusable Render Function

**Placement:** After the "renderCards() Pattern" section.
**Demonstrates:** The same `renderCards()` function called in multiple contexts — on load, on filter, on sort. Shows why functions beat copy-pasted code. Uses `map().join('')` pattern.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reusable Render Function</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      padding: 2rem;
      max-width: 760px;
      margin: 0 auto;
    }

    h1 { font-size: 1.2rem; color: #a29bfe; margin-bottom: 0.25rem; }
    .subtitle { font-size: 0.82rem; opacity: 0.5; margin-bottom: 1.5rem; }

    /* ── Filter bar ───────────────────────────────────────── */
    .filter-bar {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-bottom: 1.5rem;
    }

    .filter-btn {
      padding: 0.4rem 1rem;
      background: transparent;
      border: 2px solid #2d3561;
      border-radius: 100px;
      color: #aaa;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: border-color 0.2s, color 0.2s, background 0.2s;
    }

    .filter-btn.active {
      background: #6c5ce7;
      border-color: #6c5ce7;
      color: #fff;
    }

    /* ── Card grid ────────────────────────────────────────── */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 1rem;
      margin-bottom: 1rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 12px;
      padding: 1.25rem;
      transition: transform 0.2s, border-color 0.2s;
    }

    .card:hover {
      transform: translateY(-3px);
      border-color: #6c5ce7;
    }

    .card-emoji { font-size: 1.5rem; margin-bottom: 0.5rem; }

    .card-title {
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
    }

    .card-category {
      display: inline-block;
      background: rgba(108,92,231,0.15);
      color: #a29bfe;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      padding: 0.15rem 0.55rem;
      border-radius: 100px;
    }

    .count-bar {
      font-size: 0.78rem;
      color: #636e72;
      margin-bottom: 1rem;
    }
  </style>
</head>
<body>

  <h1>Project Gallery</h1>
  <p class="subtitle">The same <code>renderCards()</code> function is called by load, filter, and sort.</p>

  <div class="filter-bar">
    <button class="filter-btn active" data-filter="all">All</button>
    <button class="filter-btn" data-filter="design">Design</button>
    <button class="filter-btn" data-filter="code">Code</button>
    <button class="filter-btn" data-filter="ux">UX</button>
  </div>

  <p class="count-bar" id="count-bar"></p>
  <div class="card-grid" id="card-grid"></div>

  <script>
    // ── Data ──────────────────────────────────────────────────
    const projects = [
      { emoji: '🎨', title: 'Brand Identity',  category: 'design' },
      { emoji: '💻', title: 'Portfolio Site',   category: 'code'   },
      { emoji: '🗂️', title: 'UX Case Study',    category: 'ux'     },
      { emoji: '🖌️', title: 'Icon System',      category: 'design' },
      { emoji: '⚡', title: 'React Dashboard',  category: 'code'   },
      { emoji: '📊', title: 'Data Viz Report',  category: 'ux'     },
      { emoji: '🌐', title: 'Landing Page',     category: 'code'   },
      { emoji: '✏️', title: 'Typography Guide', category: 'design' }
    ];

    // ── renderCards — one function, called everywhere ─────────
    function renderCards(items) {
      const grid = document.querySelector('#card-grid');

      grid.innerHTML = items.map(function(project) {
        return `
          <div class="card">
            <p class="card-emoji">${project.emoji}</p>
            <h3 class="card-title">${project.title}</h3>
            <span class="card-category">${project.category}</span>
          </div>
        `;
      }).join('');

      document.querySelector('#count-bar').textContent =
        'Showing ' + items.length + ' of ' + projects.length + ' projects';
    }

    // ── Filter buttons ────────────────────────────────────────
    const filterBtns = document.querySelectorAll('.filter-btn');

    filterBtns.forEach(function(btn) {
      btn.addEventListener('click', function() {
        // Update active button
        filterBtns.forEach(function(b) { b.classList.remove('active'); });
        btn.classList.add('active');

        // Filter and re-render — same renderCards() function
        const filter = btn.dataset.filter;
        if (filter === 'all') {
          renderCards(projects);
        } else {
          const filtered = projects.filter(function(p) {
            return p.category === filter;
          });
          renderCards(filtered);
        }
      });
    });

    // Initial render on page load — same renderCards() function
    renderCards(projects);
  </script>

</body>
</html>
```
