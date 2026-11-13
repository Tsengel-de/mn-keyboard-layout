#!/usr/bin/env bash
# ==============================================================================
# All-in-One Mongolian Keyboard Layout Suite - Linux (XKB) Installer
# Author: Tsengel (tsengel@tsengel.de)
# Part of "Mongolian for All" / tsengel.de Language Foundation
# ==============================================================================

set -euo pipefail

XKB_SYMBOLS_DIR="/usr/share/X11/xkb/symbols"
TARGET_FILE="${XKB_SYMBOLS_DIR}/mn"
BACKUP_FILE="${XKB_SYMBOLS_DIR}/mn.orig.backup"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_FILE="${SCRIPT_DIR}/mn"

echo "=========================================================="
echo "🇲🇳 Mongolian All-in-One Keyboard Suite - Linux Installer"
echo "Author: Tsengel (tsengel.de)"
echo "=========================================================="

TEMP_SOURCE=""
if [ ! -f "${SOURCE_FILE}" ]; then
    echo "⬇️ Source file not found locally. Downloading unified XKB file from mn.tsengel.de..."
    TEMP_SOURCE="$(mktemp)"
    if curl -fsSL https://mn.tsengel.de/downloads/mn-xkb-symbols -o "${TEMP_SOURCE}"; then
        SOURCE_FILE="${TEMP_SOURCE}"
    else
        echo "❌ Error: Could not download symbols file." >&2
        exit 1
    fi
fi

if [ ! -d "${XKB_SYMBOLS_DIR}" ]; then
    echo "❌ Error: XKB directory ${XKB_SYMBOLS_DIR} not found. Is X11/XKB installed?" >&2
    exit 1
fi

echo "1. Checking original system backup..."
if [ -f "${TARGET_FILE}" ] && [ ! -f "${BACKUP_FILE}" ]; then
    echo "   Creating original backup: ${BACKUP_FILE}"
    sudo cp "${TARGET_FILE}" "${BACKUP_FILE}"
elif [ -f "${BACKUP_FILE}" ]; then
    echo "   Original backup exists at: ${BACKUP_FILE}"
fi

echo "2. Installing All-in-One Mongolian Suite to ${TARGET_FILE}..."
sudo cp "${SOURCE_FILE}" "${TARGET_FILE}"
sudo chmod 644 "${TARGET_FILE}"

echo "3. Registering Classical Script variant in XKB rules (evdev.xml)..."
EVDEV_XML="/usr/share/X11/xkb/rules/evdev.xml"
if [ -f "${EVDEV_XML}" ]; then
    if ! grep -q "<name>bichig</name>" "${EVDEV_XML}"; then
        if [ ! -f "${EVDEV_XML}.orig.backup" ]; then
            sudo cp "${EVDEV_XML}" "${EVDEV_XML}.orig.backup"
        fi
        sudo python3 -c '
with open("/usr/share/X11/xkb/rules/evdev.xml", "r") as f:
    c = f.read()
tgt = """        <name>mn</name>
        <!-- Keyboard indicator for Mongolian layouts -->
        <shortDescription>mn</shortDescription>
        <description>Mongolian</description>
        <countryList>
          <iso3166Id>MN</iso3166Id>
        </countryList>
        <languageList>
          <iso639Id>mon</iso639Id>
        </languageList>
      </configItem>
      <variantList/>"""
rep = """        <name>mn</name>
        <!-- Keyboard indicator for Mongolian layouts -->
        <shortDescription>mn</shortDescription>
        <description>Mongolian (Cyrillic - Bachka)</description>
        <countryList>
          <iso3166Id>MN</iso3166Id>
        </countryList>
        <languageList>
          <iso639Id>mon</iso639Id>
        </languageList>
      </configItem>
      <variantList>
        <variant>
          <configItem>
            <name>bichig</name>
            <description>Mongolian Script (Traditional - Bachka)</description>
          </configItem>
        </variant>
      </variantList>"""
if tgt in c:
    with open("/usr/share/X11/xkb/rules/evdev.xml", "w") as f:
        f.write(c.replace(tgt, rep, 1))
' 2>/dev/null || true
    fi
fi

echo "4. Installing Classical Mongolian Fonts..."
FONT_TARGET="${HOME}/.local/share/fonts"
mkdir -p "${FONT_TARGET}"
if [ -d "${SCRIPT_DIR}/fonts" ]; then
    cp -v "${SCRIPT_DIR}/fonts/"*.ttf "${FONT_TARGET}/" 2>/dev/null || true
elif [ -d "${SCRIPT_DIR}/../data/fonts" ]; then
    cp -v "${SCRIPT_DIR}/../data/fonts/"*.ttf "${FONT_TARGET}/" 2>/dev/null || true
fi
if command -v fc-cache >/dev/null 2>&1; then
    fc-cache -f "${FONT_TARGET}" 2>/dev/null || true
fi

echo "5. Automatically enabling Dual-Layouts (Cyrillic & Bichig) in GNOME..."
if command -v gsettings >/dev/null 2>&1; then
    python3 -c '
import subprocess, ast
try:
    res = subprocess.run(["gsettings", "get", "org.gnome.desktop.input-sources", "sources"], capture_output=True, text=True)
    if res.returncode == 0 and res.stdout.strip():
        sources = ast.literal_eval(res.stdout.strip())
        # Remove legacy/useless chinese variants if present
        sources = [s for s in sources if not s[1].startswith("cn+mon_")]
        if ("xkb", "mn") not in sources:
            sources.append(("xkb", "mn"))
        if ("xkb", "mn+bichig") not in sources:
            sources.append(("xkb", "mn+bichig"))
        out_str = "[" + ", ".join(f"(\x27{s[0]}\x27, \x27{s[1]}\x27)" for s in sources) + "]"
        subprocess.run(["gsettings", "set", "org.gnome.desktop.input-sources", "sources", out_str], check=True)
        print("   ✅ GNOME input sources enabled:", out_str)
except Exception as e:
    print("   (GNOME gsettings notice:", e, ")")
' || true
fi

echo "6. Clearing XKB cache..."
if [ -d "/var/lib/xkb" ]; then
    sudo rm -rf /var/lib/xkb/*.xkm 2>/dev/null || true
fi

echo ""
echo "✅ Mongolian All-in-One Dual-Layout Suite installed successfully!"
echo "----------------------------------------------------------"
echo "Integrated Dual Layouts (Хос Гар):"
echo "  1) Default:  Mongolian Cyrillic (Bachka mn-custom: All 35 Cyrillic letters on Base/Shift)"
echo "  2) Bichig:   Mongolian Script (Bachka Phonetics: [=ᠥ, ]=ᠦ, A=ᠠ...)"
echo ""
echo "Quick Switch via Terminal (X11):"
echo "  - setxkbmap mn                    # Mongolian Cyrillic (Bachka)"
echo "  - setxkbmap mn -variant bichig    # Mongolian Script (Bachka)"
echo ""
echo "In GNOME / Ubuntu / Fedora Settings:"
echo "  Settings -> Keyboard -> Input Sources -> Add 'Mongolian'"
echo "  (Switch anytime using Super + Space)"
echo ""
echo "To revert:"
echo "  Run: ./uninstall.sh"
echo "=========================================================="

if [ -n "${TEMP_SOURCE}" ] && [ -f "${TEMP_SOURCE}" ]; then
    rm -f "${TEMP_SOURCE}"
fi
