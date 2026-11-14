/**
 * bichig-suggest.js
 * Traditional Mongolian Script Predictive Word Recommender & Autocomplete
 * Author: Tsengel (tsengel.de)
 * Part of mn-keyboard-layout
 */

(function () {
  'use strict';

  let dictData = null;
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

  // Load compact dictionary
  async function loadDictionary() {
    if (dictData) return;
    try {
      const resp = await fetch('data/bichig-dict.json');
      if (resp.ok) {
        dictData = await resp.json();
        console.log(`[BichigSuggest] Loaded ${dictData.length} words.`);
      }
    } catch (e) {
      console.warn('[BichigSuggest] Could not load dictionary:', e);
    }
  }

  // Find matching suggestions for a given token
  function searchSuggestions(token, max = 6) {
    if (!dictData || !token || token.trim().length < 1) return [];
    const t = token.trim();
    const tLow = t.toLowerCase();
    const tNorm = normalizeLatin(tLow);

    const matches = [];
    const seen = new Set();

    // 1. Script prefix match
    for (let i = 0; i < dictData.length; i++) {
      const [script, cyr, galig] = dictData[i];
      if (script.startsWith(t)) {
        matches.push(dictData[i]);
        seen.add(script);
        if (matches.length >= max) return matches;
      }
    }

    // 2. Cyrillic prefix match
    for (let i = 0; i < dictData.length; i++) {
      const [script, cyr, galig] = dictData[i];
      if (!seen.has(script) && cyr.toLowerCase().startsWith(tLow)) {
        matches.push(dictData[i]);
        seen.add(script);
        if (matches.length >= max) return matches;
      }
    }

    // 3. Normalized Latin prefix match
    for (let i = 0; i < dictData.length; i++) {
      const [script, cyr, galig] = dictData[i];
      if (!seen.has(script) && (galig.toLowerCase().startsWith(tLow) || galig.toLowerCase().startsWith(tNorm))) {
        matches.push(dictData[i]);
        seen.add(script);
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

    const [scriptWord, cyrWord] = activeSuggestions[index];
    const { start, end } = getCurrentWordInfo(box);

    const before = box.value.substring(0, start);
    const after = box.value.substring(end);
    
    // Add non-breaking space or standard space
    const insertVal = scriptWord + ' ';
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

    matches.forEach(([script, cyr, galig], idx) => {
      const chip = document.createElement('div');
      chip.className = 'suggest-chip';
      chip.innerHTML = `
        <span class="suggest-num">${idx + 1}</span>
        <span class="suggest-script">${script}</span>
        <span class="suggest-cyr">(${cyr})</span>
      `;
      chip.title = `${cyr} [${galig}]`;
      chip.onclick = (e) => {
        e.preventDefault();
        selectSuggestion(idx);
      };
      bar.appendChild(chip);
    });
  }

  // Update suggestions based on current textarea state
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

    const matches = searchSuggestions(word, 6);
    renderSuggestions(matches);
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

    // Create toggle in editor tools
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

      // Number keys 1-6
      if (e.key >= '1' && e.key <= '6') {
        const num = parseInt(e.key, 10);
        if (num <= activeSuggestions.length) {
          e.preventDefault();
          selectSuggestion(num - 1);
          return;
        }
      }

      // Tab or Enter selects first suggestion if active
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
    search: searchSuggestions,
    enable: () => { isEnabled = true; },
    disable: () => { isEnabled = false; hideSuggestions(); },
    update: updateSuggestions
  };
})();
