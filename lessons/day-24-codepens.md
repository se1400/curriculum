# Day 24 — Arrays: Core Methods — CodePens

---

## CODEPEN 1 — Interactive To-Do List

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Array To-Do List</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: system-ui, sans-serif;
      background: #f0f2f5;
      min-height: 100vh;
      display: flex;
      align-items: flex-start;
      justify-content: center;
      padding: 2rem 1rem;
    }
    .card {
      background: #fff;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.1);
      padding: 1.5rem;
      width: 100%;
      max-width: 500px;
    }
    h1 { font-size: 1.4rem; margin-bottom: 0.25rem; color: #1a1a2e; }
    .subtitle { font-size: 0.85rem; color: #666; margin-bottom: 1.25rem; }
    .input-row {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }
    input[type="text"] {
      flex: 1;
      padding: 0.6rem 0.9rem;
      border: 2px solid #e0e0e0;
      border-radius: 8px;
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.2s;
    }
    input[type="text"]:focus { border-color: #4f46e5; }
    .btn {
      padding: 0.6rem 1rem;
      border: none;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: opacity 0.15s, transform 0.1s;
    }
    .btn:active { transform: scale(0.97); }
    .btn-add   { background: #4f46e5; color: #fff; }
    .btn-pop   { background: #f59e0b; color: #fff; }
    .btn-shift { background: #10b981; color: #fff; }
    .btn-group {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }
    .count {
      font-size: 0.85rem;
      color: #888;
      margin-bottom: 0.5rem;
    }
    ul { list-style: none; }
    .task-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.65rem 0.8rem;
      border-radius: 8px;
      margin-bottom: 0.4rem;
      background: #f8f9ff;
      border: 1px solid #e8eaf6;
      transition: background 0.15s;
    }
    .task-item:hover { background: #eef0ff; }
    .task-text { font-size: 0.95rem; color: #333; }
    .task-meta { font-size: 0.75rem; color: #999; margin-left: 0.5rem; }
    .btn-remove {
      background: none;
      border: none;
      color: #dc2626;
      font-size: 1.1rem;
      cursor: pointer;
      padding: 0.1rem 0.4rem;
      border-radius: 4px;
      transition: background 0.15s;
    }
    .btn-remove:hover { background: #fee2e2; }
    .empty { text-align: center; color: #bbb; padding: 1.5rem 0; font-style: italic; }
    .state-panel {
      margin-top: 1.25rem;
      background: #1e1e2e;
      border-radius: 8px;
      padding: 0.9rem 1rem;
    }
    .state-label { font-size: 0.75rem; color: #888; margin-bottom: 0.4rem; font-family: monospace; }
    .state-code { font-size: 0.8rem; color: #a9dc76; font-family: monospace; white-space: pre-wrap; word-break: break-all; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Array To-Do List</h1>
    <p class="subtitle">The array is the single source of truth — every button mutates it, then re-renders.</p>

    <div class="input-row">
      <input type="text" id="taskInput" placeholder="Add a task…">
      <button class="btn btn-add" onclick="addTask()">Add (push)</button>
    </div>

    <div class="btn-group">
      <button class="btn btn-pop"   onclick="removeLast()">Remove Last (pop)</button>
      <button class="btn btn-shift" onclick="removeFirst()">Remove First (shift)</button>
    </div>

    <p class="count" id="count">0 items</p>
    <ul id="taskList"></ul>

    <div class="state-panel">
      <div class="state-label">// Current array state</div>
      <div class="state-code" id="stateDisplay">[]</div>
    </div>
  </div>

  <script>
    const tasks = [];

    function renderList() {
      const list = document.getElementById('taskList');
      const count = document.getElementById('count');
      const stateDisplay = document.getElementById('stateDisplay');

      count.textContent = tasks.length === 1 ? '1 item' : `${tasks.length} items`;
      stateDisplay.textContent = JSON.stringify(tasks, null, 2);

      if (tasks.length === 0) {
        list.innerHTML = '<p class="empty">No tasks yet — type one above!</p>';
        return;
      }

      list.innerHTML = tasks.map((task, index) => `
        <li class="task-item">
          <span>
            <span class="task-text">${task}</span>
            <span class="task-meta">[${index}]</span>
          </span>
          <button class="btn-remove" onclick="removeAt(${index})" title="Remove">×</button>
        </li>
      `).join('');
    }

    function addTask() {
      const input = document.getElementById('taskInput');
      const value = input.value.trim();
      if (!value) return;
      tasks.push(value);   // ← push()
      input.value = '';
      input.focus();
      renderList();
    }

    function removeLast() {
      if (tasks.length === 0) return;
      tasks.pop();          // ← pop()
      renderList();
    }

    function removeFirst() {
      if (tasks.length === 0) return;
      tasks.shift();        // ← shift()
      renderList();
    }

    function removeAt(index) {
      tasks.splice(index, 1); // ← splice()
      renderList();
    }

    document.getElementById('taskInput').addEventListener('keydown', e => {
      if (e.key === 'Enter') addTask();
    });

    renderList();
  </script>
</body>
</html>
```

---

## CODEPEN 2 — Product Sort Demo

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Array Sort Demo</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.4rem; color: #1a1a2e; margin-bottom: 0.25rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.25rem; }
    .controls {
      display: flex; flex-wrap: wrap; gap: 0.5rem;
      justify-content: center; margin-bottom: 0.75rem;
    }
    .btn {
      padding: 0.5rem 1rem; border: 2px solid #4f46e5;
      border-radius: 20px; background: #fff;
      color: #4f46e5; font-size: 0.85rem; font-weight: 600;
      cursor: pointer; transition: all 0.2s;
    }
    .btn:hover { background: #eef; }
    .btn.active { background: #4f46e5; color: #fff; }
    .sort-mode {
      text-align: center; font-size: 0.8rem; color: #888;
      margin-bottom: 1rem; min-height: 1.2em;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 1rem; max-width: 900px; margin: 0 auto;
    }
    .card {
      background: #fff; border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.08);
      padding: 1rem; transition: transform 0.2s;
    }
    .card:hover { transform: translateY(-3px); }
    .card-name { font-weight: 700; font-size: 0.95rem; color: #1a1a2e; margin-bottom: 0.4rem; }
    .card-price { font-size: 1.15rem; color: #4f46e5; font-weight: 700; margin-bottom: 0.4rem; }
    .badge {
      display: inline-block; padding: 0.2rem 0.6rem;
      border-radius: 20px; font-size: 0.72rem; font-weight: 600;
    }
    .badge-tech    { background: #dbeafe; color: #1d4ed8; }
    .badge-audio   { background: #dcfce7; color: #166534; }
    .badge-office  { background: #fef3c7; color: #92400e; }
    .badge-home    { background: #fce7f3; color: #9d174d; }
  </style>
</head>
<body>
  <h1>Array Sort Demo</h1>
  <p class="subtitle">Uses <code>toSorted()</code> — the original array is never mutated.</p>

  <div class="controls">
    <button class="btn active" onclick="sortBy('original')">Original Order</button>
    <button class="btn" onclick="sortBy('name-az')">Name A→Z</button>
    <button class="btn" onclick="sortBy('name-za')">Name Z→A</button>
    <button class="btn" onclick="sortBy('price-asc')">Price Low→High</button>
    <button class="btn" onclick="sortBy('price-desc')">Price High→Low</button>
  </div>
  <p class="sort-mode" id="sortMode">Showing original order</p>

  <div class="grid" id="grid"></div>

  <script>
    const products = [
      { name: 'Wireless Headphones', price: 79.99,  category: 'audio'  },
      { name: 'USB-C Hub',           price: 34.99,  category: 'tech'   },
      { name: 'Notebook',            price: 12.99,  category: 'office' },
      { name: 'Smart Bulb Pack',     price: 24.99,  category: 'home'   },
      { name: 'Mechanical Keyboard', price: 129.99, category: 'tech'   },
      { name: 'Desk Organiser',      price: 19.99,  category: 'office' },
      { name: 'Portable Speaker',    price: 49.99,  category: 'audio'  },
      { name: 'LED Desk Lamp',       price: 39.99,  category: 'home'   },
    ];

    let currentSort = 'original';

    const sortLabels = {
      'original':   'Showing original order',
      'name-az':    'Sorted by name A → Z',
      'name-za':    'Sorted by name Z → A',
      'price-asc':  'Sorted by price: low → high',
      'price-desc': 'Sorted by price: high → low',
    };

    function getSorted(mode) {
      switch (mode) {
        case 'name-az':    return products.toSorted((a, b) => a.name.localeCompare(b.name));
        case 'name-za':    return products.toSorted((a, b) => b.name.localeCompare(a.name));
        case 'price-asc':  return products.toSorted((a, b) => a.price - b.price);
        case 'price-desc': return products.toSorted((a, b) => b.price - a.price);
        default:           return [...products];
      }
    }

    function sortBy(mode) {
      currentSort = mode;
      document.querySelectorAll('.btn').forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');
      document.getElementById('sortMode').textContent = sortLabels[mode];
      render(getSorted(mode));
    }

    function render(arr) {
      document.getElementById('grid').innerHTML = arr.map(p => `
        <div class="card">
          <div class="card-name">${p.name}</div>
          <div class="card-price">$${p.price.toFixed(2)}</div>
          <span class="badge badge-${p.category}">${p.category}</span>
        </div>
      `).join('');
    }

    render(getSorted('original'));
  </script>
</body>
</html>
```

---

## CODEPEN 3 — Mutation Trap Visualizer

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mutation Trap Visualizer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.5rem; }
    .intro { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }
    .panels { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; max-width: 800px; margin: 0 auto; }
    @media (max-width: 600px) { .panels { grid-template-columns: 1fr; } }
    .panel {
      background: #fff; border-radius: 12px;
      padding: 1.25rem; box-shadow: 0 2px 12px rgba(0,0,0,0.09);
    }
    .panel-bug  { border-top: 4px solid #ef4444; }
    .panel-fix  { border-top: 4px solid #22c55e; }
    .panel-title {
      font-weight: 700; font-size: 1rem; margin-bottom: 0.3rem;
    }
    .panel-bug  .panel-title { color: #ef4444; }
    .panel-fix  .panel-title { color: #22c55e; }
    .panel-sub { font-size: 0.78rem; color: #888; margin-bottom: 1rem; }
    code {
      background: #f3f4f6; border-radius: 4px;
      padding: 0.1rem 0.4rem; font-size: 0.82rem; color: #374151;
    }
    .array-display {
      background: #f8f9ff; border: 1px solid #e8eaf6;
      border-radius: 8px; padding: 0.6rem 0.8rem;
      font-family: monospace; font-size: 0.85rem;
      margin-bottom: 0.5rem; min-height: 2.2rem;
    }
    .label { font-size: 0.78rem; color: #555; margin-bottom: 0.2rem; font-weight: 600; }
    .btn {
      display: block; width: 100%;
      padding: 0.55rem; border: none; border-radius: 8px;
      font-size: 0.88rem; font-weight: 600; cursor: pointer;
      margin-top: 0.75rem; transition: opacity 0.15s;
    }
    .btn:hover { opacity: 0.85; }
    .btn-bug { background: #fee2e2; color: #991b1b; }
    .btn-fix { background: #dcfce7; color: #166534; }
    .warning { font-size: 0.8rem; margin-top: 0.6rem; padding: 0.4rem 0.6rem; border-radius: 6px; }
    .warning-red   { background: #fef2f2; color: #dc2626; border: 1px solid #fecaca; }
    .warning-green { background: #f0fdf4; color: #16a34a; border: 1px solid #bbf7d0; }
    .reset-btn {
      display: block; margin: 1.25rem auto 0;
      padding: 0.5rem 1.5rem; background: #6b7280;
      color: #fff; border: none; border-radius: 8px;
      font-size: 0.88rem; cursor: pointer; font-weight: 600;
    }
  </style>
</head>
<body>
  <h1>The Array Mutation Trap</h1>
  <p class="intro">
    <code>const arr2 = arr1</code> copies a <em>reference</em>, not the data.
    <code>const arr2 = [...arr1]</code> creates a true independent copy.
  </p>

  <div class="panels">
    <!-- BUG PANEL -->
    <div class="panel panel-bug">
      <div class="panel-title">⚠ The Bug</div>
      <div class="panel-sub"><code>const bugArr2 = bugArr1</code></div>

      <div class="label">bugArr1</div>
      <div class="array-display" id="bugArr1Display"></div>

      <div class="label">bugArr2 <em style="font-weight:400;color:#aaa">(supposed to be separate…)</em></div>
      <div class="array-display" id="bugArr2Display"></div>

      <button class="btn btn-bug" onclick="bugAdd()">Add item to bugArr2</button>
      <div class="warning warning-red" id="bugWarning" style="display:none">
        ⚠ bugArr1 changed too — they are the same array in memory!
      </div>
    </div>

    <!-- FIX PANEL -->
    <div class="panel panel-fix">
      <div class="panel-title">✓ The Fix</div>
      <div class="panel-sub"><code>const fixArr2 = [...fixArr1]</code></div>

      <div class="label">fixArr1</div>
      <div class="array-display" id="fixArr1Display"></div>

      <div class="label">fixArr2 <em style="font-weight:400;color:#aaa">(independent copy)</em></div>
      <div class="array-display" id="fixArr2Display"></div>

      <button class="btn btn-fix" onclick="fixAdd()">Add item to fixArr2</button>
      <div class="warning warning-green" id="fixWarning" style="display:none">
        ✓ fixArr1 is untouched — spread created a real copy!
      </div>
    </div>
  </div>

  <button class="reset-btn" onclick="reset()">↺ Reset</button>

  <script>
    let bugArr1, bugArr2, fixArr1, fixArr2, bugCount, fixCount;

    function reset() {
      bugArr1 = ['Alpha', 'Beta', 'Gamma'];
      bugArr2 = bugArr1;        // ← reference (same array)
      fixArr1 = ['Alpha', 'Beta', 'Gamma'];
      fixArr2 = [...fixArr1];   // ← spread copy (new array)
      bugCount = fixCount = 0;
      document.getElementById('bugWarning').style.display = 'none';
      document.getElementById('fixWarning').style.display = 'none';
      updateDisplays();
    }

    function bugAdd() {
      bugCount++;
      bugArr2.push('Item ' + bugCount);
      document.getElementById('bugWarning').style.display = 'block';
      updateDisplays();
    }

    function fixAdd() {
      fixCount++;
      fixArr2.push('Item ' + fixCount);
      document.getElementById('fixWarning').style.display = 'block';
      updateDisplays();
    }

    function fmt(arr) { return '[' + arr.map(v => `"${v}"`).join(', ') + ']'; }

    function updateDisplays() {
      document.getElementById('bugArr1Display').textContent = fmt(bugArr1);
      document.getElementById('bugArr2Display').textContent = fmt(bugArr2);
      document.getElementById('fixArr1Display').textContent = fmt(fixArr1);
      document.getElementById('fixArr2Display').textContent = fmt(fixArr2);
    }

    reset();
  </script>
</body>
</html>
```

---

## CODEPEN 4 — at() and findLast() Explorer

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>at() and findLast() Explorer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.25rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }

    .cards-row {
      display: flex; flex-wrap: wrap; gap: 0.6rem;
      justify-content: center; margin-bottom: 1.5rem;
    }
    .card-chip {
      width: 80px; height: 80px; border-radius: 10px;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      background: #fff; border: 2px solid #e5e7eb;
      box-shadow: 0 1px 4px rgba(0,0,0,0.07);
      transition: all 0.25s; cursor: default;
    }
    .card-chip .chip-idx  { font-size: 0.65rem; color: #aaa; }
    .card-chip .chip-name { font-size: 0.78rem; font-weight: 700; color: #374151; }
    .card-chip .chip-num  { font-size: 1.1rem; font-weight: 800; color: #4f46e5; }
    .card-chip.highlight-at    { border-color: #f59e0b; background: #fffbeb; box-shadow: 0 0 0 3px #f59e0b44; }
    .card-chip.highlight-find  { border-color: #8b5cf6; background: #f5f3ff; box-shadow: 0 0 0 3px #8b5cf644; }

    .controls {
      display: grid; grid-template-columns: 1fr 1fr;
      gap: 1rem; max-width: 700px; margin: 0 auto;
    }
    @media (max-width: 500px) { .controls { grid-template-columns: 1fr; } }
    .control-box {
      background: #fff; border-radius: 10px;
      padding: 1rem; box-shadow: 0 2px 10px rgba(0,0,0,0.07);
    }
    .control-box h2 { font-size: 0.95rem; margin-bottom: 0.75rem; color: #1a1a2e; }
    .input-row { display: flex; gap: 0.5rem; margin-bottom: 0.6rem; align-items: center; }
    label { font-size: 0.8rem; color: #555; white-space: nowrap; }
    input[type="number"], input[type="text"] {
      flex: 1; padding: 0.4rem 0.6rem;
      border: 1px solid #d1d5db; border-radius: 6px; font-size: 0.88rem;
    }
    .quick-btns { display: flex; gap: 0.4rem; flex-wrap: wrap; margin-bottom: 0.6rem; }
    .qbtn {
      padding: 0.3rem 0.6rem; border: none; border-radius: 6px;
      background: #fff7ed; color: #c2410c;
      font-size: 0.75rem; font-weight: 600; cursor: pointer;
    }
    .result-box {
      background: #f8f9ff; border-radius: 6px;
      padding: 0.5rem 0.7rem; font-size: 0.82rem; color: #374151;
      font-family: monospace; min-height: 2.5rem;
    }
    .result-box code { background: none; font-size: inherit; padding: 0; }
  </style>
</head>
<body>
  <h1>at() and findLast() Explorer</h1>
  <p class="subtitle">Explore negative indexing and searching from the end of an array.</p>

  <div class="cards-row" id="cardsRow"></div>

  <div class="controls">
    <!-- at() panel -->
    <div class="control-box">
      <h2>🔢 array.at(index)</h2>
      <div class="quick-btns">
        <button class="qbtn" onclick="runAt(0)">First (0)</button>
        <button class="qbtn" onclick="runAt(-1)">Last (−1)</button>
        <button class="qbtn" onclick="runAt(-2)">2nd-to-last (−2)</button>
      </div>
      <div class="input-row">
        <label>Index:</label>
        <input type="number" id="atIndex" value="-1" min="-10" max="9">
        <button class="qbtn" onclick="runAt(+document.getElementById('atIndex').value)">Go</button>
      </div>
      <div class="result-box" id="atResult">Click a button or enter an index.</div>
    </div>

    <!-- findLast() panel -->
    <div class="control-box">
      <h2>🔍 array.findLast()</h2>
      <div class="input-row">
        <label>Name contains:</label>
        <input type="text" id="findInput" placeholder="e.g. Beta" oninput="runFind()">
      </div>
      <div class="result-box" id="findResult">Type a search term above.</div>
    </div>
  </div>

  <script>
    const items = [
      { name: 'Alpha',   num: 1  },
      { name: 'Beta',    num: 2  },
      { name: 'Gamma',   num: 3  },
      { name: 'Delta',   num: 4  },
      { name: 'Beta',    num: 5  },
      { name: 'Epsilon', num: 6  },
      { name: 'Zeta',    num: 7  },
      { name: 'Gamma',   num: 8  },
      { name: 'Eta',     num: 9  },
      { name: 'Beta',    num: 10 },
    ];

    function renderCards(highlightAt = null, highlightFind = null) {
      document.getElementById('cardsRow').innerHTML = items.map((item, i) => {
        let cls = 'card-chip';
        if (i === highlightAt)  cls += ' highlight-at';
        if (i === highlightFind) cls += ' highlight-find';
        return `
          <div class="${cls}">
            <span class="chip-idx">[${i}]</span>
            <span class="chip-num">${item.num}</span>
            <span class="chip-name">${item.name}</span>
          </div>`;
      }).join('');
    }

    function runAt(n) {
      document.getElementById('atIndex').value = n;
      const result = items.at(n);
      const realIndex = n < 0 ? items.length + n : n;
      if (!result) {
        document.getElementById('atResult').textContent = 'Index out of range — returned undefined.';
        renderCards();
        return;
      }
      document.getElementById('atResult').innerHTML =
        `<code>items.at(${n})</code> → "${result.name} ${result.num}" (index ${realIndex})`;
      renderCards(realIndex, null);
    }

    function runFind() {
      const term = document.getElementById('findInput').value.trim();
      if (!term) { document.getElementById('findResult').textContent = 'Type a search term above.'; renderCards(); return; }
      const result = items.findLast(item => item.name.toLowerCase().includes(term.toLowerCase()));
      const idx    = items.findLastIndex(item => item.name.toLowerCase().includes(term.toLowerCase()));
      if (!result) {
        document.getElementById('findResult').textContent = 'No match found.';
        renderCards();
        return;
      }
      document.getElementById('findResult').innerHTML =
        `<code>findLast()</code> → "${result.name} ${result.num}"<br>` +
        `<code>findLastIndex()</code> → index <strong>${idx}</strong>`;
      renderCards(null, idx);
    }

    renderCards();
  </script>
</body>
</html>
```

---

## CODEPEN 5 — Spread & Destructuring Lab

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Spread & Destructuring Lab</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }

    .sections { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; max-width: 850px; margin: 0 auto; }
    @media (max-width: 600px) { .sections { grid-template-columns: 1fr; } }

    .section { background: #fff; border-radius: 12px; padding: 1.25rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
    .section h2 { font-size: 1rem; margin-bottom: 0.25rem; color: #1a1a2e; }
    .section .sec-sub { font-size: 0.78rem; color: #888; margin-bottom: 1rem; }

    .op-btn {
      display: block; width: 100%; text-align: left;
      padding: 0.55rem 0.75rem; margin-bottom: 0.4rem;
      background: #f8f9ff; border: 1px solid #e8eaf6;
      border-radius: 8px; font-size: 0.83rem; cursor: pointer;
      transition: background 0.15s; color: #374151; font-family: monospace;
    }
    .op-btn:hover { background: #eef0ff; border-color: #c7d2fe; }
    .op-btn.active { background: #eef0ff; border-color: #4f46e5; color: #4338ca; font-weight: 600; }

    .result-area {
      margin-top: 0.75rem; background: #1e1e2e; border-radius: 8px;
      padding: 0.75rem 0.9rem; font-family: monospace;
      font-size: 0.82rem; color: #a9dc76; min-height: 3.5rem;
    }
    .result-label { font-size: 0.7rem; color: #666; margin-bottom: 0.3rem; }

    /* destructuring visual */
    .dest-row { display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap; margin-bottom: 0.5rem; }
    .chip {
      padding: 0.25rem 0.6rem; border-radius: 6px; font-size: 0.8rem;
      font-weight: 600; font-family: monospace;
    }
    .chip-val  { background: #dbeafe; color: #1d4ed8; }
    .chip-var  { background: #dcfce7; color: #166534; }
    .chip-rest { background: #fef3c7; color: #92400e; }
    .chip-skip { background: #f3f4f6; color: #9ca3af; text-decoration: line-through; }
    .arrow { color: #aaa; font-size: 0.9rem; }

    .toggle-row { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.75rem; }
    .toggle-btn {
      padding: 0.3rem 0.7rem; border: 1px solid #d1d5db; border-radius: 6px;
      background: #fff; font-size: 0.78rem; cursor: pointer; transition: all 0.15s;
    }
    .toggle-btn.on { background: #4f46e5; color: #fff; border-color: #4f46e5; }
  </style>
</head>
<body>
  <h1>Spread &amp; Destructuring Lab</h1>
  <p class="subtitle">Explore copying, merging, and pattern-matching arrays.</p>

  <div class="sections">
    <!-- SPREAD -->
    <div class="section">
      <h2>Spread Operator</h2>
      <p class="sec-sub">A = [1, 2, 3] &nbsp;|&nbsp; B = [4, 5, 6]</p>

      <button class="op-btn active" onclick="showSpread('copy')">[...A] — copy</button>
      <button class="op-btn" onclick="showSpread('merge')">[...A, ...B] — merge</button>
      <button class="op-btn" onclick="showSpread('prepend')">[0, ...A] — prepend</button>
      <button class="op-btn" onclick="showSpread('append')">[...A, 7] — append</button>

      <div class="result-label" style="margin-top:0.75rem">// Result</div>
      <div class="result-area" id="spreadResult">[1, 2, 3]</div>
    </div>

    <!-- DESTRUCTURING -->
    <div class="section">
      <h2>Array Destructuring</h2>
      <p class="sec-sub">const arr = [10, 20, 30, 40, 50]</p>

      <div class="toggle-row">
        <button class="toggle-btn on" id="toggleRest" onclick="toggleFeature('rest')">...rest</button>
        <button class="toggle-btn" id="toggleSkip" onclick="toggleFeature('skip')">Skip element</button>
        <button class="toggle-btn" id="toggleDefault" onclick="toggleFeature('default')">Default value</button>
      </div>

      <div id="destVisual"></div>
      <div class="result-label">// What each variable gets</div>
      <div class="result-area" id="destResult"></div>
    </div>
  </div>

  <script>
    const A = [1, 2, 3];
    const B = [4, 5, 6];
    const arr = [10, 20, 30, 40, 50];

    const spreadOps = {
      copy:    { expr: '[...A]',       result: [...A] },
      merge:   { expr: '[...A, ...B]', result: [...A, ...B] },
      prepend: { expr: '[0, ...A]',    result: [0, ...A] },
      append:  { expr: '[...A, 7]',    result: [...A, 7] },
    };

    function showSpread(op) {
      document.querySelectorAll('.op-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      const { expr, result } = spreadOps[op];
      document.getElementById('spreadResult').textContent =
        `${expr}\n→ ${JSON.stringify(result)}`;
    }

    let features = { rest: true, skip: false, default: false };

    function toggleFeature(f) {
      features[f] = !features[f];
      document.getElementById('toggle' + f.charAt(0).toUpperCase() + f.slice(1))
        .classList.toggle('on', features[f]);
      renderDest();
    }

    function renderDest() {
      const visual = document.getElementById('destVisual');
      const result = document.getElementById('destResult');

      const useRest = features.rest;
      const useSkip = features.skip;
      const useDef  = features.default;

      // Build the pattern
      // We always have first (arr[0]=10), optionally skip arr[1], get second (arr[2 or 1]), then rest
      let varFirst  = 10;
      let varSecond = useSkip ? 30 : 20;
      let restArr   = useSkip ? [40, 50] : [30, 40, 50];
      let defValue  = useDef ? undefined : undefined;

      // Visual chips
      let srcChips = arr.map((v, i) => {
        if (useSkip && i === 1) return `<span class="chip chip-skip">${v}</span>`;
        return `<span class="chip chip-val">${v}</span>`;
      }).join(' ');

      let pattern, vars;
      if (useSkip && useRest) {
        pattern = `const [first, , second, ...rest] = arr`;
        vars    = `first = 10, second = 30, rest = [40, 50]`;
        visual.innerHTML = `
          <div class="dest-row">${srcChips}</div>
          <div class="dest-row">
            <span class="chip chip-var">first = 10</span>
            <span class="chip chip-skip">skipped</span>
            <span class="chip chip-var">second = 30</span>
            <span class="chip chip-rest">rest = [40, 50]</span>
          </div>`;
      } else if (useSkip) {
        pattern = `const [first, , second] = arr`;
        vars    = `first = 10, second = 30`;
        visual.innerHTML = `
          <div class="dest-row">${srcChips}</div>
          <div class="dest-row">
            <span class="chip chip-var">first = 10</span>
            <span class="chip chip-skip">skipped</span>
            <span class="chip chip-var">second = 30</span>
          </div>`;
      } else if (useRest) {
        pattern = `const [first, second, ...rest] = arr`;
        vars    = `first = 10, second = 20, rest = [30, 40, 50]`;
        visual.innerHTML = `
          <div class="dest-row">${srcChips}</div>
          <div class="dest-row">
            <span class="chip chip-var">first = 10</span>
            <span class="chip chip-var">second = 20</span>
            <span class="chip chip-rest">rest = [30, 40, 50]</span>
          </div>`;
      } else {
        pattern = `const [first, second] = arr`;
        vars    = `first = 10, second = 20`;
        visual.innerHTML = `
          <div class="dest-row">${srcChips}</div>
          <div class="dest-row">
            <span class="chip chip-var">first = 10</span>
            <span class="chip chip-var">second = 20</span>
          </div>`;
      }

      let defNote = '';
      if (useDef) {
        pattern = pattern.replace('] = arr', ', missing = 0] = arr');
        vars += ', missing = 0 (default — arr[3] is undefined)';
        defNote = '\n// arr has no index 4 match → default 0 used';
      }

      result.textContent = `${pattern}${defNote}\n// → ${vars}`;
    }

    renderDest();
  </script>
</body>
</html>
```
