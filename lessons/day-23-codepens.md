# Day 23 — Loops & Generating HTML: CodePen Code Blocks

Each section below contains the complete HTML for one CodePen embed referenced in the article. Each CodePen is a single, self-contained HTML file with CSS in a `<style>` block in `<head>` and JavaScript in a `<script>` block at the bottom of `<body>`.

---

## CODEPEN 1 — for Loop Visualizer

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>for Loop Visualizer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      min-height: 100vh;
      padding: 1.5rem;
    }

    h1 {
      text-align: center;
      font-size: 1.4rem;
      color: #7dd3fc;
      margin-bottom: 1.5rem;
      letter-spacing: 0.02em;
    }

    .panel {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 1.25rem;
      margin-bottom: 1.25rem;
    }

    .panel h2 {
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #94a3b8;
      margin-bottom: 1rem;
    }

    /* Controls */
    .controls {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
      gap: 1rem;
    }

    .control-group label {
      display: block;
      font-size: 0.8rem;
      color: #94a3b8;
      margin-bottom: 0.35rem;
    }

    .control-group input,
    .control-group select {
      width: 100%;
      padding: 0.45rem 0.65rem;
      background: #0f172a;
      border: 1.5px solid #475569;
      border-radius: 6px;
      color: #e2e8f0;
      font-size: 0.95rem;
    }

    .control-group input:focus,
    .control-group select:focus {
      outline: none;
      border-color: #38bdf8;
    }

    /* Condition toggle */
    .toggle-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-top: 1rem;
      font-size: 0.9rem;
    }

    .toggle-row label { color: #94a3b8; }

    .toggle-btn {
      padding: 0.3rem 0.8rem;
      border-radius: 6px;
      border: 1.5px solid #475569;
      background: #0f172a;
      color: #e2e8f0;
      cursor: pointer;
      font-family: monospace;
      font-size: 0.95rem;
      transition: border-color 0.2s, background 0.2s;
    }

    .toggle-btn.active-lt  { border-color: #22c55e; color: #22c55e; background: #14532d22; }
    .toggle-btn.active-lte { border-color: #ef4444; color: #ef4444; background: #7f1d1d22; }

    /* Run button */
    .run-btn {
      display: block;
      width: 100%;
      margin-top: 1rem;
      padding: 0.65rem;
      background: #0ea5e9;
      color: #fff;
      border: none;
      border-radius: 8px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s;
    }

    .run-btn:hover { background: #0284c7; }
    .run-btn:disabled { background: #334155; cursor: not-allowed; }

    /* Code display */
    .code-display {
      font-family: 'Courier New', monospace;
      font-size: 0.88rem;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 1rem;
      line-height: 1.8;
      white-space: pre;
    }

    .code-kw  { color: #c084fc; }
    .code-var { color: #38bdf8; }
    .code-num { color: #fb923c; }
    .code-op  { color: #f472b6; }
    .code-hi  { background: #1e3a5f; border-radius: 3px; padding: 0 2px; }

    /* Visualization area */
    .viz-area {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      min-height: 60px;
      align-items: center;
    }

    .viz-block {
      width: 48px;
      height: 48px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 1.05rem;
      border: 2px solid transparent;
      transition: all 0.3s ease;
      opacity: 0;
      transform: scale(0.6);
    }

    .viz-block.appear {
      opacity: 1;
      transform: scale(1);
    }

    .viz-block.current {
      border-color: #fbbf24;
      box-shadow: 0 0 12px #fbbf2466;
    }

    .color-0  { background: #1e40af; color: #93c5fd; }
    .color-1  { background: #166534; color: #86efac; }
    .color-2  { background: #92400e; color: #fcd34d; }
    .color-3  { background: #7c2d12; color: #fb923c; }
    .color-4  { background: #4c1d95; color: #c4b5fd; }
    .color-5  { background: #0e7490; color: #67e8f9; }
    .color-6  { background: #065f46; color: #6ee7b7; }
    .color-7  { background: #881337; color: #fda4af; }
    .color-8  { background: #1e3a5f; color: #93c5fd; }
    .color-9  { background: #3b0764; color: #e9d5ff; }
    .color-oob { background: #450a0a; color: #ef4444; border: 2px solid #ef4444 !important; }

    /* Status row */
    .status-row {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
      margin-top: 0.75rem;
    }

    .status-pill {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 20px;
      padding: 0.25rem 0.75rem;
      font-size: 0.85rem;
    }

    .status-pill .label { color: #64748b; }
    .status-pill .value { color: #f1f5f9; font-family: monospace; font-weight: 600; }

    .pill-green  { border-color: #22c55e; }
    .pill-yellow { border-color: #eab308; }
    .pill-red    { border-color: #ef4444; }

    /* Output log */
    .log {
      font-family: 'Courier New', monospace;
      font-size: 0.85rem;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      max-height: 160px;
      overflow-y: auto;
      line-height: 1.7;
    }

    .log-entry { color: #86efac; }
    .log-oob   { color: #f87171; }
    .log-info  { color: #94a3b8; font-style: italic; }
    .log-warn  { color: #fbbf24; }

    /* Warning callout */
    .warn-box {
      background: #431407;
      border: 1px solid #c2410c;
      border-radius: 8px;
      padding: 0.65rem 1rem;
      font-size: 0.85rem;
      color: #fdba74;
      display: none;
    }

    .warn-box.show { display: block; }
  </style>
</head>
<body>

<h1>for Loop Visualizer</h1>

<!-- Controls -->
<div class="panel">
  <h2>Loop Parameters</h2>
  <div class="controls">
    <div class="control-group">
      <label for="start">Start (i = )</label>
      <input type="number" id="start" value="0" min="0" max="20">
    </div>
    <div class="control-group">
      <label for="end">End value</label>
      <input type="number" id="end" value="5" min="1" max="20">
    </div>
    <div class="control-group">
      <label for="step">Step (i += )</label>
      <input type="number" id="step" value="1" min="1" max="10">
    </div>
    <div class="control-group">
      <label for="speed">Speed</label>
      <select id="speed">
        <option value="900">Slow</option>
        <option value="500" selected>Medium</option>
        <option value="200">Fast</option>
      </select>
    </div>
  </div>

  <div class="toggle-row">
    <label>Condition operator:</label>
    <button class="toggle-btn active-lt" id="btn-lt" title="Use less-than (correct for arrays)">i &lt; end</button>
    <button class="toggle-btn" id="btn-lte" title="Use less-than-or-equal (shows the off-by-one bug)">i &lt;= end</button>
    <span id="oboe-label" style="font-size:0.78rem; color:#94a3b8;"></span>
  </div>

  <button class="run-btn" id="run-btn">▶  Run Loop</button>
</div>

<!-- Code display -->
<div class="panel">
  <h2>Generated Loop Code</h2>
  <div class="code-display" id="code-display">
    <span class="code-kw">for</span> (<span class="code-kw">let</span> <span class="code-var">i</span> <span class="code-op">=</span> <span class="code-num" id="cd-start">0</span>; <span class="code-var">i</span> <span class="code-op" id="cd-op">&lt;</span> <span class="code-num" id="cd-end">5</span>; <span class="code-var">i</span> <span class="code-op">+=</span> <span class="code-num" id="cd-step">1</span>) {
      console.log(<span class="code-var">i</span>); <span style="color:#475569">// iteration body</span>
    }
  </div>
</div>

<!-- Visualization -->
<div class="panel">
  <h2>Visualization</h2>
  <div class="viz-area" id="viz-area"></div>
  <div class="status-row" id="status-row">
    <div class="status-pill pill-yellow">
      <span class="label">i =</span>
      <span class="value" id="s-i">—</span>
    </div>
    <div class="status-pill" id="s-cond-pill">
      <span class="label">condition:</span>
      <span class="value" id="s-cond">—</span>
    </div>
    <div class="status-pill">
      <span class="label">iterations:</span>
      <span class="value" id="s-iter">0</span>
    </div>
  </div>
  <div class="warn-box" id="warn-box">
    ⚠️ Off-by-one! The loop ran one extra iteration — index <strong id="oob-index"></strong> is out of bounds. When you use <code>&lt;=</code> instead of <code>&lt;</code>, you get one extra (undefined) slot at the end.
  </div>
</div>

<!-- Output log -->
<div class="panel">
  <h2>Console Output</h2>
  <div class="log" id="log"><span class="log-info">Click "Run Loop" to start...</span></div>
</div>

<script>
  const startInput  = document.getElementById('start');
  const endInput    = document.getElementById('end');
  const stepInput   = document.getElementById('step');
  const speedSelect = document.getElementById('speed');
  const runBtn      = document.getElementById('run-btn');
  const btnLt       = document.getElementById('btn-lt');
  const btnLte      = document.getElementById('btn-lte');
  const oboeLabel   = document.getElementById('oboe-label');

  const vizArea     = document.getElementById('viz-area');
  const logEl       = document.getElementById('log');
  const warnBox     = document.getElementById('warn-box');
  const oobIndex    = document.getElementById('oob-index');

  const siEl        = document.getElementById('s-i');
  const sCondEl     = document.getElementById('s-cond');
  const sCondPill   = document.getElementById('s-cond-pill');
  const sIterEl     = document.getElementById('s-iter');

  const cdStart     = document.getElementById('cd-start');
  const cdEnd       = document.getElementById('cd-end');
  const cdStep      = document.getElementById('cd-step');
  const cdOp        = document.getElementById('cd-op');

  let useLte = false;
  let running = false;

  function updateCodeDisplay() {
    cdStart.textContent = startInput.value;
    cdEnd.textContent   = endInput.value;
    cdStep.textContent  = stepInput.value;
    cdOp.textContent    = useLte ? '<=' : '<';
  }

  [startInput, endInput, stepInput].forEach(el =>
    el.addEventListener('input', updateCodeDisplay)
  );

  btnLt.addEventListener('click', () => {
    useLte = false;
    btnLt.className  = 'toggle-btn active-lt';
    btnLte.className = 'toggle-btn';
    oboeLabel.textContent = '';
    updateCodeDisplay();
  });

  btnLte.addEventListener('click', () => {
    useLte = true;
    btnLt.className  = 'toggle-btn';
    btnLte.className = 'toggle-btn active-lte';
    oboeLabel.textContent = '← demonstrates the off-by-one bug!';
    updateCodeDisplay();
  });

  function sleep(ms) {
    return new Promise(res => setTimeout(res, ms));
  }

  function logLine(text, cls = 'log-entry') {
    const div = document.createElement('div');
    div.className = cls;
    div.textContent = text;
    logEl.appendChild(div);
    logEl.scrollTop = logEl.scrollHeight;
  }

  async function runLoop() {
    if (running) return;
    running = true;
    runBtn.disabled = true;
    runBtn.textContent = '⏳ Running...';

    const start = parseInt(startInput.value);
    const end   = parseInt(endInput.value);
    const step  = Math.max(1, parseInt(stepInput.value));
    const delay = parseInt(speedSelect.value);

    vizArea.innerHTML = '';
    logEl.innerHTML = '';
    warnBox.classList.remove('show');
    siEl.textContent    = '—';
    sCondEl.textContent = '—';
    sIterEl.textContent = '0';
    sCondPill.style.borderColor = '';

    logLine(`for (let i = ${start}; i ${useLte ? '<=' : '<'} ${end}; i += ${step})`, 'log-info');

    let iterations = 0;
    let colorIdx = 0;

    for (let i = start; useLte ? i <= end : i < end; i += step) {
      // Update status
      siEl.textContent    = i;
      const condResult    = useLte ? `${i} <= ${end}` : `${i} < ${end}`;
      sCondEl.textContent = condResult + ' → true';
      sCondPill.style.borderColor = '#22c55e';
      sIterEl.textContent = ++iterations;

      // Create block
      const block = document.createElement('div');
      block.className = `viz-block color-${colorIdx % 10}`;
      block.textContent = i;
      vizArea.appendChild(block);

      requestAnimationFrame(() => {
        setTimeout(() => block.classList.add('appear', 'current'), 10);
      });

      logLine(`  i = ${i} → console.log(${i})`);
      await sleep(delay);

      block.classList.remove('current');
      colorIdx++;
    }

    // Show off-by-one case if lte is selected
    if (useLte) {
      const badI = start + Math.ceil((end - start + 1) / step) * step;
      // Last iteration that triggered the condition was 'end' itself
      const oob = end;

      siEl.textContent    = oob;
      sCondEl.textContent = useLte ? `${oob} <= ${oob}` : `${oob} < ${oob}`;

      // Add an out-of-bounds block
      const badBlock = document.createElement('div');
      badBlock.className = 'viz-block color-oob';
      badBlock.textContent = end;
      vizArea.appendChild(badBlock);
      requestAnimationFrame(() => setTimeout(() => badBlock.classList.add('appear', 'current'), 10));

      logLine(`  ⚠ i = ${oob} → array[${oob}] would be undefined!`, 'log-warn');

      oobIndex.textContent = oob;
      await sleep(delay);
      badBlock.classList.remove('current');
      warnBox.classList.add('show');
    }

    // Final condition check — false
    const finalI = start + iterations * step;
    const finalCond = useLte
      ? `${finalI} <= ${end} → false (but off-by-one already happened!)`
      : `${finalI} < ${end} → false`;
    siEl.textContent    = finalI;
    sCondEl.textContent = finalCond;
    sCondPill.style.borderColor = '#ef4444';

    logLine(`Loop complete — ${iterations} iteration${iterations !== 1 ? 's' : ''}`, 'log-info');

    running = false;
    runBtn.disabled = false;
    runBtn.textContent = '▶  Run Loop';
  }

  runBtn.addEventListener('click', runLoop);
  updateCodeDisplay();
</script>
</body>
</html>
```

---

## CODEPEN 2 — Loop Types Comparison

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Loop Types Comparison</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      padding: 1.25rem;
      min-height: 100vh;
    }

    h1 {
      text-align: center;
      font-size: 1.3rem;
      color: #7dd3fc;
      margin-bottom: 0.5rem;
    }

    .subtitle {
      text-align: center;
      font-size: 0.85rem;
      color: #64748b;
      margin-bottom: 1.25rem;
    }

    /* Data array display */
    .data-panel {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 1rem 1.25rem;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .data-label {
      font-size: 0.8rem;
      color: #94a3b8;
      font-family: monospace;
    }

    .data-items {
      display: flex;
      gap: 0.4rem;
      flex-wrap: wrap;
    }

    .data-chip {
      background: #0ea5e920;
      border: 1px solid #0ea5e9;
      color: #7dd3fc;
      border-radius: 6px;
      padding: 0.2rem 0.55rem;
      font-family: monospace;
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.3rem;
    }

    .chip-index {
      font-size: 0.65rem;
      color: #475569;
      background: #0f172a;
      border-radius: 3px;
      padding: 0 3px;
    }

    /* Three-column panel grid */
    .panel-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1rem;
      margin-bottom: 1.25rem;
    }

    .loop-panel {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      overflow: hidden;
    }

    .loop-panel-header {
      padding: 0.65rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .for-panel .loop-panel-header    { background: #1e3a5f; border-bottom: 1px solid #1d4ed8; }
    .while-panel .loop-panel-header  { background: #1e3d2f; border-bottom: 1px solid #16a34a; }
    .forof-panel .loop-panel-header  { background: #3b1f5c; border-bottom: 1px solid #7c3aed; }

    .loop-type-label {
      font-family: monospace;
      font-size: 0.95rem;
      font-weight: 700;
    }

    .for-panel    .loop-type-label { color: #60a5fa; }
    .while-panel  .loop-type-label { color: #4ade80; }
    .forof-panel  .loop-type-label { color: #c084fc; }

    .iteration-badge {
      font-size: 0.7rem;
      background: #0f172a;
      padding: 0.15rem 0.5rem;
      border-radius: 10px;
      color: #94a3b8;
    }

    /* Code snippet in each panel */
    .code-snip {
      font-family: 'Courier New', monospace;
      font-size: 0.75rem;
      background: #0f172a;
      color: #94a3b8;
      padding: 0.65rem 1rem;
      border-bottom: 1px solid #1e293b;
      white-space: pre;
      line-height: 1.6;
    }

    .ck  { color: #c084fc; }
    .cv  { color: #38bdf8; }
    .cn  { color: #fb923c; }
    .cs  { color: #86efac; }
    .cc  { color: #475569; }

    /* Step display area */
    .step-area {
      padding: 0.75rem 1rem;
    }

    .step-list {
      list-style: none;
      font-family: monospace;
      font-size: 0.82rem;
      max-height: 140px;
      overflow-y: auto;
    }

    .step-item {
      padding: 0.2rem 0;
      color: #64748b;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: color 0.2s;
    }

    .step-item.active {
      color: #f1f5f9;
    }

    .step-item.done {
      color: #4ade80;
    }

    .step-num {
      font-size: 0.65rem;
      color: #334155;
      min-width: 18px;
      text-align: right;
    }

    .step-arrow { color: #334155; }
    .step-item.active .step-arrow { color: #fbbf24; }
    .step-item.done  .step-arrow  { color: #22c55e; }

    /* Current item highlight */
    .current-item-display {
      margin-top: 0.5rem;
      font-family: monospace;
      font-size: 0.8rem;
      color: #94a3b8;
      min-height: 1.5em;
    }

    .current-item-display .hi { color: #fbbf24; font-weight: 700; }

    /* Controls */
    .controls-row {
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
      align-items: center;
    }

    button {
      padding: 0.5rem 1.1rem;
      border-radius: 8px;
      border: none;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: opacity 0.2s, transform 0.1s;
    }

    button:active { transform: scale(0.97); }
    button:disabled { opacity: 0.4; cursor: not-allowed; }

    .btn-step  { background: #0ea5e9; color: #fff; }
    .btn-run   { background: #22c55e; color: #0f172a; }
    .btn-reset { background: #334155; color: #e2e8f0; }

    /* When to use info */
    .when-to-use {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 1rem 1.25rem;
    }

    .when-to-use h2 {
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      color: #94a3b8;
      margin-bottom: 0.75rem;
    }

    .when-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 0.75rem;
    }

    .when-card {
      background: #0f172a;
      border-radius: 8px;
      padding: 0.75rem;
    }

    .when-card h3 {
      font-family: monospace;
      font-size: 0.85rem;
      margin-bottom: 0.4rem;
    }

    .for-card    h3 { color: #60a5fa; }
    .while-card  h3 { color: #4ade80; }
    .forof-card  h3 { color: #c084fc; }

    .when-card p {
      font-size: 0.78rem;
      color: #64748b;
      line-height: 1.5;
    }
  </style>
</head>
<body>

<h1>Loop Types Comparison</h1>
<p class="subtitle">Three loops. Same array. Step through to see how each one works.</p>

<!-- Data display -->
<div class="data-panel">
  <span class="data-label">const fruits =</span>
  <div class="data-items" id="data-items"></div>
</div>

<!-- Three panels -->
<div class="panel-grid">

  <!-- for loop -->
  <div class="loop-panel for-panel">
    <div class="loop-panel-header">
      <span class="loop-type-label">for loop</span>
      <span class="iteration-badge" id="for-badge">iteration 0 / 0</span>
    </div>
    <div class="code-snip"><span class="ck">for</span> (<span class="ck">let</span> <span class="cv">i</span> = <span class="cn">0</span>; <span class="cv">i</span> &lt; fruits.length; <span class="cv">i</span>++) {
  console.log(fruits[<span class="cv">i</span>]);
}</div>
    <div class="step-area">
      <ul class="step-list" id="for-steps"></ul>
      <div class="current-item-display" id="for-current"></div>
    </div>
  </div>

  <!-- while loop -->
  <div class="loop-panel while-panel">
    <div class="loop-panel-header">
      <span class="loop-type-label">while loop</span>
      <span class="iteration-badge" id="while-badge">iteration 0 / 0</span>
    </div>
    <div class="code-snip"><span class="ck">let</span> <span class="cv">i</span> = <span class="cn">0</span>;
<span class="ck">while</span> (<span class="cv">i</span> &lt; fruits.length) {
  console.log(fruits[<span class="cv">i</span>]);
  <span class="cv">i</span>++;
}</div>
    <div class="step-area">
      <ul class="step-list" id="while-steps"></ul>
      <div class="current-item-display" id="while-current"></div>
    </div>
  </div>

  <!-- for...of loop -->
  <div class="loop-panel forof-panel">
    <div class="loop-panel-header">
      <span class="loop-type-label">for...of loop</span>
      <span class="iteration-badge" id="forof-badge">iteration 0 / 0</span>
    </div>
    <div class="code-snip"><span class="ck">for</span> (<span class="ck">const</span> <span class="cv">fruit</span> <span class="ck">of</span> fruits) {
  console.log(<span class="cv">fruit</span>);
}</div>
    <div class="step-area">
      <ul class="step-list" id="forof-steps"></ul>
      <div class="current-item-display" id="forof-current"></div>
    </div>
  </div>

</div>

<!-- Controls -->
<div class="loop-panel" style="padding:1rem 1.25rem; margin-bottom:1.25rem;">
  <div class="controls-row">
    <button class="btn-step" id="btn-step">▶ Step All</button>
    <button class="btn-run"  id="btn-run">⚡ Run All</button>
    <button class="btn-reset" id="btn-reset">↺ Reset</button>
    <span style="font-size:0.82rem;color:#64748b;" id="status-msg">Press Step to advance one iteration at a time</span>
  </div>
</div>

<!-- When to use -->
<div class="when-to-use">
  <h2>When to use each loop</h2>
  <div class="when-grid">
    <div class="when-card for-card">
      <h3>for</h3>
      <p>When you need the index, or precise control over start/step/end. Also when iterating backward or with non-1 steps.</p>
    </div>
    <div class="when-card while-card">
      <h3>while</h3>
      <p>When the number of iterations is unknown — waiting for user input, retrying an operation, game loops.</p>
    </div>
    <div class="when-card forof-card">
      <h3>for...of</h3>
      <p>The modern default for arrays, strings, NodeLists, Sets. Cleaner code, no index math, no off-by-one risk.</p>
    </div>
  </div>
</div>

<script>
  const fruits = ['🍎 Apple', '🍌 Banana', '🍒 Cherry', '🍇 Grape', '🥝 Kiwi'];

  // Populate data chips
  const dataItems = document.getElementById('data-items');
  fruits.forEach((f, i) => {
    const chip = document.createElement('div');
    chip.className = 'data-chip';
    chip.innerHTML = `<span class="chip-index">[${i}]</span>${f}`;
    dataItems.appendChild(chip);
  });

  // State
  let currentStep = 0;
  const total = fruits.length;
  let runTimer = null;

  // Build step lists
  function buildSteps(ulId, makeText) {
    const ul = document.getElementById(ulId);
    ul.innerHTML = '';
    fruits.forEach((f, i) => {
      const li = document.createElement('li');
      li.className = 'step-item';
      li.innerHTML = `<span class="step-num">${i + 1}</span><span class="step-arrow">▶</span>${makeText(f, i)}`;
      ul.appendChild(li);
    });
    return ul;
  }

  const forUl    = buildSteps('for-steps',    (f, i) => `fruits[${i}] → "${f}"`);
  const whileUl  = buildSteps('while-steps',  (f, i) => `i=${i}, fruits[${i}] → "${f}"`);
  const forofUl  = buildSteps('forof-steps',  (f) => `fruit = "${f}"`);

  function updatePanels(step) {
    ['for', 'while', 'forof'].forEach(type => {
      const ul = document.getElementById(`${type}-steps`);
      const items = ul.querySelectorAll('.step-item');
      items.forEach((item, i) => {
        item.classList.remove('active', 'done');
        if (i < step)       item.classList.add('done');
        else if (i === step) item.classList.add('active');
      });

      const badge   = document.getElementById(`${type}-badge`);
      const current = document.getElementById(`${type}-current`);

      badge.textContent = `iteration ${Math.min(step + 1, total)} / ${total}`;

      if (step < total) {
        const f = fruits[step];
        if (type === 'for')   current.innerHTML = `<span class="hi">i = ${step}</span>, fruits[${step}] = "${f}"`;
        if (type === 'while') current.innerHTML = `<span class="hi">i = ${step}</span> &lt; ${total} → true → "${f}"`;
        if (type === 'forof') current.innerHTML = `<span class="hi">fruit</span> = "${f}"`;
      } else {
        current.innerHTML = `<span style="color:#4ade80">✓ Loop complete</span>`;
        badge.textContent = `done — ${total} iterations`;
      }
    });
  }

  function step() {
    if (currentStep >= total) return;
    updatePanels(currentStep);
    currentStep++;
    updateButtons();
    if (currentStep >= total) {
      document.getElementById('status-msg').textContent = 'All loops finished — same result, different syntax!';
    }
  }

  function reset() {
    clearInterval(runTimer);
    currentStep = 0;
    ['for', 'while', 'forof'].forEach(type => {
      const ul = document.getElementById(`${type}-steps`);
      ul.querySelectorAll('.step-item').forEach(li => li.classList.remove('active','done'));
      document.getElementById(`${type}-badge`).textContent   = `iteration 0 / ${total}`;
      document.getElementById(`${type}-current`).innerHTML   = '';
    });
    document.getElementById('status-msg').textContent = 'Press Step to advance one iteration at a time';
    updateButtons();
  }

  function updateButtons() {
    const done = currentStep >= total;
    document.getElementById('btn-step').disabled = done;
    document.getElementById('btn-run').disabled  = done;
  }

  document.getElementById('btn-step').addEventListener('click', step);

  document.getElementById('btn-run').addEventListener('click', () => {
    document.getElementById('btn-run').disabled  = true;
    document.getElementById('btn-step').disabled = true;
    document.getElementById('status-msg').textContent = 'Running...';
    runTimer = setInterval(() => {
      if (currentStep >= total) { clearInterval(runTimer); return; }
      step();
    }, 600);
  });

  document.getElementById('btn-reset').addEventListener('click', reset);

  updateButtons();
</script>
</body>
</html>
```

---

## CODEPEN 3 — HTML Generator: Lists and Cards

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HTML Generator: Lists and Cards</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f8fafc;
      color: #1e293b;
      padding: 1.25rem;
    }

    h1 {
      font-size: 1.3rem;
      color: #0f172a;
      margin-bottom: 0.25rem;
    }

    .subtitle {
      font-size: 0.85rem;
      color: #64748b;
      margin-bottom: 1.25rem;
    }

    /* Input panel */
    .input-panel {
      background: #fff;
      border: 1.5px solid #e2e8f0;
      border-radius: 10px;
      padding: 1.1rem;
      margin-bottom: 1rem;
    }

    .input-panel h2 {
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #64748b;
      margin-bottom: 0.75rem;
    }

    .item-list {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      margin-bottom: 0.75rem;
    }

    .item-row {
      display: flex;
      gap: 0.4rem;
      align-items: center;
    }

    .item-input {
      flex: 1;
      padding: 0.4rem 0.65rem;
      border: 1.5px solid #e2e8f0;
      border-radius: 6px;
      font-size: 0.9rem;
      color: #0f172a;
    }

    .item-input:focus { outline: none; border-color: #6366f1; }

    .remove-btn {
      padding: 0.35rem 0.55rem;
      background: #fee2e2;
      color: #b91c1c;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 700;
    }

    .remove-btn:hover { background: #fecaca; }

    .btn-row {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    button {
      padding: 0.4rem 0.9rem;
      border: none;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: opacity 0.15s;
    }

    .btn-add      { background: #e0e7ff; color: #4338ca; }
    .btn-add:hover{ background: #c7d2fe; }
    .btn-generate { background: #6366f1; color: #fff; }
    .btn-generate:hover { background: #4f46e5; }

    /* Output type toggle */
    .toggle-group {
      display: flex;
      background: #f1f5f9;
      border-radius: 8px;
      padding: 3px;
      gap: 2px;
      width: fit-content;
      margin-bottom: 1rem;
    }

    .toggle-group button {
      padding: 0.35rem 0.9rem;
      border-radius: 6px;
      background: transparent;
      color: #64748b;
      font-size: 0.82rem;
      font-weight: 600;
      transition: background 0.15s, color 0.15s;
    }

    .toggle-group button.active {
      background: #fff;
      color: #0f172a;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    /* Method toggle */
    .method-row {
      display: flex;
      gap: 0.75rem;
      align-items: center;
      margin-bottom: 1rem;
      font-size: 0.85rem;
    }

    .method-row label { color: #64748b; }

    .method-btn {
      padding: 0.3rem 0.75rem;
      border-radius: 6px;
      background: #f1f5f9;
      color: #475569;
      border: 1.5px solid #e2e8f0;
      font-size: 0.82rem;
    }

    .method-btn.active { border-color: #6366f1; color: #4338ca; background: #e0e7ff; }

    /* Generated output area */
    .output-section { margin-bottom: 1rem; }

    .output-section h2 {
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #64748b;
      margin-bottom: 0.6rem;
    }

    .output-container {
      background: #fff;
      border: 1.5px solid #e2e8f0;
      border-radius: 10px;
      padding: 1.1rem;
      min-height: 80px;
    }

    /* List output */
    .output-container ul {
      padding-left: 1.25rem;
    }

    .output-container li {
      padding: 0.3rem 0;
      color: #334155;
      font-size: 0.95rem;
      border-bottom: 1px solid #f1f5f9;
    }

    .output-container li:last-child { border-bottom: none; }

    /* Card output */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
      gap: 0.75rem;
    }

    .gen-card {
      background: linear-gradient(135deg, #6366f1, #8b5cf6);
      color: #fff;
      border-radius: 10px;
      padding: 1rem 0.75rem;
      text-align: center;
      font-weight: 600;
      font-size: 0.9rem;
      box-shadow: 0 4px 12px rgba(99,102,241,0.3);
      animation: pop 0.25s ease-out;
    }

    @keyframes pop {
      from { transform: scale(0.85); opacity: 0; }
      to   { transform: scale(1);    opacity: 1; }
    }

    .gen-card .card-num {
      font-size: 0.65rem;
      opacity: 0.7;
      margin-bottom: 0.3rem;
    }

    /* Table output */
    .output-container table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
    }

    .output-container th {
      background: #f8fafc;
      padding: 0.5rem 0.75rem;
      text-align: left;
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #64748b;
      border-bottom: 2px solid #e2e8f0;
    }

    .output-container td {
      padding: 0.5rem 0.75rem;
      color: #334155;
      border-bottom: 1px solid #f1f5f9;
    }

    .output-container tr:last-child td { border-bottom: none; }
    .output-container tr:hover td { background: #f8fafc; }

    /* Code panel */
    .code-panel {
      background: #1e293b;
      border-radius: 10px;
      padding: 1rem;
    }

    .code-panel h2 {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      color: #64748b;
      margin-bottom: 0.65rem;
    }

    pre {
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      line-height: 1.65;
      color: #cbd5e1;
      white-space: pre-wrap;
      word-break: break-word;
    }

    .kw { color: #c084fc; }
    .fn { color: #38bdf8; }
    .st { color: #86efac; }
    .co { color: #475569; }
    .va { color: #fbbf24; }
  </style>
</head>
<body>

<h1>HTML Generator: Lists, Cards, and Tables</h1>
<p class="subtitle">Add items, pick an output format, pick a method, then click Generate.</p>

<!-- Input panel -->
<div class="input-panel">
  <h2>Data Items</h2>
  <div class="item-list" id="item-list"></div>
  <div class="btn-row">
    <button class="btn-add" id="add-btn">+ Add Item</button>
    <button class="btn-generate" id="generate-btn">⚡ Generate HTML</button>
  </div>
</div>

<!-- Format + method toggles -->
<div style="display:flex; gap:1rem; flex-wrap:wrap; align-items:center; margin-bottom:1rem;">
  <div>
    <div style="font-size:0.75rem;color:#64748b;margin-bottom:0.3rem;">Output Format</div>
    <div class="toggle-group">
      <button class="active" data-format="list">List</button>
      <button data-format="cards">Cards</button>
      <button data-format="table">Table</button>
    </div>
  </div>
  <div>
    <div style="font-size:0.75rem;color:#64748b;margin-bottom:0.3rem;">JS Method</div>
    <div class="method-row" style="margin-bottom:0;">
      <button class="method-btn active" data-method="innerHTML">innerHTML</button>
      <button class="method-btn" data-method="createElement">createElement</button>
    </div>
  </div>
</div>

<!-- Output -->
<div class="output-section">
  <h2>Rendered Output</h2>
  <div class="output-container" id="output-container">
    <p style="color:#94a3b8;font-style:italic;font-size:0.85rem;">Click "Generate HTML" to see your output here.</p>
  </div>
</div>

<!-- Code display -->
<div class="code-panel">
  <h2>The JavaScript Code Used</h2>
  <pre id="code-display"></pre>
</div>

<script>
  const defaultItems = ['Buy groceries', 'Call the dentist', 'Read a book', 'Go for a walk', 'Water the plants'];

  let currentFormat = 'list';
  let currentMethod = 'innerHTML';

  const itemList   = document.getElementById('item-list');
  const outputEl   = document.getElementById('output-container');
  const codeEl     = document.getElementById('code-display');

  function createItemRow(value = '') {
    const row = document.createElement('div');
    row.className = 'item-row';

    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'item-input';
    input.value = value;
    input.placeholder = 'Item text...';

    const removeBtn = document.createElement('button');
    removeBtn.className = 'remove-btn';
    removeBtn.textContent = '✕';
    removeBtn.addEventListener('click', () => {
      row.remove();
    });

    row.appendChild(input);
    row.appendChild(removeBtn);
    return row;
  }

  function getItems() {
    return [...itemList.querySelectorAll('.item-input')]
      .map(inp => inp.value.trim())
      .filter(v => v.length > 0);
  }

  // Init default items
  defaultItems.forEach(text => itemList.appendChild(createItemRow(text)));

  document.getElementById('add-btn').addEventListener('click', () => {
    itemList.appendChild(createItemRow());
    itemList.lastElementChild.querySelector('input').focus();
  });

  // Format toggles
  document.querySelectorAll('.toggle-group button').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.toggle-group button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFormat = btn.dataset.format;
    });
  });

  // Method toggles
  document.querySelectorAll('.method-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.method-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentMethod = btn.dataset.method;
    });
  });

  function generateInnerHTML(items) {
    let code = '';
    let htmlStr = '';

    if (currentFormat === 'list') {
      code = `const items = ${JSON.stringify(items)};\nlet html = '';\n\nfor (const item of items) {\n  html += \`<li>\${item}</li>\`;\n}\n\ncontainer.innerHTML = \`<ul>\${html}</ul>\`;`;
      let inner = '';
      for (const item of items) { inner += `<li>${item}</li>`; }
      outputEl.innerHTML = `<ul>${inner}</ul>`;

    } else if (currentFormat === 'cards') {
      code = `const items = ${JSON.stringify(items)};\nlet html = '';\n\nfor (const [i, item] of items.entries()) {\n  html += \`\n    <div class="gen-card">\n      <div class="card-num">#\${i + 1}</div>\n      \${item}\n    </div>\n  \`;\n}\n\ncontainer.innerHTML = \`<div class="card-grid">\${html}</div>\`;`;
      let inner = '';
      for (const [i, item] of items.entries()) {
        inner += `<div class="gen-card"><div class="card-num">#${i + 1}</div>${item}</div>`;
      }
      outputEl.innerHTML = `<div class="card-grid">${inner}</div>`;

    } else {
      code = `const items = ${JSON.stringify(items)};\nlet html = '<table><thead><tr><th>#</th><th>Item</th></tr></thead><tbody>';\n\nfor (const [i, item] of items.entries()) {\n  html += \`<tr><td>\${i + 1}</td><td>\${item}</td></tr>\`;\n}\n\nhtml += '</tbody></table>';\ncontainer.innerHTML = html;`;
      let rows = '';
      for (const [i, item] of items.entries()) { rows += `<tr><td>${i + 1}</td><td>${item}</td></tr>`; }
      outputEl.innerHTML = `<table><thead><tr><th>#</th><th>Item</th></tr></thead><tbody>${rows}</tbody></table>`;
    }

    return code;
  }

  function generateCreateElement(items) {
    let code = '';

    if (currentFormat === 'list') {
      code = `const items = ${JSON.stringify(items)};\nconst ul = document.createElement('ul');\n\nfor (const item of items) {\n  const li = document.createElement('li');\n  li.textContent = item;\n  // attach listeners here if needed\n  ul.appendChild(li);\n}\n\ncontainer.innerHTML = '';\ncontainer.appendChild(ul);`;

      const ul = document.createElement('ul');
      for (const item of items) {
        const li = document.createElement('li');
        li.textContent = item;
        ul.appendChild(li);
      }
      outputEl.innerHTML = '';
      outputEl.appendChild(ul);

    } else if (currentFormat === 'cards') {
      code = `const items = ${JSON.stringify(items)};\nconst grid = document.createElement('div');\ngrid.className = 'card-grid';\n\nfor (const [i, item] of items.entries()) {\n  const card = document.createElement('div');\n  card.className = 'gen-card';\n  card.innerHTML = \`<div class="card-num">#\${i+1}</div>\${item}\`;\n  card.addEventListener('click', () => alert(item));\n  grid.appendChild(card);\n}\n\ncontainer.innerHTML = '';\ncontainer.appendChild(grid);`;

      const grid = document.createElement('div');
      grid.className = 'card-grid';
      for (const [i, item] of items.entries()) {
        const card = document.createElement('div');
        card.className = 'gen-card';
        card.innerHTML = `<div class="card-num">#${i+1}</div>${item}`;
        card.style.cursor = 'pointer';
        card.title = 'Click me!';
        card.addEventListener('click', () => alert(`You clicked: ${item}`));
        grid.appendChild(card);
      }
      outputEl.innerHTML = '';
      outputEl.appendChild(grid);

    } else {
      code = `const items = ${JSON.stringify(items)};\nconst table  = document.createElement('table');\nconst thead  = document.createElement('thead');\nconst tbody  = document.createElement('tbody');\n\nthead.innerHTML = '<tr><th>#</th><th>Item</th></tr>';\ntable.appendChild(thead);\n\nfor (const [i, item] of items.entries()) {\n  const tr = document.createElement('tr');\n  tr.innerHTML = \`<td>\${i + 1}</td><td>\${item}</td>\`;\n  tbody.appendChild(tr);\n}\n\ntable.appendChild(tbody);\ncontainer.innerHTML = '';\ncontainer.appendChild(table);`;

      const table = document.createElement('table');
      const thead = document.createElement('thead');
      const tbody = document.createElement('tbody');
      thead.innerHTML = '<tr><th>#</th><th>Item</th></tr>';
      table.appendChild(thead);
      for (const [i, item] of items.entries()) {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${i + 1}</td><td>${item}</td>`;
        tbody.appendChild(tr);
      }
      table.appendChild(tbody);
      outputEl.innerHTML = '';
      outputEl.appendChild(table);
    }

    return code;
  }

  document.getElementById('generate-btn').addEventListener('click', () => {
    const items = getItems();
    if (items.length === 0) {
      outputEl.innerHTML = '<p style="color:#ef4444;">Add at least one item first.</p>';
      codeEl.textContent = '';
      return;
    }

    let code = currentMethod === 'innerHTML'
      ? generateInnerHTML(items)
      : generateCreateElement(items);

    codeEl.textContent = code;
  });
</script>
</body>
</html>
```

---

## CODEPEN 4 — Product Card Grid from Data

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Card Grid</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f1f5f9;
      color: #1e293b;
      padding: 1.25rem;
    }

    h1 {
      font-size: 1.3rem;
      color: #0f172a;
      margin-bottom: 0.25rem;
    }

    .subtitle {
      font-size: 0.85rem;
      color: #64748b;
      margin-bottom: 1.25rem;
    }

    /* Filter bar */
    .filter-bar {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      align-items: center;
      margin-bottom: 1rem;
    }

    .filter-btn {
      padding: 0.4rem 0.9rem;
      border: 1.5px solid #e2e8f0;
      border-radius: 20px;
      background: #fff;
      color: #64748b;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }

    .filter-btn:hover { border-color: #6366f1; color: #4338ca; }

    .filter-btn.active {
      background: #6366f1;
      color: #fff;
      border-color: #6366f1;
    }

    /* Sort / count row */
    .action-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .item-count {
      font-size: 0.82rem;
      color: #64748b;
    }

    .item-count strong { color: #0f172a; }

    .sort-btn {
      padding: 0.38rem 0.85rem;
      border: 1.5px solid #e2e8f0;
      border-radius: 8px;
      background: #fff;
      color: #334155;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: border-color 0.15s;
    }

    .sort-btn:hover { border-color: #6366f1; color: #4338ca; }
    .sort-btn.asc::after  { content: ' ↑'; }
    .sort-btn.desc::after { content: ' ↓'; }

    /* Card grid */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
      gap: 1rem;
    }

    /* Individual card */
    .product-card {
      background: #fff;
      border: 1.5px solid #e2e8f0;
      border-radius: 14px;
      padding: 1.1rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      transition: transform 0.2s, box-shadow 0.2s;
      animation: fadeUp 0.3s ease-out;
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(12px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    .product-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 10px 30px rgba(0,0,0,0.10);
    }

    .card-icon {
      font-size: 2.2rem;
      line-height: 1;
    }

    .card-name {
      font-size: 0.95rem;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.3;
    }

    .card-category {
      display: inline-block;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.15rem 0.55rem;
      border-radius: 10px;
      width: fit-content;
    }

    .cat-Electronics { background: #dbeafe; color: #1d4ed8; }
    .cat-Furniture   { background: #dcfce7; color: #166534; }
    .cat-Audio       { background: #fae8ff; color: #7e22ce; }
    .cat-Accessories { background: #fef9c3; color: #854d0e; }
    .cat-Lighting    { background: #ffedd5; color: #9a3412; }
    .cat-Storage     { background: #f0fdf4; color: #166534; }

    .card-stars {
      font-size: 0.95rem;
      color: #f59e0b;
      letter-spacing: 0.05em;
    }

    .card-rating-num {
      font-size: 0.75rem;
      color: #94a3b8;
      margin-left: 0.25rem;
    }

    .card-price {
      font-size: 1.1rem;
      font-weight: 800;
      color: #0f172a;
      margin-top: auto;
    }

    /* Empty state */
    .empty-state {
      grid-column: 1 / -1;
      text-align: center;
      padding: 3rem 1rem;
      color: #94a3b8;
    }

    .empty-state p { font-size: 0.95rem; margin-top: 0.5rem; }
  </style>
</head>
<body>

<h1>Product Card Grid</h1>
<p class="subtitle">Filter by category or sort by price — all powered by looping over data.</p>

<div class="filter-bar" id="filter-bar"></div>

<div class="action-bar">
  <div class="item-count" id="item-count"></div>
  <button class="sort-btn" id="sort-btn">Sort by Price</button>
</div>

<div class="card-grid" id="card-grid"></div>

<script>
  const products = [
    { name: "Mechanical Keyboard",  price: 129.99, category: "Electronics",  rating: 4.5, icon: "⌨️"  },
    { name: "Ergonomic Mouse",       price: 59.99,  category: "Electronics",  rating: 4.2, icon: "🖱️"  },
    { name: "Standing Desk Mat",     price: 34.99,  category: "Furniture",    rating: 4.8, icon: "🟩"  },
    { name: "USB-C Hub 7-Port",      price: 49.99,  category: "Electronics",  rating: 3.9, icon: "🔌"  },
    { name: "Noise-Cancel Headphones", price: 199.99, category: "Audio",      rating: 4.7, icon: "🎧"  },
    { name: "Monitor Light Bar",     price: 44.99,  category: "Lighting",     rating: 4.3, icon: "💡"  },
    { name: "Laptop Stand",          price: 39.99,  category: "Furniture",    rating: 4.6, icon: "💻"  },
    { name: "Cable Management Box",  price: 24.99,  category: "Storage",      rating: 4.1, icon: "📦"  },
    { name: "Webcam 1080p",          price: 79.99,  category: "Electronics",  rating: 4.0, icon: "📷"  },
    { name: "Desk Organizer",        price: 27.99,  category: "Accessories",  rating: 4.4, icon: "🗂️"  },
  ];

  let activeCategory = 'All';
  let sortDir = null; // null | 'asc' | 'desc'

  function getStars(rating) {
    const full  = Math.floor(rating);
    const empty = 5 - full;
    return '★'.repeat(full) + '☆'.repeat(empty);
  }

  function getFilteredSorted() {
    let data = activeCategory === 'All'
      ? [...products]
      : products.filter(p => p.category === activeCategory);

    if (sortDir === 'asc')  data.sort((a, b) => a.price - b.price);
    if (sortDir === 'desc') data.sort((a, b) => b.price - a.price);

    return data;
  }

  function renderCards() {
    const grid = document.getElementById('card-grid');
    const data = getFilteredSorted();

    document.getElementById('item-count').innerHTML =
      `Showing <strong>${data.length}</strong> of <strong>${products.length}</strong> products`;

    if (data.length === 0) {
      grid.innerHTML = `
        <div class="empty-state">
          <div style="font-size:2.5rem">🔍</div>
          <p>No products in this category.</p>
        </div>`;
      return;
    }

    let html = '';

    for (const product of data) {
      const stars = getStars(product.rating);
      const catClass = `cat-${product.category}`;

      html += `
        <div class="product-card">
          <div class="card-icon">${product.icon}</div>
          <div class="card-name">${product.name}</div>
          <span class="card-category ${catClass}">${product.category}</span>
          <div class="card-stars">
            ${stars}<span class="card-rating-num">${product.rating}</span>
          </div>
          <div class="card-price">$${product.price.toFixed(2)}</div>
        </div>`;
    }

    grid.innerHTML = html;
  }

  function buildFilters() {
    const categories = ['All', ...new Set(products.map(p => p.category))];
    const bar = document.getElementById('filter-bar');

    for (const cat of categories) {
      const btn = document.createElement('button');
      btn.className = 'filter-btn' + (cat === 'All' ? ' active' : '');
      btn.textContent = cat;
      btn.addEventListener('click', () => {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeCategory = cat;
        renderCards();
      });
      bar.appendChild(btn);
    }
  }

  // Sort button cycles: none → asc → desc → none
  document.getElementById('sort-btn').addEventListener('click', function() {
    if (sortDir === null)   { sortDir = 'asc';  this.className = 'sort-btn asc';  }
    else if (sortDir === 'asc')  { sortDir = 'desc'; this.className = 'sort-btn desc'; }
    else                         { sortDir = null;   this.className = 'sort-btn';      }
    renderCards();
  });

  buildFilters();
  renderCards();
</script>
</body>
</html>
```

---

## CODEPEN 5 — Array.from() Pattern Lab

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Array.from() Pattern Lab</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      padding: 1.25rem;
    }

    h1 {
      font-size: 1.3rem;
      color: #7dd3fc;
      margin-bottom: 0.25rem;
      text-align: center;
    }

    .subtitle {
      text-align: center;
      font-size: 0.82rem;
      color: #64748b;
      margin-bottom: 1.5rem;
    }

    /* Section panels */
    .demo-section {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 1.25rem;
      margin-bottom: 1.25rem;
    }

    .demo-section h2 {
      font-size: 0.95rem;
      color: #7dd3fc;
      margin-bottom: 0.25rem;
    }

    .demo-section .desc {
      font-size: 0.8rem;
      color: #64748b;
      margin-bottom: 1rem;
      line-height: 1.5;
    }

    .code-snip {
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 0.65rem 0.9rem;
      margin-bottom: 0.9rem;
      color: #94a3b8;
      line-height: 1.65;
      white-space: pre-wrap;
    }

    .kw { color: #c084fc; }
    .fn { color: #38bdf8; }
    .st { color: #86efac; }
    .nu { color: #fb923c; }
    .va { color: #fbbf24; }
    .co { color: #475569; }

    /* Controls row */
    .ctrl-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
      margin-bottom: 0.75rem;
    }

    .ctrl-row label {
      font-size: 0.82rem;
      color: #94a3b8;
    }

    input[type="range"] {
      accent-color: #6366f1;
      cursor: pointer;
    }

    input[type="number"] {
      width: 64px;
      padding: 0.3rem 0.5rem;
      background: #0f172a;
      border: 1.5px solid #475569;
      border-radius: 6px;
      color: #e2e8f0;
      font-size: 0.9rem;
      text-align: center;
    }

    input[type="number"]:focus { outline: none; border-color: #6366f1; }

    .val-display {
      font-family: monospace;
      font-size: 0.9rem;
      color: #f1f5f9;
      min-width: 2ch;
    }

    /* Star rating */
    .stars-output {
      font-size: 2rem;
      letter-spacing: 0.1em;
      line-height: 1;
      margin-bottom: 0.4rem;
    }

    .star-filled { color: #f59e0b; }
    .star-empty  { color: #334155; }

    .stars-label {
      font-size: 0.8rem;
      color: #64748b;
      font-family: monospace;
    }

    /* Grid builder */
    .cell-grid {
      display: grid;
      gap: 4px;
      width: fit-content;
      max-width: 100%;
    }

    .grid-cell {
      width: 38px;
      height: 38px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.7rem;
      font-weight: 700;
      color: rgba(255,255,255,0.8);
      transition: transform 0.15s;
    }

    .grid-cell:hover { transform: scale(1.15); cursor: default; }

    /* Week display */
    .week-grid {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 6px;
    }

    .day-cell {
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 0.5rem 0.25rem;
      text-align: center;
    }

    .day-name {
      font-size: 0.65rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #64748b;
      margin-bottom: 0.3rem;
    }

    .day-num {
      font-size: 1.05rem;
      font-weight: 700;
      color: #f1f5f9;
    }

    .day-cell.today {
      border-color: #6366f1;
      background: #1e1b4b;
    }

    .day-cell.today .day-num { color: #818cf8; }

    /* Object.entries settings list */
    .settings-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }

    .settings-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 0.5rem 0.85rem;
      font-size: 0.85rem;
    }

    .setting-key   { color: #7dd3fc; font-family: monospace; }
    .setting-value { color: #86efac; font-family: monospace; }
    .setting-value.bool-true  { color: #4ade80; }
    .setting-value.bool-false { color: #f87171; }

    /* Array output readout */
    .array-output {
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      color: #64748b;
      margin-top: 0.4rem;
    }

    .array-output span { color: #fb923c; }
  </style>
</head>
<body>

<h1>Array.from() Pattern Lab</h1>
<p class="subtitle">Interactive demos of <code>Array.from()</code> and <code>Object.entries()</code></p>

<!-- Demo 1: Star Rating -->
<div class="demo-section">
  <h2>Demo 1 — Star Rating Generator</h2>
  <p class="desc"><code>Array.from({length: 5}, (_, i) =&gt; i &lt; score ? '★' : '☆')</code> builds the star string without a traditional loop.</p>

  <div class="code-snip"><span class="kw">function</span> <span class="fn">starRating</span>(score, outOf = <span class="nu">5</span>) {
  <span class="kw">return</span> <span class="fn">Array.from</span>({ length: outOf }, (<span class="va">_</span>, i) =>
    i &lt; score ? <span class="st">'★'</span> : <span class="st">'☆'</span>
  ).join(<span class="st">''</span>);
}</div>

  <div class="ctrl-row">
    <label>Score:</label>
    <input type="range" id="star-range" min="0" max="5" step="0.5" value="3.5">
    <span class="val-display" id="star-val">3.5</span>
    <label>Out of:</label>
    <input type="number" id="star-outof" min="3" max="10" value="5">
  </div>

  <div class="stars-output" id="stars-display"></div>
  <div class="stars-label"  id="stars-label"></div>
  <div class="array-output" id="stars-array"></div>
</div>

<!-- Demo 2: Grid Builder -->
<div class="demo-section">
  <h2>Demo 2 — Grid Builder</h2>
  <p class="desc"><code>Array.from({length: n * n}, (_, i) =&gt; ...)</code> creates a flat list of cells that CSS grid turns into a square grid.</p>

  <div class="code-snip"><span class="kw">const</span> cells = <span class="fn">Array.from</span>(
  { length: cols * rows },
  (<span class="va">_</span>, i) => <span class="st">`&lt;div class="cell"&gt;\${i + 1}&lt;/div&gt;`</span>
);
container.innerHTML = cells.join(<span class="st">''</span>);</div>

  <div class="ctrl-row">
    <label>Columns:</label>
    <input type="range" id="grid-cols" min="2" max="8" value="4">
    <span class="val-display" id="grid-cols-val">4</span>
    <label>Rows:</label>
    <input type="range" id="grid-rows" min="2" max="8" value="4">
    <span class="val-display" id="grid-rows-val">4</span>
  </div>

  <div id="grid-container"></div>
  <div class="array-output" id="grid-info"></div>
</div>

<!-- Demo 3: Calendar Week -->
<div class="demo-section">
  <h2>Demo 3 — Calendar Week</h2>
  <p class="desc"><code>Array.from({length: 7}, (_, i) =&gt; ...)</code> generates 7 day cells for a week view. Today is highlighted.</p>

  <div class="code-snip"><span class="kw">const</span> dayNames = [<span class="st">'Sun'</span>, <span class="st">'Mon'</span>, ..., <span class="st">'Sat'</span>];
<span class="kw">const</span> today = <span class="kw">new</span> <span class="fn">Date</span>();

<span class="fn">Array.from</span>({ length: <span class="nu">7</span> }, (<span class="va">_</span>, i) => {
  <span class="kw">const</span> d = <span class="kw">new</span> <span class="fn">Date</span>(weekStart);
  d.setDate(weekStart.getDate() + i);
  <span class="kw">return</span> d;
});</div>

  <div id="week-grid" class="week-grid"></div>
</div>

<!-- Demo 4: Object.entries -->
<div class="demo-section">
  <h2>Demo 4 — Object.entries() Settings List</h2>
  <p class="desc"><code>Object.entries(config)</code> returns <code>[key, value]</code> pairs you can loop over with <code>for...of</code>, turning a plain object into a rendered list.</p>

  <div class="code-snip"><span class="kw">for</span> (<span class="kw">const</span> [key, value] <span class="kw">of</span> <span class="fn">Object.entries</span>(config)) {
  html += <span class="st">`&lt;li&gt;&lt;strong&gt;\${key}&lt;/strong&gt;: \${value}&lt;/li&gt;`</span>;
}</div>

  <ul class="settings-list" id="settings-list"></ul>
</div>

<script>
  // ---- Demo 1: Star Rating ----
  const starRange  = document.getElementById('star-range');
  const starOutof  = document.getElementById('star-outof');
  const starVal    = document.getElementById('star-val');
  const starsDisp  = document.getElementById('stars-display');
  const starsLabel = document.getElementById('stars-label');
  const starsArr   = document.getElementById('stars-array');

  function renderStars() {
    const score = parseFloat(starRange.value);
    const outOf = parseInt(starOutof.value) || 5;
    starVal.textContent = score;

    const starsArray = Array.from({ length: outOf }, (_, i) => {
      if (i < Math.floor(score)) return { char: '★', cls: 'star-filled' };
      if (i < score)             return { char: '½', cls: 'star-filled' };
      return                            { char: '☆', cls: 'star-empty'  };
    });

    starsDisp.innerHTML = starsArray
      .map(s => `<span class="${s.cls}">${s.char}</span>`)
      .join('');

    starsLabel.textContent = `Array.from({length: ${outOf}}, ...) → ${starsArray.map(s => `"${s.char}"`).join(', ')}`;
    starsArr.innerHTML   = `<span>Result array:</span> [${starsArray.map(s => `"${s.char}"`).join(', ')}]`;
  }

  starRange.addEventListener('input', renderStars);
  starOutof.addEventListener('input', renderStars);
  renderStars();

  // ---- Demo 2: Grid Builder ----
  const gridColsRange = document.getElementById('grid-cols');
  const gridRowsRange = document.getElementById('grid-rows');
  const gridColsVal   = document.getElementById('grid-cols-val');
  const gridRowsVal   = document.getElementById('grid-rows-val');
  const gridContainer = document.getElementById('grid-container');
  const gridInfo      = document.getElementById('grid-info');

  // Color palette for cells
  const cellColors = [
    '#1d4ed8','#0369a1','#047857','#7c3aed',
    '#be185d','#b45309','#0f766e','#6d28d9',
    '#dc2626','#059669','#4338ca','#d97706',
  ];

  function renderGrid() {
    const cols = parseInt(gridColsRange.value);
    const rows = parseInt(gridRowsRange.value);
    const total = cols * rows;
    gridColsVal.textContent = cols;
    gridRowsVal.textContent = rows;

    const cells = Array.from({ length: total }, (_, i) => {
      const color = cellColors[i % cellColors.length];
      return `<div class="grid-cell" style="background:${color}" title="Cell ${i+1}">${i + 1}</div>`;
    });

    gridContainer.innerHTML = `<div class="cell-grid" style="grid-template-columns:repeat(${cols},38px);">${cells.join('')}</div>`;
    gridInfo.innerHTML = `<span>Array.from(&#123;length: ${cols} × ${rows} = ${total}&#125;, (_, i) =&gt; ...)</span> — ${total} cells generated`;
  }

  gridColsRange.addEventListener('input', renderGrid);
  gridRowsRange.addEventListener('input', renderGrid);
  renderGrid();

  // ---- Demo 3: Calendar Week ----
  function renderWeek() {
    const dayNames  = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const today     = new Date();
    const weekStart = new Date(today);
    weekStart.setDate(today.getDate() - today.getDay()); // Sunday of this week

    const weekDays = Array.from({ length: 7 }, (_, i) => {
      const d = new Date(weekStart);
      d.setDate(weekStart.getDate() + i);
      return d;
    });

    const weekGrid = document.getElementById('week-grid');
    weekGrid.innerHTML = weekDays.map((d, i) => {
      const isToday = d.toDateString() === today.toDateString();
      return `
        <div class="day-cell${isToday ? ' today' : ''}">
          <div class="day-name">${dayNames[i]}</div>
          <div class="day-num">${d.getDate()}</div>
        </div>`;
    }).join('');
  }

  renderWeek();

  // ---- Demo 4: Object.entries ----
  const appConfig = {
    theme:       'dark',
    language:    'en-US',
    fontSize:    16,
    animations:  true,
    autoSave:    true,
    tabSize:     2,
    lineNumbers: true,
    wordWrap:    false,
  };

  function renderSettings() {
    const ul = document.getElementById('settings-list');
    ul.innerHTML = '';

    for (const [key, value] of Object.entries(appConfig)) {
      const li = document.createElement('li');
      li.className = 'settings-item';

      let valueClass = 'setting-value';
      if (value === true)  valueClass += ' bool-true';
      if (value === false) valueClass += ' bool-false';

      li.innerHTML = `
        <span class="setting-key">${key}</span>
        <span class="${valueClass}">${JSON.stringify(value)}</span>`;
      ul.appendChild(li);
    }
  }

  renderSettings();
</script>
</body>
</html>
```
