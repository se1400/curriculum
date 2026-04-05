# Day 20 — CodePen Examples
## Toggle Everything: classList.toggle() and the UI Patterns Every Website Uses

---

## CodePen 1 — Dark Mode Toggle

**Placement:** After the "Dark Mode Toggle" section.
**Demonstrates:** `classList.toggle('dark-mode')` on `document.body`, CSS custom properties switching entire page theme, `classList.contains()` for button label update, smooth transitions.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dark Mode Toggle</title>
  <style>
    /* ── Two states defined in CSS ──────────────────────────── */
    :root {
      --bg:      #f8f9fa;
      --surface: #ffffff;
      --text:    #1a1a2e;
      --muted:   #636e72;
      --accent:  #6c5ce7;
      --border:  #dee2e6;
    }

    body.dark-mode {
      --bg:      #1a1a2e;
      --surface: #16213e;
      --text:    #eeeeee;
      --muted:   #adb5bd;
      --accent:  #a29bfe;
      --border:  #2d3561;
    }

    /* ── All transitions live in CSS — JS only toggles the class ── */
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      padding: 2rem;
      transition: background 0.35s ease, color 0.35s ease;
    }

    /* ── Header ────────────────────────────────────────────── */
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border);
      transition: border-color 0.35s;
    }

    .logo {
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--accent);
      transition: color 0.35s;
    }

    .toggle-btn {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem 1rem;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 100px;
      color: var(--text);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.35s, border-color 0.35s, color 0.35s;
    }

    /* ── Cards ─────────────────────────────────────────────── */
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem;
      margin-bottom: 1.5rem;
    }

    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
      transition: background 0.35s, border-color 0.35s;
    }

    .card-icon {
      font-size: 1.5rem;
      margin-bottom: 0.75rem;
    }

    .card h3 {
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 0.35rem;
      color: var(--accent);
      transition: color 0.35s;
    }

    .card p {
      font-size: 0.82rem;
      color: var(--muted);
      line-height: 1.5;
      transition: color 0.35s;
    }

    /* ── Code note ──────────────────────────────────────────── */
    .note {
      background: var(--surface);
      border: 1px solid var(--border);
      border-left: 3px solid var(--accent);
      border-radius: 8px;
      padding: 0.85rem 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      color: var(--muted);
      transition: background 0.35s, border-color 0.35s, color 0.35s;
    }

    .note strong { color: var(--accent); transition: color 0.35s; }
  </style>
</head>
<body>

  <div class="header">
    <span class="logo">&#9670; MyPortfolio</span>
    <button class="toggle-btn" id="theme-btn">
      <span id="theme-icon">&#9790;</span>
      <span id="theme-label">Dark Mode</span>
    </button>
  </div>

  <div class="grid">
    <div class="card">
      <div class="card-icon">&#127775;</div>
      <h3>Design</h3>
      <p>Every color on this page reads from a CSS custom property. Change one variable, the whole page shifts.</p>
    </div>
    <div class="card">
      <div class="card-icon">&#9889;</div>
      <h3>JavaScript</h3>
      <p>One line toggles the dark-mode class. CSS transitions handle the rest — no animation logic in JS.</p>
    </div>
    <div class="card">
      <div class="card-icon">&#9654;</div>
      <h3>Performance</h3>
      <p>Opacity and color transitions are GPU-accelerated. This toggle costs nothing in performance.</p>
    </div>
  </div>

  <div class="note">
    <strong>The JS:</strong> document.body.classList.toggle('dark-mode')  &mdash;  that's the entire toggle.
  </div>

  <script>
    const btn   = document.querySelector('#theme-btn');
    const icon  = document.querySelector('#theme-icon');
    const label = document.querySelector('#theme-label');

    btn.addEventListener('click', function() {
      // One line — CSS custom properties and transitions do everything else
      document.body.classList.toggle('dark-mode');

      const isDark = document.body.classList.contains('dark-mode');
      icon.textContent  = isDark ? '&#9728;' : '&#9790;';
      label.textContent = isDark ? 'Light Mode' : 'Dark Mode';
    });
  </script>

</body>
</html>
```

---

## CodePen 2 — Accordion

**Placement:** After the "Accordion" section.
**Demonstrates:** `max-height` transition trick, `classList.toggle('open')`, single-open mode (close others when one opens), `aria-expanded` toggling. Pays off Lesson 9 transitions.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Accordion</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      gap: 0.5rem;
    }

    h1 {
      font-size: 1.2rem;
      color: #a29bfe;
      margin-bottom: 1rem;
      text-align: center;
    }

    .accordion {
      width: 100%;
      max-width: 560px;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .accordion-item {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 10px;
      overflow: hidden;
      transition: border-color 0.3s;
    }

    .accordion-item.open {
      border-color: #6c5ce7;
    }

    /* ── Header / trigger ─────────────────────────────────── */
    .accordion-header {
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 1.25rem;
      background: transparent;
      border: none;
      color: #eee;
      font-size: 0.95rem;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      font-family: inherit;
    }

    .accordion-header:hover { background: rgba(108,92,231,0.08); }

    .chevron {
      font-size: 0.75rem;
      color: #6c5ce7;
      transition: transform 0.3s ease;
    }

    .accordion-item.open .chevron {
      transform: rotate(180deg);
    }

    /* ── Body — max-height transition ────────────────────── */
    .accordion-body {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.35s ease;
    }

    .accordion-item.open .accordion-body {
      max-height: 300px;  /* Larger than any content */
    }

    .accordion-content {
      padding: 0 1.25rem 1.25rem;
      font-size: 0.88rem;
      color: #b2bec3;
      line-height: 1.7;
      border-top: 1px solid #2d3561;
      padding-top: 1rem;
    }

    .accordion-content code {
      background: #0d1117;
      padding: 0.1rem 0.4rem;
      border-radius: 3px;
      font-size: 0.82rem;
      color: #a29bfe;
    }
  </style>
</head>
<body>

  <h1>Accordion — Click to Expand</h1>

  <div class="accordion">

    <div class="accordion-item">
      <button class="accordion-header" aria-expanded="false">
        How does the animation work?
        <span class="chevron">&#9660;</span>
      </button>
      <div class="accordion-body">
        <div class="accordion-content">
          The body starts at <code>max-height: 0</code> with <code>overflow: hidden</code>. When the <code>.open</code> class is added, <code>max-height</code> jumps to a large value. The CSS <code>transition</code> on <code>max-height</code> animates that change smoothly. JavaScript never touches timing or easing &mdash; it just toggles the class.
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-header" aria-expanded="false">
        Why use max-height instead of height?
        <span class="chevron">&#9660;</span>
      </button>
      <div class="accordion-body">
        <div class="accordion-content">
          CSS cannot transition to <code>height: auto</code> (it doesn&rsquo;t know the final value). <code>max-height</code> works because you set it to a number larger than the content, and CSS can transition between two known numbers. The catch: make sure your <code>max-height</code> is bigger than the tallest possible content.
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-header" aria-expanded="false">
        What is aria-expanded for?
        <span class="chevron">&#9660;</span>
      </button>
      <div class="accordion-body">
        <div class="accordion-content">
          Screen readers announce the state of interactive elements. Setting <code>aria-expanded="true"</code> when open and <code>aria-expanded="false"</code> when closed tells assistive technology whether the section is currently visible. It takes one line of JavaScript and makes your accordion usable by everyone.
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-header" aria-expanded="false">
        Can multiple panels be open at once?
        <span class="chevron">&#9660;</span>
      </button>
      <div class="accordion-body">
        <div class="accordion-content">
          That depends on your design choice. This demo uses single-open mode: opening one panel closes all others. To allow multiple open at once, remove the &ldquo;close others&rdquo; loop and just toggle the clicked item. Both are valid patterns for different use cases.
        </div>
      </div>
    </div>

  </div>

  <script>
    const items = document.querySelectorAll('.accordion-item');

    items.forEach(function(item) {
      const header = item.querySelector('.accordion-header');

      header.addEventListener('click', function() {
        const isCurrentlyOpen = item.classList.contains('open');

        // Close all items (single-open mode)
        items.forEach(function(el) {
          el.classList.remove('open');
          el.querySelector('.accordion-header').setAttribute('aria-expanded', 'false');
        });

        // If this item was closed, open it
        if (!isCurrentlyOpen) {
          item.classList.add('open');
          header.setAttribute('aria-expanded', 'true');
        }
      });
    });
  </script>

</body>
</html>
```

---

## CodePen 3 — Real Hamburger Navigation

**Placement:** After the "Real Hamburger Menu" section.
**Demonstrates:** `classList.toggle('nav-open')` replacing the CSS checkbox hack from Lesson 13, `aria-expanded` update, slide-in transition. Students recognize this pattern immediately.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hamburger Navigation</title>
  <style>
    :root {
      --accent: #6c5ce7;
      --bg:     #1a1a2e;
      --nav-bg: #16213e;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: var(--bg);
      color: #eee;
      min-height: 100vh;
    }

    /* ── Top bar ───────────────────────────────────────────── */
    .topbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 1.5rem;
      background: var(--nav-bg);
      border-bottom: 1px solid #2d3561;
      position: relative;
      z-index: 10;
    }

    .logo {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--accent);
    }

    /* ── Hamburger button ──────────────────────────────────── */
    .menu-btn {
      background: none;
      border: none;
      color: #eee;
      font-size: 1.4rem;
      cursor: pointer;
      width: 2.5rem;
      height: 2.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 6px;
      transition: background 0.2s;
    }

    .menu-btn:hover { background: rgba(255,255,255,0.08); }

    /* ── Nav overlay — slides in from right ────────────────── */
    .nav-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0);
      pointer-events: none;
      transition: background 0.3s;
      z-index: 20;
    }

    .nav-overlay.nav-open {
      background: rgba(0,0,0,0.5);
      pointer-events: auto;
    }

    .nav-links {
      position: absolute;
      top: 0;
      right: -280px;
      width: 280px;
      height: 100%;
      background: var(--nav-bg);
      padding: 5rem 2rem 2rem;
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      transition: right 0.3s ease;
      border-left: 1px solid #2d3561;
    }

    /* JS toggles .nav-open on the overlay — CSS handles the slide */
    .nav-overlay.nav-open .nav-links {
      right: 0;
    }

    .nav-links a {
      display: block;
      padding: 0.75rem 1rem;
      color: #eee;
      text-decoration: none;
      border-radius: 8px;
      font-size: 1rem;
      transition: background 0.2s, color 0.2s;
    }

    .nav-links a:hover {
      background: rgba(108,92,231,0.15);
      color: var(--accent);
    }

    .nav-links a.active {
      background: rgba(108,92,231,0.2);
      color: var(--accent);
    }

    /* ── Page content ──────────────────────────────────────── */
    .page-content {
      padding: 2rem 1.5rem;
      max-width: 600px;
    }

    .page-content h1 {
      font-size: 1.5rem;
      color: var(--accent);
      margin-bottom: 0.5rem;
    }

    .page-content p {
      font-size: 0.9rem;
      opacity: 0.65;
      line-height: 1.7;
      margin-bottom: 1rem;
    }

    .note {
      background: #16213e;
      border: 1px solid #2d3561;
      border-left: 3px solid var(--accent);
      border-radius: 8px;
      padding: 1rem;
      font-size: 0.82rem;
      color: #b2bec3;
    }
  </style>
</head>
<body>

  <div class="topbar">
    <span class="logo">&#9670; Studio</span>
    <button class="menu-btn" id="menu-btn" aria-expanded="false" aria-label="Open menu">
      &#9776;
    </button>
  </div>

  <!-- Overlay contains both the backdrop and the nav -->
  <div class="nav-overlay" id="nav-overlay">
    <nav class="nav-links">
      <a href="#" class="active">Home</a>
      <a href="#">Work</a>
      <a href="#">About</a>
      <a href="#">Services</a>
      <a href="#">Contact</a>
    </nav>
  </div>

  <div class="page-content">
    <h1>Real Hamburger Navigation</h1>
    <p>In Lesson 13 you built a hamburger menu with a hidden checkbox and CSS sibling selectors &mdash; a clever hack. Now you can do it properly: <code>classList.toggle()</code> slides the nav in, <code>aria-expanded</code> keeps it accessible, and clicking the backdrop closes it.</p>

    <div class="note">
      The CSS is almost identical to Lesson 13. The difference is that JavaScript adds and removes the class instead of relying on <code>:checked</code>. Cleaner code, same visual result.
    </div>
  </div>

  <script>
    const menuBtn  = document.querySelector('#menu-btn');
    const overlay  = document.querySelector('#nav-overlay');

    function openNav() {
      overlay.classList.add('nav-open');
      menuBtn.setAttribute('aria-expanded', 'true');
      menuBtn.innerHTML = '&#10005;';  // ✕ close icon
      menuBtn.setAttribute('aria-label', 'Close menu');
    }

    function closeNav() {
      overlay.classList.remove('nav-open');
      menuBtn.setAttribute('aria-expanded', 'false');
      menuBtn.innerHTML = '&#9776;';  // ☰ hamburger icon
      menuBtn.setAttribute('aria-label', 'Open menu');
    }

    menuBtn.addEventListener('click', function() {
      if (overlay.classList.contains('nav-open')) {
        closeNav();
      } else {
        openNav();
      }
    });

    // Close when clicking the backdrop
    overlay.addEventListener('click', function(event) {
      if (event.target === overlay) closeNav();
    });
  </script>

</body>
</html>
```

---

## CodePen 4 — Modal + Toast Notification

**Placement:** After the "Modal Dialog" section.
**Demonstrates:** Modal open/close with `classList.add/remove`, backdrop click to close, `setTimeout` for auto-dismissing toast notification. Combines the modal and setTimeout concepts in one demo.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modal + Toast</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 1rem;
      padding: 2rem;
    }

    h1 { font-size: 1.3rem; color: #a29bfe; }

    .subtitle { font-size: 0.85rem; opacity: 0.55; text-align: center; }

    /* ── Trigger buttons ──────────────────────────────────── */
    .btn-row { display: flex; gap: 0.75rem; }

    .btn {
      padding: 0.65rem 1.5rem;
      border: none;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
    }

    .btn-primary { background: #6c5ce7; color: #fff; }
    .btn-outline { background: transparent; border: 2px solid #6c5ce7; color: #a29bfe; }

    /* ── Modal overlay ────────────────────────────────────── */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
      z-index: 100;
    }

    .modal-overlay.open {
      opacity: 1;
      pointer-events: auto;
    }

    .modal {
      background: #16213e;
      border: 1px solid #2d3561;
      border-radius: 16px;
      padding: 2rem;
      max-width: 420px;
      width: 100%;
      transform: translateY(12px);
      transition: transform 0.25s ease;
    }

    .modal-overlay.open .modal {
      transform: translateY(0);
    }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 1rem;
    }

    .modal-header h2 { font-size: 1.1rem; color: #a29bfe; }

    .close-btn {
      background: none;
      border: none;
      color: #636e72;
      font-size: 1.2rem;
      cursor: pointer;
      line-height: 1;
      padding: 0;
    }

    .modal p { font-size: 0.88rem; color: #b2bec3; line-height: 1.7; margin-bottom: 1.25rem; }

    .modal-footer { display: flex; gap: 0.6rem; justify-content: flex-end; }

    /* ── Toast notification ───────────────────────────────── */
    .toast {
      position: fixed;
      bottom: 1.5rem;
      left: 50%;
      transform: translateX(-50%) translateY(120%);
      background: #00b894;
      color: #fff;
      padding: 0.75rem 1.5rem;
      border-radius: 100px;
      font-size: 0.88rem;
      font-weight: 600;
      white-space: nowrap;
      transition: transform 0.3s ease;
      z-index: 200;
    }

    .toast.visible {
      transform: translateX(-50%) translateY(0);
    }
  </style>
</head>
<body>

  <h1>Modal + Toast</h1>
  <p class="subtitle">Open the modal, then confirm to see the toast auto-dismiss.</p>

  <div class="btn-row">
    <button class="btn btn-primary" id="open-modal-btn">Open Modal</button>
    <button class="btn btn-outline"  id="toast-only-btn">Show Toast Only</button>
  </div>

  <!-- Modal -->
  <div class="modal-overlay" id="modal-overlay">
    <div class="modal">
      <div class="modal-header">
        <h2>Confirm Action</h2>
        <button class="close-btn" id="close-btn" aria-label="Close">&times;</button>
      </div>
      <p>This is a modal dialog. The backdrop is a semi-transparent overlay. Click outside the modal or the close button to dismiss it. After confirming, a toast notification will appear and auto-dismiss after 3 seconds.</p>
      <div class="modal-footer">
        <button class="btn btn-outline"  id="cancel-btn">Cancel</button>
        <button class="btn btn-primary"  id="confirm-btn">Confirm</button>
      </div>
    </div>
  </div>

  <!-- Toast -->
  <div class="toast" id="toast">Action confirmed!</div>

  <script>
    const overlay    = document.querySelector('#modal-overlay');
    const toast      = document.querySelector('#toast');
    let toastTimeout = null;

    function openModal() {
      overlay.classList.add('open');
    }

    function closeModal() {
      overlay.classList.remove('open');
    }

    function showToast(message) {
      toast.textContent = message;
      toast.classList.add('visible');

      // Cancel any existing timer before starting a new one
      clearTimeout(toastTimeout);

      // Auto-dismiss after 3 seconds
      toastTimeout = setTimeout(function() {
        toast.classList.remove('visible');
      }, 3000);
    }

    // Open modal
    document.querySelector('#open-modal-btn').addEventListener('click', openModal);

    // Close modal — three different triggers, same function
    document.querySelector('#close-btn').addEventListener('click', closeModal);
    document.querySelector('#cancel-btn').addEventListener('click', closeModal);

    // Backdrop click — only close if the overlay itself was clicked, not the modal inside
    overlay.addEventListener('click', function(event) {
      if (event.target === overlay) closeModal();
    });

    // Confirm button: close modal, show toast
    document.querySelector('#confirm-btn').addEventListener('click', function() {
      closeModal();
      showToast('Action confirmed! This toast dismisses in 3 seconds.');
    });

    // Toast-only button (for testing setTimeout independently)
    document.querySelector('#toast-only-btn').addEventListener('click', function() {
      showToast('Toast notification — auto-dismisses after 3 seconds.');
    });
  </script>

</body>
</html>
```

---

## CodePen 5 — Live Clock with setInterval

**Placement:** After the "setInterval — Repeated Actions" section.
**Demonstrates:** `setInterval` updating a clock every second, `clearInterval` to stop it, the `Date` object for getting hours/minutes/seconds, `padStart()` for zero-padding.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Live Clock</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #1a1a2e;
      color: #eee;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 1.5rem;
      padding: 2rem;
    }

    .clock-card {
      background: #16213e;
      border: 2px solid #6c5ce7;
      border-radius: 20px;
      padding: 2.5rem 3.5rem;
      text-align: center;
    }

    .clock-label {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #6c5ce7;
      margin-bottom: 0.75rem;
    }

    .clock-time {
      font-size: 4rem;
      font-weight: 800;
      font-family: 'Courier New', monospace;
      color: #eee;
      letter-spacing: 0.05em;
      font-variant-numeric: tabular-nums;
      line-height: 1;
    }

    .clock-time .separator {
      color: #6c5ce7;
      animation: blink 1s step-end infinite;
    }

    @keyframes blink {
      0%, 100% { opacity: 1; }
      50%       { opacity: 0.3; }
    }

    .clock-date {
      font-size: 0.85rem;
      color: #636e72;
      margin-top: 0.75rem;
    }

    /* ── Controls ─────────────────────────────────────────── */
    .controls { display: flex; gap: 0.75rem; }

    .btn {
      padding: 0.55rem 1.25rem;
      border: none;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
    }

    .btn-stop  { background: #d63031; color: #fff; }
    .btn-start { background: #00b894; color: #fff; }
    .btn-start:disabled,
    .btn-stop:disabled  { opacity: 0.35; cursor: not-allowed; }

    /* ── Interval counter panel ───────────────────────────── */
    .meta-panel {
      background: #0d1117;
      border-radius: 10px;
      padding: 0.75rem 1.25rem;
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      color: #aaa;
      text-align: center;
      line-height: 1.8;
    }

    .meta-panel .hl { color: #55efc4; }
  </style>
</head>
<body>

  <div class="clock-card">
    <p class="clock-label">Current Time</p>
    <p class="clock-time">
      <span id="hours">00</span><span class="separator">:</span><span id="minutes">00</span><span class="separator">:</span><span id="seconds">00</span>
    </p>
    <p class="clock-date" id="clock-date"></p>
  </div>

  <div class="controls">
    <button class="btn btn-stop"  id="stop-btn">Stop Clock</button>
    <button class="btn btn-start" id="start-btn" disabled>Start Clock</button>
  </div>

  <div class="meta-panel">
    setInterval fires every: <span class="hl">1000ms</span><br>
    Tick count: <span class="hl" id="tick-count">0</span><br>
    Status: <span class="hl" id="status">Running</span>
  </div>

  <script>
    let clockId   = null;
    let tickCount = 0;

    const days   = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

    function updateClock() {
      const now = new Date();

      // padStart(2, '0') adds a leading zero if the number is single-digit
      const h = String(now.getHours()).padStart(2, '0');
      const m = String(now.getMinutes()).padStart(2, '0');
      const s = String(now.getSeconds()).padStart(2, '0');

      document.querySelector('#hours').textContent   = h;
      document.querySelector('#minutes').textContent = m;
      document.querySelector('#seconds').textContent = s;

      // Build a readable date string
      const dayName   = days[now.getDay()];
      const monthName = months[now.getMonth()];
      const date      = now.getDate();
      const year      = now.getFullYear();
      document.querySelector('#clock-date').textContent = dayName + ', ' + monthName + ' ' + date + ', ' + year;

      tickCount = tickCount + 1;
      document.querySelector('#tick-count').textContent = tickCount;
    }

    function startClock() {
      if (clockId !== null) return;  // Already running
      updateClock();  // Run once immediately so there is no 1-second blank
      clockId = setInterval(updateClock, 1000);
      document.querySelector('#status').textContent = 'Running';
      document.querySelector('#stop-btn').disabled  = false;
      document.querySelector('#start-btn').disabled = true;
    }

    function stopClock() {
      clearInterval(clockId);
      clockId = null;
      document.querySelector('#status').textContent = 'Stopped';
      document.querySelector('#stop-btn').disabled  = true;
      document.querySelector('#start-btn').disabled = false;
    }

    document.querySelector('#stop-btn').addEventListener('click',  stopClock);
    document.querySelector('#start-btn').addEventListener('click', startClock);

    // Start immediately on page load
    startClock();
  </script>

</body>
</html>
```
