# Day 24 CodePens — Forms That Remember

## CodePen 1: Form Values Inspector

All five common input types in one form. On submit, reads every value and displays it with labels. Shows `.value`, `.checked`, radio `:checked`, and `Number()` conversion.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Form Values Inspector</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: system-ui, sans-serif;
    background: #0f0f1a;
    color: #e8e8f0;
    min-height: 100vh;
    padding: 2rem;
    display: flex;
    gap: 2rem;
    align-items: flex-start;
  }

  h2 {
    font-size: 1.1rem;
    color: #a78bfa;
    margin-bottom: 1.25rem;
    text-transform: uppercase;
    letter-spacing: .06em;
  }

  .panel {
    background: #1a1a2e;
    border: 1px solid #2e2e4a;
    border-radius: 12px;
    padding: 1.5rem;
    flex: 1;
    min-width: 260px;
  }

  .form-group {
    margin-bottom: 1rem;
  }

  label {
    display: block;
    font-size: .85rem;
    color: #a0a0c0;
    margin-bottom: .3rem;
  }

  input[type="text"],
  input[type="email"],
  input[type="number"],
  select,
  textarea {
    width: 100%;
    padding: .55rem .75rem;
    background: #12122a;
    border: 1px solid #2e2e4a;
    border-radius: 8px;
    color: #e8e8f0;
    font-size: .9rem;
    outline: none;
  }

  input[type="text"]:focus,
  input[type="email"]:focus,
  input[type="number"]:focus,
  select:focus {
    border-color: #a78bfa;
  }

  .radio-group {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .radio-group label {
    display: flex;
    align-items: center;
    gap: .4rem;
    color: #e8e8f0;
    cursor: pointer;
  }

  .checkbox-label {
    display: flex;
    align-items: center;
    gap: .5rem;
    cursor: pointer;
    color: #e8e8f0;
  }

  input[type="range"] {
    width: 100%;
    accent-color: #a78bfa;
  }

  .range-value {
    font-size: .85rem;
    color: #a78bfa;
    margin-top: .2rem;
  }

  button {
    width: 100%;
    padding: .7rem;
    background: #a78bfa;
    color: #0f0f1a;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    font-size: .95rem;
    cursor: pointer;
    margin-top: .5rem;
    transition: background .2s;
  }

  button:hover { background: #c4b5fd; }

  .result-list {
    list-style: none;
  }

  .result-list li {
    display: flex;
    justify-content: space-between;
    padding: .5rem 0;
    border-bottom: 1px solid #2e2e4a;
    font-size: .9rem;
    gap: .5rem;
  }

  .result-list li:last-child { border-bottom: none; }

  .result-list .key {
    color: #a0a0c0;
    font-size: .8rem;
    text-transform: uppercase;
    letter-spacing: .05em;
    white-space: nowrap;
  }

  .result-list .val {
    color: #a78bfa;
    font-weight: 600;
    text-align: right;
  }

  .empty-state {
    color: #4a4a6a;
    font-size: .9rem;
    text-align: center;
    padding: 2rem 0;
  }
</style>
</head>
<body>

<div class="panel">
  <h2>The Form</h2>
  <form id="inspectorForm">

    <div class="form-group">
      <label for="nameInput">Name (text)</label>
      <input type="text" id="nameInput" value="Maria">
    </div>

    <div class="form-group">
      <label for="emailInput">Email (email)</label>
      <input type="email" id="emailInput" value="maria@example.com">
    </div>

    <div class="form-group">
      <label for="ageInput">Age (number)</label>
      <input type="number" id="ageInput" value="28" min="1" max="120">
    </div>

    <div class="form-group">
      <label for="countrySelect">Country (select)</label>
      <select id="countrySelect">
        <option value="us">United States</option>
        <option value="uk">United Kingdom</option>
        <option value="ca">Canada</option>
        <option value="au">Australia</option>
      </select>
    </div>

    <div class="form-group">
      <label>Shirt Size (radio)</label>
      <div class="radio-group">
        <label><input type="radio" name="size" value="S"> S</label>
        <label><input type="radio" name="size" value="M" checked> M</label>
        <label><input type="radio" name="size" value="L"> L</label>
        <label><input type="radio" name="size" value="XL"> XL</label>
      </div>
    </div>

    <div class="form-group">
      <label class="checkbox-label">
        <input type="checkbox" id="agreeCheck" checked>
        Agree to terms (checkbox)
      </label>
    </div>

    <div class="form-group">
      <label for="volumeRange">Volume (range)</label>
      <input type="range" id="volumeRange" min="0" max="100" value="70">
      <div class="range-value" id="rangeDisplay">70</div>
    </div>

    <button type="submit">Read All Values</button>
  </form>
</div>

<div class="panel">
  <h2>Values Read by JavaScript</h2>
  <ul class="result-list" id="results">
    <li><span class="empty-state" style="width:100%;">Submit the form to see the values</span></li>
  </ul>
</div>

<script>
  // Live range display
  const volumeRange   = document.querySelector('#volumeRange');
  const rangeDisplay  = document.querySelector('#rangeDisplay');
  volumeRange.addEventListener('input', function() {
    rangeDisplay.textContent = volumeRange.value;
  });

  document.querySelector('#inspectorForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Read each input type differently
    const name    = document.querySelector('#nameInput').value;
    const email   = document.querySelector('#emailInput').value;
    const age     = Number(document.querySelector('#ageInput').value);   // string → number
    const country = document.querySelector('#countrySelect').value;
    const size    = document.querySelector('input[name="size"]:checked').value;  // radio
    const agreed  = document.querySelector('#agreeCheck').checked;       // boolean
    const volume  = Number(document.querySelector('#volumeRange').value); // string → number

    // Display the results
    const results = document.querySelector('#results');
    results.innerHTML = `
      <li><span class="key">name</span>    <span class="val">"${name}"</span></li>
      <li><span class="key">email</span>   <span class="val">"${email}"</span></li>
      <li><span class="key">age</span>     <span class="val">${age} (${typeof age})</span></li>
      <li><span class="key">country</span> <span class="val">"${country}"</span></li>
      <li><span class="key">size</span>    <span class="val">"${size}"</span></li>
      <li><span class="key">agreed</span>  <span class="val">${agreed} (${typeof agreed})</span></li>
      <li><span class="key">volume</span>  <span class="val">${volume} (${typeof volume})</span></li>
    `;
  });
</script>
</body>
</html>
```

---

## CodePen 2: Validation with Error Messages

A signup form with name, email, password, confirm password, and a terms checkbox. Each field has its own error message that slides in when the check fails and disappears when it passes.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Validation with Error Messages</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: system-ui, sans-serif;
    background: #0d1117;
    color: #e6edf3;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
  }

  .card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 16px;
    padding: 2rem;
    width: 100%;
    max-width: 420px;
  }

  h2 {
    font-size: 1.3rem;
    margin-bottom: .4rem;
  }

  .subtitle {
    font-size: .875rem;
    color: #8b949e;
    margin-bottom: 1.75rem;
  }

  .form-group {
    margin-bottom: 1rem;
  }

  label {
    display: block;
    font-size: .85rem;
    color: #8b949e;
    margin-bottom: .35rem;
  }

  input[type="text"],
  input[type="email"],
  input[type="password"] {
    width: 100%;
    padding: .6rem .85rem;
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 8px;
    color: #e6edf3;
    font-size: .9rem;
    outline: none;
    transition: border-color .2s;
  }

  input:focus { border-color: #58a6ff; }

  input.invalid { border-color: #f85149; }
  input.valid   { border-color: #3fb950; }

  .error-msg {
    color: #f85149;
    font-size: .8rem;
    max-height: 0;
    overflow: hidden;
    transition: max-height .25s ease, margin-top .25s ease;
    margin-top: 0;
  }

  .error-msg.visible {
    max-height: 30px;
    margin-top: .3rem;
  }

  .checkbox-row {
    display: flex;
    align-items: flex-start;
    gap: .6rem;
    margin-bottom: 1.25rem;
  }

  .checkbox-row input { margin-top: 3px; accent-color: #58a6ff; }

  .checkbox-row label {
    font-size: .85rem;
    color: #8b949e;
    cursor: pointer;
  }

  button {
    width: 100%;
    padding: .7rem;
    background: #238636;
    color: #fff;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    font-size: .95rem;
    cursor: pointer;
    transition: background .2s;
  }

  button:hover { background: #2ea043; }

  .success-banner {
    display: none;
    background: #1f3a29;
    border: 1px solid #3fb950;
    color: #3fb950;
    border-radius: 8px;
    padding: .85rem 1rem;
    font-size: .9rem;
    margin-top: 1rem;
    text-align: center;
  }

  .success-banner.visible { display: block; }
</style>
</head>
<body>

<div class="card">
  <h2>Create Account</h2>
  <p class="subtitle">All fields are required.</p>

  <form id="signupForm" novalidate>

    <div class="form-group">
      <label for="name">Full Name</label>
      <input type="text" id="name" placeholder="Maria Garcia">
      <span class="error-msg" id="nameError"></span>
    </div>

    <div class="form-group">
      <label for="email">Email</label>
      <input type="email" id="email" placeholder="maria@example.com">
      <span class="error-msg" id="emailError"></span>
    </div>

    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" id="password" placeholder="At least 8 characters">
      <span class="error-msg" id="passwordError"></span>
    </div>

    <div class="form-group">
      <label for="confirm">Confirm Password</label>
      <input type="password" id="confirm" placeholder="Repeat your password">
      <span class="error-msg" id="confirmError"></span>
    </div>

    <div class="checkbox-row">
      <input type="checkbox" id="terms">
      <label for="terms">I agree to the Terms of Service and Privacy Policy</label>
    </div>
    <span class="error-msg" id="termsError" style="display:block; margin-top:-.75rem; margin-bottom:.75rem;"></span>

    <button type="submit">Create Account</button>
  </form>

  <div class="success-banner" id="successBanner">
    Account created successfully! Welcome aboard.
  </div>
</div>

<script>
  const nameInput  = document.querySelector('#name');
  const emailInput = document.querySelector('#email');
  const pwInput    = document.querySelector('#password');
  const cfInput    = document.querySelector('#confirm');
  const termsCheck = document.querySelector('#terms');

  const nameError  = document.querySelector('#nameError');
  const emailError = document.querySelector('#emailError');
  const pwError    = document.querySelector('#passwordError');
  const cfError    = document.querySelector('#confirmError');
  const termsError = document.querySelector('#termsError');

  function showError(errorEl, inputEl, message) {
    errorEl.textContent = message;
    errorEl.classList.add('visible');
    inputEl.classList.add('invalid');
    inputEl.classList.remove('valid');
  }

  function clearError(errorEl, inputEl) {
    errorEl.textContent = '';
    errorEl.classList.remove('visible');
    inputEl.classList.remove('invalid');
    inputEl.classList.add('valid');
  }

  document.querySelector('#signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let isValid = true;

    // Clear all errors first
    [nameInput, emailInput, pwInput, cfInput].forEach(function(el) {
      el.classList.remove('invalid', 'valid');
    });
    [nameError, emailError, pwError, cfError, termsError].forEach(function(el) {
      el.textContent = '';
      el.classList.remove('visible');
    });

    // Name: must not be empty
    if (nameInput.value.trim() === '') {
      showError(nameError, nameInput, 'Full name is required');
      isValid = false;
    } else {
      clearError(nameError, nameInput);
    }

    // Email: must contain @ and a dot after it
    if (!emailInput.value.includes('@') || !emailInput.value.includes('.')) {
      showError(emailError, emailInput, 'Enter a valid email address');
      isValid = false;
    } else {
      clearError(emailError, emailInput);
    }

    // Password: must be at least 8 characters
    if (pwInput.value.length < 8) {
      showError(pwError, pwInput, 'Password must be at least 8 characters');
      isValid = false;
    } else {
      clearError(pwError, pwInput);
    }

    // Confirm: must match password
    if (cfInput.value !== pwInput.value) {
      showError(cfError, cfInput, 'Passwords do not match');
      isValid = false;
    } else if (cfInput.value.length >= 8) {
      clearError(cfError, cfInput);
    }

    // Terms: must be checked
    if (!termsCheck.checked) {
      termsError.textContent = 'You must agree to the Terms of Service';
      termsError.classList.add('visible');
      isValid = false;
    }

    if (isValid) {
      document.querySelector('#signupForm').style.display = 'none';
      document.querySelector('#successBanner').classList.add('visible');
    }
  });
</script>
</body>
</html>
```

---

## CodePen 3: localStorage Key-Value Demo

A stripped-down interactive demo: type a value, save it, reload and load it back, then clear it. Every operation shows a timestamp log. DevTools hint guides students to the Application tab.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>localStorage Demo</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: system-ui, sans-serif;
    background: #1a1a2e;
    color: #e8e8f0;
    min-height: 100vh;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
  }

  h2 {
    font-size: 1.2rem;
    color: #ffeaa7;
    text-align: center;
  }

  .hint {
    font-size: .8rem;
    color: #74b9ff;
    text-align: center;
    background: #1e2d42;
    border: 1px solid #2e4a6a;
    border-radius: 8px;
    padding: .6rem 1rem;
    max-width: 520px;
  }

  .controls {
    display: flex;
    gap: .75rem;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 520px;
    width: 100%;
  }

  input[type="text"] {
    flex: 1;
    min-width: 180px;
    padding: .6rem .85rem;
    background: #12122a;
    border: 1px solid #2e2e4a;
    border-radius: 8px;
    color: #e8e8f0;
    font-size: .9rem;
    outline: none;
  }

  input[type="text"]:focus { border-color: #a78bfa; }

  button {
    padding: .6rem 1.1rem;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    font-size: .85rem;
    cursor: pointer;
    transition: opacity .2s;
  }

  button:hover { opacity: .85; }

  .btn-save  { background: #a78bfa; color: #0f0f1a; }
  .btn-load  { background: #74b9ff; color: #0f0f1a; }
  .btn-clear { background: #fd79a8; color: #0f0f1a; }

  .display-box {
    background: #12122a;
    border: 1px solid #2e2e4a;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    max-width: 520px;
    width: 100%;
    min-height: 60px;
  }

  .display-box .label {
    font-size: .75rem;
    color: #6060a0;
    text-transform: uppercase;
    letter-spacing: .06em;
    margin-bottom: .4rem;
  }

  .display-box .value {
    font-size: 1.1rem;
    color: #a78bfa;
    font-weight: 600;
    word-break: break-all;
  }

  .display-box .value.null-val { color: #4a4a6a; font-style: italic; }

  .log {
    background: #0a0a18;
    border: 1px solid #2e2e4a;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    max-width: 520px;
    width: 100%;
    font-family: monospace;
    font-size: .8rem;
    min-height: 120px;
    max-height: 200px;
    overflow-y: auto;
  }

  .log .log-line { padding: .2rem 0; border-bottom: 1px solid #1a1a2e; color: #a0a0c0; }
  .log .log-line:last-child { border-bottom: none; }
  .log .log-line .action { color: #ffeaa7; margin-right: .5rem; }
  .log .log-line .data   { color: #a78bfa; }
</style>
</head>
<body>

<h2>localStorage: Save, Load, Clear</h2>

<p class="hint">
  Open DevTools &rarr; <strong>Application</strong> tab &rarr; <strong>Local Storage</strong> to watch changes happen in real time.
</p>

<div class="controls">
  <input type="text" id="valueInput" placeholder="Type something to save...">
  <button class="btn-save"  id="saveBtn">setItem()</button>
  <button class="btn-load"  id="loadBtn">getItem()</button>
  <button class="btn-clear" id="clearBtn">removeItem()</button>
</div>

<div class="display-box" id="displayBox">
  <div class="label">Current value in localStorage</div>
  <div class="value null-val" id="displayValue">— not loaded yet —</div>
</div>

<div class="log" id="logPanel">
  <div class="log-line"><span class="action">// Activity log</span></div>
</div>

<script>
  const KEY = 'demo_value';

  function addLog(action, data) {
    const log  = document.querySelector('#logPanel');
    const time = new Date().toLocaleTimeString();
    const line = document.createElement('div');
    line.className = 'log-line';
    line.innerHTML = `<span class="action">[${time}] ${action}</span><span class="data">${data}</span>`;
    log.appendChild(line);
    log.scrollTop = log.scrollHeight;
  }

  function updateDisplay(value) {
    const el = document.querySelector('#displayValue');
    if (value === null) {
      el.textContent = 'null — key does not exist';
      el.classList.add('null-val');
    } else {
      el.textContent = '"' + value + '"';
      el.classList.remove('null-val');
    }
  }

  // SAVE — localStorage.setItem(key, value)
  document.querySelector('#saveBtn').addEventListener('click', function() {
    const val = document.querySelector('#valueInput').value;
    if (val === '') {
      addLog('setItem() skipped:', 'input is empty');
      return;
    }
    localStorage.setItem(KEY, val);
    updateDisplay(val);
    addLog('localStorage.setItem("demo_value", ', '"' + val + '")');
  });

  // LOAD — localStorage.getItem(key)
  document.querySelector('#loadBtn').addEventListener('click', function() {
    const val = localStorage.getItem(KEY);
    updateDisplay(val);
    if (val === null) {
      addLog('localStorage.getItem("demo_value")', '→ null (key not found)');
    } else {
      addLog('localStorage.getItem("demo_value")', '→ "' + val + '"');
    }
  });

  // CLEAR — localStorage.removeItem(key)
  document.querySelector('#clearBtn').addEventListener('click', function() {
    localStorage.removeItem(KEY);
    updateDisplay(null);
    addLog('localStorage.removeItem("demo_value")', '→ key deleted');
  });

  // Check on load if a value is already stored
  const existing = localStorage.getItem(KEY);
  if (existing !== null) {
    updateDisplay(existing);
    addLog('Page loaded — found existing value:', '"' + existing + '"');
  } else {
    addLog('Page loaded — no saved value found', '(key does not exist yet)');
  }
</script>
</body>
</html>
```

---

## CodePen 4: Persistent To-Do List

Add tasks to a list. Each entry saves to localStorage. A delete button removes individual items. Refresh the page — all tasks are still there.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Persistent To-Do List</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: system-ui, sans-serif;
    background: #0f172a;
    color: #e2e8f0;
    min-height: 100vh;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
  }

  h2 {
    font-size: 1.4rem;
    color: #38bdf8;
  }

  .subtitle {
    font-size: .85rem;
    color: #64748b;
    text-align: center;
    margin-top: -.75rem;
  }

  .add-row {
    display: flex;
    gap: .75rem;
    width: 100%;
    max-width: 480px;
  }

  input[type="text"] {
    flex: 1;
    padding: .65rem .9rem;
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 10px;
    color: #e2e8f0;
    font-size: .95rem;
    outline: none;
    transition: border-color .2s;
  }

  input[type="text"]:focus { border-color: #38bdf8; }

  .btn-add {
    padding: .65rem 1.2rem;
    background: #38bdf8;
    color: #0f172a;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    font-size: .9rem;
    cursor: pointer;
    white-space: nowrap;
    transition: background .2s;
  }

  .btn-add:hover { background: #7dd3fc; }

  .task-list {
    list-style: none;
    width: 100%;
    max-width: 480px;
    display: flex;
    flex-direction: column;
    gap: .6rem;
  }

  .task-item {
    display: flex;
    align-items: center;
    gap: .75rem;
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: .7rem 1rem;
    animation: slideIn .2s ease;
  }

  @keyframes slideIn {
    from { opacity: 0; transform: translateY(-6px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .task-item input[type="checkbox"] {
    width: 18px;
    height: 18px;
    accent-color: #38bdf8;
    cursor: pointer;
    flex-shrink: 0;
  }

  .task-text {
    flex: 1;
    font-size: .95rem;
    line-height: 1.4;
    transition: color .2s;
  }

  .task-item.done .task-text {
    text-decoration: line-through;
    color: #475569;
  }

  .btn-delete {
    background: none;
    border: none;
    color: #475569;
    font-size: 1.1rem;
    cursor: pointer;
    padding: .1rem .3rem;
    border-radius: 4px;
    transition: color .2s;
    flex-shrink: 0;
  }

  .btn-delete:hover { color: #f87171; }

  .empty-state {
    color: #334155;
    font-size: .9rem;
    text-align: center;
    padding: 2rem;
    border: 1px dashed #334155;
    border-radius: 10px;
    width: 100%;
    max-width: 480px;
  }

  .footer-row {
    display: flex;
    gap: 1rem;
    align-items: center;
    font-size: .8rem;
    color: #475569;
    width: 100%;
    max-width: 480px;
  }

  .btn-clear-all {
    background: none;
    border: 1px solid #334155;
    color: #64748b;
    border-radius: 6px;
    padding: .3rem .7rem;
    font-size: .8rem;
    cursor: pointer;
    margin-left: auto;
    transition: border-color .2s, color .2s;
  }

  .btn-clear-all:hover { border-color: #f87171; color: #f87171; }
</style>
</head>
<body>

<h2>To-Do List</h2>
<p class="subtitle">Refreshes and survives. Try it.</p>

<div class="add-row">
  <input type="text" id="taskInput" placeholder="Add a new task...">
  <button class="btn-add" id="addBtn">Add Task</button>
</div>

<ul class="task-list" id="taskList"></ul>

<div class="footer-row">
  <span id="countLabel"></span>
  <button class="btn-clear-all" id="clearAllBtn">Clear All</button>
</div>

<script>
  // Load from localStorage on startup
  let tasks = [];
  try {
    tasks = JSON.parse(localStorage.getItem('todo_tasks')) || [];
  } catch {
    tasks = [];
  }

  function save() {
    localStorage.setItem('todo_tasks', JSON.stringify(tasks));
  }

  function render() {
    const list = document.querySelector('#taskList');

    if (tasks.length === 0) {
      list.innerHTML = '<li class="empty-state">No tasks yet. Add one above.</li>';
      document.querySelector('#countLabel').textContent = '';
      return;
    }

    list.innerHTML = tasks.map(function(task, index) {
      return `
        <li class="task-item ${task.done ? 'done' : ''}" data-index="${index}">
          <input type="checkbox" ${task.done ? 'checked' : ''} data-action="toggle">
          <span class="task-text">${task.text}</span>
          <button class="btn-delete" data-action="delete" title="Delete task">&#10005;</button>
        </li>
      `;
    }).join('');

    const remaining = tasks.filter(function(t) { return !t.done; }).length;
    document.querySelector('#countLabel').textContent =
      remaining + ' task' + (remaining === 1 ? '' : 's') + ' remaining';
  }

  // Add a new task
  function addTask() {
    const input = document.querySelector('#taskInput');
    const text  = input.value.trim();
    if (text === '') return;

    tasks.push({ text: text, done: false });
    save();
    render();
    input.value = '';
    input.focus();
  }

  document.querySelector('#addBtn').addEventListener('click', addTask);

  document.querySelector('#taskInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') addTask();
  });

  // Event delegation for toggle and delete
  document.querySelector('#taskList').addEventListener('click', function(event) {
    const item   = event.target.closest('[data-index]');
    const action = event.target.dataset.action;
    if (!item || !action) return;

    const index = Number(item.dataset.index);

    if (action === 'toggle') {
      tasks[index].done = !tasks[index].done;
    } else if (action === 'delete') {
      tasks.splice(index, 1);
    }

    save();
    render();
  });

  // Clear all tasks
  document.querySelector('#clearAllBtn').addEventListener('click', function() {
    tasks = [];
    save();
    render();
  });

  // Initial render
  render();
</script>
</body>
</html>
```

---

## CodePen 5: Full Registration Form

A complete example: validation on submit with animated error messages, object creation on success, localStorage persistence, and a card grid displaying all saved entries. Refresh — the entries survive.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Registration Form with localStorage</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: system-ui, sans-serif;
    background: #111827;
    color: #f9fafb;
    min-height: 100vh;
    padding: 2rem;
  }

  .layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    max-width: 900px;
    margin: 0 auto;
  }

  @media (max-width: 640px) { .layout { grid-template-columns: 1fr; } }

  h2 {
    font-size: 1.1rem;
    color: #6ee7b7;
    margin-bottom: 1.25rem;
    text-transform: uppercase;
    letter-spacing: .07em;
  }

  .panel {
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 14px;
    padding: 1.75rem;
  }

  .form-group {
    margin-bottom: .9rem;
  }

  label {
    display: block;
    font-size: .8rem;
    color: #9ca3af;
    margin-bottom: .3rem;
    text-transform: uppercase;
    letter-spacing: .04em;
  }

  input[type="text"],
  input[type="email"],
  select {
    width: 100%;
    padding: .6rem .85rem;
    background: #111827;
    border: 1px solid #374151;
    border-radius: 8px;
    color: #f9fafb;
    font-size: .9rem;
    outline: none;
    transition: border-color .2s;
  }

  input:focus, select:focus { border-color: #6ee7b7; }
  input.field-error { border-color: #f87171; }

  .error-msg {
    color: #f87171;
    font-size: .78rem;
    max-height: 0;
    overflow: hidden;
    transition: max-height .2s ease;
  }

  .error-msg.visible {
    max-height: 24px;
    margin-top: .2rem;
  }

  .btn-submit {
    width: 100%;
    padding: .7rem;
    background: #6ee7b7;
    color: #111827;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    font-size: .95rem;
    cursor: pointer;
    margin-top: .5rem;
    transition: background .2s;
  }

  .btn-submit:hover { background: #a7f3d0; }

  .entries-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.25rem;
  }

  .entries-header h2 { margin-bottom: 0; }

  .btn-clear {
    background: none;
    border: 1px solid #374151;
    color: #6b7280;
    border-radius: 6px;
    padding: .25rem .65rem;
    font-size: .78rem;
    cursor: pointer;
    transition: border-color .2s, color .2s;
  }

  .btn-clear:hover { border-color: #f87171; color: #f87171; }

  .entry-grid {
    display: flex;
    flex-direction: column;
    gap: .65rem;
    max-height: 420px;
    overflow-y: auto;
  }

  .entry-card {
    background: #111827;
    border: 1px solid #374151;
    border-radius: 10px;
    padding: .85rem 1rem;
    animation: fadeUp .2s ease;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .entry-name  { font-weight: 700; color: #f9fafb; font-size: .95rem; }
  .entry-email { font-size: .8rem; color: #6ee7b7; margin-top: .15rem; }
  .entry-meta  { font-size: .75rem; color: #4b5563; margin-top: .3rem; }

  .empty-state {
    color: #374151;
    font-size: .9rem;
    text-align: center;
    padding: 2.5rem 1rem;
    border: 1px dashed #374151;
    border-radius: 10px;
  }

  .toast {
    position: fixed;
    bottom: 1.5rem;
    right: 1.5rem;
    background: #6ee7b7;
    color: #111827;
    padding: .65rem 1.1rem;
    border-radius: 8px;
    font-weight: 700;
    font-size: .85rem;
    transform: translateY(80px);
    opacity: 0;
    transition: transform .3s ease, opacity .3s ease;
    pointer-events: none;
  }

  .toast.visible {
    transform: translateY(0);
    opacity: 1;
  }
</style>
</head>
<body>

<div class="layout">

  <div class="panel">
    <h2>New Registration</h2>
    <form id="regForm" novalidate>

      <div class="form-group">
        <label for="regName">Full Name</label>
        <input type="text" id="regName" placeholder="Maria Garcia">
        <span class="error-msg" id="regNameError"></span>
      </div>

      <div class="form-group">
        <label for="regEmail">Email</label>
        <input type="email" id="regEmail" placeholder="maria@example.com">
        <span class="error-msg" id="regEmailError"></span>
      </div>

      <div class="form-group">
        <label for="regRole">Role</label>
        <select id="regRole">
          <option value="">Select a role...</option>
          <option value="Designer">Designer</option>
          <option value="Developer">Developer</option>
          <option value="Product Manager">Product Manager</option>
          <option value="Marketing">Marketing</option>
          <option value="Other">Other</option>
        </select>
        <span class="error-msg" id="regRoleError"></span>
      </div>

      <button class="btn-submit" type="submit">Save Registration</button>
    </form>
  </div>

  <div class="panel">
    <div class="entries-header">
      <h2>Saved Entries</h2>
      <button class="btn-clear" id="clearAllBtn">Clear All</button>
    </div>
    <div class="entry-grid" id="entryGrid"></div>
  </div>

</div>

<div class="toast" id="toast">Registration saved!</div>

<script>
  const STORAGE_KEY = 'registrations';

  // Load from localStorage on startup
  let entries = [];
  try {
    entries = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
  } catch {
    entries = [];
  }

  // --- Validation helpers ---

  function showError(errorEl, inputEl, message) {
    errorEl.textContent = message;
    errorEl.classList.add('visible');
    inputEl.classList.add('field-error');
  }

  function clearError(errorEl, inputEl) {
    errorEl.textContent = '';
    errorEl.classList.remove('visible');
    inputEl.classList.remove('field-error');
  }

  // --- Render entries ---

  function renderEntries() {
    const grid = document.querySelector('#entryGrid');

    if (entries.length === 0) {
      grid.innerHTML = '<div class="empty-state">No registrations yet.<br>Fill out the form to add one.</div>';
      return;
    }

    // Show newest first
    grid.innerHTML = [...entries].reverse().map(function(e) {
      return `
        <div class="entry-card">
          <div class="entry-name">${e.name}</div>
          <div class="entry-email">${e.email}</div>
          <div class="entry-meta">${e.role} &middot; ${e.date}</div>
        </div>
      `;
    }).join('');
  }

  // --- Toast notification ---

  function showToast(message) {
    const toast = document.querySelector('#toast');
    toast.textContent = message;
    toast.classList.add('visible');
    setTimeout(function() {
      toast.classList.remove('visible');
    }, 2500);
  }

  // --- Form submit ---

  document.querySelector('#regForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const nameInput  = document.querySelector('#regName');
    const emailInput = document.querySelector('#regEmail');
    const roleSelect = document.querySelector('#regRole');

    const nameError  = document.querySelector('#regNameError');
    const emailError = document.querySelector('#regEmailError');
    const roleError  = document.querySelector('#regRoleError');

    let isValid = true;

    clearError(nameError,  nameInput);
    clearError(emailError, emailInput);
    clearError(roleError,  roleSelect);

    if (nameInput.value.trim() === '') {
      showError(nameError, nameInput, 'Full name is required');
      isValid = false;
    }

    if (!emailInput.value.includes('@') || !emailInput.value.includes('.')) {
      showError(emailError, emailInput, 'Enter a valid email address');
      isValid = false;
    }

    if (roleSelect.value === '') {
      showError(roleError, roleSelect, 'Please select a role');
      isValid = false;
    }

    if (!isValid) return;

    // Build entry object from form values
    const entry = {
      name:  nameInput.value.trim(),
      email: emailInput.value.trim(),
      role:  roleSelect.value,
      date:  new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
    };

    // Save to array and localStorage
    entries.push(entry);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(entries));

    renderEntries();
    showToast('Registration saved!');

    // Reset the form
    event.target.reset();
    nameInput.focus();
  });

  // --- Clear all ---

  document.querySelector('#clearAllBtn').addEventListener('click', function() {
    entries = [];
    localStorage.removeItem(STORAGE_KEY);
    renderEntries();
  });

  // Initial render
  renderEntries();
</script>
</body>
</html>
```
