#!/usr/bin/env python3
"""
Generate compact Mongolian Cyrillic dictionary (Tsevel Dictionary & Lexicon)
Extracts headwords and concise definitions from apple-dictionary-mongolian/data/tsevel/monmon.txt
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSEVEL_SRC = os.path.join(REPO_DIR, "..", "apple-dictionary-mongolian", "data", "tsevel", "monmon.txt")
BICHIG_SRC = os.path.join(REPO_DIR, "..", "apple-dictionary-mongolian", "data", "bichig_mapping.json")
OUT_DIR = os.path.join(REPO_DIR, "web", "data")
OUT_FILE = os.path.join(OUT_DIR, "cyrillic-dict.json")

def clean_html(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:45]

def main():
    if not os.path.exists(TSEVEL_SRC):
        print(f"❌ Source file not found: {TSEVEL_SRC}")
        return

    with open(TSEVEL_SRC, "r", encoding="utf-8") as f:
        parts = f.read().split("\x00")

    dict_map = {}
    for i in range(0, len(parts) - 1, 2):
        raw_word = parts[i].strip()
        defin = clean_html(parts[i + 1])
        clean_w = raw_word.split(" ")[0].strip().lower()
        if clean_w and clean_w not in dict_map:
            dict_map[clean_w] = defin

    if os.path.exists(BICHIG_SRC):
        with open(BICHIG_SRC, "r", encoding="utf-8") as f:
            bichig = json.load(f)
        for c in bichig:
            c_low = c.strip().lower()
            if c_low and c_low not in dict_map:
                dict_map[c_low] = ""

    entries = [[w, d] for w, d in dict_map.items()]
    entries.sort(key=lambda x: (len(x[0]), x[0]))

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))

    size_kb = os.path.getsize(OUT_FILE) / 1024
    print(f"✅ Generated {OUT_FILE}: {len(entries)} words ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
