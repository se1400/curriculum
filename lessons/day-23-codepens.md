# Day 23 — CodePen Examples
## Filter, Search, Find: Array Iteration Methods and Live Search

---

## CodePen 1 — map, filter, find Basics

**Placement:** After the "find" section.
**Demonstrates:** All four methods in isolation — an array of numbers with buttons showing each method's result. Builds understanding before applying to objects.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Array Methods Basics</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      padding: 2rem;
      max-width: 700px;
      margin: 0 auto;
    }

    h1 { font-size: 1.2rem; color: #a29bfe; margin-bottom: 1.5rem; }

    .method-card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 12px;
      padding: 1.25rem;
      margin-bottom: 1rem;
    }

    .method-card.active { border-color: #6c5ce7; }

    .method-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
    }

    .method-name {
      font-family: 'Courier New', monospace;
      font-size: 0.9rem;
      font-weight: 700;
      color: #74b9ff;
    }

    .method-desc {
      font-size: 0.78rem;
      opacity: 0.55;
    }

    .run-btn {
      padding: 0.35rem 0.9rem;
      background: #6c5ce7;
      color: #fff;
      border: none;
      border-radius: 6px;
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
    }

    .code-example {
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      background: #0d1117;
      border-radius: 6px;
      padding: 0.6rem 0.85rem;
      color: #636e72;
      margin-bottom: 0.75rem;
    }

    .kw  { color: #a29bfe; }
    .fn  { color: #74b9ff; }
    .hl  { color: #55efc4; }
    .arr { color: #fdcb6e; }

    .result-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-size: 0.85rem;
    }

    .result-label { opacity: 0.5; white-space: nowrap; }
    .result-value { font-family: 'Courier New', monospace; color: #a29bfe; font-size: 0.82rem; }

    .original-display {
      background: #0d1117;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.82rem;
      margin-bottom: 1.5rem;
      color: #636e72;
    }

    .original-display .arr { color: #fdcb6e; }
  </style>
</head>
<body>

  <h1>Array Iteration Methods</h1>

  <div class="original-display">
    <span class="kw">const</span> numbers = [<span class="arr">3, 7, 2, 9, 5, 1, 8, 4, 6</span>];
  </div>

  <!-- forEach -->
  <div class="method-card" id="foreach-card">
    <div class="method-header">
      <div>
        <p class="method-name">forEach()</p>
        <p class="method-desc">Run a function for each item. Returns nothing.</p>
      </div>
      <button class="run-btn" onclick="runForEach()">Run</button>
    </div>
    <div class="code-example">
      numbers.<span class="fn">forEach</span>(n => console.log(n * 2))
    </div>
    <div class="result-row">
      <span class="result-label">Console output:</span>
      <span class="result-value" id="foreach-result">—</span>
    </div>
  </div>

  <!-- map -->
  <div class="method-card" id="map-card">
    <div class="method-header">
      <div>
        <p class="method-name">map()</p>
        <p class="method-desc">Transform each item. Returns a NEW array of the same length.</p>
      </div>
      <button class="run-btn" onclick="runMap()">Run</button>
    </div>
    <div class="code-example">
      <span class="kw">const</span> doubled = numbers.<span class="fn">map</span>(n => n * 2)
    </div>
    <div class="result-row">
      <span class="result-label">doubled =</span>
      <span class="result-value" id="map-result">—</span>
    </div>
  </div>

  <!-- filter -->
  <div class="method-card" id="filter-card">
    <div class="method-header">
      <div>
        <p class="method-name">filter()</p>
        <p class="method-desc">Keep items that pass the test. Returns a NEW, shorter array.</p>
      </div>
      <button class="run-btn" onclick="runFilter()">Run</button>
    </div>
    <div class="code-example">
      <span class="kw">const</span> evens = numbers.<span class="fn">filter</span>(n => n % 2 === 0)
    </div>
    <div class="result-row">
      <span class="result-label">evens =</span>
      <span class="result-value" id="filter-result">—</span>
    </div>
  </div>

  <!-- find -->
  <div class="method-card" id="find-card">
    <div class="method-header">
      <div>
        <p class="method-name">find()</p>
        <p class="method-desc">Returns the FIRST item that passes. Returns the item itself, not an array.</p>
      </div>
      <button class="run-btn" onclick="runFind()">Run</button>
    </div>
    <div class="code-example">
      <span class="kw">const</span> firstBig = numbers.<span class="fn">find</span>(n => n > 7)
    </div>
    <div class="result-row">
      <span class="result-label">firstBig =</span>
      <span class="result-value" id="find-result">—</span>
    </div>
  </div>

  <script>
    const numbers = [3, 7, 2, 9, 5, 1, 8, 4, 6];

    function runForEach() {
      const results = [];
      numbers.forEach(n => results.push(n * 2));
      document.querySelector('#foreach-result').textContent = '[' + results.join(', ') + ']';
      document.querySelector('#foreach-card').classList.add('active');
    }

    function runMap() {
      const doubled = numbers.map(n => n * 2);
      document.querySelector('#map-result').textContent = '[' + doubled.join(', ') + ']';
      document.querySelector('#map-card').classList.add('active');
    }

    function runFilter() {
      const evens = numbers.filter(n => n % 2 === 0);
      document.querySelector('#filter-result').textContent = '[' + evens.join(', ') + ']';
      document.querySelector('#filter-card').classList.add('active');
    }

    function runFind() {
      const firstBig = numbers.find(n => n > 7);
      document.querySelector('#find-result').textContent = firstBig;
      document.querySelector('#find-card').classList.add('active');
    }
  </script>

</body>
</html>
```

---

## CodePen 2 — Category Filter Gallery

**Placement:** After the "Category Filter Buttons" section.
**Demonstrates:** Filter buttons + `products.filter()` + `renderProducts()`. Active button state managed with `forEach`. Click a category → only matching cards show.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Category Filter</title>
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

    .filter-bar {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-bottom: 1.5rem;
      align-items: center;
    }

    .filter-btn {
      padding: 0.4rem 1rem;
      background: transparent;
      border: 2px solid #2d3561;
      border-radius: 100px;
      color: #aaa;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .filter-btn.active {
      background: #6c5ce7;
      border-color: #6c5ce7;
      color: #fff;
    }

    .count { font-size: 0.78rem; color: #636e72; margin-left: auto; }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
      gap: 0.9rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 12px;
      padding: 1.1rem;
      transition: transform 0.2s, border-color 0.2s;
    }

    .card:hover { transform: translateY(-3px); border-color: #6c5ce7; }

    .card-emoji { font-size: 1.75rem; margin-bottom: 0.4rem; }
    .card-title { font-size: 0.9rem; font-weight: 700; margin-bottom: 0.2rem; }
    .card-price { font-size: 0.95rem; font-weight: 800; color: #55efc4; margin-bottom: 0.3rem; }

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

    .empty-state {
      grid-column: 1 / -1;
      text-align: center;
      opacity: 0.35;
      padding: 3rem;
      font-size: 0.9rem;
    }
  </style>
</head>
<body>

  <h1>Product Gallery</h1>

  <div class="filter-bar">
    <button class="filter-btn active" data-category="all">All</button>
    <button class="filter-btn" data-category="Electronics">Electronics</button>
    <button class="filter-btn" data-category="Footwear">Footwear</button>
    <button class="filter-btn" data-category="Kitchen">Kitchen</button>
    <button class="filter-btn" data-category="Fitness">Fitness</button>
    <button class="filter-btn" data-category="Home">Home</button>
    <span class="count" id="count"></span>
  </div>

  <div class="grid" id="grid"></div>

  <script>
    const products = [
      { id: 1, emoji: '🎧', name: 'Wireless Headphones', price: 79.99,  category: 'Electronics' },
      { id: 2, emoji: '👟', name: 'Running Shoes',       price: 119.00, category: 'Footwear'    },
      { id: 3, emoji: '☕', name: 'Ceramic Mug Set',     price: 24.99,  category: 'Kitchen'     },
      { id: 4, emoji: '🧘', name: 'Yoga Mat',            price: 38.50,  category: 'Fitness'     },
      { id: 5, emoji: '📱', name: 'Phone Stand',         price: 19.99,  category: 'Electronics' },
      { id: 6, emoji: '🕯️', name: 'Soy Candle Set',      price: 32.00,  category: 'Home'        },
      { id: 7, emoji: '👟', name: 'Casual Sneakers',     price: 65.00,  category: 'Footwear'    },
      { id: 8, emoji: '🌱', name: 'Indoor Plant Kit',    price: 29.99,  category: 'Home'        },
      { id: 9, emoji: '🍳', name: 'Cast Iron Pan',       price: 54.99,  category: 'Kitchen'     }
    ];

    let activeCategory = 'all';

    function renderProducts(items) {
      const grid = document.querySelector('#grid');

      if (items.length === 0) {
        grid.innerHTML = '<p class="empty-state">No products in this category.</p>';
        document.querySelector('#count').textContent = '0 items';
        return;
      }

      grid.innerHTML = items.map(p => `
        <div class="card" data-id="${p.id}">
          <p class="card-emoji">${p.emoji}</p>
          <h3 class="card-title">${p.name}</h3>
          <p class="card-price">$${p.price.toFixed(2)}</p>
          <span class="badge">${p.category}</span>
        </div>
      `).join('');

      document.querySelector('#count').textContent = items.length + ' item' + (items.length !== 1 ? 's' : '');
    }

    function filterAndRender() {
      // filter() keeps only items matching the active category
      const results = activeCategory === 'all'
        ? products
        : products.filter(p => p.category === activeCategory);

      renderProducts(results);
    }

    const filterBtns = document.querySelectorAll('.filter-btn');

    filterBtns.forEach(function(btn) {
      btn.addEventListener('click', function() {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeCategory = btn.dataset.category;
        filterAndRender();
      });
    });

    filterAndRender();
  </script>

</body>
</html>
```

---

## CodePen 3 — Live Search

**Placement:** After the "Live Search" section.
**Demonstrates:** `addEventListener('input')` + `filter()` on name with `.toLowerCase().includes()`. Results update on every keystroke. Empty state shows clearly.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Live Search</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      padding: 2rem;
      max-width: 760px;
      margin: 0 auto;
    }

    h1 { font-size: 1.2rem; color: #a29bfe; margin-bottom: 0.35rem; }

    .subtitle { font-size: 0.82rem; opacity: 0.5; margin-bottom: 1.5rem; }

    .search-wrap {
      position: relative;
      margin-bottom: 1.25rem;
    }

    .search-icon {
      position: absolute;
      left: 0.9rem;
      top: 50%;
      transform: translateY(-50%);
      opacity: 0.4;
      font-size: 1rem;
    }

    #search-input {
      width: 100%;
      padding: 0.7rem 1rem 0.7rem 2.5rem;
      background: #16213e;
      border: 2px solid #2d3561;
      border-radius: 10px;
      color: #eee;
      font-size: 1rem;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s;
    }

    #search-input:focus { border-color: #6c5ce7; }
    #search-input::placeholder { opacity: 0.35; }

    .results-meta {
      font-size: 0.78rem;
      color: #636e72;
      margin-bottom: 1rem;
      min-height: 1.2rem;
    }

    .results-meta .hl { color: #6c5ce7; font-weight: 700; }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 0.85rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 12px;
      padding: 1.1rem;
      transition: border-color 0.2s, transform 0.2s;
    }

    .card:hover { transform: translateY(-3px); border-color: #6c5ce7; }

    .card-emoji { font-size: 1.75rem; margin-bottom: 0.4rem; }
    .card-title { font-size: 0.9rem; font-weight: 700; margin-bottom: 0.2rem; }
    .card-price { font-size: 0.95rem; font-weight: 800; color: #55efc4; margin-bottom: 0.3rem; }

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

    /* Highlight the matching text in card titles */
    .match { background: rgba(108,92,231,0.3); border-radius: 2px; }

    .empty-state {
      grid-column: 1 / -1;
      text-align: center;
      padding: 3rem;
      opacity: 0.35;
    }

    .empty-state p { font-size: 0.9rem; }
    .empty-state .query { color: #a29bfe; font-weight: 700; opacity: 1; }
  </style>
</head>
<body>

  <h1>Live Search</h1>
  <p class="subtitle">Results update on every keystroke using filter() + input event.</p>

  <div class="search-wrap">
    <span class="search-icon">&#128269;</span>
    <input type="text" id="search-input" placeholder="Search products…" autocomplete="off">
  </div>

  <p class="results-meta" id="meta"></p>
  <div class="grid" id="grid"></div>

  <script>
    const products = [
      { id: 1,  emoji: '🎧', name: 'Wireless Headphones', price: 79.99,  category: 'Electronics' },
      { id: 2,  emoji: '👟', name: 'Running Shoes',       price: 119.00, category: 'Footwear'    },
      { id: 3,  emoji: '☕', name: 'Ceramic Mug Set',     price: 24.99,  category: 'Kitchen'     },
      { id: 4,  emoji: '🧘', name: 'Yoga Mat',            price: 38.50,  category: 'Fitness'     },
      { id: 5,  emoji: '📚', name: 'Design Handbook',     price: 45.00,  category: 'Books'       },
      { id: 6,  emoji: '🕯️', name: 'Soy Candle Set',      price: 32.00,  category: 'Home'        },
      { id: 7,  emoji: '🎒', name: 'Minimalist Backpack', price: 89.95,  category: 'Accessories' },
      { id: 8,  emoji: '🌱', name: 'Indoor Plant Kit',    price: 29.99,  category: 'Home'        },
      { id: 9,  emoji: '🍳', name: 'Cast Iron Pan',       price: 54.99,  category: 'Kitchen'     },
      { id: 10, emoji: '📱', name: 'Wireless Charger',    price: 34.99,  category: 'Electronics' }
    ];

    let searchQuery = '';

    // Highlight matching text in a string
    function highlight(text, query) {
      if (!query) return text;
      const regex = new RegExp('(' + query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
      return text.replace(regex, '<mark class="match">$1</mark>');
    }

    function renderProducts(items, query) {
      const grid = document.querySelector('#grid');
      const meta = document.querySelector('#meta');

      if (items.length === 0) {
        grid.innerHTML = `
          <div class="empty-state">
            <p>No results for <span class="query">"${query}"</span></p>
            <p style="margin-top:.5rem;font-size:.8rem;">Try a different search term.</p>
          </div>`;
        meta.innerHTML = 'No results for <span class="hl">"' + query + '"</span>';
        return;
      }

      grid.innerHTML = items.map(p => `
        <div class="card" data-id="${p.id}">
          <p class="card-emoji">${p.emoji}</p>
          <h3 class="card-title">${highlight(p.name, query)}</h3>
          <p class="card-price">$${p.price.toFixed(2)}</p>
          <span class="badge">${p.category}</span>
        </div>
      `).join('');

      if (query) {
        meta.innerHTML = 'Found <span class="hl">' + items.length + '</span> result' +
          (items.length !== 1 ? 's' : '') + ' for <span class="hl">"' + query + '"</span>';
      } else {
        meta.textContent = 'Showing all ' + items.length + ' products';
      }
    }

    function filterAndRender() {
      // filter() keeps items whose name includes the search query
      const results = products.filter(p =>
        p.name.toLowerCase().includes(searchQuery)
      );
      renderProducts(results, searchQuery);
    }

    // 'input' event fires on every keystroke — perfect for live search
    document.querySelector('#search-input').addEventListener('input', function(event) {
      searchQuery = event.target.value.toLowerCase().trim();
      filterAndRender();
    });

    filterAndRender();
  </script>

</body>
</html>
```

---

## CodePen 4 — Filter + Search Combined

**Placement:** After the "Chaining filter() and map()" section.
**Demonstrates:** Category filters AND live search working together. Both conditions must pass. Shows the real-world pattern of composing filters.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Filter + Search Combined</title>
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

    .toolbar {
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
      align-items: center;
      margin-bottom: 1.25rem;
    }

    #search-input {
      padding: 0.5rem 0.9rem;
      background: #16213e;
      border: 2px solid #2d3561;
      border-radius: 8px;
      color: #eee;
      font-size: 0.85rem;
      font-family: inherit;
      outline: none;
      width: 200px;
      transition: border-color 0.2s;
    }

    #search-input:focus { border-color: #6c5ce7; }
    #search-input::placeholder { opacity: 0.35; }

    .filter-btn {
      padding: 0.4rem 0.9rem;
      background: transparent;
      border: 2px solid #2d3561;
      border-radius: 100px;
      color: #aaa;
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .filter-btn.active { background: #6c5ce7; border-color: #6c5ce7; color: #fff; }

    .meta {
      font-size: 0.78rem;
      color: #636e72;
      margin-bottom: 1rem;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(185px, 1fr));
      gap: 0.85rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 12px;
      padding: 1rem;
      transition: border-color 0.2s, transform 0.2s;
    }

    .card:hover { transform: translateY(-3px); border-color: #6c5ce7; }

    .card-emoji { font-size: 1.5rem; margin-bottom: 0.35rem; }
    .card-title { font-size: 0.88rem; font-weight: 700; margin-bottom: 0.2rem; }
    .card-price { font-size: 0.9rem; font-weight: 800; color: #55efc4; }

    .badge {
      display: inline-block;
      font-size: 0.62rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #a29bfe;
      background: rgba(108,92,231,0.12);
      padding: 0.1rem 0.4rem;
      border-radius: 100px;
      margin-top: 0.3rem;
    }

    .empty-state {
      grid-column: 1 / -1;
      text-align: center;
      opacity: 0.35;
      padding: 2.5rem;
      font-size: 0.88rem;
    }
  </style>
</head>
<body>

  <h1>Filter + Search Combined</h1>

  <div class="toolbar">
    <input type="text" id="search-input" placeholder="Search…">
    <button class="filter-btn active" data-category="all">All</button>
    <button class="filter-btn" data-category="Electronics">Electronics</button>
    <button class="filter-btn" data-category="Footwear">Footwear</button>
    <button class="filter-btn" data-category="Kitchen">Kitchen</button>
    <button class="filter-btn" data-category="Home">Home</button>
  </div>

  <p class="meta" id="meta"></p>
  <div class="grid" id="grid"></div>

  <script>
    const products = [
      { id: 1,  emoji: '🎧', name: 'Wireless Headphones', price: 79.99,  category: 'Electronics' },
      { id: 2,  emoji: '👟', name: 'Running Shoes',       price: 119.00, category: 'Footwear'    },
      { id: 3,  emoji: '☕', name: 'Ceramic Mug Set',     price: 24.99,  category: 'Kitchen'     },
      { id: 4,  emoji: '🧘', name: 'Yoga Mat',            price: 38.50,  category: 'Fitness'     },
      { id: 5,  emoji: '📱', name: 'Wireless Charger',    price: 34.99,  category: 'Electronics' },
      { id: 6,  emoji: '🕯️', name: 'Soy Candle Set',      price: 32.00,  category: 'Home'        },
      { id: 7,  emoji: '👟', name: 'Trail Running Shoes', price: 145.00, category: 'Footwear'    },
      { id: 8,  emoji: '🌱', name: 'Indoor Plant Kit',    price: 29.99,  category: 'Home'        },
      { id: 9,  emoji: '🍳', name: 'Cast Iron Pan',       price: 54.99,  category: 'Kitchen'     },
      { id: 10, emoji: '🎒', name: 'Laptop Backpack',     price: 89.95,  category: 'Electronics' }
    ];

    // State — stored outside handlers so filterAndRender() can access both
    let activeCategory = 'all';
    let searchQuery    = '';

    function renderProducts(items) {
      const grid = document.querySelector('#grid');
      const meta = document.querySelector('#meta');

      meta.textContent = 'Showing ' + items.length + ' of ' + products.length + ' products';

      if (items.length === 0) {
        grid.innerHTML = '<p class="empty-state">No products match your filters.</p>';
        return;
      }

      grid.innerHTML = items.map(p => `
        <div class="card" data-id="${p.id}">
          <p class="card-emoji">${p.emoji}</p>
          <h3 class="card-title">${p.name}</h3>
          <p class="card-price">$${p.price.toFixed(2)}</p>
          <span class="badge">${p.category}</span>
        </div>
      `).join('');
    }

    function filterAndRender() {
      // One filter() call with two conditions using &&
      const results = products.filter(function(p) {
        const matchesCategory = activeCategory === 'all' || p.category === activeCategory;
        const matchesSearch   = p.name.toLowerCase().includes(searchQuery);
        return matchesCategory && matchesSearch;
      });

      renderProducts(results);
    }

    // Category buttons
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(function(btn) {
      btn.addEventListener('click', function() {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeCategory = btn.dataset.category;
        filterAndRender();
      });
    });

    // Live search
    document.querySelector('#search-input').addEventListener('input', function(event) {
      searchQuery = event.target.value.toLowerCase().trim();
      filterAndRender();
    });

    filterAndRender();
  </script>

</body>
</html>
```

---

## CodePen 5 — Card Click → Modal with Event Delegation

**Placement:** After the "Event Delegation" section.
**Demonstrates:** One event listener on the container, `event.target.closest('.card')`, `find()` by `data-id`, opening a modal with full product details. Brings together Days 20, 22, and 23.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gallery with Modal</title>
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

    h1 { font-size: 1.2rem; color: #a29bfe; margin-bottom: 0.25rem; }
    .subtitle { font-size: 0.82rem; opacity: 0.5; margin-bottom: 1.5rem; }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 0.9rem;
    }

    .card {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 12px;
      padding: 1.1rem;
      cursor: pointer;
      transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    }

    .card:hover {
      transform: translateY(-4px);
      border-color: #6c5ce7;
      box-shadow: 0 8px 24px rgba(108,92,231,0.2);
    }

    .card-emoji { font-size: 1.75rem; margin-bottom: 0.4rem; }
    .card-title { font-size: 0.88rem; font-weight: 700; margin-bottom: 0.2rem; }
    .card-price { font-size: 0.92rem; font-weight: 800; color: #55efc4; }

    .click-hint {
      font-size: 0.65rem;
      opacity: 0.35;
      margin-top: 0.4rem;
    }

    /* ── Modal ────────────────────────────────────────────── */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.7);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s;
      z-index: 100;
    }

    .modal-overlay.open {
      opacity: 1;
      pointer-events: auto;
    }

    .modal {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 20px;
      padding: 2rem;
      max-width: 400px;
      width: 100%;
      transform: translateY(16px) scale(0.97);
      transition: transform 0.25s;
    }

    .modal-overlay.open .modal { transform: translateY(0) scale(1); }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 1.25rem;
    }

    .modal-emoji { font-size: 2.5rem; }

    .close-btn {
      background: none;
      border: none;
      color: #636e72;
      font-size: 1.3rem;
      cursor: pointer;
      padding: 0;
      line-height: 1;
    }

    .modal-name  { font-size: 1.2rem; font-weight: 700; margin-bottom: 0.25rem; }
    .modal-price { font-size: 1.5rem; font-weight: 800; color: #55efc4; margin-bottom: 1rem; }

    .detail-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
    }

    .detail-item {
      background: #0d1117;
      border-radius: 8px;
      padding: 0.65rem 0.85rem;
    }

    .detail-label { font-size: 0.68rem; opacity: 0.5; text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 0.2rem; }
    .detail-value { font-size: 0.9rem; font-weight: 600; }

    .stars { color: #fdcb6e; font-size: 0.9rem; }

    .stock-badge {
      display: inline-block;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 100px;
      width: 100%;
      text-align: center;
    }

    .in-stock    { background: rgba(0,184,148,0.15); color: #00b894; }
    .out-stock   { background: rgba(214,48,49,0.15);  color: #d63031; }
  </style>
</head>
<body>

  <h1>Gallery + Modal</h1>
  <p class="subtitle">Click any card — event delegation catches all clicks with one listener.</p>

  <div class="grid" id="grid"></div>

  <div class="modal-overlay" id="modal-overlay">
    <div class="modal" id="modal">
      <div class="modal-header">
        <span class="modal-emoji" id="modal-emoji"></span>
        <button class="close-btn" id="close-btn">&times;</button>
      </div>
      <h2 class="modal-name"  id="modal-name"></h2>
      <p  class="modal-price" id="modal-price"></p>
      <div class="detail-grid" id="modal-details"></div>
      <span class="stock-badge" id="modal-stock"></span>
    </div>
  </div>

  <script>
    const products = [
      { id: 1, emoji: '🎧', name: 'Wireless Headphones', price: 79.99,  category: 'Electronics', rating: 4.8, inStock: true  },
      { id: 2, emoji: '👟', name: 'Running Shoes',       price: 119.00, category: 'Footwear',    rating: 4.6, inStock: true  },
      { id: 3, emoji: '☕', name: 'Ceramic Mug Set',     price: 24.99,  category: 'Kitchen',     rating: 4.9, inStock: false },
      { id: 4, emoji: '🧘', name: 'Yoga Mat',            price: 38.50,  category: 'Fitness',     rating: 4.7, inStock: true  },
      { id: 5, emoji: '📚', name: 'Design Handbook',     price: 45.00,  category: 'Books',       rating: 4.5, inStock: true  },
      { id: 6, emoji: '🕯️', name: 'Soy Candle Set',      price: 32.00,  category: 'Home',        rating: 4.3, inStock: false },
      { id: 7, emoji: '🎒', name: 'Minimalist Backpack', price: 89.95,  category: 'Accessories', rating: 4.7, inStock: true  },
      { id: 8, emoji: '🌱', name: 'Indoor Plant Kit',    price: 29.99,  category: 'Home',        rating: 4.4, inStock: true  }
    ];

    const overlay = document.querySelector('#modal-overlay');

    function renderProducts(items) {
      document.querySelector('#grid').innerHTML = items.map(p => `
        <div class="card" data-id="${p.id}">
          <p class="card-emoji">${p.emoji}</p>
          <h3 class="card-title">${p.name}</h3>
          <p class="card-price">$${p.price.toFixed(2)}</p>
          <p class="click-hint">Click for details →</p>
        </div>
      `).join('');
    }

    function openModal(product) {
      const stars = '★'.repeat(Math.floor(product.rating)) + '☆'.repeat(5 - Math.floor(product.rating));

      document.querySelector('#modal-emoji').textContent = product.emoji;
      document.querySelector('#modal-name').textContent  = product.name;
      document.querySelector('#modal-price').textContent = '$' + product.price.toFixed(2);

      document.querySelector('#modal-details').innerHTML = `
        <div class="detail-item">
          <p class="detail-label">Category</p>
          <p class="detail-value">${product.category}</p>
        </div>
        <div class="detail-item">
          <p class="detail-label">Rating</p>
          <p class="detail-value"><span class="stars">${stars}</span> ${product.rating}</p>
        </div>
      `;

      const stockEl = document.querySelector('#modal-stock');
      if (product.inStock) {
        stockEl.textContent = '✓ In Stock';
        stockEl.className   = 'stock-badge in-stock';
      } else {
        stockEl.textContent = '✗ Out of Stock';
        stockEl.className   = 'stock-badge out-stock';
      }

      overlay.classList.add('open');
    }

    function closeModal() { overlay.classList.remove('open'); }

    // Event delegation — ONE listener handles ALL card clicks
    document.querySelector('#grid').addEventListener('click', function(event) {
      const card = event.target.closest('.card');
      if (!card) return;

      const id      = Number(card.dataset.id);
      const product = products.find(p => p.id === id);
      if (product) openModal(product);
    });

    document.querySelector('#close-btn').addEventListener('click', closeModal);
    overlay.addEventListener('click', function(event) {
      if (event.target === overlay) closeModal();
    });

    renderProducts(products);
  </script>

</body>
</html>
```
