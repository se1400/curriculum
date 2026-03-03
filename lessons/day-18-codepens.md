# Day 18 CodePens — JavaScript Foundations: Data Types and Variables

---

## CODEPEN 1 — typeof and Data Types Explorer

**Placement:** After the `typeof` operator section (after LISTING 18.15)

**Purpose:** Students interact with `typeof` on all primitive types including BigInt and Symbol. A live input lets them type any value and see its type.

---

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>typeof Explorer</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>typeof Explorer</h1>
    <p class="subtitle">Explore JavaScript's type system — including BigInt and Symbol</p>

    <section class="card">
      <h2>Built-in Type Examples</h2>
      <table class="type-table">
        <thead>
          <tr>
            <th>Value</th>
            <th>typeof result</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody id="type-table-body"></tbody>
      </table>
    </section>

    <section class="card">
      <h2>Live typeof Tester</h2>
      <p>Type a value below and see what <code>typeof</code> returns.</p>
      <div class="input-row">
        <input type="text" id="value-input" placeholder='Try: 42, "hello", true, null, undefined ...' autocomplete="off">
        <button id="check-btn">Check Type</button>
      </div>
      <div id="result-display" class="result-display hidden">
        <div class="result-inner">
          <span class="result-label">typeof</span>
          <span id="result-value" class="result-code"></span>
          <span class="result-arrow">→</span>
          <span id="result-type" class="result-type"></span>
        </div>
        <p id="result-note" class="result-note"></p>
      </div>
    </section>

    <section class="card">
      <h2>Important Quirks</h2>
      <ul class="quirk-list">
        <li><code>typeof null</code> returns <strong>"object"</strong> — a historical bug. Use <code>=== null</code> to check for null.</li>
        <li><code>typeof []</code> returns <strong>"object"</strong> — arrays are objects. Use <code>Array.isArray()</code> to check for arrays.</li>
        <li><code>typeof NaN</code> returns <strong>"number"</strong> — NaN is technically a numeric value.</li>
        <li><code>typeof function(){}</code> returns <strong>"function"</strong> — functions get their own typeof result.</li>
      </ul>
    </section>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

---

### CSS

```css
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #0f172a;
  color: #e2e8f0;
  min-height: 100vh;
  padding: 2rem 1rem;
}

.container {
  max-width: 760px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

h1 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #f8fafc;
}

.subtitle {
  color: #94a3b8;
  margin-top: 0.25rem;
  font-size: 0.95rem;
}

h2 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #cbd5e1;
  margin-bottom: 1rem;
}

.card {
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 12px;
  padding: 1.5rem;
}

/* Type Table */
.type-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.type-table th {
  text-align: left;
  padding: 0.5rem 0.75rem;
  color: #64748b;
  font-weight: 600;
  border-bottom: 1px solid #334155;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.type-table td {
  padding: 0.55rem 0.75rem;
  border-bottom: 1px solid #1e293b;
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 0.875rem;
}

.type-table tr:last-child td {
  border-bottom: none;
}

.type-table tr:hover td {
  background: #263347;
}

.value-col {
  color: #fbbf24;
}

.type-col {
  font-weight: 700;
}

.type-string   { color: #34d399; }
.type-number   { color: #60a5fa; }
.type-boolean  { color: #f472b6; }
.type-undefined { color: #94a3b8; }
.type-object   { color: #fb923c; }
.type-function { color: #a78bfa; }
.type-symbol   { color: #f9a8d4; }
.type-bigint   { color: #86efac; }

.note-col {
  color: #64748b;
  font-family: system-ui, sans-serif;
  font-size: 0.8rem;
}

/* Live tester */
.input-row {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

input[type="text"] {
  flex: 1;
  background: #0f172a;
  border: 1px solid #475569;
  border-radius: 8px;
  padding: 0.6rem 0.9rem;
  color: #e2e8f0;
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 0.9rem;
  outline: none;
  transition: border-color 0.15s;
}

input[type="text"]:focus {
  border-color: #60a5fa;
}

button {
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 0.6rem 1.25rem;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
  white-space: nowrap;
}

button:hover {
  background: #1d4ed8;
}

.result-display {
  background: #0f172a;
  border: 1px solid #334155;
  border-radius: 8px;
  padding: 1rem 1.25rem;
}

.result-display.hidden {
  display: none;
}

.result-inner {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 1rem;
}

.result-label {
  color: #64748b;
}

.result-code {
  color: #fbbf24;
  font-weight: 600;
}

.result-arrow {
  color: #475569;
}

.result-type {
  font-weight: 700;
  font-size: 1.1rem;
}

.result-note {
  margin-top: 0.6rem;
  font-size: 0.85rem;
  color: #64748b;
  font-family: system-ui, sans-serif;
}

/* Quirk list */
.quirk-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.quirk-list li {
  padding-left: 1.25rem;
  position: relative;
  color: #94a3b8;
  font-size: 0.9rem;
  line-height: 1.5;
}

.quirk-list li::before {
  content: '⚠';
  position: absolute;
  left: 0;
  color: #fbbf24;
  font-size: 0.8rem;
}

code {
  background: #0f172a;
  padding: 0.1em 0.4em;
  border-radius: 4px;
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 0.875em;
  color: #f8fafc;
}
```

---

### JS

```js
// Data for the type table
const typeExamples = [
  { value: '"hello"',       result: 'string',    note: 'Any text in quotes' },
  { value: '42',            result: 'number',    note: 'Integers and decimals share this type' },
  { value: '3.14',          result: 'number',    note: 'Same type as integers' },
  { value: 'true',          result: 'boolean',   note: 'true or false' },
  { value: 'false',         result: 'boolean',   note: 'true or false' },
  { value: 'undefined',     result: 'undefined', note: 'Unassigned variable' },
  { value: 'null',          result: 'object',    note: '⚠ Historical bug — null is NOT an object' },
  { value: '{}',            result: 'object',    note: 'Plain objects' },
  { value: '[]',            result: 'object',    note: '⚠ Arrays are objects — use Array.isArray()' },
  { value: 'function(){}',  result: 'function',  note: 'Functions get their own result' },
  { value: 'Symbol("x")',   result: 'symbol',    note: 'Unique identifiers (ES2015)' },
  { value: '42n',           result: 'bigint',    note: 'Integers beyond MAX_SAFE_INTEGER (ES2020)' },
  { value: 'NaN',           result: 'number',    note: '⚠ NaN is technically numeric type' },
  { value: 'Infinity',      result: 'number',    note: 'Also a number' },
];

const colorMap = {
  string:    'type-string',
  number:    'type-number',
  boolean:   'type-boolean',
  undefined: 'type-undefined',
  object:    'type-object',
  function:  'type-function',
  symbol:    'type-symbol',
  bigint:    'type-bigint',
};

// Render the table
const tbody = document.getElementById('type-table-body');

typeExamples.forEach(({ value, result, note }) => {
  const tr = document.createElement('tr');
  tr.innerHTML = `
    <td class="value-col">${value}</td>
    <td class="type-col ${colorMap[result] || ''}">"${result}"</td>
    <td class="note-col">${note}</td>
  `;
  tbody.appendChild(tr);
});

// Notes for the live tester
const typeNotes = {
  string:    'Strings represent text. Single quotes, double quotes, and backticks all produce strings.',
  number:    'JavaScript has one number type for both integers and decimals (64-bit float).',
  boolean:   'Booleans are true or false. They are the result of comparisons.',
  undefined: 'undefined means no value has been assigned.',
  object:    'Could be an object, array, or null. Use === null or Array.isArray() to distinguish.',
  function:  'Functions are callable objects — they get their own typeof result.',
  symbol:    'Symbols are unique, guaranteed-distinct values (ES2015+).',
  bigint:    'BigInt handles integers larger than Number.MAX_SAFE_INTEGER (ES2020+).',
};

// Live tester
const input   = document.getElementById('value-input');
const btn     = document.getElementById('check-btn');
const display = document.getElementById('result-display');
const resultValue = document.getElementById('result-value');
const resultType  = document.getElementById('result-type');
const resultNote  = document.getElementById('result-note');

function checkType() {
  const raw = input.value.trim();
  if (!raw) return;

  let evaluated;
  let typeResult;

  try {
    // Use Function constructor to safely evaluate the expression
    evaluated = Function('"use strict"; return (' + raw + ')')();
    typeResult = typeof evaluated;
  } catch (e) {
    display.classList.remove('hidden');
    resultValue.textContent = raw;
    resultType.textContent = 'SyntaxError';
    resultType.className = 'result-type type-undefined';
    resultNote.textContent = 'Could not evaluate that expression. Try: 42, "hello", true, null, undefined, [], {}, 42n';
    return;
  }

  display.classList.remove('hidden');
  resultValue.textContent = raw;
  resultType.textContent = `"${typeResult}"`;
  resultType.className = `result-type ${colorMap[typeResult] || ''}`;
  resultNote.textContent = typeNotes[typeResult] || '';
}

btn.addEventListener('click', checkType);
input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') checkType();
});
```

---

## CODEPEN 2 — Template Literals vs String Concatenation

**Placement:** After the Strings in Depth section / template literals subsection (after LISTING 18.19)

**Purpose:** Side-by-side comparison of old concatenation vs. modern template literals. Shows multi-line strings, expression evaluation, and a practical greeting builder.

---

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Template Literals vs Concatenation</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>Template Literals vs. Concatenation</h1>
    <p class="subtitle">Two ways to build strings — one modern, one legacy</p>

    <section class="card">
      <h2>Greeting Builder</h2>
      <p>Fill in the fields and watch both methods produce the same output — but notice which code is easier to read.</p>
      <div class="form-grid">
        <label for="first-name">First Name</label>
        <input type="text" id="first-name" value="Jordan" maxlength="30">

        <label for="last-name">Last Name</label>
        <input type="text" id="last-name" value="Rivera" maxlength="30">

        <label for="score">Score</label>
        <input type="number" id="score" value="1450" min="0" max="99999">

        <label for="rank">Rank</label>
        <input type="number" id="rank" value="3" min="1" max="9999">
      </div>
    </section>

    <div class="comparison">
      <div class="panel">
        <div class="panel-header old-header">
          <span class="badge badge-old">Legacy</span>
          String Concatenation with <code>+</code>
        </div>
        <div class="panel-code">
          <pre id="concat-code"></pre>
        </div>
        <div class="panel-output">
          <div class="output-label">Output</div>
          <div id="concat-output" class="output-text"></div>
        </div>
      </div>

      <div class="panel">
        <div class="panel-header new-header">
          <span class="badge badge-new">Modern</span>
          Template Literal with <code>`${ }`</code>
        </div>
        <div class="panel-code">
          <pre id="template-code"></pre>
        </div>
        <div class="panel-output">
          <div class="output-label">Output</div>
          <div id="template-output" class="output-text"></div>
        </div>
      </div>
    </div>

    <section class="card">
      <h2>Multi-line Strings</h2>
      <div class="comparison-small">
        <div class="sub-panel">
          <div class="sub-header old-header">Legacy — Concatenation</div>
          <pre class="code-block"><code>"Dear " + name + ",\n" +
"Thank you for your order.\n" +
"Total: $" + total.toFixed(2)</code></pre>
        </div>
        <div class="sub-panel">
          <div class="sub-header new-header">Modern — Template Literal</div>
          <pre class="code-block"><code id="multiline-demo"></code></pre>
        </div>
      </div>
      <div class="multiline-output">
        <div class="output-label">Rendered Output</div>
        <div id="multiline-result" class="output-text"></div>
      </div>
    </section>

    <section class="card expressions-card">
      <h2>Expressions Inside <code>${ }</code></h2>
      <p>Any valid JavaScript expression works inside template literal placeholders.</p>
      <div id="expression-examples"></div>
    </section>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

---

### CSS

```css
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #0f172a;
  color: #e2e8f0;
  min-height: 100vh;
  padding: 2rem 1rem;
}

.container {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

h1 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #f8fafc;
}

.subtitle {
  color: #94a3b8;
  margin-top: 0.25rem;
  font-size: 0.95rem;
}

h2 {
  font-size: 1.05rem;
  font-weight: 600;
  color: #cbd5e1;
  margin-bottom: 1rem;
}

.card {
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 12px;
  padding: 1.5rem;
}

/* Form */
.form-grid {
  display: grid;
  grid-template-columns: auto 1fr auto 1fr;
  gap: 0.6rem 1rem;
  align-items: center;
}

label {
  color: #94a3b8;
  font-size: 0.875rem;
  font-weight: 500;
  white-space: nowrap;
}

input[type="text"],
input[type="number"] {
  background: #0f172a;
  border: 1px solid #475569;
  border-radius: 6px;
  padding: 0.45rem 0.75rem;
  color: #e2e8f0;
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 0.875rem;
  outline: none;
  width: 100%;
  transition: border-color 0.15s;
}

input:focus {
  border-color: #60a5fa;
}

/* Comparison panels */
.comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

@media (max-width: 600px) {
  .comparison { grid-template-columns: 1fr; }
  .form-grid  { grid-template-columns: auto 1fr; }
}

.panel {
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 12px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.panel-header {
  padding: 0.75rem 1rem;
  font-size: 0.85rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.old-header { background: #2d1f0e; color: #fb923c; border-bottom: 1px solid #7c3d14; }
.new-header { background: #0d2537; color: #34d399; border-bottom: 1px solid #0e4f3a; }

.badge {
  display: inline-block;
  padding: 0.15em 0.5em;
  border-radius: 999px;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.badge-old { background: #7c3d14; color: #fed7aa; }
.badge-new { background: #064e3b; color: #a7f3d0; }

.panel-code {
  padding: 1rem;
  flex: 1;
}

.panel-code pre {
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 0.78rem;
  color: #94a3b8;
  white-space: pre-wrap;
  word-break: break-word;
  line-height: 1.6;
}

.panel-output {
  border-top: 1px solid #334155;
  padding: 0.75rem 1rem;
}

.output-label {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #475569;
  margin-bottom: 0.4rem;
}

.output-text {
  font-size: 0.9rem;
  color: #f8fafc;
  line-height: 1.6;
  white-space: pre-line;
}

/* Multi-line section */
.comparison-small {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 1rem;
}

.sub-panel {
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #334155;
}

.sub-header {
  padding: 0.5rem 0.75rem;
  font-size: 0.8rem;
  font-weight: 600;
}

.code-block {
  padding: 0.75rem;
  background: #0f172a;
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 0.8rem;
  color: #94a3b8;
  line-height: 1.6;
  white-space: pre-wrap;
}

.multiline-output {
  background: #0f172a;
  border: 1px solid #334155;
  border-radius: 8px;
  padding: 0.75rem 1rem;
  margin-top: 0.5rem;
}

/* Expression examples */
.expression-examples {
  margin-top: 0.5rem;
}

.expr-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem 1.5rem;
  padding: 0.5rem 0;
  border-bottom: 1px solid #334155;
  align-items: baseline;
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 0.85rem;
}

.expr-row:last-child { border-bottom: none; }

.expr-code  { color: #94a3b8; }
.expr-result { color: #fbbf24; font-weight: 600; }

code {
  background: #0f172a;
  padding: 0.1em 0.35em;
  border-radius: 4px;
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 0.85em;
}
```

---

### JS

```js
const firstInput = document.getElementById('first-name');
const lastInput  = document.getElementById('last-name');
const scoreInput = document.getElementById('score');
const rankInput  = document.getElementById('rank');

const concatCode    = document.getElementById('concat-code');
const templateCode  = document.getElementById('template-code');
const concatOutput  = document.getElementById('concat-output');
const templateOutput = document.getElementById('template-output');

function update() {
  const first = firstInput.value  || 'Jordan';
  const last  = lastInput.value   || 'Rivera';
  const score = Number(scoreInput.value) || 0;
  const rank  = Number(rankInput.value)  || 1;
  const full  = first + ' ' + last;

  // Legacy code display
  concatCode.textContent =
    `var fullName = firstName + " " + lastName;\n` +
    `var msg = "Hello, " + fullName + "!\\n" +\n` +
    `          "Score: " + score + " pts\\n" +\n` +
    `          "Global Rank: #" + rank;`;

  // Modern code display
  templateCode.textContent =
    `const fullName = \`\${firstName} \${lastName}\`;\n` +
    `const msg = \`Hello, \${fullName}!\\n\` +\n` +
    `            \`Score: \${score} pts\\n\` +\n` +
    `            \`Global Rank: #\${rank}\`;`;

  const output =
    `Hello, ${full}!\nScore: ${score} pts\nGlobal Rank: #${rank}`;

  concatOutput.textContent  = output;
  templateOutput.textContent = output;
}

// Multi-line demo
const name  = 'Jordan';
const total = 89.97;
const multilineDemo = document.getElementById('multiline-demo');
const multilineResult = document.getElementById('multiline-result');

multilineDemo.textContent =
  '`Dear ${name},\n' +
  'Thank you for your order.\n' +
  'Total: $${total.toFixed(2)}`';

multilineResult.textContent =
  `Dear ${name},\nThank you for your order.\nTotal: $${total.toFixed(2)}`;

// Expression examples
const exprContainer = document.getElementById('expression-examples');

const expressions = [
  { code: '`${2 + 2}`',                        result: `${2 + 2}` },
  { code: '`${"hello".toUpperCase()}`',         result: `${'hello'.toUpperCase()}` },
  { code: '`${true ? "yes" : "no"}`',           result: `${true ? 'yes' : 'no'}` },
  { code: '`${(29.99 * 3).toFixed(2)}`',        result: `${(29.99 * 3).toFixed(2)}` },
  { code: '`${new Date().getFullYear()}`',       result: `${new Date().getFullYear()}` },
  { code: '`${[1,2,3].join(" + ")}`',           result: `${[1,2,3].join(' + ')}` },
];

expressions.forEach(({ code, result }) => {
  const row = document.createElement('div');
  row.className = 'expr-row';
  row.innerHTML = `<span class="expr-code">${code}</span><span class="expr-result">"${result}"</span>`;
  exprContainer.appendChild(row);
});

// Bind live updates
[firstInput, lastInput, scoreInput, rankInput].forEach(el => {
  el.addEventListener('input', update);
});

update();
```

---

## CODEPEN 3 — The Math Object Playground

**Placement:** After the Math Object section (after LISTING 18.26)

**Purpose:** Interactive demo of Math methods. Buttons for random number generation, a slider for rounding demos, and a display of Math constants.

---

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Math Object Playground</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>Math Object Playground</h1>
    <p class="subtitle">Explore JavaScript's built-in <code>Math</code> object interactively</p>

    <div class="grid-two">

      <!-- Random Number Section -->
      <section class="card">
        <h2>Math.random()</h2>
        <p class="card-desc">Returns a float in <strong>[0, 1)</strong> — 0 is possible, 1 is never returned.</p>
        <div class="rand-display">
          <div class="rand-value" id="rand-value">—</div>
          <div class="rand-label">Math.random()</div>
        </div>
        <button class="btn" id="btn-random">Generate Random Float</button>

        <div class="divider"></div>

        <p class="card-desc">Random integer in a range using <code>Math.floor(Math.random() * (max - min + 1)) + min</code>:</p>
        <div class="range-controls">
          <label>Min <input type="number" id="rand-min" value="1" min="-100" max="100"></label>
          <span class="range-sep">to</span>
          <label>Max <input type="number" id="rand-max" value="6" min="-100" max="100"></label>
        </div>
        <div class="rand-display">
          <div class="rand-value rand-int" id="rand-int-value">—</div>
          <div class="rand-label">Random Integer</div>
        </div>
        <button class="btn btn-secondary" id="btn-random-int">Generate Random Integer</button>
      </section>

      <!-- Rounding Section -->
      <section class="card">
        <h2>Rounding Methods</h2>
        <p class="card-desc">Drag the slider to explore how each rounding method handles the value.</p>
        <div class="slider-area">
          <input type="range" id="round-slider" min="-3" max="3" step="0.1" value="1.7">
          <div class="slider-value" id="slider-display">1.7</div>
        </div>
        <div class="rounding-results" id="rounding-results"></div>
      </section>
    </div>

    <!-- More Math Methods -->
    <section class="card">
      <h2>More Math Methods</h2>
      <div class="methods-grid" id="methods-grid"></div>
    </section>

    <!-- Constants -->
    <section class="card constants-card">
      <h2>Math Constants</h2>
      <div class="constants-grid" id="constants-grid"></div>
    </section>

  </div>
  <script src="script.js"></script>
</body>
</html>
```

---

### CSS

```css
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #0f172a;
  color: #e2e8f0;
  min-height: 100vh;
  padding: 2rem 1rem;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

h1 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #f8fafc;
}

.subtitle {
  color: #94a3b8;
  margin-top: 0.25rem;
  font-size: 0.95rem;
}

h2 {
  font-size: 1.05rem;
  font-weight: 600;
  color: #cbd5e1;
  margin-bottom: 0.75rem;
}

.card {
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 12px;
  padding: 1.5rem;
}

.card-desc {
  font-size: 0.875rem;
  color: #94a3b8;
  line-height: 1.5;
  margin-bottom: 1rem;
}

.grid-two {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

@media (max-width: 580px) {
  .grid-two { grid-template-columns: 1fr; }
}

/* Random display */
.rand-display {
  text-align: center;
  background: #0f172a;
  border-radius: 10px;
  padding: 1.2rem;
  margin-bottom: 0.75rem;
}

.rand-value {
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 1.6rem;
  font-weight: 700;
  color: #60a5fa;
  letter-spacing: -0.02em;
}

.rand-int {
  color: #34d399;
  font-size: 2rem;
}

.rand-label {
  font-size: 0.75rem;
  color: #475569;
  margin-top: 0.25rem;
  font-family: 'Fira Code', 'Courier New', monospace;
}

.btn {
  width: 100%;
  padding: 0.65rem 1rem;
  border: none;
  border-radius: 8px;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: background 0.15s;
}

.btn:hover { background: #1d4ed8; }

.btn-secondary {
  background: #059669;
}

.btn-secondary:hover { background: #047857; }

.divider {
  border-top: 1px solid #334155;
  margin: 1.25rem 0;
}

.range-controls {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  flex-wrap: wrap;
}

.range-controls label {
  font-size: 0.8rem;
  color: #94a3b8;
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

.range-controls input[type="number"] {
  width: 65px;
  background: #0f172a;
  border: 1px solid #475569;
  border-radius: 6px;
  padding: 0.3rem 0.5rem;
  color: #e2e8f0;
  font-family: 'Fira Code', monospace;
  font-size: 0.875rem;
  text-align: center;
}

.range-sep {
  color: #475569;
  font-size: 0.8rem;
}

/* Slider */
.slider-area {
  margin-bottom: 1rem;
}

input[type="range"] {
  width: 100%;
  accent-color: #8b5cf6;
  cursor: pointer;
}

.slider-value {
  text-align: center;
  font-family: 'Fira Code', monospace;
  font-size: 1.5rem;
  font-weight: 700;
  color: #a78bfa;
  margin-top: 0.5rem;
}

/* Rounding results */
.rounding-results {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.round-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #0f172a;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  font-family: 'Fira Code', monospace;
  font-size: 0.875rem;
}

.round-method { color: #94a3b8; }
.round-result { color: #fbbf24; font-weight: 700; }

/* Methods grid */
.methods-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 0.6rem;
}

.method-card {
  background: #0f172a;
  border-radius: 8px;
  padding: 0.75rem;
}

.method-call {
  font-family: 'Fira Code', monospace;
  font-size: 0.8rem;
  color: #94a3b8;
  margin-bottom: 0.3rem;
}

.method-result {
  font-family: 'Fira Code', monospace;
  font-size: 1rem;
  font-weight: 700;
  color: #f8fafc;
}

/* Constants */
.constants-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 0.6rem;
}

.const-card {
  background: #0f172a;
  border-radius: 8px;
  padding: 0.75rem;
}

.const-name {
  font-family: 'Fira Code', monospace;
  font-size: 0.8rem;
  color: #f472b6;
  margin-bottom: 0.25rem;
}

.const-value {
  font-family: 'Fira Code', monospace;
  font-size: 0.9rem;
  font-weight: 600;
  color: #f8fafc;
}

code {
  background: #0f172a;
  padding: 0.1em 0.35em;
  border-radius: 4px;
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 0.85em;
}
```

---

### JS

```js
// Random Float
const randValue  = document.getElementById('rand-value');
const btnRandom  = document.getElementById('btn-random');

btnRandom.addEventListener('click', () => {
  const n = Math.random();
  randValue.textContent = n.toFixed(10);
  randValue.style.color = '#60a5fa';
});

// Random Integer
const randIntValue = document.getElementById('rand-int-value');
const btnRandomInt = document.getElementById('btn-random-int');
const randMin = document.getElementById('rand-min');
const randMax = document.getElementById('rand-max');

btnRandomInt.addEventListener('click', () => {
  const min = Number(randMin.value);
  const max = Number(randMax.value);
  if (min > max) {
    randIntValue.textContent = 'min > max!';
    return;
  }
  const result = Math.floor(Math.random() * (max - min + 1)) + min;
  randIntValue.textContent = result;
});

// Rounding slider
const slider        = document.getElementById('round-slider');
const sliderDisplay = document.getElementById('slider-display');
const roundingDiv   = document.getElementById('rounding-results');

function updateRounding() {
  const v = parseFloat(slider.value);
  sliderDisplay.textContent = v.toFixed(1);

  const methods = [
    { label: 'Math.round(x)',  value: Math.round(v)  },
    { label: 'Math.floor(x)',  value: Math.floor(v)  },
    { label: 'Math.ceil(x)',   value: Math.ceil(v)   },
    { label: 'Math.trunc(x)',  value: Math.trunc(v)  },
  ];

  roundingDiv.innerHTML = '';
  methods.forEach(({ label, value }) => {
    const row = document.createElement('div');
    row.className = 'round-row';
    row.innerHTML = `<span class="round-method">${label}</span><span class="round-result">${value}</span>`;
    roundingDiv.appendChild(row);
  });
}

slider.addEventListener('input', updateRounding);
updateRounding();

// More Methods
const methodsGrid = document.getElementById('methods-grid');

const methodExamples = [
  { call: 'Math.abs(-42)',       result: Math.abs(-42) },
  { call: 'Math.abs(42)',        result: Math.abs(42) },
  { call: 'Math.pow(2, 10)',     result: Math.pow(2, 10) },
  { call: '2 ** 10',             result: 2 ** 10 },
  { call: 'Math.sqrt(144)',      result: Math.sqrt(144) },
  { call: 'Math.cbrt(27)',       result: Math.cbrt(27) },
  { call: 'Math.min(3,1,4,1,5)', result: Math.min(3,1,4,1,5) },
  { call: 'Math.max(3,1,4,1,5)', result: Math.max(3,1,4,1,5) },
  { call: 'Math.log2(8)',        result: Math.log2(8) },
  { call: 'Math.log10(1000)',    result: Math.log10(1000) },
  { call: 'Math.sign(-5)',       result: Math.sign(-5) },
  { call: 'Math.sign(0)',        result: Math.sign(0) },
];

methodExamples.forEach(({ call, result }) => {
  const card = document.createElement('div');
  card.className = 'method-card';
  card.innerHTML = `<div class="method-call">${call}</div><div class="method-result">${result}</div>`;
  methodsGrid.appendChild(card);
});

// Constants
const constantsGrid = document.getElementById('constants-grid');

const constants = [
  { name: 'Math.PI',      value: Math.PI },
  { name: 'Math.E',       value: Math.E },
  { name: 'Math.SQRT2',   value: Math.SQRT2 },
  { name: 'Math.LN2',     value: Math.LN2 },
  { name: 'Math.LN10',    value: Math.LN10 },
  { name: 'Math.LOG2E',   value: Math.LOG2E },
];

constants.forEach(({ name, value }) => {
  const card = document.createElement('div');
  card.className = 'const-card';
  card.innerHTML = `<div class="const-name">${name}</div><div class="const-value">${value}</div>`;
  constantsGrid.appendChild(card);
});
```

---

## CODEPEN 4 — Truthy and Falsy Explorer

**Placement:** After the Truthy and Falsy section (after LISTING 18.28)

**Purpose:** Shows all 6 falsy values. A list of various values with Boolean() evaluation, color-coded green/red for truthy/falsy.

---

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Truthy and Falsy Explorer</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>Truthy &amp; Falsy Explorer</h1>
    <p class="subtitle">In JavaScript, every value has a boolean interpretation. Only 6 values are falsy — everything else is truthy.</p>

    <div class="legend">
      <div class="legend-item truthy-label">Truthy — evaluates to <code>true</code> in a boolean context</div>
      <div class="legend-item falsy-label">Falsy — evaluates to <code>false</code> in a boolean context</div>
    </div>

    <section class="card">
      <h2>The 6 Falsy Values</h2>
      <p class="card-note">Memorize these. Everything else is truthy.</p>
      <div class="falsy-grid" id="falsy-grid"></div>
    </section>

    <section class="card">
      <h2>Truthy &amp; Falsy Values in the Wild</h2>
      <p class="card-note">Click <strong>Evaluate All</strong> to see each value's boolean interpretation.</p>
      <button class="btn" id="btn-evaluate">Evaluate All with Boolean()</button>
      <div class="values-list" id="values-list"></div>
    </section>

    <section class="card">
      <h2>Live Boolean() Tester</h2>
      <p class="card-note">Type any value and see if it is truthy or falsy.</p>
      <div class="input-row">
        <input type="text" id="live-input" placeholder='Try: 0, "", [], {}, "false", null ...'>
        <button class="btn btn-test" id="btn-test">Test</button>
      </div>
      <div id="live-result" class="live-result hidden"></div>
    </section>

    <section class="card">
      <h2>Common Gotchas</h2>
      <ul class="gotcha-list">
        <li><code>[]</code> — empty array is <strong>truthy</strong>. Use <code>arr.length === 0</code> to check if empty.</li>
        <li><code>{}</code> — empty object is <strong>truthy</strong>. Use <code>Object.keys(obj).length === 0</code>.</li>
        <li><code>"false"</code> — the string "false" is <strong>truthy</strong>. Only the boolean <code>false</code> is falsy.</li>
        <li><code>"0"</code> — the string "0" is <strong>truthy</strong>. Only the number <code>0</code> is falsy.</li>
        <li><code>-0</code> — negative zero is <strong>falsy</strong>. Same as <code>0</code> in boolean context.</li>
        <li><code>0n</code> — BigInt zero is <strong>falsy</strong>. Any non-zero BigInt is truthy.</li>
      </ul>
    </section>
  </div>
  <script src="script.js"></script>
</body>
</html>
```

---

### CSS

```css
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #0f172a;
  color: #e2e8f0;
  min-height: 100vh;
  padding: 2rem 1rem;
}

.container {
  max-width: 680px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

h1 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #f8fafc;
}

.subtitle {
  color: #94a3b8;
  margin-top: 0.25rem;
  font-size: 0.95rem;
  line-height: 1.5;
}

h2 {
  font-size: 1.05rem;
  font-weight: 600;
  color: #cbd5e1;
  margin-bottom: 0.5rem;
}

.card {
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 12px;
  padding: 1.5rem;
}

.card-note {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 1rem;
}

/* Legend */
.legend {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.legend-item {
  flex: 1;
  min-width: 200px;
  padding: 0.6rem 0.9rem;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 500;
}

.truthy-label {
  background: #052e16;
  color: #86efac;
  border: 1px solid #166534;
}

.falsy-label {
  background: #2d0f0f;
  color: #fca5a5;
  border: 1px solid #7f1d1d;
}

/* Falsy grid */
.falsy-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.6rem;
}

@media (max-width: 440px) {
  .falsy-grid { grid-template-columns: repeat(2, 1fr); }
}

.falsy-chip {
  background: #2d0f0f;
  border: 1px solid #7f1d1d;
  border-radius: 8px;
  padding: 0.75rem;
  text-align: center;
}

.falsy-value {
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 1.1rem;
  font-weight: 700;
  color: #fca5a5;
  display: block;
  margin-bottom: 0.25rem;
}

.falsy-desc {
  font-size: 0.7rem;
  color: #64748b;
}

/* Values list */
.values-list {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  margin-top: 1rem;
}

.value-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.55rem 0.9rem;
  border-radius: 8px;
  border: 1px solid #334155;
  background: #0f172a;
  transition: all 0.25s ease;
}

.value-row.truthy {
  border-color: #166534;
  background: #052e16;
}

.value-row.falsy {
  border-color: #7f1d1d;
  background: #2d0f0f;
}

.value-code {
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 0.9rem;
  color: #e2e8f0;
  flex: 1;
}

.value-eval {
  font-family: 'Fira Code', monospace;
  font-size: 0.8rem;
  color: #475569;
  flex: 1;
  text-align: center;
}

.value-badge {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.2em 0.6em;
  border-radius: 999px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  min-width: 60px;
  text-align: center;
}

.badge-truthy { background: #166534; color: #bbf7d0; }
.badge-falsy  { background: #7f1d1d; color: #fecaca; }
.badge-pending { background: #334155; color: #64748b; }

/* Buttons */
.btn {
  padding: 0.65rem 1.25rem;
  border: none;
  border-radius: 8px;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: background 0.15s;
}

.btn:hover { background: #1d4ed8; }
.btn-test  { background: #7c3aed; flex-shrink: 0; }
.btn-test:hover { background: #6d28d9; }

/* Live tester */
.input-row {
  display: flex;
  gap: 0.6rem;
  margin-bottom: 0.75rem;
}

input[type="text"] {
  flex: 1;
  background: #0f172a;
  border: 1px solid #475569;
  border-radius: 8px;
  padding: 0.55rem 0.85rem;
  color: #e2e8f0;
  font-family: 'Fira Code', monospace;
  font-size: 0.875rem;
  outline: none;
  transition: border-color 0.15s;
}

input:focus { border-color: #60a5fa; }

.live-result {
  padding: 1rem 1.25rem;
  border-radius: 8px;
  font-family: 'Fira Code', monospace;
  font-size: 1rem;
  font-weight: 700;
  text-align: center;
  transition: all 0.2s;
}

.live-result.hidden { display: none; }
.live-result.truthy { background: #052e16; color: #86efac; border: 1px solid #166534; }
.live-result.falsy  { background: #2d0f0f; color: #fca5a5; border: 1px solid #7f1d1d; }
.live-result.error  { background: #1c1205; color: #fde68a; border: 1px solid #92400e; }

/* Gotcha list */
.gotcha-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.gotcha-list li {
  padding-left: 1.25rem;
  position: relative;
  font-size: 0.875rem;
  color: #94a3b8;
  line-height: 1.5;
}

.gotcha-list li::before {
  content: '!';
  position: absolute;
  left: 0;
  color: #fbbf24;
  font-weight: 900;
  font-size: 0.8rem;
}

code {
  background: #0f172a;
  padding: 0.1em 0.4em;
  border-radius: 4px;
  font-family: 'Fira Code', monospace;
  font-size: 0.85em;
  color: #f8fafc;
}
```

---

### JS

```js
// The 6 falsy values
const falsyValues = [
  { value: 'false',     desc: 'boolean false' },
  { value: '0',         desc: 'number zero' },
  { value: '""',        desc: 'empty string' },
  { value: 'null',      desc: 'intentional absence' },
  { value: 'undefined', desc: 'unassigned value' },
  { value: 'NaN',       desc: 'Not a Number' },
];

const falsyGrid = document.getElementById('falsy-grid');
falsyValues.forEach(({ value, desc }) => {
  const chip = document.createElement('div');
  chip.className = 'falsy-chip';
  chip.innerHTML = `<span class="falsy-value">${value}</span><span class="falsy-desc">${desc}</span>`;
  falsyGrid.appendChild(chip);
});

// Values list — mix of truthy and falsy
const allValues = [
  { display: 'false',       raw: false },
  { display: '0',           raw: 0 },
  { display: '""',          raw: '' },
  { display: 'null',        raw: null },
  { display: 'undefined',   raw: undefined },
  { display: 'NaN',         raw: NaN },
  { display: 'true',        raw: true },
  { display: '1',           raw: 1 },
  { display: '-1',          raw: -1 },
  { display: '"hello"',     raw: 'hello' },
  { display: '"0"',         raw: '0' },
  { display: '"false"',     raw: 'false' },
  { display: '[]',          raw: [] },
  { display: '{}',          raw: {} },
  { display: '[0]',         raw: [0] },
  { display: 'Infinity',    raw: Infinity },
];

const valuesList = document.getElementById('values-list');
let rows = [];

allValues.forEach(({ display, raw }) => {
  const row = document.createElement('div');
  row.className = 'value-row';

  const isTruthy = Boolean(raw);
  row.innerHTML = `
    <span class="value-code">${display}</span>
    <span class="value-eval">Boolean(${display})</span>
    <span class="value-badge badge-pending">?</span>
  `;

  row._isTruthy = isTruthy;
  valuesList.appendChild(row);
  rows.push(row);
});

let evaluated = false;

document.getElementById('btn-evaluate').addEventListener('click', () => {
  if (evaluated) {
    // Reset
    rows.forEach(row => {
      row.className = 'value-row';
      row.querySelector('.value-badge').className = 'value-badge badge-pending';
      row.querySelector('.value-badge').textContent = '?';
    });
    document.getElementById('btn-evaluate').textContent = 'Evaluate All with Boolean()';
    evaluated = false;
  } else {
    rows.forEach((row, i) => {
      const isTruthy = row._isTruthy;
      setTimeout(() => {
        row.classList.add(isTruthy ? 'truthy' : 'falsy');
        const badge = row.querySelector('.value-badge');
        badge.className = `value-badge ${isTruthy ? 'badge-truthy' : 'badge-falsy'}`;
        badge.textContent = isTruthy ? 'truthy' : 'falsy';
      }, i * 60);
    });
    document.getElementById('btn-evaluate').textContent = 'Reset';
    evaluated = true;
  }
});

// Live tester
const liveInput  = document.getElementById('live-input');
const btnTest    = document.getElementById('btn-test');
const liveResult = document.getElementById('live-result');

function testValue() {
  const raw = liveInput.value;
  if (raw === '') return;

  try {
    const evaluated = Function('"use strict"; return Boolean(' + raw + ')')();
    liveResult.className = `live-result ${evaluated ? 'truthy' : 'falsy'}`;
    liveResult.textContent = `Boolean(${raw}) → ${evaluated} — "${raw}" is ${evaluated ? 'TRUTHY' : 'FALSY'}`;
  } catch (e) {
    liveResult.className = 'live-result error';
    liveResult.textContent = `Could not evaluate: ${e.message}`;
  }
}

btnTest.addEventListener('click', testValue);
liveInput.addEventListener('keydown', e => { if (e.key === 'Enter') testValue(); });
```

---

## CODEPEN 5 — Equality Comparison: == vs ===

**Placement:** After the Loose vs. Strict Equality section (after LISTING 18.30)

**Purpose:** Visual table showing comparisons where == and === give different results. Color-coded true/false results for each operator.

---

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>== vs === Equality Explorer</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>== vs. === Equality</h1>
    <p class="subtitle">Loose equality (<code>==</code>) coerces types before comparing. Strict equality (<code>===</code>) never coerces — different types always return <code>false</code>.</p>

    <div class="rule-banner">
      Always use <code>===</code> and <code>!==</code>. Never use <code>==</code> or <code>!=</code>.
    </div>

    <section class="card">
      <h2>Side-by-Side Comparison</h2>
      <p class="card-note">These are real pairs where == and === give <em>different</em> results. This is why == causes bugs.</p>

      <div class="comparison-header">
        <span class="col-expr">Expression</span>
        <span class="col-loose"><code>==</code> (loose)</span>
        <span class="col-strict"><code>===</code> (strict)</span>
        <span class="col-why">Why they differ</span>
      </div>

      <div id="comparison-rows"></div>
    </section>

    <section class="card">
      <h2>Same-Type Comparisons — == and === Agree</h2>
      <p class="card-note">When both values have the same type, == and === behave identically. The difference only appears across types.</p>
      <div id="same-type-rows"></div>
    </section>

    <section class="card">
      <h2>Live Equality Tester</h2>
      <p class="card-note">Enter two values separated by a comma and compare them with both operators.</p>
      <div class="live-row">
        <input type="text" id="val-a" placeholder="Left value (e.g. 0)">
        <span class="vs-label">vs</span>
        <input type="text" id="val-b" placeholder="Right value (e.g. false)">
        <button class="btn" id="btn-compare">Compare</button>
      </div>
      <div id="live-comparison" class="live-comparison hidden"></div>
    </section>

    <section class="card coercion-card">
      <h2>How == Coercion Works (Simplified)</h2>
      <ol class="coercion-steps">
        <li>If types are the same, compare values directly (same as ===).</li>
        <li>If one is <code>null</code> and the other is <code>undefined</code>, return <code>true</code>.</li>
        <li>If one is a number and the other is a string, convert the string to a number, then compare.</li>
        <li>If one is a boolean, convert it to a number (true → 1, false → 0), then compare.</li>
        <li>If one is an object and the other is a primitive, convert the object to a primitive, then compare.</li>
        <li>Otherwise, return <code>false</code>.</li>
      </ol>
      <p class="coercion-note">These rules are complex, context-dependent, and hard to memorize. This is why <strong>always using ===</strong> is the correct rule — not an opinion.</p>
    </section>
  </div>
  <script src="script.js"></script>
</body>
</html>
```

---

### CSS

```css
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #0f172a;
  color: #e2e8f0;
  min-height: 100vh;
  padding: 2rem 1rem;
}

.container {
  max-width: 760px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

h1 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #f8fafc;
}

.subtitle {
  color: #94a3b8;
  margin-top: 0.25rem;
  font-size: 0.95rem;
  line-height: 1.5;
}

h2 {
  font-size: 1.05rem;
  font-weight: 600;
  color: #cbd5e1;
  margin-bottom: 0.6rem;
}

.card {
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 12px;
  padding: 1.5rem;
}

.card-note {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 1rem;
  line-height: 1.5;
}

/* Rule banner */
.rule-banner {
  background: #1a1a00;
  border: 1px solid #ca8a04;
  border-radius: 10px;
  padding: 0.85rem 1.25rem;
  color: #fde047;
  font-weight: 600;
  font-size: 0.95rem;
  text-align: center;
}

/* Comparison table */
.comparison-header {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 2fr;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: #475569;
  border-bottom: 1px solid #334155;
  margin-bottom: 0.5rem;
}

@media (max-width: 500px) {
  .comparison-header { grid-template-columns: 2fr 1fr 1fr; }
  .col-why { display: none; }
  .why-cell { display: none; }
}

.comparison-row {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 2fr;
  gap: 0.5rem;
  padding: 0.55rem 0.75rem;
  border-radius: 6px;
  margin-bottom: 0.35rem;
  background: #0f172a;
  align-items: center;
  font-size: 0.875rem;
}

.comparison-row:hover { background: #151f30; }

.expr-cell {
  font-family: 'Fira Code', 'Courier New', monospace;
  color: #cbd5e1;
}

.result-cell {
  text-align: center;
  font-family: 'Fira Code', monospace;
  font-weight: 700;
  padding: 0.2em 0.4em;
  border-radius: 4px;
  font-size: 0.875rem;
}

.result-true  { color: #86efac; background: #052e16; }
.result-false { color: #fca5a5; background: #2d0f0f; }

.why-cell {
  font-size: 0.78rem;
  color: #64748b;
  line-height: 1.4;
}

/* Same-type rows */
#same-type-rows .comparison-row {
  grid-template-columns: 2fr 1fr 1fr 2fr;
}

/* Live tester */
.live-row {
  display: flex;
  gap: 0.5rem;
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: 0.75rem;
}

input[type="text"] {
  flex: 1;
  min-width: 100px;
  background: #0f172a;
  border: 1px solid #475569;
  border-radius: 8px;
  padding: 0.55rem 0.85rem;
  color: #e2e8f0;
  font-family: 'Fira Code', monospace;
  font-size: 0.875rem;
  outline: none;
  transition: border-color 0.15s;
}

input:focus { border-color: #60a5fa; }

.vs-label {
  color: #475569;
  font-weight: 600;
  font-size: 0.9rem;
}

.btn {
  padding: 0.6rem 1.1rem;
  border: none;
  border-radius: 8px;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: background 0.15s;
  white-space: nowrap;
}

.btn:hover { background: #1d4ed8; }

.live-comparison {
  background: #0f172a;
  border: 1px solid #334155;
  border-radius: 8px;
  overflow: hidden;
}

.live-comparison.hidden { display: none; }

.live-result-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1rem;
  font-family: 'Fira Code', monospace;
  font-size: 0.95rem;
  border-bottom: 1px solid #1e293b;
}

.live-result-row:last-child { border-bottom: none; }

.live-expr { color: #94a3b8; }

.live-badge {
  font-weight: 700;
  padding: 0.2em 0.65em;
  border-radius: 5px;
}

.badge-true  { color: #86efac; background: #052e16; }
.badge-false { color: #fca5a5; background: #2d0f0f; }
.badge-error { color: #fde68a; background: #1c1205; }

/* Coercion steps */
.coercion-steps {
  padding-left: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.coercion-steps li {
  font-size: 0.875rem;
  color: #94a3b8;
  line-height: 1.5;
}

.coercion-note {
  margin-top: 1rem;
  font-size: 0.875rem;
  color: #64748b;
  line-height: 1.5;
  padding: 0.75rem;
  background: #0f172a;
  border-radius: 8px;
  border-left: 3px solid #ca8a04;
}

code {
  background: #0f172a;
  padding: 0.1em 0.4em;
  border-radius: 4px;
  font-family: 'Fira Code', monospace;
  font-size: 0.85em;
  color: #f8fafc;
}
```

---

### JS

```js
// Cross-type comparisons — where == and === differ
const crossTypeComparisons = [
  {
    expr:   '0 == false',
    left:   0,
    right:  false,
    why:    'false coerces to 0; 0 == 0 is true'
  },
  {
    expr:   '"" == false',
    left:   '',
    right:  false,
    why:    'false → 0, "" → 0; 0 == 0 is true'
  },
  {
    expr:   '"" == 0',
    left:   '',
    right:  0,
    why:    'empty string coerces to 0'
  },
  {
    expr:   '"1" == 1',
    left:   '1',
    right:  1,
    why:    '"1" coerces to the number 1'
  },
  {
    expr:   'null == undefined',
    left:   null,
    right:  undefined,
    why:    'special rule: these two are loosely equal'
  },
  {
    expr:   'null == 0',
    left:   null,
    right:  0,
    why:    'null only equals undefined loosely, nothing else'
  },
  {
    expr:   '[0] == false',
    left:   [0],
    right:  false,
    why:    '[0] → "0" → 0; false → 0; 0 == 0'
  },
  {
    expr:   '"0" == false',
    left:   '0',
    right:  false,
    why:    'false → 0; "0" → 0; 0 == 0'
  },
];

// Same-type comparisons — both operators agree
const sameTypeComparisons = [
  { expr: '1 === 1',           left: 1,         right: 1,         why: 'Same type, same value' },
  { expr: '"a" === "a"',       left: 'a',        right: 'a',       why: 'Same type, same value' },
  { expr: 'null === null',     left: null,       right: null,      why: 'Same type, same value' },
  { expr: '1 === 2',           left: 1,          right: 2,         why: 'Same type, different value' },
  { expr: 'NaN === NaN',       left: NaN,        right: NaN,       why: 'NaN is the only value not equal to itself' },
];

function makeRow(comparison, container) {
  /* eslint-disable eqeqeq */
  let looseResult, strictResult;
  try {
    looseResult  = comparison.left == comparison.right;
    strictResult = comparison.left === comparison.right;
  } catch(e) {
    return;
  }
  /* eslint-enable eqeqeq */

  const row = document.createElement('div');
  row.className = 'comparison-row';
  row.innerHTML = `
    <span class="expr-cell">${comparison.expr}</span>
    <span class="result-cell ${looseResult ? 'result-true' : 'result-false'}">${looseResult}</span>
    <span class="result-cell ${strictResult ? 'result-true' : 'result-false'}">${strictResult}</span>
    <span class="why-cell">${comparison.why || ''}</span>
  `;
  container.appendChild(row);
}

const crossContainer = document.getElementById('comparison-rows');
crossTypeComparisons.forEach(c => makeRow(c, crossContainer));

const sameContainer = document.getElementById('same-type-rows');
sameTypeComparisons.forEach(c => makeRow(c, sameContainer));

// Live tester
const valA       = document.getElementById('val-a');
const valB       = document.getElementById('val-b');
const btnCompare = document.getElementById('btn-compare');
const liveComp   = document.getElementById('live-comparison');

function compare() {
  const rawA = valA.value.trim();
  const rawB = valB.value.trim();
  if (!rawA || !rawB) return;

  let a, b;
  try {
    a = Function('"use strict"; return (' + rawA + ')')();
    b = Function('"use strict"; return (' + rawB + ')')();
  } catch(e) {
    liveComp.classList.remove('hidden');
    liveComp.innerHTML = `<div class="live-result-row"><span class="live-expr">Error evaluating values</span><span class="live-badge badge-error">${e.message}</span></div>`;
    return;
  }

  /* eslint-disable eqeqeq */
  const loose  = a == b;
  const strict = a === b;
  /* eslint-enable eqeqeq */

  liveComp.classList.remove('hidden');
  liveComp.innerHTML = `
    <div class="live-result-row">
      <span class="live-expr">${rawA} == ${rawB}</span>
      <span class="live-badge ${loose ? 'badge-true' : 'badge-false'}">${loose}</span>
    </div>
    <div class="live-result-row">
      <span class="live-expr">${rawA} === ${rawB}</span>
      <span class="live-badge ${strict ? 'badge-true' : 'badge-false'}">${strict}</span>
    </div>
    <div class="live-result-row">
      <span class="live-expr" style="color:#475569; font-size:0.8rem">typeof: ${rawA} is "${typeof a}" — ${rawB} is "${typeof b}"</span>
      <span class="live-badge" style="background:#1e293b; color:#64748b">${typeof a === typeof b ? 'same type' : 'different types'}</span>
    </div>
  `;
}

btnCompare.addEventListener('click', compare);
[valA, valB].forEach(el => el.addEventListener('keydown', e => {
  if (e.key === 'Enter') compare();
}));
```
