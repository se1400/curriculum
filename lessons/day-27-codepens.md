# Day 27 — Array Iteration Methods — CodePens

---

## CODEPEN 1 — map() Card Renderer

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>map() Card Renderer</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1rem; }
    .controls { display: flex; gap: 0.75rem; justify-content: center; margin-bottom: 1.25rem; flex-wrap: wrap; }
    .btn {
      padding: 0.5rem 1.1rem; border: none; border-radius: 20px;
      font-size: 0.85rem; font-weight: 700; cursor: pointer; transition: all 0.2s;
    }
    .btn-shuffle { background: #4f46e5; color: #fff; }
    .btn-shuffle:hover { background: #4338ca; }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 1rem; max-width: 900px; margin: 0 auto 1.5rem;
    }
    .card {
      background: #fff; border-radius: 12px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.08);
      padding: 1rem; transition: transform 0.2s;
    }
    .card:hover { transform: translateY(-3px); }
    .card-name { font-weight: 700; font-size: 0.95rem; margin-bottom: 0.4rem; color: #1a1a2e; }
    .badge {
      display: inline-block; padding: 0.2rem 0.55rem; border-radius: 20px;
      font-size: 0.7rem; font-weight: 700; margin-bottom: 0.5rem;
    }
    .badge-audio  { background: #dcfce7; color: #166534; }
    .badge-tech   { background: #dbeafe; color: #1d4ed8; }
    .badge-office { background: #fef3c7; color: #92400e; }
    .badge-home   { background: #fce7f3; color: #9d174d; }
    .card-price { font-size: 1.1rem; font-weight: 800; color: #4f46e5; margin-bottom: 0.3rem; }
    .stars { color: #f59e0b; font-size: 0.85rem; }

    .code-panel {
      max-width: 900px; margin: 0 auto;
      background: #1e1e2e; border-radius: 12px; padding: 1rem 1.25rem;
    }
    .code-label { font-size: 0.72rem; color: #666; font-family: monospace; margin-bottom: 0.5rem; }
    .code-block { font-size: 0.8rem; color: #a9dc76; font-family: monospace; white-space: pre-wrap; line-height: 1.6; }
  </style>
</head>
<body>
  <h1>map() Card Renderer</h1>
  <p class="subtitle">The array drives the grid. <code>map()</code> renders every card.</p>

  <div class="controls">
    <button class="btn btn-shuffle" onclick="shuffle()">🔀 Shuffle Array</button>
  </div>

  <div class="grid" id="grid"></div>

  <div class="code-panel">
    <div class="code-label">// The map() call that generates this grid</div>
    <div class="code-block">grid.innerHTML = products.map(p => `
  &lt;div class="card"&gt;
    &lt;div class="card-name"&gt;${"{"}p.name{"}"}&lt;/div&gt;
    &lt;span class="badge badge-${"{"}p.category{"}"}"&gt;${"{"}p.category{"}"}&lt;/span&gt;
    &lt;div class="card-price"&gt;$${"{"}p.price.toFixed(2){"}"}&lt;/div&gt;
    &lt;div class="stars"&gt;${"{"}"★".repeat(p.rating) + "☆".repeat(5-p.rating){"}"}&lt;/div&gt;
  &lt;/div&gt;
`).join('');</div>
  </div>

  <script>
    const products = [
      { name: 'Wireless Headphones', price: 79.99,  category: 'audio',  rating: 4 },
      { name: 'USB-C Hub',           price: 34.99,  category: 'tech',   rating: 5 },
      { name: 'Notebook Set',        price: 12.99,  category: 'office', rating: 4 },
      { name: 'Smart Bulb Pack',     price: 24.99,  category: 'home',   rating: 3 },
      { name: 'Mechanical Keyboard', price: 129.99, category: 'tech',   rating: 5 },
      { name: 'Desk Organiser',      price: 19.99,  category: 'office', rating: 4 },
      { name: 'Portable Speaker',    price: 49.99,  category: 'audio',  rating: 4 },
      { name: 'LED Desk Lamp',       price: 39.99,  category: 'home',   rating: 3 },
      { name: 'Cable Organiser',     price: 9.99,   category: 'office', rating: 3 },
      { name: 'Earbuds Pro',         price: 89.99,  category: 'audio',  rating: 5 },
    ];

    function render(arr) {
      document.getElementById('grid').innerHTML = arr.map(p => `
        <div class="card">
          <div class="card-name">${p.name}</div>
          <span class="badge badge-${p.category}">${p.category}</span>
          <div class="card-price">$${p.price.toFixed(2)}</div>
          <div class="stars">${'★'.repeat(p.rating) + '☆'.repeat(5 - p.rating)}</div>
        </div>
      `).join('');
    }

    function shuffle() {
      const arr = [...products];
      for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }
      render(arr);
    }

    render(products);
  </script>
</body>
</html>
```

---

## CODEPEN 2 — filter() Category Toggle

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>filter() Category Toggle</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1rem; }

    .filter-bar {
      display: flex; flex-wrap: wrap; gap: 0.5rem;
      justify-content: center; margin-bottom: 0.5rem;
    }
    .filter-btn {
      padding: 0.45rem 1rem; border: 2px solid #e5e7eb; border-radius: 20px;
      background: #fff; color: #555; font-size: 0.85rem; font-weight: 600;
      cursor: pointer; transition: all 0.2s;
    }
    .filter-btn:hover { border-color: #4f46e5; color: #4f46e5; }
    .filter-btn.active { background: #4f46e5; color: #fff; border-color: #4f46e5; }

    .count {
      text-align: center; font-size: 0.82rem; color: #888;
      margin-bottom: 1.25rem; min-height: 1.3em;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 1rem; max-width: 900px; margin: 0 auto;
    }
    .card {
      background: #fff; border-radius: 12px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.08);
      padding: 1rem; animation: fadeIn 0.3s ease; transition: transform 0.2s;
    }
    .card:hover { transform: translateY(-3px); }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
    .card-name { font-weight: 700; font-size: 0.95rem; margin-bottom: 0.35rem; color: #1a1a2e; }
    .badge {
      display: inline-block; padding: 0.2rem 0.55rem; border-radius: 20px;
      font-size: 0.7rem; font-weight: 700; margin-bottom: 0.5rem;
    }
    .badge-audio  { background: #dcfce7; color: #166534; }
    .badge-tech   { background: #dbeafe; color: #1d4ed8; }
    .badge-office { background: #fef3c7; color: #92400e; }
    .badge-home   { background: #fce7f3; color: #9d174d; }
    .card-price { font-size: 1.1rem; font-weight: 800; color: #4f46e5; }
  </style>
</head>
<body>
  <h1>filter() Category Toggle</h1>
  <p class="subtitle">Click a category — <code>filter()</code> keeps only matching items, then <code>map()</code> renders them.</p>

  <div class="filter-bar" id="filterBar"></div>
  <p class="count" id="count"></p>
  <div class="grid" id="grid"></div>

  <script>
    const products = [
      { name: 'Wireless Headphones', price: 79.99,  category: 'Audio'  },
      { name: 'Portable Speaker',    price: 49.99,  category: 'Audio'  },
      { name: 'Earbuds Pro',         price: 89.99,  category: 'Audio'  },
      { name: 'USB-C Hub',           price: 34.99,  category: 'Tech'   },
      { name: 'Mechanical Keyboard', price: 129.99, category: 'Tech'   },
      { name: 'Wireless Mouse',      price: 44.99,  category: 'Tech'   },
      { name: 'Notebook Set',        price: 12.99,  category: 'Office' },
      { name: 'Desk Organiser',      price: 19.99,  category: 'Office' },
      { name: 'Smart Bulb Pack',     price: 24.99,  category: 'Home'   },
      { name: 'LED Desk Lamp',       price: 39.99,  category: 'Home'   },
      { name: 'Cable Organiser',     price: 9.99,   category: 'Office' },
      { name: 'Smart Plug',          price: 15.99,  category: 'Home'   },
    ];

    const categories = ['All', ...new Set(products.map(p => p.category))];
    let selected = 'All';

    // Build filter buttons
    document.getElementById('filterBar').innerHTML = categories.map(cat => `
      <button class="filter-btn ${cat === selected ? 'active' : ''}"
              onclick="setCategory('${cat}')">${cat}</button>
    `).join('');

    function setCategory(cat) {
      selected = cat;
      document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.toggle('active', btn.textContent === cat);
      });
      render();
    }

    function render() {
      const visible = selected === 'All'
        ? products
        : products.filter(p => p.category === selected);  // ← filter()

      document.getElementById('count').textContent =
        `Showing ${visible.length} of ${products.length} products`;

      document.getElementById('grid').innerHTML = visible.map(p => `  // ← map()
        <div class="card">
          <div class="card-name">${p.name}</div>
          <span class="badge badge-${p.category.toLowerCase()}">${p.category}</span>
          <div class="card-price">$${p.price.toFixed(2)}</div>
        </div>
      `).join('');
    }

    render();
  </script>
</body>
</html>
```

---

## CODEPEN 3 — reduce() Shopping Cart

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>reduce() Shopping Cart</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }

    .layout { display: grid; grid-template-columns: 1fr 360px; gap: 1.25rem; max-width: 920px; margin: 0 auto; }
    @media (max-width: 700px) { .layout { grid-template-columns: 1fr; } }

    /* Products */
    .products-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 0.75rem; }
    .product-card {
      background: #fff; border-radius: 10px; padding: 0.9rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.07); text-align: center;
    }
    .product-name { font-size: 0.85rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.3rem; }
    .product-price { font-size: 1rem; font-weight: 800; color: #4f46e5; margin-bottom: 0.6rem; }
    .add-btn {
      width: 100%; padding: 0.4rem; border: none; border-radius: 8px;
      background: #4f46e5; color: #fff; font-size: 0.8rem; font-weight: 700;
      cursor: pointer; transition: background 0.15s;
    }
    .add-btn:hover { background: #4338ca; }
    .badge-small {
      font-size: 0.65rem; padding: 0.15rem 0.5rem; border-radius: 20px;
      font-weight: 700; display: inline-block; margin-bottom: 0.4rem;
    }

    /* Cart */
    .cart-panel {
      background: #fff; border-radius: 12px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.08);
      padding: 1.1rem; display: flex; flex-direction: column; gap: 0.75rem;
      align-self: start; position: sticky; top: 1rem;
    }
    .cart-header { display: flex; justify-content: space-between; align-items: center; }
    .cart-title { font-weight: 700; font-size: 1rem; color: #1a1a2e; }
    .cart-badge {
      background: #4f46e5; color: #fff; border-radius: 20px;
      padding: 0.15rem 0.6rem; font-size: 0.75rem; font-weight: 700;
    }
    .cart-empty { font-size: 0.85rem; color: #bbb; text-align: center; padding: 1rem 0; font-style: italic; }

    .cart-item { display: flex; justify-content: space-between; align-items: center; gap: 0.5rem; }
    .item-info { flex: 1; }
    .item-name  { font-size: 0.83rem; font-weight: 600; color: #374151; }
    .item-price { font-size: 0.75rem; color: #888; }
    .qty-ctrl { display: flex; align-items: center; gap: 0.3rem; }
    .qty-btn {
      width: 24px; height: 24px; border: 1px solid #e5e7eb; border-radius: 6px;
      background: #f8f9ff; color: #4f46e5; font-weight: 700; font-size: 0.9rem;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
      padding: 0; transition: background 0.15s;
    }
    .qty-btn:hover { background: #e0e7ff; }
    .qty-num { font-size: 0.85rem; font-weight: 700; min-width: 20px; text-align: center; }
    .item-total { font-size: 0.85rem; font-weight: 700; color: #4f46e5; min-width: 50px; text-align: right; }
    .remove-btn {
      background: none; border: none; color: #dc2626;
      cursor: pointer; font-size: 0.9rem; padding: 0 0.2rem;
    }

    .cart-divider { border: none; border-top: 1px solid #f3f4f6; }
    .cart-totals { font-size: 0.85rem; color: #555; }
    .total-row { display: flex; justify-content: space-between; padding: 0.15rem 0; }
    .grand-total { font-weight: 800; font-size: 1rem; color: #1a1a2e; }

    .reduce-code {
      background: #1e1e2e; border-radius: 8px; padding: 0.6rem 0.8rem;
      font-size: 0.72rem; color: #a9dc76; font-family: monospace; white-space: pre-wrap; line-height: 1.5;
    }
    .clear-btn {
      width: 100%; padding: 0.45rem; border: 1px solid #e5e7eb; border-radius: 8px;
      background: #fff; color: #888; font-size: 0.82rem; cursor: pointer; transition: all 0.15s;
    }
    .clear-btn:hover { background: #fef2f2; color: #dc2626; border-color: #fecaca; }
  </style>
</head>
<body>
  <h1>reduce() Shopping Cart</h1>
  <p class="subtitle">Add items and watch <code>reduce()</code> compute the cart total.</p>

  <div class="layout">
    <div class="products-grid" id="productsGrid"></div>
    <div class="cart-panel">
      <div class="cart-header">
        <span class="cart-title">🛒 Cart</span>
        <span class="cart-badge" id="cartBadge">0</span>
      </div>
      <div id="cartItems"><p class="cart-empty">Your cart is empty.</p></div>
      <hr class="cart-divider">
      <div class="cart-totals" id="cartTotals"></div>
      <div class="reduce-code" id="reduceCode">// Add items to see reduce() in action</div>
      <button class="clear-btn" onclick="clearCart()">Clear Cart</button>
    </div>
  </div>

  <script>
    const catalog = [
      { id: 1, name: 'Headphones',    price: 79.99,  category: 'audio',  emoji: '🎧' },
      { id: 2, name: 'USB-C Hub',     price: 34.99,  category: 'tech',   emoji: '🔌' },
      { id: 3, name: 'Notebook',      price: 12.99,  category: 'office', emoji: '📓' },
      { id: 4, name: 'Desk Lamp',     price: 39.99,  category: 'home',   emoji: '💡' },
      { id: 5, name: 'Keyboard',      price: 129.99, category: 'tech',   emoji: '⌨️' },
      { id: 6, name: 'Speaker',       price: 49.99,  category: 'audio',  emoji: '🔊' },
    ];

    let cart = [];

    const badgeColors = { audio: '#dcfce7 #166534', tech: '#dbeafe #1d4ed8', office: '#fef3c7 #92400e', home: '#fce7f3 #9d174d' };

    document.getElementById('productsGrid').innerHTML = catalog.map(p => {
      const [bg, color] = badgeColors[p.category].split(' ');
      return `
        <div class="product-card">
          <div style="font-size:1.8rem;margin-bottom:0.3rem">${p.emoji}</div>
          <div class="product-name">${p.name}</div>
          <span class="badge-small" style="background:${bg};color:${color}">${p.category}</span>
          <div class="product-price">$${p.price.toFixed(2)}</div>
          <button class="add-btn" onclick="addToCart(${p.id})">Add to Cart</button>
        </div>`;
    }).join('');

    function addToCart(id) {
      const existing = cart.find(i => i.id === id);
      if (existing) {
        existing.qty++;
      } else {
        const product = catalog.find(p => p.id === id);
        cart.push({ ...product, qty: 1 });
      }
      renderCart();
    }

    function updateQty(id, delta) {
      const item = cart.find(i => i.id === id);
      if (!item) return;
      item.qty += delta;
      if (item.qty <= 0) cart = cart.filter(i => i.id !== id);
      renderCart();
    }

    function removeItem(id) { cart = cart.filter(i => i.id !== id); renderCart(); }
    function clearCart()    { cart = []; renderCart(); }

    function renderCart() {
      const totalQty   = cart.reduce((sum, i) => sum + i.qty, 0);
      const subtotal   = cart.reduce((sum, i) => sum + i.price * i.qty, 0);
      const tax        = subtotal * 0.08;
      const grandTotal = subtotal + tax;

      document.getElementById('cartBadge').textContent = totalQty;

      if (cart.length === 0) {
        document.getElementById('cartItems').innerHTML = '<p class="cart-empty">Your cart is empty.</p>';
        document.getElementById('cartTotals').innerHTML = '';
        document.getElementById('reduceCode').textContent = '// Add items to see reduce() in action';
        return;
      }

      document.getElementById('cartItems').innerHTML = cart.map(item => `
        <div class="cart-item">
          <div class="item-info">
            <div class="item-name">${item.emoji} ${item.name}</div>
            <div class="item-price">$${item.price.toFixed(2)} each</div>
          </div>
          <div class="qty-ctrl">
            <button class="qty-btn" onclick="updateQty(${item.id}, -1)">−</button>
            <span class="qty-num">${item.qty}</span>
            <button class="qty-btn" onclick="updateQty(${item.id},  1)">+</button>
          </div>
          <div class="item-total">$${(item.price * item.qty).toFixed(2)}</div>
          <button class="remove-btn" onclick="removeItem(${item.id})">×</button>
        </div>
      `).join('');

      document.getElementById('cartTotals').innerHTML = `
        <div class="total-row"><span>Subtotal</span><span>$${subtotal.toFixed(2)}</span></div>
        <div class="total-row"><span>Tax (8%)</span><span>$${tax.toFixed(2)}</span></div>
        <div class="total-row grand-total"><span>Total</span><span>$${grandTotal.toFixed(2)}</span></div>
      `;

      document.getElementById('reduceCode').textContent =
`// reduce() computes the grand total
const subtotal = cart.reduce(
  (sum, item) => sum + item.price * item.qty,
  0  // ← starting value
);
// Current result: $${subtotal.toFixed(2)}`;
    }
  </script>
</body>
</html>
```

---

## CODEPEN 4 — Method Decision Lab

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Array Method Decision Lab</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 2rem 1rem; }
    h1 { text-align: center; font-size: 1.3rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .subtitle { text-align: center; font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; }
    .container { max-width: 800px; margin: 0 auto; }

    .btn-row { display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; margin-bottom: 1.25rem; }
    .meth-btn {
      padding: 0.5rem 1rem; border: 2px solid transparent; border-radius: 20px;
      font-size: 0.85rem; font-weight: 700; cursor: pointer; transition: all 0.2s;
    }
    .meth-btn.active { transform: scale(1.05); }
    .btn-forEach  { background: #dbeafe; color: #1d4ed8; border-color: #93c5fd; }
    .btn-map      { background: #dcfce7; color: #166534; border-color: #86efac; }
    .btn-filter   { background: #fce7f3; color: #9d174d; border-color: #f9a8d4; }
    .btn-find     { background: #fef3c7; color: #92400e; border-color: #fcd34d; }
    .btn-some     { background: #ede9fe; color: #5b21b6; border-color: #c4b5fd; }
    .btn-every    { background: #ffedd5; color: #9a3412; border-color: #fdba74; }
    .btn-reduce   { background: #e0f2fe; color: #0369a1; border-color: #7dd3fc; }

    .result-panel {
      background: #fff; border-radius: 12px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.08); padding: 1.25rem; margin-bottom: 1.25rem;
    }
    .r-method { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #888; margin-bottom: 0.3rem; }
    .r-code { background: #1e1e2e; border-radius: 8px; padding: 0.65rem 0.9rem; font-family: monospace; font-size: 0.83rem; color: #a9dc76; margin-bottom: 0.75rem; white-space: pre-wrap; }
    .r-output-label { font-size: 0.72rem; color: #888; margin-bottom: 0.4rem; }
    .r-output { background: #f8f9ff; border: 1px solid #e8eaf6; border-radius: 8px; padding: 0.65rem 0.9rem; font-size: 0.88rem; color: #374151; }
    .item-row { padding: 0.25rem 0; border-bottom: 1px solid #f0f0f0; font-size: 0.85rem; }
    .item-row:last-child { border-bottom: none; }
    .bool-result { font-size: 1.5rem; font-weight: 800; text-align: center; padding: 0.5rem 0; }
    .bool-true  { color: #16a34a; }
    .bool-false { color: #dc2626; }
    .single-result { font-size: 0.95rem; font-family: monospace; }

    .placeholder { color: #bbb; font-style: italic; text-align: center; padding: 1.5rem; }
  </style>
</head>
<body>
  <h1>Method Decision Lab</h1>
  <p class="subtitle">One dataset. Seven methods. Click to see what each one does.</p>

  <div class="container">
    <div class="btn-row">
      <button class="meth-btn btn-forEach" onclick="runMethod('forEach')">forEach</button>
      <button class="meth-btn btn-map"     onclick="runMethod('map')">map</button>
      <button class="meth-btn btn-filter"  onclick="runMethod('filter')">filter</button>
      <button class="meth-btn btn-find"    onclick="runMethod('find')">find</button>
      <button class="meth-btn btn-some"    onclick="runMethod('some')">some</button>
      <button class="meth-btn btn-every"   onclick="runMethod('every')">every</button>
      <button class="meth-btn btn-reduce"  onclick="runMethod('reduce')">reduce</button>
    </div>

    <div class="result-panel" id="resultPanel">
      <div class="placeholder">Click a method button to see it in action on the student dataset.</div>
    </div>
  </div>

  <script>
    const students = [
      { name: 'Alice',   subject: 'Math',    grade: 'A', score: 94, passed: true  },
      { name: 'Bob',     subject: 'Science', grade: 'B', score: 82, passed: true  },
      { name: 'Carol',   subject: 'Math',    grade: 'A', score: 91, passed: true  },
      { name: 'David',   subject: 'English', grade: 'C', score: 71, passed: true  },
      { name: 'Eve',     subject: 'Science', grade: 'D', score: 62, passed: true  },
      { name: 'Frank',   subject: 'Math',    grade: 'B', score: 85, passed: true  },
      { name: 'Grace',   subject: 'English', grade: 'A', score: 97, passed: true  },
      { name: 'Hector',  subject: 'Science', grade: 'F', score: 45, passed: false },
      { name: 'Iris',    subject: 'English', grade: 'C', score: 73, passed: true  },
      { name: 'Jake',    subject: 'Math',    grade: 'B', score: 88, passed: true  },
    ];

    const methods = {
      forEach: {
        code: `students.forEach(s => {\n  console.log(s.name);\n});`,
        run: () => students.map(s => `<div class="item-row">• ${s.name}</div>`).join(''),
        outputLabel: 'Names logged (side effect — forEach returns undefined)',
        type: 'list',
      },
      map: {
        code: `const scores = students.map(s => s.name + ': ' + s.score);`,
        run: () => students.map(s => `<div class="item-row">${s.name}: ${s.score}</div>`).join(''),
        outputLabel: 'New array — every student transformed to a name:score string',
        type: 'list',
      },
      filter: {
        code: `const passing = students.filter(s => s.passed);`,
        run: () => students.filter(s => s.passed).map(s => `<div class="item-row">✓ ${s.name} (${s.grade})</div>`).join(''),
        outputLabel: `Passing students — ${students.filter(s => s.passed).length} of ${students.length}`,
        type: 'list',
      },
      find: {
        code: `const firstA = students.find(s => s.grade === 'A');`,
        run: () => { const r = students.find(s => s.grade === 'A'); return `<div class="single-result">${JSON.stringify(r, null, 2)}</div>`; },
        outputLabel: 'First student with grade A (find stops at first match)',
        type: 'single',
      },
      some: {
        code: `const hasFailingStudent = students.some(s => s.grade === 'F');`,
        run: () => students.some(s => s.grade === 'F'),
        outputLabel: 'Does ANY student have a grade F?',
        type: 'bool',
      },
      every: {
        code: `const allPassed = students.every(s => s.passed);`,
        run: () => students.every(s => s.passed),
        outputLabel: 'Did ALL students pass?',
        type: 'bool',
      },
      reduce: {
        code: `const avg = students.reduce((sum, s) => sum + s.score, 0) / students.length;`,
        run: () => { const avg = students.reduce((sum, s) => sum + s.score, 0) / students.length; return `<div class="single-result">Average score: <strong>${avg.toFixed(1)}</strong></div>`; },
        outputLabel: 'Single value — average score from all students',
        type: 'single',
      },
    };

    function runMethod(name) {
      document.querySelectorAll('.meth-btn').forEach(b => b.classList.remove('active'));
      document.querySelector('.btn-' + name).classList.add('active');

      const m = methods[name];
      let outputHTML = '';

      if (m.type === 'bool') {
        const val = m.run();
        outputHTML = `<div class="bool-result ${val ? 'bool-true' : 'bool-false'}">${val ? '✓ true' : '✗ false'}</div>`;
      } else {
        outputHTML = `<div class="r-output">${m.run()}</div>`;
      }

      document.getElementById('resultPanel').innerHTML = `
        <div class="r-method">${name}()</div>
        <div class="r-code">${m.code}</div>
        <div class="r-output-label">${m.outputLabel}</div>
        ${outputHTML}
      `;
    }
  </script>
</body>
</html>
```

---

## CODEPEN 5 — Full Pipeline: Filterable + Sortable Product Grid

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Filterable + Sortable Product Grid</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f0f2f5; padding: 1.5rem 1rem; }
    h1 { text-align: center; font-size: 1.25rem; color: #1a1a2e; margin-bottom: 0.25rem; }
    .subtitle { text-align: center; font-size: 0.82rem; color: #666; margin-bottom: 1.25rem; }

    .layout { display: grid; grid-template-columns: 220px 1fr; gap: 1.25rem; max-width: 1000px; margin: 0 auto; }
    @media (max-width: 640px) { .layout { grid-template-columns: 1fr; } }

    .sidebar { background: #fff; border-radius: 12px; padding: 1.1rem; box-shadow: 0 2px 10px rgba(0,0,0,0.07); align-self: start; }
    .sidebar h2 { font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.06em; color: #888; margin-bottom: 0.75rem; }

    .filter-btns { display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 1.25rem; }
    .filter-btn {
      padding: 0.4rem 0.75rem; border: 1.5px solid #e5e7eb; border-radius: 8px;
      background: #fff; color: #555; font-size: 0.83rem; text-align: left;
      cursor: pointer; transition: all 0.15s;
    }
    .filter-btn:hover { border-color: #4f46e5; color: #4f46e5; }
    .filter-btn.active { background: #4f46e5; color: #fff; border-color: #4f46e5; }

    select {
      width: 100%; padding: 0.4rem 0.6rem; border: 1.5px solid #e5e7eb;
      border-radius: 8px; font-size: 0.83rem; background: #fff; outline: none; margin-bottom: 1rem;
    }

    .toggle-row { display: flex; align-items: center; gap: 0.5rem; font-size: 0.83rem; color: #555; }
    input[type="checkbox"] { width: 16px; height: 16px; cursor: pointer; accent-color: #4f46e5; }

    /* Main */
    .main-area { display: flex; flex-direction: column; gap: 0.75rem; }
    .toolbar { display: flex; justify-content: space-between; align-items: center; }
    .count-label { font-size: 0.82rem; color: #888; }

    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 0.9rem; }
    .card {
      background: #fff; border-radius: 10px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.07); padding: 0.9rem;
      transition: transform 0.2s; animation: fadeIn 0.25s ease;
    }
    .card:hover { transform: translateY(-2px); }
    .card.out { opacity: 0.55; }
    @keyframes fadeIn { from { opacity:0; transform:translateY(6px);} to {opacity:1;transform:translateY(0);} }
    .card-name  { font-weight: 700; font-size: 0.88rem; margin-bottom: 0.3rem; color: #1a1a2e; }
    .badge { display: inline-block; padding: 0.15rem 0.5rem; border-radius: 20px; font-size: 0.65rem; font-weight: 700; margin-bottom: 0.4rem; }
    .badge-audio  { background: #dcfce7; color: #166534; }
    .badge-tech   { background: #dbeafe; color: #1d4ed8; }
    .badge-office { background: #fef3c7; color: #92400e; }
    .badge-home   { background: #fce7f3; color: #9d174d; }
    .card-price { font-size: 1rem; font-weight: 800; color: #4f46e5; margin-bottom: 0.25rem; }
    .stars { font-size: 0.75rem; color: #f59e0b; margin-bottom: 0.3rem; }
    .stock { font-size: 0.72rem; font-weight: 700; }
    .in-stock { color: #16a34a; } .out-of-stock { color: #dc2626; }

    .pipeline-code {
      background: #1e1e2e; border-radius: 10px; padding: 0.9rem 1rem;
    }
    .pipeline-label { font-size: 0.7rem; color: #666; font-family: monospace; margin-bottom: 0.4rem; }
    .pipeline-text { font-size: 0.75rem; color: #a9dc76; font-family: monospace; white-space: pre-wrap; line-height: 1.6; }
  </style>
</head>
<body>
  <h1>Filterable + Sortable Product Grid</h1>
  <p class="subtitle">One pipeline: <code>filter().filter().sort().map().join('')</code></p>

  <div class="layout">
    <div class="sidebar">
      <h2>Category</h2>
      <div class="filter-btns" id="catBtns"></div>

      <h2>Sort By</h2>
      <select id="sortSelect" onchange="render()">
        <option value="name-az">Name A→Z</option>
        <option value="name-za">Name Z→A</option>
        <option value="price-asc">Price: Low→High</option>
        <option value="price-desc">Price: High→Low</option>
        <option value="rating-desc">Rating: High→Low</option>
      </select>

      <div class="toggle-row">
        <input type="checkbox" id="inStockOnly" onchange="render()">
        <label for="inStockOnly">In Stock Only</label>
      </div>
    </div>

    <div class="main-area">
      <div class="toolbar">
        <span class="count-label" id="countLabel"></span>
      </div>
      <div class="grid" id="grid"></div>
      <div class="pipeline-code">
        <div class="pipeline-label">// The complete pipeline</div>
        <div class="pipeline-text" id="pipelineText"></div>
      </div>
    </div>
  </div>

  <script>
    const products = [
      { name: 'Wireless Headphones', price: 79.99,  category: 'Audio',  rating: 4, inStock: true  },
      { name: 'Portable Speaker',    price: 49.99,  category: 'Audio',  rating: 4, inStock: true  },
      { name: 'Earbuds Pro',         price: 89.99,  category: 'Audio',  rating: 5, inStock: false },
      { name: 'USB-C Hub',           price: 34.99,  category: 'Tech',   rating: 5, inStock: false },
      { name: 'Mechanical Keyboard', price: 129.99, category: 'Tech',   rating: 5, inStock: true  },
      { name: 'Wireless Mouse',      price: 44.99,  category: 'Tech',   rating: 4, inStock: true  },
      { name: 'Notebook Set',        price: 12.99,  category: 'Office', rating: 4, inStock: true  },
      { name: 'Desk Organiser',      price: 19.99,  category: 'Office', rating: 3, inStock: true  },
      { name: 'Smart Bulb Pack',     price: 24.99,  category: 'Home',   rating: 3, inStock: true  },
      { name: 'LED Desk Lamp',       price: 39.99,  category: 'Home',   rating: 3, inStock: false },
      { name: 'Cable Organiser',     price: 9.99,   category: 'Office', rating: 3, inStock: true  },
      { name: 'Smart Plug',          price: 15.99,  category: 'Home',   rating: 4, inStock: true  },
    ];

    const categories = ['All', ...new Set(products.map(p => p.category))];
    let selectedCat = 'All';

    document.getElementById('catBtns').innerHTML = categories.map(cat => `
      <button class="filter-btn ${cat === selectedCat ? 'active' : ''}" onclick="setCat('${cat}')">${cat}</button>
    `).join('');

    function setCat(cat) {
      selectedCat = cat;
      document.querySelectorAll('.filter-btn').forEach(b => {
        b.classList.toggle('active', b.textContent === cat);
      });
      render();
    }

    function getSortFn(mode) {
      switch (mode) {
        case 'name-az':    return (a, b) => a.name.localeCompare(b.name);
        case 'name-za':    return (a, b) => b.name.localeCompare(a.name);
        case 'price-asc':  return (a, b) => a.price - b.price;
        case 'price-desc': return (a, b) => b.price - a.price;
        case 'rating-desc':return (a, b) => b.rating - a.rating;
        default:           return () => 0;
      }
    }

    function render() {
      const sortMode    = document.getElementById('sortSelect').value;
      const inStockOnly = document.getElementById('inStockOnly').checked;

      const visible = products
        .filter(p => selectedCat === 'All' || p.category === selectedCat)
        .filter(p => !inStockOnly || p.inStock)
        .sort(getSortFn(sortMode))
        .map(p => `
          <div class="card ${!p.inStock ? 'out' : ''}">
            <div class="card-name">${p.name}</div>
            <span class="badge badge-${p.category.toLowerCase()}">${p.category}</span>
            <div class="card-price">$${p.price.toFixed(2)}</div>
            <div class="stars">${'★'.repeat(p.rating) + '☆'.repeat(5 - p.rating)}</div>
            <div class="stock ${p.inStock ? 'in-stock' : 'out-of-stock'}">${p.inStock ? '✓ In Stock' : '✗ Out of Stock'}</div>
          </div>`)
        .join('');

      const count = (products
        .filter(p => selectedCat === 'All' || p.category === selectedCat)
        .filter(p => !inStockOnly || p.inStock)).length;

      document.getElementById('grid').innerHTML = visible;
      document.getElementById('countLabel').textContent = `Showing ${count} of ${products.length} products`;
      document.getElementById('pipelineText').textContent =
`products
  .filter(p => ${selectedCat === 'All' ? '"All" — no filter' : `p.category === '${selectedCat}'`})
  .filter(p => ${inStockOnly ? 'p.inStock' : 'true — in-stock filter off'})
  .sort(${sortMode})
  .map(p => renderCard(p))
  .join('')`;
    }

    render();
  </script>
</body>
</html>
```
