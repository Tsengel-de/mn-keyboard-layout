#!/usr/bin/env python3
"""
Generate compact Traditional Mongolian Script dictionary for Web Autocomplete
Extracts from apple-dictionary-mongolian/data/bichig_mapping.json
"""

import json
import os

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DICT_SRC = os.path.join(REPO_DIR, "..", "apple-dictionary-mongolian", "data", "bichig_mapping.json")
OUT_DIR = os.path.join(REPO_DIR, "web", "data")
OUT_FILE = os.path.join(OUT_DIR, "bichig-dict.json")

def main():
    if not os.path.exists(DICT_SRC):
        print(f"❌ Source dictionary not found at: {DICT_SRC}")
        return

    with open(DICT_SRC, "r", encoding="utf-8") as f:
        raw = json.load(f)

    entries = []
    for cyr, data in raw.items():
        s = data.get("s", "").strip()
        g = data.get("g", "").strip()
        c = cyr.strip()
        if s and c:
            entries.append([s, c, g])

    # Sort: shorter words first (more common prefixes)
    entries.sort(key=lambda x: (len(x[0]), x[0]))

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))

    size_kb = os.path.getsize(OUT_FILE) / 1024
    print(f"✅ Generated {OUT_FILE}: {len(entries)} words ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
