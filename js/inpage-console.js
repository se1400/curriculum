// inpage-console.js
(function () {
  function attachInPageConsole() {
    const box = document.createElement('div');
    box.id = 'inpage-console';
    box.style.cssText = [
      'font-family: monospace',
      'font-size: 12px',
      'background: #111',
      'color: #0f0',
      'padding: 8px',
      'max-height: 150px',
      'overflow-y: auto',
      'margin-top: 16px',
      'border-top: 1px solid #444',
      'white-space: pre-wrap'
    ].join(';');

    box.innerHTML = 'Console output:\n';

    function ensureAttached() {
      if (!box.isConnected) {
        if (document.body) {
          document.body.appendChild(box);
        } else {
          setTimeout(ensureAttached, 0);
        }
      }
    }

    function writeLine(type, args) {
      ensureAttached();
      const line = document.createElement('div');
      line.textContent = '[' + type + ']\n' + args.map(String).join(' ');
      box.appendChild(line);
      box.scrollTop = box.scrollHeight;
    }

    ['log', 'warn', 'error'].forEach(function (type) {
      const original = console[type] ? console[type].bind(console) : null;
      console[type] = function () {
        const args = Array.prototype.slice.call(arguments);
        writeLine(type, args);
        if (original) {
          original.apply(console, args);
        }
      };
    });

    window.addEventListener('error', function (evt) {
      writeLine('error', [evt.message]);
    });

    ensureAttached();
  }

  // expose a global function so Pens can opt in
  window.attachInPageConsole = attachInPageConsole;
})();
