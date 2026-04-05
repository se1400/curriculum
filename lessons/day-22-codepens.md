# Day 22 — CodePen Examples
## Objects and Galleries: Arrays of Objects and Data-Driven Interfaces

---

## CodePen 1 — Object Explorer

**Placement:** After the "JavaScript Objects" section.
**Demonstrates:** A single object with multiple properties displayed in a styled card. Dot notation reading properties, `.toFixed()` for price formatting, showing property names and types.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Object Explorer</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      padding: 2rem;
      align-items: start;
      max-width: 820px;
      margin: 0 auto;
    }

    h2 {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.09em;
      color: #74b9ff;
      margin-bottom: 1rem;
    }

    /* ── Code Panel ────────────────────────────────────────── */
    .code-panel {
      background: #0d1117;
      border-radius: 12px;
      padding: 1.25rem;
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      line-height: 2;
    }

    .kw  { color: #a29bfe; }
    .key { color: #74b9ff; }
    .str { color: #55efc4; }
    .num { color: #fdcb6e; }
    .boo { color: #fd79a8; }
    .dim { color: #636e72; }

    /* ── Display Card ──────────────────────────────────────── */
    .product-card {
      background: #16213e;
      border: 2px solid #6c5ce7;
      border-radius: 16px;
      overflow: hidden;
    }

    .product-card .card-img {
      background: linear-gradient(135deg, #6c5ce7, #a29bfe);
      height: 100px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 3rem;
    }

    .card-body { padding: 1.25rem; }

    .card-category {
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #a29bfe;
      margin-bottom: 0.35rem;
    }

    .card-title {
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
    }

    .card-price {
      font-size: 1.4rem;
      font-weight: 800;
      color: #55efc4;
    }

    .card-stock {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.2rem 0.55rem;
      border-radius: 100px;
      margin-top: 0.5rem;
    }

    .in-stock    { background: rgba(0,184,148,0.15); color: #00b894; }
    .out-of-stock { background: rgba(214,48,49,0.15); color: #d63031; }

    .prop-list {
      margin-top: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }

    .prop-row {
      display: flex;
      justify-content: space-between;
      font-size: 0.8rem;
      padding: 0.3rem 0;
      border-bottom: 1px solid #2d3561;
    }

    .prop-row:last-child { border-bottom: none; }
    .prop-key   { color: #74b9ff; font-family: 'Courier New', monospace; }
    .prop-value { color: #eee; }
    .prop-type  { color: #636e72; font-size: 0.72rem; }
  </style>
</head>
<body>

  <div>
    <h2>JavaScript Object</h2>
    <div class="code-panel">
      <span class="kw">const</span> product = {<br>
      &nbsp;&nbsp;<span class="key">id</span>:       <span class="num">1</span>,<br>
      &nbsp;&nbsp;<span class="key">name</span>:     <span class="str">'Wireless Headphones'</span>,<br>
      &nbsp;&nbsp;<span class="key">price</span>:    <span class="num">79.99</span>,<br>
      &nbsp;&nbsp;<span class="key">category</span>: <span class="str">'Electronics'</span>,<br>
      &nbsp;&nbsp;<span class="key">emoji</span>:    <span class="str">'🎧'</span>,<br>
      &nbsp;&nbsp;<span class="key">inStock</span>:  <span class="boo">true</span><br>
      };<br><br>
      <span class="dim">// Dot notation reads any property</span><br>
      product.<span class="key">name</span>      <span class="dim">→ 'Wireless Headphones'</span><br>
      product.<span class="key">price</span>     <span class="dim">→ 79.99</span><br>
      product.<span class="key">inStock</span>   <span class="dim">→ true</span>
    </div>
  </div>

  <div>
    <h2>Rendered Card</h2>
    <div class="product-card" id="card"></div>
  </div>

  <script>
    // ── The object ────────────────────────────────────────────
    const product = {
      id:       1,
      name:     'Wireless Headphones',
      price:    79.99,
      category: 'Electronics',
      emoji:    '🎧',
      inStock:  true
    };

    // ── Render the card using dot notation ────────────────────
    const stockClass   = product.inStock ? 'in-stock'     : 'out-of-stock';
    const stockLabel   = product.inStock ? 'In Stock'     : 'Out of Stock';

    document.querySelector('#card').innerHTML = `
      <div class="card-img">${product.emoji}</div>
      <div class="card-body">
        <p class="card-category">${product.category}</p>
        <h3 class="card-title">${product.name}</h3>
        <p class="card-price">$${product.price.toFixed(2)}</p>
        <span class="card-stock ${stockClass}">${stockLabel}</span>
        <div class="prop-list">
          <div class="prop-row">
            <span class="prop-key">product.id</span>
            <span class="prop-value">${product.id}</span>
            <span class="prop-type">number</span>
          </div>
          <div class="prop-row">
            <span class="prop-key">product.name</span>
            <span class="prop-value">${product.name}</span>
            <span class="prop-type">string</span>
          </div>
          <div class="prop-row">
            <span class="prop-key">product.price</span>
            <span class="prop-value">$${product.price.toFixed(2)}</span>
            <span class="prop-type">number</span>
          </div>
          <div class="prop-row">
            <span class="prop-key">product.inStock</span>
            <span class="prop-value">${product.inStock}</span>
            <span class="prop-type">boolean</span>
          </div>
        </div>
      </div>
    `;
  </script>

</body>
</html>
```

---

## CodePen 2 — Product Gallery

**Placement:** After the "Rendering Arrays of Objects as Cards" section.
**Demonstrates:** Array of 8 objects → `renderProducts()` function → styled flexbox card grid. Each card shows name, price (`.toFixed(2)`), category badge, and emoji.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Gallery</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      padding: 2rem;
      max-width: 900px;
      margin: 0 auto;
    }

    .page-header {
      margin-bottom: 1.5rem;
    }

    .page-header h1 { font-size: 1.3rem; color: #a29bfe; }
    .page-header p  { font-size: 0.82rem; opacity: 0.5; margin-top: 0.25rem; }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 1rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 14px;
      overflow: hidden;
      transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
      cursor: default;
    }

    .card:hover {
      transform: translateY(-4px);
      border-color: #6c5ce7;
      box-shadow: 0 10px 30px rgba(108,92,231,0.2);
    }

    .card-thumb {
      height: 100px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.5rem;
    }

    .card-body { padding: 1rem; }

    .badge {
      display: inline-block;
      background: rgba(108,92,231,0.15);
      color: #a29bfe;
      font-size: 0.65rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      padding: 0.15rem 0.5rem;
      border-radius: 100px;
      margin-bottom: 0.4rem;
    }

    .card-title {
      font-size: 0.92rem;
      font-weight: 700;
      margin-bottom: 0.35rem;
      line-height: 1.3;
    }

    .card-price {
      font-size: 1.05rem;
      font-weight: 800;
      color: #55efc4;
    }
  </style>
</head>
<body>

  <div class="page-header">
    <h1>Product Gallery</h1>
    <p>Array of 8 objects → renderProducts() → styled card grid</p>
  </div>

  <div class="grid" id="grid"></div>

  <script>
    // ── Array of objects — each item is one product record ────
    const products = [
      { id: 1, emoji: '🎧', name: 'Wireless Headphones', price: 79.99,  category: 'Electronics' },
      { id: 2, emoji: '👟', name: 'Running Shoes',       price: 119.00, category: 'Footwear'    },
      { id: 3, emoji: '☕', name: 'Ceramic Mug Set',     price: 24.99,  category: 'Kitchen'     },
      { id: 4, emoji: '🧘', name: 'Yoga Mat',            price: 38.50,  category: 'Fitness'     },
      { id: 5, emoji: '📚', name: 'Design Handbook',     price: 45.00,  category: 'Books'       },
      { id: 6, emoji: '🕯️', name: 'Soy Candle Set',      price: 32.00,  category: 'Home'        },
      { id: 7, emoji: '🎒', name: 'Minimalist Backpack', price: 89.95,  category: 'Accessories' },
      { id: 8, emoji: '🌱', name: 'Indoor Plant Kit',    price: 29.99,  category: 'Home'        }
    ];

    // ── renderProducts — maps objects to HTML cards ───────────
    function renderProducts(items) {
      const grid = document.querySelector('#grid');

      if (items.length === 0) {
        grid.innerHTML = '<p style="opacity:.4;text-align:center;padding:2rem;grid-column:1/-1;">No products found.</p>';
        return;
      }

      grid.innerHTML = items.map(product => `
        <div class="card" data-id="${product.id}">
          <div class="card-thumb" style="background: hsl(${product.id * 37 + 200}, 40%, 18%);">
            ${product.emoji}
          </div>
          <div class="card-body">
            <span class="badge">${product.category}</span>
            <h3 class="card-title">${product.name}</h3>
            <p class="card-price">$${product.price.toFixed(2)}</p>
          </div>
        </div>
      `).join('');
    }

    renderProducts(products);
  </script>

</body>
</html>
```

---

## CodePen 3 — Sort Buttons

**Placement:** After the "Sorting Arrays" section.
**Demonstrates:** Three sort buttons that re-sort the array (with spread to avoid mutation) and call `renderProducts()`. Shows `sort((a,b) => a.price - b.price)` and `localeCompare()`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sort Buttons</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      padding: 2rem;
      max-width: 860px;
      margin: 0 auto;
    }

    h1 { font-size: 1.2rem; color: #a29bfe; margin-bottom: 1.5rem; }

    .sort-bar {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-bottom: 1.5rem;
      align-items: center;
    }

    .sort-label {
      font-size: 0.75rem;
      opacity: 0.5;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      margin-right: 0.25rem;
    }

    .sort-btn {
      padding: 0.4rem 1rem;
      background: transparent;
      border: 2px solid #2d3561;
      border-radius: 8px;
      color: #aaa;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: border-color 0.2s, color 0.2s, background 0.2s;
    }

    .sort-btn.active {
      background: #6c5ce7;
      border-color: #6c5ce7;
      color: #fff;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 0.85rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 12px;
      padding: 1rem;
      transition: border-color 0.2s;
    }

    .card:hover { border-color: #6c5ce7; }

    .card-emoji { font-size: 1.5rem; margin-bottom: 0.5rem; }
    .card-title { font-size: 0.9rem; font-weight: 700; margin-bottom: 0.25rem; }

    .card-price {
      font-size: 1rem;
      font-weight: 800;
      color: #55efc4;
      margin-bottom: 0.2rem;
    }

    .badge {
      font-size: 0.65rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #a29bfe;
      background: rgba(108,92,231,0.12);
      padding: 0.12rem 0.45rem;
      border-radius: 100px;
    }
  </style>
</head>
<body>

  <h1>Sort Buttons Demo</h1>

  <div class="sort-bar">
    <span class="sort-label">Sort by:</span>
    <button class="sort-btn active" id="sort-default">Default</button>
    <button class="sort-btn" id="sort-price-asc">Price ↑</button>
    <button class="sort-btn" id="sort-price-desc">Price ↓</button>
    <button class="sort-btn" id="sort-name">Name A–Z</button>
  </div>

  <div class="grid" id="grid"></div>

  <script>
    const products = [
      { id: 1, emoji: '🎧', name: 'Wireless Headphones', price: 79.99,  category: 'Electronics' },
      { id: 2, emoji: '👟', name: 'Running Shoes',       price: 119.00, category: 'Footwear'    },
      { id: 3, emoji: '☕', name: 'Ceramic Mug Set',     price: 24.99,  category: 'Kitchen'     },
      { id: 4, emoji: '🧘', name: 'Yoga Mat',            price: 38.50,  category: 'Fitness'     },
      { id: 5, emoji: '📚', name: 'Design Handbook',     price: 45.00,  category: 'Books'       },
      { id: 6, emoji: '🕯️', name: 'Soy Candle Set',      price: 32.00,  category: 'Home'        }
    ];

    function renderProducts(items) {
      document.querySelector('#grid').innerHTML = items.map(p => `
        <div class="card" data-id="${p.id}">
          <p class="card-emoji">${p.emoji}</p>
          <h3 class="card-title">${p.name}</h3>
          <p class="card-price">$${p.price.toFixed(2)}</p>
          <span class="badge">${p.category}</span>
        </div>
      `).join('');
    }

    function setActive(id) {
      document.querySelectorAll('.sort-btn').forEach(b => b.classList.remove('active'));
      document.querySelector('#' + id).classList.add('active');
    }

    // Default order
    document.querySelector('#sort-default').addEventListener('click', function() {
      setActive('sort-default');
      renderProducts(products);
    });

    // Price low → high — sort a COPY with spread to protect original
    document.querySelector('#sort-price-asc').addEventListener('click', function() {
      setActive('sort-price-asc');
      const sorted = [...products].sort((a, b) => a.price - b.price);
      renderProducts(sorted);
    });

    // Price high → low
    document.querySelector('#sort-price-desc').addEventListener('click', function() {
      setActive('sort-price-desc');
      const sorted = [...products].sort((a, b) => b.price - a.price);
      renderProducts(sorted);
    });

    // Name A–Z — localeCompare handles alphabetical correctly
    document.querySelector('#sort-name').addEventListener('click', function() {
      setActive('sort-name');
      const sorted = [...products].sort((a, b) => a.name.localeCompare(b.name));
      renderProducts(sorted);
    });

    renderProducts(products);
  </script>

</body>
</html>
```

---

## CodePen 4 — Card Click to Detail Panel

**Placement:** After the "Connecting Cards to Data: the data-id Pattern" section.
**Demonstrates:** Event delegation on the container, `event.target.closest('.card')`, reading `dataset.id`, `find()` to locate the matching object, updating a detail panel with the full object data.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Card Click Detail</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: grid;
      grid-template-columns: 1fr 300px;
      gap: 2rem;
      padding: 2rem;
    }

    h2 {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #74b9ff;
      margin-bottom: 1rem;
    }

    /* ── Card grid ────────────────────────────────────────── */
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
      gap: 0.85rem;
      align-content: start;
    }

    .card {
      background: #16213e;
      border: 2px solid #2d3561;
      border-radius: 12px;
      padding: 1rem;
      cursor: pointer;
      transition: border-color 0.2s, transform 0.2s, box-shadow 0.2s;
    }

    .card:hover {
      border-color: #6c5ce7;
      transform: translateY(-3px);
    }

    .card.selected {
      border-color: #6c5ce7;
      box-shadow: 0 0 0 3px rgba(108,92,231,0.25);
    }

    .card-emoji { font-size: 1.75rem; margin-bottom: 0.4rem; }
    .card-name  { font-size: 0.85rem; font-weight: 700; }
    .card-price { font-size: 0.82rem; color: #55efc4; margin-top: 0.2rem; }

    /* ── Detail panel ─────────────────────────────────────── */
    .detail-panel {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 14px;
      padding: 1.5rem;
      align-self: start;
    }

    .detail-empty {
      text-align: center;
      opacity: 0.3;
      font-size: 0.85rem;
      padding: 2rem 0;
    }

    .detail-emoji { font-size: 3rem; margin-bottom: 0.75rem; text-align: center; }

    .detail-name {
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
      text-align: center;
    }

    .detail-price {
      font-size: 1.4rem;
      font-weight: 800;
      color: #55efc4;
      text-align: center;
      margin-bottom: 1rem;
    }

    .detail-row {
      display: flex;
      justify-content: space-between;
      font-size: 0.82rem;
      padding: 0.45rem 0;
      border-bottom: 1px solid #2d3561;
    }

    .detail-row:last-child { border-bottom: none; }
    .detail-key   { color: #74b9ff; font-family: 'Courier New', monospace; font-size: 0.75rem; }
    .detail-value { color: #eee; }
  </style>
</head>
<body>

  <div>
    <h2>Click a Card</h2>
    <div class="grid" id="grid"></div>
  </div>

  <div class="detail-panel">
    <h2>Product Detail</h2>
    <div id="detail">
      <p class="detail-empty">Click any card to see its full details here.</p>
    </div>
  </div>

  <script>
    const products = [
      { id: 1, emoji: '🎧', name: 'Wireless Headphones', price: 79.99,  category: 'Electronics', inStock: true,  rating: 4.8 },
      { id: 2, emoji: '👟', name: 'Running Shoes',       price: 119.00, category: 'Footwear',    inStock: true,  rating: 4.6 },
      { id: 3, emoji: '☕', name: 'Ceramic Mug Set',     price: 24.99,  category: 'Kitchen',     inStock: false, rating: 4.9 },
      { id: 4, emoji: '🧘', name: 'Yoga Mat',            price: 38.50,  category: 'Fitness',     inStock: true,  rating: 4.7 },
      { id: 5, emoji: '📚', name: 'Design Handbook',     price: 45.00,  category: 'Books',       inStock: true,  rating: 4.5 },
      { id: 6, emoji: '🕯️', name: 'Soy Candle Set',      price: 32.00,  category: 'Home',        inStock: false, rating: 4.3 }
    ];

    const grid   = document.querySelector('#grid');
    const detail = document.querySelector('#detail');

    function renderProducts(items) {
      grid.innerHTML = items.map(p => `
        <div class="card" data-id="${p.id}">
          <p class="card-emoji">${p.emoji}</p>
          <p class="card-name">${p.name}</p>
          <p class="card-price">$${p.price.toFixed(2)}</p>
        </div>
      `).join('');
    }

    function showDetail(product) {
      const stockText  = product.inStock ? '✓ In Stock'     : '✗ Out of Stock';
      const stockColor = product.inStock ? 'color:#00b894;' : 'color:#d63031;';
      const stars = '★'.repeat(Math.floor(product.rating)) + '☆'.repeat(5 - Math.floor(product.rating));

      detail.innerHTML = `
        <p class="detail-emoji">${product.emoji}</p>
        <p class="detail-name">${product.name}</p>
        <p class="detail-price">$${product.price.toFixed(2)}</p>
        <div>
          <div class="detail-row">
            <span class="detail-key">id</span>
            <span class="detail-value">${product.id}</span>
          </div>
          <div class="detail-row">
            <span class="detail-key">category</span>
            <span class="detail-value">${product.category}</span>
          </div>
          <div class="detail-row">
            <span class="detail-key">inStock</span>
            <span class="detail-value" style="${stockColor}">${stockText}</span>
          </div>
          <div class="detail-row">
            <span class="detail-key">rating</span>
            <span class="detail-value" style="color:#fdcb6e;">${stars} ${product.rating}</span>
          </div>
        </div>
      `;
    }

    // Event delegation — one listener handles ALL card clicks
    grid.addEventListener('click', function(event) {
      const card = event.target.closest('.card');
      if (!card) return;

      // Highlight selected card
      document.querySelectorAll('.card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');

      // Convert string id to number, find the matching object
      const id      = Number(card.dataset.id);
      const product = products.find(p => p.id === id);

      if (product) showDetail(product);
    });

    renderProducts(products);
  </script>

</body>
</html>
```

---

## CodePen 5 — Build Your Collection

**Placement:** After the "Building the Object" section.
**Demonstrates:** A form that creates new objects from input values and pushes them to the array, then re-renders. Shows form → object → array → `renderProducts()` loop.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Build Your Collection</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
      padding: 2rem;
      align-items: start;
    }

    h2 { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.08em; color: #74b9ff; margin-bottom: 1rem; }

    /* ── Form ─────────────────────────────────────────────── */
    .form-panel {
      background: #16213e;
      border-radius: 14px;
      padding: 1.5rem;
    }

    .field { margin-bottom: 1rem; }

    label {
      display: block;
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      opacity: 0.55;
      margin-bottom: 0.35rem;
    }

    input, select {
      width: 100%;
      padding: 0.55rem 0.75rem;
      background: #0d1117;
      border: 1px solid #2d3561;
      border-radius: 8px;
      color: #eee;
      font-size: 0.9rem;
      font-family: inherit;
      outline: none;
    }

    input:focus, select:focus { border-color: #6c5ce7; }
    input::placeholder { opacity: 0.35; }

    .submit-btn {
      width: 100%;
      padding: 0.65rem;
      background: #6c5ce7;
      color: #fff;
      border: none;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
    }

    /* ── Gallery ──────────────────────────────────────────── */
    .gallery-col h2 { margin-bottom: 0.5rem; }

    .count { font-size: 0.78rem; color: #636e72; margin-bottom: 1rem; }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(175px, 1fr));
      gap: 0.85rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 12px;
      padding: 1rem;
      animation: appear 0.2s ease;
      transition: border-color 0.2s;
    }

    .card:hover { border-color: #6c5ce7; }

    @keyframes appear {
      from { opacity: 0; transform: scale(0.92); }
      to   { opacity: 1; transform: scale(1); }
    }

    .card-emoji { font-size: 1.75rem; margin-bottom: 0.4rem; }
    .card-name  { font-size: 0.88rem; font-weight: 700; margin-bottom: 0.2rem; }
    .card-price { font-size: 0.95rem; font-weight: 800; color: #55efc4; }

    .card-cat {
      display: inline-block;
      font-size: 0.65rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #a29bfe;
      background: rgba(108,92,231,0.12);
      padding: 0.12rem 0.45rem;
      border-radius: 100px;
      margin-top: 0.3rem;
    }

    .empty-state {
      grid-column: 1 / -1;
      text-align: center;
      opacity: 0.3;
      font-size: 0.85rem;
      padding: 2rem;
    }
  </style>
</head>
<body>

  <div class="form-panel">
    <h2>Add a Product</h2>
    <form id="add-form">
      <div class="field">
        <label>Emoji</label>
        <input type="text" id="emoji" placeholder="🎁" maxlength="2" value="🎁">
      </div>
      <div class="field">
        <label>Product Name</label>
        <input type="text" id="name" placeholder="e.g. Leather Wallet" maxlength="30">
      </div>
      <div class="field">
        <label>Price ($)</label>
        <input type="number" id="price" placeholder="29.99" min="0" step="0.01">
      </div>
      <div class="field">
        <label>Category</label>
        <select id="category">
          <option>Electronics</option>
          <option>Footwear</option>
          <option>Kitchen</option>
          <option>Fitness</option>
          <option>Books</option>
          <option>Home</option>
          <option>Accessories</option>
        </select>
      </div>
      <button type="submit" class="submit-btn">+ Add to Gallery</button>
    </form>
  </div>

  <div class="gallery-col">
    <h2>Your Collection</h2>
    <p class="count" id="count"></p>
    <div class="grid" id="grid"></div>
  </div>

  <script>
    // Start with a few items
    let products = [
      { id: 1, emoji: '🎧', name: 'Wireless Headphones', price: 79.99, category: 'Electronics' },
      { id: 2, emoji: '☕', name: 'Ceramic Mug Set',     price: 24.99, category: 'Kitchen'     }
    ];

    let nextId = products.length + 1;

    function renderProducts(items) {
      const grid = document.querySelector('#grid');

      if (items.length === 0) {
        grid.innerHTML = '<p class="empty-state">No products yet — add one using the form.</p>';
        document.querySelector('#count').textContent = '';
        return;
      }

      grid.innerHTML = items.map(p => `
        <div class="card" data-id="${p.id}">
          <p class="card-emoji">${p.emoji}</p>
          <p class="card-name">${p.name}</p>
          <p class="card-price">$${p.price.toFixed(2)}</p>
          <span class="card-cat">${p.category}</span>
        </div>
      `).join('');

      document.querySelector('#count').textContent = items.length + ' items in collection';
    }

    document.querySelector('#add-form').addEventListener('submit', function(event) {
      event.preventDefault();

      const name  = document.querySelector('#name').value.trim();
      const price = Number(document.querySelector('#price').value);

      if (!name || !price) return;

      // Build a new object from form values
      const newProduct = {
        id:       nextId,
        emoji:    document.querySelector('#emoji').value || '📦',
        name:     name,
        price:    price,
        category: document.querySelector('#category').value
      };

      // Push to the array and re-render
      products.push(newProduct);
      nextId = nextId + 1;
      renderProducts(products);

      // Clear the inputs
      document.querySelector('#name').value  = '';
      document.querySelector('#price').value = '';
      document.querySelector('#emoji').value = '🎁';
      document.querySelector('#name').focus();
    });

    renderProducts(products);
  </script>

</body>
</html>
```
