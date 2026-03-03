# Day 20 — DOM Events & Event Handling: CodePen Code Blocks

Each numbered section corresponds to the `[CODEPEN #]` placeholder in the article.

---

## CODEPEN 1 — addEventListener vs. removeEventListener

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>addEventListener vs. removeEventListener</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, -apple-system, sans-serif;
      background: #f1f5f9;
      color: #1e293b;
      padding: 2rem;
      min-height: 100vh;
    }

    h1 {
      font-size: 1.5rem;
      margin-bottom: 0.25rem;
      color: #0f172a;
    }

    .subtitle {
      color: #64748b;
      margin-bottom: 2rem;
      font-size: 0.95rem;
    }

    .demo-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      max-width: 800px;
    }

    @media (max-width: 600px) {
      .demo-grid { grid-template-columns: 1fr; }
    }

    .panel {
      background: white;
      border-radius: 12px;
      padding: 1.5rem;
      box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.05);
    }

    .panel h2 {
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      color: #0f172a;
    }

    .panel p {
      font-size: 0.85rem;
      color: #64748b;
      margin-bottom: 1rem;
      line-height: 1.5;
    }

    .btn-row {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-bottom: 1rem;
    }

    button {
      padding: 0.45rem 1rem;
      border: none;
      border-radius: 6px;
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      transition: opacity 0.15s, transform 0.1s;
    }

    button:active { transform: scale(0.97); }

    .btn-add    { background: #22c55e; color: white; }
    .btn-remove { background: #ef4444; color: white; }
    .btn-fire   { background: #3b82f6; color: white; }
    .btn-anon   { background: #a855f7; color: white; }

    button:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .counter-display {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      margin-bottom: 0.75rem;
    }

    .counter-number {
      font-size: 2rem;
      font-weight: 800;
      color: #3b82f6;
      min-width: 2.5rem;
      text-align: center;
    }

    .counter-label {
      font-size: 0.8rem;
      color: #64748b;
      line-height: 1.3;
    }

    .status-msg {
      font-size: 0.82rem;
      border-radius: 6px;
      padding: 0.5rem 0.75rem;
      min-height: 2rem;
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }

    .status-msg.warning {
      background: #fef9c3;
      border-color: #fde68a;
      color: #854d0e;
    }

    .status-msg.error {
      background: #fef2f2;
      border-color: #fecaca;
      color: #991b1b;
    }

    .status-msg.info {
      background: #eff6ff;
      border-color: #bfdbfe;
      color: #1e40af;
    }

    .log-panel {
      background: #0f172a;
      border-radius: 8px;
      padding: 1rem;
      max-height: 150px;
      overflow-y: auto;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
    }

    .log-entry {
      color: #94a3b8;
      padding: 0.1rem 0;
    }

    .log-entry.success { color: #4ade80; }
    .log-entry.error   { color: #f87171; }
    .log-entry.warn    { color: #fbbf24; }
    .log-entry.info    { color: #60a5fa; }

    .full-width {
      grid-column: 1 / -1;
    }
  </style>
</head>
<body>

  <h1>addEventListener & removeEventListener</h1>
  <p class="subtitle">Learn why named functions are required to remove listeners — and why anonymous functions cannot be removed.</p>

  <div class="demo-grid">

    <!-- Named function panel -->
    <div class="panel">
      <h2>Named Function (Removable)</h2>
      <p>A named function reference lets you add and remove the same listener precisely. Notice the counter only increments while the listener is attached.</p>

      <div class="counter-display">
        <div class="counter-number" id="named-count">0</div>
        <div class="counter-label">clicks handled<br>by named listener</div>
      </div>

      <div class="btn-row">
        <button class="btn-add"    id="add-named">Add Listener</button>
        <button class="btn-remove" id="remove-named">Remove Listener</button>
        <button class="btn-fire"   id="fire-named">Click Me!</button>
      </div>

      <div class="status-msg info" id="named-status">Listener is currently ATTACHED</div>
    </div>

    <!-- Anonymous function panel -->
    <div class="panel">
      <h2>Anonymous Function (Not Removable)</h2>
      <p>Each time you click "Add Anon Listener", a new anonymous function is created. They cannot be removed — and they stack up!</p>

      <div class="counter-display">
        <div class="counter-number" id="anon-count">0</div>
        <div class="counter-label">clicks handled<br>(listeners stacking!)</div>
      </div>

      <div class="btn-row">
        <button class="btn-anon"   id="add-anon">Add Anon Listener</button>
        <button class="btn-remove" id="try-remove-anon">Try to Remove</button>
        <button class="btn-fire"   id="fire-anon">Click Me!</button>
      </div>

      <div class="status-msg warning" id="anon-status">0 anonymous listeners attached</div>
    </div>

    <!-- Event log -->
    <div class="panel full-width">
      <h2>Event Log</h2>
      <div class="log-panel" id="log"></div>
    </div>

  </div>

  <script>
    // ── Named function demo ──────────────────────────────────────────────
    const fireNamedBtn   = document.getElementById('fire-named');
    const addNamedBtn    = document.getElementById('add-named');
    const removeNamedBtn = document.getElementById('remove-named');
    const namedCount     = document.getElementById('named-count');
    const namedStatus    = document.getElementById('named-status');

    let namedClicks   = 0;
    let namedAttached = true;

    // This is the named function — we hold a reference to it
    function handleNamedClick() {
      namedClicks++;
      namedCount.textContent = namedClicks;
      log('Named handler fired — click #' + namedClicks, 'success');
    }

    // Attach it immediately
    fireNamedBtn.addEventListener('click', handleNamedClick);

    addNamedBtn.addEventListener('click', () => {
      if (!namedAttached) {
        fireNamedBtn.addEventListener('click', handleNamedClick);
        namedAttached = true;
        setStatus(namedStatus, 'Listener is currently ATTACHED', 'info');
        log('Named listener ADDED to button', 'info');
      } else {
        log('Listener already attached — ignored (no duplicate)', 'warn');
      }
    });

    removeNamedBtn.addEventListener('click', () => {
      if (namedAttached) {
        fireNamedBtn.removeEventListener('click', handleNamedClick);
        namedAttached = false;
        setStatus(namedStatus, 'Listener is REMOVED — clicks do nothing', 'error');
        log('Named listener REMOVED from button', 'error');
      } else {
        log('Nothing to remove — listener is not attached', 'warn');
      }
    });

    // ── Anonymous function demo ──────────────────────────────────────────
    const fireAnonBtn    = document.getElementById('fire-anon');
    const addAnonBtn     = document.getElementById('add-anon');
    const tryRemoveAnon  = document.getElementById('try-remove-anon');
    const anonCount      = document.getElementById('anon-count');
    const anonStatus     = document.getElementById('anon-status');

    let anonListenerCount = 0;

    addAnonBtn.addEventListener('click', () => {
      // A new arrow function object is created every time this runs
      fireAnonBtn.addEventListener('click', () => {
        anonCount.textContent = parseInt(anonCount.textContent) + 1;
      });
      anonListenerCount++;
      setStatus(anonStatus, anonListenerCount + ' anonymous listener(s) attached — stacking!', 'warning');
      log('Anonymous listener #' + anonListenerCount + ' added (cannot be removed)', 'warn');
    });

    tryRemoveAnon.addEventListener('click', () => {
      // This creates yet ANOTHER new arrow function — it does not match any attached listener
      fireAnonBtn.removeEventListener('click', () => {
        anonCount.textContent = parseInt(anonCount.textContent) + 1;
      });
      setStatus(anonStatus, 'removeEventListener had no effect! ' + anonListenerCount + ' listener(s) still attached', 'error');
      log('removeEventListener called with a new anonymous fn — did nothing!', 'error');
    });

    // ── Helpers ──────────────────────────────────────────────────────────
    function log(message, type = '') {
      const logEl = document.getElementById('log');
      const entry = document.createElement('div');
      entry.className = 'log-entry ' + type;
      const time = new Date().toLocaleTimeString('en-US', { hour12: false });
      entry.textContent = '[' + time + '] ' + message;
      logEl.appendChild(entry);
      logEl.scrollTop = logEl.scrollHeight;
    }

    function setStatus(el, message, type) {
      el.textContent = message;
      el.className = 'status-msg ' + type;
    }

    log('Demo ready. Named listener attached to "Click Me!" button.', 'info');
  </script>

</body>
</html>
```

---

## CODEPEN 2 — Mouse Events & Pointer Events

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mouse Events & Pointer Events</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, -apple-system, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      min-height: 100vh;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    h1 {
      font-size: 1.4rem;
      color: #f8fafc;
    }

    .subtitle {
      font-size: 0.875rem;
      color: #64748b;
      margin-top: 0.2rem;
    }

    .layout {
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 1rem;
      flex: 1;
    }

    @media (max-width: 680px) {
      .layout { grid-template-columns: 1fr; }
    }

    /* ── Interaction Zone ── */
    .zone-wrapper {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .interaction-zone {
      flex: 1;
      min-height: 300px;
      border-radius: 12px;
      border: 2px solid #334155;
      background: #1e293b;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: crosshair;
      position: relative;
      transition: background 0.2s, border-color 0.2s;
      user-select: none;
      -webkit-user-select: none;
    }

    .interaction-zone.hovered {
      background: #1a3a52;
      border-color: #38bdf8;
    }

    .zone-prompt {
      color: #475569;
      font-size: 0.95rem;
      text-align: center;
      pointer-events: none;
      padding: 1rem;
    }

    .coord-display {
      position: absolute;
      bottom: 0.75rem;
      right: 0.75rem;
      font-family: 'Courier New', monospace;
      font-size: 0.75rem;
      color: #64748b;
      background: rgba(0,0,0,0.4);
      padding: 0.25rem 0.5rem;
      border-radius: 4px;
    }

    .cursor-dot {
      position: absolute;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #38bdf8;
      pointer-events: none;
      transform: translate(-50%, -50%);
      transition: opacity 0.2s;
      opacity: 0;
      box-shadow: 0 0 8px #38bdf8;
    }

    /* ── Event type chips ── */
    .event-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
    }

    .chip {
      font-size: 0.72rem;
      font-weight: 600;
      padding: 0.2rem 0.55rem;
      border-radius: 20px;
      border: 1px solid;
      cursor: pointer;
      transition: opacity 0.15s;
    }

    .chip.active   { opacity: 1; }
    .chip.inactive { opacity: 0.35; }

    .chip-click      { background: #1e3a5f; color: #60a5fa; border-color: #3b82f6; }
    .chip-enter      { background: #14532d; color: #4ade80; border-color: #22c55e; }
    .chip-leave      { background: #422006; color: #fb923c; border-color: #f97316; }
    .chip-move       { background: #3b0764; color: #e879f9; border-color: #c026d3; }
    .chip-down       { background: #1c1917; color: #f5f5f4; border-color: #78716c; }
    .chip-pointer    { background: #1a3a52; color: #38bdf8; border-color: #0ea5e9; }
    .chip-dblclick   { background: #4c1d95; color: #c4b5fd; border-color: #7c3aed; }

    /* ── Log Panel ── */
    .log-panel {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }

    .log-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.75rem 1rem;
      border-bottom: 1px solid #334155;
      font-size: 0.8rem;
      font-weight: 700;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .clear-btn {
      background: #334155;
      color: #94a3b8;
      border: none;
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      font-size: 0.72rem;
      cursor: pointer;
    }

    .clear-btn:hover { background: #475569; }

    .log-entries {
      flex: 1;
      overflow-y: auto;
      padding: 0.5rem;
      font-family: 'Courier New', monospace;
      font-size: 0.75rem;
      max-height: 400px;
    }

    .log-entry {
      display: grid;
      grid-template-columns: auto 1fr auto;
      gap: 0.5rem;
      align-items: baseline;
      padding: 0.3rem 0.4rem;
      border-radius: 4px;
      margin-bottom: 1px;
      animation: slideIn 0.15s ease;
    }

    @keyframes slideIn {
      from { opacity: 0; transform: translateX(6px); }
      to   { opacity: 1; transform: translateX(0); }
    }

    .log-entry:nth-child(odd) { background: rgba(255,255,255,0.02); }

    .log-time  { color: #475569; font-size: 0.68rem; }
    .log-name  { font-weight: 700; }
    .log-extra { color: #64748b; font-size: 0.68rem; text-align: right; }

    .type-click    { color: #60a5fa; }
    .type-enter    { color: #4ade80; }
    .type-leave    { color: #fb923c; }
    .type-move     { color: #e879f9; }
    .type-down     { color: #f5f5f4; }
    .type-pointer  { color: #38bdf8; }
    .type-dblclick { color: #c4b5fd; }

    .log-empty {
      color: #334155;
      text-align: center;
      padding: 2rem;
      font-size: 0.8rem;
    }
  </style>
</head>
<body>

  <div>
    <h1>Mouse Events &amp; Pointer Events</h1>
    <p class="subtitle">Pointer events handle both mouse and touch with one set of handlers. Interact with the zone to see each event fire.</p>
  </div>

  <div class="layout">

    <div class="zone-wrapper">
      <div class="interaction-zone" id="zone">
        <div class="zone-prompt" id="zone-prompt">
          Move your mouse, click, double-click,<br>or touch this area (on mobile).
        </div>
        <div class="cursor-dot" id="cursor-dot"></div>
        <div class="coord-display" id="coords">x: — &nbsp; y: —</div>
      </div>

      <div class="event-chips" id="chips">
        <span class="chip chip-click active"    data-type="click">click</span>
        <span class="chip chip-dblclick active" data-type="dblclick">dblclick</span>
        <span class="chip chip-enter active"    data-type="pointerenter">pointerenter</span>
        <span class="chip chip-leave active"    data-type="pointerleave">pointerleave</span>
        <span class="chip chip-down active"     data-type="pointerdown">pointerdown</span>
        <span class="chip chip-down active"     data-type="pointerup">pointerup</span>
        <span class="chip chip-move active"     data-type="pointermove">pointermove</span>
        <span class="chip chip-pointer active"  data-type="pointercancel">pointercancel</span>
      </div>
    </div>

    <div class="log-panel">
      <div class="log-header">
        <span>Event Log</span>
        <button class="clear-btn" id="clear-log">Clear</button>
      </div>
      <div class="log-entries" id="log">
        <div class="log-empty">Events will appear here…</div>
      </div>
    </div>

  </div>

  <script>
    const zone      = document.getElementById('zone');
    const log       = document.getElementById('log');
    const cursorDot = document.getElementById('cursor-dot');
    const coords    = document.getElementById('coords');
    const prompt    = document.getElementById('zone-prompt');

    // Track which event types are enabled via chip toggles
    const enabled = new Set([
      'click', 'dblclick', 'pointerenter', 'pointerleave',
      'pointerdown', 'pointerup', 'pointermove', 'pointercancel'
    ]);

    // Color map by event type
    const typeClass = {
      click:        'type-click',
      dblclick:     'type-dblclick',
      pointerenter: 'type-enter',
      pointerleave: 'type-leave',
      pointerdown:  'type-down',
      pointerup:    'type-down',
      pointermove:  'type-move',
      pointercancel:'type-pointer',
    };

    // ── Chip toggle ──────────────────────────────────────────────────────
    document.getElementById('chips').addEventListener('click', (e) => {
      const chip = e.target.closest('.chip[data-type]');
      if (!chip) return;
      const type = chip.dataset.type;
      if (enabled.has(type)) {
        enabled.delete(type);
        chip.classList.replace('active', 'inactive');
      } else {
        enabled.add(type);
        chip.classList.replace('inactive', 'active');
      }
    });

    // ── Logging helper ───────────────────────────────────────────────────
    let moveThrottle = null;

    function logEvent(type, detail = '') {
      if (!enabled.has(type)) return;

      // Throttle pointermove to avoid overwhelming the log
      if (type === 'pointermove') {
        if (moveThrottle) return;
        moveThrottle = setTimeout(() => { moveThrottle = null; }, 80);
      }

      const isEmpty = log.querySelector('.log-empty');
      if (isEmpty) isEmpty.remove();

      const now = new Date();
      const time = now.toLocaleTimeString('en-US', {
        hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false
      });

      const entry = document.createElement('div');
      entry.className = 'log-entry';
      entry.innerHTML =
        `<span class="log-time">${time}</span>` +
        `<span class="log-name ${typeClass[type] || ''}">${type}</span>` +
        `<span class="log-extra">${detail}</span>`;

      log.prepend(entry);

      // Cap log at 60 entries
      const entries = log.querySelectorAll('.log-entry');
      if (entries.length > 60) entries[entries.length - 1].remove();
    }

    // ── Attach listeners ─────────────────────────────────────────────────
    zone.addEventListener('click',        (e) => logEvent('click', `(${e.clientX}, ${e.clientY})`));
    zone.addEventListener('dblclick',     (e) => logEvent('dblclick', `(${e.clientX}, ${e.clientY})`));
    zone.addEventListener('pointerdown',  (e) => logEvent('pointerdown', e.pointerType));
    zone.addEventListener('pointerup',    (e) => logEvent('pointerup', e.pointerType));
    zone.addEventListener('pointercancel',(e) => logEvent('pointercancel', e.pointerType));

    zone.addEventListener('pointerenter', (e) => {
      zone.classList.add('hovered');
      prompt.style.opacity = '0.2';
      cursorDot.style.opacity = '1';
      logEvent('pointerenter', e.pointerType);
    });

    zone.addEventListener('pointerleave', (e) => {
      zone.classList.remove('hovered');
      prompt.style.opacity = '1';
      cursorDot.style.opacity = '0';
      coords.textContent = 'x: —   y: —';
      logEvent('pointerleave', e.pointerType);
    });

    zone.addEventListener('pointermove', (e) => {
      const rect = zone.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      cursorDot.style.left = x + 'px';
      cursorDot.style.top  = y + 'px';
      coords.textContent = `x: ${Math.round(x)}   y: ${Math.round(y)}`;
      logEvent('pointermove', `(${Math.round(x)}, ${Math.round(y)})`);
    });

    // ── Clear button ─────────────────────────────────────────────────────
    document.getElementById('clear-log').addEventListener('click', () => {
      log.innerHTML = '<div class="log-empty">Events will appear here…</div>';
    });
  </script>

</body>
</html>
```

---

## CODEPEN 3 — Keyboard Events Explorer

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Keyboard Events Explorer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, -apple-system, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      min-height: 100vh;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    h1 { font-size: 1.4rem; color: #f8fafc; }
    .subtitle { font-size: 0.875rem; color: #64748b; margin-top: 0.2rem; }

    /* ── Input ── */
    .input-wrapper {
      position: relative;
      max-width: 480px;
    }

    .key-input {
      width: 100%;
      background: #1e293b;
      border: 2px solid #334155;
      color: #f1f5f9;
      font-size: 1.1rem;
      padding: 0.75rem 1rem;
      border-radius: 10px;
      outline: none;
      caret-color: #38bdf8;
      transition: border-color 0.2s;
    }

    .key-input:focus {
      border-color: #38bdf8;
      box-shadow: 0 0 0 3px rgba(56,189,248,0.15);
    }

    .input-hint {
      font-size: 0.78rem;
      color: #475569;
      margin-top: 0.4rem;
    }

    /* ── Info Cards ── */
    .info-row {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 0.75rem;
      max-width: 800px;
    }

    .info-card {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 0.85rem 1rem;
    }

    .info-label {
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #64748b;
      margin-bottom: 0.35rem;
    }

    .info-value {
      font-family: 'Courier New', monospace;
      font-size: 1.1rem;
      font-weight: 700;
      color: #38bdf8;
      min-height: 1.5rem;
      word-break: break-all;
    }

    .info-value.empty { color: #334155; }

    /* ── Big key display ── */
    .big-key {
      background: #1e293b;
      border: 2px solid #334155;
      border-bottom: 4px solid #1e3a5f;
      border-radius: 12px;
      padding: 1rem 1.5rem;
      display: inline-block;
      font-size: 2rem;
      font-weight: 800;
      color: #f1f5f9;
      min-width: 80px;
      text-align: center;
      transition: all 0.05s;
    }

    .big-key.pressed {
      background: #0f3460;
      border-color: #38bdf8;
      border-bottom-width: 2px;
      transform: translateY(2px);
      color: #38bdf8;
    }

    /* ── Modifier keys ── */
    .modifiers-row {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      max-width: 480px;
    }

    .mod-key {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 6px;
      padding: 0.35rem 0.75rem;
      font-size: 0.82rem;
      font-weight: 700;
      color: #475569;
      transition: all 0.1s;
    }

    .mod-key.active {
      background: #1a3a52;
      border-color: #38bdf8;
      color: #38bdf8;
    }

    /* ── Shortcut panel ── */
    .shortcuts-panel {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 1rem 1.25rem;
      max-width: 480px;
    }

    .shortcuts-panel h3 {
      font-size: 0.85rem;
      font-weight: 700;
      color: #94a3b8;
      margin-bottom: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .shortcut-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.4rem 0;
      border-bottom: 1px solid #1e293b;
    }

    .shortcut-row:last-child { border-bottom: none; }

    .shortcut-keys {
      display: flex;
      gap: 0.25rem;
      min-width: 130px;
    }

    .key-badge {
      background: #0f172a;
      border: 1px solid #475569;
      border-radius: 4px;
      padding: 0.15rem 0.45rem;
      font-family: 'Courier New', monospace;
      font-size: 0.75rem;
      color: #94a3b8;
    }

    .shortcut-desc {
      font-size: 0.82rem;
      color: #64748b;
      flex: 1;
    }

    .shortcut-result {
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.2rem 0.6rem;
      border-radius: 20px;
      background: #0f172a;
      color: #334155;
      transition: all 0.3s;
    }

    .shortcut-result.fired {
      background: #14532d;
      color: #4ade80;
    }

    /* ── Event log ── */
    .event-log {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      max-height: 150px;
      overflow-y: auto;
      padding: 0.5rem;
      font-family: 'Courier New', monospace;
      font-size: 0.75rem;
      max-width: 800px;
    }

    .log-entry {
      padding: 0.2rem 0.4rem;
      border-radius: 3px;
      color: #94a3b8;
    }

    .log-entry.down { color: #60a5fa; }
    .log-entry.up   { color: #f87171; }
    .log-entry.shortcut { color: #4ade80; font-weight: 700; }
    .log-empty { color: #334155; padding: 0.5rem; }
  </style>
</head>
<body>

  <div>
    <h1>Keyboard Events Explorer</h1>
    <p class="subtitle">Click into the input below and press any key to see event details. Try keyboard shortcuts too.</p>
  </div>

  <div class="input-wrapper">
    <input
      type="text"
      class="key-input"
      id="key-input"
      placeholder="Click here and press any key…"
      autocomplete="off"
      spellcheck="false"
    >
    <p class="input-hint">Tip: try Ctrl+S, Escape, arrow keys, Shift+letters</p>
  </div>

  <!-- Big key display -->
  <div class="big-key" id="big-key">?</div>

  <!-- Info cards -->
  <div class="info-row">
    <div class="info-card">
      <div class="info-label">event.key</div>
      <div class="info-value empty" id="val-key">—</div>
    </div>
    <div class="info-card">
      <div class="info-label">event.code</div>
      <div class="info-value empty" id="val-code">—</div>
    </div>
    <div class="info-card">
      <div class="info-label">event.type</div>
      <div class="info-value empty" id="val-type">—</div>
    </div>
    <div class="info-card">
      <div class="info-label">repeat?</div>
      <div class="info-value empty" id="val-repeat">—</div>
    </div>
  </div>

  <!-- Modifier keys -->
  <div class="modifiers-row">
    <div class="mod-key" id="mod-shift">⇧ Shift</div>
    <div class="mod-key" id="mod-ctrl">Ctrl</div>
    <div class="mod-key" id="mod-alt">Alt</div>
    <div class="mod-key" id="mod-meta">⌘ Meta</div>
  </div>

  <!-- Shortcuts panel -->
  <div class="shortcuts-panel">
    <h3>Detected Shortcuts</h3>
    <div class="shortcut-row">
      <div class="shortcut-keys">
        <span class="key-badge">Ctrl</span>
        <span class="key-badge">+</span>
        <span class="key-badge">S</span>
      </div>
      <div class="shortcut-desc">Save document</div>
      <div class="shortcut-result" id="result-save">—</div>
    </div>
    <div class="shortcut-row">
      <div class="shortcut-keys">
        <span class="key-badge">Escape</span>
      </div>
      <div class="shortcut-desc">Close panel</div>
      <div class="shortcut-result" id="result-escape">—</div>
    </div>
    <div class="shortcut-row">
      <div class="shortcut-keys">
        <span class="key-badge">Shift</span>
        <span class="key-badge">+</span>
        <span class="key-badge">?</span>
      </div>
      <div class="shortcut-desc">Open help</div>
      <div class="shortcut-result" id="result-help">—</div>
    </div>
    <div class="shortcut-row">
      <div class="shortcut-keys">
        <span class="key-badge">↑</span>
        <span class="key-badge">↓</span>
        <span class="key-badge">←</span>
        <span class="key-badge">→</span>
      </div>
      <div class="shortcut-desc">Arrow keys</div>
      <div class="shortcut-result" id="result-arrow">—</div>
    </div>
  </div>

  <!-- Event log -->
  <div class="event-log" id="log">
    <div class="log-empty">Keyboard events will appear here…</div>
  </div>

  <script>
    const input    = document.getElementById('key-input');
    const bigKey   = document.getElementById('big-key');
    const valKey   = document.getElementById('val-key');
    const valCode  = document.getElementById('val-code');
    const valType  = document.getElementById('val-type');
    const valRepeat= document.getElementById('val-repeat');
    const log      = document.getElementById('log');

    const modShift = document.getElementById('mod-shift');
    const modCtrl  = document.getElementById('mod-ctrl');
    const modAlt   = document.getElementById('mod-alt');
    const modMeta  = document.getElementById('mod-meta');

    const resultSave   = document.getElementById('result-save');
    const resultEscape = document.getElementById('result-escape');
    const resultHelp   = document.getElementById('result-help');
    const resultArrow  = document.getElementById('result-arrow');

    function flashResult(el, text) {
      el.textContent = text;
      el.classList.add('fired');
      setTimeout(() => {
        el.classList.remove('fired');
        el.textContent = '—';
      }, 1500);
    }

    function addLog(message, cls) {
      const empty = log.querySelector('.log-empty');
      if (empty) empty.remove();
      const entry = document.createElement('div');
      entry.className = 'log-entry ' + cls;
      entry.textContent = message;
      log.prepend(entry);
      const entries = log.querySelectorAll('.log-entry');
      if (entries.length > 30) entries[entries.length - 1].remove();
    }

    function updateModifiers(e) {
      modShift.classList.toggle('active', e.shiftKey);
      modCtrl.classList.toggle('active',  e.ctrlKey);
      modAlt.classList.toggle('active',   e.altKey);
      modMeta.classList.toggle('active',  e.metaKey);
    }

    // ── keydown ──────────────────────────────────────────────────────────
    input.addEventListener('keydown', (e) => {
      updateModifiers(e);

      // Display key info
      const displayKey = e.key === ' ' ? 'Space' : e.key;
      bigKey.textContent = displayKey.length > 4 ? displayKey.substring(0, 4) : displayKey;
      bigKey.classList.add('pressed');

      valKey.textContent    = JSON.stringify(e.key);
      valKey.classList.remove('empty');
      valCode.textContent   = e.code;
      valCode.classList.remove('empty');
      valType.textContent   = 'keydown';
      valType.classList.remove('empty');
      valRepeat.textContent = e.repeat ? 'yes (held)' : 'no';
      valRepeat.classList.remove('empty');

      // Log entry
      const mods = [
        e.ctrlKey  ? 'Ctrl'  : '',
        e.metaKey  ? 'Meta'  : '',
        e.shiftKey ? 'Shift' : '',
        e.altKey   ? 'Alt'   : '',
      ].filter(Boolean).join('+');

      const combo = mods ? mods + '+' + e.key : e.key;
      addLog(`↓ keydown  key="${e.key}"  code="${e.code}"${e.repeat ? '  [repeat]' : ''}  ${mods}`, 'down');

      // ── Shortcut detection ────────────────────────────────────────────
      if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        flashResult(resultSave, '✓ Saved!');
        addLog('⚡ SHORTCUT: Ctrl+S — "Save document" fired', 'shortcut');
      }

      if (e.key === 'Escape') {
        flashResult(resultEscape, '✓ Closed!');
        addLog('⚡ SHORTCUT: Escape — "Close panel" fired', 'shortcut');
      }

      if (e.shiftKey && e.key === '?') {
        flashResult(resultHelp, '✓ Help!');
        addLog('⚡ SHORTCUT: Shift+? — "Open help" fired', 'shortcut');
      }

      if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
        const arrows = { ArrowUp: '↑', ArrowDown: '↓', ArrowLeft: '←', ArrowRight: '→' };
        flashResult(resultArrow, arrows[e.key]);
        addLog(`⚡ SHORTCUT: Arrow key ${arrows[e.key]} detected`, 'shortcut');
      }
    });

    // ── keyup ────────────────────────────────────────────────────────────
    input.addEventListener('keyup', (e) => {
      updateModifiers(e);
      bigKey.classList.remove('pressed');
      valType.textContent = 'keyup';
      addLog(`↑ keyup    key="${e.key}"  code="${e.code}"`, 'up');
    });
  </script>

</body>
</html>
```

---

## CODEPEN 4 — Event Delegation with Dynamic List

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Event Delegation — Dynamic Task List</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, -apple-system, sans-serif;
      background: #f8fafc;
      color: #1e293b;
      min-height: 100vh;
      padding: 2rem 1rem;
    }

    .container {
      max-width: 680px;
      margin: 0 auto;
    }

    h1 { font-size: 1.5rem; color: #0f172a; margin-bottom: 0.25rem; }
    .subtitle { color: #64748b; font-size: 0.9rem; margin-bottom: 1.5rem; }

    /* ── Info banner ── */
    .info-banner {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      margin-bottom: 1.25rem;
      font-size: 0.85rem;
      color: #1e40af;
    }

    .info-banner strong { display: block; margin-bottom: 0.25rem; }

    .listener-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: #dbeafe;
      border: 1px solid #93c5fd;
      border-radius: 20px;
      padding: 0.2rem 0.7rem;
      font-size: 0.78rem;
      font-weight: 700;
      color: #1d4ed8;
      margin-top: 0.35rem;
    }

    .listener-count {
      background: #1d4ed8;
      color: white;
      border-radius: 20px;
      padding: 0 0.4rem;
      font-size: 0.7rem;
    }

    /* ── Add Task Form ── */
    .add-form {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1rem;
    }

    .task-input {
      flex: 1;
      padding: 0.65rem 0.9rem;
      border: 2px solid #e2e8f0;
      border-radius: 8px;
      font-size: 0.95rem;
      color: #1e293b;
      background: white;
      outline: none;
      transition: border-color 0.2s;
    }

    .task-input:focus {
      border-color: #3b82f6;
      box-shadow: 0 0 0 3px rgba(59,130,246,0.1);
    }

    .add-btn {
      padding: 0.65rem 1.25rem;
      background: #3b82f6;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.15s;
      white-space: nowrap;
    }

    .add-btn:hover { background: #2563eb; }

    /* ── Task List ── */
    .task-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .task-item {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      background: white;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 0.75rem 1rem;
      box-shadow: 0 1px 2px rgba(0,0,0,0.04);
      transition: box-shadow 0.15s, opacity 0.2s;
      animation: slideIn 0.2s ease;
    }

    @keyframes slideIn {
      from { opacity: 0; transform: translateY(-6px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    .task-item.removing {
      opacity: 0;
      transform: translateX(20px);
      transition: opacity 0.2s, transform 0.2s;
    }

    .task-item.editing {
      border-color: #3b82f6;
      box-shadow: 0 0 0 3px rgba(59,130,246,0.1);
    }

    .task-check {
      width: 18px;
      height: 18px;
      cursor: pointer;
      flex-shrink: 0;
      accent-color: #3b82f6;
    }

    .task-text {
      flex: 1;
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.4;
    }

    .task-item.done .task-text {
      text-decoration: line-through;
      color: #94a3b8;
    }

    .task-edit-input {
      flex: 1;
      border: none;
      outline: none;
      font-size: 0.95rem;
      color: #334155;
      background: transparent;
      display: none;
    }

    .task-item.editing .task-text       { display: none; }
    .task-item.editing .task-edit-input { display: block; }

    .task-actions {
      display: flex;
      gap: 0.35rem;
      flex-shrink: 0;
    }

    .btn-edit,
    .btn-save,
    .btn-delete {
      padding: 0.3rem 0.65rem;
      border: none;
      border-radius: 6px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      transition: opacity 0.15s;
    }

    .btn-edit   { background: #f1f5f9; color: #475569; }
    .btn-save   { background: #dcfce7; color: #166534; display: none; }
    .btn-delete { background: #fee2e2; color: #991b1b; }

    .task-item.editing .btn-edit   { display: none; }
    .task-item.editing .btn-save   { display: inline-block; }

    .btn-edit:hover   { background: #e2e8f0; }
    .btn-save:hover   { background: #bbf7d0; }
    .btn-delete:hover { background: #fecaca; }

    /* ── Empty State ── */
    .empty-state {
      text-align: center;
      padding: 3rem 1rem;
      color: #94a3b8;
      border: 2px dashed #e2e8f0;
      border-radius: 10px;
    }

    .empty-state p { margin-top: 0.5rem; font-size: 0.875rem; }

    /* ── Event log ── */
    .log-section {
      margin-top: 1.5rem;
      background: #0f172a;
      border-radius: 10px;
      overflow: hidden;
    }

    .log-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.6rem 1rem;
      border-bottom: 1px solid #1e293b;
    }

    .log-title {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #64748b;
    }

    .clear-log {
      background: none;
      border: none;
      color: #475569;
      font-size: 0.75rem;
      cursor: pointer;
    }

    .log-entries {
      padding: 0.5rem;
      max-height: 130px;
      overflow-y: auto;
      font-family: 'Courier New', monospace;
      font-size: 0.75rem;
    }

    .log-entry {
      padding: 0.15rem 0.4rem;
      color: #94a3b8;
    }

    .log-entry.add    { color: #4ade80; }
    .log-entry.delete { color: #f87171; }
    .log-entry.edit   { color: #fbbf24; }
    .log-entry.check  { color: #60a5fa; }
    .log-entry.system { color: #a78bfa; }
  </style>
</head>
<body>

  <div class="container">

    <h1>Event Delegation — Dynamic Task List</h1>
    <p class="subtitle">All clicks are handled by a single listener on the <code>&lt;ul&gt;</code> — including items added after load.</p>

    <div class="info-banner">
      <strong>How this works:</strong>
      ONE <code>click</code> listener is attached to the <code>&lt;ul&gt;</code>. When you click any Edit, Save, Delete, or checkbox inside it — the click bubbles up and the single handler uses <code>event.target.closest()</code> to figure out what was clicked.
      <br>
      <span class="listener-badge">
        Total event listeners on list items:
        <span class="listener-count" id="listener-count">0</span>
        (always zero!)
      </span>
    </div>

    <!-- Add task form -->
    <div class="add-form">
      <input
        type="text"
        class="task-input"
        id="task-input"
        placeholder="Add a new task…"
        maxlength="120"
      >
      <button class="add-btn" id="add-btn">Add Task</button>
    </div>

    <!-- The list — ONE listener attached here in JS -->
    <ul class="task-list" id="task-list">
      <!-- Initial items loaded by JS -->
    </ul>

    <!-- Event log -->
    <div class="log-section">
      <div class="log-header">
        <span class="log-title">Delegation Log — all events handled by one listener</span>
        <button class="clear-log" id="clear-log">Clear</button>
      </div>
      <div class="log-entries" id="log"></div>
    </div>

  </div>

  <script>
    const taskList  = document.getElementById('task-list');
    const taskInput = document.getElementById('task-input');
    const addBtn    = document.getElementById('add-btn');
    const log       = document.getElementById('log');
    let taskId      = 0;

    // ── Create a task item element ────────────────────────────────────────
    function createTaskElement(text) {
      taskId++;
      const li = document.createElement('li');
      li.className = 'task-item';
      li.dataset.id = taskId;
      li.innerHTML = `
        <input type="checkbox" class="task-check" aria-label="Mark task complete">
        <span class="task-text">${escapeHTML(text)}</span>
        <input type="text" class="task-edit-input" value="${escapeHTML(text)}" maxlength="120">
        <div class="task-actions">
          <button class="btn-edit" data-action="edit">Edit</button>
          <button class="btn-save" data-action="save">Save</button>
          <button class="btn-delete" data-action="delete">Delete</button>
        </div>
      `;
      return li;
    }

    function escapeHTML(str) {
      return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // ── Add task ──────────────────────────────────────────────────────────
    function addTask() {
      const text = taskInput.value.trim();
      if (!text) {
        taskInput.focus();
        return;
      }

      // Remove empty state if present
      const empty = taskList.querySelector('.empty-state');
      if (empty) empty.remove();

      const li = createTaskElement(text);
      taskList.appendChild(li);
      taskInput.value = '';
      taskInput.focus();

      addLog(`Task #${taskId} added: "${text.substring(0, 30)}${text.length > 30 ? '…' : ''}"`, 'add');
    }

    // ── THE SINGLE DELEGATED LISTENER ─────────────────────────────────────
    // This one listener on taskList handles ALL interactions for ALL items,
    // including items that don't exist yet when this code runs.
    taskList.addEventListener('click', (event) => {

      // --- Check button ---
      const checkbox = event.target.closest('.task-check');
      if (checkbox) {
        const li = checkbox.closest('.task-item');
        li.classList.toggle('done', checkbox.checked);
        const text = li.querySelector('.task-text').textContent;
        addLog(`Task #${li.dataset.id} ${checkbox.checked ? 'checked' : 'unchecked'}: "${text.substring(0, 25)}…"`, 'check');
        return;
      }

      // Look for a button with a data-action attribute
      const btn = event.target.closest('button[data-action]');
      if (!btn) return; // Click was in empty space — ignore

      const li     = btn.closest('.task-item');
      const id     = li.dataset.id;
      const action = btn.dataset.action;

      if (action === 'delete') {
        const text = li.querySelector('.task-text').textContent;
        addLog(`Task #${id} deleted: "${text.substring(0, 30)}${text.length > 30 ? '…' : ''}"`, 'delete');

        li.classList.add('removing');
        setTimeout(() => {
          li.remove();
          if (taskList.children.length === 0) showEmptyState();
        }, 200);
      }

      else if (action === 'edit') {
        li.classList.add('editing');
        const editInput = li.querySelector('.task-edit-input');
        editInput.focus();
        editInput.select();
        addLog(`Task #${id} — edit mode activated`, 'edit');
      }

      else if (action === 'save') {
        const editInput  = li.querySelector('.task-edit-input');
        const taskText   = li.querySelector('.task-text');
        const newText    = editInput.value.trim();
        if (newText) {
          taskText.textContent = newText;
          editInput.value      = newText;
        }
        li.classList.remove('editing');
        addLog(`Task #${id} saved: "${newText.substring(0, 30)}${newText.length > 30 ? '…' : ''}"`, 'edit');
      }
    });

    // ── Empty state ───────────────────────────────────────────────────────
    function showEmptyState() {
      const div = document.createElement('div');
      div.className = 'empty-state';
      div.innerHTML = '<strong>No tasks yet</strong><p>Add a task above to get started.</p>';
      taskList.appendChild(div);
    }

    // ── Add button & Enter key ────────────────────────────────────────────
    addBtn.addEventListener('click', addTask);
    taskInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') addTask();
    });

    // ── Log helper ────────────────────────────────────────────────────────
    function addLog(message, cls = '') {
      const entry = document.createElement('div');
      entry.className = 'log-entry ' + cls;
      const time = new Date().toLocaleTimeString('en-US', { hour12: false });
      entry.textContent = `[${time}] ${message}`;
      log.prepend(entry);
      const entries = log.querySelectorAll('.log-entry');
      if (entries.length > 40) entries[entries.length - 1].remove();
    }

    document.getElementById('clear-log').addEventListener('click', () => {
      log.innerHTML = '';
    });

    // ── Seed initial tasks ────────────────────────────────────────────────
    const seedTasks = [
      'Read the event delegation section of the lesson',
      'Try clicking Edit on a task to rename it',
      'Add a new task using the input above',
      'Delete a task and watch the log',
    ];

    seedTasks.forEach(text => {
      taskList.appendChild(createTaskElement(text));
    });

    addLog('Demo loaded. ONE listener on <ul> handles all ' + seedTasks.length + ' items.', 'system');
    addLog('Note: listener count on list items is always 0 — delegation at work!', 'system');
  </script>

</body>
</html>
```

---

## CODEPEN 5 — Form Events & Validation

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Form Events & Validation</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, -apple-system, sans-serif;
      background: #f1f5f9;
      color: #1e293b;
      min-height: 100vh;
      padding: 2rem 1rem;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .page-header {
      text-align: center;
      margin-bottom: 2rem;
      max-width: 480px;
    }

    h1 { font-size: 1.5rem; color: #0f172a; margin-bottom: 0.25rem; }
    .subtitle { color: #64748b; font-size: 0.9rem; }

    /* ── Card ── */
    .card {
      background: white;
      border-radius: 16px;
      padding: 2rem;
      box-shadow: 0 4px 24px rgba(0,0,0,0.08);
      width: 100%;
      max-width: 480px;
    }

    .card h2 {
      font-size: 1.15rem;
      margin-bottom: 1.5rem;
      color: #0f172a;
    }

    /* ── Field ── */
    .field {
      margin-bottom: 1.25rem;
    }

    label {
      display: block;
      font-size: 0.85rem;
      font-weight: 600;
      color: #475569;
      margin-bottom: 0.35rem;
    }

    label .required {
      color: #ef4444;
      margin-left: 2px;
    }

    .input-wrap {
      position: relative;
    }

    input[type="text"],
    input[type="email"],
    input[type="password"] {
      width: 100%;
      padding: 0.65rem 2.5rem 0.65rem 0.9rem;
      border: 2px solid #e2e8f0;
      border-radius: 8px;
      font-size: 0.95rem;
      color: #1e293b;
      background: white;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }

    input:focus {
      border-color: #3b82f6;
      box-shadow: 0 0 0 3px rgba(59,130,246,0.1);
    }

    /* Validation state borders */
    input.valid   { border-color: #22c55e; }
    input.invalid { border-color: #ef4444; }

    input.valid:focus   { box-shadow: 0 0 0 3px rgba(34,197,94,0.12); }
    input.invalid:focus { box-shadow: 0 0 0 3px rgba(239,68,68,0.12); }

    /* Status icon */
    .status-icon {
      position: absolute;
      right: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1rem;
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.2s;
    }

    input.valid   + .status-icon,
    input.invalid + .status-icon { opacity: 1; }

    /* Error / helper message */
    .field-message {
      font-size: 0.78rem;
      margin-top: 0.35rem;
      min-height: 1rem;
      transition: color 0.2s;
    }

    .field-message.error  { color: #dc2626; }
    .field-message.hint   { color: #64748b; }
    .field-message.ok     { color: #16a34a; }

    /* Password strength bar */
    .strength-bar {
      height: 4px;
      border-radius: 2px;
      background: #e2e8f0;
      margin-top: 0.4rem;
      overflow: hidden;
    }

    .strength-fill {
      height: 100%;
      border-radius: 2px;
      transition: width 0.3s, background 0.3s;
      width: 0;
    }

    /* ── Submit button ── */
    .submit-btn {
      width: 100%;
      padding: 0.8rem;
      background: #3b82f6;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.15s, transform 0.1s;
      margin-top: 0.5rem;
    }

    .submit-btn:hover    { background: #2563eb; }
    .submit-btn:active   { transform: scale(0.99); }
    .submit-btn:disabled { background: #94a3b8; cursor: not-allowed; }

    /* ── Event log strip ── */
    .event-strip {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin-bottom: 1.25rem;
    }

    .event-pill {
      font-size: 0.7rem;
      font-weight: 700;
      padding: 0.2rem 0.6rem;
      border-radius: 20px;
      opacity: 0.3;
      transition: opacity 0.1s, background 0.1s;
    }

    .event-pill.lit { opacity: 1; }

    .pill-input    { background: #dbeafe; color: #1d4ed8; }
    .pill-change   { background: #fef9c3; color: #854d0e; }
    .pill-focus    { background: #dcfce7; color: #166534; }
    .pill-blur     { background: #fee2e2; color: #991b1b; }
    .pill-submit   { background: #f3e8ff; color: #6b21a8; }
    .pill-reset    { background: #f1f5f9; color: #475569; }

    /* ── Success panel ── */
    .success-panel {
      display: none;
      background: #f0fdf4;
      border: 2px solid #86efac;
      border-radius: 12px;
      padding: 1.5rem;
      text-align: center;
      animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.97); }
      to   { opacity: 1; transform: scale(1); }
    }

    .success-panel.visible { display: block; }

    .success-icon { font-size: 2.5rem; margin-bottom: 0.5rem; }

    .success-panel h3 {
      color: #166534;
      margin-bottom: 0.75rem;
    }

    .success-data {
      text-align: left;
      background: white;
      border: 1px solid #86efac;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      color: #374151;
      margin-bottom: 1rem;
    }

    .success-data .data-row {
      display: flex;
      gap: 0.5rem;
      padding: 0.2rem 0;
    }

    .data-key   { color: #6b21a8; font-weight: 700; min-width: 100px; }
    .data-val   { color: #1e293b; }

    .try-again-btn {
      background: #166534;
      color: white;
      border: none;
      border-radius: 8px;
      padding: 0.6rem 1.5rem;
      font-weight: 700;
      cursor: pointer;
      font-size: 0.9rem;
    }

    .try-again-btn:hover { background: #14532d; }
  </style>
</head>
<body>

  <div class="page-header">
    <h1>Form Events & Validation</h1>
    <p class="subtitle">Watch the event indicator strip — every form event fires in real time.</p>
  </div>

  <div class="card">

    <!-- Event indicators -->
    <div class="event-strip">
      <span class="event-pill pill-input"  id="pill-input">input</span>
      <span class="event-pill pill-change" id="pill-change">change</span>
      <span class="event-pill pill-focus"  id="pill-focus">focus</span>
      <span class="event-pill pill-blur"   id="pill-blur">blur</span>
      <span class="event-pill pill-submit" id="pill-submit">submit</span>
      <span class="event-pill pill-reset"  id="pill-reset">reset</span>
    </div>

    <!-- The form -->
    <form id="signup-form" novalidate>
      <h2>Create Account</h2>

      <!-- Name -->
      <div class="field">
        <label for="name">Full Name <span class="required">*</span></label>
        <div class="input-wrap">
          <input type="text" id="name" name="name" autocomplete="off" placeholder="Jane Smith">
          <span class="status-icon" id="name-icon"></span>
        </div>
        <div class="field-message hint" id="name-msg">Enter your first and last name.</div>
      </div>

      <!-- Email -->
      <div class="field">
        <label for="email">Email Address <span class="required">*</span></label>
        <div class="input-wrap">
          <input type="email" id="email" name="email" autocomplete="off" placeholder="jane@example.com">
          <span class="status-icon" id="email-icon"></span>
        </div>
        <div class="field-message hint" id="email-msg">We'll never share your email.</div>
      </div>

      <!-- Password -->
      <div class="field">
        <label for="password">Password <span class="required">*</span></label>
        <div class="input-wrap">
          <input type="password" id="password" name="password" autocomplete="new-password" placeholder="At least 8 characters">
          <span class="status-icon" id="password-icon"></span>
        </div>
        <div class="strength-bar"><div class="strength-fill" id="strength-fill"></div></div>
        <div class="field-message hint" id="password-msg">Min 8 chars, include a number and a symbol.</div>
      </div>

      <!-- Confirm Password -->
      <div class="field">
        <label for="confirm">Confirm Password <span class="required">*</span></label>
        <div class="input-wrap">
          <input type="password" id="confirm" name="confirm" autocomplete="new-password" placeholder="Repeat your password">
          <span class="status-icon" id="confirm-icon"></span>
        </div>
        <div class="field-message hint" id="confirm-msg">Re-enter your password to confirm.</div>
      </div>

      <button type="submit" class="submit-btn" id="submit-btn">Create Account</button>
      <button type="reset"  style="display:none" id="hidden-reset">Reset</button>
    </form>

    <!-- Success panel (hidden until submit) -->
    <div class="success-panel" id="success-panel">
      <div class="success-icon">✓</div>
      <h3>Account Created!</h3>
      <div class="success-data" id="success-data"></div>
      <button class="try-again-btn" id="try-again">Try Again</button>
    </div>

  </div>

  <script>
    const form     = document.getElementById('signup-form');
    const nameEl   = document.getElementById('name');
    const emailEl  = document.getElementById('email');
    const passEl   = document.getElementById('password');
    const confEl   = document.getElementById('confirm');

    // ── Pill flash helper ─────────────────────────────────────────────────
    const pillTimers = {};
    function flashPill(id) {
      const pill = document.getElementById('pill-' + id);
      if (!pill) return;
      pill.classList.add('lit');
      clearTimeout(pillTimers[id]);
      pillTimers[id] = setTimeout(() => pill.classList.remove('lit'), 600);
    }

    // ── Field state helpers ───────────────────────────────────────────────
    function setValid(input, iconEl, msgEl, msg) {
      input.classList.remove('invalid');
      input.classList.add('valid');
      iconEl.textContent = '✓';
      msgEl.textContent  = msg || '';
      msgEl.className    = 'field-message ok';
    }

    function setInvalid(input, iconEl, msgEl, msg) {
      input.classList.remove('valid');
      input.classList.add('invalid');
      iconEl.textContent = '✕';
      msgEl.textContent  = msg;
      msgEl.className    = 'field-message error';
    }

    function clearState(input, iconEl, msgEl, hint) {
      input.classList.remove('valid', 'invalid');
      iconEl.textContent = '';
      msgEl.textContent  = hint;
      msgEl.className    = 'field-message hint';
    }

    // ── Validation functions ──────────────────────────────────────────────
    function validateName() {
      const v = nameEl.value.trim();
      const icon = document.getElementById('name-icon');
      const msg  = document.getElementById('name-msg');
      if (!v)          { setInvalid(nameEl, icon, msg, 'Full name is required.'); return false; }
      if (v.length < 2){ setInvalid(nameEl, icon, msg, 'Name must be at least 2 characters.'); return false; }
      if (!v.includes(' ')){ setInvalid(nameEl, icon, msg, 'Please enter both first and last name.'); return false; }
      setValid(nameEl, icon, msg, 'Looks good!');
      return true;
    }

    function validateEmail() {
      const v = emailEl.value.trim();
      const icon = document.getElementById('email-icon');
      const msg  = document.getElementById('email-msg');
      if (!v) { setInvalid(emailEl, icon, msg, 'Email address is required.'); return false; }
      const ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
      if (!ok) { setInvalid(emailEl, icon, msg, 'Please enter a valid email address.'); return false; }
      setValid(emailEl, icon, msg, 'Valid email address.');
      return true;
    }

    function getPasswordStrength(v) {
      let score = 0;
      if (v.length >= 8)  score++;
      if (v.length >= 12) score++;
      if (/[0-9]/.test(v)) score++;
      if (/[^a-zA-Z0-9]/.test(v)) score++;
      if (/[A-Z]/.test(v) && /[a-z]/.test(v)) score++;
      return score; // 0–5
    }

    function validatePassword() {
      const v    = passEl.value;
      const icon = document.getElementById('password-icon');
      const msg  = document.getElementById('password-msg');
      const fill = document.getElementById('strength-fill');
      const score = getPasswordStrength(v);

      const colors  = ['#ef4444', '#f97316', '#eab308', '#22c55e', '#16a34a'];
      const labels  = ['Very weak', 'Weak', 'Fair', 'Strong', 'Very strong'];
      const widths  = ['20%', '40%', '60%', '80%', '100%'];

      if (!v) {
        clearState(passEl, icon, msg, 'Min 8 chars, include a number and a symbol.');
        fill.style.width = '0';
        return false;
      }

      if (score < 3) {
        fill.style.width      = widths[score] || '20%';
        fill.style.background = colors[score] || '#ef4444';
        setInvalid(passEl, icon, msg, labels[score] + ' — add numbers, symbols, or more length.');
        return false;
      }

      fill.style.width      = widths[score - 1];
      fill.style.background = colors[score - 1];
      setValid(passEl, icon, msg, labels[score - 1] + ' password.');
      return true;
    }

    function validateConfirm() {
      const icon = document.getElementById('confirm-icon');
      const msg  = document.getElementById('confirm-msg');
      if (!confEl.value) {
        clearState(confEl, icon, msg, 'Re-enter your password to confirm.');
        return false;
      }
      if (confEl.value !== passEl.value) {
        setInvalid(confEl, icon, msg, 'Passwords do not match.');
        return false;
      }
      setValid(confEl, icon, msg, 'Passwords match!');
      return true;
    }

    // ── input event — real-time feedback ─────────────────────────────────
    nameEl.addEventListener('input',  () => { flashPill('input'); validateName(); });
    emailEl.addEventListener('input', () => { flashPill('input'); validateEmail(); });
    passEl.addEventListener('input',  () => {
      flashPill('input');
      validatePassword();
      if (confEl.value) validateConfirm(); // Keep confirm in sync
    });
    confEl.addEventListener('input',  () => { flashPill('input'); validateConfirm(); });

    // ── change event ──────────────────────────────────────────────────────
    [nameEl, emailEl, passEl, confEl].forEach(el => {
      el.addEventListener('change', () => flashPill('change'));
    });

    // ── focus / blur ──────────────────────────────────────────────────────
    [nameEl, emailEl, passEl, confEl].forEach(el => {
      el.addEventListener('focus', () => flashPill('focus'));
      el.addEventListener('blur',  () => flashPill('blur'));
    });

    // Validate on blur (when user leaves a field)
    nameEl.addEventListener('blur',  validateName);
    emailEl.addEventListener('blur', validateEmail);
    passEl.addEventListener('blur',  validatePassword);
    confEl.addEventListener('blur',  validateConfirm);

    // ── submit event ──────────────────────────────────────────────────────
    form.addEventListener('submit', (event) => {
      event.preventDefault(); // Always prevent the default page reload
      flashPill('submit');

      const allValid = validateName() & validateEmail() & validatePassword() & validateConfirm();

      if (!allValid) {
        // Focus the first invalid field
        const firstInvalid = form.querySelector('.invalid');
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      // Show success
      form.style.display = 'none';
      const successPanel = document.getElementById('success-panel');
      const successData  = document.getElementById('success-data');

      successData.innerHTML = `
        <div class="data-row"><span class="data-key">name:</span><span class="data-val">${escapeHTML(nameEl.value.trim())}</span></div>
        <div class="data-row"><span class="data-key">email:</span><span class="data-val">${escapeHTML(emailEl.value.trim())}</span></div>
        <div class="data-row"><span class="data-key">password:</span><span class="data-val">${'•'.repeat(passEl.value.length)} (${passEl.value.length} chars)</span></div>
        <div class="data-row"><span class="data-key">submitted:</span><span class="data-val">${new Date().toLocaleString()}</span></div>
      `;
      successPanel.classList.add('visible');
    });

    // ── reset event ───────────────────────────────────────────────────────
    form.addEventListener('reset', () => {
      flashPill('reset');

      // Clear all custom validation state — the browser resets field values,
      // but NOT our added classes and error messages.
      [
        { input: nameEl,  icon: 'name-icon',     msg: 'name-msg',     hint: 'Enter your first and last name.' },
        { input: emailEl, icon: 'email-icon',    msg: 'email-msg',    hint: "We'll never share your email." },
        { input: passEl,  icon: 'password-icon', msg: 'password-msg', hint: 'Min 8 chars, include a number and a symbol.' },
        { input: confEl,  icon: 'confirm-icon',  msg: 'confirm-msg',  hint: 'Re-enter your password to confirm.' },
      ].forEach(({ input, icon, msg, hint }) => {
        clearState(input, document.getElementById(icon), document.getElementById(msg), hint);
      });

      document.getElementById('strength-fill').style.width = '0';
    });

    // ── Try again ─────────────────────────────────────────────────────────
    document.getElementById('try-again').addEventListener('click', () => {
      document.getElementById('success-panel').classList.remove('visible');
      form.style.display = '';
      form.reset();
      nameEl.focus();
    });

    function escapeHTML(str) {
      return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }
  </script>

</body>
</html>
```
