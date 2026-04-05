# Day 25 CodePens — Fetch: Data from the Web

## CodePen 1: fetch() Basics

The four-line fetch pattern in complete isolation. A button triggers a fetch from a free API, converts the JSON response, and displays a single item. A status panel shows each step as it happens.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>fetch() Basics</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: system-ui, sans-serif;
    background: #0f0f1a;
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
    color: #a78bfa;
    text-align: center;
  }

  p.desc {
    font-size: .85rem;
    color: #6060a0;
    text-align: center;
    max-width: 480px;
  }

  .btn-fetch {
    padding: .75rem 2rem;
    background: #a78bfa;
    color: #0f0f1a;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    font-size: 1rem;
    cursor: pointer;
    transition: background .2s;
  }

  .btn-fetch:hover { background: #c4b5fd; }
  .btn-fetch:disabled { background: #3a3a6a; color: #6060a0; cursor: not-allowed; }

  .steps {
    display: flex;
    flex-direction: column;
    gap: .5rem;
    width: 100%;
    max-width: 540px;
  }

  .step {
    display: flex;
    align-items: center;
    gap: .75rem;
    background: #1a1a2e;
    border: 1px solid #2e2e4a;
    border-radius: 10px;
    padding: .7rem 1rem;
    font-size: .85rem;
    color: #4a4a7a;
    transition: border-color .3s, color .3s;
  }

  .step.active {
    border-color: #a78bfa;
    color: #e8e8f0;
  }

  .step.done {
    border-color: #6ee7b7;
    color: #6ee7b7;
  }

  .step.error {
    border-color: #f87171;
    color: #f87171;
  }

  .step-num {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #2e2e4a;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: .75rem;
    font-weight: 700;
    flex-shrink: 0;
    transition: background .3s;
  }

  .step.active .step-num { background: #a78bfa; color: #0f0f1a; }
  .step.done  .step-num  { background: #6ee7b7; color: #0f0f1a; }
  .step.error .step-num  { background: #f87171; color: #0f0f1a; }

  .result-card {
    background: #1a1a2e;
    border: 1px solid #6ee7b7;
    border-radius: 14px;
    padding: 1.5rem;
    width: 100%;
    max-width: 540px;
    display: none;
    animation: fadeIn .3s ease;
  }

  .result-card.visible { display: block; }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .result-card img {
    width: 100%;
    max-height: 180px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 1rem;
  }

  .result-card h3 {
    font-size: 1.1rem;
    color: #e8e8f0;
    margin-bottom: .4rem;
  }

  .result-card .meta {
    font-size: .82rem;
    color: #6ee7b7;
    margin-bottom: .6rem;
  }

  .result-card .detail {
    font-size: .82rem;
    color: #8080b0;
    line-height: 1.5;
  }
</style>
</head>
<body>

<h2>The fetch() Recipe</h2>
<p class="desc">Click the button. Watch each step of the fetch happen in sequence.</p>

<button class="btn-fetch" id="fetchBtn">Fetch a Random Meal</button>

<div class="steps">
  <div class="step" id="step1">
    <span class="step-num">1</span>
    <span>fetch(url) — send the HTTP request</span>
  </div>
  <div class="step" id="step2">
    <span class="step-num">2</span>
    <span>.then(response =&gt; response.json()) — convert response to data</span>
  </div>
  <div class="step" id="step3">
    <span class="step-num">3</span>
    <span>.then(data =&gt; renderCard(data)) — use the data</span>
  </div>
  <div class="step" id="step4">
    <span class="step-num">4</span>
    <span>.catch(error =&gt; showError()) — handle any failures</span>
  </div>
</div>

<div class="result-card" id="resultCard"></div>

<script>
  const btn  = document.querySelector('#fetchBtn');
  const card = document.querySelector('#resultCard');

  function setStep(num, state) {
    const el = document.querySelector('#step' + num);
    el.classList.remove('active', 'done', 'error');
    el.classList.add(state);
  }

  function resetSteps() {
    [1, 2, 3, 4].forEach(function(n) {
      const el = document.querySelector('#step' + n);
      el.classList.remove('active', 'done', 'error');
    });
    card.classList.remove('visible');
  }

  btn.addEventListener('click', function() {
    btn.disabled = true;
    resetSteps();

    // Step 1: fetch() — send the request
    setStep(1, 'active');

    fetch('https://www.themealdb.com/api/json/v1/1/random.php')
      .then(function(response) {
        // Step 1 done, Step 2 active
        setStep(1, 'done');
        setStep(2, 'active');

        // Convert the response body to JSON
        return response.json();
      })
      .then(function(data) {
        // Step 2 done, Step 3 active
        setStep(2, 'done');
        setStep(3, 'active');

        // Use the data
        const meal = data.meals[0];

        card.innerHTML = `
          <img src="${meal.strMealThumb}" alt="${meal.strMeal}">
          <h3>${meal.strMeal}</h3>
          <div class="meta">${meal.strCategory} &middot; ${meal.strArea}</div>
          <div class="detail">First instruction: ${meal.strInstructions.split('.')[0]}.</div>
        `;
        card.classList.add('visible');

        setStep(3, 'done');
        setStep(4, 'done');  // .catch() was standby — mark as done (no error)
        btn.disabled = false;
      })
      .catch(function(error) {
        setStep(4, 'error');
        card.innerHTML = '<h3 style="color:#f87171;">Failed to load data</h3><p class="detail">Check your connection and try again.</p>';
        card.classList.add('visible');
        btn.disabled = false;
      });
  });
</script>
</body>
</html>
```

---

## CodePen 2: Loading and Error States

A gallery that demonstrates all three states: loading (spinner), loaded (cards), and error (friendly message with retry). A toggle lets you simulate a network failure.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Loading and Error States</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: system-ui, sans-serif;
    background: #111827;
    color: #f9fafb;
    min-height: 100vh;
    padding: 2rem;
  }

  .top-bar {
    display: flex;
    gap: 1rem;
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 1.5rem;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
  }

  h2 {
    font-size: 1.1rem;
    color: #6ee7b7;
    flex: 1;
  }

  .toggle-row {
    display: flex;
    align-items: center;
    gap: .5rem;
    font-size: .8rem;
    color: #6b7280;
  }

  .toggle-row input[type="checkbox"] { accent-color: #f87171; }

  button {
    padding: .55rem 1.1rem;
    background: #6ee7b7;
    color: #111827;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    font-size: .85rem;
    cursor: pointer;
    transition: background .2s;
  }

  button:hover { background: #a7f3d0; }

  #container {
    max-width: 700px;
    margin: 0 auto;
    min-height: 200px;
  }

  /* Loading state */
  .loading-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    padding: 3rem;
    color: #6b7280;
  }

  .spinner {
    width: 36px;
    height: 36px;
    border: 3px solid #374151;
    border-top-color: #6ee7b7;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin { to { transform: rotate(360deg); } }

  /* Error state */
  .error-state {
    text-align: center;
    padding: 3rem;
    background: #1f1515;
    border: 1px solid #7f1d1d;
    border-radius: 14px;
    color: #fca5a5;
  }

  .error-state h3 { color: #f87171; margin-bottom: .5rem; }
  .error-state p  { font-size: .85rem; color: #9ca3af; margin-bottom: 1rem; }
  .error-state button { background: #f87171; color: #fff; }
  .error-state button:hover { background: #fca5a5; }

  /* Card grid */
  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 1rem;
  }

  .card {
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 12px;
    overflow: hidden;
    animation: fadeIn .25s ease;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .card img {
    width: 100%;
    height: 100px;
    object-fit: cover;
    display: block;
  }

  .card-body {
    padding: .75rem;
  }

  .card-title {
    font-size: .85rem;
    font-weight: 700;
    color: #f9fafb;
    margin-bottom: .2rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .card-meta {
    font-size: .75rem;
    color: #6ee7b7;
  }
</style>
</head>
<body>

<div class="top-bar">
  <h2>Meal Gallery</h2>
  <label class="toggle-row">
    <input type="checkbox" id="simulateError">
    Simulate network error
  </label>
  <button id="loadBtn">Load Meals</button>
</div>

<div id="container">
  <div class="loading-state" style="display:none;" id="loadingEl">
    <div class="spinner"></div>
    <span>Loading meals&hellip;</span>
  </div>
</div>

<script>
  function showLoading() {
    document.querySelector('#container').innerHTML = `
      <div class="loading-state">
        <div class="spinner"></div>
        <span>Loading meals&hellip;</span>
      </div>
    `;
  }

  function showError() {
    document.querySelector('#container').innerHTML = `
      <div class="error-state">
        <h3>Could not load meals</h3>
        <p>Check your internet connection or the API may be temporarily unavailable.</p>
        <button id="retryBtn">Try Again</button>
      </div>
    `;
    document.querySelector('#retryBtn').addEventListener('click', loadMeals);
  }

  function renderCards(meals) {
    if (!meals || meals.length === 0) {
      document.querySelector('#container').innerHTML =
        '<p style="color:#6b7280; text-align:center; padding:2rem;">No meals found.</p>';
      return;
    }

    document.querySelector('#container').innerHTML = `
      <div class="card-grid">
        ${meals.slice(0, 12).map(function(meal) {
          return `
            <div class="card">
              <img src="${meal.strMealThumb}/preview" alt="${meal.strMeal}"
                   onerror="this.src='https://via.placeholder.com/160x100?text=No+Image'">
              <div class="card-body">
                <div class="card-title">${meal.strMeal}</div>
                <div class="card-meta">${meal.strCategory}</div>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }

  function loadMeals() {
    // 1. Show loading state BEFORE the request
    showLoading();

    const simulateError = document.querySelector('#simulateError').checked;
    const url = simulateError
      ? 'https://this-url-does-not-exist.invalid/api'
      : 'https://www.themealdb.com/api/json/v1/1/search.php?s=chicken';

    // 2. Fetch the data
    fetch(url)
      .then(function(response) { return response.json(); })
      .then(function(data) {
        // 3. Use the data
        renderCards(data.meals);
      })
      .catch(function(error) {
        // 4. Handle errors
        showError();
      });
  }

  document.querySelector('#loadBtn').addEventListener('click', loadMeals);

  // Auto-load on start
  loadMeals();
</script>
</body>
</html>
```

---

## CodePen 3: Fetch + Filter + Search

A fully functional gallery powered by a real API. The data comes from fetch(), but the filter buttons and live search from Day 23 work exactly the same. Shows that renderCards() is data-source-agnostic.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fetch + Filter + Search</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: system-ui, sans-serif;
    background: #0d1117;
    color: #e6edf3;
    min-height: 100vh;
    padding: 1.5rem;
  }

  h2 {
    text-align: center;
    font-size: 1.2rem;
    color: #58a6ff;
    margin-bottom: 1.25rem;
  }

  .controls {
    display: flex;
    gap: .75rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 1.25rem;
  }

  .search-input {
    padding: .55rem .9rem;
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    color: #e6edf3;
    font-size: .9rem;
    outline: none;
    width: 200px;
    transition: border-color .2s;
  }

  .search-input:focus { border-color: #58a6ff; }

  .filter-btn {
    padding: .45rem .95rem;
    background: #161b22;
    border: 1px solid #30363d;
    color: #8b949e;
    border-radius: 8px;
    font-size: .82rem;
    cursor: pointer;
    transition: all .2s;
  }

  .filter-btn:hover { border-color: #58a6ff; color: #e6edf3; }
  .filter-btn.active { background: #58a6ff; color: #0d1117; border-color: #58a6ff; font-weight: 700; }

  #container {
    max-width: 800px;
    margin: 0 auto;
    min-height: 200px;
  }

  .loading-text {
    text-align: center;
    color: #30363d;
    padding: 3rem;
    font-size: .95rem;
  }

  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(175px, 1fr));
    gap: 1rem;
  }

  .card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    overflow: hidden;
    cursor: pointer;
    transition: border-color .2s, transform .2s;
  }

  .card:hover { border-color: #58a6ff; transform: translateY(-2px); }

  .card img {
    width: 100%;
    height: 120px;
    object-fit: cover;
    display: block;
  }

  .card-body { padding: .75rem; }

  .card-title {
    font-size: .85rem;
    font-weight: 700;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    color: #e6edf3;
    margin-bottom: .25rem;
  }

  .badge {
    display: inline-block;
    background: #1f3a5f;
    color: #58a6ff;
    font-size: .7rem;
    padding: .15rem .5rem;
    border-radius: 4px;
  }

  .empty-state {
    text-align: center;
    color: #30363d;
    padding: 3rem;
    font-size: .9rem;
    border: 1px dashed #30363d;
    border-radius: 12px;
  }

  .results-count {
    text-align: center;
    font-size: .78rem;
    color: #30363d;
    margin-bottom: .75rem;
  }
</style>
</head>
<body>

<h2>Meal Browser — Powered by fetch()</h2>

<div class="controls">
  <input type="text" class="search-input" id="searchInput" placeholder="Search meals...">
  <button class="filter-btn active" data-category="all">All</button>
  <button class="filter-btn" data-category="Chicken">Chicken</button>
  <button class="filter-btn" data-category="Beef">Beef</button>
  <button class="filter-btn" data-category="Vegetarian">Vegetarian</button>
  <button class="filter-btn" data-category="Pasta">Pasta</button>
</div>

<div id="container">
  <p class="loading-text">Loading meals&hellip;</p>
</div>

<script>
  // State
  let allMeals      = [];
  let activeCategory = 'all';
  let searchQuery   = '';

  // Fetch meals from the API — called once on page load
  fetch('https://www.themealdb.com/api/json/v1/1/search.php?s=')
    .then(function(response) { return response.json(); })
    .then(function(data) {
      allMeals = data.meals || [];
      filterAndRender();
    })
    .catch(function() {
      document.querySelector('#container').innerHTML =
        '<p class="empty-state">Failed to load meals. Try refreshing.</p>';
    });

  // Filter + render — same pattern as Day 23
  function filterAndRender() {
    const results = allMeals.filter(function(meal) {
      const matchesCategory = activeCategory === 'all' || meal.strCategory === activeCategory;
      const matchesSearch   = meal.strMeal.toLowerCase().includes(searchQuery);
      return matchesCategory && matchesSearch;
    });
    renderCards(results);
  }

  // Render function — unchanged from Day 23 pattern
  function renderCards(meals) {
    const container = document.querySelector('#container');

    if (meals.length === 0) {
      container.innerHTML = `<p class="empty-state">No meals match &ldquo;${searchQuery || activeCategory}&rdquo;.</p>`;
      return;
    }

    container.innerHTML = `
      <p class="results-count">${meals.length} meal${meals.length === 1 ? '' : 's'} found</p>
      <div class="card-grid">
        ${meals.slice(0, 20).map(function(meal) {
          return `
            <div class="card" data-id="${meal.idMeal}">
              <img src="${meal.strMealThumb}/preview" alt="${meal.strMeal}">
              <div class="card-body">
                <div class="card-title">${meal.strMeal}</div>
                <span class="badge">${meal.strCategory}</span>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }

  // Filter buttons
  document.querySelectorAll('.filter-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.filter-btn').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      activeCategory = btn.dataset.category;
      filterAndRender();
    });
  });

  // Live search
  document.querySelector('#searchInput').addEventListener('input', function() {
    searchQuery = this.value.toLowerCase();
    filterAndRender();
  });
</script>
</body>
</html>
```

---

## CodePen 4: Multi-API Explorer

Choose from three different free APIs. Each fetch returns differently shaped JSON — students learn to read the structure and adjust accordingly. Shows that the render function adapts to the data, not the other way around.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Multi-API Explorer</title>
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

  p.desc {
    font-size: .85rem;
    color: #6060a0;
    text-align: center;
    max-width: 520px;
  }

  .api-buttons {
    display: flex;
    gap: .75rem;
    flex-wrap: wrap;
    justify-content: center;
  }

  .api-btn {
    padding: .6rem 1.2rem;
    border: 2px solid #2e2e4a;
    background: #12122a;
    color: #a0a0c0;
    border-radius: 10px;
    font-size: .85rem;
    font-weight: 600;
    cursor: pointer;
    transition: all .2s;
  }

  .api-btn:hover { border-color: #a78bfa; color: #e8e8f0; }
  .api-btn.active { border-color: #ffeaa7; color: #ffeaa7; background: #2a2a1e; }

  .url-display {
    font-family: monospace;
    font-size: .78rem;
    color: #6ee7b7;
    background: #0a120a;
    border: 1px solid #1a3a1a;
    border-radius: 8px;
    padding: .5rem .85rem;
    max-width: 600px;
    width: 100%;
    word-break: break-all;
    text-align: center;
  }

  #container {
    width: 100%;
    max-width: 660px;
    min-height: 200px;
  }

  .loading-text {
    text-align: center;
    color: #4a4a7a;
    padding: 2.5rem;
    font-size: .9rem;
  }

  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: .85rem;
  }

  .card {
    background: #12122a;
    border: 1px solid #2e2e4a;
    border-radius: 12px;
    overflow: hidden;
    transition: border-color .2s;
  }

  .card:hover { border-color: #a78bfa; }

  .card img {
    width: 100%;
    height: 100px;
    object-fit: cover;
    display: block;
    background: #1a1a2e;
  }

  .card-body { padding: .7rem; }

  .card-name {
    font-size: .82rem;
    font-weight: 700;
    color: #e8e8f0;
    margin-bottom: .2rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .card-sub {
    font-size: .73rem;
    color: #a78bfa;
  }

  .error-msg {
    text-align: center;
    color: #f87171;
    padding: 2rem;
    border: 1px dashed #4a1a1a;
    border-radius: 10px;
  }
</style>
</head>
<body>

<h2>Multi-API Explorer</h2>
<p class="desc">Every API returns differently shaped JSON. Pick one and see how the fetch data maps to the render function.</p>

<div class="api-buttons">
  <button class="api-btn active" data-api="meals">TheMealDB</button>
  <button class="api-btn" data-api="pokemon">PokéAPI</button>
  <button class="api-btn" data-api="countries">REST Countries</button>
</div>

<div class="url-display" id="urlDisplay">https://www.themealdb.com/api/json/v1/1/search.php?s=a</div>

<div id="container">
  <p class="loading-text">Click an API button to load data</p>
</div>

<script>
  const APIs = {
    meals: {
      url:    'https://www.themealdb.com/api/json/v1/1/search.php?s=a',
      // Response shape: { meals: [ { strMeal, strCategory, strMealThumb, ... } ] }
      extract: function(data) { return data.meals || []; },
      render: function(item) {
        return `
          <div class="card">
            <img src="${item.strMealThumb}/preview" alt="${item.strMeal}">
            <div class="card-body">
              <div class="card-name">${item.strMeal}</div>
              <div class="card-sub">${item.strCategory}</div>
            </div>
          </div>
        `;
      }
    },

    pokemon: {
      url:    'https://pokeapi.co/api/v2/pokemon?limit=20',
      // Response shape: { results: [ { name, url } ] }
      // We fetch each pokémon sprite separately — simplified: use sprite URL pattern
      extract: function(data) { return data.results || []; },
      render: function(item, index) {
        const id  = index + 1;
        const img = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${id}.png`;
        return `
          <div class="card">
            <img src="${img}" alt="${item.name}" style="height:80px; object-fit:contain; padding:.5rem; background:#1a1a2e;">
            <div class="card-body">
              <div class="card-name" style="text-transform:capitalize;">${item.name}</div>
              <div class="card-sub">#${id}</div>
            </div>
          </div>
        `;
      }
    },

    countries: {
      url:    'https://restcountries.com/v3.1/region/europe?fields=name,flags,capital,population',
      // Response shape: [ { name: { common }, flags: { png }, capital: [...], population } ]
      extract: function(data) { return Array.isArray(data) ? data.slice(0, 20) : []; },
      render: function(item) {
        const pop = (item.population / 1000000).toFixed(1) + 'M';
        return `
          <div class="card">
            <img src="${item.flags.png}" alt="${item.name.common} flag" style="height:80px; object-fit:cover;">
            <div class="card-body">
              <div class="card-name">${item.name.common}</div>
              <div class="card-sub">${item.capital?.[0] || '—'} &middot; ${pop}</div>
            </div>
          </div>
        `;
      }
    }
  };

  let currentApi = 'meals';

  function loadApi(apiKey) {
    const api = APIs[apiKey];
    document.querySelector('#urlDisplay').textContent = api.url;
    document.querySelector('#container').innerHTML = '<p class="loading-text">Fetching from API&hellip;</p>';

    fetch(api.url)
      .then(function(response) { return response.json(); })
      .then(function(data) {
        const items = api.extract(data);

        if (items.length === 0) {
          document.querySelector('#container').innerHTML = '<p class="loading-text">No data returned.</p>';
          return;
        }

        document.querySelector('#container').innerHTML =
          '<div class="card-grid">' +
          items.map(function(item, index) {
            return api.render(item, index);
          }).join('') +
          '</div>';
      })
      .catch(function() {
        document.querySelector('#container').innerHTML =
          '<p class="error-msg">Failed to load from this API. Try another one.</p>';
      });
  }

  document.querySelectorAll('.api-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.api-btn').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      currentApi = btn.dataset.api;
      loadApi(currentApi);
    });
  });

  // Auto-load the default
  loadApi('meals');
</script>
</body>
</html>
```

---

## CodePen 5: async/await Version

The same meal gallery as CodePen 3, rewritten using async/await instead of .then(). Side-by-side code comments show the equivalence. Students see that it's the same operation, just different syntax.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>async/await Fetch</title>
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
    font-size: 1.2rem;
    color: #818cf8;
    text-align: center;
  }

  .syntax-toggle {
    display: flex;
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 10px;
    overflow: hidden;
  }

  .syntax-btn {
    padding: .5rem 1.25rem;
    background: none;
    border: none;
    color: #64748b;
    font-size: .85rem;
    font-weight: 600;
    cursor: pointer;
    transition: all .2s;
  }

  .syntax-btn.active {
    background: #818cf8;
    color: #0f172a;
  }

  .code-panel {
    background: #0a0f1e;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    max-width: 600px;
    width: 100%;
    font-family: monospace;
    font-size: .8rem;
    line-height: 1.6;
    color: #94a3b8;
    white-space: pre;
    overflow-x: auto;
  }

  .code-panel .kw   { color: #818cf8; }
  .code-panel .fn   { color: #67e8f9; }
  .code-panel .str  { color: #86efac; }
  .code-panel .cmt  { color: #475569; font-style: italic; }

  .load-btn {
    padding: .65rem 2rem;
    background: #818cf8;
    color: #0f172a;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    font-size: .95rem;
    cursor: pointer;
    transition: background .2s;
  }

  .load-btn:hover { background: #a5b4fc; }

  #container {
    max-width: 700px;
    width: 100%;
    min-height: 180px;
  }

  .loading-msg {
    text-align: center;
    color: #334155;
    padding: 2.5rem;
  }

  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
    gap: 1rem;
  }

  .card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    overflow: hidden;
    animation: fadeIn .2s ease;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .card img { width: 100%; height: 110px; object-fit: cover; display: block; }

  .card-body { padding: .7rem; }

  .card-name {
    font-size: .85rem;
    font-weight: 700;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .card-area {
    font-size: .75rem;
    color: #818cf8;
    margin-top: .2rem;
  }

  .error-msg {
    text-align: center;
    color: #f87171;
    padding: 2rem;
    border: 1px dashed #450a0a;
    border-radius: 10px;
  }
</style>
</head>
<body>

<h2>async/await vs .then() — Same Result</h2>

<div class="syntax-toggle">
  <button class="syntax-btn active" id="btnThen">Show .then() version</button>
  <button class="syntax-btn" id="btnAsync">Show async/await version</button>
</div>

<div class="code-panel" id="codeDisplay"></div>

<button class="load-btn" id="loadBtn">Load Meals</button>

<div id="container">
  <p class="loading-msg">Click the button to load</p>
</div>

<script>
  const THEN_CODE =
`<span class="cmt">// .then() version</span>
<span class="kw">function</span> <span class="fn">loadMeals</span>() {
  container.innerHTML = <span class="str">'&lt;p&gt;Loading...&lt;/p&gt;'</span>;

  <span class="fn">fetch</span>(<span class="str">'https://...themealdb.../search.php?s=pasta'</span>)
    .then(<span class="kw">function</span>(response) {
      <span class="kw">return</span> response.<span class="fn">json</span>();
    })
    .then(<span class="kw">function</span>(data) {
      <span class="fn">renderCards</span>(data.meals);
    })
    .catch(<span class="kw">function</span>(error) {
      container.innerHTML = <span class="str">'&lt;p&gt;Failed to load.&lt;/p&gt;'</span>;
    });
}`;

  const ASYNC_CODE =
`<span class="cmt">// async/await version — same result</span>
<span class="kw">async function</span> <span class="fn">loadMeals</span>() {
  container.innerHTML = <span class="str">'&lt;p&gt;Loading...&lt;/p&gt;'</span>;

  <span class="kw">try</span> {
    <span class="kw">const</span> response = <span class="kw">await</span> <span class="fn">fetch</span>(<span class="str">'https://...themealdb.../search.php?s=pasta'</span>);
    <span class="kw">const</span> data     = <span class="kw">await</span> response.<span class="fn">json</span>();
    <span class="fn">renderCards</span>(data.meals);
  } <span class="kw">catch</span> (error) {
    container.innerHTML = <span class="str">'&lt;p&gt;Failed to load.&lt;/p&gt;'</span>;
  }
}`;

  // Show .then() code by default
  document.querySelector('#codeDisplay').innerHTML = THEN_CODE;

  document.querySelector('#btnThen').addEventListener('click', function() {
    document.querySelector('#btnThen').classList.add('active');
    document.querySelector('#btnAsync').classList.remove('active');
    document.querySelector('#codeDisplay').innerHTML = THEN_CODE;
  });

  document.querySelector('#btnAsync').addEventListener('click', function() {
    document.querySelector('#btnAsync').classList.add('active');
    document.querySelector('#btnThen').classList.remove('active');
    document.querySelector('#codeDisplay').innerHTML = ASYNC_CODE;
  });

  // ---- The actual fetch using async/await ----
  const container = document.querySelector('#container');

  function renderCards(meals) {
    if (!meals || meals.length === 0) {
      container.innerHTML = '<p class="loading-msg">No meals found.</p>';
      return;
    }

    container.innerHTML = '<div class="card-grid">' +
      meals.slice(0, 12).map(function(meal) {
        return `
          <div class="card">
            <img src="${meal.strMealThumb}/preview" alt="${meal.strMeal}">
            <div class="card-body">
              <div class="card-name">${meal.strMeal}</div>
              <div class="card-area">${meal.strArea || meal.strCategory}</div>
            </div>
          </div>
        `;
      }).join('') +
      '</div>';
  }

  // async/await version
  async function loadMeals() {
    container.innerHTML = '<p class="loading-msg">Loading meals&hellip;</p>';

    try {
      const response = await fetch('https://www.themealdb.com/api/json/v1/1/search.php?s=pasta');
      const data     = await response.json();
      renderCards(data.meals);
    } catch (error) {
      container.innerHTML = '<p class="error-msg">Failed to load meals. Try again.</p>';
    }
  }

  document.querySelector('#loadBtn').addEventListener('click', loadMeals);
</script>
</body>
</html>
```
