# Day 26 — Strings & Numbers In Depth + Timers — CodePens

---

## CODEPEN 1 — String Method Playground

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>String Method Playground</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }
    .layout { max-width: 800px; margin: 0 auto; }
    textarea {
      width: 100%; padding: 0.75rem 1rem; border: 2px solid #e5e7eb;
      border-radius: 10px; font-size: 0.95rem; font-family: inherit;
      resize: vertical; min-height: 80px; outline: none; transition: border-color 0.2s;
      margin-bottom: 1rem;
    }
    textarea:focus { border-color: #4f46e5; }
    .btn-grid { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.25rem; }
    .mbtn {
      padding: 0.45rem 0.85rem; border: none; border-radius: 20px;
      font-size: 0.82rem; font-weight: 600; cursor: pointer; transition: all 0.15s;
    }
    .mbtn:hover { filter: brightness(0.9); }
    .cat-case   .mbtn { background: #dbeafe; color: #1d4ed8; }
    .cat-search .mbtn { background: #dcfce7; color: #166534; }
    .cat-edit   .mbtn { background: #fce7f3; color: #9d174d; }
    .cat-info   .mbtn { background: #fef3c7; color: #92400e; }
    .result-panel {
      background: #1e1e2e; border-radius: 12px; padding: 1.1rem 1.25rem; min-height: 80px;
    }
    .r-method { font-family: monospace; font-size: 0.78rem; color: #888; margin-bottom: 0.4rem; }
    .r-value  { font-family: monospace; font-size: 1rem; color: #a9dc76; word-break: break-all; }
    .r-placeholder { color: #555; font-size: 0.85rem; font-style: italic; }
  </style>
</head>
<body>
  <h1>String Method Playground</h1>
  <p class="subtitle">Type any text, then click a method to transform it.</p>
  <div class="layout">
    <textarea id="input">  Hello, World! This is JavaScript.  </textarea>

    <div class="btn-grid">
      <div class="cat-case">
        <button class="mbtn" onclick="run('toUpperCase()', s => s.toUpperCase())">toUpperCase()</button>
        <button class="mbtn" onclick="run('toLowerCase()', s => s.toLowerCase())">toLowerCase()</button>
        <button class="mbtn" onclick="run('Title Case', s => s.toLowerCase().replace(/\b\w/g, c => c.toUpperCase()))">Title Case</button>
      </div>
      <div class="cat-edit" style="display:contents">
        <button class="mbtn" style="background:#fce7f3;color:#9d174d" onclick="run('trim()', s => s.trim())">trim()</button>
        <button class="mbtn" style="background:#fce7f3;color:#9d174d" onclick="run('replaceAll(\" \", \"-\")', s => s.trim().replaceAll(' ', '-'))">spaces→dashes</button>
        <button class="mbtn" style="background:#fce7f3;color:#9d174d" onclick="run('remove vowels', s => s.replace(/[aeiou]/gi, ''))">Remove Vowels</button>
        <button class="mbtn" style="background:#fce7f3;color:#9d174d" onclick="run('reverse', s => s.split('').reverse().join(''))">Reverse</button>
      </div>
      <div class="cat-search" style="display:contents">
        <button class="mbtn" style="background:#dcfce7;color:#166534" onclick="run('includes(\"JavaScript\")', s => String(s.includes('JavaScript')))">includes("JavaScript")?</button>
        <button class="mbtn" style="background:#dcfce7;color:#166534" onclick="run('startsWith(\"Hello\")', s => String(s.trim().startsWith('Hello')))">startsWith("Hello")?</button>
        <button class="mbtn" style="background:#dcfce7;color:#166534" onclick="run('indexOf(\"!\")', s => String(s.indexOf('!')))">indexOf("!")</button>
      </div>
      <div class="cat-info" style="display:contents">
        <button class="mbtn" style="background:#fef3c7;color:#92400e" onclick="run('length', s => String(s.length))">length</button>
        <button class="mbtn" style="background:#fef3c7;color:#92400e" onclick="run('word count', s => String(s.trim().split(/\s+/).filter(Boolean).length) + ' words')">Word Count</button>
        <button class="mbtn" style="background:#fef3c7;color:#92400e" onclick="run('slice(0,10)+\"...\"', s => s.trim().slice(0, 10) + '...')">Truncate (10)</button>
        <button class="mbtn" style="background:#fef3c7;color:#92400e" onclick="run('split(\" \")', s => JSON.stringify(s.trim().split(' ')))">split(" ")</button>
      </div>
    </div>

    <div class="result-panel">
      <div class="r-method" id="rMethod">Click a button to apply a string method.</div>
      <div class="r-value"  id="rValue"><span class="r-placeholder">Result appears here.</span></div>
    </div>
  </div>

  <script>
    function run(methodLabel, fn) {
      const str = document.getElementById('input').value;
      const result = fn(str);
      document.getElementById('rMethod').textContent = 'str.' + methodLabel + '  →';
      document.getElementById('rValue').textContent = result;
    }
  </script>
</body>
</html>
```

---

## CODEPEN 2 — Price/Number Formatter with Intl.NumberFormat

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Intl.NumberFormat Formatter</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }
    .container { max-width: 760px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.25rem; }

    .panel { background: #fff; border-radius: 12px; padding: 1.25rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
    .panel h2 { font-size: 0.95rem; margin-bottom: 1rem; color: #1a1a2e; }

    .input-row { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; flex-wrap: wrap; }
    label { font-size: 0.85rem; font-weight: 600; color: #555; }
    input[type="number"] {
      padding: 0.5rem 0.75rem; border: 2px solid #e5e7eb; border-radius: 8px;
      font-size: 1rem; width: 160px; outline: none; transition: border-color 0.2s;
    }
    input[type="number"]:focus { border-color: #4f46e5; }

    .format-btns { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem; }
    .fbtn {
      padding: 0.45rem 0.9rem; border: 2px solid #e5e7eb; border-radius: 20px;
      font-size: 0.83rem; font-weight: 600; cursor: pointer; background: #fff;
      color: #374151; transition: all 0.2s;
    }
    .fbtn:hover { border-color: #4f46e5; color: #4f46e5; }
    .fbtn.active { background: #4f46e5; color: #fff; border-color: #4f46e5; }

    .result-display {
      background: #f8f9ff; border-radius: 10px; padding: 1rem 1.25rem;
      text-align: center;
    }
    .result-formatted { font-size: 2rem; font-weight: 800; color: #4f46e5; }
    .result-code { font-size: 0.75rem; font-family: monospace; color: #888; margin-top: 0.4rem; }

    /* Floating point panel */
    .fp-panel { background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 1rem 1.25rem; }
    .fp-panel h2 { color: #92400e; }
    .fp-inputs { display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap; margin-bottom: 0.75rem; }
    .fp-inputs input { width: 90px; padding: 0.4rem 0.6rem; border: 1px solid #d1d5db; border-radius: 6px; font-size: 0.9rem; }
    .fp-add-btn {
      padding: 0.4rem 0.9rem; background: #f59e0b; color: #fff; border: none;
      border-radius: 8px; font-size: 0.85rem; font-weight: 700; cursor: pointer;
    }
    .fp-results { display: flex; gap: 0.75rem; flex-wrap: wrap; }
    .fp-result { flex: 1; min-width: 150px; border-radius: 8px; padding: 0.6rem 0.8rem; }
    .fp-result.raw      { background: #fee2e2; }
    .fp-result.formatted { background: #dcfce7; }
    .fp-label { font-size: 0.7rem; font-weight: 700; color: #555; margin-bottom: 0.2rem; }
    .fp-val   { font-size: 1rem; font-weight: 700; }
    .fp-result.raw .fp-val { color: #dc2626; }
    .fp-result.formatted .fp-val { color: #16a34a; }
  </style>
</head>
<body>
  <h1>Number Formatter</h1>
  <p class="subtitle">Format numbers correctly with <code>Intl.NumberFormat</code>.</p>

  <div class="container">
    <div class="panel">
      <h2>Format a Number</h2>
      <div class="input-row">
        <label>Value:</label>
        <input type="number" id="numInput" value="1234567.89" oninput="formatNumber()">
      </div>
      <div class="format-btns">
        <button class="fbtn active" data-fmt="usd"       onclick="setFmt(this)">USD ($)</button>
        <button class="fbtn"         data-fmt="eur"       onclick="setFmt(this)">EUR (€)</button>
        <button class="fbtn"         data-fmt="gbp"       onclick="setFmt(this)">GBP (£)</button>
        <button class="fbtn"         data-fmt="percent"   onclick="setFmt(this)">Percent</button>
        <button class="fbtn"         data-fmt="compact"   onclick="setFmt(this)">Compact</button>
        <button class="fbtn"         data-fmt="plain"     onclick="setFmt(this)">Plain (2 dec)</button>
      </div>
      <div class="result-display">
        <div class="result-formatted" id="fmtResult">$1,234,567.89</div>
        <div class="result-code" id="fmtCode">new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value)</div>
      </div>
    </div>

    <div class="fp-panel">
      <h2>⚠ The Floating-Point Problem</h2>
      <div class="fp-inputs">
        <input type="number" id="fp1" value="0.1" step="0.01">
        <span>+</span>
        <input type="number" id="fp2" value="0.2" step="0.01">
        <button class="fp-add-btn" onclick="fpCalc()">Calculate</button>
      </div>
      <div class="fp-results">
        <div class="fp-result raw">
          <div class="fp-label">Raw JavaScript result</div>
          <div class="fp-val" id="fpRaw">0.30000000000000004</div>
        </div>
        <div class="fp-result formatted">
          <div class="fp-label">Formatted with Intl.NumberFormat</div>
          <div class="fp-val" id="fpFormatted">0.30</div>
        </div>
      </div>
    </div>
  </div>

  <script>
    let currentFmt = 'usd';

    const formatters = {
      usd:     { locale: 'en-US',  opts: { style: 'currency', currency: 'USD' },     code: "new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value)" },
      eur:     { locale: 'de-DE',  opts: { style: 'currency', currency: 'EUR' },     code: "new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(value)" },
      gbp:     { locale: 'en-GB',  opts: { style: 'currency', currency: 'GBP' },     code: "new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP' }).format(value)" },
      percent: { locale: 'en-US',  opts: { style: 'percent', maximumFractionDigits: 1 }, code: "new Intl.NumberFormat('en-US', { style: 'percent' }).format(value / 100)" },
      compact: { locale: 'en-US',  opts: { notation: 'compact' },                    code: "new Intl.NumberFormat('en-US', { notation: 'compact' }).format(value)" },
      plain:   { locale: 'en-US',  opts: { minimumFractionDigits: 2, maximumFractionDigits: 2 }, code: "new Intl.NumberFormat('en-US', { minimumFractionDigits: 2 }).format(value)" },
    };

    function setFmt(btn) {
      document.querySelectorAll('.fbtn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFmt = btn.dataset.fmt;
      formatNumber();
    }

    function formatNumber() {
      let value = parseFloat(document.getElementById('numInput').value) || 0;
      const { locale, opts, code } = formatters[currentFmt];
      const displayValue = currentFmt === 'percent' ? value / 100 : value;
      const formatted = new Intl.NumberFormat(locale, opts).format(displayValue);
      document.getElementById('fmtResult').textContent = formatted;
      document.getElementById('fmtCode').textContent = code;
    }

    function fpCalc() {
      const a = parseFloat(document.getElementById('fp1').value) || 0;
      const b = parseFloat(document.getElementById('fp2').value) || 0;
      const raw = a + b;
      document.getElementById('fpRaw').textContent = String(raw);
      document.getElementById('fpFormatted').textContent =
        new Intl.NumberFormat('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(raw);
    }
  </script>
</body>
</html>
```

---

## CODEPEN 3 — Live Clock + Countdown Timer

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Live Clock & Countdown Timer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #1a1a2e; padding: 2rem 1rem; color: #e2e8f0; }
    h1 { text-align: center; font-size: 1.3rem; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #64748b; margin-bottom: 2rem; }
    .container { max-width: 600px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.5rem; }

    .card { background: #0f172a; border-radius: 16px; padding: 1.5rem; border: 1px solid #1e293b; }
    .card-label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; color: #64748b; margin-bottom: 1rem; }

    /* Clock */
    .clock-displays { display: flex; gap: 1rem; flex-wrap: wrap; }
    .clock-display { flex: 1; min-width: 120px; text-align: center; background: #1e293b; border-radius: 10px; padding: 0.75rem; }
    .clock-fmt { font-size: 0.7rem; color: #64748b; margin-bottom: 0.3rem; }
    .clock-time { font-size: 1.4rem; font-family: 'Courier New', monospace; font-weight: 700; color: #38bdf8; letter-spacing: 0.05em; }
    .clock-tz { font-size: 0.65rem; color: #475569; margin-top: 0.2rem; }
    .pulse { animation: pulse 1s ease-in-out infinite; }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }

    /* Countdown */
    .countdown-setup { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; flex-wrap: wrap; }
    .countdown-setup label { font-size: 0.85rem; color: #94a3b8; }
    input[type="number"] {
      padding: 0.4rem 0.6rem; background: #1e293b; border: 1px solid #334155;
      border-radius: 8px; color: #e2e8f0; font-size: 0.9rem; width: 80px; outline: none;
    }
    .cbtns { display: flex; gap: 0.5rem; flex-wrap: wrap; }
    .cbtn {
      padding: 0.45rem 1rem; border: none; border-radius: 8px;
      font-size: 0.85rem; font-weight: 700; cursor: pointer; transition: opacity 0.15s;
    }
    .cbtn:hover { opacity: 0.85; }
    .cbtn-start { background: #22c55e; color: #fff; }
    .cbtn-pause { background: #f59e0b; color: #fff; }
    .cbtn-reset { background: #475569; color: #fff; }

    .countdown-display { text-align: center; margin: 1rem 0; }
    .countdown-time { font-size: 3.5rem; font-family: 'Courier New', monospace; font-weight: 800; color: #38bdf8; transition: color 0.5s; }
    .countdown-time.warning { color: #f59e0b; }
    .countdown-time.done    { color: #ef4444; }
    .countdown-msg { font-size: 1rem; color: #ef4444; margin-top: 0.3rem; min-height: 1.4em; }

    .progress-bar { height: 6px; background: #1e293b; border-radius: 3px; overflow: hidden; }
    .progress-fill {
      height: 100%; background: #38bdf8; border-radius: 3px;
      transition: width 0.9s linear, background 0.5s;
    }
    .progress-fill.warning { background: #f59e0b; }
    .progress-fill.done    { background: #ef4444; }
  </style>
</head>
<body>
  <h1>Live Clock &amp; Countdown Timer</h1>
  <p class="subtitle">Using <code>setInterval</code> to update the DOM every second.</p>

  <div class="container">
    <!-- CLOCK -->
    <div class="card">
      <div class="card-label">⏰ Live Clock — setInterval updates every second</div>
      <div class="clock-displays">
        <div class="clock-display">
          <div class="clock-fmt">12-Hour</div>
          <div class="clock-time" id="clock12">--:--:-- --</div>
        </div>
        <div class="clock-display">
          <div class="clock-fmt">24-Hour</div>
          <div class="clock-time" id="clock24">--:--:--</div>
        </div>
        <div class="clock-display">
          <div class="clock-fmt">Seconds <span class="pulse" id="clockDot">●</span></div>
          <div class="clock-time" id="clockSec">--</div>
          <div class="clock-tz" id="clockTz"></div>
        </div>
      </div>
    </div>

    <!-- COUNTDOWN -->
    <div class="card">
      <div class="card-label">⏳ Countdown Timer — clearInterval stops it</div>
      <div class="countdown-setup">
        <label>Seconds:</label>
        <input type="number" id="durationInput" value="60" min="1" max="300">
        <div class="cbtns">
          <button class="cbtn cbtn-start" id="startBtn" onclick="startCountdown()">Start</button>
          <button class="cbtn cbtn-pause" id="pauseBtn" onclick="pauseCountdown()" disabled>Pause</button>
          <button class="cbtn cbtn-reset" onclick="resetCountdown()">Reset</button>
        </div>
      </div>
      <div class="countdown-display">
        <div class="countdown-time" id="countdownDisplay">01:00</div>
        <div class="countdown-msg" id="countdownMsg"></div>
      </div>
      <div class="progress-bar"><div class="progress-fill" id="progressFill" style="width:100%"></div></div>
    </div>
  </div>

  <script>
    // CLOCK
    function updateClock() {
      const now = new Date();
      const h24 = String(now.getHours()).padStart(2, '0');
      const min = String(now.getMinutes()).padStart(2, '0');
      const sec = String(now.getSeconds()).padStart(2, '0');
      const h12raw = now.getHours() % 12 || 12;
      const ampm   = now.getHours() < 12 ? 'AM' : 'PM';
      document.getElementById('clock12').textContent = `${String(h12raw).padStart(2,'0')}:${min}:${sec} ${ampm}`;
      document.getElementById('clock24').textContent = `${h24}:${min}:${sec}`;
      document.getElementById('clockSec').textContent = sec;
      document.getElementById('clockTz').textContent = Intl.DateTimeFormat().resolvedOptions().timeZone;
    }
    updateClock();
    setInterval(updateClock, 1000);

    // COUNTDOWN
    let countdownId = null;
    let remaining = 60;
    let totalDuration = 60;
    let running = false;

    function fmtTime(s) {
      return String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
    }

    function updateCountdownUI() {
      const el     = document.getElementById('countdownDisplay');
      const fill   = document.getElementById('progressFill');
      const pct    = (remaining / totalDuration) * 100;
      const isWarn = remaining <= Math.min(10, totalDuration * 0.2);
      const isDone = remaining === 0;

      el.textContent = fmtTime(remaining);
      el.className = 'countdown-time' + (isDone ? ' done' : isWarn ? ' warning' : '');
      fill.style.width = pct + '%';
      fill.className = 'progress-fill' + (isDone ? ' done' : isWarn ? ' warning' : '');
      document.getElementById('countdownMsg').textContent = isDone ? '⏰ Time\'s up!' : '';
    }

    function startCountdown() {
      if (running) return;
      if (remaining === 0) resetCountdown();
      totalDuration = totalDuration || parseInt(document.getElementById('durationInput').value) || 60;
      running = true;
      document.getElementById('startBtn').disabled = true;
      document.getElementById('pauseBtn').disabled = false;
      countdownId = setInterval(() => {
        remaining--;
        updateCountdownUI();
        if (remaining <= 0) {
          clearInterval(countdownId);
          running = false;
          document.getElementById('startBtn').disabled = false;
          document.getElementById('pauseBtn').disabled = true;
        }
      }, 1000);
    }

    function pauseCountdown() {
      if (!running) return;
      clearInterval(countdownId);
      running = false;
      document.getElementById('startBtn').disabled = false;
      document.getElementById('pauseBtn').disabled = true;
    }

    function resetCountdown() {
      clearInterval(countdownId);
      running = false;
      totalDuration = parseInt(document.getElementById('durationInput').value) || 60;
      remaining = totalDuration;
      document.getElementById('startBtn').disabled = false;
      document.getElementById('pauseBtn').disabled = true;
      document.getElementById('countdownMsg').textContent = '';
      updateCountdownUI();
    }

    resetCountdown();
  </script>
</body>
</html>
```

---

## CODEPEN 4 — Debounce Demo

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Debounce Demo</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 0.75rem; }
    .delay-row { text-align: center; margin-bottom: 1.5rem; font-size: 0.85rem; color: #555; }
    .delay-row input { margin: 0 0.5rem; vertical-align: middle; }
    .delay-label { font-weight: 700; color: #4f46e5; }

    .panels { display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; max-width: 800px; margin: 0 auto; }
    @media (max-width: 560px) { .panels { grid-template-columns: 1fr; } }

    .panel { background: #fff; border-radius: 12px; padding: 1.1rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
    .panel-bad  { border-top: 4px solid #ef4444; }
    .panel-good { border-top: 4px solid #22c55e; }
    .panel-title { font-weight: 700; font-size: 0.95rem; margin-bottom: 0.3rem; }
    .panel-bad  .panel-title { color: #ef4444; }
    .panel-good .panel-title { color: #22c55e; }
    .panel-sub { font-size: 0.75rem; color: #888; margin-bottom: 0.9rem; }

    input[type="text"] {
      width: 100%; padding: 0.5rem 0.75rem; border: 1.5px solid #e5e7eb;
      border-radius: 8px; font-size: 0.9rem; outline: none; margin-bottom: 0.75rem;
      transition: border-color 0.2s;
    }
    input[type="text"]:focus { border-color: #4f46e5; }

    .counter { font-size: 1.8rem; font-weight: 800; text-align: center; margin-bottom: 0.5rem; }
    .panel-bad  .counter { color: #ef4444; }
    .panel-good .counter { color: #22c55e; }
    .counter-label { text-align: center; font-size: 0.72rem; color: #888; margin-bottom: 0.75rem; }

    .status { font-size: 0.78rem; padding: 0.3rem 0.6rem; border-radius: 6px; text-align: center; margin-bottom: 0.75rem; }
    .status-bad  { background: #fef2f2; color: #dc2626; }
    .status-good { background: #f0fdf4; color: #16a34a; }

    .log { background: #f8f9ff; border-radius: 8px; padding: 0.5rem 0.7rem; max-height: 140px; overflow-y: auto; }
    .log-entry { font-size: 0.72rem; font-family: monospace; color: #555; padding: 0.15rem 0; border-bottom: 1px solid #f0f0f0; }
    .log-entry:last-child { border-bottom: none; }

    .reset-btn {
      display: block; margin: 1rem auto 0;
      padding: 0.45rem 1.25rem; background: #6b7280;
      color: #fff; border: none; border-radius: 8px;
      font-size: 0.85rem; font-weight: 600; cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>Debounce Demo</h1>
  <p class="subtitle">Why debouncing expensive event handlers is critical.</p>

  <div class="delay-row">
    Debounce delay: <input type="range" id="delaySlider" min="100" max="1000" step="50" value="400" oninput="updateDelay()">
    <span class="delay-label" id="delayLabel">400ms</span>
  </div>

  <div class="panels">
    <div class="panel panel-bad">
      <div class="panel-title">⚠ Without Debounce</div>
      <div class="panel-sub">Every keystroke fires an "API call" immediately.</div>
      <input type="text" id="rawInput" placeholder="Type to search…" oninput="rawHandler()">
      <div class="counter" id="rawCount">0</div>
      <div class="counter-label">API calls made</div>
      <div class="status status-bad">⚠ Too many requests!</div>
      <div class="log" id="rawLog"><div class="log-entry">Waiting for input…</div></div>
    </div>

    <div class="panel panel-good">
      <div class="panel-title">✓ With Debounce</div>
      <div class="panel-sub">Fires only after typing stops for <span id="goodDelay">400</span>ms.</div>
      <input type="text" id="debounceInput" placeholder="Type to search…" oninput="debounceHandler()">
      <div class="counter" id="debounceCount">0</div>
      <div class="counter-label">API calls made</div>
      <div class="status status-good">✓ Efficient — waits for pause!</div>
      <div class="log" id="debounceLog"><div class="log-entry">Waiting for input…</div></div>
    </div>
  </div>
  <button class="reset-btn" onclick="resetAll()">↺ Reset Counters</button>

  <script>
    let rawCount = 0, debounceCount = 0;
    let debounceTimer = null;
    let delayMs = 400;

    function updateDelay() {
      delayMs = parseInt(document.getElementById('delaySlider').value);
      document.getElementById('delayLabel').textContent = delayMs + 'ms';
      document.getElementById('goodDelay').textContent = delayMs + 'ms';
    }

    function addLog(logId, term) {
      const log = document.getElementById(logId);
      const t = new Date().toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
      const entry = document.createElement('div');
      entry.className = 'log-entry';
      entry.textContent = `${t} — API call for: "${term || '(empty)'}"`;
      log.insertBefore(entry, log.firstChild);
      if (log.children.length > 20) log.removeChild(log.lastChild);
    }

    function rawHandler() {
      rawCount++;
      document.getElementById('rawCount').textContent = rawCount;
      addLog('rawLog', document.getElementById('rawInput').value);
    }

    function debounce(fn, delay) {
      return function(...args) {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => fn.apply(this, args), delay);
      };
    }

    const debouncedSearch = debounce(function(value) {
      debounceCount++;
      document.getElementById('debounceCount').textContent = debounceCount;
      addLog('debounceLog', value);
    }, 0); // delay injected via wrapper below

    function debounceHandler() {
      clearTimeout(debounceTimer);
      const value = document.getElementById('debounceInput').value;
      debounceTimer = setTimeout(() => {
        debounceCount++;
        document.getElementById('debounceCount').textContent = debounceCount;
        addLog('debounceLog', value);
      }, delayMs);
    }

    function resetAll() {
      rawCount = debounceCount = 0;
      clearTimeout(debounceTimer);
      document.getElementById('rawCount').textContent = '0';
      document.getElementById('debounceCount').textContent = '0';
      document.getElementById('rawInput').value = '';
      document.getElementById('debounceInput').value = '';
      document.getElementById('rawLog').innerHTML = '<div class="log-entry">Waiting for input…</div>';
      document.getElementById('debounceLog').innerHTML = '<div class="log-entry">Waiting for input…</div>';
    }
  </script>
</body>
</html>
```

---

## CODEPEN 5 — URL Slug Generator

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>URL Slug Generator</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }
    .container { max-width: 680px; margin: 0 auto; }

    .input-card { background: #fff; border-radius: 12px; padding: 1.25rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); margin-bottom: 1.25rem; }
    label { display: block; font-size: 0.82rem; font-weight: 700; color: #555; margin-bottom: 0.4rem; }
    input[type="text"] {
      width: 100%; padding: 0.6rem 0.9rem; border: 2px solid #e5e7eb;
      border-radius: 8px; font-size: 1rem; outline: none; transition: border-color 0.2s;
    }
    input[type="text"]:focus { border-color: #4f46e5; }

    .pipeline { background: #fff; border-radius: 12px; padding: 1.25rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); margin-bottom: 1.25rem; }
    .pipeline h2 { font-size: 0.9rem; color: #555; margin-bottom: 1rem; }

    .step { display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 0.75rem; }
    .step-num {
      width: 28px; height: 28px; border-radius: 50%; background: #e0e7ff; color: #4f46e5;
      font-size: 0.78rem; font-weight: 800; flex-shrink: 0;
      display: flex; align-items: center; justify-content: center;
    }
    .step-body { flex: 1; }
    .step-method { font-family: monospace; font-size: 0.78rem; color: #4f46e5; margin-bottom: 0.2rem; font-weight: 600; }
    .step-result {
      background: #f8f9ff; border: 1px solid #e8eaf6; border-radius: 6px;
      padding: 0.35rem 0.6rem; font-size: 0.85rem; font-family: monospace;
      color: #374151; word-break: break-all;
    }
    .arrow { text-align: center; color: #aaa; font-size: 0.9rem; margin-bottom: 0.5rem; }

    .final-card {
      background: #4f46e5; border-radius: 12px; padding: 1.25rem;
      box-shadow: 0 4px 20px rgba(79,70,229,0.25); margin-bottom: 1.25rem;
    }
    .final-label { font-size: 0.75rem; color: rgba(255,255,255,0.7); margin-bottom: 0.4rem; }
    .final-slug { font-size: 1.2rem; font-family: monospace; font-weight: 700; color: #fff; word-break: break-all; margin-bottom: 0.75rem; }
    .copy-btn {
      padding: 0.4rem 1rem; background: rgba(255,255,255,0.2); color: #fff;
      border: 1px solid rgba(255,255,255,0.4); border-radius: 8px;
      font-size: 0.83rem; cursor: pointer; font-weight: 600; transition: background 0.15s;
    }
    .copy-btn:hover { background: rgba(255,255,255,0.35); }

    .code-card { background: #1e1e2e; border-radius: 12px; padding: 1.1rem 1.25rem; }
    .code-label { font-size: 0.72rem; color: #666; font-family: monospace; margin-bottom: 0.5rem; }
    .code-block { font-size: 0.82rem; color: #a9dc76; font-family: monospace; white-space: pre-wrap; line-height: 1.6; }
  </style>
</head>
<body>
  <h1>URL Slug Generator</h1>
  <p class="subtitle">Watch string methods chain together to transform text into a URL slug.</p>

  <div class="container">
    <div class="input-card">
      <label>Article Title</label>
      <input type="text" id="titleInput" value="  Hello, World! This is a JavaScript Tutorial.  " oninput="generateSlug()">
    </div>

    <div class="pipeline">
      <h2>Step-by-step transformation</h2>
      <div class="step">
        <div class="step-num">0</div>
        <div class="step-body">
          <div class="step-method">Original string</div>
          <div class="step-result" id="step0"></div>
        </div>
      </div>
      <div class="arrow">↓</div>
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-body">
          <div class="step-method">.trim()</div>
          <div class="step-result" id="step1"></div>
        </div>
      </div>
      <div class="arrow">↓</div>
      <div class="step">
        <div class="step-num">2</div>
        <div class="step-body">
          <div class="step-method">.toLowerCase()</div>
          <div class="step-result" id="step2"></div>
        </div>
      </div>
      <div class="arrow">↓</div>
      <div class="step">
        <div class="step-num">3</div>
        <div class="step-body">
          <div class="step-method">.replaceAll(' ', '-')</div>
          <div class="step-result" id="step3"></div>
        </div>
      </div>
      <div class="arrow">↓</div>
      <div class="step">
        <div class="step-num">4</div>
        <div class="step-body">
          <div class="step-method">.replace(/[^a-z0-9-]/g, '')</div>
          <div class="step-result" id="step4"></div>
        </div>
      </div>
    </div>

    <div class="final-card">
      <div class="final-label">Final URL slug</div>
      <div class="final-slug" id="finalSlug"></div>
      <button class="copy-btn" id="copyBtn" onclick="copySlug()">Copy Slug</button>
    </div>

    <div class="code-card">
      <div class="code-label">// The complete one-liner</div>
      <div class="code-block">const slug = title
  .trim()
  .toLowerCase()
  .replaceAll(' ', '-')
  .replace(/[^a-z0-9-]/g, '');</div>
    </div>
  </div>

  <script>
    function generateSlug() {
      const raw = document.getElementById('titleInput').value;
      const s1 = raw.trim();
      const s2 = s1.toLowerCase();
      const s3 = s2.replaceAll(' ', '-');
      const s4 = s3.replace(/[^a-z0-9-]/g, '');

      document.getElementById('step0').textContent = raw   || '(empty)';
      document.getElementById('step1').textContent = s1   || '(empty)';
      document.getElementById('step2').textContent = s2   || '(empty)';
      document.getElementById('step3').textContent = s3   || '(empty)';
      document.getElementById('step4').textContent = s4   || '(empty)';
      document.getElementById('finalSlug').textContent = s4 || '(no slug)';
    }

    function copySlug() {
      const slug = document.getElementById('finalSlug').textContent;
      navigator.clipboard.writeText(slug).then(() => {
        const btn = document.getElementById('copyBtn');
        btn.textContent = '✓ Copied!';
        setTimeout(() => { btn.textContent = 'Copy Slug'; }, 2000);
      });
    }

    generateSlug();
  </script>
</body>
</html>
```
