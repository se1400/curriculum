# Day 25 — Objects & JSON — CodePens

---

## CODEPEN 1 — Object-to-Card Renderer

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Object-to-Card Renderer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }

    .layout {
      display: grid; grid-template-columns: 1fr 1fr;
      gap: 1.5rem; max-width: 850px; margin: 0 auto;
      align-items: start;
    }
    @media (max-width: 640px) { .layout { grid-template-columns: 1fr; } }

    .form-panel { background: #fff; border-radius: 12px; padding: 1.25rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
    .form-panel h2 { font-size: 0.95rem; color: #555; margin-bottom: 1rem; }
    .field { margin-bottom: 0.85rem; }
    label { display: block; font-size: 0.78rem; font-weight: 600; color: #555; margin-bottom: 0.3rem; }
    input[type="text"] {
      width: 100%; padding: 0.5rem 0.75rem; border: 2px solid #e5e7eb;
      border-radius: 8px; font-size: 0.9rem; outline: none; transition: border-color 0.2s;
    }
    input[type="text"]:focus { border-color: #4f46e5; }

    .card-panel { display: flex; flex-direction: column; gap: 1rem; }
    .profile-card {
      background: #fff; border-radius: 12px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.08);
      padding: 1.5rem; text-align: center;
    }
    .avatar {
      width: 72px; height: 72px; border-radius: 50%;
      background: linear-gradient(135deg, #4f46e5, #7c3aed);
      display: flex; align-items: center; justify-content: center;
      margin: 0 auto 1rem; font-size: 1.5rem; font-weight: 700; color: #fff;
    }
    .card-name { font-size: 1.15rem; font-weight: 700; color: #1a1a2e; }
    .card-role { font-size: 0.88rem; color: #4f46e5; font-weight: 600; margin-top: 0.2rem; }
    .card-company { font-size: 0.83rem; color: #888; margin-top: 0.15rem; }
    .card-details { margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #f0f0f0; text-align: left; }
    .card-detail { display: flex; align-items: center; gap: 0.5rem; font-size: 0.82rem; color: #555; margin-bottom: 0.4rem; }
    .card-detail span.icon { font-size: 1rem; }

    .json-panel {
      background: #1e1e2e; border-radius: 10px;
      padding: 0.9rem 1rem;
    }
    .json-label { font-size: 0.7rem; color: #666; margin-bottom: 0.4rem; font-family: monospace; }
    .json-code { font-size: 0.78rem; color: #a9dc76; font-family: monospace; white-space: pre-wrap; line-height: 1.5; }
  </style>
</head>
<body>
  <h1>Object → Card Renderer</h1>
  <p class="subtitle">Type in the form — the card and object update live.</p>

  <div class="layout">
    <div class="form-panel">
      <h2>Edit the object</h2>
      <div class="field"><label>Name</label><input type="text" id="f-name"    value="Alex Rivera" oninput="update()"></div>
      <div class="field"><label>Role</label><input type="text" id="f-role"    value="Front-End Developer" oninput="update()"></div>
      <div class="field"><label>Company</label><input type="text" id="f-company" value="Acme Corp" oninput="update()"></div>
      <div class="field"><label>Email</label><input type="text" id="f-email"  value="alex@acme.com" oninput="update()"></div>
      <div class="field"><label>Location</label><input type="text" id="f-loc"  value="Portland, OR" oninput="update()"></div>
    </div>

    <div class="card-panel">
      <div class="profile-card">
        <div class="avatar" id="avatar">AR</div>
        <div class="card-name"    id="card-name">Alex Rivera</div>
        <div class="card-role"    id="card-role">Front-End Developer</div>
        <div class="card-company" id="card-company">Acme Corp</div>
        <div class="card-details">
          <div class="card-detail"><span class="icon">✉</span><span id="card-email">alex@acme.com</span></div>
          <div class="card-detail"><span class="icon">📍</span><span id="card-loc">Portland, OR</span></div>
        </div>
      </div>

      <div class="json-panel">
        <div class="json-label">// The object (JSON.stringify)</div>
        <div class="json-code" id="jsonDisplay"></div>
      </div>
    </div>
  </div>

  <script>
    function update() {
      const person = {
        name:     document.getElementById('f-name').value    || 'Your Name',
        role:     document.getElementById('f-role').value    || '',
        company:  document.getElementById('f-company').value || '',
        email:    document.getElementById('f-email').value   || '',
        location: document.getElementById('f-loc').value     || '',
      };

      const initials = person.name.trim().split(/\s+/).map(w => w[0] || '').join('').toUpperCase().slice(0, 2);

      document.getElementById('avatar').textContent    = initials || '?';
      document.getElementById('card-name').textContent    = person.name;
      document.getElementById('card-role').textContent    = person.role;
      document.getElementById('card-company').textContent = person.company;
      document.getElementById('card-email').textContent   = person.email;
      document.getElementById('card-loc').textContent     = person.location;
      document.getElementById('jsonDisplay').textContent  = JSON.stringify(person, null, 2);
    }

    update();
  </script>
</body>
</html>
```

---

## CODEPEN 2 — Array of Objects → Card Grid

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Array of Objects → Card Grid</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1rem; }
    .toggle-btn {
      display: block; margin: 0 auto 1.5rem;
      padding: 0.45rem 1.25rem; border: 2px solid #4f46e5;
      background: #fff; color: #4f46e5; border-radius: 20px;
      font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: all 0.2s;
    }
    .toggle-btn:hover, .toggle-btn.on { background: #4f46e5; color: #fff; }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem; max-width: 900px; margin: 0 auto 1.5rem;
    }
    .card {
      background: #fff; border-radius: 12px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.08); padding: 1.1rem;
      transition: transform 0.2s;
    }
    .card:hover { transform: translateY(-3px); }
    .card-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.6rem; }
    .card-name { font-weight: 700; font-size: 0.95rem; color: #1a1a2e; }
    .badge {
      padding: 0.2rem 0.55rem; border-radius: 20px;
      font-size: 0.7rem; font-weight: 700; white-space: nowrap;
    }
    .badge-tech    { background: #dbeafe; color: #1d4ed8; }
    .badge-audio   { background: #dcfce7; color: #166534; }
    .badge-office  { background: #fef3c7; color: #92400e; }
    .badge-home    { background: #fce7f3; color: #9d174d; }
    .card-price { font-size: 1.2rem; font-weight: 800; color: #4f46e5; margin-bottom: 0.4rem; }
    .stars { color: #f59e0b; font-size: 0.9rem; margin-bottom: 0.4rem; }
    .stock { font-size: 0.78rem; font-weight: 600; }
    .in-stock { color: #16a34a; } .out-of-stock { color: #dc2626; }

    .json-box {
      display: none; max-width: 900px; margin: 0 auto;
      background: #1e1e2e; border-radius: 12px; padding: 1rem 1.25rem;
    }
    .json-box.visible { display: block; }
    .json-label { font-size: 0.72rem; color: #666; font-family: monospace; margin-bottom: 0.4rem; }
    .json-code { font-size: 0.77rem; color: #a9dc76; font-family: monospace; white-space: pre-wrap; line-height: 1.5; }
  </style>
</head>
<body>
  <h1>Array of Objects → Card Grid</h1>
  <p class="subtitle">Each object in the array becomes a card on screen.</p>
  <button class="toggle-btn" id="toggleBtn" onclick="toggleJSON()">Show Source Data (JSON)</button>

  <div class="grid" id="grid"></div>
  <div class="json-box" id="jsonBox">
    <div class="json-label">// The products array</div>
    <div class="json-code" id="jsonCode"></div>
  </div>

  <script>
    const products = [
      { id: 1, name: 'Wireless Headphones', price: 79.99,  category: 'audio',  rating: 4, inStock: true  },
      { id: 2, name: 'USB-C Hub',           price: 34.99,  category: 'tech',   rating: 5, inStock: true  },
      { id: 3, name: 'Notebook Set',        price: 12.99,  category: 'office', rating: 4, inStock: true  },
      { id: 4, name: 'Smart Bulb Pack',     price: 24.99,  category: 'home',   rating: 3, inStock: false },
      { id: 5, name: 'Mechanical Keyboard', price: 129.99, category: 'tech',   rating: 5, inStock: true  },
      { id: 6, name: 'Desk Organiser',      price: 19.99,  category: 'office', rating: 4, inStock: true  },
      { id: 7, name: 'Portable Speaker',    price: 49.99,  category: 'audio',  rating: 4, inStock: false },
      { id: 8, name: 'LED Desk Lamp',       price: 39.99,  category: 'home',   rating: 3, inStock: true  },
    ];

    function stars(n) { return '★'.repeat(n) + '☆'.repeat(5 - n); }

    document.getElementById('grid').innerHTML = products.map(p => `
      <div class="card">
        <div class="card-header">
          <div class="card-name">${p.name}</div>
          <span class="badge badge-${p.category}">${p.category}</span>
        </div>
        <div class="card-price">$${p.price.toFixed(2)}</div>
        <div class="stars">${stars(p.rating)}</div>
        <div class="stock ${p.inStock ? 'in-stock' : 'out-of-stock'}">
          ${p.inStock ? '✓ In Stock' : '✗ Out of Stock'}
        </div>
      </div>
    `).join('');

    document.getElementById('jsonCode').textContent = JSON.stringify(products, null, 2);

    function toggleJSON() {
      const box = document.getElementById('jsonBox');
      const btn = document.getElementById('toggleBtn');
      box.classList.toggle('visible');
      btn.classList.toggle('on');
      btn.textContent = box.classList.contains('visible') ? 'Hide Source Data' : 'Show Source Data (JSON)';
    }
  </script>
</body>
</html>
```

---

## CODEPEN 3 — Object.entries() Settings Panel

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Object.entries() Settings Panel</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }

    .container { max-width: 700px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.25rem; }

    .settings-panel { background: #fff; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); overflow: hidden; }
    .panel-header { padding: 0.9rem 1.25rem; background: #4f46e5; color: #fff; font-weight: 700; font-size: 0.95rem; }
    .setting-row {
      display: flex; align-items: center; justify-content: space-between;
      padding: 0.75rem 1.25rem; border-bottom: 1px solid #f3f4f6;
    }
    .setting-row:last-child { border-bottom: none; }
    .setting-key { font-size: 0.88rem; font-weight: 600; color: #374151; text-transform: capitalize; }
    .setting-input { display: flex; align-items: center; gap: 0.5rem; }
    input[type="text"].s-input {
      padding: 0.35rem 0.6rem; border: 1px solid #d1d5db;
      border-radius: 6px; font-size: 0.85rem; width: 160px; outline: none;
      transition: border-color 0.2s;
    }
    input[type="text"].s-input:focus { border-color: #4f46e5; }
    select.s-select {
      padding: 0.35rem 0.6rem; border: 1px solid #d1d5db;
      border-radius: 6px; font-size: 0.85rem; background: #fff; outline: none;
    }
    .toggle-wrap { display: flex; align-items: center; gap: 0.5rem; }
    .toggle {
      width: 40px; height: 22px; background: #d1d5db; border-radius: 11px;
      position: relative; cursor: pointer; transition: background 0.2s; border: none;
    }
    .toggle.on { background: #4f46e5; }
    .toggle::after {
      content: ''; position: absolute; top: 3px; left: 3px;
      width: 16px; height: 16px; background: #fff; border-radius: 50%;
      transition: transform 0.2s;
    }
    .toggle.on::after { transform: translateX(18px); }

    .json-panel { background: #1e1e2e; border-radius: 12px; padding: 1rem 1.25rem; }
    .json-label { font-size: 0.72rem; color: #666; font-family: monospace; margin-bottom: 0.5rem; }
    .json-code { font-size: 0.8rem; color: #a9dc76; font-family: monospace; white-space: pre-wrap; line-height: 1.6; }
  </style>
</head>
<body>
  <h1>Object.entries() Settings Panel</h1>
  <p class="subtitle">Built with <code>Object.entries()</code> — each key-value pair becomes a settings row.</p>

  <div class="container">
    <div class="settings-panel">
      <div class="panel-header">⚙ Application Settings</div>
      <div id="settingsRows"></div>
    </div>

    <div class="json-panel">
      <div class="json-label">// Current settings object (updates as you change values)</div>
      <div class="json-code" id="jsonOutput"></div>
    </div>
  </div>

  <script>
    let settings = {
      theme:         'light',
      fontSize:      '16px',
      language:      'English',
      notifications: true,
      autoSave:      true,
      timezone:      'UTC-7',
      displayName:   'Alex',
      colorScheme:   'blue',
    };

    const selectOptions = {
      theme:       ['light', 'dark', 'auto'],
      language:    ['English', 'Spanish', 'French', 'German'],
      colorScheme: ['blue', 'green', 'purple', 'red'],
      timezone:    ['UTC-8', 'UTC-7', 'UTC-6', 'UTC-5', 'UTC+0', 'UTC+1'],
    };

    function buildRows() {
      const container = document.getElementById('settingsRows');
      container.innerHTML = Object.entries(settings).map(([key, value]) => {
        const label = key.replace(/([A-Z])/g, ' $1');
        let input = '';
        if (typeof value === 'boolean') {
          input = `
            <div class="toggle-wrap">
              <button class="toggle ${value ? 'on' : ''}" id="toggle-${key}" onclick="toggleBool('${key}')"></button>
              <span id="bool-${key}" style="font-size:0.82rem;color:${value ? '#4f46e5' : '#9ca3af'}">${value ? 'On' : 'Off'}</span>
            </div>`;
        } else if (selectOptions[key]) {
          input = `<select class="s-select" onchange="updateSetting('${key}', this.value)">
            ${selectOptions[key].map(opt => `<option ${opt === value ? 'selected' : ''}>${opt}</option>`).join('')}
          </select>`;
        } else {
          input = `<input type="text" class="s-input" value="${value}" oninput="updateSetting('${key}', this.value)">`;
        }
        return `<div class="setting-row"><span class="setting-key">${label}</span><div class="setting-input">${input}</div></div>`;
      }).join('');
      updateJSON();
    }

    function updateSetting(key, value) {
      settings[key] = value;
      updateJSON();
    }

    function toggleBool(key) {
      settings[key] = !settings[key];
      const btn = document.getElementById('toggle-' + key);
      const lbl = document.getElementById('bool-' + key);
      btn.classList.toggle('on', settings[key]);
      lbl.textContent = settings[key] ? 'On' : 'Off';
      lbl.style.color = settings[key] ? '#4f46e5' : '#9ca3af';
      updateJSON();
    }

    function updateJSON() {
      document.getElementById('jsonOutput').textContent = JSON.stringify(settings, null, 2);
    }

    buildRows();
  </script>
</body>
</html>
```

---

## CODEPEN 4 — Destructuring Lab

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Destructuring Lab</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }

    .container { max-width: 820px; margin: 0 auto; display: flex; flex-direction: column; gap: 1rem; }

    .section { background: #fff; border-radius: 12px; padding: 1.25rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
    .section h2 { font-size: 0.95rem; margin-bottom: 0.25rem; color: #1a1a2e; }
    .sec-sub { font-size: 0.78rem; color: #888; margin-bottom: 0.9rem; }

    .code-display {
      background: #1e1e2e; color: #a9dc76; font-family: monospace;
      font-size: 0.82rem; border-radius: 8px; padding: 0.7rem 1rem;
      margin-bottom: 0.75rem; white-space: pre;
    }
    .chips-row { display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center; margin-bottom: 0.6rem; }
    .chip {
      padding: 0.3rem 0.7rem; border-radius: 20px; font-size: 0.8rem;
      font-weight: 600; font-family: monospace;
    }
    .chip-source { background: #e5e7eb; color: #374151; }
    .chip-dest   { background: #dbeafe; color: #1d4ed8; }
    .chip-rename { background: #fce7f3; color: #9d174d; }
    .chip-default{ background: #dcfce7; color: #166534; }
    .chip-missing{ background: #fef3c7; color: #92400e; text-decoration: line-through; opacity: 0.7; }
    .arrow { color: #aaa; }

    .toggle-row { display: flex; gap: 0.5rem; margin-bottom: 0.75rem; flex-wrap: wrap; }
    .tbtn {
      padding: 0.3rem 0.7rem; border: 1px solid #d1d5db; border-radius: 6px;
      background: #fff; font-size: 0.78rem; cursor: pointer; transition: all 0.15s;
    }
    .tbtn.on { background: #4f46e5; color: #fff; border-color: #4f46e5; }

    .result-row { display: flex; flex-wrap: wrap; gap: 0.6rem; }
    .result-item {
      background: #f8f9ff; border: 1px solid #e8eaf6; border-radius: 8px;
      padding: 0.4rem 0.75rem; font-size: 0.82rem; font-family: monospace;
    }
    .result-item .rk { color: #6366f1; font-weight: 700; }
    .result-item .rv { color: #374151; }
  </style>
</head>
<body>
  <h1>Destructuring Lab</h1>
  <p class="subtitle">Object and array destructuring — visually, with renaming and defaults.</p>

  <div class="container">

    <!-- OBJECT DESTRUCTURING -->
    <div class="section">
      <h2>Object Destructuring</h2>
      <p class="sec-sub">user = { firstName: 'Jordan', lastName: 'Lee', email: 'jordan@example.com', role: 'admin', age: 29 }</p>

      <div class="toggle-row">
        <button class="tbtn on" id="tb-rename" onclick="toggleObj('rename')">Rename</button>
        <button class="tbtn"    id="tb-default" onclick="toggleObj('default')">Default value</button>
      </div>

      <div class="code-display" id="objCode"></div>
      <div class="chips-row" id="objChips"></div>
      <div class="result-row" id="objResult"></div>
    </div>

    <!-- ARRAY DESTRUCTURING -->
    <div class="section">
      <h2>Array Destructuring</h2>
      <p class="sec-sub">colors = ['red', 'green', 'blue', 'yellow', 'purple']</p>

      <div class="toggle-row">
        <button class="tbtn on" id="tb-rest" onclick="toggleArr('rest')">...rest</button>
        <button class="tbtn"    id="tb-skip" onclick="toggleArr('skip')">Skip element</button>
      </div>

      <div class="code-display" id="arrCode"></div>
      <div class="chips-row" id="arrChips"></div>
      <div class="result-row" id="arrResult"></div>
    </div>

  </div>

  <script>
    const user   = { firstName: 'Jordan', lastName: 'Lee', email: 'jordan@example.com', role: 'admin', age: 29 };
    const colors = ['red', 'green', 'blue', 'yellow', 'purple'];

    let objToggles = { rename: true, default: false };
    let arrToggles = { rest: true, skip: false };

    function toggleObj(f) {
      objToggles[f] = !objToggles[f];
      document.getElementById('tb-' + f).classList.toggle('on', objToggles[f]);
      renderObj();
    }
    function toggleArr(f) {
      arrToggles[f] = !arrToggles[f];
      document.getElementById('tb-' + f).classList.toggle('on', arrToggles[f]);
      renderArr();
    }

    function renderObj() {
      const { rename, default: def } = objToggles;
      let pattern, results;
      if (rename && def) {
        pattern = `const { firstName: name, role: userRole, nickname = 'No nickname' } = user`;
        results = [
          { k: 'name',     v: `"${user.firstName}"`, cls: 'chip-rename' },
          { k: 'userRole', v: `"${user.role}"`,       cls: 'chip-rename' },
          { k: 'nickname', v: '"No nickname"',         cls: 'chip-default' },
        ];
      } else if (rename) {
        pattern = `const { firstName: name, role: userRole } = user`;
        results = [
          { k: 'name',     v: `"${user.firstName}"`, cls: 'chip-rename' },
          { k: 'userRole', v: `"${user.role}"`,       cls: 'chip-rename' },
        ];
      } else if (def) {
        pattern = `const { firstName, email, nickname = 'No nickname' } = user`;
        results = [
          { k: 'firstName', v: `"${user.firstName}"`, cls: 'chip-dest' },
          { k: 'email',     v: `"${user.email}"`,      cls: 'chip-dest' },
          { k: 'nickname',  v: '"No nickname"',         cls: 'chip-default' },
        ];
      } else {
        pattern = `const { firstName, role, email } = user`;
        results = [
          { k: 'firstName', v: `"${user.firstName}"`, cls: 'chip-dest' },
          { k: 'role',      v: `"${user.role}"`,       cls: 'chip-dest' },
          { k: 'email',     v: `"${user.email}"`,      cls: 'chip-dest' },
        ];
      }
      document.getElementById('objCode').textContent = pattern;
      document.getElementById('objChips').innerHTML = results.map(r =>
        `<span class="chip ${r.cls}">${r.k} = ${r.v}</span>`
      ).join('<span class="arrow">  </span>');
      document.getElementById('objResult').innerHTML = results.map(r =>
        `<div class="result-item"><span class="rk">${r.k}</span> = <span class="rv">${r.v}</span></div>`
      ).join('');
    }

    function renderArr() {
      const { rest, skip } = arrToggles;
      let pattern, items;
      if (skip && rest) {
        pattern = `const [first, , third, ...rest] = colors`;
        items = [
          { v: '"red"',    var: 'first' },
          { v: '"green"',  var: null,   skip: true },
          { v: '"blue"',   var: 'third' },
          { v: '...',      var: 'rest → ["yellow","purple"]', rest: true },
        ];
      } else if (skip) {
        pattern = `const [first, , third] = colors`;
        items = [
          { v: '"red"',   var: 'first' },
          { v: '"green"', var: null, skip: true },
          { v: '"blue"',  var: 'third' },
        ];
      } else if (rest) {
        pattern = `const [first, second, ...rest] = colors`;
        items = [
          { v: '"red"',   var: 'first' },
          { v: '"green"', var: 'second' },
          { v: '...',     var: 'rest → ["blue","yellow","purple"]', rest: true },
        ];
      } else {
        pattern = `const [first, second] = colors`;
        items = [
          { v: '"red"',   var: 'first' },
          { v: '"green"', var: 'second' },
        ];
      }
      document.getElementById('arrCode').textContent = pattern;
      document.getElementById('arrChips').innerHTML = items.map(item => {
        if (item.skip) return `<span class="chip chip-missing">${item.v} (skipped)</span>`;
        if (item.rest) return `<span class="chip chip-default">${item.var}</span>`;
        return `<span class="chip chip-source">${item.v}</span><span class="arrow"> → </span><span class="chip chip-dest">${item.var}</span>`;
      }).join('<span style="color:#ddd;padding:0 0.2rem">  </span>');
      document.getElementById('arrResult').innerHTML = items.filter(i => !i.skip).map(i =>
        `<div class="result-item"><span class="rk">${i.var.split(' →')[0]}</span> = <span class="rv">${i.rest ? '["blue","yellow","purple"]' : i.v}</span></div>`
      ).join('');
    }

    renderObj();
    renderArr();
  </script>
</body>
</html>
```

---

## CODEPEN 5 — structuredClone() Deep Copy Demo

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>structuredClone() Deep Copy Demo</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }

    .panels { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; max-width: 1000px; margin: 0 auto; }
    @media (max-width: 700px) { .panels { grid-template-columns: 1fr; } }

    .panel { background: #fff; border-radius: 12px; padding: 1.1rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
    .panel-a { border-top: 4px solid #ef4444; }
    .panel-b { border-top: 4px solid #f59e0b; }
    .panel-c { border-top: 4px solid #22c55e; }

    .panel-title { font-weight: 700; font-size: 0.95rem; margin-bottom: 0.2rem; }
    .panel-a .panel-title { color: #ef4444; }
    .panel-b .panel-title { color: #f59e0b; }
    .panel-c .panel-title { color: #22c55e; }
    .panel-code { font-family: monospace; font-size: 0.75rem; color: #888; margin-bottom: 0.9rem; background: #f8f9ff; border-radius: 6px; padding: 0.4rem 0.6rem; }

    .obj-displays { display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 0.75rem; }
    .obj-display { border-radius: 8px; padding: 0.5rem 0.7rem; font-size: 0.75rem; font-family: monospace; white-space: pre-wrap; line-height: 1.4; }
    .obj-label { font-size: 0.68rem; font-weight: 700; margin-bottom: 0.2rem; }
    .original-display { background: #f8f9ff; border: 1px solid #e8eaf6; }
    .copy-display     { background: #f0fdf4; border: 1px solid #bbf7d0; }
    .copy-display.tainted { background: #fef2f2; border-color: #fecaca; }

    .btns { display: flex; flex-direction: column; gap: 0.4rem; }
    .action-btn {
      padding: 0.45rem 0.7rem; border: none; border-radius: 8px;
      font-size: 0.78rem; font-weight: 600; cursor: pointer; text-align: left; transition: opacity 0.15s;
    }
    .action-btn:hover { opacity: 0.85; }
    .btn-name { background: #dbeafe; color: #1e40af; }
    .btn-city { background: #fce7f3; color: #9d174d; }

    .status { font-size: 0.75rem; margin-top: 0.6rem; padding: 0.35rem 0.6rem; border-radius: 6px; }
    .status-red    { background: #fef2f2; color: #dc2626; border: 1px solid #fecaca; }
    .status-yellow { background: #fffbeb; color: #92400e; border: 1px solid #fde68a; }
    .status-green  { background: #f0fdf4; color: #16a34a; border: 1px solid #bbf7d0; }

    .reset-btn {
      display: block; margin: 1.25rem auto 0;
      padding: 0.5rem 1.5rem; background: #6b7280;
      color: #fff; border: none; border-radius: 8px;
      font-size: 0.88rem; cursor: pointer; font-weight: 600;
    }
  </style>
</head>
<body>
  <h1>Copy Strategies: Reference vs Shallow vs Deep</h1>
  <p class="subtitle">Explore how each copy method handles nested objects differently.</p>

  <div class="panels">
    <!-- PANEL A: Reference -->
    <div class="panel panel-a">
      <div class="panel-title">⚠ Reference</div>
      <div class="panel-code">const copy = original</div>
      <div class="obj-displays">
        <div><div class="obj-label" style="color:#ef4444">original</div><div class="obj-display original-display" id="a-orig"></div></div>
        <div><div class="obj-label" style="color:#555">copy (= original)</div><div class="obj-display copy-display" id="a-copy"></div></div>
      </div>
      <div class="btns">
        <button class="action-btn btn-name" onclick="doA('name')">Change copy.name → "Bobby"</button>
        <button class="action-btn btn-city" onclick="doA('city')">Change copy.address.city → "Miami"</button>
      </div>
      <div class="status status-red" id="a-status">Both point to the same object in memory.</div>
    </div>

    <!-- PANEL B: Shallow -->
    <div class="panel panel-b">
      <div class="panel-title">⚡ Shallow Copy</div>
      <div class="panel-code">const copy = { ...original }</div>
      <div class="obj-displays">
        <div><div class="obj-label" style="color:#92400e">original</div><div class="obj-display original-display" id="b-orig"></div></div>
        <div><div class="obj-label" style="color:#555">copy (spread)</div><div class="obj-display copy-display" id="b-copy"></div></div>
      </div>
      <div class="btns">
        <button class="action-btn btn-name" onclick="doB('name')">Change copy.name → "Bobby"</button>
        <button class="action-btn btn-city" onclick="doB('city')">Change copy.address.city → "Miami"</button>
      </div>
      <div class="status status-yellow" id="b-status">Top-level: independent ✓  Nested: still shared ✗</div>
    </div>

    <!-- PANEL C: Deep -->
    <div class="panel panel-c">
      <div class="panel-title">✓ Deep Copy</div>
      <div class="panel-code">const copy = structuredClone(original)</div>
      <div class="obj-displays">
        <div><div class="obj-label" style="color:#166534">original</div><div class="obj-display original-display" id="c-orig"></div></div>
        <div><div class="obj-label" style="color:#555">copy (structuredClone)</div><div class="obj-display copy-display" id="c-copy"></div></div>
      </div>
      <div class="btns">
        <button class="action-btn btn-name" onclick="doC('name')">Change copy.name → "Bobby"</button>
        <button class="action-btn btn-city" onclick="doC('city')">Change copy.address.city → "Miami"</button>
      </div>
      <div class="status status-green" id="c-status">Fully independent — original is always safe. ✓</div>
    </div>
  </div>

  <button class="reset-btn" onclick="init()">↺ Reset All</button>

  <script>
    let aOrig, aCopy, bOrig, bCopy, cOrig, cCopy;

    function fmt(obj) { return JSON.stringify(obj, null, 2); }

    function refresh() {
      document.getElementById('a-orig').textContent = fmt(aOrig);
      document.getElementById('a-copy').textContent = fmt(aCopy);
      document.getElementById('b-orig').textContent = fmt(bOrig);
      document.getElementById('b-copy').textContent = fmt(bCopy);
      document.getElementById('c-orig').textContent = fmt(cOrig);
      document.getElementById('c-copy').textContent = fmt(cCopy);
    }

    function doA(field) {
      if (field === 'name') aCopy.name = 'Bobby';
      else aCopy.address.city = 'Miami';
      document.getElementById('a-copy').classList.add('tainted');
      document.getElementById('a-status').textContent = '⚠ original also changed — they are the SAME object!';
      refresh();
    }

    function doB(field) {
      const statusEl = document.getElementById('b-status');
      const copyEl   = document.getElementById('b-copy');
      if (field === 'name') {
        bCopy.name = 'Bobby';
        statusEl.textContent = '✓ copy.name changed — original.name is safe (top-level independent)';
        copyEl.classList.remove('tainted');
      } else {
        bCopy.address.city = 'Miami';
        statusEl.textContent = '⚠ original.address.city also changed — nested objects are still shared!';
        copyEl.classList.add('tainted');
      }
      refresh();
    }

    function doC(field) {
      if (field === 'name') cCopy.name = 'Bobby';
      else cCopy.address.city = 'Miami';
      document.getElementById('c-status').textContent = '✓ original is completely untouched — structuredClone works!';
      document.getElementById('c-copy').classList.remove('tainted');
      refresh();
    }

    function init() {
      const base = { name: 'Alice', age: 30, address: { city: 'Portland', zip: '97201' } };
      aOrig = { ...base, address: { ...base.address } };
      aCopy = aOrig;
      bOrig = { ...base, address: { ...base.address } };
      bCopy = { ...bOrig };
      cOrig = { ...base, address: { ...base.address } };
      cCopy = structuredClone(cOrig);

      document.getElementById('a-copy').classList.remove('tainted');
      document.getElementById('b-copy').classList.remove('tainted');
      document.getElementById('c-copy').classList.remove('tainted');
      document.getElementById('a-status').textContent = 'Both point to the same object in memory.';
      document.getElementById('b-status').textContent = 'Top-level: independent ✓  Nested: still shared ✗';
      document.getElementById('c-status').textContent = 'Fully independent — original is always safe. ✓';
      refresh();
    }

    init();
  </script>
</body>
</html>
```
