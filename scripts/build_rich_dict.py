#!/usr/bin/env python3
"""
Generate unified Dual-Script dictionary (Cyrillic + Traditional Script + Tsevel Definitions)
Source: apple-dictionary-mongolian data (bichig_mapping.json & tsevel/monmon.txt)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSEVEL_SRC = os.path.join(REPO_DIR, "..", "apple-dictionary-mongolian", "data", "tsevel", "monmon.txt")
BICHIG_SRC = os.path.join(REPO_DIR, "..", "apple-dictionary-mongolian", "data", "bichig_mapping.json")
OUT_DIR = os.path.join(REPO_DIR, "web", "data")
OUT_FILE = os.path.join(OUT_DIR, "mongol-dict.json")

def clean_html(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:45]

def main():
    if not os.path.exists(BICHIG_SRC):
        print(f"❌ Source not found: {BICHIG_SRC}")
        return

    with open(BICHIG_SRC, "r", encoding="utf-8") as f:
        bichig = json.load(f)

    tsevel_defs = {}
    if os.path.exists(TSEVEL_SRC):
        with open(TSEVEL_SRC, "r", encoding="utf-8") as f:
            parts = f.read().split("\x00")
        for i in range(0, len(parts) - 1, 2):
            raw_w = parts[i].strip().split(" ")[0].strip().lower()
            if raw_w and raw_w not in tsevel_defs:
                tsevel_defs[raw_w] = clean_html(parts[i + 1])

    entries = []
    for cyr, data in bichig.items():
        c_low = cyr.strip().lower()
        script = data.get("s", "").strip()
        defn = tsevel_defs.get(c_low, "")
        if c_low and script:
            entries.append([c_low, script, defn])

    # Sort: shorter words first
    entries.sort(key=lambda x: (len(x[0]), x[0]))

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))

    size_kb = os.path.getsize(OUT_FILE) / 1024
    print(f"✅ Generated {OUT_FILE}: {len(entries)} words ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
