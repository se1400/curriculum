# Day 19 — The DOM: Selecting & Manipulating Elements: CodePen Code Blocks

Each numbered section corresponds to the `[CODEPEN #]` placeholder in the article.

---

## CODEPEN 1 — querySelector & querySelectorAll Explorer

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>querySelector & querySelectorAll Explorer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
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
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }

    .layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      max-width: 900px;
    }

    @media (max-width: 600px) {
      .layout { grid-template-columns: 1fr; }
    }

    .panel {
      background: white;
      border-radius: 10px;
      padding: 1.25rem;
      border: 1px solid #e2e8f0;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }

    .panel h2 {
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #94a3b8;
      margin-bottom: 0.75rem;
    }

    /* --- Selector Control Panel --- */
    .control-group {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }

    #selector-input {
      flex: 1;
      padding: 0.5rem 0.75rem;
      border: 2px solid #e2e8f0;
      border-radius: 6px;
      font-size: 0.95rem;
      font-family: 'Courier New', monospace;
      color: #0f172a;
      background: #f8fafc;
      transition: border-color 0.15s;
    }

    #selector-input:focus {
      outline: none;
      border-color: #6366f1;
      background: white;
    }

    #selector-input.is-error {
      border-color: #ef4444;
      background: #fef2f2;
    }

    .btn {
      padding: 0.5rem 1rem;
      border: none;
      border-radius: 6px;
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.15s, transform 0.1s;
    }

    .btn:active { transform: scale(0.97); }

    .btn-primary {
      background: #6366f1;
      color: white;
    }

    .btn-primary:hover { background: #4f46e5; }

    .btn-ghost {
      background: #f1f5f9;
      color: #475569;
      border: 1px solid #e2e8f0;
    }

    .btn-ghost:hover { background: #e2e8f0; }

    .presets {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin-bottom: 0.75rem;
    }

    .preset-btn {
      padding: 0.3rem 0.6rem;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      color: #334155;
      cursor: pointer;
      transition: all 0.15s;
    }

    .preset-btn:hover {
      background: #6366f1;
      color: white;
      border-color: #6366f1;
    }

    #result-bar {
      padding: 0.5rem 0.75rem;
      border-radius: 6px;
      font-size: 0.875rem;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      color: #475569;
      min-height: 2.2rem;
    }

    #result-bar.has-matches {
      background: #f0fdf4;
      border-color: #86efac;
      color: #166534;
    }

    #result-bar.no-matches {
      background: #fff7ed;
      border-color: #fdba74;
      color: #9a3412;
    }

    #result-bar.has-error {
      background: #fef2f2;
      border-color: #fca5a5;
      color: #991b1b;
    }

    /* --- Demo Content Area --- */
    #demo-content h3 { font-size: 1.15rem; margin-bottom: 0.75rem; }

    #demo-content p { margin-bottom: 0.6rem; line-height: 1.55; font-size: 0.9rem; }

    #demo-content p.note { color: #0369a1; font-style: italic; }
    #demo-content p.warning { color: #b45309; }

    #demo-content ul {
      margin: 0.5rem 0 0.75rem 1.25rem;
    }

    #demo-content li { margin-bottom: 0.3rem; font-size: 0.9rem; }

    #demo-content .tag {
      display: inline-block;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      font-size: 0.8rem;
      font-weight: 600;
    }

    .tag-js   { background: #fef9c3; color: #713f12; }
    .tag-css  { background: #dbeafe; color: #1e3a8a; }
    .tag-html { background: #fee2e2; color: #7f1d1d; }

    /* Highlight class applied by JS */
    .highlight {
      background: #fef08a;
      font-weight: 700;
      outline: 2px solid #eab308;
      outline-offset: 1px;
      border-radius: 2px;
    }
  </style>
</head>
<body>

  <h1>querySelector &amp; querySelectorAll Explorer</h1>
  <p class="subtitle">Type any CSS selector to highlight matching elements on the page. Try the preset buttons too.</p>

  <div class="layout">

    <!-- Control Panel -->
    <div class="panel">
      <h2>Selector Controls</h2>

      <div class="control-group">
        <input type="text" id="selector-input" placeholder="e.g.  p, .note, li:first-child" spellcheck="false">
        <button class="btn btn-primary" id="run-btn">Select</button>
        <button class="btn btn-ghost" id="clear-btn">Clear</button>
      </div>

      <p style="font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;">Preset selectors:</p>
      <div class="presets">
        <button class="preset-btn" data-selector="p">p</button>
        <button class="preset-btn" data-selector=".note">.note</button>
        <button class="preset-btn" data-selector=".warning">.warning</button>
        <button class="preset-btn" data-selector="[data-role]">[data-role]</button>
        <button class="preset-btn" data-selector="li:nth-child(2)">li:nth-child(2)</button>
        <button class="preset-btn" data-selector=".tag">.tag</button>
        <button class="preset-btn" data-selector="h3, p">h3, p</button>
        <button class="preset-btn" data-selector="li:last-child">li:last-child</button>
        <button class="preset-btn" data-selector="[data-role='admin']">[data-role="admin"]</button>
      </div>

      <div id="result-bar">Enter a selector above and click Select.</div>

      <div id="code-output" style="margin-top:1rem; font-family: 'Courier New', monospace; font-size:0.8rem; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:0.75rem; color:#334155; min-height:3.5rem;"></div>
    </div>

    <!-- Demo Content -->
    <div class="panel" id="demo-content">
      <h2>Demo Content</h2>

      <h3>Introduction to Selectors</h3>

      <p>This is a plain paragraph with no special class. It will match the <code>p</code> selector.</p>

      <p class="note" data-role="user">This paragraph has class <code>note</code> and a <code>data-role="user"</code> attribute.</p>

      <p class="warning" data-role="admin">This paragraph has class <code>warning</code> and <code>data-role="admin"</code>.</p>

      <p>Topics covered in this lesson:</p>

      <ul id="topic-list">
        <li>querySelector</li>
        <li>querySelectorAll</li>
        <li>textContent and innerHTML</li>
        <li>classList API</li>
        <li>Creating and removing elements</li>
      </ul>

      <p>Related technology tags:</p>
      <div style="display:flex; gap:0.4rem; flex-wrap:wrap; margin-top:0.25rem;">
        <span class="tag tag-js">JavaScript</span>
        <span class="tag tag-css">CSS</span>
        <span class="tag tag-html">HTML</span>
      </div>
    </div>

  </div>

  <script>
    const input     = document.getElementById('selector-input');
    const runBtn    = document.getElementById('run-btn');
    const clearBtn  = document.getElementById('clear-btn');
    const resultBar = document.getElementById('result-bar');
    const codeOut   = document.getElementById('code-output');
    const content   = document.getElementById('demo-content');

    function clearHighlights() {
      content.querySelectorAll('.highlight').forEach(el => el.classList.remove('highlight'));
    }

    function runSelector() {
      clearHighlights();
      input.classList.remove('is-error');
      const selector = input.value.trim();

      if (!selector) {
        resultBar.textContent = 'Enter a selector above and click Select.';
        resultBar.className = '';
        codeOut.textContent = '';
        return;
      }

      let matches;
      try {
        matches = content.querySelectorAll(selector);
      } catch (e) {
        resultBar.textContent = `Invalid selector: ${e.message}`;
        resultBar.className = 'has-error';
        input.classList.add('is-error');
        codeOut.textContent = '';
        return;
      }

      matches.forEach(el => el.classList.add('highlight'));

      const count = matches.length;
      if (count === 0) {
        resultBar.textContent = `No elements matched "${selector}"`;
        resultBar.className = 'no-matches';
      } else {
        resultBar.textContent = `${count} element${count !== 1 ? 's' : ''} matched "${selector}"`;
        resultBar.className = 'has-matches';
      }

      codeOut.textContent =
        `// querySelector (first match only)\n` +
        `document.querySelector('${selector}');\n` +
        `// → ${count > 0 ? matches[0].tagName.toLowerCase() + (matches[0].id ? '#'+matches[0].id : matches[0].className ? '.'+[...matches[0].classList].join('.') : '') : 'null'}\n\n` +
        `// querySelectorAll (all ${count} matches)\n` +
        `document.querySelectorAll('${selector}');\n` +
        `// → NodeList(${count})`;
    }

    runBtn.addEventListener('click', runSelector);
    input.addEventListener('keydown', e => { if (e.key === 'Enter') runSelector(); });

    clearBtn.addEventListener('click', () => {
      clearHighlights();
      input.value = '';
      input.classList.remove('is-error');
      resultBar.textContent = 'Enter a selector above and click Select.';
      resultBar.className = '';
      codeOut.textContent = '';
      input.focus();
    });

    document.querySelectorAll('.preset-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        input.value = btn.dataset.selector;
        runSelector();
      });
    });
  </script>

</body>
</html>
```

---

## CODEPEN 2 — Attribute & dataset Explorer

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Attribute & dataset Explorer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f1f5f9;
      color: #1e293b;
      padding: 2rem;
    }

    h1 { font-size: 1.4rem; margin-bottom: 0.25rem; }
    .subtitle { color: #64748b; font-size: 0.875rem; margin-bottom: 1.5rem; }

    .layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      max-width: 860px;
    }

    @media (max-width: 580px) { .layout { grid-template-columns: 1fr; } }

    /* --- Product Card --- */
    .card {
      background: white;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
      overflow: hidden;
      box-shadow: 0 2px 8px rgba(0,0,0,0.07);
      transition: box-shadow 0.2s;
    }

    .card-img {
      width: 100%;
      height: 140px;
      object-fit: cover;
    }

    .card-body { padding: 1rem; }

    .card-category {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #94a3b8;
      margin-bottom: 0.3rem;
    }

    .card-title {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
    }

    .card-price {
      font-size: 1.25rem;
      font-weight: 800;
      color: #4f46e5;
      margin-bottom: 0.75rem;
    }

    .card-badge {
      display: inline-block;
      padding: 0.2rem 0.6rem;
      border-radius: 99px;
      font-size: 0.75rem;
      font-weight: 700;
      background: #dcfce7;
      color: #166534;
    }

    .card-badge.out { background: #fee2e2; color: #991b1b; }

    .card-footer {
      padding: 0.75rem 1rem;
      border-top: 1px solid #f1f5f9;
      display: flex;
      gap: 0.5rem;
    }

    .card-footer button {
      flex: 1;
      padding: 0.45rem;
      border: none;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.15s, opacity 0.15s;
    }

    .card-footer button:disabled {
      opacity: 0.45;
      cursor: not-allowed;
    }

    .btn-add  { background: #4f46e5; color: white; }
    .btn-add:not(:disabled):hover  { background: #4338ca; }
    .btn-wish { background: #f1f5f9; color: #475569; border: 1px solid #e2e8f0; }
    .btn-wish:not(:disabled):hover { background: #e2e8f0; }

    /* --- Control Panel --- */
    .panel {
      background: white;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
      padding: 1.25rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    }

    .panel h2 {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #94a3b8;
      margin-bottom: 1rem;
    }

    .action-group { margin-bottom: 1rem; }

    .action-group label {
      display: block;
      font-size: 0.8rem;
      font-weight: 600;
      color: #475569;
      margin-bottom: 0.3rem;
    }

    .action-row {
      display: flex;
      gap: 0.4rem;
      flex-wrap: wrap;
    }

    .btn {
      padding: 0.4rem 0.75rem;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      background: #f8fafc;
      color: #334155;
      transition: all 0.15s;
    }
    .btn:hover { background: #4f46e5; color: white; border-color: #4f46e5; }

    .output-box {
      margin-top: 1rem;
      background: #0f172a;
      color: #94a3b8;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      min-height: 5rem;
      white-space: pre-wrap;
      line-height: 1.6;
    }

    .output-box .key   { color: #7dd3fc; }
    .output-box .value { color: #86efac; }
    .output-box .code  { color: #f9a8d4; }
  </style>
</head>
<body>

  <h1>Attribute &amp; dataset Explorer</h1>
  <p class="subtitle">Click the buttons to inspect and modify attributes on the product card in real time.</p>

  <div class="layout">

    <!-- Product Card -->
    <div>
      <div class="card"
           id="product-card"
           data-product-id="SKU-7291"
           data-category="Electronics"
           data-price="149.99"
           data-in-stock="true">

        <img class="card-img"
             src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=280&fit=crop"
             alt="Wireless headphones on a neutral background">

        <div class="card-body">
          <p class="card-category" id="card-category">Electronics</p>
          <h2 class="card-title">Wireless Headphones</h2>
          <p class="card-price" id="card-price">$149.99</p>
          <span class="card-badge" id="stock-badge">In Stock</span>
        </div>

        <div class="card-footer">
          <button class="btn-add"  id="add-btn">Add to Cart</button>
          <button class="btn-wish" id="wish-btn">Wishlist</button>
        </div>
      </div>

      <!-- Attribute viewer -->
      <div style="margin-top:1rem; background:white; border-radius:10px; border:1px solid #e2e8f0; padding:1rem;">
        <p style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em; color:#94a3b8; margin-bottom:0.5rem;">Live data-* Attributes</p>
        <div id="attr-viewer" style="font-family:'Courier New',monospace; font-size:0.8rem; color:#334155; line-height:1.8;"></div>
      </div>
    </div>

    <!-- Control Panel -->
    <div class="panel">
      <h2>Attribute Methods Demo</h2>

      <div class="action-group">
        <label>getAttribute / hasAttribute</label>
        <div class="action-row">
          <button class="btn" data-action="get-id">getAttribute('data-product-id')</button>
          <button class="btn" data-action="get-price">getAttribute('data-price')</button>
          <button class="btn" data-action="has-sale">hasAttribute('data-sale')?</button>
        </div>
      </div>

      <div class="action-group">
        <label>setAttribute</label>
        <div class="action-row">
          <button class="btn" data-action="set-sale">Add data-sale="20%"</button>
          <button class="btn" data-action="set-category">Change category → "Audio"</button>
          <button class="btn" data-action="set-price">Raise price → $199.99</button>
        </div>
      </div>

      <div class="action-group">
        <label>removeAttribute</label>
        <div class="action-row">
          <button class="btn" data-action="remove-sale">removeAttribute('data-sale')</button>
        </div>
      </div>

      <div class="action-group">
        <label>dataset API</label>
        <div class="action-row">
          <button class="btn" data-action="read-dataset">Read all dataset values</button>
          <button class="btn" data-action="write-dataset">dataset.color = "Midnight Black"</button>
        </div>
      </div>

      <div class="action-group">
        <label>Boolean attributes &amp; disabled</label>
        <div class="action-row">
          <button class="btn" data-action="toggle-stock">Toggle in-stock / out-of-stock</button>
          <button class="btn" data-action="toggle-disabled">Toggle Add to Cart disabled</button>
        </div>
      </div>

      <div class="output-box" id="output">// Click a button to see the result here.</div>
    </div>

  </div>

  <script>
    const card      = document.getElementById('product-card');
    const output    = document.getElementById('output');
    const addBtn    = document.getElementById('add-btn');
    const badge     = document.getElementById('stock-badge');
    const priceEl   = document.getElementById('card-price');
    const catEl     = document.getElementById('card-category');
    const attrViewer = document.getElementById('attr-viewer');

    function log(codeStr, resultStr) {
      output.innerHTML =
        `<span class="code">${escHtml(codeStr)}</span>\n// → <span class="value">${escHtml(String(resultStr))}</span>`;
    }

    function escHtml(str) {
      return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    }

    function refreshAttrViewer() {
      const attrs = ['data-product-id','data-category','data-price','data-in-stock','data-sale','data-color'];
      attrViewer.innerHTML = attrs
        .filter(a => card.hasAttribute(a))
        .map(a => `<span style="color:#6366f1">${a}</span> = "<span style="color:#059669">${escHtml(card.getAttribute(a))}</span>"`)
        .join('\n');
    }

    refreshAttrViewer();

    const actions = {
      'get-id': () => log(
        `card.getAttribute('data-product-id')`,
        card.getAttribute('data-product-id')
      ),
      'get-price': () => log(
        `card.getAttribute('data-price')`,
        card.getAttribute('data-price') + '  (always a string)'
      ),
      'has-sale': () => log(
        `card.hasAttribute('data-sale')`,
        card.hasAttribute('data-sale')
      ),
      'set-sale': () => {
        card.setAttribute('data-sale', '20%');
        refreshAttrViewer();
        log(`card.setAttribute('data-sale', '20%')`, 'attribute added ✓');
      },
      'set-category': () => {
        card.setAttribute('data-category', 'Audio');
        card.dataset.category = 'Audio';
        catEl.textContent = 'Audio';
        refreshAttrViewer();
        log(`card.setAttribute('data-category', 'Audio')`, 'category updated ✓');
      },
      'set-price': () => {
        card.setAttribute('data-price', '199.99');
        priceEl.textContent = '$199.99';
        refreshAttrViewer();
        log(`card.setAttribute('data-price', '199.99')`, 'price updated ✓');
      },
      'remove-sale': () => {
        card.removeAttribute('data-sale');
        refreshAttrViewer();
        log(`card.removeAttribute('data-sale')`, 'attribute removed ✓');
      },
      'read-dataset': () => {
        const entries = Object.entries(card.dataset)
          .map(([k, v]) => `  ${k}: "${v}"`)
          .join('\n');
        output.innerHTML = `<span class="code">card.dataset</span>\n<span class="value">{\n${escHtml(entries)}\n}</span>`;
      },
      'write-dataset': () => {
        card.dataset.color = 'Midnight Black';
        refreshAttrViewer();
        log(`card.dataset.color = 'Midnight Black'`, 'data-color attribute created ✓');
      },
      'toggle-stock': () => {
        const inStock = card.dataset.inStock === 'true';
        card.dataset.inStock = String(!inStock);
        if (inStock) {
          badge.textContent = 'Out of Stock';
          badge.classList.add('out');
          addBtn.disabled = true;
        } else {
          badge.textContent = 'In Stock';
          badge.classList.remove('out');
          addBtn.disabled = false;
        }
        refreshAttrViewer();
        log(`card.dataset.inStock = '${card.dataset.inStock}'`, `button disabled: ${addBtn.disabled}`);
      },
      'toggle-disabled': () => {
        addBtn.disabled = !addBtn.disabled;
        log(`addBtn.disabled = ${addBtn.disabled}`, `Add to Cart is now ${addBtn.disabled ? 'disabled' : 'enabled'}`);
      }
    };

    document.querySelectorAll('[data-action]').forEach(btn => {
      btn.addEventListener('click', () => {
        actions[btn.dataset.action]?.();
      });
    });
  </script>

</body>
</html>
```

---

## CODEPEN 3 — classList Toggle Demo

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>classList Toggle Demo</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f1f5f9;
      color: #1e293b;
      padding: 2rem;
      min-height: 100vh;
    }

    h1 { font-size: 1.4rem; margin-bottom: 0.25rem; }
    .subtitle { color: #64748b; font-size: 0.875rem; margin-bottom: 1.5rem; }

    .layout {
      display: grid;
      grid-template-columns: 1fr 1.4fr;
      gap: 1.5rem;
      max-width: 860px;
    }

    @media (max-width: 580px) { .layout { grid-template-columns: 1fr; } }

    /* ==========================================
       THE DEMO CARD — affected by classList
    ========================================== */
    .card-wrapper {
      display: flex;
      align-items: flex-start;
      justify-content: center;
      padding: 2rem 1rem;
      background: white;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      min-height: 260px;
    }

    .demo-card {
      background: #6366f1;
      color: white;
      width: 180px;
      padding: 1.25rem;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.95rem;
      text-align: center;
      line-height: 1.4;
      transition: all 0.3s ease;
    }

    /* State classes */
    .demo-card.is-large {
      width: 260px;
      font-size: 1.15rem;
      padding: 2rem;
    }

    .demo-card.is-dark {
      background: #0f172a;
      color: #94a3b8;
    }

    .demo-card.has-border {
      border: 4px solid #fbbf24;
      box-shadow: 0 0 0 4px rgba(251, 191, 36, 0.25);
    }

    .demo-card.is-rounded {
      border-radius: 9999px;
    }

    .demo-card.theme-success {
      background: #16a34a;
    }

    /* Class pill badges */
    .class-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem;
      margin-top: 0.85rem;
      justify-content: center;
    }

    .class-pill {
      padding: 0.2rem 0.55rem;
      background: rgba(255,255,255,0.2);
      border-radius: 99px;
      font-size: 0.7rem;
      font-weight: 700;
    }

    /* ==========================================
       CONTROL PANEL
    ========================================== */
    .panel {
      background: white;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
      padding: 1.25rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    .panel h2 {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #94a3b8;
      margin-bottom: 1rem;
    }

    .method-group { margin-bottom: 1rem; }

    .method-label {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.4rem;
    }

    .method-name {
      font-family: 'Courier New', monospace;
      font-size: 0.82rem;
      font-weight: 700;
      color: #4f46e5;
      background: #eef2ff;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
    }

    .method-desc {
      font-size: 0.75rem;
      color: #64748b;
    }

    .btn-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem;
    }

    .btn {
      padding: 0.35rem 0.7rem;
      border-radius: 6px;
      font-size: 0.78rem;
      font-weight: 600;
      border: 1px solid #e2e8f0;
      background: #f8fafc;
      color: #334155;
      cursor: pointer;
      transition: all 0.15s;
    }
    .btn:hover { background: #4f46e5; color: white; border-color: #4f46e5; }

    .btn.active-state { background: #dcfce7; color: #15803d; border-color: #86efac; }
    .btn.active-state:hover { background: #16a34a; color: white; border-color: #16a34a; }

    /* Output area */
    .output-box {
      margin-top: 1rem;
      background: #0f172a;
      color: #94a3b8;
      border-radius: 8px;
      padding: 0.65rem 0.9rem;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      min-height: 3rem;
      white-space: pre-wrap;
      line-height: 1.7;
    }
  </style>
</head>
<body>

  <h1>classList Toggle Demo</h1>
  <p class="subtitle">Use the buttons to add, remove, toggle, and inspect classes on the card. Watch it change in real time.</p>

  <div class="layout">

    <!-- Demo card -->
    <div>
      <div class="card-wrapper">
        <div class="demo-card" id="demo-card">
          <div>Demo Card</div>
          <div style="font-size:0.75rem; font-weight:400; margin-top:0.5rem; opacity:0.8;">Modify my classes</div>
          <div class="class-pills" id="class-pills"></div>
        </div>
      </div>

      <!-- Current classList display -->
      <div style="margin-top:1rem; background:white; border-radius:10px; border:1px solid #e2e8f0; padding:0.9rem;">
        <p style="font-size:0.75rem; font-weight:600; color:#64748b; margin-bottom:0.35rem;">card.className</p>
        <code id="classname-display" style="font-size:0.8rem; color:#4f46e5; word-break:break-all;">demo-card</code>
      </div>
    </div>

    <!-- Controls -->
    <div class="panel">
      <h2>classList Methods</h2>

      <!-- add -->
      <div class="method-group">
        <div class="method-label">
          <span class="method-name">.add()</span>
          <span class="method-desc">Add a class (safe if already present)</span>
        </div>
        <div class="btn-row">
          <button class="btn" data-action="add" data-class="is-large">add("is-large")</button>
          <button class="btn" data-action="add" data-class="is-dark">add("is-dark")</button>
          <button class="btn" data-action="add" data-class="has-border">add("has-border")</button>
          <button class="btn" data-action="add" data-class="is-rounded">add("is-rounded")</button>
        </div>
      </div>

      <!-- remove -->
      <div class="method-group">
        <div class="method-label">
          <span class="method-name">.remove()</span>
          <span class="method-desc">Remove a class (safe if already absent)</span>
        </div>
        <div class="btn-row">
          <button class="btn" data-action="remove" data-class="is-large">remove("is-large")</button>
          <button class="btn" data-action="remove" data-class="is-dark">remove("is-dark")</button>
          <button class="btn" data-action="remove" data-class="has-border">remove("has-border")</button>
          <button class="btn" data-action="remove" data-class="is-rounded">remove("is-rounded")</button>
        </div>
      </div>

      <!-- toggle -->
      <div class="method-group">
        <div class="method-label">
          <span class="method-name">.toggle()</span>
          <span class="method-desc">Add if absent, remove if present</span>
        </div>
        <div class="btn-row">
          <button class="btn" data-action="toggle" data-class="is-large">toggle("is-large")</button>
          <button class="btn" data-action="toggle" data-class="is-dark">toggle("is-dark")</button>
          <button class="btn" data-action="toggle" data-class="has-border">toggle("has-border")</button>
          <button class="btn" data-action="toggle" data-class="is-rounded">toggle("is-rounded")</button>
        </div>
      </div>

      <!-- contains -->
      <div class="method-group">
        <div class="method-label">
          <span class="method-name">.contains()</span>
          <span class="method-desc">Returns true or false</span>
        </div>
        <div class="btn-row">
          <button class="btn" data-action="contains" data-class="is-large">contains("is-large")?</button>
          <button class="btn" data-action="contains" data-class="is-dark">contains("is-dark")?</button>
          <button class="btn" data-action="contains" data-class="has-border">contains("has-border")?</button>
        </div>
      </div>

      <!-- replace -->
      <div class="method-group">
        <div class="method-label">
          <span class="method-name">.replace()</span>
          <span class="method-desc">Swap one class for another</span>
        </div>
        <div class="btn-row">
          <button class="btn" data-action="replace" data-old="is-dark" data-new="theme-success">replace("is-dark" → "theme-success")</button>
          <button class="btn" data-action="replace" data-old="theme-success" data-new="is-dark">replace("theme-success" → "is-dark")</button>
        </div>
      </div>

      <div class="output-box" id="output">// Click a button to see what classList does.</div>
    </div>

  </div>

  <script>
    const card     = document.getElementById('demo-card');
    const pills    = document.getElementById('class-pills');
    const display  = document.getElementById('classname-display');
    const output   = document.getElementById('output');

    const STATE_CLASSES = ['is-large','is-dark','has-border','is-rounded','theme-success'];

    function refreshPills() {
      pills.innerHTML = STATE_CLASSES
        .filter(c => card.classList.contains(c))
        .map(c => `<span class="class-pill">${c}</span>`)
        .join('');
      display.textContent = card.className;
    }

    function log(code, result) {
      output.textContent = `${code}\n// → ${result}`;
    }

    document.querySelectorAll('[data-action]').forEach(btn => {
      btn.addEventListener('click', () => {
        const action = btn.dataset.action;
        const cls    = btn.dataset.class;

        if (action === 'add') {
          card.classList.add(cls);
          log(`card.classList.add('${cls}')`, 'class added (no error if already present)');
        } else if (action === 'remove') {
          card.classList.remove(cls);
          log(`card.classList.remove('${cls}')`, 'class removed (no error if already absent)');
        } else if (action === 'toggle') {
          const wasAdded = card.classList.toggle(cls);
          log(`card.classList.toggle('${cls}')`, `${wasAdded} (true = added, false = removed)`);
        } else if (action === 'contains') {
          const result = card.classList.contains(cls);
          log(`card.classList.contains('${cls}')`, result);
        } else if (action === 'replace') {
          const oldCls = btn.dataset.old;
          const newCls = btn.dataset.new;
          const success = card.classList.replace(oldCls, newCls);
          log(`card.classList.replace('${oldCls}', '${newCls}')`, success
            ? `true — replacement successful`
            : `false — '${oldCls}' was not present, nothing changed`);
        }

        refreshPills();
      });
    });

    refreshPills();
  </script>

</body>
</html>
```

---

## CODEPEN 4 — Dynamic Element Creation

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dynamic Element Creation</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f1f5f9;
      color: #1e293b;
      padding: 2rem;
      min-height: 100vh;
    }

    h1 { font-size: 1.4rem; margin-bottom: 0.25rem; }
    .subtitle { color: #64748b; font-size: 0.875rem; margin-bottom: 1.5rem; }

    .app {
      max-width: 560px;
      background: white;
      border-radius: 14px;
      border: 1px solid #e2e8f0;
      box-shadow: 0 4px 16px rgba(0,0,0,0.08);
      overflow: hidden;
    }

    /* Header */
    .app-header {
      padding: 1.25rem 1.5rem;
      background: #4f46e5;
      color: white;
    }

    .app-header h2 { font-size: 1.1rem; margin-bottom: 0.15rem; }

    .item-count {
      font-size: 0.8rem;
      opacity: 0.8;
    }

    /* Input area */
    .input-area {
      padding: 1rem 1.5rem;
      display: flex;
      gap: 0.5rem;
      border-bottom: 1px solid #f1f5f9;
    }

    #task-input {
      flex: 1;
      padding: 0.55rem 0.85rem;
      border: 2px solid #e2e8f0;
      border-radius: 8px;
      font-size: 0.95rem;
      color: #1e293b;
      background: #f8fafc;
      transition: border-color 0.15s, background 0.15s;
    }

    #task-input:focus {
      outline: none;
      border-color: #6366f1;
      background: white;
    }

    .btn-add {
      padding: 0.55rem 1.1rem;
      background: #4f46e5;
      color: white;
      border: none;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.9rem;
      cursor: pointer;
      transition: background 0.15s, transform 0.1s;
      white-space: nowrap;
    }

    .btn-add:hover { background: #4338ca; }
    .btn-add:active { transform: scale(0.96); }

    /* Task list */
    #task-list {
      list-style: none;
      margin: 0;
      padding: 0;
      min-height: 80px;
      max-height: 360px;
      overflow-y: auto;
    }

    .task-item {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.75rem 1.5rem;
      border-bottom: 1px solid #f8fafc;
      animation: slideIn 0.2s ease;
    }

    @keyframes slideIn {
      from { opacity: 0; transform: translateY(-8px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    .task-item:last-child { border-bottom: none; }
    .task-item:hover { background: #fafafa; }

    .task-check {
      width: 18px;
      height: 18px;
      border: 2px solid #cbd5e1;
      border-radius: 4px;
      cursor: pointer;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.7rem;
      color: white;
      background: white;
      transition: all 0.15s;
    }

    .task-item.done .task-check {
      background: #22c55e;
      border-color: #22c55e;
    }

    .task-item.done .task-check::after { content: '✓'; }

    .task-label {
      flex: 1;
      font-size: 0.925rem;
      color: #334155;
      transition: all 0.2s;
    }

    .task-item.done .task-label {
      text-decoration: line-through;
      color: #94a3b8;
    }

    .task-meta {
      font-size: 0.7rem;
      color: #94a3b8;
      white-space: nowrap;
    }

    .btn-remove {
      background: none;
      border: none;
      color: #cbd5e1;
      cursor: pointer;
      font-size: 1rem;
      line-height: 1;
      padding: 0.2rem 0.3rem;
      border-radius: 4px;
      transition: color 0.15s, background 0.15s;
      flex-shrink: 0;
    }

    .btn-remove:hover { color: #ef4444; background: #fee2e2; }

    /* Empty state */
    .empty-state {
      padding: 2.5rem 1rem;
      text-align: center;
      color: #94a3b8;
      font-size: 0.9rem;
    }

    .empty-state .icon { font-size: 2rem; display: block; margin-bottom: 0.5rem; }

    /* Footer */
    .app-footer {
      padding: 0.85rem 1.5rem;
      border-top: 1px solid #f1f5f9;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
    }

    .footer-info { font-size: 0.78rem; color: #94a3b8; }

    .btn-clear {
      padding: 0.4rem 0.85rem;
      background: #fee2e2;
      color: #dc2626;
      border: none;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.15s;
    }

    .btn-clear:hover { background: #fecaca; }
    .btn-clear:disabled { opacity: 0.4; cursor: not-allowed; }

    /* Code log */
    .code-log {
      margin-top: 1.25rem;
      background: #0f172a;
      border-radius: 10px;
      padding: 0.85rem 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      color: #94a3b8;
      line-height: 1.7;
      max-height: 140px;
      overflow-y: auto;
      max-width: 560px;
    }

    .log-line { display: block; }
    .log-line .kw { color: #c084fc; }
    .log-line .fn { color: #67e8f9; }
    .log-line .str { color: #86efac; }
    .log-line .comment { color: #475569; }
  </style>
</head>
<body>

  <h1>Dynamic Element Creation</h1>
  <p class="subtitle">Each item is built with <code>createElement</code>, configured, and inserted with <code>appendChild</code>. Clear all uses <code>replaceChildren()</code>.</p>

  <div class="app">
    <div class="app-header">
      <h2>Task Manager</h2>
      <p class="item-count" id="count-label">0 tasks</p>
    </div>

    <div class="input-area">
      <input type="text" id="task-input" placeholder="Add a new task…" maxlength="80" autocomplete="off">
      <button class="btn-add" id="add-btn">+ Add</button>
    </div>

    <ul id="task-list">
      <li class="empty-state" id="empty-msg">
        <span class="icon">📋</span>
        No tasks yet. Add one above!
      </li>
    </ul>

    <div class="app-footer">
      <span class="footer-info" id="footer-info">Add tasks to get started</span>
      <button class="btn-clear" id="clear-btn" disabled>Clear All</button>
    </div>
  </div>

  <div class="code-log" id="code-log">
    <span class="log-line"><span class="comment">// DOM operations will be logged here</span></span>
  </div>

  <script>
    const taskInput = document.getElementById('task-input');
    const addBtn    = document.getElementById('add-btn');
    const taskList  = document.getElementById('task-list');
    const emptyMsg  = document.getElementById('empty-msg');
    const clearBtn  = document.getElementById('clear-btn');
    const countLabel = document.getElementById('count-label');
    const footerInfo = document.getElementById('footer-info');
    const codeLog   = document.getElementById('code-log');

    let taskCount = 0;
    let doneCount = 0;

    function logCode(html) {
      const line = document.createElement('span');
      line.className = 'log-line';
      line.innerHTML = html;
      codeLog.appendChild(line);
      codeLog.scrollTop = codeLog.scrollHeight;
    }

    function updateStats() {
      const items = taskList.querySelectorAll('.task-item');
      const total = items.length;
      const done  = taskList.querySelectorAll('.task-item.done').length;

      countLabel.textContent = `${total} task${total !== 1 ? 's' : ''}`;
      footerInfo.textContent = total === 0
        ? 'Add tasks to get started'
        : `${done} of ${total} completed`;
      clearBtn.disabled = total === 0;
    }

    function addTask() {
      const text = taskInput.value.trim();
      if (!text) { taskInput.focus(); return; }

      // Remove empty state message
      if (emptyMsg.parentNode) emptyMsg.remove();

      taskCount++;
      const id = taskCount;
      const now = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

      // --- createElement sequence ---
      const li = document.createElement('li');
      li.classList.add('task-item');
      li.dataset.taskId = id;

      const check = document.createElement('div');
      check.classList.add('task-check');
      check.title = 'Mark complete';

      const label = document.createElement('span');
      label.classList.add('task-label');
      label.textContent = text;   // textContent — safe for user input

      const meta = document.createElement('span');
      meta.classList.add('task-meta');
      meta.textContent = now;

      const removeBtn = document.createElement('button');
      removeBtn.classList.add('btn-remove');
      removeBtn.innerHTML = '&times;';
      removeBtn.setAttribute('aria-label', `Remove task: ${text}`);

      // Assemble
      li.appendChild(check);
      li.appendChild(label);
      li.appendChild(meta);
      li.appendChild(removeBtn);

      // Insert into the list
      taskList.appendChild(li);

      logCode(
        `<span class="kw">const</span> li = <span class="fn">document.createElement</span>(<span class="str">'li'</span>);\n` +
        `li.textContent = <span class="str">'${text.replace(/'/g, "\\'").substring(0, 30)}${text.length > 30 ? '…' : ''}'</span>;\n` +
        `taskList.<span class="fn">appendChild</span>(li); <span class="comment">// #${id}</span>`
      );

      // Toggle done
      check.addEventListener('click', () => {
        li.classList.toggle('done');
        updateStats();
      });

      // Remove item
      removeBtn.addEventListener('click', () => {
        li.remove();
        logCode(
          `taskItem_${id}.<span class="fn">remove</span>(); <span class="comment">// removed task #${id}</span>`
        );
        if (!taskList.querySelector('.task-item')) {
          taskList.appendChild(emptyMsg);
        }
        updateStats();
      });

      taskInput.value = '';
      taskInput.focus();
      updateStats();
    }

    // Clear all with replaceChildren()
    clearBtn.addEventListener('click', () => {
      taskList.replaceChildren(emptyMsg);
      logCode(
        `taskList.<span class="fn">replaceChildren</span>(emptyMsg); <span class="comment">// cleared all tasks</span>`
      );
      taskCount = 0;
      doneCount = 0;
      updateStats();
    });

    addBtn.addEventListener('click', addTask);
    taskInput.addEventListener('keydown', e => { if (e.key === 'Enter') addTask(); });
  </script>

</body>
</html>
```

---

## CODEPEN 5 — DOM Traversal Explorer

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DOM Traversal Explorer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: system-ui, sans-serif;
      background: #f1f5f9;
      color: #1e293b;
      padding: 2rem;
    }

    h1 { font-size: 1.4rem; margin-bottom: 0.25rem; }
    .subtitle { color: #64748b; font-size: 0.875rem; margin-bottom: 1.5rem; }

    .layout {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 1.5rem;
      max-width: 900px;
    }

    @media (max-width: 620px) { .layout { grid-template-columns: 1fr; } }

    /* ==========================================
       ORG CHART TREE
    ========================================== */
    .tree-panel {
      background: white;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
      padding: 1.5rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    .tree-panel h2 {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #94a3b8;
      margin-bottom: 1rem;
    }

    .tree-hint {
      font-size: 0.78rem;
      color: #64748b;
      margin-bottom: 1rem;
      padding: 0.5rem 0.75rem;
      background: #f8fafc;
      border-radius: 6px;
      border-left: 3px solid #6366f1;
    }

    nav#org-tree {
      /* Intentional: wrapping in <nav> so closest('nav') can be demonstrated */
    }

    .tree {
      list-style: none;
      padding: 0;
    }

    .tree ul {
      list-style: none;
      padding-left: 1.5rem;
      margin-top: 0.35rem;
      border-left: 2px solid #e2e8f0;
    }

    .tree-node {
      margin: 0.3rem 0;
    }

    .node-label {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.4rem 0.75rem;
      border-radius: 6px;
      border: 2px solid transparent;
      cursor: pointer;
      font-size: 0.88rem;
      font-weight: 500;
      background: #f8fafc;
      color: #334155;
      transition: all 0.15s;
      user-select: none;
    }

    .node-label:hover {
      background: #eef2ff;
      border-color: #a5b4fc;
      color: #4338ca;
    }

    .node-label.selected {
      background: #4f46e5;
      color: white;
      border-color: #4f46e5;
      box-shadow: 0 2px 8px rgba(79,70,229,0.3);
    }

    /* Roles */
    .node-label[data-role="ceo"]    { background: #fef3c7; color: #78350f; }
    .node-label[data-role="ceo"].selected { background: #d97706; color: white; border-color: #d97706; }

    .node-label[data-role="vp"]     { background: #dbeafe; color: #1e3a8a; }
    .node-label[data-role="vp"].selected { background: #2563eb; color: white; border-color: #2563eb; }

    .node-label[data-role="manager"] { background: #dcfce7; color: #14532d; }
    .node-label[data-role="manager"].selected { background: #16a34a; color: white; border-color: #16a34a; }

    .node-label[data-role="engineer"],
    .node-label[data-role="designer"] { background: #f1f5f9; color: #334155; }
    .node-label[data-role="engineer"].selected,
    .node-label[data-role="designer"].selected { background: #475569; color: white; border-color: #475569; }

    .role-icon { font-size: 0.9rem; }

    /* Highlight related nodes */
    .node-label.is-parent   { outline: 2px dashed #f59e0b; outline-offset: 2px; }
    .node-label.is-child    { outline: 2px dashed #22c55e; outline-offset: 2px; }
    .node-label.is-sibling  { outline: 2px dashed #60a5fa; outline-offset: 2px; }
    .node-label.is-ancestor { outline: 2px dashed #f97316; outline-offset: 2px; }

    /* Legend */
    .legend {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 1rem;
    }

    .legend-item {
      display: flex;
      align-items: center;
      gap: 0.3rem;
      font-size: 0.72rem;
      color: #64748b;
    }

    .legend-dot {
      width: 12px;
      height: 12px;
      border-radius: 2px;
      border: 2px dashed;
    }

    /* ==========================================
       INFO PANEL
    ========================================== */
    .info-panel {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .info-box {
      background: white;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
      padding: 1.1rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    .info-box h2 {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #94a3b8;
      margin-bottom: 0.75rem;
    }

    .prop-list {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .prop-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
      align-items: center;
    }

    .prop-key {
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      color: #6366f1;
      font-weight: 600;
    }

    .prop-val {
      font-size: 0.82rem;
      color: #334155;
      background: #f8fafc;
      padding: 0.25rem 0.5rem;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .prop-val.null-val { color: #94a3b8; font-style: italic; }
    .prop-val.true-val { color: #16a34a; }

    .code-snippet {
      background: #0f172a;
      border-radius: 8px;
      padding: 0.75rem;
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      color: #94a3b8;
      white-space: pre-wrap;
      line-height: 1.65;
    }

    .code-snippet .kw  { color: #c084fc; }
    .code-snippet .fn  { color: #67e8f9; }
    .code-snippet .str { color: #86efac; }
    .code-snippet .num { color: #fbbf24; }
  </style>
</head>
<body>

  <h1>DOM Traversal Explorer</h1>
  <p class="subtitle">Click any node in the org chart. See its parent, children, siblings, and <code>closest()</code> result in real time.</p>

  <div class="layout">

    <!-- Org Chart -->
    <div class="tree-panel">
      <h2>Company Org Chart (click any node)</h2>
      <p class="tree-hint">Click a node to select it. Related nodes will be highlighted: parent (orange), children (green), siblings (blue).</p>

      <nav id="org-tree">
        <ul class="tree">
          <li class="tree-node" data-id="ceo">
            <span class="node-label" data-role="ceo" data-name="Alex Chen" data-depth="0">
              <span class="role-icon">👑</span> CEO &mdash; Alex Chen
            </span>
            <ul>
              <li class="tree-node" data-id="vp-eng">
                <span class="node-label" data-role="vp" data-name="Jordan Lee" data-depth="1">
                  <span class="role-icon">🏗️</span> VP Engineering &mdash; Jordan Lee
                </span>
                <ul>
                  <li class="tree-node" data-id="mgr-fe">
                    <span class="node-label" data-role="manager" data-name="Sam Park" data-depth="2">
                      <span class="role-icon">📋</span> Mgr Frontend &mdash; Sam Park
                    </span>
                    <ul>
                      <li class="tree-node" data-id="eng1">
                        <span class="node-label" data-role="engineer" data-name="Riley Kim" data-depth="3">
                          <span class="role-icon">💻</span> Engineer &mdash; Riley Kim
                        </span>
                      </li>
                      <li class="tree-node" data-id="eng2">
                        <span class="node-label" data-role="designer" data-name="Casey Wu" data-depth="3">
                          <span class="role-icon">🎨</span> Designer &mdash; Casey Wu
                        </span>
                      </li>
                      <li class="tree-node" data-id="eng3">
                        <span class="node-label" data-role="engineer" data-name="Morgan Hayes" data-depth="3">
                          <span class="role-icon">💻</span> Engineer &mdash; Morgan Hayes
                        </span>
                      </li>
                    </ul>
                  </li>
                  <li class="tree-node" data-id="mgr-be">
                    <span class="node-label" data-role="manager" data-name="Drew Patel" data-depth="2">
                      <span class="role-icon">📋</span> Mgr Backend &mdash; Drew Patel
                    </span>
                    <ul>
                      <li class="tree-node" data-id="eng4">
                        <span class="node-label" data-role="engineer" data-name="Quinn Torres" data-depth="3">
                          <span class="role-icon">💻</span> Engineer &mdash; Quinn Torres
                        </span>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
              <li class="tree-node" data-id="vp-design">
                <span class="node-label" data-role="vp" data-name="Taylor Morgan" data-depth="1">
                  <span class="role-icon">🎨</span> VP Design &mdash; Taylor Morgan
                </span>
                <ul>
                  <li class="tree-node" data-id="des1">
                    <span class="node-label" data-role="designer" data-name="Avery Nguyen" data-depth="2">
                      <span class="role-icon">🖌️</span> Designer &mdash; Avery Nguyen
                    </span>
                  </li>
                </ul>
              </li>
            </ul>
          </li>
        </ul>
      </nav>

      <div class="legend">
        <div class="legend-item"><div class="legend-dot" style="border-color:#f59e0b"></div> parentElement</div>
        <div class="legend-item"><div class="legend-dot" style="border-color:#22c55e"></div> children</div>
        <div class="legend-item"><div class="legend-dot" style="border-color:#60a5fa"></div> siblings</div>
        <div class="legend-item"><div class="legend-dot" style="border-color:#f97316"></div> closest(nav)</div>
      </div>
    </div>

    <!-- Info Panel -->
    <div class="info-panel">

      <div class="info-box">
        <h2>Selected Node</h2>
        <div class="prop-list" id="selected-info">
          <p style="color:#94a3b8; font-size:0.85rem;">Click any node in the tree to inspect it.</p>
        </div>
      </div>

      <div class="info-box">
        <h2>Traversal Results</h2>
        <div class="prop-list" id="traversal-info">
          <p style="color:#94a3b8; font-size:0.85rem;">Results appear here after selection.</p>
        </div>
      </div>

      <div class="info-box">
        <h2>Code</h2>
        <div class="code-snippet" id="code-display">// Select a node to see the code</div>
      </div>

    </div>

  </div>

  <script>
    const tree         = document.getElementById('org-tree');
    const selectedInfo = document.getElementById('selected-info');
    const traversalInfo = document.getElementById('traversal-info');
    const codeDisplay  = document.getElementById('code-display');

    function clearHighlights() {
      tree.querySelectorAll('.node-label').forEach(el => {
        el.classList.remove('selected', 'is-parent', 'is-child', 'is-sibling', 'is-ancestor');
      });
    }

    function makePropRow(key, value, cls = '') {
      const row = document.createElement('div');
      row.className = 'prop-row';

      const k = document.createElement('span');
      k.className = 'prop-key';
      k.textContent = key;

      const v = document.createElement('span');
      v.className = 'prop-val' + (cls ? ' ' + cls : '');
      v.textContent = value;
      v.title = value;

      row.appendChild(k);
      row.appendChild(v);
      return row;
    }

    tree.addEventListener('click', event => {
      const label = event.target.closest('.node-label');
      if (!label) return;

      clearHighlights();
      label.classList.add('selected');

      const name  = label.dataset.name;
      const role  = label.dataset.role;
      const depth = label.dataset.depth;

      // --- parentElement ---
      // The .node-label is inside a .tree-node <li>
      // parentElement of the label → <li class="tree-node">
      // parentElement of that <li> → <ul>
      // parentElement of that <ul> → parent <li class="tree-node"> (or <nav> if top level)
      const parentLI = label.parentElement;       // <li class="tree-node"> that wraps this label
      const parentUL = parentLI.parentElement;    // the <ul> containing this <li>
      const parentNode = parentUL.parentElement;  // parent <li> or <nav>
      const parentLabel = parentNode.querySelector(':scope > .node-label');

      if (parentLabel && parentLabel !== label) {
        parentLabel.classList.add('is-parent');
      }

      // --- children (sibling <li> items in the same <ul>, which are siblings of the selected li) ---
      const siblingLIs = [...parentUL.children].filter(li => li !== parentLI && li.matches('.tree-node'));
      siblingLIs.forEach(sib => {
        const sibLabel = sib.querySelector(':scope > .node-label');
        if (sibLabel) sibLabel.classList.add('is-sibling');
      });

      // --- element's own children (nested list items) ---
      const ownUL = parentLI.querySelector(':scope > ul');
      if (ownUL) {
        ownUL.querySelectorAll(':scope > .tree-node > .node-label').forEach(cl => {
          cl.classList.add('is-child');
        });
      }

      // --- closest('nav') ---
      const ancestorNav = label.closest('nav');
      if (ancestorNav) {
        // highlight the tree panel border
        ancestorNav.style.outline = '3px dashed #f97316';
        ancestorNav.style.outlineOffset = '4px';
        ancestorNav.style.borderRadius = '6px';
        setTimeout(() => {
          ancestorNav.style.outline = '';
          ancestorNav.style.outlineOffset = '';
        }, 1400);
      }

      // --- matches() ---
      const matchesVP = label.matches('[data-role="vp"]');
      const matchesManager = label.matches('[data-role="manager"]');

      // Children count
      const childrenCount = ownUL ? ownUL.querySelectorAll(':scope > .tree-node').length : 0;
      const siblingCount = siblingLIs.length;

      // Populate selected-info
      selectedInfo.innerHTML = '';
      selectedInfo.appendChild(makePropRow('name', name));
      selectedInfo.appendChild(makePropRow('data-role', role));
      selectedInfo.appendChild(makePropRow('data-depth', depth));
      selectedInfo.appendChild(makePropRow('tagName', label.tagName.toLowerCase()));

      // Populate traversal-info
      traversalInfo.innerHTML = '';
      traversalInfo.appendChild(makePropRow(
        'parentElement',
        parentLabel ? parentLabel.dataset.name : '<nav> (top level)',
      ));
      traversalInfo.appendChild(makePropRow(
        'children.length',
        childrenCount,
      ));
      traversalInfo.appendChild(makePropRow(
        'nextElementSibling',
        (() => {
          const next = parentLI.nextElementSibling;
          return next ? (next.querySelector('.node-label')?.dataset.name || 'exists') : 'null';
        })(),
        parentLI.nextElementSibling ? '' : 'null-val'
      ));
      traversalInfo.appendChild(makePropRow(
        'previousElementSibling',
        (() => {
          const prev = parentLI.previousElementSibling;
          return prev ? (prev.querySelector('.node-label')?.dataset.name || 'exists') : 'null';
        })(),
        parentLI.previousElementSibling ? '' : 'null-val'
      ));
      traversalInfo.appendChild(makePropRow(
        'closest("nav")',
        ancestorNav ? '#org-tree <nav>' : 'null',
        ancestorNav ? 'true-val' : 'null-val'
      ));
      traversalInfo.appendChild(makePropRow(
        'matches("[data-role=\'vp\']")',
        matchesVP,
        matchesVP ? 'true-val' : ''
      ));

      // Code display
      const nodeName = name.replace(/'/g, "\\'");
      codeDisplay.innerHTML =
        `<span class="kw">const</span> label = clickedElement;\n\n` +
        `<span class="comment">// parentElement (up the tree)</span>\n` +
        `label.parentElement;  <span class="comment">// &lt;li&gt;</span>\n` +
        `label.parentElement.parentElement; <span class="comment">// &lt;ul&gt;</span>\n\n` +
        `<span class="comment">// children (down the tree)</span>\n` +
        `label.parentElement.children; <span class="comment">// HTMLCollection(${childrenCount})</span>\n\n` +
        `<span class="comment">// traversal</span>\n` +
        `label.nextElementSibling;\n` +
        `label.previousElementSibling;\n\n` +
        `<span class="comment">// walk up to find ancestor</span>\n` +
        `label.<span class="fn">closest</span>(<span class="str">'nav'</span>);\n` +
        `<span class="comment">// → ${ancestorNav ? '#org-tree' : 'null'}</span>\n\n` +
        `<span class="comment">// test this element against a selector</span>\n` +
        `label.<span class="fn">matches</span>(<span class="str">'[data-role="vp"]'</span>);\n` +
        `<span class="comment">// → ${matchesVP}</span>`;
    });
  </script>

</body>
</html>
```
