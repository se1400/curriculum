# Day 22 — Functions: CodePen Code Blocks

Each section below contains the HTML, CSS, and JS for one CodePen embed referenced in the article.

---

## CODEPEN 1 — Three Function Syntax Styles Comparison

**HTML**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Three Function Syntax Styles</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      min-height: 100vh;
      padding: 2rem 1rem;
    }

    h1 {
      text-align: center;
      font-size: 1.4rem;
      color: #f1f5f9;
      margin-bottom: 0.4rem;
    }

    .subtitle {
      text-align: center;
      color: #94a3b8;
      font-size: 0.9rem;
      margin-bottom: 2rem;
    }

    .panels {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem;
      max-width: 960px;
      margin: 0 auto 2rem;
    }

    .panel {
      background: #1e293b;
      border-radius: 10px;
      overflow: hidden;
      border: 1px solid #334155;
    }

    .panel-header {
      padding: 0.75rem 1rem;
      font-weight: 700;
      font-size: 0.85rem;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .panel-declaration .panel-header { background: #1e3a5f; color: #60a5fa; }
    .panel-expression  .panel-header { background: #1e3a2a; color: #4ade80; }
    .panel-arrow       .panel-header { background: #3b1f47; color: #c084fc; }

    .badge {
      font-size: 0.7rem;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      font-weight: 600;
      margin-left: auto;
    }
    .panel-declaration .badge { background: #1d4ed8; color: #bfdbfe; }
    .panel-expression  .badge { background: #15803d; color: #bbf7d0; }
    .panel-arrow       .badge { background: #7e22ce; color: #e9d5ff; }

    .panel-body {
      padding: 1rem;
    }

    .code-block {
      background: #0f172a;
      border-radius: 6px;
      padding: 0.85rem;
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      line-height: 1.65;
      overflow-x: auto;
      border: 1px solid #1e293b;
      margin-bottom: 0.75rem;
    }

    .kw   { color: #c084fc; }
    .fn   { color: #60a5fa; }
    .par  { color: #e2e8f0; }
    .str  { color: #4ade80; }
    .cm   { color: #64748b; font-style: italic; }
    .ret  { color: #fb923c; }

    .note {
      font-size: 0.78rem;
      color: #94a3b8;
      line-height: 1.5;
      padding: 0.5rem 0.6rem;
      background: #1e293b;
      border-left: 3px solid #334155;
      border-radius: 0 4px 4px 0;
    }

    .demo-area {
      max-width: 480px;
      margin: 0 auto;
      background: #1e293b;
      border-radius: 10px;
      padding: 1.5rem;
      border: 1px solid #334155;
    }

    .demo-area h2 {
      font-size: 1rem;
      color: #f1f5f9;
      margin-bottom: 1rem;
      text-align: center;
    }

    .input-row {
      display: flex;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }

    .input-row input {
      flex: 1;
      padding: 0.6rem 0.8rem;
      background: #0f172a;
      border: 1.5px solid #334155;
      border-radius: 6px;
      color: #e2e8f0;
      font-size: 1rem;
    }

    .input-row input:focus {
      outline: none;
      border-color: #60a5fa;
    }

    .input-row button {
      padding: 0.6rem 1.2rem;
      background: #3b82f6;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
    }

    .input-row button:hover { background: #2563eb; }

    .results {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .result-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.55rem 0.75rem;
      background: #0f172a;
      border-radius: 6px;
      font-size: 0.88rem;
    }

    .result-label {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      width: 90px;
      flex-shrink: 0;
    }

    .result-value {
      color: #f1f5f9;
      font-family: monospace;
    }

    .label-decl { color: #60a5fa; }
    .label-expr { color: #4ade80; }
    .label-arrow { color: #c084fc; }

    .hoist-box {
      margin-top: 1.25rem;
      padding: 0.85rem;
      border-radius: 8px;
      font-size: 0.82rem;
      line-height: 1.6;
    }

    .hoist-success {
      background: #052e16;
      border: 1px solid #166534;
      color: #86efac;
    }

    .hoist-fail {
      background: #2d0000;
      border: 1px solid #7f1d1d;
      color: #fca5a5;
    }

    .hoist-title {
      font-weight: 700;
      margin-bottom: 0.35rem;
    }
  </style>
</head>
<body>

  <h1>Three Function Syntax Styles</h1>
  <p class="subtitle">The same squaring operation written three ways</p>

  <div class="panels">

    <div class="panel panel-declaration">
      <div class="panel-header">
        Function Declaration
        <span class="badge">Hoisted</span>
      </div>
      <div class="panel-body">
        <div class="code-block">
<span class="kw">function</span> <span class="fn">square</span>(<span class="par">n</span>) {<br>
&nbsp;&nbsp;<span class="ret">return</span> <span class="par">n</span> * <span class="par">n</span>;<br>
}
        </div>
        <div class="note">
          Uses the <code>function</code> keyword. Fully hoisted &mdash; you can call it before it appears in the file. Best for top-level named utilities.
        </div>
      </div>
    </div>

    <div class="panel panel-expression">
      <div class="panel-header">
        Function Expression
        <span class="badge">Not Hoisted</span>
      </div>
      <div class="panel-body">
        <div class="code-block">
<span class="kw">const</span> <span class="fn">square</span> = <span class="kw">function</span>(<span class="par">n</span>) {<br>
&nbsp;&nbsp;<span class="ret">return</span> <span class="par">n</span> * <span class="par">n</span>;<br>
};
        </div>
        <div class="note">
          Stored as a variable value. Not available before its declaration line. Good when you want a function as data.
        </div>
      </div>
    </div>

    <div class="panel panel-arrow">
      <div class="panel-header">
        Arrow Function
        <span class="badge">Concise</span>
      </div>
      <div class="panel-body">
        <div class="code-block">
<span class="kw">const</span> <span class="fn">square</span> = <span class="par">n</span> =&gt; <span class="par">n</span> * <span class="par">n</span>;<br>
<br>
<span class="cm">// Or with explicit return:</span><br>
<span class="kw">const</span> <span class="fn">square</span> = <span class="par">n</span> =&gt; {<br>
&nbsp;&nbsp;<span class="ret">return</span> <span class="par">n</span> * <span class="par">n</span>;<br>
};
        </div>
        <div class="note">
          Implicit return when no curly braces. No own <code>this</code>. Ideal for callbacks and short operations.
        </div>
      </div>
    </div>

  </div>

  <div class="demo-area">
    <h2>Try It &mdash; All Three Produce the Same Result</h2>
    <div class="input-row">
      <input type="number" id="numInput" value="7" min="0" max="999">
      <button id="runBtn">Square It</button>
    </div>
    <div class="results">
      <div class="result-row">
        <span class="result-label label-decl">Declaration</span>
        <span class="result-value" id="out-decl">&mdash;</span>
      </div>
      <div class="result-row">
        <span class="result-label label-expr">Expression</span>
        <span class="result-value" id="out-expr">&mdash;</span>
      </div>
      <div class="result-row">
        <span class="result-label label-arrow">Arrow</span>
        <span class="result-value" id="out-arrow">&mdash;</span>
      </div>
    </div>

    <div class="hoist-box hoist-success">
      <div class="hoist-title">Hoisting Demo</div>
      Calling the <strong>declaration</strong> before its definition in the file works fine &mdash; declarations are fully hoisted. Calling an <strong>expression or arrow</strong> before its definition throws a ReferenceError (TDZ). See the console for details.
    </div>
  </div>

</body>
</html>
```

**CSS**
```css
/* All styles are inside the <style> block in the HTML above. */
```

**JS**
```js
// --- Function Declaration (hoisted — can call before definition) ---
function squareDecl(n) {
  return n * n;
}

// --- Function Expression (not hoisted) ---
const squareExpr = function squareExpression(n) {
  // Note: "squareExpression" is a named function expression —
  // the name appears in stack traces but is not accessible outside.
  return n * n;
};

// --- Arrow Function (implicit return) ---
const squareArrow = n => n * n;

// --- Hoisting demo (runs immediately to show the behavior) ---
// This works because squareDecl is a declaration:
try {
  const hoistResult = squareDecl(5);
  console.log('Hoisting: squareDecl(5) called BEFORE definition in execution order would show 25 here if JS allowed re-ordering, but in this demo the function is defined above.');
} catch (e) {
  console.error('Hoisting error:', e.message);
}

// --- Interactive demo ---
const numInput = document.getElementById('numInput');
const runBtn   = document.getElementById('runBtn');
const outDecl  = document.getElementById('out-decl');
const outExpr  = document.getElementById('out-expr');
const outArrow = document.getElementById('out-arrow');

function runDemo() {
  const n = Number(numInput.value);

  const dResult = squareDecl(n);
  const eResult = squareExpr(n);
  const aResult = squareArrow(n);

  outDecl.textContent  = `${n} × ${n} = ${dResult}`;
  outExpr.textContent  = `${n} × ${n} = ${eResult}`;
  outArrow.textContent = `${n} × ${n} = ${aResult}`;

  // Confirm they are all equal
  if (dResult === eResult && eResult === aResult) {
    console.log(`All three return the same value: ${dResult}`);
  }
}

runBtn.addEventListener('click', runDemo);
numInput.addEventListener('keydown', e => { if (e.key === 'Enter') runDemo(); });

// Run once on load
runDemo();

// --- Console demonstrations for the learner ---
console.log('=== Function Syntax Comparison ===');
console.log('squareDecl(9):', squareDecl(9));
console.log('squareExpr(9):', squareExpr(9));
console.log('squareArrow(9):', squareArrow(9));

// Named function expressions appear in stack traces
console.log('squareExpr.name:', squareExpr.name); // "squareExpression"
console.log('squareArrow.name:', squareArrow.name); // "squareArrow" (inferred from variable)
console.log('squareDecl.name:', squareDecl.name);  // "squareDecl"
```

---

## CODEPEN 2 — Parameters, Defaults & Rest

**HTML**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Parameters, Defaults & Rest</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f8fafc;
      color: #1e293b;
      padding: 2rem 1rem;
    }

    h1 {
      text-align: center;
      font-size: 1.4rem;
      margin-bottom: 0.35rem;
      color: #0f172a;
    }

    .subtitle {
      text-align: center;
      color: #64748b;
      font-size: 0.9rem;
      margin-bottom: 2rem;
    }

    .sections {
      display: flex;
      flex-direction: column;
      gap: 2rem;
      max-width: 640px;
      margin: 0 auto;
    }

    .section-card {
      background: white;
      border-radius: 12px;
      padding: 1.5rem;
      border: 1px solid #e2e8f0;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }

    .section-card h2 {
      font-size: 1rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid #f1f5f9;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .tag {
      font-size: 0.7rem;
      font-weight: 600;
      padding: 0.15rem 0.5rem;
      border-radius: 999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .tag-blue   { background: #dbeafe; color: #1d4ed8; }
    .tag-green  { background: #dcfce7; color: #166534; }
    .tag-purple { background: #f3e8ff; color: #7e22ce; }
    .tag-orange { background: #fff7ed; color: #c2410c; }

    .controls {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }

    label {
      font-size: 0.82rem;
      font-weight: 600;
      color: #475569;
      display: flex;
      flex-direction: column;
      gap: 0.3rem;
    }

    input[type="text"],
    input[type="number"] {
      padding: 0.5rem 0.65rem;
      border: 1.5px solid #cbd5e1;
      border-radius: 6px;
      font-size: 0.95rem;
      color: #0f172a;
      width: 160px;
    }

    input:focus {
      outline: none;
      border-color: #6366f1;
      box-shadow: 0 0 0 3px rgba(99,102,241,0.12);
    }

    .run-btn {
      align-self: flex-end;
      padding: 0.52rem 1.1rem;
      background: #6366f1;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
    }

    .run-btn:hover { background: #4f46e5; }

    .param-slots {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 1rem;
    }

    .slot {
      background: #f1f5f9;
      border-radius: 8px;
      padding: 0.5rem 0.8rem;
      font-size: 0.82rem;
      min-width: 120px;
    }

    .slot-name {
      font-weight: 700;
      color: #475569;
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.2rem;
    }

    .slot-value {
      font-family: monospace;
      font-size: 0.95rem;
    }

    .slot-value.received  { color: #166534; }
    .slot-value.defaulted { color: #1d4ed8; }
    .slot-value.undef     { color: #dc2626; }
    .slot-value.rest      { color: #7e22ce; }

    .output-box {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 0.75rem;
      font-family: monospace;
      font-size: 0.9rem;
      color: #0f172a;
      min-height: 2.5rem;
    }

    .guard-demo {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    .guard-input-row {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .guard-input-row input {
      width: 100px;
    }

    .guard-result {
      padding: 0.6rem 0.8rem;
      border-radius: 6px;
      font-size: 0.88rem;
      font-family: monospace;
      min-height: 2.2rem;
    }

    .guard-ok    { background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }
    .guard-fail  { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }
  </style>
</head>
<body>

  <h1>Parameters, Defaults &amp; Rest</h1>
  <p class="subtitle">See exactly what each parameter receives when you call a function</p>

  <div class="sections">

    <!-- SECTION 1: Too few / too many arguments -->
    <div class="section-card">
      <h2>Positional Arguments <span class="tag tag-blue">Too Few / Too Many</span></h2>
      <div class="controls">
        <label>
          subject
          <input type="text" id="arg-subject" value="The sky">
        </label>
        <label>
          adjective (optional)
          <input type="text" id="arg-adjective" placeholder="leave blank to omit">
        </label>
        <button class="run-btn" id="run-positional">Run</button>
      </div>
      <div class="param-slots" id="slots-positional">
        <div class="slot">
          <div class="slot-name">subject</div>
          <div class="slot-value" id="slot-subject">&mdash;</div>
        </div>
        <div class="slot">
          <div class="slot-name">adjective</div>
          <div class="slot-value" id="slot-adjective">&mdash;</div>
        </div>
      </div>
      <div class="output-box" id="out-positional">&mdash;</div>
    </div>

    <!-- SECTION 2: Default parameters -->
    <div class="section-card">
      <h2>Default Parameters <span class="tag tag-green">Fallback Values</span></h2>
      <div class="controls">
        <label>
          name (default: "World")
          <input type="text" id="def-name" placeholder="leave blank for default">
        </label>
        <label>
          punctuation (default: "!")
          <input type="text" id="def-punct" placeholder="leave blank for default">
        </label>
        <button class="run-btn" id="run-defaults">Run</button>
      </div>
      <div class="param-slots">
        <div class="slot">
          <div class="slot-name">name</div>
          <div class="slot-value" id="slot-def-name">&mdash;</div>
        </div>
        <div class="slot">
          <div class="slot-name">punctuation</div>
          <div class="slot-value" id="slot-def-punct">&mdash;</div>
        </div>
      </div>
      <div class="output-box" id="out-defaults">&mdash;</div>
    </div>

    <!-- SECTION 3: Rest parameters -->
    <div class="section-card">
      <h2>Rest Parameters <span class="tag tag-purple">...collects the rest</span></h2>
      <div class="controls">
        <label>
          Numbers (comma-separated)
          <input type="text" id="rest-nums" value="10, 20, 30, 5, 15">
        </label>
        <button class="run-btn" id="run-rest">Run</button>
      </div>
      <div class="param-slots" id="slots-rest">
        <!-- populated by JS -->
      </div>
      <div class="output-box" id="out-rest">&mdash;</div>
    </div>

    <!-- SECTION 4: Guard clause -->
    <div class="section-card">
      <h2>Guard Clause (Early Return) <span class="tag tag-orange">Precondition Check</span></h2>
      <div class="guard-demo">
        <p style="font-size:0.85rem; color:#475569; line-height:1.6;">
          This function divides two numbers. Guard clauses catch bad input <em>before</em> the main logic runs.
        </p>
        <div class="guard-input-row">
          <label>
            dividend
            <input type="number" id="guard-a" value="100">
          </label>
          <label>
            divisor
            <input type="number" id="guard-b" value="4">
          </label>
          <button class="run-btn" id="run-guard">Run</button>
        </div>
        <div class="guard-result" id="guard-result">Result will appear here</div>
      </div>
    </div>

  </div>

</body>
</html>
```

**CSS**
```css
/* All styles are inside the <style> block in the HTML above. */
```

**JS**
```js
// ============================================================
// SECTION 1 — Positional Arguments
// ============================================================
function describe(subject, adjective) {
  return subject + ' is ' + adjective;
}

document.getElementById('run-positional').addEventListener('click', () => {
  const subject   = document.getElementById('arg-subject').value;
  const adjective = document.getElementById('arg-adjective').value;

  const slotSubject   = document.getElementById('slot-subject');
  const slotAdjective = document.getElementById('slot-adjective');
  const output        = document.getElementById('out-positional');

  slotSubject.textContent = JSON.stringify(subject);
  slotSubject.className   = 'slot-value received';

  if (adjective === '') {
    // Simulating a call with too few args: describe(subject)
    slotAdjective.textContent = 'undefined';
    slotAdjective.className   = 'slot-value undef';
    output.textContent = `describe("${subject}") → "${describe(subject)}"`;
    output.textContent += '\n⚠ adjective was not provided — received undefined';
  } else {
    slotAdjective.textContent = JSON.stringify(adjective);
    slotAdjective.className   = 'slot-value received';
    output.textContent = `describe("${subject}", "${adjective}") → "${describe(subject, adjective)}"`;
  }
});

// ============================================================
// SECTION 2 — Default Parameters
// ============================================================
function greet(name = 'World', punctuation = '!') {
  return 'Hello, ' + name + punctuation;
}

document.getElementById('run-defaults').addEventListener('click', () => {
  const rawName  = document.getElementById('def-name').value;
  const rawPunct = document.getElementById('def-punct').value;

  // Treat blank input as "not provided" (undefined triggers the default)
  const nameArg  = rawName  === '' ? undefined : rawName;
  const punctArg = rawPunct === '' ? undefined : rawPunct;

  const slotName  = document.getElementById('slot-def-name');
  const slotPunct = document.getElementById('slot-def-punct');
  const output    = document.getElementById('out-defaults');

  if (nameArg === undefined) {
    slotName.textContent = '"World" (default)';
    slotName.className   = 'slot-value defaulted';
  } else {
    slotName.textContent = JSON.stringify(nameArg);
    slotName.className   = 'slot-value received';
  }

  if (punctArg === undefined) {
    slotPunct.textContent = '"!" (default)';
    slotPunct.className   = 'slot-value defaulted';
  } else {
    slotPunct.textContent = JSON.stringify(punctArg);
    slotPunct.className   = 'slot-value received';
  }

  const result = greet(nameArg, punctArg);
  output.textContent = `greet(${nameArg !== undefined ? '"' + nameArg + '"' : ''}, ${punctArg !== undefined ? '"' + punctArg + '"' : ''}) → "${result}"`;
});

// ============================================================
// SECTION 3 — Rest Parameters
// ============================================================
function sumAll(...numbers) {
  const total = numbers.reduce((acc, n) => acc + n, 0);
  return { numbers, total };
}

document.getElementById('run-rest').addEventListener('click', () => {
  const raw    = document.getElementById('rest-nums').value;
  const nums   = raw.split(',').map(s => Number(s.trim())).filter(n => !isNaN(n));
  const slotsEl = document.getElementById('slots-rest');
  const output  = document.getElementById('out-rest');

  // Build slot display
  slotsEl.innerHTML = '';
  nums.forEach((n, i) => {
    const slot = document.createElement('div');
    slot.className = 'slot';
    slot.innerHTML = `<div class="slot-name">numbers[${i}]</div>
                      <div class="slot-value rest">${n}</div>`;
    slotsEl.appendChild(slot);
  });

  if (nums.length === 0) {
    slotsEl.innerHTML = '<div class="slot"><div class="slot-name">numbers</div><div class="slot-value rest">[] (empty array)</div></div>';
    output.textContent = 'sumAll() → { numbers: [], total: 0 }';
    return;
  }

  const { numbers, total } = sumAll(...nums);
  output.textContent = `sumAll(${nums.join(', ')}) → total: ${total}\n...numbers array: [${numbers.join(', ')}]`;

  console.log('Rest params demo:', { numbers, total });
});

// ============================================================
// SECTION 4 — Guard Clause
// ============================================================
function safeDivide(a, b) {
  // Guard clause 1: check types
  if (typeof a !== 'number' || typeof b !== 'number') {
    return { ok: false, message: 'Both arguments must be numbers.' };
  }
  // Guard clause 2: prevent division by zero
  if (b === 0) {
    return { ok: false, message: 'Cannot divide by zero.' };
  }
  // Happy path — no nested if needed
  return { ok: true, value: a / b };
}

document.getElementById('run-guard').addEventListener('click', () => {
  const a      = Number(document.getElementById('guard-a').value);
  const b      = Number(document.getElementById('guard-b').value);
  const result = document.getElementById('guard-result');
  const res    = safeDivide(a, b);

  if (res.ok) {
    result.textContent = `safeDivide(${a}, ${b}) → ${res.value}`;
    result.className   = 'guard-result guard-ok';
  } else {
    result.textContent = `safeDivide(${a}, ${b}) → Error: ${res.message}`;
    result.className   = 'guard-result guard-fail';
  }
});

// ---- Run all demos on page load ----
document.getElementById('run-positional').click();
document.getElementById('run-defaults').click();
document.getElementById('run-rest').click();
document.getElementById('run-guard').click();
```

---

## CODEPEN 3 — Callbacks in Action

**HTML**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Callbacks in Action</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      padding: 2rem 1rem;
    }

    h1 {
      text-align: center;
      font-size: 1.4rem;
      margin-bottom: 0.35rem;
    }

    .subtitle {
      text-align: center;
      color: #64748b;
      font-size: 0.9rem;
      margin-bottom: 2rem;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      max-width: 900px;
      margin: 0 auto;
    }

    .card {
      background: #1e293b;
      border-radius: 12px;
      padding: 1.5rem;
      border: 1px solid #334155;
    }

    .card h2 {
      font-size: 0.95rem;
      font-weight: 700;
      color: #f1f5f9;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .type-badge {
      font-size: 0.68rem;
      padding: 0.15rem 0.45rem;
      border-radius: 999px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .sync  { background: #1e3a5f; color: #93c5fd; }
    .async { background: #3b2413; color: #fb923c; }
    .event { background: #1a2e1a; color: #86efac; }

    /* Timeline (synchronous callbacks) */
    .timeline {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      margin-bottom: 1rem;
    }

    .timeline-step {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.45rem 0.7rem;
      border-radius: 6px;
      background: #0f172a;
      font-size: 0.82rem;
      opacity: 0.35;
      transition: opacity 0.3s, background 0.3s;
    }

    .timeline-step.active {
      opacity: 1;
      background: #1e3a5f;
    }

    .timeline-step.done {
      opacity: 0.7;
      background: #0f2818;
    }

    .step-num {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: #334155;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.72rem;
      font-weight: 700;
      flex-shrink: 0;
    }

    .timeline-step.active .step-num  { background: #3b82f6; }
    .timeline-step.done   .step-num  { background: #22c55e; }

    .step-label { flex: 1; }
    .step-cb    { font-size: 0.72rem; color: #60a5fa; font-family: monospace; }

    button.action-btn {
      width: 100%;
      padding: 0.6rem;
      background: #3b82f6;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      margin-top: 0.75rem;
    }

    button.action-btn:hover:not(:disabled) { background: #2563eb; }
    button.action-btn:disabled { opacity: 0.5; cursor: not-allowed; }

    /* Async timer demo */
    .timer-display {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.85rem;
      background: #0f172a;
      border-radius: 8px;
      margin-bottom: 0.75rem;
    }

    .timer-bar-wrap {
      flex: 1;
      height: 8px;
      background: #334155;
      border-radius: 4px;
      overflow: hidden;
    }

    .timer-bar {
      height: 100%;
      width: 0%;
      background: #fb923c;
      border-radius: 4px;
      transition: none;
    }

    .timer-label {
      font-size: 0.82rem;
      color: #94a3b8;
      white-space: nowrap;
    }

    .log-box {
      background: #0f172a;
      border-radius: 6px;
      padding: 0.6rem 0.75rem;
      font-size: 0.8rem;
      font-family: monospace;
      min-height: 3.5rem;
      color: #94a3b8;
      line-height: 1.7;
      white-space: pre-wrap;
    }

    .log-line-main   { color: #e2e8f0; }
    .log-line-cb     { color: #60a5fa; }
    .log-line-result { color: #4ade80; }
    .log-line-warn   { color: #fb923c; }

    /* Custom callback runner */
    .runner-input {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      margin-bottom: 0.75rem;
    }

    .runner-input input {
      padding: 0.55rem 0.7rem;
      background: #0f172a;
      border: 1.5px solid #334155;
      border-radius: 6px;
      color: #e2e8f0;
      font-size: 0.9rem;
    }

    .runner-input input:focus {
      outline: none;
      border-color: #6366f1;
    }

    /* Event callback demo */
    .click-zone {
      height: 80px;
      border: 2px dashed #334155;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      color: #64748b;
      cursor: pointer;
      transition: background 0.2s, border-color 0.2s;
      margin-bottom: 0.75rem;
      user-select: none;
    }

    .click-zone:hover {
      background: #1e293b;
      border-color: #4ade80;
      color: #4ade80;
    }

    .click-zone.flash {
      background: #052e16;
      border-color: #22c55e;
      color: #86efac;
    }

    .remove-row {
      display: flex;
      gap: 0.5rem;
    }

    .remove-row button {
      flex: 1;
      padding: 0.5rem;
      border: none;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
    }

    #add-listener-btn   { background: #1e3a5f; color: #93c5fd; }
    #remove-listener-btn { background: #2d0000; color: #fca5a5; }
    #add-listener-btn:hover   { background: #1d4ed8; color: white; }
    #remove-listener-btn:hover { background: #7f1d1d; color: white; }
  </style>
</head>
<body>

  <h1>Callbacks in Action</h1>
  <p class="subtitle">Functions passed to other functions &mdash; the pattern behind everything</p>

  <div class="grid">

    <!-- Card 1: Synchronous callbacks -->
    <div class="card">
      <h2>doTask() calls your callback <span class="type-badge sync">Synchronous</span></h2>

      <div class="timeline" id="sync-timeline">
        <div class="timeline-step" id="step-0">
          <div class="step-num">1</div>
          <span class="step-label">doTask() starts</span>
        </div>
        <div class="timeline-step" id="step-1">
          <div class="step-num">2</div>
          <div>
            <div class="step-label">Work happens inside doTask()</div>
          </div>
        </div>
        <div class="timeline-step" id="step-2">
          <div class="step-num">3</div>
          <div>
            <div class="step-label">doTask() calls your callback</div>
            <div class="step-cb">callback("Task complete")</div>
          </div>
        </div>
        <div class="timeline-step" id="step-3">
          <div class="step-num">4</div>
          <span class="step-label">Your callback code runs</span>
        </div>
      </div>

      <div class="runner-input">
        <input type="text" id="callback-msg" placeholder='Your callback message...' value="I ran after the task finished!">
      </div>

      <div class="log-box" id="sync-log">Click Run to see the sequence.</div>
      <button class="action-btn" id="run-sync">Run doTask()</button>
    </div>

    <!-- Card 2: Async callback (setTimeout) -->
    <div class="card">
      <h2>setTimeout callback <span class="type-badge async">Asynchronous</span></h2>

      <div class="timer-display">
        <div class="timer-bar-wrap">
          <div class="timer-bar" id="timer-bar"></div>
        </div>
        <span class="timer-label" id="timer-label">Ready</span>
      </div>

      <div class="log-box" id="async-log">Click "Start Timer" to begin.</div>
      <button class="action-btn" id="run-async">Start Timer (2s)</button>
    </div>

    <!-- Card 3: Event handlers are callbacks -->
    <div class="card">
      <h2>Event handlers = callbacks <span class="type-badge event">Events</span></h2>

      <div class="click-zone" id="click-zone">
        Click me &mdash; my handler is a callback!
      </div>

      <div class="log-box" id="event-log">Waiting for clicks...</div>

      <div class="remove-row">
        <button id="add-listener-btn">Add listener</button>
        <button id="remove-listener-btn">Remove listener</button>
      </div>
    </div>

  </div>

</body>
</html>
```

**CSS**
```css
/* All styles are inside the <style> block in the HTML above. */
```

**JS**
```js
// ============================================================
// CARD 1 — Synchronous Callbacks: doTask()
// ============================================================

// A function that accepts and calls a callback
function doTask(taskName, callback) {
  // The function does its work, then calls the callback
  const result = `Processed: "${taskName}"`;
  callback(result); // synchronous — callback runs right here, right now
}

const steps = ['step-0', 'step-1', 'step-2', 'step-3'];
let syncRunning = false;

async function animateSync() {
  if (syncRunning) return;
  syncRunning = true;

  const log = document.getElementById('sync-log');
  const msg = document.getElementById('callback-msg').value || 'Callback ran!';
  const btn = document.getElementById('run-sync');
  btn.disabled = true;

  // Reset
  steps.forEach(id => {
    const el = document.getElementById(id);
    el.classList.remove('active', 'done');
  });
  log.textContent = '';

  // Animate step by step
  function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

  function appendLog(text, cls = '') {
    const line = document.createElement('div');
    line.className = cls;
    line.textContent = text;
    log.appendChild(line);
  }

  // Step 0
  document.getElementById('step-0').classList.add('active');
  appendLog('→ doTask("My Task", callback) called', 'log-line-main');
  await wait(700);
  document.getElementById('step-0').classList.replace('active', 'done');

  // Step 1
  document.getElementById('step-1').classList.add('active');
  appendLog('  Working inside doTask()...', 'log-line-main');
  await wait(800);
  document.getElementById('step-1').classList.replace('active', 'done');

  // Step 2
  document.getElementById('step-2').classList.add('active');
  appendLog('  callback("Processed: My Task") called', 'log-line-cb');
  await wait(700);
  document.getElementById('step-2').classList.replace('active', 'done');

  // Step 3 — callback runs
  document.getElementById('step-3').classList.add('active');

  // Actually call the function
  doTask('My Task', function namedOnComplete(result) {
    appendLog(`  ✓ Callback received: "${result}"`, 'log-line-result');
    appendLog(`  ✓ Your message: "${msg}"`, 'log-line-result');
  });

  await wait(300);
  document.getElementById('step-3').classList.replace('active', 'done');

  btn.disabled = false;
  syncRunning = false;
}

document.getElementById('run-sync').addEventListener('click', animateSync);

// ============================================================
// CARD 2 — Asynchronous Callbacks: setTimeout
// ============================================================
let asyncTimer = null;
let asyncRunning = false;

function startTimer() {
  if (asyncRunning) return;
  asyncRunning = true;

  const log    = document.getElementById('async-log');
  const bar    = document.getElementById('timer-bar');
  const label  = document.getElementById('timer-label');
  const btn    = document.getElementById('run-async');

  btn.disabled = true;
  log.textContent = '';
  bar.style.transition = 'none';
  bar.style.width = '0%';
  label.textContent = 'Waiting...';

  function appendLog(text, cls = '') {
    const line = document.createElement('div');
    line.className = cls;
    line.textContent = text;
    log.appendChild(line);
  }

  appendLog('→ setTimeout(callback, 2000) registered', 'log-line-main');
  appendLog('→ Code AFTER setTimeout runs immediately:', 'log-line-main');
  appendLog('  "I run before the callback!"', 'log-line-warn');

  // Animate the bar
  requestAnimationFrame(() => {
    bar.style.transition = 'width 2s linear';
    bar.style.width = '100%';
  });

  let elapsed = 0;
  const tick = setInterval(() => {
    elapsed += 100;
    label.textContent = (elapsed / 1000).toFixed(1) + 's';
  }, 100);

  // The actual asynchronous callback
  asyncTimer = setTimeout(function callbackAfterDelay() {
    clearInterval(tick);
    label.textContent = '2.0s — Done!';
    appendLog('', '');
    appendLog('→ (2 seconds later) callback runs:', 'log-line-cb');
    appendLog('  "I am the delayed callback!"', 'log-line-result');

    btn.disabled = false;
    asyncRunning = false;
    bar.style.transition = 'none';
  }, 2000);
}

document.getElementById('run-async').addEventListener('click', startTimer);

// ============================================================
// CARD 3 — Event Handlers Are Callbacks
// ============================================================
const clickZone = document.getElementById('click-zone');
const eventLog  = document.getElementById('event-log');
let clickCount  = 0;
let listenerActive = true;

// Named callback — can be added and removed
function handleZoneClick(event) {
  clickCount++;

  // Flash the zone
  clickZone.classList.add('flash');
  setTimeout(() => clickZone.classList.remove('flash'), 200);

  const line = document.createElement('div');
  line.className = 'log-line-result';
  line.textContent = `Click #${clickCount} — handleZoneClick() called at ${new Date().toLocaleTimeString()}`;
  eventLog.appendChild(line);
  eventLog.scrollTop = eventLog.scrollHeight;
}

// Add listener initially
clickZone.addEventListener('click', handleZoneClick);

document.getElementById('add-listener-btn').addEventListener('click', () => {
  if (!listenerActive) {
    clickZone.addEventListener('click', handleZoneClick);
    listenerActive = true;

    const line = document.createElement('div');
    line.className = 'log-line-cb';
    line.textContent = '→ addEventListener("click", handleZoneClick) — listener active';
    eventLog.appendChild(line);
  }
});

document.getElementById('remove-listener-btn').addEventListener('click', () => {
  if (listenerActive) {
    // Named callback is required for removal — anonymous callbacks cannot be removed!
    clickZone.removeEventListener('click', handleZoneClick);
    listenerActive = false;

    const line = document.createElement('div');
    line.className = 'log-line-warn';
    line.textContent = '→ removeEventListener("click", handleZoneClick) — listener removed';
    eventLog.appendChild(line);
  }
});

// Log the concept
console.log('=== Callbacks Demo ===');
console.log('handleZoneClick is a named callback function:');
console.log(handleZoneClick);
console.log('It is passed as the second argument to addEventListener —');
console.log('the browser "calls it back" whenever the click event fires.');
console.log('Because it is named, it can also be removed with removeEventListener.');
```

---

## CODEPEN 4 — Closure Counter & Private State

**HTML**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Closures: Private State & Factory Functions</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      padding: 2rem 1rem;
    }

    h1 {
      text-align: center;
      font-size: 1.4rem;
      margin-bottom: 0.35rem;
    }

    .subtitle {
      text-align: center;
      color: #64748b;
      font-size: 0.9rem;
      margin-bottom: 2.5rem;
    }

    /* --- Counters section --- */
    .counters-section h2,
    .theme-section h2 {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #64748b;
      text-align: center;
      margin-bottom: 1.25rem;
    }

    .counters-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      justify-content: center;
      margin-bottom: 2.5rem;
    }

    .counter-card {
      background: #1e293b;
      border-radius: 14px;
      padding: 1.25rem;
      width: 200px;
      border: 1px solid #334155;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.75rem;
    }

    .counter-title {
      font-size: 0.82rem;
      font-weight: 700;
      color: #94a3b8;
      text-align: center;
    }

    .counter-value {
      font-size: 3rem;
      font-weight: 900;
      color: #f1f5f9;
      line-height: 1;
      font-variant-numeric: tabular-nums;
    }

    .counter-detail {
      font-size: 0.72rem;
      color: #475569;
      text-align: center;
    }

    .counter-detail code {
      background: #0f172a;
      padding: 0.1rem 0.3rem;
      border-radius: 3px;
      color: #7dd3fc;
    }

    .counter-btns {
      display: flex;
      gap: 0.4rem;
    }

    .counter-btn {
      width: 38px;
      height: 38px;
      border-radius: 8px;
      border: none;
      font-size: 1.3rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.1s;
    }

    .counter-btn:active { transform: scale(0.93); }

    .btn-dec  { background: #1e3a5f; color: #60a5fa; }
    .btn-inc  { background: #052e16; color: #4ade80; }
    .btn-reset { background: #2d1b00; color: #fbbf24; font-size: 0.85rem; }

    .btn-dec:hover   { background: #1d4ed8; color: white; }
    .btn-inc:hover   { background: #166534; color: white; }
    .btn-reset:hover { background: #78350f; color: white; }

    .privacy-note {
      text-align: center;
      font-size: 0.8rem;
      color: #475569;
      margin-bottom: 2rem;
      font-style: italic;
    }

    .privacy-note code {
      background: #1e293b;
      padding: 0.1rem 0.35rem;
      border-radius: 3px;
      color: #f87171;
      font-style: normal;
    }

    /* --- Color theme section --- */
    .theme-section {
      max-width: 520px;
      margin: 0 auto;
    }

    .theme-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      justify-content: center;
      margin-bottom: 1rem;
    }

    .theme-card {
      border-radius: 12px;
      overflow: hidden;
      width: 120px;
      border: 1px solid #334155;
      cursor: pointer;
      transition: transform 0.15s, box-shadow 0.15s;
    }

    .theme-card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.4); }

    .theme-preview {
      height: 60px;
      display: flex;
      gap: 2px;
    }

    .theme-swatch {
      flex: 1;
    }

    .theme-label {
      background: #1e293b;
      padding: 0.4rem;
      text-align: center;
      font-size: 0.72rem;
      color: #94a3b8;
      font-weight: 600;
    }

    .theme-hue-label {
      font-size: 0.7rem;
      color: #475569;
    }

    .active-theme-display {
      background: #1e293b;
      border-radius: 10px;
      padding: 1rem;
      text-align: center;
      border: 1px solid #334155;
    }

    .active-theme-bar {
      height: 36px;
      border-radius: 6px;
      margin-bottom: 0.6rem;
      transition: background 0.4s;
    }

    .active-theme-name {
      font-size: 0.85rem;
      color: #94a3b8;
      margin-bottom: 0.25rem;
    }

    .active-theme-values {
      font-size: 0.78rem;
      font-family: monospace;
      color: #64748b;
    }

    /* Closure explanation box */
    .explanation {
      max-width: 640px;
      margin: 2rem auto 0;
      background: #1e293b;
      border-radius: 10px;
      padding: 1.25rem;
      border: 1px solid #334155;
    }

    .explanation h3 {
      font-size: 0.85rem;
      color: #60a5fa;
      margin-bottom: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .explanation pre {
      background: #0f172a;
      border-radius: 6px;
      padding: 0.85rem;
      font-size: 0.78rem;
      line-height: 1.65;
      overflow-x: auto;
      color: #e2e8f0;
    }

    .kw  { color: #c084fc; }
    .fn  { color: #60a5fa; }
    .cm  { color: #475569; font-style: italic; }
    .str { color: #4ade80; }
  </style>
</head>
<body>

  <h1>Closures: Private State</h1>
  <p class="subtitle">Each counter and theme generator has its own isolated memory &mdash; that's a closure</p>

  <div class="counters-section">
    <h2>Independent Counters (each has private <code>count</code>)</h2>
    <div class="counters-grid" id="counters-grid">
      <!-- Populated by JS -->
    </div>
    <p class="privacy-note">
      Try: <code>counterA.count</code> in the console &rarr; undefined. The variable is truly private.
    </p>
  </div>

  <div class="theme-section">
    <h2>Color Theme Generator (each theme remembers its hue)</h2>
    <div class="theme-grid" id="theme-grid">
      <!-- Populated by JS -->
    </div>
    <div class="active-theme-display">
      <div class="active-theme-bar" id="active-bar"></div>
      <div class="active-theme-name" id="active-name">Click a theme card</div>
      <div class="active-theme-values" id="active-values"></div>
    </div>
  </div>

  <div class="explanation">
    <h3>How the Closure Works</h3>
    <pre><span class="kw">function</span> <span class="fn">createCounter</span>(start = 0, step = 1) {
  <span class="kw">let</span> count = start; <span class="cm">// &larr; private state, lives in the closure</span>

  <span class="kw">return</span> {
    increment() { count += step; <span class="kw">return</span> count; },
    decrement() { count -= step; <span class="kw">return</span> count; },
    reset()     { count = start; <span class="kw">return</span> count; },
    value()     { <span class="kw">return</span> count; }
  };
}

<span class="cm">// Each call creates a NEW closure with its OWN private count</span>
<span class="kw">const</span> counterA = createCounter(0, 1);  <span class="cm">// count = 0, step = 1</span>
<span class="kw">const</span> counterB = createCounter(100, 5); <span class="cm">// count = 100, step = 5</span>

<span class="cm">// They are completely independent:</span>
counterA.increment(); <span class="cm">// 1</span>
counterB.increment(); <span class="cm">// 105 — counterB's count, unaffected by A</span></pre>
  </div>

</body>
</html>
```

**CSS**
```css
/* All styles are inside the <style> block in the HTML above. */
```

**JS**
```js
// ============================================================
// FACTORY FUNCTION — createCounter
// This is the closure: each call creates a new scope with
// its own private `count` variable.
// ============================================================
function createCounter(label, start = 0, step = 1) {
  let count = start; // private — inaccessible from outside

  return {
    increment() { count += step; return count; },
    decrement() { count -= step; return count; },
    reset()     { count = start; return count; },
    value()     { return count; },
    label, start, step
  };
}

// Create three independent counters
const counterConfigs = [
  { label: 'Counter A', start: 0,   step: 1,  id: 'counterA' },
  { label: 'Counter B', start: 100, step: 5,  id: 'counterB' },
  { label: 'Counter C', start: 0,   step: 10, id: 'counterC' },
];

const counters = {};
const grid = document.getElementById('counters-grid');

counterConfigs.forEach(cfg => {
  const counter = createCounter(cfg.label, cfg.start, cfg.step);
  counters[cfg.id] = counter;

  // Build card DOM
  const card = document.createElement('div');
  card.className = 'counter-card';
  card.innerHTML = `
    <div class="counter-title">${cfg.label}</div>
    <div class="counter-value" id="val-${cfg.id}">${cfg.start}</div>
    <div class="counter-detail">
      start: <code>${cfg.start}</code>&nbsp;&nbsp;step: <code>${cfg.step}</code>
    </div>
    <div class="counter-btns">
      <button class="counter-btn btn-dec"  data-id="${cfg.id}" data-action="dec">−</button>
      <button class="counter-btn btn-reset" data-id="${cfg.id}" data-action="reset">↺</button>
      <button class="counter-btn btn-inc"  data-id="${cfg.id}" data-action="inc">+</button>
    </div>
  `;
  grid.appendChild(card);
});

// Delegate events
grid.addEventListener('click', e => {
  const btn = e.target.closest('[data-action]');
  if (!btn) return;

  const { id, action } = btn.dataset;
  const counter = counters[id];
  let newVal;

  if (action === 'inc')   newVal = counter.increment();
  if (action === 'dec')   newVal = counter.decrement();
  if (action === 'reset') newVal = counter.reset();

  document.getElementById(`val-${id}`).textContent = newVal;

  console.log(`${id}.${action}() → ${newVal} (private count inside closure)`);
});

// Demonstrate privacy in console
window.counterA = counters.counterA;
window.counterB = counters.counterB;
window.counterC = counters.counterC;
console.log('=== Closure Demo ===');
console.log('counterA is available as window.counterA');
console.log('Try: counterA.count   → undefined (private!)');
console.log('Try: counterA.value() → shows the count through the public API');

// ============================================================
// FACTORY FUNCTION — createColorTheme
// Another closure: each theme generator remembers its baseHue
// ============================================================
function createColorTheme(name, baseHue) {
  // baseHue is private — remembered in the closure
  function hsl(h, s, l) {
    return `hsl(${h}, ${s}%, ${l}%)`;
  }

  return {
    name,
    baseHue, // expose for display purposes
    primary()   { return hsl(baseHue, 70, 55); },
    light()     { return hsl(baseHue, 60, 80); },
    dark()      { return hsl(baseHue, 70, 30); },
    accent()    { return hsl((baseHue + 180) % 360, 65, 55); },
    swatches()  { return [this.dark(), this.primary(), this.light(), this.accent()]; }
  };
}

const themes = [
  createColorTheme('Ocean',   210),
  createColorTheme('Forest',  130),
  createColorTheme('Sunset',  20),
  createColorTheme('Violet',  270),
  createColorTheme('Rose',    340),
];

const themeGrid = document.getElementById('theme-grid');
const activeBar    = document.getElementById('active-bar');
const activeName   = document.getElementById('active-name');
const activeValues = document.getElementById('active-values');

function selectTheme(theme) {
  activeBar.style.background =
    `linear-gradient(to right, ${theme.dark()}, ${theme.primary()}, ${theme.light()})`;
  activeName.textContent = `${theme.name} Theme (baseHue: ${theme.baseHue}°)`;
  activeValues.textContent =
    `primary: ${theme.primary()}  |  light: ${theme.light()}  |  dark: ${theme.dark()}  |  accent: ${theme.accent()}`;
}

themes.forEach(theme => {
  const card = document.createElement('div');
  card.className = 'theme-card';

  const preview = document.createElement('div');
  preview.className = 'theme-preview';
  theme.swatches().forEach(color => {
    const swatch = document.createElement('div');
    swatch.className = 'theme-swatch';
    swatch.style.background = color;
    preview.appendChild(swatch);
  });

  const label = document.createElement('div');
  label.className = 'theme-label';
  label.innerHTML = `${theme.name}<br><span class="theme-hue-label">${theme.baseHue}°</span>`;

  card.appendChild(preview);
  card.appendChild(label);
  card.addEventListener('click', () => selectTheme(theme));
  themeGrid.appendChild(card);
});

// Select first theme by default
selectTheme(themes[0]);

console.log('=== Color Theme Closures ===');
themes.forEach(t => {
  console.log(`${t.name} (hue ${t.baseHue}°): primary=${t.primary()}`);
});
```

---

## CODEPEN 5 — Scope Explorer

**HTML**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Scope Explorer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      padding: 2rem 1rem;
    }

    h1 {
      text-align: center;
      font-size: 1.4rem;
      margin-bottom: 0.35rem;
    }

    .subtitle {
      text-align: center;
      color: #64748b;
      font-size: 0.9rem;
      margin-bottom: 2rem;
    }

    .layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      max-width: 900px;
      margin: 0 auto;
    }

    @media (max-width: 640px) { .layout { grid-template-columns: 1fr; } }

    /* Scope zone visualization */
    .scope-map {
      position: relative;
    }

    .scope-map h2 {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      color: #64748b;
      margin-bottom: 0.75rem;
    }

    .zone {
      border-radius: 10px;
      padding: 1rem;
      position: relative;
    }

    .zone-global {
      background: rgba(30, 58, 138, 0.25);
      border: 2px solid #1e3a8a;
    }

    .zone-function {
      background: rgba(20, 83, 45, 0.3);
      border: 2px solid #166534;
      margin-top: 0.75rem;
    }

    .zone-block {
      background: rgba(76, 29, 149, 0.3);
      border: 2px solid #6b21a8;
      margin-top: 0.75rem;
    }

    .zone-label {
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .zone-global   .zone-label { color: #93c5fd; }
    .zone-function .zone-label { color: #86efac; }
    .zone-block    .zone-label { color: #d8b4fe; }

    .dot {
      width: 8px; height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }

    .dot-global   { background: #3b82f6; }
    .dot-function { background: #22c55e; }
    .dot-block    { background: #a855f7; }

    .var-list {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }

    .var-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      padding: 0.3rem 0.5rem;
      background: rgba(0,0,0,0.25);
      border-radius: 5px;
      cursor: pointer;
      transition: background 0.15s;
    }

    .var-item:hover { background: rgba(255,255,255,0.07); }

    .var-item.highlighted {
      outline: 2px solid #fbbf24;
    }

    .var-name {
      font-family: monospace;
      font-weight: 700;
    }

    .var-global   .var-name { color: #93c5fd; }
    .var-function .var-name { color: #86efac; }
    .var-block    .var-name { color: #d8b4fe; }

    .var-val {
      font-family: monospace;
      color: #94a3b8;
      font-size: 0.75rem;
    }

    .scope-badge {
      margin-left: auto;
      font-size: 0.65rem;
      padding: 0.1rem 0.35rem;
      border-radius: 999px;
      font-weight: 600;
    }

    .badge-global   { background: #1e3a8a; color: #93c5fd; }
    .badge-function { background: #14532d; color: #86efac; }
    .badge-block    { background: #4c1d95; color: #d8b4fe; }

    /* Interactive panel */
    .interactive {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .interactive h2 {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      color: #64748b;
    }

    .lookup-card {
      background: #1e293b;
      border-radius: 10px;
      padding: 1.25rem;
      border: 1px solid #334155;
    }

    .lookup-card h3 {
      font-size: 0.85rem;
      color: #f1f5f9;
      margin-bottom: 0.75rem;
    }

    .lookup-row {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }

    .lookup-row select,
    .lookup-row input {
      padding: 0.5rem 0.65rem;
      background: #0f172a;
      border: 1.5px solid #334155;
      border-radius: 6px;
      color: #e2e8f0;
      font-size: 0.88rem;
    }

    .lookup-row select:focus,
    .lookup-row input:focus {
      outline: none;
      border-color: #6366f1;
    }

    .lookup-row button {
      padding: 0.5rem 1rem;
      background: #6366f1;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
    }

    .lookup-row button:hover { background: #4f46e5; }

    .chain-display {
      display: flex;
      flex-direction: column;
      gap: 0.3rem;
    }

    .chain-step {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.78rem;
      padding: 0.35rem 0.6rem;
      border-radius: 5px;
      opacity: 0;
      transform: translateX(-8px);
      transition: opacity 0.25s, transform 0.25s;
    }

    .chain-step.visible {
      opacity: 1;
      transform: translateX(0);
    }

    .chain-step.found    { background: #052e16; border-left: 3px solid #22c55e; }
    .chain-step.notfound { background: #2d0000; border-left: 3px solid #dc2626; }
    .chain-step.searching { background: #1e293b; border-left: 3px solid #475569; }

    .chain-icon { font-size: 0.9rem; }

    /* Shadow demo */
    .shadow-demo {
      background: #1e293b;
      border-radius: 10px;
      padding: 1.25rem;
      border: 1px solid #334155;
    }

    .shadow-demo h3 {
      font-size: 0.85rem;
      color: #f1f5f9;
      margin-bottom: 0.75rem;
    }

    .shadow-boxes {
      display: flex;
      gap: 0.6rem;
      flex-wrap: wrap;
      margin-bottom: 0.75rem;
    }

    .shadow-box {
      flex: 1;
      min-width: 120px;
      padding: 0.65rem;
      border-radius: 8px;
      font-size: 0.78rem;
      font-family: monospace;
      line-height: 1.6;
    }

    .shadow-global-box   { background: #1e3a5f; border: 1px solid #1e40af; }
    .shadow-function-box { background: #14532d; border: 1px solid #166534; }

    .shadow-box .label {
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.4rem;
      font-style: normal;
    }

    .shadow-global-box   .label { color: #93c5fd; }
    .shadow-function-box .label { color: #86efac; }

    .run-shadow-btn {
      padding: 0.5rem 1rem;
      background: #a855f7;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
    }

    .run-shadow-btn:hover { background: #9333ea; }

    .shadow-output {
      margin-top: 0.6rem;
      background: #0f172a;
      border-radius: 6px;
      padding: 0.6rem 0.75rem;
      font-family: monospace;
      font-size: 0.8rem;
      line-height: 1.7;
      min-height: 2rem;
      color: #94a3b8;
    }

    .out-global   { color: #93c5fd; }
    .out-function { color: #86efac; }
    .out-warn     { color: #fb923c; }
  </style>
</head>
<body>

  <h1>Scope Explorer</h1>
  <p class="subtitle">See where variables live and how JavaScript finds them</p>

  <div class="layout">

    <!-- LEFT: Scope zone map -->
    <div class="scope-map">
      <h2>Scope Zone Map</h2>
      <div class="zone zone-global">
        <div class="zone-label"><span class="dot dot-global"></span>Global Scope</div>
        <div class="var-list">
          <div class="var-item var-global" data-var="appName" data-scope="global">
            <span class="var-name">appName</span>
            <span class="var-val">= "ScopeDemo"</span>
            <span class="scope-badge badge-global">global</span>
          </div>
          <div class="var-item var-global" data-var="version" data-scope="global">
            <span class="var-name">version</span>
            <span class="var-val">= 3</span>
            <span class="scope-badge badge-global">global</span>
          </div>
          <div class="var-item var-global" data-var="status" data-scope="global">
            <span class="var-name">status</span>
            <span class="var-val">= "global"</span>
            <span class="scope-badge badge-global">global</span>
          </div>
        </div>

        <div class="zone zone-function">
          <div class="zone-label"><span class="dot dot-function"></span>Function Scope (inside checkStatus)</div>
          <div class="var-list">
            <div class="var-item var-function" data-var="status" data-scope="function">
              <span class="var-name">status</span>
              <span class="var-val">= "local" (shadows global!)</span>
              <span class="scope-badge badge-function">function</span>
            </div>
            <div class="var-item var-function" data-var="message" data-scope="function">
              <span class="var-name">message</span>
              <span class="var-val">= "I am local"</span>
              <span class="scope-badge badge-function">function</span>
            </div>

            <div class="zone zone-block">
              <div class="zone-label"><span class="dot dot-block"></span>Block Scope (inside if block)</div>
              <div class="var-list">
                <div class="var-item var-block" data-var="blockOnly" data-scope="block">
                  <span class="var-name">blockOnly</span>
                  <span class="var-val">= "I live here only"</span>
                  <span class="scope-badge badge-block">block</span>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>

    <!-- RIGHT: Interactive tools -->
    <div class="interactive">
      <h2>Interactive Tools</h2>

      <!-- Scope chain lookup -->
      <div class="lookup-card">
        <h3>Scope Chain Lookup</h3>
        <p style="font-size:0.78rem; color:#64748b; margin-bottom:0.6rem; line-height:1.5;">
          Pick a variable and a starting scope. Watch JavaScript walk the chain to find it.
        </p>
        <div class="lookup-row">
          <select id="lookup-var">
            <option value="blockOnly">blockOnly</option>
            <option value="message">message</option>
            <option value="status">status</option>
            <option value="appName">appName</option>
            <option value="version">version</option>
            <option value="notDefined">notDefined</option>
          </select>
          <select id="lookup-from">
            <option value="block">From: block scope</option>
            <option value="function">From: function scope</option>
            <option value="global">From: global scope</option>
          </select>
          <button id="run-lookup">Look up</button>
        </div>
        <div class="chain-display" id="chain-display">
          <!-- Steps populated by JS -->
        </div>
      </div>

      <!-- Shadowing demo -->
      <div class="shadow-demo">
        <h3>Variable Shadowing</h3>
        <div class="shadow-boxes">
          <div class="shadow-box shadow-global-box">
            <div class="label">Global Scope</div>
            <code>const status = "global"</code>
          </div>
          <div class="shadow-box shadow-function-box">
            <div class="label">Function Scope</div>
            <code>const status = "local"</code><br>
            <span style="color:#475569; font-size:0.7rem">(shadows global)</span>
          </div>
        </div>
        <button class="run-shadow-btn" id="run-shadow">Run Shadow Demo</button>
        <div class="shadow-output" id="shadow-output">Output will appear here</div>
      </div>

    </div>
  </div>

</body>
</html>
```

**CSS**
```css
/* All styles are inside the <style> block in the HTML above. */
```

**JS**
```js
// ============================================================
// The actual variables that match the scope map visualization
// ============================================================

// --- Global scope ---
const appName = 'ScopeDemo';
const version = 3;
const status  = 'global'; // will be shadowed inside the function

// --- Function scope (simulated for the demo) ---
function checkStatus() {
  const status  = 'local';     // shadows the global "status"
  const message = 'I am local'; // only exists in this function

  if (true) {
    const blockOnly = 'I live here only'; // only exists in this block
    console.log('From block scope:');
    console.log('  blockOnly:', blockOnly); // found here
    console.log('  message:', message);     // found in function scope (outer)
    console.log('  status:', status);       // found in function scope — "local" (shadow)
    console.log('  appName:', appName);     // found in global scope (chain goes up)
  }

  // blockOnly is not accessible here
  try {
    console.log(blockOnly);
  } catch (e) {
    console.log('blockOnly from function scope: ReferenceError —', e.message);
  }

  return { status, message };
}

// ============================================================
// Scope chain lookup simulation
// ============================================================

// Defines what variables exist at each scope level in this demo
const scopeChain = [
  {
    name: 'block scope',
    color: '#a855f7',
    vars: { blockOnly: '"I live here only"' }
  },
  {
    name: 'function scope (checkStatus)',
    color: '#22c55e',
    vars: { status: '"local"', message: '"I am local"' }
  },
  {
    name: 'global scope',
    color: '#3b82f6',
    vars: { appName: '"ScopeDemo"', version: '3', status: '"global"' }
  }
];

const fromOrder = { block: 0, function: 1, global: 2 };

function runScopeChainLookup() {
  const varName  = document.getElementById('lookup-var').value;
  const fromKey  = document.getElementById('lookup-from').value;
  const display  = document.getElementById('chain-display');

  display.innerHTML = '';

  const startIndex = fromOrder[fromKey];
  const chain      = scopeChain.slice(startIndex); // only look outward from start

  let found = false;
  const steps = [];

  for (let i = 0; i < chain.length; i++) {
    const scope = chain[i];
    if (scope.vars[varName] !== undefined) {
      steps.push({ scope, varName, result: scope.vars[varName], type: 'found' });
      found = true;
      break;
    } else {
      steps.push({ scope, varName, result: null, type: 'notfound-step' });
    }
  }

  if (!found) {
    steps.push({ type: 'error', varName });
  }

  // Animate each step
  steps.forEach((step, i) => {
    setTimeout(() => {
      const el = document.createElement('div');

      if (step.type === 'found') {
        el.className = 'chain-step found';
        el.innerHTML = `
          <span class="chain-icon">✓</span>
          <span>Found <strong style="color:#86efac; font-family:monospace">${step.varName}</strong>
          in <strong>${step.scope.name}</strong>:
          <span style="font-family:monospace; color:#fbbf24">${step.result}</span></span>
        `;
      } else if (step.type === 'notfound-step') {
        el.className = 'chain-step searching';
        el.innerHTML = `
          <span class="chain-icon">→</span>
          <span><strong style="font-family:monospace; color:#f87171">${step.varName}</strong>
          not in <strong>${step.scope.name}</strong>, looking outward...</span>
        `;
      } else {
        el.className = 'chain-step notfound';
        el.innerHTML = `
          <span class="chain-icon">✗</span>
          <span><strong style="font-family:monospace; color:#f87171">${step.varName}</strong>
          not found in any scope &mdash;
          <strong>ReferenceError: ${step.varName} is not defined</strong></span>
        `;
      }

      display.appendChild(el);
      // Trigger animation
      requestAnimationFrame(() => {
        requestAnimationFrame(() => el.classList.add('visible'));
      });

      // Highlight the matching var item in the map
      if (step.type === 'found') {
        document.querySelectorAll('.var-item').forEach(el2 => el2.classList.remove('highlighted'));
        const match = document.querySelector(
          `.var-item[data-var="${step.varName}"][data-scope="${step.scope.name.includes('block') ? 'block' : step.scope.name.includes('function') ? 'function' : 'global'}"]`
        );
        if (match) match.classList.add('highlighted');
      }
    }, i * 400);
  });
}

document.getElementById('run-lookup').addEventListener('click', runScopeChainLookup);

// ============================================================
// Variable shadowing demo
// ============================================================
document.getElementById('run-shadow').addEventListener('click', () => {
  const output = document.getElementById('shadow-output');
  output.innerHTML = '';

  function appendLine(text, cls = '') {
    const line = document.createElement('div');
    line.className = cls;
    line.textContent = text;
    output.appendChild(line);
  }

  // Global status
  appendLine(`Global scope → status = "${status}"`, 'out-global');

  // Inside function — status is shadowed
  (function checkStatus() {
    const status = 'local'; // shadows global

    appendLine(`Function scope → status = "${status}"`, 'out-function');
    appendLine('  (the global "status" is hidden from here)', 'out-warn');

    if (true) {
      const blockOnly = 'block-level value';
      appendLine(`Block scope → blockOnly = "${blockOnly}"`, 'out-function');
    }
  })();

  // Back in global scope — status is unchanged
  appendLine(`Back in global scope → status = "${status}" (unchanged)`, 'out-global');
  appendLine('The function never modified the global status — it created its own.', 'out-warn');

  console.log('=== Shadowing Demo ===');
  console.log('Global status:', status);
  const funcResult = checkStatus();
  console.log('checkStatus() returned:', funcResult);
  console.log('Global status after calling checkStatus:', status, '(unchanged)');
});

// ============================================================
// Console demonstrations
// ============================================================
console.log('=== Scope Explorer ===');
console.log('Global variables accessible here:');
console.log('  appName:', appName);
console.log('  version:', version);
console.log('  status:', status);
console.log('');
console.log('Running checkStatus() to demonstrate function scope:');
const result = checkStatus();
console.log('Return value:', result);
console.log('Global status after call:', status, '— still "global"!');

// Demonstrate block scope
{
  const blockDemo = 'I am block-scoped';
  console.log('Inside block:', blockDemo);
}
// console.log(blockDemo); // would throw ReferenceError
console.log('blockDemo after block — would throw ReferenceError if accessed here');
```
