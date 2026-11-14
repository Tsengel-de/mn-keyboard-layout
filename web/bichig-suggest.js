/**
 * bichig-suggest.js
 * Dual-Mode Word Recommender & Predictive Autocomplete
 * 
 * In Cyrillic Mode:
 *   - Searches by Cyrillic prefix
 *   - Displays Cyrillic word + Traditional script counter-part + Tsevel definition
 *   - Selecting INSERTS CYRILLIC word into textarea!
 * 
 * In Traditional Script Mode:
 *   - Searches by Traditional script prefix (or Cyrillic phonetic prefix)
 *   - Displays Traditional script + Cyrillic meaning
 *   - Selecting INSERTS TRADITIONAL SCRIPT word into textarea!
 * 
 * Author: Tsengel (tsengel.de)
 * Part of mn-keyboard-layout
 */

(function () {
  'use strict';

  let dict = null;
  let isEnabled = true;
  let activeSuggestions = [];

  // Load unified dictionary
  async function loadDictionary() {
    if (dict) return;
    try {
      const resp = await fetch('data/mongol-dict.json');
      if (resp.ok) {
        dict = await resp.json();
        console.log(`[Suggest] Loaded Mongol dictionary (${dict.length} words).`);
      }
    } catch (e) {
      console.warn('[Suggest] Could not load dictionary:', e);
    }
  }

  // Get current word around cursor
  function getCurrentWordInfo(textarea) {
    const pos = textarea.selectionStart;
    const text = textarea.value;
    const leftText = text.substring(0, pos);

    // Delimiters: spaces, newlines, tabs, punctuation
    const delimRegex = /[\s\n\r\t.,;:!?()—–"'/\\\[\]{}|]+/g;
    let match;
    let lastIndex = 0;
    while ((match = delimRegex.exec(leftText)) !== null) {
      lastIndex = match.index + match[0].length;
    }

    const currentWord = leftText.substring(lastIndex);
    return {
      word: currentWord,
      start: lastIndex,
      end: pos
    };
  }

  // Search suggestions based on mode
  function search(token, isBichig, max = 6) {
    if (!dict || !token || token.trim().length < 1) return [];
    const t = token.trim();
    const tLow = t.toLowerCase();

    const matches = [];
    const seen = new Set();

    if (isBichig) {
      // 1. Script prefix match
      for (let i = 0; i < dict.length; i++) {
        const [cyr, script, defn] = dict[i];
        if (script.startsWith(t)) {
          matches.push({ cyr, script, defn, target: script });
          seen.add(script);
          if (matches.length >= max) return matches;
        }
      }

      // 2. Cyrillic phonetic prefix match (typing cyrillic to get script)
      for (let i = 0; i < dict.length; i++) {
        const [cyr, script, defn] = dict[i];
        if (!seen.has(script) && cyr.startsWith(tLow)) {
          matches.push({ cyr, script, defn, target: script });
          seen.add(script);
          if (matches.length >= max) return matches;
        }
      }
    } else {
      // Cyrillic mode: search by Cyrillic prefix
      for (let i = 0; i < dict.length; i++) {
        const [cyr, script, defn] = dict[i];
        if (cyr.startsWith(tLow)) {
          matches.push({ cyr, script, defn, target: cyr });
          if (matches.length >= max) return matches;
        }
      }
    }

    return matches;
  }

  // Select a suggestion and insert into textarea
  function selectSuggestion(index) {
    const box = document.getElementById('typing-box');
    if (!box || index < 0 || index >= activeSuggestions.length) return;

    const item = activeSuggestions[index];
    const { word, start, end } = getCurrentWordInfo(box);

    const before = box.value.substring(0, start);
    const after = box.value.substring(end);

    let insertWord = item.target;

    // Preserve first-letter capitalization in Cyrillic mode
    const isBichig = (typeof window.currentMode !== 'undefined' && window.currentMode === 'bichig');
    if (!isBichig && word.length > 0 && word[0] === word[0].toUpperCase() && word[0] !== word[0].toLowerCase()) {
      insertWord = insertWord.charAt(0).toUpperCase() + insertWord.slice(1);
    }

    const insertVal = insertWord + ' ';
    box.value = before + insertVal + after;
    box.selectionStart = box.selectionEnd = start + insertVal.length;
    box.focus();

    hideSuggestions();
  }

  function hideSuggestions() {
    activeSuggestions = [];
    const bar = document.getElementById('bichig-suggest-bar');
    if (bar) {
      bar.innerHTML = '';
      bar.style.display = 'none';
    }
  }

  // Render suggestion bar
  function renderSuggestions(matches, isBichig) {
    activeSuggestions = matches;
    const bar = document.getElementById('bichig-suggest-bar');
    if (!bar) return;

    if (!matches || matches.length === 0) {
      hideSuggestions();
      return;
    }

    bar.innerHTML = '';
    bar.style.display = 'flex';

    matches.forEach((item, idx) => {
      const chip = document.createElement('div');
      chip.className = 'suggest-chip';

      if (isBichig) {
        // Traditional Script is primary
        chip.innerHTML = `
          <span class="suggest-num">${idx + 1}</span>
          <span class="suggest-script">${item.script}</span>
          <span class="suggest-cyr">(${item.cyr})</span>
        `;
        chip.title = `${item.cyr}: ${item.defn || ''}`;
      } else {
        // Cyrillic is primary, traditional script shown as companion
        const shortDef = item.defn ? ` - ${item.defn}` : '';
        chip.innerHTML = `
          <span class="suggest-num">${idx + 1}</span>
          <span class="suggest-cyr-word">${item.cyr}</span>
          <span class="suggest-script-mini">${item.script}</span>
          ${item.defn ? `<span class="suggest-def">${shortDef}</span>` : ''}
        `;
        chip.title = `${item.cyr} [${item.script}]: ${item.defn || ''}`;
      }

      chip.onclick = (e) => {
        e.preventDefault();
        selectSuggestion(idx);
      };
      bar.appendChild(chip);
    });
  }

  // Update suggestions based on current textarea state and layout mode
  function updateSuggestions() {
    if (!isEnabled) {
      hideSuggestions();
      return;
    }

    const box = document.getElementById('typing-box');
    if (!box) return;

    const { word } = getCurrentWordInfo(box);
    if (!word || word.trim().length === 0) {
      hideSuggestions();
      return;
    }

    const isBichig = (typeof window.currentMode !== 'undefined' && window.currentMode === 'bichig');

    if (!dict) {
      loadDictionary().then(updateSuggestions);
      return;
    }

    const matches = search(word, isBichig, 6);
    renderSuggestions(matches, isBichig);
  }

  // Initialize UI and event listeners
  function init() {
    const box = document.getElementById('typing-box');
    if (!box) return;

    // Create suggest bar if not exists
    let bar = document.getElementById('bichig-suggest-bar');
    if (!bar) {
      bar = document.createElement('div');
      bar.id = 'bichig-suggest-bar';
      bar.className = 'suggest-bar';
      bar.style.display = 'none';
      box.parentNode.insertBefore(bar, box);
    }

    // Create toggle button in editor tools
    const tools = document.querySelector('.editor-tools');
    if (tools && !document.getElementById('btn-toggle-suggest')) {
      const toggleBtn = document.createElement('button');
      toggleBtn.id = 'btn-toggle-suggest';
      toggleBtn.className = 'btn btn-suggest active';
      toggleBtn.innerHTML = '💡 Зөв үг санал болгох: <strong>Асаалттай</strong>';
      toggleBtn.onclick = () => {
        isEnabled = !isEnabled;
        toggleBtn.classList.toggle('active', isEnabled);
        toggleBtn.innerHTML = `💡 Зөв үг санал болгох: <strong>${isEnabled ? 'Асаалттай' : 'Унтраастай'}</strong>`;
        if (!isEnabled) hideSuggestions();
        else updateSuggestions();
      };
      tools.insertBefore(toggleBtn, tools.firstChild);
    }

    // Keyboard navigation in suggestions (Numbers 1-6, Tab)
    box.addEventListener('keydown', (e) => {
      if (!isEnabled || activeSuggestions.length === 0) return;

      // Number keys 1-6 (when Alt/Ctrl not held)
      if (!e.altKey && !e.ctrlKey && !e.metaKey && e.key >= '1' && e.key <= '6') {
        const num = parseInt(e.key, 10);
        if (num <= activeSuggestions.length) {
          e.preventDefault();
          selectSuggestion(num - 1);
          return;
        }
      }

      // Tab selects first suggestion
      if (e.key === 'Tab') {
        e.preventDefault();
        selectSuggestion(0);
        return;
      }

      // Escape hides
      if (e.key === 'Escape') {
        hideSuggestions();
        return;
      }
    });

    box.addEventListener('input', updateSuggestions);
    box.addEventListener('keyup', (e) => {
      if (['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) {
        updateSuggestions();
      }
    });

    // Intercept insertChar / backspaceChar calls
    const origInsertChar = window.insertChar;
    if (origInsertChar) {
      window.insertChar = function (ch) {
        origInsertChar(ch);
        setTimeout(updateSuggestions, 10);
      };
    }

    const origBackspaceChar = window.backspaceChar;
    if (origBackspaceChar) {
      window.backspaceChar = function () {
        origBackspaceChar();
        setTimeout(updateSuggestions, 10);
      };
    }

    // Hook mode change
    const origSetLayoutMode = window.setLayoutMode;
    if (origSetLayoutMode) {
      window.setLayoutMode = function (m) {
        origSetLayoutMode(m);
        hideSuggestions();
        setTimeout(updateSuggestions, 10);
      };
    }

    loadDictionary();
  }

  // Auto-init on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose API
  window.BichigSuggest = {
    search: search,
    enable: () => { isEnabled = true; },
    disable: () => { isEnabled = false; hideSuggestions(); },
    update: updateSuggestions,
    onModeChange: () => { hideSuggestions(); }
  };
})();
