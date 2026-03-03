# Day 28 — Local Storage & Practical Patterns: CodePens

---

## CODEPEN 1 — Theme Switcher with Persistence

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Theme Switcher with localStorage</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 24px;
      padding: 32px;
      transition: background-color 0.4s, color 0.4s;
    }

    /* Light theme (default) */
    body[data-theme="light"] {
      background: #f5f5f5;
      color: #1a1a1a;
      --card-bg: #ffffff;
      --card-border: #e0e0e0;
    }

    /* Dark theme */
    body[data-theme="dark"] {
      background: #0f0f0f;
      color: #f0f0f0;
      --card-bg: #1e1e1e;
      --card-border: #333;
    }

    h1 { font-size: 1.8rem; }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 24px 32px;
      text-align: center;
      max-width: 420px;
      width: 100%;
      transition: background 0.4s, border-color 0.4s;
    }

    .card p { opacity: 0.7; margin-top: 8px; line-height: 1.5; }

    #theme-toggle {
      padding: 10px 24px;
      border: 2px solid currentColor;
      border-radius: 999px;
      background: transparent;
      color: inherit;
      font-size: 1rem;
      cursor: pointer;
      transition: background 0.2s, color 0.2s;
    }

    #theme-toggle:hover {
      background: currentColor;
    }

    body[data-theme="light"] #theme-toggle:hover { color: #f5f5f5; }
    body[data-theme="dark"]  #theme-toggle:hover { color: #0f0f0f; }

    .status {
      font-size: 0.85rem;
      opacity: 0.55;
      font-family: monospace;
    }
  </style>
</head>
<body data-theme="light">
  <h1>Theme Switcher</h1>

  <div class="card">
    <p>Your theme preference is saved to <code>localStorage</code>. Refresh the page — it remembers which mode you chose.</p>
  </div>

  <button id="theme-toggle">☾ Dark Mode</button>

  <p class="status" id="status">localStorage: theme = "light"</p>

  <script>
    const toggle = document.querySelector('#theme-toggle');
    const statusEl = document.querySelector('#status');

    function applyTheme(theme) {
      document.body.dataset.theme = theme;
      toggle.textContent = theme === 'dark' ? '☀ Light Mode' : '☾ Dark Mode';
      statusEl.textContent = `localStorage: theme = "${theme}"`;
    }

    // Restore saved theme on load
    const saved = localStorage.getItem('theme') || 'light';
    applyTheme(saved);

    toggle.addEventListener('click', () => {
      const current = document.body.dataset.theme;
      const next = current === 'dark' ? 'light' : 'dark';
      localStorage.setItem('theme', next);
      applyTheme(next);
    });
  </script>
</body>
</html>
```

---

## CODEPEN 2 — Offline-Aware App with navigator.onLine

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Offline Detection</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f0f4f8;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 24px;
      padding: 32px;
    }

    /* Offline banner */
    #offline-banner {
      position: fixed;
      top: 0; left: 0; right: 0;
      background: #e53935;
      color: white;
      text-align: center;
      padding: 12px 16px;
      font-weight: 600;
      font-size: 0.95rem;
      transform: translateY(-100%);
      transition: transform 0.3s ease;
      z-index: 100;
    }

    #offline-banner.visible { transform: translateY(0); }

    /* Online banner */
    #online-banner {
      position: fixed;
      top: 0; left: 0; right: 0;
      background: #43a047;
      color: white;
      text-align: center;
      padding: 12px 16px;
      font-weight: 600;
      font-size: 0.95rem;
      transform: translateY(-100%);
      transition: transform 0.3s ease;
      z-index: 100;
    }

    #online-banner.visible { transform: translateY(0); }

    h1 { font-size: 1.6rem; color: #1a1a2e; }

    .status-card {
      background: white;
      border-radius: 16px;
      padding: 32px 40px;
      text-align: center;
      box-shadow: 0 4px 20px rgba(0,0,0,0.08);
      max-width: 400px;
      width: 100%;
    }

    .indicator {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-size: 1.1rem;
      font-weight: 600;
      margin: 12px 0;
    }

    .dot {
      width: 14px; height: 14px;
      border-radius: 50%;
      background: #ccc;
      transition: background 0.3s;
    }

    .dot.online  { background: #43a047; box-shadow: 0 0 8px #43a04788; }
    .dot.offline { background: #e53935; box-shadow: 0 0 8px #e5393588; }

    .instructions {
      margin-top: 20px;
      font-size: 0.85rem;
      color: #666;
      line-height: 1.6;
    }

    code {
      background: #f0f0f0;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.9em;
    }

    .simulate-btns {
      display: flex;
      gap: 10px;
      justify-content: center;
      margin-top: 20px;
    }

    .simulate-btns button {
      padding: 8px 20px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-size: 0.9rem;
      font-weight: 600;
    }

    #sim-offline {
      background: #fce4e4;
      color: #c62828;
    }

    #sim-online {
      background: #e8f5e9;
      color: #2e7d32;
    }

    .log {
      width: 100%;
      max-width: 400px;
      background: white;
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    }

    .log h3 { font-size: 0.85rem; color: #888; margin-bottom: 8px; }

    .log-list {
      list-style: none;
      font-family: monospace;
      font-size: 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 4px;
      max-height: 120px;
      overflow-y: auto;
    }

    .log-item { color: #333; }
    .log-item.offline { color: #e53935; }
    .log-item.online  { color: #43a047; }
  </style>
</head>
<body>
  <div id="offline-banner">⚠ You are offline — changes are being saved locally</div>
  <div id="online-banner">✓ Back online</div>

  <h1>Offline Detection</h1>

  <div class="status-card">
    <p>Current status:</p>
    <div class="indicator">
      <span class="dot" id="dot"></span>
      <span id="status-text">Checking…</span>
    </div>
    <div class="instructions">
      Use browser DevTools &rarr; Network tab &rarr; select <strong>Offline</strong><br>
      to simulate going offline, or use the demo buttons below.
    </div>
    <div class="simulate-btns">
      <button id="sim-offline">Simulate Offline</button>
      <button id="sim-online">Simulate Online</button>
    </div>
  </div>

  <div class="log">
    <h3>Event log</h3>
    <ul class="log-list" id="log"></ul>
  </div>

  <script>
    const offlineBanner = document.querySelector('#offline-banner');
    const onlineBanner  = document.querySelector('#online-banner');
    const dot           = document.querySelector('#dot');
    const statusText    = document.querySelector('#status-text');
    const logList       = document.querySelector('#log');

    let onlineBannerTimer = null;

    function addLog(message, type) {
      const li = document.createElement('li');
      li.className = `log-item ${type}`;
      const time = new Date().toLocaleTimeString();
      li.textContent = `[${time}] ${message}`;
      logList.prepend(li);
    }

    function setOffline() {
      dot.className = 'dot offline';
      statusText.textContent = 'Offline';
      offlineBanner.classList.add('visible');
      onlineBanner.classList.remove('visible');
      addLog('Connection lost — navigator.onLine = false', 'offline');
    }

    function setOnline() {
      dot.className = 'dot online';
      statusText.textContent = 'Online';
      offlineBanner.classList.remove('visible');

      onlineBanner.classList.add('visible');
      clearTimeout(onlineBannerTimer);
      onlineBannerTimer = setTimeout(() => {
        onlineBanner.classList.remove('visible');
      }, 2500);

      addLog('Connection restored — navigator.onLine = true', 'online');
    }

    // Real events
    window.addEventListener('offline', setOffline);
    window.addEventListener('online', setOnline);

    // Initialize from real status
    if (navigator.onLine) {
      dot.className = 'dot online';
      statusText.textContent = 'Online';
      addLog('Page loaded — navigator.onLine = true', 'online');
    } else {
      setOffline();
    }

    // Demo simulation buttons
    document.querySelector('#sim-offline').addEventListener('click', setOffline);
    document.querySelector('#sim-online').addEventListener('click', setOnline);
  </script>
</body>
</html>
```

---

## CODEPEN 3 — Error Handling Showcase (try/catch/finally)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Error Handling with try/catch/finally</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f5f5f5;
      padding: 32px 20px;
      min-height: 100vh;
    }

    h1 { text-align: center; margin-bottom: 8px; color: #1a1a2e; }
    .subtitle { text-align: center; color: #666; margin-bottom: 32px; font-size: 0.95rem; }

    .demo-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      max-width: 980px;
      margin: 0 auto;
    }

    .demo-card {
      background: white;
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    }

    .demo-card h3 { font-size: 1rem; margin-bottom: 4px; color: #1a1a2e; }
    .demo-card p  { font-size: 0.85rem; color: #666; margin-bottom: 14px; line-height: 1.5; }

    .input-row {
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
    }

    .input-row input {
      flex: 1;
      padding: 8px 12px;
      border: 1.5px solid #d0d0d0;
      border-radius: 8px;
      font-size: 0.9rem;
      outline: none;
    }

    .input-row input:focus { border-color: #5c6bc0; }

    button.try-btn {
      padding: 8px 16px;
      background: #5c6bc0;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-size: 0.9rem;
      white-space: nowrap;
    }

    button.try-btn:hover { background: #3f51b5; }

    .result-box {
      border-radius: 8px;
      padding: 10px 12px;
      font-size: 0.85rem;
      font-family: monospace;
      line-height: 1.5;
      min-height: 48px;
    }

    .result-box.neutral { background: #f5f5f5; color: #555; }
    .result-box.success { background: #e8f5e9; color: #2e7d32; border-left: 3px solid #43a047; }
    .result-box.error   { background: #fce4e4; color: #c62828; border-left: 3px solid #e53935; }
    .result-box.finally { background: #fff8e1; color: #e65100; border-left: 3px solid #ffa000; }

    .flow-log {
      margin-top: 8px;
      font-size: 0.78rem;
      color: #888;
      font-family: monospace;
    }

    .flow-step {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      margin: 2px;
    }
    .flow-step.try    { background: #e3f2fd; color: #1565c0; }
    .flow-step.catch  { background: #fce4e4; color: #c62828; }
    .flow-step.fin    { background: #fff8e1; color: #e65100; }
  </style>
</head>
<body>
  <h1>Error Handling</h1>
  <p class="subtitle">See how try / catch / finally responds to success and failure</p>

  <div class="demo-grid">

    <!-- Demo 1: JSON parse -->
    <div class="demo-card">
      <h3>1. Parse JSON safely</h3>
      <p>Try valid JSON like <code>{"name":"Alex"}</code> and invalid JSON like <code>{broken}</code> to see the catch block activate.</p>
      <div class="input-row">
        <input id="json-input" value='{"name":"Alex","score":42}' placeholder="Enter JSON…">
        <button class="try-btn" id="json-btn">Parse</button>
      </div>
      <div class="result-box neutral" id="json-result">Result appears here…</div>
      <div class="flow-log" id="json-flow"></div>
    </div>

    <!-- Demo 2: Division with custom errors -->
    <div class="demo-card">
      <h3>2. Custom error types</h3>
      <p>Enter two numbers to divide. Try <code>10 / 0</code> (RangeError) or <code>10 / abc</code> (TypeError).</p>
      <div class="input-row">
        <input id="div-a" value="10" style="max-width:80px">
        <span style="line-height:36px;font-size:1.2rem;">/</span>
        <input id="div-b" value="2" style="max-width:80px">
        <button class="try-btn" id="div-btn">Divide</button>
      </div>
      <div class="result-box neutral" id="div-result">Result appears here…</div>
      <div class="flow-log" id="div-flow"></div>
    </div>

    <!-- Demo 3: localStorage failure simulation -->
    <div class="demo-card">
      <h3>3. Safe localStorage write</h3>
      <p>Simulates what happens when storage is unavailable (e.g., private browsing, quota exceeded). Toggle the failure switch.</p>
      <div class="input-row">
        <input id="storage-val" value="Hello, world!" placeholder="Value to save…">
        <button class="try-btn" id="storage-btn">Save</button>
      </div>
      <label style="font-size:0.85rem;display:flex;align-items:center;gap:8px;margin-bottom:10px;">
        <input type="checkbox" id="storage-fail"> Simulate failure
      </label>
      <div class="result-box neutral" id="storage-result">Result appears here…</div>
      <div class="flow-log" id="storage-flow"></div>
    </div>

    <!-- Demo 4: finally always runs -->
    <div class="demo-card">
      <h3>4. finally always runs</h3>
      <p>The <code>finally</code> block executes regardless of success or failure — useful for cleanup like hiding a loading spinner.</p>
      <div class="input-row">
        <input id="fin-input" value="valid" placeholder='"valid" or anything else…'>
        <button class="try-btn" id="fin-btn">Run</button>
      </div>
      <div class="result-box neutral" id="fin-result">Result appears here…</div>
      <div class="flow-log" id="fin-flow"></div>
    </div>

  </div>

  <script>
    function showFlow(el, steps) {
      el.innerHTML = steps.map(([label, type]) =>
        `<span class="flow-step ${type}">${label}</span>`
      ).join(' → ');
    }

    // --- 1. JSON parse ---
    document.querySelector('#json-btn').addEventListener('click', () => {
      const input  = document.querySelector('#json-input').value;
      const result = document.querySelector('#json-result');
      const flow   = document.querySelector('#json-flow');

      try {
        const parsed = JSON.parse(input);
        result.className = 'result-box success';
        result.textContent = 'Parsed: ' + JSON.stringify(parsed, null, 2);
        showFlow(flow, [['try ✓', 'try'], ['finally', 'fin']]);
      } catch (err) {
        result.className = 'result-box error';
        result.textContent = `${err.name}: ${err.message}`;
        showFlow(flow, [['try ✗', 'try'], ['catch', 'catch'], ['finally', 'fin']]);
      } finally {
        // In a real app: hideLoadingSpinner()
      }
    });

    // --- 2. Custom errors ---
    document.querySelector('#div-btn').addEventListener('click', () => {
      const a      = document.querySelector('#div-a').value;
      const b      = document.querySelector('#div-b').value;
      const result = document.querySelector('#div-result');
      const flow   = document.querySelector('#div-flow');

      function divide(x, y) {
        if (isNaN(Number(x)) || isNaN(Number(y))) {
          throw new TypeError('Both values must be numbers');
        }
        if (Number(y) === 0) {
          throw new RangeError('Cannot divide by zero');
        }
        return Number(x) / Number(y);
      }

      try {
        const answer = divide(a, b);
        result.className = 'result-box success';
        result.textContent = `${a} / ${b} = ${answer}`;
        showFlow(flow, [['try ✓', 'try'], ['finally', 'fin']]);
      } catch (err) {
        result.className = 'result-box error';
        result.textContent = `${err.name}: ${err.message}`;
        showFlow(flow, [['try ✗', 'try'], ['catch', 'catch'], ['finally', 'fin']]);
      } finally {
        // cleanup
      }
    });

    // --- 3. localStorage with simulated failure ---
    document.querySelector('#storage-btn').addEventListener('click', () => {
      const value  = document.querySelector('#storage-val').value;
      const fail   = document.querySelector('#storage-fail').checked;
      const result = document.querySelector('#storage-result');
      const flow   = document.querySelector('#storage-flow');

      function saveItem(key, val) {
        if (fail) throw new DOMException('QuotaExceededError');
        localStorage.setItem(key, JSON.stringify(val));
        return localStorage.getItem(key);
      }

      try {
        const saved = saveItem('demo-key', value);
        result.className = 'result-box success';
        result.textContent = `Saved! localStorage value: ${saved}`;
        showFlow(flow, [['try ✓', 'try'], ['finally', 'fin']]);
      } catch (err) {
        result.className = 'result-box error';
        result.textContent = `Storage failed: ${err.name} — falling back to in-memory only`;
        showFlow(flow, [['try ✗', 'try'], ['catch', 'catch'], ['finally', 'fin']]);
      } finally {
        // always: update UI regardless
      }
    });

    // --- 4. finally always runs ---
    document.querySelector('#fin-btn').addEventListener('click', () => {
      const input  = document.querySelector('#fin-input').value.trim();
      const result = document.querySelector('#fin-result');
      const flow   = document.querySelector('#fin-flow');

      const messages = [];

      try {
        messages.push('try block ran');
        if (input !== 'valid') throw new Error(`"${input}" is not valid`);
        messages.push('success path complete');
        result.className = 'result-box success';
        result.textContent = messages.join(' → ');
        showFlow(flow, [['try ✓', 'try'], ['finally', 'fin']]);
      } catch (err) {
        messages.push(`caught: ${err.message}`);
        result.className = 'result-box error';
        result.textContent = messages.join(' → ');
        showFlow(flow, [['try ✗', 'try'], ['catch', 'catch'], ['finally', 'fin']]);
      } finally {
        messages.push('finally ran');
        // In a real app this would update the displayed text,
        // but we set it above for clarity. finally always executes.
      }
    });
  </script>
</body>
</html>
```

---

## CODEPEN 4 — Persistent To-Do List (Full CRUD)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Persistent To-Do List</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f0f4f8;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 40px 20px;
    }

    .app {
      background: white;
      border-radius: 20px;
      padding: 28px;
      max-width: 480px;
      width: 100%;
      box-shadow: 0 4px 24px rgba(0,0,0,0.08);
    }

    .header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 20px;
    }

    h1 { font-size: 1.5rem; color: #1a1a2e; }

    .stats {
      font-size: 0.85rem;
      color: #888;
    }

    .stats span { color: #5c6bc0; font-weight: 700; }

    form {
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
    }

    input[type="text"] {
      flex: 1;
      padding: 10px 14px;
      border: 2px solid #e0e0e0;
      border-radius: 10px;
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.2s;
    }

    input[type="text"]:focus { border-color: #5c6bc0; }

    button.add-btn {
      padding: 10px 20px;
      background: #5c6bc0;
      color: white;
      border: none;
      border-radius: 10px;
      cursor: pointer;
      font-size: 0.95rem;
      font-weight: 600;
      transition: background 0.2s;
    }

    button.add-btn:hover { background: #3f51b5; }

    .filters {
      display: flex;
      gap: 8px;
      margin-bottom: 16px;
    }

    .filter-btn {
      padding: 5px 14px;
      border: 1.5px solid #e0e0e0;
      border-radius: 999px;
      background: transparent;
      font-size: 0.8rem;
      cursor: pointer;
      transition: all 0.2s;
      color: #555;
    }

    .filter-btn.active {
      background: #5c6bc0;
      border-color: #5c6bc0;
      color: white;
    }

    #todo-list { list-style: none; display: flex; flex-direction: column; gap: 8px; }

    .todo-item {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 12px 14px;
      background: #f8f9fa;
      border-radius: 10px;
      animation: slideIn 0.2s ease;
    }

    @keyframes slideIn {
      from { opacity: 0; transform: translateY(-8px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    .todo-item input[type="checkbox"] {
      width: 18px; height: 18px;
      accent-color: #5c6bc0;
      cursor: pointer;
      flex-shrink: 0;
    }

    .todo-text {
      flex: 1;
      font-size: 0.95rem;
      color: #333;
      transition: color 0.2s;
    }

    .todo-text.done {
      text-decoration: line-through;
      color: #bbb;
    }

    .delete-btn {
      background: none;
      border: none;
      cursor: pointer;
      color: #ccc;
      font-size: 1.1rem;
      padding: 2px 6px;
      border-radius: 6px;
      transition: background 0.2s, color 0.2s;
    }

    .delete-btn:hover { background: #fce4e4; color: #e53935; }

    .empty {
      text-align: center;
      color: #bbb;
      font-size: 0.9rem;
      padding: 32px 0;
    }

    .footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 16px;
      padding-top: 16px;
      border-top: 1px solid #f0f0f0;
    }

    .clear-btn {
      background: none;
      border: none;
      color: #e53935;
      font-size: 0.8rem;
      cursor: pointer;
      padding: 4px 8px;
      border-radius: 6px;
    }

    .clear-btn:hover { background: #fce4e4; }

    .persist-note {
      font-size: 0.75rem;
      color: #bbb;
    }
  </style>
</head>
<body>
  <div class="app">
    <div class="header">
      <h1>To-Do List</h1>
      <p class="stats"><span id="done-count">0</span> / <span id="total-count">0</span> done</p>
    </div>

    <form id="todo-form">
      <input type="text" id="todo-input" placeholder="Add a new task…" autocomplete="off">
      <button type="submit" class="add-btn">Add</button>
    </form>

    <div class="filters">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="active">Active</button>
      <button class="filter-btn" data-filter="done">Done</button>
    </div>

    <ul id="todo-list"></ul>

    <div class="footer">
      <button class="clear-btn" id="clear-done">Clear completed</button>
      <span class="persist-note">💾 Saved to localStorage</span>
    </div>
  </div>

  <script>
    // === DATA LAYER ===
    function getTodos() {
      return JSON.parse(localStorage.getItem('todos-v1') || '[]');
    }
    function saveTodos(todos) {
      localStorage.setItem('todos-v1', JSON.stringify(todos));
    }

    // === STATE ===
    let currentFilter = 'all';

    // === LOGIC ===
    function getFiltered(todos) {
      if (currentFilter === 'active') return todos.filter(t => !t.done);
      if (currentFilter === 'done')   return todos.filter(t => t.done);
      return todos;
    }

    // === DISPLAY ===
    function renderTodos() {
      const todos    = getTodos();
      const filtered = getFiltered(todos);
      const list     = document.querySelector('#todo-list');

      document.querySelector('#total-count').textContent = todos.length;
      document.querySelector('#done-count').textContent  = todos.filter(t => t.done).length;

      if (filtered.length === 0) {
        list.innerHTML = `<li class="empty">${
          currentFilter === 'done' ? 'No completed tasks' :
          currentFilter === 'active' ? 'All tasks done! 🎉' :
          'Add a task above to get started'
        }</li>`;
        return;
      }

      list.innerHTML = filtered
        .map(todo => `
          <li class="todo-item" data-id="${todo.id}">
            <input type="checkbox" ${todo.done ? 'checked' : ''}>
            <span class="todo-text ${todo.done ? 'done' : ''}">${escapeHTML(todo.text)}</span>
            <button class="delete-btn" aria-label="Delete">&times;</button>
          </li>
        `)
        .join('');
    }

    function escapeHTML(str) {
      return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    }

    // === EVENTS ===
    document.querySelector('#todo-form').addEventListener('submit', e => {
      e.preventDefault();
      const input = document.querySelector('#todo-input');
      const text  = input.value.trim();
      if (!text) return;

      const todos = getTodos();
      todos.push({ id: Date.now(), text, done: false });
      saveTodos(todos);
      renderTodos();
      input.value = '';
      input.focus();
    });

    document.querySelector('#todo-list').addEventListener('click', e => {
      const item = e.target.closest('[data-id]');
      if (!item) return;
      const id    = Number(item.dataset.id);
      let todos   = getTodos();

      if (e.target.type === 'checkbox') {
        todos = todos.map(t => t.id === id ? { ...t, done: e.target.checked } : t);
        saveTodos(todos);
        renderTodos();
      }

      if (e.target.classList.contains('delete-btn')) {
        todos = todos.filter(t => t.id !== id);
        saveTodos(todos);
        renderTodos();
      }
    });

    document.querySelectorAll('.filter-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        currentFilter = btn.dataset.filter;
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        renderTodos();
      });
    });

    document.querySelector('#clear-done').addEventListener('click', () => {
      saveTodos(getTodos().filter(t => !t.done));
      renderTodos();
    });

    // Initialize
    renderTodos();
  </script>
</body>
</html>
```

---

## CODEPEN 5 — Shopping Cart with localStorage Persistence

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Persistent Shopping Cart</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f5f5f5;
      min-height: 100vh;
      padding: 24px 16px;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1a1a2e;
      color: white;
      padding: 14px 24px;
      border-radius: 14px;
      margin-bottom: 24px;
      max-width: 900px;
      margin-inline: auto;
    }

    header h1 { font-size: 1.2rem; font-weight: 700; }

    .cart-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.9rem;
    }

    .badge {
      background: #e53935;
      color: white;
      border-radius: 999px;
      padding: 2px 8px;
      font-size: 0.75rem;
      font-weight: 700;
      min-width: 22px;
      text-align: center;
    }

    .layout {
      display: grid;
      grid-template-columns: 1fr 320px;
      gap: 20px;
      max-width: 900px;
      margin: 0 auto;
    }

    @media (max-width: 680px) { .layout { grid-template-columns: 1fr; } }

    h2 { font-size: 1rem; color: #444; margin-bottom: 14px; }

    .product-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
      gap: 14px;
    }

    .product-card {
      background: white;
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .product-emoji { font-size: 2.2rem; text-align: center; }
    .product-name  { font-weight: 600; font-size: 0.9rem; color: #333; }
    .product-price { color: #5c6bc0; font-weight: 700; font-size: 0.95rem; }

    .add-btn {
      margin-top: auto;
      padding: 7px;
      background: #5c6bc0;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 600;
      transition: background 0.2s;
    }

    .add-btn:hover { background: #3f51b5; }

    /* Cart panel */
    .cart-panel {
      background: white;
      border-radius: 14px;
      padding: 20px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.07);
      align-self: start;
      position: sticky;
      top: 20px;
    }

    #cart-list { list-style: none; display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px; min-height: 40px; }

    .cart-item {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.88rem;
    }

    .cart-item-name { flex: 1; color: #333; }
    .cart-item-price { color: #5c6bc0; font-weight: 600; white-space: nowrap; }

    .qty-controls {
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .qty-btn {
      width: 22px; height: 22px;
      border: 1.5px solid #e0e0e0;
      background: white;
      border-radius: 4px;
      cursor: pointer;
      font-size: 0.85rem;
      display: flex; align-items: center; justify-content: center;
      font-weight: 700;
      color: #555;
    }

    .qty-btn:hover { background: #f5f5f5; }
    .qty-label { font-size: 0.85rem; min-width: 16px; text-align: center; color: #333; }

    .cart-empty { color: #bbb; font-size: 0.9rem; text-align: center; padding: 16px 0; }

    .divider { border: none; border-top: 1px solid #f0f0f0; margin: 12px 0; }

    .total-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-weight: 700;
      font-size: 1.05rem;
      color: #1a1a2e;
      margin-bottom: 12px;
    }

    .checkout-btn {
      width: 100%;
      padding: 11px;
      background: #1a1a2e;
      color: white;
      border: none;
      border-radius: 10px;
      cursor: pointer;
      font-size: 0.95rem;
      font-weight: 600;
    }

    .checkout-btn:hover { background: #2d2d4e; }

    .clear-cart-btn {
      width: 100%;
      padding: 7px;
      background: none;
      border: 1px solid #f0f0f0;
      border-radius: 8px;
      color: #aaa;
      cursor: pointer;
      font-size: 0.8rem;
      margin-top: 6px;
    }

    .clear-cart-btn:hover { background: #fce4e4; color: #e53935; border-color: #fce4e4; }

    .persist-note {
      text-align: center;
      font-size: 0.72rem;
      color: #ccc;
      margin-top: 8px;
    }
  </style>
</head>
<body>

  <header>
    <h1>🛍 Shop</h1>
    <div class="cart-badge">
      🛒 Cart <span class="badge" id="cart-badge">0</span>
    </div>
  </header>

  <div class="layout">
    <div>
      <h2>Products</h2>
      <div class="product-grid" id="product-grid"></div>
    </div>

    <div class="cart-panel">
      <h2>Your Cart</h2>
      <ul id="cart-list"></ul>
      <hr class="divider">
      <div class="total-row">
        <span>Total</span>
        <span id="cart-total">$0.00</span>
      </div>
      <button class="checkout-btn">Checkout</button>
      <button class="clear-cart-btn" id="clear-cart">Clear cart</button>
      <p class="persist-note">💾 Cart saved to localStorage</p>
    </div>
  </div>

  <script>
    const PRODUCTS = [
      { id: 1, name: 'Headphones', emoji: '🎧', price: 49.99 },
      { id: 2, name: 'Keyboard',   emoji: '⌨️', price: 89.00 },
      { id: 3, name: 'Mouse',      emoji: '🖱️', price: 34.50 },
      { id: 4, name: 'Webcam',     emoji: '📷', price: 65.00 },
      { id: 5, name: 'Monitor',    emoji: '🖥️', price: 299.99 },
      { id: 6, name: 'Desk Lamp',  emoji: '💡', price: 22.00 },
    ];

    // === DATA LAYER ===
    function getCart() {
      return JSON.parse(localStorage.getItem('shop-cart') || '[]');
    }
    function saveCart(cart) {
      localStorage.setItem('shop-cart', JSON.stringify(cart));
    }

    // === LOGIC ===
    function addToCart(cart, product) {
      const existing = cart.find(i => i.id === product.id);
      if (existing) {
        return cart.map(i => i.id === product.id ? { ...i, qty: i.qty + 1 } : i);
      }
      return [...cart, { ...product, qty: 1 }];
    }

    function updateQty(cart, id, delta) {
      const updated = cart.map(i => i.id === id ? { ...i, qty: i.qty + delta } : i);
      return updated.filter(i => i.qty > 0);
    }

    function getTotal(cart) {
      return cart.reduce((sum, i) => sum + i.price * i.qty, 0);
    }

    function getTotalItems(cart) {
      return cart.reduce((n, i) => n + i.qty, 0);
    }

    // === DISPLAY ===
    function renderProducts() {
      document.querySelector('#product-grid').innerHTML = PRODUCTS.map(p => `
        <div class="product-card">
          <div class="product-emoji">${p.emoji}</div>
          <div class="product-name">${p.name}</div>
          <div class="product-price">$${p.price.toFixed(2)}</div>
          <button class="add-btn" data-id="${p.id}">Add to Cart</button>
        </div>
      `).join('');
    }

    function renderCart() {
      const cart   = getCart();
      const list   = document.querySelector('#cart-list');
      const total  = document.querySelector('#cart-total');
      const badge  = document.querySelector('#cart-badge');

      badge.textContent = getTotalItems(cart);
      total.textContent = `$${getTotal(cart).toFixed(2)}`;

      if (cart.length === 0) {
        list.innerHTML = '<li class="cart-empty">Your cart is empty</li>';
        return;
      }

      list.innerHTML = cart.map(item => `
        <li class="cart-item" data-id="${item.id}">
          <span class="cart-item-name">${item.emoji} ${item.name}</span>
          <div class="qty-controls">
            <button class="qty-btn" data-action="dec">−</button>
            <span class="qty-label">${item.qty}</span>
            <button class="qty-btn" data-action="inc">+</button>
          </div>
          <span class="cart-item-price">$${(item.price * item.qty).toFixed(2)}</span>
        </li>
      `).join('');
    }

    // === EVENTS ===
    document.querySelector('#product-grid').addEventListener('click', e => {
      const btn = e.target.closest('.add-btn');
      if (!btn) return;
      const id      = Number(btn.dataset.id);
      const product = PRODUCTS.find(p => p.id === id);
      saveCart(addToCart(getCart(), product));
      renderCart();
    });

    document.querySelector('#cart-list').addEventListener('click', e => {
      const item   = e.target.closest('[data-id]');
      const action = e.target.dataset.action;
      if (!item || !action) return;
      const id = Number(item.dataset.id);
      saveCart(updateQty(getCart(), id, action === 'inc' ? 1 : -1));
      renderCart();
    });

    document.querySelector('#clear-cart').addEventListener('click', () => {
      saveCart([]);
      renderCart();
    });

    // Init
    renderProducts();
    renderCart();
  </script>
</body>
</html>
```
