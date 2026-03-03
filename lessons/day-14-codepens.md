# Day 14 — CSS Transitions & Transforms: CodePen Code Blocks

Each section contains the HTML (paste into the CodePen HTML panel) and CSS (paste into the CodePen CSS panel). The HTML includes full document structure so students see a complete, valid page.

---

## CODEPEN 1 — Basic Transitions: All Four Sub-Properties

**Demonstrates:** transition-property, transition-duration, transition-timing-function, transition-delay, and the shorthand. Three buttons side by side show progressively more sophisticated transitions.

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS Transitions — All Four Properties</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <h1>CSS Transition Properties</h1>
  <p class="intro">Hover each button to see how each sub-property affects the animation.</p>

  <div class="demo-row">

    <div class="demo">
      <button class="btn btn--basic">Basic (0.3s ease)</button>
      <p class="label">transition: background-color 0.3s ease</p>
    </div>

    <div class="demo">
      <button class="btn btn--delayed">Delayed (0.5s, 0.2s delay)</button>
      <p class="label">transition: background-color 0.5s ease 0.2s</p>
    </div>

    <div class="demo">
      <button class="btn btn--multi">Multi-Property</button>
      <p class="label">background-color + transform + box-shadow</p>
    </div>

  </div>

  <div class="demo-row">

    <div class="demo">
      <div class="box box--color">
        <span>Color</span>
      </div>
      <p class="label">Hover: color transition</p>
    </div>

    <div class="demo">
      <div class="box box--size">
        <span>Size</span>
      </div>
      <p class="label">Hover: width + height (causes layout shift)</p>
    </div>

    <div class="demo">
      <div class="box box--transform">
        <span>Transform</span>
      </div>
      <p class="label">Hover: transform (no layout shift)</p>
    </div>

  </div>

  <div class="note">
    <strong>Key observation:</strong> The "Size" box pushes other elements when it grows.
    The "Transform" box does not — transform never affects layout.
  </div>

</body>
</html>
```

### CSS
```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #f8f9fa;
  color: #333;
}

h1 {
  font-size: 1.4rem;
  margin-bottom: 0.5rem;
}

.intro {
  color: #555;
  margin-bottom: 2rem;
}

.demo-row {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
  align-items: flex-start;
  flex-wrap: wrap;
}

.demo {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.label {
  font-size: 0.75rem;
  color: #666;
  font-family: monospace;
  max-width: 220px;
}

/* === BUTTONS === */

.btn {
  padding: 0.7rem 1.4rem;
  border: none;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  color: white;
}

/* Button 1: basic color transition */
.btn--basic {
  background-color: #4f6df5;
  transition: background-color 0.3s ease;
}
.btn--basic:hover {
  background-color: #c0392b;
}

/* Button 2: delayed transition */
.btn--delayed {
  background-color: #2ecc71;
  transition: background-color 0.5s ease 0.2s;
}
.btn--delayed:hover {
  background-color: #1a6b3c;
}

/* Button 3: multiple properties */
.btn--multi {
  background-color: #9b59b6;
  box-shadow: 0 2px 6px rgba(0,0,0,0.15);
  transition: background-color 0.2s ease-out,
              transform 0.15s ease-out,
              box-shadow 0.2s ease-out;
}
.btn--multi:hover {
  background-color: #6c3483;
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}
.btn--multi:active {
  transform: translateY(-1px);
  box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}

/* === BOXES === */

.box {
  width: 120px;
  height: 80px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: white;
  font-size: 0.9rem;
  cursor: pointer;
}

/* Box 1: color transition */
.box--color {
  background-color: #e67e22;
  transition: background-color 0.4s ease;
}
.box--color:hover {
  background-color: #1abc9c;
}

/* Box 2: width/height — causes layout reflow */
.box--size {
  background-color: #e74c3c;
  transition: width 0.3s ease, height 0.3s ease;
}
.box--size:hover {
  width: 180px;
  height: 120px;
}

/* Box 3: transform — no layout reflow */
.box--transform {
  background-color: #3498db;
  transition: transform 0.3s ease;
}
.box--transform:hover {
  transform: scale(1.4);
}

.note {
  padding: 1rem 1.25rem;
  background: #fff8e1;
  border-left: 4px solid #f39c12;
  border-radius: 0 6px 6px 0;
  font-size: 0.875rem;
  line-height: 1.5;
  max-width: 600px;
}
```

### JS
```js
// No JavaScript needed for this demo
```

---

## CODEPEN 2 — Timing Functions Visualizer

**Demonstrates:** ease, linear, ease-in, ease-out, ease-in-out, cubic-bezier. A "Go!" button triggers all transitions simultaneously so students can compare the pace of each.

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Timing Functions Comparison</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <h1>Timing Functions</h1>
  <p class="intro">Click <strong>Go!</strong> to animate all tracks at once. Watch how each easing function affects the pace.</p>

  <button id="go-btn">Go!</button>

  <div class="tracks">

    <div class="track">
      <div class="track__label">ease (default)</div>
      <div class="track__rail">
        <div class="ball ball--ease">ease</div>
      </div>
    </div>

    <div class="track">
      <div class="track__label">linear</div>
      <div class="track__rail">
        <div class="ball ball--linear">linear</div>
      </div>
    </div>

    <div class="track">
      <div class="track__label">ease-in</div>
      <div class="track__rail">
        <div class="ball ball--ease-in">ease-in</div>
      </div>
    </div>

    <div class="track">
      <div class="track__label">ease-out</div>
      <div class="track__rail">
        <div class="ball ball--ease-out">ease-out</div>
      </div>
    </div>

    <div class="track">
      <div class="track__label">ease-in-out</div>
      <div class="track__rail">
        <div class="ball ball--ease-in-out">ease-in-out</div>
      </div>
    </div>

    <div class="track">
      <div class="track__label">cubic-bezier (springy)</div>
      <div class="track__rail">
        <div class="ball ball--spring">spring</div>
      </div>
    </div>

  </div>

</body>
</html>
```

### CSS
```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #1a1a2e;
  color: #eee;
}

h1 {
  font-size: 1.4rem;
  margin-bottom: 0.5rem;
}

.intro {
  color: #aaa;
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
}

#go-btn {
  padding: 0.6rem 2rem;
  background: #4f6df5;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  margin-bottom: 2rem;
  transition: background 0.15s;
}

#go-btn:hover { background: #3a56d4; }

.tracks {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.track {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.track__label {
  width: 180px;
  font-size: 0.8rem;
  font-family: monospace;
  color: #bbb;
  flex-shrink: 0;
}

.track__rail {
  flex: 1;
  height: 46px;
  background: rgba(255,255,255,0.06);
  border-radius: 6px;
  position: relative;
  overflow: hidden;
}

.ball {
  position: absolute;
  left: 4px;
  top: 50%;
  transform: translateY(-50%);
  width: 80px;
  height: 36px;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  font-weight: 700;
  color: white;
  transition: left 1.4s;  /* duration set here; easing differs per class */
}

/* Trigger state: all balls slide to the right */
.animating .ball {
  left: calc(100% - 84px);
}

/* Each ball has a different timing function */
.ball--ease        { background: #4f6df5; transition-timing-function: ease; }
.ball--linear      { background: #2ecc71; transition-timing-function: linear; }
.ball--ease-in     { background: #e67e22; transition-timing-function: ease-in; }
.ball--ease-out    { background: #e74c3c; transition-timing-function: ease-out; }
.ball--ease-in-out { background: #9b59b6; transition-timing-function: ease-in-out; }
.ball--spring      { background: #1abc9c; transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1); }
```

### JS
```js
const btn = document.getElementById('go-btn');
const rail = document.querySelector('.tracks');
let animating = false;

btn.addEventListener('click', () => {
  animating = !animating;
  // Toggle the .animating class on the tracks container
  // This triggers the CSS transition on all .ball elements at once
  rail.classList.toggle('animating', animating);
  btn.textContent = animating ? 'Reset' : 'Go!';
});
```

---

## CODEPEN 3 — 2D Transforms Explorer

**Demonstrates:** translate, rotate, scale, skew, combined transforms, and transform-origin. Hover each tile to see the transform applied with a smooth transition.

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2D Transforms Explorer</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <h1>2D Transforms</h1>
  <p class="intro">Hover each tile to see the transform in action.</p>

  <div class="grid">

    <div class="tile tile--translate">
      <span class="tile__icon">↗</span>
      <strong>translate</strong>
      <code>translateX(20px) translateY(-20px)</code>
    </div>

    <div class="tile tile--rotate">
      <span class="tile__icon">↻</span>
      <strong>rotate</strong>
      <code>rotate(45deg)</code>
    </div>

    <div class="tile tile--scale-up">
      <span class="tile__icon">⊕</span>
      <strong>scale up</strong>
      <code>scale(1.3)</code>
    </div>

    <div class="tile tile--scale-down">
      <span class="tile__icon">⊖</span>
      <strong>scale down</strong>
      <code>scale(0.7)</code>
    </div>

    <div class="tile tile--skew">
      <span class="tile__icon">//</span>
      <strong>skewX</strong>
      <code>skewX(20deg)</code>
    </div>

    <div class="tile tile--combined">
      <span class="tile__icon">★</span>
      <strong>combined</strong>
      <code>rotate(15deg) scale(1.1) translateY(-8px)</code>
    </div>

    <div class="tile tile--origin-tl">
      <span class="tile__icon">◤</span>
      <strong>origin: top left</strong>
      <code>rotate(45deg) — origin: top left</code>
    </div>

    <div class="tile tile--origin-br">
      <span class="tile__icon">◢</span>
      <strong>origin: bottom right</strong>
      <code>rotate(45deg) — origin: bottom right</code>
    </div>

  </div>

</body>
</html>
```

### CSS
```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #f0f2f5;
  color: #333;
}

h1 {
  font-size: 1.4rem;
  margin-bottom: 0.4rem;
}

.intro {
  color: #666;
  margin-bottom: 2rem;
  font-size: 0.95rem;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1.25rem;
}

.tile {
  background: white;
  border-radius: 10px;
  padding: 1.5rem 1rem;
  text-align: center;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.tile strong {
  font-size: 0.95rem;
  color: #222;
}

.tile code {
  font-size: 0.65rem;
  color: #666;
  line-height: 1.4;
  word-break: break-all;
}

.tile__icon {
  font-size: 1.6rem;
  margin-bottom: 0.25rem;
}

/* Individual hover transforms */
.tile--translate:hover    { transform: translateX(20px) translateY(-20px); box-shadow: 0 8px 20px rgba(0,0,0,0.12); }
.tile--rotate:hover       { transform: rotate(45deg); }
.tile--scale-up:hover     { transform: scale(1.3); box-shadow: 0 12px 30px rgba(0,0,0,0.15); }
.tile--scale-down:hover   { transform: scale(0.7); }
.tile--skew:hover         { transform: skewX(20deg); }
.tile--combined:hover     { transform: rotate(15deg) scale(1.1) translateY(-8px); box-shadow: 0 12px 30px rgba(0,0,0,0.15); }

/* Transform origin demos — both rotate 45deg, different pivot */
.tile--origin-tl {
  transform-origin: top left;
}
.tile--origin-tl:hover { transform: rotate(45deg); }

.tile--origin-br {
  transform-origin: bottom right;
}
.tile--origin-br:hover { transform: rotate(45deg); }

/* Color-code the tiles */
.tile--translate    { border-top: 3px solid #4f6df5; }
.tile--rotate       { border-top: 3px solid #e67e22; }
.tile--scale-up     { border-top: 3px solid #2ecc71; }
.tile--scale-down   { border-top: 3px solid #e74c3c; }
.tile--skew         { border-top: 3px solid #9b59b6; }
.tile--combined     { border-top: 3px solid #1abc9c; }
.tile--origin-tl    { border-top: 3px solid #f39c12; }
.tile--origin-br    { border-top: 3px solid #34495e; }
```

### JS
```js
// No JavaScript needed for this demo
```

---

## CODEPEN 4 — 3D Card Flip

**Demonstrates:** perspective, transform-style: preserve-3d, backface-visibility, rotateY. A realistic card that flips to reveal a back face on hover.

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>3D Card Flip</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <h1>3D Card Flip</h1>
  <p class="intro">Hover the card to flip it. Click to keep it flipped.</p>

  <div class="cards">

    <!-- Card 1: hover to flip -->
    <div class="scene">
      <div class="card" id="card1">
        <div class="card__face card__face--front">
          <div class="card__content">
            <span class="card__emoji">🌐</span>
            <h2>HTML</h2>
            <p>Hover to flip</p>
          </div>
        </div>
        <div class="card__face card__face--back">
          <div class="card__content">
            <span class="card__emoji">📄</span>
            <h2>Structure</h2>
            <p>HTML defines the content and meaning of a web page.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Card 2: hover to flip -->
    <div class="scene">
      <div class="card" id="card2">
        <div class="card__face card__face--front">
          <div class="card__content">
            <span class="card__emoji">🎨</span>
            <h2>CSS</h2>
            <p>Hover to flip</p>
          </div>
        </div>
        <div class="card__face card__face--back">
          <div class="card__content">
            <span class="card__emoji">✨</span>
            <h2>Presentation</h2>
            <p>CSS controls layout, color, typography, and animation.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Card 3: hover to flip -->
    <div class="scene">
      <div class="card" id="card3">
        <div class="card__face card__face--front">
          <div class="card__content">
            <span class="card__emoji">⚡</span>
            <h2>JavaScript</h2>
            <p>Hover to flip</p>
          </div>
        </div>
        <div class="card__face card__face--back">
          <div class="card__content">
            <span class="card__emoji">🔧</span>
            <h2>Behavior</h2>
            <p>JavaScript adds interactivity, logic, and dynamic content.</p>
          </div>
        </div>
      </div>
    </div>

  </div>

</body>
</html>
```

### CSS
```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #1a1a2e;
  color: white;
  min-height: 100vh;
}

h1 {
  font-size: 1.4rem;
  margin-bottom: 0.4rem;
}

.intro {
  color: #aaa;
  margin-bottom: 2.5rem;
  font-size: 0.95rem;
}

.cards {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
}

/* ─── The scene provides the 3D perspective ─── */
.scene {
  perspective: 800px;
  width: 220px;
  height: 300px;
}

/* ─── The card is the 3D container that flips ─── */
.card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;         /* Critical: children exist in 3D space */
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

/* Flip on hover */
.scene:hover .card {
  transform: rotateY(180deg);
}

/* Flip and stay on click */
.card.is-flipped {
  transform: rotateY(180deg);
}

/* ─── Both faces position absolutely on top of each other ─── */
.card__face {
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 14px;
  backface-visibility: hidden;          /* Critical: hide when back is facing viewer */
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}

/* Front face */
.card__face--front {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Back face starts rotated 180deg — so it's "behind" the front */
.card__face--back {
  transform: rotateY(180deg);
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

/* Card content layout */
.card__content {
  text-align: center;
  color: white;
}

.card__emoji {
  font-size: 2.5rem;
  display: block;
  margin-bottom: 0.75rem;
}

.card__content h2 {
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
}

.card__content p {
  font-size: 0.85rem;
  opacity: 0.85;
  line-height: 1.5;
}
```

### JS
```js
// Click to lock a card in the flipped state (hover always works too)
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('click', () => {
    card.classList.toggle('is-flipped');
  });
});
```

---

## CODEPEN 5 — Practical UI Hover Effects (Transitions + Transforms Combined)

**Demonstrates:** Real-world patterns: button lift, image zoom, card raise, and icon spin. Each effect uses transitions and transforms together.

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Practical Hover Effects</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <h1>Practical Hover Effects</h1>
  <p class="intro">Hover each element to see transitions + transforms working together.</p>

  <section class="section">
    <h2>Button Lift</h2>
    <div class="demo-row">
      <button class="btn-lift btn-lift--primary">Primary Action</button>
      <button class="btn-lift btn-lift--ghost">Ghost Button</button>
      <button class="btn-lift btn-lift--danger">Delete</button>
    </div>
  </section>

  <section class="section">
    <h2>Card Raise</h2>
    <div class="cards-row">
      <div class="card-raise">
        <div class="card-raise__img" style="background: linear-gradient(135deg, #667eea, #764ba2);">🎨</div>
        <div class="card-raise__body">
          <h3>Design</h3>
          <p>Visual structure and aesthetics</p>
        </div>
      </div>
      <div class="card-raise">
        <div class="card-raise__img" style="background: linear-gradient(135deg, #f093fb, #f5576c);">⚡</div>
        <div class="card-raise__body">
          <h3>Performance</h3>
          <p>Speed and efficiency</p>
        </div>
      </div>
      <div class="card-raise">
        <div class="card-raise__img" style="background: linear-gradient(135deg, #4facfe, #00f2fe);">♿</div>
        <div class="card-raise__body">
          <h3>Accessibility</h3>
          <p>Usable by everyone</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <h2>Image Zoom</h2>
    <div class="demo-row">
      <div class="img-zoom">
        <div class="img-zoom__inner" style="background: linear-gradient(135deg, #a18cd1, #fbc2eb);">
          <span>Zoom on hover</span>
        </div>
      </div>
      <div class="img-zoom">
        <div class="img-zoom__inner" style="background: linear-gradient(135deg, #fccb90, #d57eeb);">
          <span>Zoom on hover</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <h2>Icon Interactions</h2>
    <div class="demo-row">
      <button class="icon-btn">
        <span class="icon-btn__icon">↓</span>
        <span>Download</span>
      </button>
      <button class="icon-btn icon-btn--rotate">
        <span class="icon-btn__icon">⚙</span>
        <span>Settings</span>
      </button>
      <button class="icon-btn icon-btn--scale">
        <span class="icon-btn__icon">♥</span>
        <span>Like</span>
      </button>
    </div>
  </section>

</body>
</html>
```

### CSS
```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #f5f6fa;
  color: #333;
}

h1 {
  font-size: 1.4rem;
  margin-bottom: 0.4rem;
}

.intro {
  color: #666;
  margin-bottom: 2rem;
  font-size: 0.95rem;
}

.section {
  margin-bottom: 3rem;
}

.section h2 {
  font-size: 1rem;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 1rem;
  font-size: 0.8rem;
}

.demo-row {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

/* ─── Button Lift ─── */
.btn-lift {
  padding: 0.7rem 1.6rem;
  border: none;
  border-radius: 7px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transform: translateY(0);
  box-shadow: 0 2px 6px rgba(0,0,0,0.12);
  transition: transform 0.15s ease-out, box-shadow 0.15s ease-out,
              background-color 0.15s ease;
}

.btn-lift--primary { background: #4f6df5; color: white; }
.btn-lift--ghost { background: white; color: #4f6df5; border: 2px solid #4f6df5; }
.btn-lift--danger { background: #e74c3c; color: white; }

.btn-lift:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.18);
}

.btn-lift:active {
  transform: translateY(-1px);
  box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}

/* ─── Card Raise ─── */
.cards-row {
  display: flex;
  gap: 1.25rem;
  flex-wrap: wrap;
}

.card-raise {
  background: white;
  border-radius: 12px;
  width: 180px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  overflow: hidden;
  transform: translateY(0);
  transition: transform 0.25s ease-out, box-shadow 0.25s ease-out;
  cursor: pointer;
}

.card-raise:hover {
  transform: translateY(-8px);
  box-shadow: 0 16px 40px rgba(0,0,0,0.14);
}

.card-raise__img {
  height: 90px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
}

.card-raise__body {
  padding: 1rem;
}

.card-raise__body h3 {
  font-size: 0.95rem;
  margin-bottom: 0.3rem;
}

.card-raise__body p {
  font-size: 0.8rem;
  color: #666;
}

/* ─── Image Zoom ─── */
.img-zoom {
  width: 200px;
  height: 130px;
  border-radius: 10px;
  overflow: hidden;     /* Critical: clips the scaled image */
}

.img-zoom__inner {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  font-weight: 700;
  color: white;
  transform: scale(1);
  transition: transform 0.4s ease-out;
}

.img-zoom:hover .img-zoom__inner {
  transform: scale(1.15);
}

/* ─── Icon Buttons ─── */
.icon-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  padding: 1rem 1.25rem;
  background: white;
  border: 1.5px solid #ddd;
  border-radius: 10px;
  cursor: pointer;
  font-size: 0.8rem;
  color: #444;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.icon-btn:hover {
  border-color: #4f6df5;
  box-shadow: 0 4px 12px rgba(79,109,245,0.15);
}

.icon-btn__icon {
  font-size: 1.6rem;
  display: block;
  transition: transform 0.3s ease;
}

/* Download: drop the arrow on hover */
.icon-btn:hover .icon-btn__icon {
  transform: translateY(3px);
}

/* Settings: spin the gear */
.icon-btn--rotate:hover .icon-btn__icon {
  transform: rotate(90deg);
}

/* Like: pulse scale the heart */
.icon-btn--scale:hover .icon-btn__icon {
  transform: scale(1.4);
  color: #e74c3c;
}
```

### JS
```js
// No JavaScript needed for this demo
```

---

## CODEPEN 6 — prefers-reduced-motion Demo

**Demonstrates:** A spinning/bouncing animation that respects the prefers-reduced-motion media query. Also includes a JavaScript toggle to simulate the effect so students can test it interactively.

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>prefers-reduced-motion</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <h1>Respecting Motion Preferences</h1>
  <p class="intro">
    Some users set their OS to <strong>Reduce Motion</strong> due to vestibular disorders,
    migraines, or personal preference. The <code>prefers-reduced-motion</code> media query
    lets us detect and respect that preference.
  </p>

  <div class="toggle-row">
    <button id="toggle-btn">Simulate: Reduce Motion OFF</button>
    <span id="status-label">Status: Full motion active</span>
  </div>

  <div class="demos" id="demo-area">

    <div class="demo-box">
      <div class="spinner">🌀</div>
      <p class="demo-label">Continuous spin</p>
      <p class="demo-sub">Reduced: pauses</p>
    </div>

    <div class="demo-box">
      <div class="bouncer">⚽</div>
      <p class="demo-label">Bounce animation</p>
      <p class="demo-sub">Reduced: no bounce</p>
    </div>

    <div class="demo-box">
      <button class="hover-btn">Hover me</button>
      <p class="demo-label">Hover transition</p>
      <p class="demo-sub">Reduced: instant snap</p>
    </div>

  </div>

  <div class="note">
    <p><strong>How to test for real:</strong></p>
    <ul>
      <li><strong>Mac:</strong> System Settings → Accessibility → Display → Reduce Motion</li>
      <li><strong>Windows:</strong> Settings → Ease of Access → Display → Show animations</li>
      <li><strong>Chrome DevTools:</strong> Rendering panel → Emulate CSS media feature <code>prefers-reduced-motion</code></li>
    </ul>
  </div>

</body>
</html>
```

### CSS
```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #1a1a2e;
  color: #eee;
  line-height: 1.6;
}

h1 {
  font-size: 1.4rem;
  margin-bottom: 0.5rem;
}

.intro {
  color: #aaa;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
  max-width: 560px;
}

.toggle-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

#toggle-btn {
  padding: 0.5rem 1.25rem;
  background: #4f6df5;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
}

#toggle-btn:hover { background: #3a56d4; }
#toggle-btn.reduced { background: #e74c3c; }

#status-label {
  font-size: 0.85rem;
  color: #aaa;
}

.demos {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  margin-bottom: 2rem;
}

.demo-box {
  background: rgba(255,255,255,0.06);
  border-radius: 12px;
  padding: 2rem 1.5rem;
  text-align: center;
  min-width: 160px;
}

.demo-label {
  font-weight: 600;
  font-size: 0.85rem;
  margin-top: 1rem;
  margin-bottom: 0.2rem;
}

.demo-sub {
  font-size: 0.75rem;
  color: #888;
}

/* === Spinner === */
.spinner {
  font-size: 2.5rem;
  display: inline-block;
  animation: spin 1.5s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

/* === Bouncer === */
.bouncer {
  font-size: 2rem;
  display: inline-block;
  animation: bounce 0.6s ease-in-out infinite alternate;
}

@keyframes bounce {
  from { transform: translateY(0); }
  to   { transform: translateY(-24px); }
}

/* === Hover button === */
.hover-btn {
  padding: 0.6rem 1.4rem;
  background: #2ecc71;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transform: translateY(0);
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  transition: transform 0.2s ease-out, box-shadow 0.2s ease-out;
}

.hover-btn:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.3);
}

/* =================================================
   PREFERS-REDUCED-MOTION — The real CSS media query
   This is what actually runs in a user's browser when
   they have Reduce Motion turned on in their OS.
   ================================================= */
@media (prefers-reduced-motion: reduce) {
  .spinner {
    animation: none;   /* Stop continuous spin */
  }

  .bouncer {
    animation: none;   /* Stop bouncing */
    transform: none;
  }

  .hover-btn {
    transition: none;  /* Instant state change */
  }
}

/* ============================================
   Simulated reduced motion for the demo button
   The JS adds/removes .force-reduced on #demo-area
   ============================================ */
#demo-area.force-reduced .spinner {
  animation: none;
}

#demo-area.force-reduced .bouncer {
  animation: none;
  transform: none;
}

#demo-area.force-reduced .hover-btn {
  transition: none;
}

/* Note box */
.note {
  background: rgba(255,255,255,0.06);
  border-left: 4px solid #f39c12;
  border-radius: 0 8px 8px 0;
  padding: 1rem 1.25rem;
  font-size: 0.85rem;
  max-width: 520px;
}

.note ul {
  margin-top: 0.5rem;
  padding-left: 1.25rem;
}

.note li {
  margin-bottom: 0.3rem;
}
```

### JS
```js
const btn = document.getElementById('toggle-btn');
const label = document.getElementById('status-label');
const demoArea = document.getElementById('demo-area');

let reduced = false;

btn.addEventListener('click', () => {
  reduced = !reduced;

  // Toggle the simulation class
  demoArea.classList.toggle('force-reduced', reduced);

  // Update button and label
  btn.textContent = reduced
    ? 'Simulate: Reduce Motion ON'
    : 'Simulate: Reduce Motion OFF';

  btn.classList.toggle('reduced', reduced);

  label.textContent = reduced
    ? 'Status: Reduced motion active — animations paused'
    : 'Status: Full motion active';
});
```
