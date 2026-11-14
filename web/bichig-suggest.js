/**
 * bichig-suggest.js
 * Dual-Mode Word Recommender & Predictive Autocomplete
 * Supports:
 *   1. Traditional Mongolian Script Mode (27,789 classical words from Lexicon)
 *   2. Mongolian Cyrillic Mode (28,306 words from Tsevel Explanatory Dictionary)
 * Author: Tsengel (tsengel.de)
 * Part of mn-keyboard-layout
 */

(function () {
  'use strict';

  let bichigDict = null;
  let cyrillicDict = null;
  let isEnabled = true;
  let activeSuggestions = [];

  // Normalize Latin input to match classical Mongolian transliteration
  function normalizeLatin(s) {
    return s.toLowerCase()
      .replace(/z/g, 'ǰ')
      .replace(/j/g, 'ǰ')
      .replace(/ch/g, 'č')
      .replace(/c/g, 'č')
      .replace(/sh/g, 'š')
      .replace(/x/g, 'q')
      .replace(/h/g, 'q')
      .replace(/g/g, 'γ');
  }

  // Load Traditional script dictionary lazily
  async function loadBichigDictionary() {
    if (bichigDict) return;
    try {
      const resp = await fetch('data/bichig-dict.json');
      if (resp.ok) {
        bichigDict = await resp.json();
        console.log(`[Suggest] Loaded Bichig dictionary (${bichigDict.length} words).`);
      }
    } catch (e) {
      console.warn('[Suggest] Could not load bichig dictionary:', e);
    }
  }

  // Load Cyrillic dictionary lazily
  async function loadCyrillicDictionary() {
    if (cyrillicDict) return;
    try {
      const resp = await fetch('data/cyrillic-dict.json');
      if (resp.ok) {
        cyrillicDict = await resp.json();
        console.log(`[Suggest] Loaded Cyrillic dictionary (${cyrillicDict.length} words).`);
      }
    } catch (e) {
      console.warn('[Suggest] Could not load cyrillic dictionary:', e);
    }
  }

  // Search in Traditional Mongolian Script dictionary
  function searchBichigSuggestions(token, max = 6) {
    if (!bichigDict || !token || token.trim().length < 1) return [];
    const t = token.trim();
    const tLow = t.toLowerCase();
    const tNorm = normalizeLatin(tLow);

    const matches = [];
    const seen = new Set();

    // 1. Script prefix match
    for (let i = 0; i < bichigDict.length; i++) {
      const [script, cyr, galig] = bichigDict[i];
      if (script.startsWith(t)) {
        matches.push({ word: script, hint: cyr, detail: galig, type: 'bichig' });
        seen.add(script);
        if (matches.length >= max) return matches;
      }
    }

    // 2. Cyrillic prefix match (phonetic lookup for script)
    for (let i = 0; i < bichigDict.length; i++) {
      const [script, cyr, galig] = bichigDict[i];
      if (!seen.has(script) && cyr.toLowerCase().startsWith(tLow)) {
        matches.push({ word: script, hint: cyr, detail: galig, type: 'bichig' });
        seen.add(script);
        if (matches.length >= max) return matches;
      }
    }

    // 3. Normalized Latin prefix match
    for (let i = 0; i < bichigDict.length; i++) {
      const [script, cyr, galig] = bichigDict[i];
      if (!seen.has(script) && (galig.toLowerCase().startsWith(tLow) || galig.toLowerCase().startsWith(tNorm))) {
        matches.push({ word: script, hint: cyr, detail: galig, type: 'bichig' });
        seen.add(script);
        if (matches.length >= max) return matches;
      }
    }

    return matches;
  }

  // Search in Cyrillic dictionary (Tsevel Explanatory Dictionary)
  function searchCyrillicSuggestions(token, max = 6) {
    if (!cyrillicDict || !token || token.trim().length < 1) return [];
    const t = token.trim().toLowerCase();

    const matches = [];
    for (let i = 0; i < cyrillicDict.length; i++) {
      const [word, def] = cyrillicDict[i];
      if (word.startsWith(t)) {
        matches.push({ word: word, hint: def, detail: '', type: 'cyrillic' });
        if (matches.length >= max) return matches;
      }
    }

    return matches;
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

  // Select a suggestion and insert into textarea
  function selectSuggestion(index) {
    const box = document.getElementById('typing-box');
    if (!box || index < 0 || index >= activeSuggestions.length) return;

    const item = activeSuggestions[index];
    const { start, end } = getCurrentWordInfo(box);

    const before = box.value.substring(0, start);
    const after = box.value.substring(end);

    const insertVal = item.word + ' ';
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
  function renderSuggestions(matches) {
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

      if (item.type === 'bichig') {
        chip.innerHTML = `
          <span class="suggest-num">${idx + 1}</span>
          <span class="suggest-script">${item.word}</span>
          <span class="suggest-cyr">(${item.hint})</span>
        `;
        chip.title = `${item.hint} [${item.detail || ''}]`;
      } else {
        // Cyrillic mode
        const shortDef = item.hint ? ` (${item.hint})` : '';
        chip.innerHTML = `
          <span class="suggest-num">${idx + 1}</span>
          <span class="suggest-cyr-word">${item.word}</span>
          <span class="suggest-def">${shortDef}</span>
        `;
        chip.title = item.hint || item.word;
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

    if (isBichig) {
      if (!bichigDict) {
        loadBichigDictionary().then(updateSuggestions);
        return;
      }
      const matches = searchBichigSuggestions(word, 6);
      renderSuggestions(matches);
    } else {
      // Cyrillic mode
      if (!cyrillicDict) {
        loadCyrillicDictionary().then(updateSuggestions);
        return;
      }
      const matches = searchCyrillicSuggestions(word, 6);
      renderSuggestions(matches);
    }
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
        if (m === 'bichig') loadBichigDictionary();
        else loadCyrillicDictionary();
      };
    }

    // Preload current mode dict
    if (typeof window.currentMode !== 'undefined' && window.currentMode === 'bichig') {
      loadBichigDictionary();
    } else {
      loadCyrillicDictionary();
    }
  }

  // Auto-init on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose API
  window.BichigSuggest = {
    searchBichig: searchBichigSuggestions,
    searchCyrillic: searchCyrillicSuggestions,
    enable: () => { isEnabled = true; },
    disable: () => { isEnabled = false; hideSuggestions(); },
    update: updateSuggestions,
    onModeChange: () => { hideSuggestions(); }
  };
})();
