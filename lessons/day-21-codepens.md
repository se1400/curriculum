# Day 21 — Control Flow: CodePen Code Blocks

Each numbered section corresponds to the `[CODEPEN #]` placeholder in the article.

---

## CODEPEN 1 — Interactive if/else Decision Tree

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>if/else Decision Tree</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem 1rem;
    }

    h1 {
      font-size: 1.5rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
      color: #f8fafc;
    }

    .subtitle {
      font-size: 0.9rem;
      color: #94a3b8;
      margin-bottom: 2rem;
      text-align: center;
    }

    .card {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 1.5rem;
      width: 100%;
      max-width: 560px;
      margin-bottom: 1.25rem;
    }

    .card h2 {
      font-size: 1rem;
      font-weight: 600;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 1rem;
    }

    .field {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      margin-bottom: 1rem;
    }

    label {
      font-size: 0.85rem;
      font-weight: 500;
      color: #cbd5e1;
    }

    input[type="text"],
    input[type="number"],
    select {
      width: 100%;
      padding: 0.6rem 0.8rem;
      background: #0f172a;
      border: 1px solid #475569;
      border-radius: 8px;
      color: #f1f5f9;
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.2s;
    }

    input:focus, select:focus {
      border-color: #6366f1;
    }

    button {
      width: 100%;
      padding: 0.75rem;
      background: #6366f1;
      color: #fff;
      border: none;
      border-radius: 8px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s;
    }

    button:hover { background: #4f46e5; }

    /* Result panel */
    .result-panel {
      width: 100%;
      max-width: 560px;
      border-radius: 12px;
      padding: 1.25rem 1.5rem;
      border: 1px solid #334155;
      background: #1e293b;
      display: none;
    }

    .result-panel.show { display: block; }

    .result-panel h2 {
      font-size: 1rem;
      font-weight: 600;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.75rem;
    }

    .verdict {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 1rem;
      padding: 0.75rem 1rem;
      border-radius: 8px;
    }

    .verdict.success { background: #052e16; color: #4ade80; border: 1px solid #166534; }
    .verdict.warning { background: #1c1917; color: #fbbf24; border: 1px solid #92400e; }
    .verdict.error   { background: #1f0a0a; color: #f87171; border: 1px solid #7f1d1d; }
    .verdict.info    { background: #0c1a2e; color: #60a5fa; border: 1px solid #1e40af; }

    .trace-title {
      font-size: 0.8rem;
      font-weight: 600;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.5rem;
    }

    .trace {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }

    .trace-step {
      font-size: 0.82rem;
      font-family: 'Courier New', monospace;
      padding: 0.3rem 0.6rem;
      border-radius: 4px;
      border-left: 3px solid transparent;
    }

    .trace-step.checked { background: #1a2535; border-left-color: #475569; color: #94a3b8; }
    .trace-step.matched { background: #0a1f12; border-left-color: #22c55e; color: #86efac; font-weight: 600; }
    .trace-step.skipped { background: #0f172a; border-left-color: #1e293b; color: #475569; text-decoration: line-through; }
  </style>
</head>
<body>

  <h1>if/else Decision Tree</h1>
  <p class="subtitle">Fill in the form and see exactly which code path fires.</p>

  <div class="card">
    <h2>Inputs</h2>

    <div class="field">
      <label for="username">Username</label>
      <input type="text" id="username" placeholder="Enter a username (leave blank to test falsy)">
    </div>

    <div class="field">
      <label for="age">Age</label>
      <input type="number" id="age" placeholder="Enter your age" min="0" max="120">
    </div>

    <div class="field">
      <label for="plan">Subscription Plan</label>
      <select id="plan">
        <option value="">-- none selected --</option>
        <option value="free">Free</option>
        <option value="basic">Basic</option>
        <option value="premium">Premium</option>
        <option value="enterprise">Enterprise</option>
      </select>
    </div>

    <button id="evaluateBtn">Evaluate Conditions</button>
  </div>

  <div class="result-panel" id="resultPanel">
    <h2>Result</h2>
    <div class="verdict" id="verdict"></div>
    <div class="trace-title">Code Path Trace</div>
    <div class="trace" id="trace"></div>
  </div>

  <script>
    document.getElementById('evaluateBtn').addEventListener('click', () => {
      const username = document.getElementById('username').value.trim();
      const age      = parseInt(document.getElementById('age').value, 10);
      const plan     = document.getElementById('plan').value;

      const panel  = document.getElementById('resultPanel');
      const verdict = document.getElementById('verdict');
      const trace   = document.getElementById('trace');

      panel.classList.add('show');
      trace.innerHTML = '';

      const steps = [];
      let resultText = '';
      let resultClass = '';

      // Step 1: Check username
      if (!username) {
        steps.push({ text: 'if (!username)  →  true', state: 'matched' });
        resultText  = 'No username entered. Please provide a username to continue.';
        resultClass = 'error';

        // Skip remaining
        steps.push({ text: 'else if (age < 13)  →  skipped', state: 'skipped' });
        steps.push({ text: 'else if (plan === "enterprise")  →  skipped', state: 'skipped' });
        steps.push({ text: 'else if (plan === "premium")  →  skipped', state: 'skipped' });
        steps.push({ text: 'else if (plan === "basic")  →  skipped', state: 'skipped' });
        steps.push({ text: 'else  →  skipped', state: 'skipped' });
      } else {
        steps.push({ text: `if (!username)  →  false  ("${username}" is truthy)`, state: 'checked' });

        // Step 2: Age check
        if (!isNaN(age) && age < 13) {
          steps.push({ text: `else if (age < 13)  →  true  (age is ${age})`, state: 'matched' });
          resultText  = `Sorry, ${username}! You must be at least 13 to use this service.`;
          resultClass = 'warning';
          steps.push({ text: 'else if (plan === "enterprise")  →  skipped', state: 'skipped' });
          steps.push({ text: 'else if (plan === "premium")  →  skipped', state: 'skipped' });
          steps.push({ text: 'else if (plan === "basic")  →  skipped', state: 'skipped' });
          steps.push({ text: 'else  →  skipped', state: 'skipped' });
        } else {
          steps.push({ text: `else if (age < 13)  →  false  (age is ${isNaN(age) ? 'not set' : age})`, state: 'checked' });

          // Step 3: Plan checks
          if (plan === 'enterprise') {
            steps.push({ text: 'else if (plan === "enterprise")  →  true', state: 'matched' });
            resultText  = `Welcome, ${username}! You have full enterprise access with dedicated support.`;
            resultClass = 'success';
            steps.push({ text: 'else if (plan === "premium")  →  skipped', state: 'skipped' });
            steps.push({ text: 'else if (plan === "basic")  →  skipped', state: 'skipped' });
            steps.push({ text: 'else  →  skipped', state: 'skipped' });
          } else if (plan === 'premium') {
            steps.push({ text: 'else if (plan === "enterprise")  →  false', state: 'checked' });
            steps.push({ text: 'else if (plan === "premium")  →  true', state: 'matched' });
            resultText  = `Welcome, ${username}! You have premium access — enjoy all features.`;
            resultClass = 'success';
            steps.push({ text: 'else if (plan === "basic")  →  skipped', state: 'skipped' });
            steps.push({ text: 'else  →  skipped', state: 'skipped' });
          } else if (plan === 'basic') {
            steps.push({ text: 'else if (plan === "enterprise")  →  false', state: 'checked' });
            steps.push({ text: 'else if (plan === "premium")  →  false', state: 'checked' });
            steps.push({ text: 'else if (plan === "basic")  →  true', state: 'matched' });
            resultText  = `Welcome, ${username}! Basic plan is active. Upgrade for more features.`;
            resultClass = 'info';
            steps.push({ text: 'else  →  skipped', state: 'skipped' });
          } else {
            steps.push({ text: 'else if (plan === "enterprise")  →  false', state: 'checked' });
            steps.push({ text: 'else if (plan === "premium")  →  false', state: 'checked' });
            steps.push({ text: 'else if (plan === "basic")  →  false', state: 'checked' });
            steps.push({ text: 'else  →  true  (no plan selected or free)', state: 'matched' });
            resultText  = `Hello, ${username}. You are on the free tier. Select a plan to unlock features.`;
            resultClass = 'warning';
          }
        }
      }

      verdict.textContent = resultText;
      verdict.className   = `verdict ${resultClass}`;

      steps.forEach(step => {
        const div = document.createElement('div');
        div.className = `trace-step ${step.state}`;
        div.textContent = step.text;
        trace.appendChild(div);
      });
    });
  </script>

</body>
</html>
```

---

## CODEPEN 2 — Ternary Operator Builder

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ternary Operator Builder</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      min-height: 100vh;
      padding: 2rem 1rem;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    h1 {
      font-size: 1.5rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
      color: #f8fafc;
      text-align: center;
    }

    .subtitle {
      font-size: 0.9rem;
      color: #94a3b8;
      margin-bottom: 2rem;
      text-align: center;
    }

    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      width: 100%;
      max-width: 800px;
      margin-bottom: 1.25rem;
    }

    @media (max-width: 600px) {
      .grid { grid-template-columns: 1fr; }
    }

    .card {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 1.25rem;
    }

    .card.full-width {
      grid-column: 1 / -1;
    }

    .card h2 {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 1rem;
    }

    .card h2.if-label    { color: #f87171; }
    .card h2.tern-label  { color: #34d399; }
    .card h2.live-label  { color: #a78bfa; }
    .card h2.nest-label  { color: #fbbf24; }

    pre {
      background: #0f172a;
      border-radius: 8px;
      padding: 1rem;
      font-size: 0.8rem;
      font-family: 'Courier New', monospace;
      line-height: 1.7;
      overflow-x: auto;
      color: #cbd5e1;
      white-space: pre-wrap;
    }

    .highlight-branch {
      display: inline;
      border-radius: 3px;
      padding: 0 2px;
    }

    .branch-true  { background: #14532d; color: #4ade80; }
    .branch-false { background: #7f1d1d; color: #fca5a5; }

    .live-section {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .input-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    label {
      font-size: 0.85rem;
      font-weight: 500;
      color: #cbd5e1;
      white-space: nowrap;
    }

    input[type="number"] {
      width: 80px;
      padding: 0.45rem 0.6rem;
      background: #0f172a;
      border: 1px solid #475569;
      border-radius: 6px;
      color: #f1f5f9;
      font-size: 0.9rem;
      outline: none;
      transition: border-color 0.2s;
    }

    input:focus { border-color: #6366f1; }

    .result-row {
      background: #0f172a;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.85rem;
    }

    .result-row span.label {
      color: #64748b;
      display: block;
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.2rem;
    }

    .result-value { font-size: 1rem; font-weight: 700; }
    .result-value.true-branch  { color: #4ade80; }
    .result-value.false-branch { color: #f87171; }

    .bad-example {
      background: #1a1000;
      border: 1px solid #92400e;
      border-radius: 8px;
      padding: 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      line-height: 1.7;
      color: #cbd5e1;
      white-space: pre-wrap;
      position: relative;
    }

    .bad-badge {
      position: absolute;
      top: 0.5rem;
      right: 0.75rem;
      background: #92400e;
      color: #fbbf24;
      font-size: 0.65rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
    }

    .good-example {
      background: #0a1a0a;
      border: 1px solid #166534;
      border-radius: 8px;
      padding: 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      line-height: 1.7;
      color: #cbd5e1;
      white-space: pre-wrap;
      position: relative;
    }

    .good-badge {
      position: absolute;
      top: 0.5rem;
      right: 0.75rem;
      background: #166534;
      color: #4ade80;
      font-size: 0.65rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
    }

    .explain {
      font-size: 0.82rem;
      color: #94a3b8;
      line-height: 1.5;
      margin-top: 0.75rem;
    }
  </style>
</head>
<body>

  <h1>Ternary Operator Builder</h1>
  <p class="subtitle">See if/else and ternary side-by-side. Live input, live results.</p>

  <div class="grid">

    <!-- if/else version -->
    <div class="card">
      <h2 class="if-label">if / else Version</h2>
      <pre id="ifCode">let greeting;
if (hour &lt; 12) {
  greeting = "Good morning";
} else {
  greeting = "Good afternoon";
}</pre>
    </div>

    <!-- ternary version -->
    <div class="card">
      <h2 class="tern-label">Ternary Version</h2>
      <pre id="ternCode">const greeting =
  hour &lt; 12
    ? "Good morning"
    : "Good afternoon";</pre>
    </div>

    <!-- live demo -->
    <div class="card full-width">
      <h2 class="live-label">Live Demo — Change the Hour</h2>
      <div class="live-section">
        <div class="input-row">
          <label for="hourInput">Current hour (0–23):</label>
          <input type="number" id="hourInput" min="0" max="23" value="9">
        </div>
        <div class="result-row">
          <span class="label">Condition: hour &lt; 12</span>
          <div class="result-value" id="condResult"></div>
        </div>
        <div class="result-row">
          <span class="label">Result value</span>
          <div class="result-value" id="greetingResult"></div>
        </div>
        <div class="result-row">
          <span class="label">Active branch</span>
          <div class="result-value" id="branchResult"></div>
        </div>
      </div>
    </div>

    <!-- nested ternary warning -->
    <div class="card full-width">
      <h2 class="nest-label">Nested Ternary — Why You Should Avoid It</h2>
      <div class="bad-example">
        <div class="bad-badge">AVOID</div>
        <span style="color:#fbbf24">// Hard to read — what does this do?</span>
const access = role === "admin"
  ? "full"
  : role === "editor"
    ? "write"
    : role === "viewer"
      ? "read"
      : "none";
      </div>
      <div class="good-example" style="margin-top:0.75rem;">
        <div class="good-badge">PREFER</div>
        <span style="color:#4ade80">// Clear intent — easy to scan</span>
let access;
if (role === "admin")       { access = "full";  }
else if (role === "editor") { access = "write"; }
else if (role === "viewer") { access = "read";  }
else                        { access = "none";  }
      </div>
      <p class="explain">
        Each nesting level in a ternary adds significant cognitive overhead. The if/else chain reads like plain English and is trivial to extend or debug. Linters like ESLint provide a <code>no-nested-ternary</code> rule specifically because nested ternaries cause real bugs.
      </p>
    </div>

  </div>

  <script>
    const hourInput      = document.getElementById('hourInput');
    const condResult     = document.getElementById('condResult');
    const greetingResult = document.getElementById('greetingResult');
    const branchResult   = document.getElementById('branchResult');

    function update() {
      const hour = parseInt(hourInput.value, 10);
      const isMorning = hour < 12;
      const greeting  = isMorning ? "Good morning" : "Good afternoon";

      condResult.textContent   = `hour < 12  →  ${isMorning}`;
      condResult.className     = `result-value ${isMorning ? 'true-branch' : 'false-branch'}`;

      greetingResult.textContent = `"${greeting}"`;
      greetingResult.className   = `result-value ${isMorning ? 'true-branch' : 'false-branch'}`;

      branchResult.textContent = isMorning ? '? branch (truthy)' : ': branch (falsy)';
      branchResult.className   = `result-value ${isMorning ? 'true-branch' : 'false-branch'}`;
    }

    hourInput.addEventListener('input', update);
    update();
  </script>

</body>
</html>
```

---

## CODEPEN 3 — ?? vs || Explorer

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>?? vs || Explorer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      min-height: 100vh;
      padding: 2rem 1rem;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    h1 {
      font-size: 1.5rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
      color: #f8fafc;
      text-align: center;
    }

    .subtitle {
      font-size: 0.9rem;
      color: #94a3b8;
      margin-bottom: 2rem;
      text-align: center;
      max-width: 500px;
    }

    .container {
      width: 100%;
      max-width: 720px;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    /* Truth table */
    .table-card {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 1.25rem;
    }

    .table-card h2 {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #94a3b8;
      margin-bottom: 1rem;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
    }

    th {
      text-align: left;
      padding: 0.5rem 0.75rem;
      background: #0f172a;
      color: #64748b;
      font-weight: 600;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    th:nth-child(1) { border-radius: 8px 0 0 8px; }
    th:last-child   { border-radius: 0 8px 8px 0; }

    td {
      padding: 0.55rem 0.75rem;
      border-bottom: 1px solid #1e293b;
      font-family: 'Courier New', monospace;
      vertical-align: middle;
    }

    tr:last-child td { border-bottom: none; }

    tr:nth-child(odd)  td { background: #131f2e; }
    tr:nth-child(even) td { background: #0f172a; }

    .value-cell {
      color: #e2e8f0;
    }

    .type-badge {
      display: inline-block;
      font-size: 0.68rem;
      padding: 0.1rem 0.35rem;
      border-radius: 3px;
      font-weight: 600;
      margin-left: 0.3rem;
      font-family: system-ui, sans-serif;
    }

    .type-null      { background: #3b0764; color: #c084fc; }
    .type-undefined { background: #1c1917; color: #a8a29e; }
    .type-falsy     { background: #1c0a0a; color: #f87171; }
    .type-truthy    { background: #052e16; color: #4ade80; }

    .result-or   { color: #f59e0b; font-weight: 700; }
    .result-null { color: #a78bfa; font-weight: 700; }

    .same  { color: #4ade80; }
    .diff  { color: #f87171; font-weight: 700; }

    /* Operator legend */
    .legend {
      display: flex;
      gap: 1.5rem;
      flex-wrap: wrap;
    }

    .legend-item {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.82rem;
    }

    .legend-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
    }

    .dot-or   { background: #f59e0b; }
    .dot-null { background: #a78bfa; }

    /* Custom tester */
    .tester-card {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 1.25rem;
    }

    .tester-card h2 {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #94a3b8;
      margin-bottom: 1rem;
    }

    .tester-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
      margin-bottom: 1rem;
    }

    input[type="text"] {
      flex: 1;
      min-width: 140px;
      padding: 0.5rem 0.75rem;
      background: #0f172a;
      border: 1px solid #475569;
      border-radius: 6px;
      color: #f1f5f9;
      font-size: 0.9rem;
      font-family: 'Courier New', monospace;
      outline: none;
      transition: border-color 0.2s;
    }

    input:focus { border-color: #6366f1; }

    .tester-label {
      font-size: 0.85rem;
      color: #94a3b8;
      font-family: 'Courier New', monospace;
      white-space: nowrap;
    }

    .tester-results {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
    }

    .tester-result {
      background: #0f172a;
      border-radius: 8px;
      padding: 0.75rem;
    }

    .tester-result .op {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.35rem;
    }

    .op-or   { color: #f59e0b; }
    .op-null { color: #a78bfa; }

    .tester-result .expression {
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      color: #64748b;
      margin-bottom: 0.25rem;
    }

    .tester-result .output {
      font-family: 'Courier New', monospace;
      font-size: 1rem;
      font-weight: 700;
    }

    .explain-box {
      background: #0c1a2e;
      border: 1px solid #1e40af;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-size: 0.82rem;
      line-height: 1.55;
      color: #93c5fd;
      margin-top: 0.75rem;
    }
  </style>
</head>
<body>

  <h1><code>??</code> vs <code>||</code> Explorer</h1>
  <p class="subtitle">See exactly when nullish coalescing and logical OR produce different results — and why it matters.</p>

  <div class="container">

    <div class="table-card">
      <h2>Truth Table — Right-hand default value is <code>"DEFAULT"</code></h2>
      <div class="legend" style="margin-bottom:0.75rem;">
        <div class="legend-item"><div class="legend-dot dot-or"></div> <code>||</code> result</div>
        <div class="legend-item"><div class="legend-dot dot-null"></div> <code>??</code> result</div>
      </div>
      <table>
        <thead>
          <tr>
            <th>Left-side value</th>
            <th>Type</th>
            <th><code>value || "DEFAULT"</code></th>
            <th><code>value ?? "DEFAULT"</code></th>
            <th>Same?</th>
          </tr>
        </thead>
        <tbody id="tableBody"></tbody>
      </table>
    </div>

    <div class="tester-card">
      <h2>Custom Value Tester</h2>
      <div class="tester-row">
        <label style="font-size:0.85rem; color:#cbd5e1; white-space:nowrap;">Left side:</label>
        <input type="text" id="customInput" placeholder='try: 0, "", false, null, undefined, "hello"' value="0">
        <span class="tester-label"><code>?? / ||</code></span>
        <input type="text" id="defaultInput" placeholder="Default value" value='"fallback"' style="max-width:130px;">
      </div>
      <div class="tester-results">
        <div class="tester-result">
          <div class="op op-or">|| (OR)</div>
          <div class="expression" id="orExpr"></div>
          <div class="output" id="orOutput" style="color:#f59e0b;"></div>
        </div>
        <div class="tester-result">
          <div class="op op-null">?? (Nullish)</div>
          <div class="expression" id="nullExpr"></div>
          <div class="output" id="nullOutput" style="color:#a78bfa;"></div>
        </div>
      </div>
      <div class="explain-box" id="explainBox"></div>
    </div>

  </div>

  <script>
    const tableData = [
      { value: null,      label: 'null',      type: 'null' },
      { value: undefined, label: 'undefined', type: 'undefined' },
      { value: 0,         label: '0',         type: 'falsy' },
      { value: '',        label: '""',        type: 'falsy' },
      { value: false,     label: 'false',     type: 'falsy' },
      { value: NaN,       label: 'NaN',       type: 'falsy' },
      { value: 'hello',   label: '"hello"',   type: 'truthy' },
      { value: 42,        label: '42',        type: 'truthy' },
      { value: true,      label: 'true',      type: 'truthy' },
      { value: [],        label: '[]',        type: 'truthy' },
    ];

    const DEFAULT_VAL = 'DEFAULT';

    const tbody = document.getElementById('tableBody');
    tableData.forEach(row => {
      const orResult   = row.value || DEFAULT_VAL;
      const nullResult = row.value ?? DEFAULT_VAL;
      const same       = String(orResult) === String(nullResult);

      const typeBadgeClass = {
        null: 'type-null', undefined: 'type-undefined',
        falsy: 'type-falsy', truthy: 'type-truthy'
      }[row.type];

      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td class="value-cell"><code>${row.label}</code></td>
        <td><span class="type-badge ${typeBadgeClass}">${row.type}</span></td>
        <td class="result-or"><code>${formatValue(orResult)}</code></td>
        <td class="result-null"><code>${formatValue(nullResult)}</code></td>
        <td class="${same ? 'same' : 'diff'}">${same ? 'yes' : 'DIFFERENT!'}</td>
      `;
      tbody.appendChild(tr);
    });

    function formatValue(v) {
      if (typeof v === 'string') return `"${v}"`;
      return String(v);
    }

    // Custom tester
    const customInput  = document.getElementById('customInput');
    const defaultInput = document.getElementById('defaultInput');

    function runTester() {
      const rawLeft    = customInput.value;
      const rawDefault = defaultInput.value;

      let leftVal, defaultVal, leftLabel, defaultLabel;

      try {
        leftVal   = Function('"use strict"; return (' + rawLeft + ')')();
        leftLabel = rawLeft;
      } catch {
        leftVal   = rawLeft;
        leftLabel = `"${rawLeft}"`;
      }

      try {
        defaultVal   = Function('"use strict"; return (' + rawDefault + ')')();
        defaultLabel = rawDefault;
      } catch {
        defaultVal   = rawDefault;
        defaultLabel = `"${rawDefault}"`;
      }

      const orResult   = leftVal || defaultVal;
      const nullResult = leftVal ?? defaultVal;

      document.getElementById('orExpr').textContent   = `${leftLabel} || ${defaultLabel}`;
      document.getElementById('nullExpr').textContent = `${leftLabel} ?? ${defaultLabel}`;
      document.getElementById('orOutput').textContent   = formatValue(orResult);
      document.getElementById('nullOutput').textContent = formatValue(nullResult);

      const isNullOrUndef = leftVal === null || leftVal === undefined;
      const isFalsy       = !leftVal && !isNullOrUndef;
      const same          = String(orResult) === String(nullResult);

      let explanation = '';
      if (isNullOrUndef) {
        explanation = `${leftLabel} is ${leftVal === null ? 'null' : 'undefined'} — both ?? and || trigger their right-hand side, so the results are the same.`;
      } else if (isFalsy) {
        explanation = `${leftLabel} is falsy but NOT null/undefined. So || replaces it with the default, but ?? keeps ${leftLabel} as-is. The results differ — this is the key distinction between the two operators!`;
      } else {
        explanation = `${leftLabel} is truthy. Both ?? and || return the left-hand value unchanged.`;
      }

      document.getElementById('explainBox').textContent = explanation;
    }

    customInput.addEventListener('input', runTester);
    defaultInput.addEventListener('input', runTester);
    runTester();
  </script>

</body>
</html>
```

---

## CODEPEN 4 — Optional Chaining Safety Demo

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Optional Chaining Safety Demo</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      min-height: 100vh;
      padding: 2rem 1rem;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    h1 {
      font-size: 1.5rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
      color: #f8fafc;
      text-align: center;
    }

    .subtitle {
      font-size: 0.9rem;
      color: #94a3b8;
      margin-bottom: 2rem;
      text-align: center;
      max-width: 540px;
    }

    .container {
      width: 100%;
      max-width: 760px;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .card {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 1.25rem;
    }

    .card h2 {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #94a3b8;
      margin-bottom: 1rem;
    }

    /* API simulation controls */
    .user-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 0.75rem;
    }

    .user-card {
      background: #0f172a;
      border: 2px solid #334155;
      border-radius: 8px;
      padding: 0.75rem;
      cursor: pointer;
      transition: border-color 0.2s, background 0.2s;
    }

    .user-card:hover { border-color: #6366f1; }
    .user-card.active { border-color: #6366f1; background: #1a1a3e; }

    .user-card .user-name {
      font-weight: 700;
      font-size: 0.9rem;
      margin-bottom: 0.3rem;
    }

    .user-card .user-note {
      font-size: 0.72rem;
      color: #64748b;
      line-height: 1.4;
    }

    .missing { color: #ef4444; }
    .present { color: #4ade80; }

    /* Toggle */
    .toggle-row {
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
      margin-top: 0.75rem;
    }

    .toggle-btn {
      padding: 0.45rem 1rem;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      border: 2px solid transparent;
      transition: all 0.2s;
    }

    .btn-danger  { background: #7f1d1d; color: #fca5a5; border-color: #b91c1c; }
    .btn-safe    { background: #052e16; color: #86efac; border-color: #166534; }
    .btn-danger:hover { background: #991b1b; }
    .btn-safe:hover   { background: #14532d; }

    /* Results */
    .results-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
    }

    @media (max-width: 540px) {
      .results-grid { grid-template-columns: 1fr; }
    }

    .result-box {
      border-radius: 8px;
      padding: 0.85rem;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      line-height: 1.6;
    }

    .result-box .box-title {
      font-family: system-ui, sans-serif;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.5rem;
    }

    .box-unsafe { background: #1f0a0a; border: 1px solid #7f1d1d; }
    .box-unsafe .box-title { color: #f87171; }

    .box-safe   { background: #0a1f12; border: 1px solid #166534; }
    .box-safe   .box-title { color: #4ade80; }

    .prop-row {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 0.2rem;
    }

    .prop-key   { color: #60a5fa; }
    .prop-arrow { color: #64748b; }
    .prop-val-ok    { color: #4ade80; }
    .prop-val-undef { color: #94a3b8; }
    .prop-val-error { color: #f87171; font-weight: 700; }

    .error-banner {
      background: #1f0a0a;
      border: 1px solid #b91c1c;
      border-radius: 6px;
      padding: 0.5rem 0.75rem;
      font-size: 0.8rem;
      font-weight: 700;
      color: #f87171;
      margin-top: 0.5rem;
      display: none;
    }

    /* Code block */
    pre.code-compare {
      background: #0f172a;
      border-radius: 8px;
      padding: 1rem;
      font-size: 0.8rem;
      font-family: 'Courier New', monospace;
      line-height: 1.7;
      overflow-x: auto;
      color: #cbd5e1;
      white-space: pre;
    }

    .c-comment { color: #475569; }
    .c-op      { color: #f59e0b; }
    .c-str     { color: #4ade80; }
    .c-key     { color: #60a5fa; }
  </style>
</head>
<body>

  <h1>Optional Chaining Safety Demo</h1>
  <p class="subtitle">Click a user from the simulated API. Then toggle between unsafe and safe property access to see the difference.</p>

  <div class="container">

    <!-- User picker -->
    <div class="card">
      <h2>Simulated API Users</h2>
      <div class="user-grid" id="userGrid"></div>
    </div>

    <!-- Access mode -->
    <div class="card">
      <h2>Access Mode</h2>
      <div class="toggle-row">
        <button class="toggle-btn btn-danger" id="btnUnsafe">Without ?. (unsafe)</button>
        <button class="toggle-btn btn-safe"   id="btnSafe">With ?. (safe)</button>
      </div>
    </div>

    <!-- Results -->
    <div class="card">
      <h2>Property Access Results</h2>
      <div class="results-grid">
        <div class="result-box box-unsafe" id="unsafeBox">
          <div class="box-title">Without ?.</div>
          <div id="unsafeResults"></div>
          <div class="error-banner" id="errorBanner"></div>
        </div>
        <div class="result-box box-safe" id="safeBox">
          <div class="box-title">With ?.</div>
          <div id="safeResults"></div>
        </div>
      </div>
    </div>

    <!-- Code comparison -->
    <div class="card">
      <h2>Code Comparison</h2>
      <pre class="code-compare"><span class="c-comment">// Without optional chaining — crashes if any link is null</span>
<span class="c-key">const</span> city   = user.address.city;               <span class="c-comment">// TypeError if address is null</span>
<span class="c-key">const</span> zip    = user.address.zip;                <span class="c-comment">// TypeError if address is null</span>
<span class="c-key">const</span> perms  = user.role.getPermissions();      <span class="c-comment">// TypeError if role is null</span>
<span class="c-key">const</span> first  = user.orders[0].id;              <span class="c-comment">// TypeError if orders is null</span>

<span class="c-comment">// With optional chaining — safe navigation</span>
<span class="c-key">const</span> city   = user<span class="c-op">?.</span>address<span class="c-op">?.</span>city;            <span class="c-comment">// undefined if address is null</span>
<span class="c-key">const</span> zip    = user<span class="c-op">?.</span>address<span class="c-op">?.</span>zip;             <span class="c-comment">// undefined if address is null</span>
<span class="c-key">const</span> perms  = user<span class="c-op">?.</span>role<span class="c-op">?.</span>getPermissions<span class="c-op">?.</span>(); <span class="c-comment">// undefined if role or method missing</span>
<span class="c-key">const</span> first  = user<span class="c-op">?.</span>orders<span class="c-op">?.</span>[0]<span class="c-op">?.</span>id;         <span class="c-comment">// undefined if orders is null</span>

<span class="c-comment">// Combine with ?? for clean defaults</span>
<span class="c-key">const</span> city   = user<span class="c-op">?.</span>address<span class="c-op">?.</span>city <span class="c-op">??</span> <span class="c-str">"City unknown"</span>;
<span class="c-key">const</span> first  = user<span class="c-op">?.</span>orders<span class="c-op">?.</span>[0]<span class="c-op">?.</span>id <span class="c-op">??</span> <span class="c-str">"No orders"</span>;</pre>
    </div>

  </div>

  <script>
    const users = [
      {
        id: 1,
        name: "Alice",
        note: "Complete profile",
        hasAddress: true, hasRole: true, hasOrders: true,
        address: { city: "Austin", zip: "78701" },
        role: { name: "admin", getPermissions() { return ["read","write","delete"]; } },
        orders: [{ id: "ORD-001", total: 89.99 }, { id: "ORD-002", total: 54.00 }]
      },
      {
        id: 2,
        name: "Bob",
        note: "address is null",
        hasAddress: false, hasRole: true, hasOrders: true,
        address: null,
        role: { name: "viewer", getPermissions() { return ["read"]; } },
        orders: [{ id: "ORD-003", total: 22.50 }]
      },
      {
        id: 3,
        name: "Carol",
        note: "role is null, no orders",
        hasAddress: true, hasRole: false, hasOrders: false,
        address: { city: "Denver", zip: "80201" },
        role: null,
        orders: null
      },
      {
        id: 4,
        name: "Dan",
        note: "Everything missing",
        hasAddress: false, hasRole: false, hasOrders: false,
        address: null,
        role: null,
        orders: null
      }
    ];

    let selectedUser = users[0];
    let mode = 'safe';

    function renderUserGrid() {
      const grid = document.getElementById('userGrid');
      grid.innerHTML = '';
      users.forEach(u => {
        const div = document.createElement('div');
        div.className = `user-card ${u.id === selectedUser.id ? 'active' : ''}`;
        div.innerHTML = `
          <div class="user-name">${u.name}</div>
          <div class="user-note">${u.note}</div>
          <div style="margin-top:0.35rem; font-size:0.7rem;">
            <span class="${u.hasAddress ? 'present' : 'missing'}">address${u.hasAddress ? ' ✓' : ' ✗'}</span> &nbsp;
            <span class="${u.hasRole ? 'present' : 'missing'}">role${u.hasRole ? ' ✓' : ' ✗'}</span> &nbsp;
            <span class="${u.hasOrders ? 'present' : 'missing'}">orders${u.hasOrders ? ' ✓' : ' ✗'}</span>
          </div>
        `;
        div.addEventListener('click', () => {
          selectedUser = u;
          renderUserGrid();
          renderResults();
        });
        grid.appendChild(div);
      });
    }

    function renderResults() {
      const user = selectedUser;
      const unsafeDiv  = document.getElementById('unsafeResults');
      const safeDiv    = document.getElementById('safeResults');
      const errorBanner = document.getElementById('errorBanner');

      // Safe results always work
      const safeCity  = user?.address?.city   ?? 'City unknown';
      const safeZip   = user?.address?.zip    ?? 'ZIP unknown';
      const safePerms = user?.role?.getPermissions?.() ?? ['no permissions'];
      const safeFirst = user?.orders?.[0]?.id ?? 'No orders';

      safeDiv.innerHTML = `
        ${row('user?.address?.city', safeCity, 'ok')}
        ${row('user?.address?.zip', safeZip, 'ok')}
        ${row('user?.role?.getPermissions?.()', JSON.stringify(safePerms), 'ok')}
        ${row('user?.orders?.[0]?.id', safeFirst, 'ok')}
      `;

      // Unsafe results
      let crashedAt = null;
      let unsafeHtml = '';

      function tryAccess(label, fn) {
        if (crashedAt) {
          return row(label, '(skipped)', 'undef');
        }
        try {
          const val = fn();
          const display = val === undefined ? 'undefined' : (Array.isArray(val) ? JSON.stringify(val) : String(val));
          return row(label, display, 'ok');
        } catch (e) {
          crashedAt = label;
          return row(label, 'TypeError!', 'error');
        }
      }

      unsafeHtml += tryAccess('user.address.city',             () => user.address.city);
      unsafeHtml += tryAccess('user.address.zip',              () => user.address.zip);
      unsafeHtml += tryAccess('user.role.getPermissions()',    () => JSON.stringify(user.role.getPermissions()));
      unsafeHtml += tryAccess('user.orders[0].id',            () => user.orders[0].id);

      unsafeDiv.innerHTML = unsafeHtml;

      if (crashedAt) {
        errorBanner.style.display = 'block';
        errorBanner.textContent = `TypeError thrown at: ${crashedAt}`;
      } else {
        errorBanner.style.display = 'none';
      }
    }

    function row(label, value, state) {
      const valClass = state === 'error' ? 'prop-val-error' : state === 'undef' ? 'prop-val-undef' : 'prop-val-ok';
      return `<div class="prop-row">
        <span class="prop-key">${label}</span>
        <span class="prop-arrow">→</span>
        <span class="${valClass}">${value}</span>
      </div>`;
    }

    document.getElementById('btnUnsafe').addEventListener('click', () => { mode = 'unsafe'; renderResults(); });
    document.getElementById('btnSafe').addEventListener('click',   () => { mode = 'safe';   renderResults(); });

    renderUserGrid();
    renderResults();
  </script>

</body>
</html>
```

---

## CODEPEN 5 — Complete Control Flow: User Dashboard Logic

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>User Dashboard — Control Flow Demo</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0a0f1e;
      color: #e2e8f0;
      min-height: 100vh;
      display: grid;
      grid-template-columns: 280px 1fr;
    }

    @media (max-width: 640px) {
      body { grid-template-columns: 1fr; }
      .sidebar { border-right: none; border-bottom: 1px solid #1e293b; }
    }

    /* Sidebar */
    .sidebar {
      background: #0f172a;
      border-right: 1px solid #1e293b;
      padding: 1.5rem 1rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .sidebar h1 {
      font-size: 1rem;
      font-weight: 700;
      color: #6366f1;
      margin-bottom: 0.25rem;
    }

    .sidebar p.desc {
      font-size: 0.75rem;
      color: #64748b;
      line-height: 1.5;
    }

    .control-group {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .control-group label.group-label {
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #475569;
    }

    .toggle-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #1e293b;
      border-radius: 8px;
      padding: 0.55rem 0.75rem;
    }

    .toggle-row label {
      font-size: 0.82rem;
      color: #cbd5e1;
    }

    /* Toggle switch */
    .switch {
      position: relative;
      width: 36px;
      height: 20px;
      flex-shrink: 0;
    }

    .switch input { display: none; }

    .slider {
      position: absolute;
      inset: 0;
      background: #334155;
      border-radius: 20px;
      cursor: pointer;
      transition: background 0.2s;
    }

    .slider::before {
      content: '';
      position: absolute;
      width: 14px;
      height: 14px;
      left: 3px;
      top: 3px;
      background: #fff;
      border-radius: 50%;
      transition: transform 0.2s;
    }

    input:checked + .slider { background: #6366f1; }
    input:checked + .slider::before { transform: translateX(16px); }

    select {
      width: 100%;
      padding: 0.5rem 0.6rem;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      color: #f1f5f9;
      font-size: 0.85rem;
      outline: none;
      cursor: pointer;
    }

    select:focus { border-color: #6366f1; }

    /* Feature flag badges */
    .flags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
    }

    .flag-btn {
      padding: 0.3rem 0.65rem;
      border-radius: 999px;
      font-size: 0.72rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.15s;
      background: #1e293b;
      color: #64748b;
      border-color: #334155;
    }

    .flag-btn.active {
      background: #312e81;
      color: #a5b4fc;
      border-color: #6366f1;
    }

    /* Main content */
    .main {
      padding: 1.5rem;
      overflow-y: auto;
    }

    /* Status bar */
    .status-bar {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 0.75rem 1rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      margin-bottom: 1.25rem;
      font-size: 0.82rem;
    }

    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }

    .dot-online  { background: #4ade80; }
    .dot-offline { background: #64748b; }

    /* Dashboard sections */
    .dash-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 0.85rem;
      margin-bottom: 1.25rem;
    }

    .stat-card {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 1rem;
    }

    .stat-card .stat-label {
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #64748b;
      margin-bottom: 0.3rem;
    }

    .stat-card .stat-value {
      font-size: 1.4rem;
      font-weight: 700;
      color: #f8fafc;
    }

    .stat-card .stat-sub {
      font-size: 0.72rem;
      color: #94a3b8;
      margin-top: 0.2rem;
    }

    /* Panels */
    .panel {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 1rem 1.25rem;
      margin-bottom: 1rem;
    }

    .panel h2 {
      font-size: 0.85rem;
      font-weight: 700;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.75rem;
    }

    .access-badge {
      display: inline-block;
      padding: 0.25rem 0.7rem;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 700;
      margin-bottom: 0.75rem;
    }

    .badge-admin    { background: #1a0a2e; color: #c084fc; border: 1px solid #7c3aed; }
    .badge-editor   { background: #0c1a2e; color: #60a5fa; border: 1px solid #2563eb; }
    .badge-viewer   { background: #0a1f12; color: #4ade80; border: 1px solid #16a34a; }
    .badge-guest    { background: #1c1917; color: #a8a29e; border: 1px solid #44403c; }
    .badge-offline  { background: #1f0a0a; color: #f87171; border: 1px solid #b91c1c; }

    .action-list {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }

    .action-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.82rem;
      color: #cbd5e1;
    }

    .action-item::before {
      content: '▶';
      font-size: 0.6rem;
      color: #6366f1;
    }

    /* Feature flags panel */
    .feature-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 0.5rem;
    }

    .feature-item {
      background: #0f172a;
      border-radius: 8px;
      padding: 0.55rem 0.75rem;
      font-size: 0.78rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .fi-on  { color: #4ade80; }
    .fi-off { color: #475569; text-decoration: line-through; }

    /* Code trace */
    .trace-panel {
      background: #050c18;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 1rem;
    }

    .trace-panel h2 {
      font-size: 0.85rem;
      font-weight: 700;
      color: #475569;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.75rem;
    }

    .trace-lines {
      font-family: 'Courier New', monospace;
      font-size: 0.75rem;
      line-height: 2;
      color: #64748b;
      display: flex;
      flex-direction: column;
      gap: 0;
    }

    .tl { padding: 0 0.5rem; border-radius: 3px; }
    .tl-fired  { background: #0a1f12; color: #86efac; }
    .tl-skip   { color: #1e293b; }
    .tl-result { background: #1a1a3e; color: #a5b4fc; }

    /* Auth wall */
    .auth-wall {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 300px;
      gap: 0.75rem;
    }

    .auth-wall .lock-icon {
      font-size: 3rem;
    }

    .auth-wall h2 {
      font-size: 1.1rem;
      font-weight: 700;
      color: #f87171;
    }

    .auth-wall p {
      font-size: 0.85rem;
      color: #64748b;
    }
  </style>
</head>
<body>

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div>
      <h1>Dashboard Controls</h1>
      <p class="desc">Every control below feeds into the JavaScript decision engine on the right.</p>
    </div>

    <div class="control-group">
      <label class="group-label">Authentication</label>
      <div class="toggle-row">
        <label for="toggleLogin">Logged in</label>
        <label class="switch">
          <input type="checkbox" id="toggleLogin" checked>
          <span class="slider"></span>
        </label>
      </div>
      <div class="toggle-row">
        <label for="toggleVerified">Email verified</label>
        <label class="switch">
          <input type="checkbox" id="toggleVerified" checked>
          <span class="slider"></span>
        </label>
      </div>
    </div>

    <div class="control-group">
      <label class="group-label">User Role</label>
      <select id="roleSelect">
        <option value="admin">Admin</option>
        <option value="editor" selected>Editor</option>
        <option value="viewer">Viewer</option>
        <option value="guest">Guest</option>
      </select>
    </div>

    <div class="control-group">
      <label class="group-label">Active Feature Flags</label>
      <div class="flags" id="flagsContainer"></div>
    </div>

    <div class="control-group">
      <label class="group-label">Config Overrides</label>
      <div class="toggle-row">
        <label for="toggleTimeout">Timeout: null</label>
        <label class="switch">
          <input type="checkbox" id="toggleTimeout">
          <span class="slider"></span>
        </label>
      </div>
      <div class="toggle-row">
        <label for="toggleTheme">Theme: undefined</label>
        <label class="switch">
          <input type="checkbox" id="toggleTheme">
          <span class="slider"></span>
        </label>
      </div>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main" id="mainContent"></main>

  <script>
    // ---- State ----
    const flags = ['analytics', 'beta-ui', 'dark-mode', 'export-pdf'];
    const activeFlags = new Set(['analytics', 'dark-mode']);

    // Build flag buttons
    const flagsContainer = document.getElementById('flagsContainer');
    flags.forEach(flag => {
      const btn = document.createElement('button');
      btn.className = `flag-btn ${activeFlags.has(flag) ? 'active' : ''}`;
      btn.textContent = flag;
      btn.addEventListener('click', () => {
        activeFlags.has(flag) ? activeFlags.delete(flag) : activeFlags.add(flag);
        btn.classList.toggle('active');
        render();
      });
      flagsContainer.appendChild(btn);
    });

    // ---- Core render function ----
    function render() {
      const isLoggedIn    = document.getElementById('toggleLogin').checked;
      const isVerified    = document.getElementById('toggleVerified').checked;
      const role          = document.getElementById('roleSelect').value;
      const timeoutIsNull = document.getElementById('toggleTimeout').checked;
      const themeIsUndef  = document.getElementById('toggleTheme').checked;

      // Simulate a config object — some values may be null/undefined
      const rawConfig = {
        timeout: timeoutIsNull ? null : 0,           // 0 is valid! Use ??=, not ||=
        theme:   themeIsUndef  ? undefined : "slate",
        maxItems: 50
      };

      // Apply defaults using ??= — preserves 0 and other valid falsy values
      rawConfig.timeout  ??= 5000;
      rawConfig.theme    ??= "light";
      rawConfig.maxItems ??= 25;

      // Simulate user data — might have incomplete profile
      const userData = isLoggedIn ? {
        name: "Jordan Lee",
        role,
        email: isVerified ? "jordan@example.com" : null,
        stats: { posts: 42, views: 1_840, comments: 118 },
        preferences: { notifications: true }
      } : null;

      // Safe access with optional chaining
      const userName    = userData?.name        ?? "Guest";
      const userEmail   = userData?.email       ?? "Email not verified";
      const postCount   = userData?.stats?.posts ?? 0;
      const viewCount   = userData?.stats?.views ?? 0;

      // Logical AND assignment: only update role if user exists
      let sessionRole = role;
      // If not logged in, force guest regardless of selector
      if (!isLoggedIn) sessionRole = "guest";

      // Determine access level via switch
      let accessLevel, accessBadgeClass, accessActions;
      switch (sessionRole) {
        case "admin":
          accessLevel      = "Full Admin Access";
          accessBadgeClass = "badge-admin";
          accessActions    = ["Manage all users", "Edit site settings", "View audit logs", "Deploy changes", "Access developer tools"];
          break;
        case "editor":
          accessLevel      = "Editor Access";
          accessBadgeClass = "badge-editor";
          accessActions    = ["Create & edit content", "Upload media", "Publish drafts", "View analytics"];
          break;
        case "viewer":
          accessLevel      = "Read-Only Access";
          accessBadgeClass = "badge-viewer";
          accessActions    = ["View published content", "Leave comments", "Download allowed files"];
          break;
        default:
          accessLevel      = "Guest Access";
          accessBadgeClass = "badge-guest";
          accessActions    = ["View public pages", "Sign up for an account"];
      }

      // Build trace for educational display
      const traceFired = [];
      traceFired.push({ text: `if (!isLoggedIn)  →  ${!isLoggedIn}`, fired: !isLoggedIn });
      traceFired.push({ text: `userData?.name ?? "Guest"  →  "${userName}"`, fired: true });
      traceFired.push({ text: `userData?.email ?? "Email not verified"  →  "${userEmail}"`, fired: true });
      traceFired.push({ text: `rawConfig.timeout ??= 5000  →  ${rawConfig.timeout}`, fired: timeoutIsNull });
      traceFired.push({ text: `rawConfig.theme ??= "light"  →  "${rawConfig.theme}"`, fired: themeIsUndef });
      traceFired.push({ text: `switch(sessionRole) case "${sessionRole}"  →  matched`, fired: true });
      const flagList = [...activeFlags].join(', ') || 'none';
      traceFired.push({ text: `active flags: [${flagList}]`, fired: activeFlags.size > 0 });

      // ---- Build HTML ----
      const main = document.getElementById('mainContent');

      if (!isLoggedIn) {
        main.innerHTML = `
          <div class="auth-wall">
            <div class="lock-icon">🔒</div>
            <h2>Authentication Required</h2>
            <p>The if (!isLoggedIn) branch fired — dashboard is hidden.</p>
            <p style="font-family:monospace; font-size:0.8rem; color:#64748b; margin-top:0.5rem;">
              if (!isLoggedIn) { showAuthWall(); return; }
            </p>
          </div>
          ${buildTrace(traceFired, rawConfig)}
        `;
        return;
      }

      main.innerHTML = `
        <div class="status-bar">
          <div class="status-dot dot-online"></div>
          <strong>${userName}</strong>
          <span style="color:#64748b">·</span>
          <span style="color:#94a3b8">${userEmail}</span>
          <span style="color:#64748b; margin-left:auto; font-size:0.75rem;">config.timeout: ${rawConfig.timeout}ms · theme: ${rawConfig.theme}</span>
        </div>

        <div class="dash-grid">
          <div class="stat-card">
            <div class="stat-label">Posts</div>
            <div class="stat-value">${postCount}</div>
            <div class="stat-sub">published articles</div>
          </div>
          <div class="stat-card">
            <div class="stat-label">Views</div>
            <div class="stat-value">${viewCount.toLocaleString()}</div>
            <div class="stat-sub">all time</div>
          </div>
          <div class="stat-card">
            <div class="stat-label">Max Items</div>
            <div class="stat-value">${rawConfig.maxItems}</div>
            <div class="stat-sub">per page (config)</div>
          </div>
        </div>

        <div class="panel">
          <h2>Role &amp; Permissions</h2>
          <span class="access-badge ${accessBadgeClass}">${accessLevel}</span>
          <div class="action-list">
            ${accessActions.map(a => `<div class="action-item">${a}</div>`).join('')}
          </div>
        </div>

        <div class="panel">
          <h2>Feature Flags</h2>
          <div class="feature-grid">
            ${flags.map(f => `
              <div class="feature-item ${activeFlags.has(f) ? 'fi-on' : 'fi-off'}">
                ${activeFlags.has(f) ? '✓' : '✗'} ${f}
              </div>
            `).join('')}
          </div>
          ${activeFlags.has('beta-ui')
            ? '<p style="margin-top:0.75rem; font-size:0.8rem; color:#a78bfa;">✦ Beta UI is active — new layout components are enabled.</p>'
            : ''
          }
          ${activeFlags.has('export-pdf')
            ? '<p style="margin-top:0.5rem; font-size:0.8rem; color:#a78bfa;">✦ PDF export is available in the toolbar.</p>'
            : ''
          }
        </div>

        ${buildTrace(traceFired, rawConfig)}
      `;
    }

    function buildTrace(traceFired, config) {
      const lines = traceFired.map(t =>
        `<div class="tl ${t.fired ? 'tl-fired' : 'tl-skip'}">${t.text}</div>`
      ).join('');

      return `
        <div class="trace-panel">
          <h2>JS Decision Trace</h2>
          <div class="trace-lines">
            ${lines}
            <div class="tl tl-result">config resolved → { timeout: ${config.timeout}, theme: "${config.theme}", maxItems: ${config.maxItems} }</div>
          </div>
        </div>
      `;
    }

    // Attach listeners
    ['toggleLogin', 'toggleVerified', 'roleSelect', 'toggleTimeout', 'toggleTheme'].forEach(id => {
      document.getElementById(id).addEventListener('change', render);
    });

    render();
  </script>

</body>
</html>
```
