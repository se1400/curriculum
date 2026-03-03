# Day 13 — HTML Forms: CodePen Code Blocks

Each section below contains the HTML, CSS, and JS for one CodePen embed referenced in the article.

---

## CODEPEN 1 — Basic Text-Type Inputs

**HTML**
```html
<form action="#" method="post" novalidate>

  <div class="form-group">
    <label for="name">Full Name</label>
    <input type="text" id="name" name="name" placeholder="Jane Smith">
  </div>

  <div class="form-group">
    <label for="email">Email Address</label>
    <input type="email" id="email" name="email" placeholder="jane@example.com">
  </div>

  <div class="form-group">
    <label for="password">Password</label>
    <input type="password" id="password" name="password" placeholder="At least 8 characters">
  </div>

  <div class="form-group">
    <label for="website">Website (optional)</label>
    <input type="url" id="website" name="website" placeholder="https://example.com">
  </div>

  <div class="form-group">
    <label for="phone">Phone Number</label>
    <input type="tel" id="phone" name="phone" placeholder="(555) 555-5555">
  </div>

  <div class="form-group">
    <label for="qty">Quantity</label>
    <input type="number" id="qty" name="qty" min="1" max="99" value="1">
  </div>

  <button type="submit">Create Account</button>

</form>
```

**CSS**
```css
* {
  box-sizing: border-box;
}

body {
  font-family: system-ui, sans-serif;
  max-width: 480px;
  margin: 2rem auto;
  padding: 0 1rem;
  color: #333;
}

.form-group {
  margin-bottom: 1.25rem;
}

label {
  display: block;
  margin-bottom: 0.35rem;
  font-weight: 600;
  font-size: 0.9rem;
}

input {
  width: 100%;
  padding: 0.6rem 0.75rem;
  border: 1.5px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  transition: border-color 0.2s, box-shadow 0.2s;
}

input:focus {
  outline: none;
  border-color: #4f6df5;
  box-shadow: 0 0 0 3px rgba(79, 109, 245, 0.15);
}

button {
  width: 100%;
  padding: 0.75rem;
  background: #4f6df5;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  margin-top: 0.5rem;
}

button:hover {
  background: #3a56d4;
}
```

**JS**
```js
// No JavaScript needed for this demo
```

---

## CODEPEN 2 — Date, Time, Range, Color, Checkbox, and Radio Inputs

**HTML**
```html
<form>

  <h2>Date &amp; Time Inputs</h2>

  <div class="form-group">
    <label for="birthday">Date</label>
    <input type="date" id="birthday" name="birthday">
  </div>

  <div class="form-group">
    <label for="meettime">Time</label>
    <input type="time" id="meettime" name="meettime">
  </div>

  <div class="form-group">
    <label for="appt">Date &amp; Time</label>
    <input type="datetime-local" id="appt" name="appt">
  </div>

  <div class="form-group">
    <label for="billing">Month</label>
    <input type="month" id="billing" name="billing">
  </div>

  <hr>

  <h2>Range &amp; Color</h2>

  <div class="form-group">
    <label for="volume">Volume: <output id="vol-out">50</output></label>
    <input type="range" id="volume" name="volume" min="0" max="100" value="50">
  </div>

  <div class="form-group">
    <label for="theme-color">Theme Color</label>
    <input type="color" id="theme-color" name="theme-color" value="#4f6df5">
  </div>

  <hr>

  <h2>Checkboxes</h2>

  <div class="form-group check-group">
    <label><input type="checkbox" name="toppings" value="cheese"> Cheese</label>
    <label><input type="checkbox" name="toppings" value="peppers" checked> Peppers</label>
    <label><input type="checkbox" name="toppings" value="mushrooms"> Mushrooms</label>
  </div>

  <h2>Radio Buttons</h2>

  <div class="form-group check-group">
    <label><input type="radio" name="size" value="sm"> Small</label>
    <label><input type="radio" name="size" value="md" checked> Medium</label>
    <label><input type="radio" name="size" value="lg"> Large</label>
  </div>

</form>
```

**CSS**
```css
* { box-sizing: border-box; }

body {
  font-family: system-ui, sans-serif;
  max-width: 480px;
  margin: 2rem auto;
  padding: 0 1rem;
  color: #333;
}

h2 {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #4f6df5;
  margin: 1.5rem 0 0.6rem;
}

hr {
  border: none;
  border-top: 1px solid #eee;
  margin: 1.5rem 0;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.35rem;
  font-weight: 600;
  font-size: 0.9rem;
}

input[type="date"],
input[type="time"],
input[type="datetime-local"],
input[type="month"] {
  padding: 0.5rem 0.6rem;
  border: 1.5px solid #ccc;
  border-radius: 4px;
  font-size: 0.95rem;
}

input[type="range"] {
  width: 100%;
  accent-color: #4f6df5;
  margin-top: 0.25rem;
}

input[type="color"] {
  width: 48px;
  height: 36px;
  border: 1.5px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
  padding: 2px;
}

.check-group label {
  font-weight: normal;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.4rem;
}
```

**JS**
```js
const rangeInput = document.getElementById('volume');
const rangeOutput = document.getElementById('vol-out');

rangeInput.addEventListener('input', () => {
  rangeOutput.textContent = rangeInput.value;
});
```

---

## CODEPEN 3 — Select, Datalist, Textarea, and Fieldset/Legend

**HTML**
```html
<form>

  <fieldset>
    <legend>Contact Preferences</legend>
    <div class="radio-group">
      <label><input type="radio" name="contact" value="email" checked> Email</label>
      <label><input type="radio" name="contact" value="phone"> Phone</label>
      <label><input type="radio" name="contact" value="text"> Text Message</label>
    </div>
  </fieldset>

  <div class="form-group">
    <label for="country">Country</label>
    <select id="country" name="country">
      <option value="">-- Select a country --</option>
      <optgroup label="North America">
        <option value="us">United States</option>
        <option value="ca">Canada</option>
        <option value="mx">Mexico</option>
      </optgroup>
      <optgroup label="Europe">
        <option value="uk">United Kingdom</option>
        <option value="de">Germany</option>
        <option value="fr">France</option>
      </optgroup>
    </select>
  </div>

  <div class="form-group">
    <label for="browser">Favorite Browser</label>
    <input type="text" id="browser" name="browser"
           list="browser-options" placeholder="Start typing...">
    <datalist id="browser-options">
      <option value="Chrome">
      <option value="Firefox">
      <option value="Safari">
      <option value="Edge">
      <option value="Opera">
    </datalist>
  </div>

  <div class="form-group">
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="4"
              placeholder="Write your message here..."></textarea>
  </div>

  <button type="submit">Send</button>

</form>
```

**CSS**
```css
* { box-sizing: border-box; }

body {
  font-family: system-ui, sans-serif;
  max-width: 480px;
  margin: 2rem auto;
  padding: 0 1rem;
  color: #333;
}

fieldset {
  border: 1.5px solid #ccc;
  border-radius: 6px;
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
}

legend {
  font-weight: 700;
  padding: 0 0.4rem;
  color: #4f6df5;
}

.radio-group label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.4rem;
  font-size: 0.95rem;
  font-weight: normal;
}

.form-group {
  margin-bottom: 1.25rem;
}

label {
  display: block;
  margin-bottom: 0.35rem;
  font-weight: 600;
  font-size: 0.9rem;
}

input[type="text"],
select,
textarea {
  width: 100%;
  padding: 0.6rem 0.75rem;
  border: 1.5px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  font-family: inherit;
  transition: border-color 0.2s, box-shadow 0.2s;
}

textarea {
  resize: vertical;
  min-height: 80px;
}

input:focus,
select:focus,
textarea:focus {
  outline: none;
  border-color: #4f6df5;
  box-shadow: 0 0 0 3px rgba(79, 109, 245, 0.15);
}

button {
  padding: 0.7rem 2rem;
  background: #4f6df5;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
}

button:hover {
  background: #3a56d4;
}
```

**JS**
```js
// No JavaScript needed for this demo
```

---

## CODEPEN 4 — HTML5 Validation Attributes in Action

**HTML**
```html
<form id="signup-form" novalidate>

  <h2>Create Account</h2>

  <div class="form-group">
    <label for="username">Username <span class="req">*</span></label>
    <input type="text" id="username" name="username"
           minlength="3" maxlength="20"
           pattern="[a-zA-Z0-9_]+"
           title="3–20 characters: letters, numbers, and underscores only"
           placeholder="e.g. cool_coder42"
           required>
    <span class="hint">3–20 characters — letters, numbers, underscores only</span>
  </div>

  <div class="form-group">
    <label for="reg-email">Email <span class="req">*</span></label>
    <input type="email" id="reg-email" name="email"
           placeholder="jane@example.com"
           required>
  </div>

  <div class="form-group">
    <label for="age">Age <span class="req">*</span></label>
    <input type="number" id="age" name="age"
           min="13" max="120"
           placeholder="Must be 13 or older"
           required>
  </div>

  <div class="form-group">
    <label for="zip">ZIP Code <span class="req">*</span></label>
    <input type="text" id="zip" name="zip"
           pattern="[0-9]{5}(-[0-9]{4})?"
           title="5-digit ZIP code, or ZIP+4 format (e.g. 12345 or 12345-6789)"
           placeholder="12345"
           required>
  </div>

  <button type="submit">Sign Up</button>

  <p id="success-msg" hidden>✅ All fields are valid! (Data would be submitted in a real form.)</p>

</form>
```

**CSS**
```css
* { box-sizing: border-box; }

body {
  font-family: system-ui, sans-serif;
  max-width: 480px;
  margin: 2rem auto;
  padding: 0 1rem;
  color: #333;
}

h2 { margin-top: 0; }

.form-group {
  margin-bottom: 1.25rem;
}

label {
  display: block;
  margin-bottom: 0.35rem;
  font-weight: 600;
  font-size: 0.9rem;
}

.req {
  color: #e53e3e;
  font-weight: normal;
}

.hint {
  display: block;
  font-size: 0.8rem;
  color: #666;
  margin-top: 0.25rem;
}

input {
  width: 100%;
  padding: 0.6rem 0.75rem;
  border: 1.5px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  transition: border-color 0.2s, box-shadow 0.2s, background-color 0.2s;
}

input:focus {
  outline: none;
  border-color: #4f6df5;
  box-shadow: 0 0 0 3px rgba(79, 109, 245, 0.15);
}

/* Valid state — only after user has typed something */
input:not(:placeholder-shown):valid {
  border-color: #38a169;
  background-color: #f0fff4;
}

/* Invalid state — only after user has typed something */
input:not(:placeholder-shown):invalid {
  border-color: #e53e3e;
  background-color: #fff5f5;
}

button {
  width: 100%;
  padding: 0.75rem;
  background: #4f6df5;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  margin-top: 0.25rem;
}

button:hover {
  background: #3a56d4;
}

#success-msg {
  margin-top: 1rem;
  padding: 0.75rem 1rem;
  background: #f0fff4;
  border: 1px solid #38a169;
  border-radius: 4px;
  color: #276749;
}
```

**JS**
```js
const form = document.getElementById('signup-form');
const successMsg = document.getElementById('success-msg');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  if (form.checkValidity()) {
    successMsg.hidden = false;
  } else {
    // Trigger the browser's built-in validation tooltips
    form.reportValidity();
  }
});
```

---

## CODEPEN 5 — Form Pseudo-Classes: Live Validation Feedback

**HTML**
```html
<form novalidate>

  <h2>Live Validation Demo</h2>
  <p class="intro">Fill in each field and watch the border color change based on your input.</p>

  <div class="form-group">
    <label for="p-email">
      Email Address
      <span class="req">(required)</span>
    </label>
    <input type="email" id="p-email" name="email"
           placeholder="jane@example.com"
           required>
    <span class="feedback valid-msg">✓ Looks good!</span>
    <span class="feedback invalid-msg">Please enter a valid email address.</span>
  </div>

  <div class="form-group">
    <label for="p-username">
      Username
      <span class="req">(required, 3–15 characters)</span>
    </label>
    <input type="text" id="p-username" name="username"
           minlength="3" maxlength="15"
           placeholder="minimum 3 characters"
           required>
    <span class="feedback valid-msg">✓ Username looks good!</span>
    <span class="feedback invalid-msg">Must be between 3 and 15 characters.</span>
  </div>

  <div class="form-group">
    <label for="p-url">
      Website
      <span class="req">(optional)</span>
    </label>
    <input type="url" id="p-url" name="website"
           placeholder="https://example.com">
    <span class="feedback valid-msg">✓ Valid URL!</span>
    <span class="feedback invalid-msg">Please include https:// at the start.</span>
  </div>

  <button type="submit">Submit</button>

</form>
```

**CSS**
```css
* { box-sizing: border-box; }

body {
  font-family: system-ui, sans-serif;
  max-width: 480px;
  margin: 2rem auto;
  padding: 0 1rem;
  color: #333;
}

h2 { margin-top: 0; }

.intro {
  color: #555;
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.35rem;
  font-weight: 600;
  font-size: 0.9rem;
}

.req {
  font-weight: normal;
  color: #666;
  font-size: 0.82rem;
}

input {
  width: 100%;
  padding: 0.6rem 0.75rem;
  border: 2px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  transition: border-color 0.25s, background-color 0.25s;
}

/* Focus style */
input:focus {
  outline: none;
  border-color: #4f6df5;
  box-shadow: 0 0 0 3px rgba(79, 109, 245, 0.15);
}

/* :placeholder-shown = field is empty */
input:placeholder-shown {
  background-color: #f9f9f9;
}

/* :required adds a left accent bar */
input:required {
  border-left: 4px solid #4f6df5;
}

/* Valid — user has typed something and it passes */
input:not(:placeholder-shown):valid {
  border-color: #38a169;
  background-color: #f0fff4;
}

input:required:not(:placeholder-shown):valid {
  border-left-color: #38a169;
}

/* Invalid — user has typed something and it fails */
input:not(:placeholder-shown):invalid {
  border-color: #e53e3e;
  background-color: #fff5f5;
}

input:required:not(:placeholder-shown):invalid {
  border-left-color: #e53e3e;
}

/* Feedback messages */
.feedback {
  display: none;
  font-size: 0.8rem;
  margin-top: 0.3rem;
}

.valid-msg { color: #276749; }
.invalid-msg { color: #c53030; }

/* Show valid message when field is non-empty and valid */
.form-group:has(input:not(:placeholder-shown):valid) .valid-msg {
  display: block;
}

/* Show invalid message when field is non-empty and invalid */
.form-group:has(input:not(:placeholder-shown):invalid) .invalid-msg {
  display: block;
}

button {
  padding: 0.7rem 2rem;
  background: #4f6df5;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
}

button:hover {
  background: #3a56d4;
}
```

**JS**
```js
// No JavaScript needed — all feedback is handled with CSS pseudo-classes!
// Try typing in each field and watch :valid / :invalid styles apply in real time.
```
