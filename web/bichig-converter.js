/**
 * bichig-converter.js
 * High-Precision Cyrillic <---> Classical Mongolian Vertical Script Converter
 * Part of mn-keyboard-layout & mongolian-script-converter suite.
 * Complies with Unicode UTN #57 (NNBSP \u202F).
 * Author: Tsengel (tsengel.de | tsengel@tsengel.de)
 */

(function () {
  'use strict';

  const NNBSP = '\u202F';

  const VOWELS_MASC_BACK = new Set(['а', 'у', 'я', 'ю']);
  const VOWELS_MASC_ROUND = new Set(['о', 'ё']);
  const VOWELS_FEM_FRONT = new Set(['э', 'ү', 'е']);
  const VOWELS_FEM_ROUND = new Set(['ө']);
  const VOWELS_NEUTRAL = new Set(['и', 'й']);
  const VOWELS_ALL = new Set([
    'а', 'у', 'я', 'ю', 'о', 'ё', 'э', 'ү', 'е', 'ө', 'и', 'й', 'ы'
  ]);
  const CONSONANTS_C9 = new Set(['д', 'ж', 'з', 'с', 'т', 'х', 'ц', 'ч', 'ш']);

  const FALLBACK_MAP = {
    'а': 'ᠠ', 'б': 'ᠪ', 'в': 'ᠸ', 'г': 'ᠭ', 'д': 'ᠳ', 'е': 'ᠶᠡ', 'ё': 'ᠶᠣ',
    'ж': 'ᠵ', 'з': 'ᠽ', 'и': 'ᠢ', 'й': 'ᠢ', 'к': 'ᠺ', 'л': 'ᠯ', 'м': 'ᠮ',
    'н': 'ᠨ', 'о': 'ᠣ', 'ө': 'ᠥ', 'п': 'ᠫ', 'р': 'ᠷ', 'с': 'ᠰ', 'т': 'ᠲ',
    'у': 'ᠤ', 'ү': 'ᠦ', 'ф': 'ᠹ', 'х': 'ᠬ', 'ц': 'ᠼ', 'ч': 'ᠴ', 'ш': 'ᠰᠢ',
    'щ': 'ᠰᠢ', 'ъ': '', 'ы': 'ᠶᠢ', 'ь': 'ᠢ', 'э': 'ᠡ', 'ю': 'ᠶᠤ', 'я': 'ᠶᠠ'
  };

  let dictMap = null;
  let isReady = false;

  function isMasculine(word) {
    const w = word.toLowerCase();
    for (let i = 0; i < w.length; i++) {
      const ch = w[i];
      if (VOWELS_MASC_BACK.has(ch) || VOWELS_MASC_ROUND.has(ch)) return true;
      if (VOWELS_FEM_FRONT.has(ch) || VOWELS_FEM_ROUND.has(ch)) return false;
    }
    return false;
  }

  function endsWithVowel(word) {
    const w = word.toLowerCase();
    return w.length > 0 && VOWELS_ALL.has(w[w.length - 1]);
  }

  function endsWithC9(word) {
    const w = word.toLowerCase();
    return w.length > 0 && CONSONANTS_C9.has(w[w.length - 1]);
  }

  const SUFFIX_RULES = [
    // Genitive
    {
      sufs: ['ийн', 'ын', 'ний', 'ны'],
      resolve: function (stem) {
        return endsWithVowel(stem) ? `${NNBSP}ᠶᠢᠨ` : (isMasculine(stem) ? `${NNBSP}ᠤᠨ` : `${NNBSP}ᠦᠨ`);
      }
    },
    // Ablative
    {
      sufs: ['аас', 'ээс', 'оос', 'өөс'],
      resolve: function (stem) {
        return isMasculine(stem) ? `${NNBSP}ᠠᠴᠠ` : `${NNBSP}ᠡᠴᠡ`;
      }
    },
    // Instrumental
    {
      sufs: ['аар', 'ээр', 'оор', 'өөр'],
      resolve: function (stem) {
        const masc = isMasculine(stem);
        if (endsWithVowel(stem)) return masc ? `${NNBSP}ᠪᠠᠷ` : `${NNBSP}ᠪᠡᠷ`;
        return masc ? `${NNBSP}ᠢᠶᠠᠷ` : `${NNBSP}ᠢᠶᠡᠷ`;
      }
    },
    // Comitative
    {
      sufs: ['тай', 'тэй', 'той'],
      resolve: function (stem) {
        return isMasculine(stem) ? `${NNBSP}ᠲᠠᠢ` : `${NNBSP}ᠲᠡᠢ`;
      }
    },
    // Directional
    {
      sufs: ['руу', 'рүү', 'луу', 'лүү'],
      resolve: function (stem) {
        return isMasculine(stem) ? `${NNBSP}ᠤᠷᠤᠭᠤ` : `${NNBSP}ᠦᠷᠦᠭᠦ`;
      }
    },
    // Plural
    {
      sufs: ['ууд', 'үүд', 'чууд', 'чүүд'],
      resolve: function (stem) {
        return isMasculine(stem) ? `${NNBSP}ᠤᠳ` : `${NNBSP}ᠦᠳ`;
      }
    },
    // Reflexive
    {
      sufs: ['аа', 'ээ', 'оо', 'өө'],
      resolve: function (stem) {
        const masc = isMasculine(stem);
        if (endsWithVowel(stem)) return masc ? `${NNBSP}ᠪᠠᠨ` : `${NNBSP}ᠪᠡᠨ`;
        return masc ? `${NNBSP}ᠢᠶᠠᠨ` : `${NNBSP}ᠢᠶᠡᠨ`;
      }
    },
    // Accusative
    {
      sufs: ['ыг', 'ийг'],
      resolve: function (stem) {
        return endsWithVowel(stem) ? `${NNBSP}ᠶᠢ` : `${NNBSP}ᠢ`;
      }
    },
    // Dative-Locative (-од/-өд/-ад/-эд, -д, -т)
    {
      sufs: ['од', 'өд', 'ад', 'эд', 'д', 'т'],
      resolve: function (stem) {
        const masc = isMasculine(stem);
        const c9 = endsWithC9(stem);
        if (c9) return masc ? `${NNBSP}ᠲᠤ` : `${NNBSP}ᠲᠦ`;
        return masc ? `${NNBSP}ᠳᠤ` : `${NNBSP}ᠳᠦ`;
      }
    }
  ];

  async function init() {
    if (isReady) return;
    try {
      const resp = await fetch('data/mongol-dict.json');
      if (resp.ok) {
        const list = await resp.json();
        dictMap = new Map();
        for (let i = 0; i < list.length; i++) {
          const item = list[i];
          const cyr = item[0].trim().toLowerCase();
          const trad = item[1].trim();
          if (cyr && trad && !dictMap.has(cyr)) {
            dictMap.set(cyr, trad);
          }
        }
        isReady = true;
        console.log(`[BichigConverter] Loaded ${dictMap.size} lemmas.`);
      }
    } catch (e) {
      console.warn('[BichigConverter] Failed to load dictionary:', e);
    }
  }

  function convertWord(word) {
    if (!word) return '';
    const w = word.trim().toLowerCase();

    // 1. Direct dictionary match
    if (dictMap && dictMap.has(w)) {
      return dictMap.get(w);
    }

    // 2. Morphological suffix detachment
    if (dictMap && w.length >= 3) {
      for (let r = 0; r < SUFFIX_RULES.length; r++) {
        const rule = SUFFIX_RULES[r];
        for (let s = 0; s < rule.sufs.length; s++) {
          const suf = rule.sufs[s];
          if (w.endsWith(suf) && w.length > suf.length) {
            const stem = w.substring(0, w.length - suf.length);
            const candidates = [stem];
            if (stem.endsWith('и')) candidates.push(stem.substring(0, stem.length - 1) + 'ь');

            for (let c = 0; c < candidates.length; c++) {
              const cand = candidates[c];
              if (dictMap.has(cand)) {
                const tradStem = dictMap.get(cand);
                const tradSuf = rule.resolve(cand);
                return tradStem + tradSuf;
              }
            }
          }
        }
      }
    }

    // 3. Fallback character-level transliteration
    let out = '';
    for (let i = 0; i < w.length; i++) {
      const ch = w[i];
      out += FALLBACK_MAP[ch] || ch;
    }
    return out;
  }

  function convertText(text, convertPunct = true) {
    if (!text) return '';
    const lines = text.split('\n');
    const outLines = [];

    for (let l = 0; l < lines.length; l++) {
      const line = lines[l];
      if (!line.trim()) {
        outLines.push('');
        continue;
      }

      const tokens = line.match(/[а-яёөүА-ЯЁӨҮ\-']+|[a-zA-Z]+|\d+|[^\w\s]|[\s]+/g) || [line];
      let lineOut = '';

      for (let t = 0; t < tokens.length; t++) {
        const tok = tokens[t];
        if (/^[а-яёөүА-ЯЁӨҮ\-']+$/.test(tok)) {
          lineOut += convertWord(tok);
        } else if (convertPunct) {
          if (tok === '...') lineOut += '\u1801';
          else if (tok === '.') lineOut += '\u1803';
          else if (tok === ',') lineOut += '\u1802';
          else if (tok === ':') lineOut += '\u1804';
          else lineOut += tok;
        } else {
          lineOut += tok;
        }
      }
      outLines.push(lineOut);
    }
    return outLines.join('\n');
  }

  window.BichigConverter = {
    init: init,
    convertWord: convertWord,
    convertText: convertText
  };

  // Auto-init on page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
