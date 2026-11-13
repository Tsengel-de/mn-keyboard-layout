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

echo "2. Installing Mongolian Suite layouts to ${XKB_SYMBOLS_DIR}..."
sudo cp "${SOURCE_FILE}" "${TARGET_FILE}"
sudo chmod 644 "${TARGET_FILE}"
BICHIG_SOURCE="${SCRIPT_DIR}/bichig"
if [ ! -f "${BICHIG_SOURCE}" ]; then
    echo "⬇️ bichig layout not found locally. Downloading from mn.tsengel.de..."
    TEMP_BICHIG="$(mktemp)"
    if curl -fsSL https://mn.tsengel.de/downloads/bichig-xkb-symbols -o "${TEMP_BICHIG}"; then
        BICHIG_SOURCE="${TEMP_BICHIG}"
    fi
fi
if [ -f "${BICHIG_SOURCE}" ]; then
    sudo cp "${BICHIG_SOURCE}" "${XKB_SYMBOLS_DIR}/bichig"
    sudo chmod 644 "${XKB_SYMBOLS_DIR}/bichig"
fi

echo "3. Registering Classical Script layout in XKB rules (evdev.xml, base.xml, lst)..."
sudo python3 -c '
layout_bichig_xml = """    <layout>
      <configItem>
        <name>bichig</name>
        <!-- Keyboard indicator for Mongolian Script -->
        <shortDescription>mgl</shortDescription>
        <description>Mongolian Script (Traditional - Tsengel)</description>
        <countryList>
          <iso3166Id>MN</iso3166Id>
        </countryList>
        <languageList>
          <iso639Id>mon</iso639Id>
        </languageList>
      </configItem>
      <variantList/>
    </layout>"""

# 1. Update evdev.xml and base.xml
for xml_path in ["/usr/share/X11/xkb/rules/evdev.xml", "/usr/share/X11/xkb/rules/base.xml"]:
    try:
        with open(xml_path, "r") as f:
            c = f.read()
        
        # Replace Bachka with Tsengel if present
        c = c.replace("Mongolian (Cyrillic - Bachka)", "Mongolian (Cyrillic - Tsengel)")
        c = c.replace("Mongolian Script (Traditional - Bachka)", "Mongolian Script (Traditional - Tsengel)")
        
        # Add top-level layout bichig if not present
        if "<name>bichig</name>" not in c or "<layout>\n      <configItem>\n        <name>bichig</name>" not in c:
            idx = c.find("<name>mn</name>")
            if idx != -1:
                end_layout = c.find("</layout>", idx)
                if end_layout != -1:
                    end_layout += len("</layout>")
                    c = c[:end_layout] + "\n" + layout_bichig_xml + c[end_layout:]
        with open(xml_path, "w") as f:
            f.write(c)
    except Exception as e:
        print("   Notice updating", xml_path, ":", e)

# 2. Update evdev.lst and base.lst
for lst_path in ["/usr/share/X11/xkb/rules/evdev.lst", "/usr/share/X11/xkb/rules/base.lst"]:
    try:
        with open(lst_path, "r") as f:
            lines = [l.replace("Bachka", "Tsengel") for l in f.readlines()]
        has_bichig_layout = False
        in_layout = False
        for l in lines:
            if l.strip() == "! layout":
                in_layout = True
            elif l.strip().startswith("! ") and in_layout:
                in_layout = False
            if in_layout and l.strip().startswith("bichig "):
                has_bichig_layout = True
                break
        if not has_bichig_layout:
            for i, l in enumerate(lines):
                if l.strip().startswith("mn "):
                    lines.insert(i + 1, "  bichig          Mongolian Script (Traditional - Tsengel)\n")
                    break
        with open(lst_path, "w") as f:
            f.writelines(lines)
    except Exception as e:
        print("   Notice updating", lst_path, ":", e)
' 2>/dev/null || true

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
        # Remove legacy/useless variants if present
        sources = [s for s in sources if not s[1].startswith("cn+mon_") and s[1] != "mn+bichig"]
        if ("xkb", "mn") not in sources:
            sources.append(("xkb", "mn"))
        if ("xkb", "bichig") not in sources:
            sources.append(("xkb", "bichig"))
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

echo "7. Setting active layout to Mongolian Cyrillic (Tsengel)..."
if command -v setxkbmap >/dev/null 2>&1; then
    setxkbmap mn 2>/dev/null || true
fi

echo ""
echo "✅ Mongolian All-in-One Dual-Layout Suite installed successfully!"
echo "----------------------------------------------------------"
echo "Integrated Dual Layouts (Хос Гар):"
echo "  1) Default:  Mongolian Cyrillic (Tsengel mn-custom: All 35 Cyrillic letters on Base/Shift)"
echo "  2) Bichig:   Mongolian Script (Tsengel Phonetics: [=ᠥ, ]=ᠦ, A=ᠠ...)"
echo ""
echo "Quick Switch via Terminal (X11):"
echo "  - setxkbmap mn                    # Mongolian Cyrillic (Tsengel)"
echo "  - setxkbmap bichig                # Mongolian Script (Tsengel)"
echo ""
echo "In GNOME / Ubuntu / Fedora Settings:"
echo "  Settings -> Keyboard -> Input Sources -> 'Mongolian (Cyrillic)' & 'Mongolian Script'"
echo "  (Switch anytime using Super + Space)"
echo ""
echo "⚠️  ЧУХАЛ / IMPORTANT (GNOME / Wayland):"
echo "   GNOME Shell нь шинэ гарын байрлалыг сешн эхлэх үед уншдаг тул"
echo "   суулгасны дараа заавал системээс нэг удаа ГАРЧ (LOG OUT / LOG IN) эсвэл"
echo "   RESTART хийнэ үү! Тэгсний дараа дээд цэс дээр 'mn' ба 'mgl' шууд гарч ирнэ."
echo "   (Please LOG OUT & Log Back In or RESTART so GNOME loads both layouts)."
echo ""
echo "To revert:"
echo "  Run: ./uninstall.sh"
echo "=========================================================="

if [ -n "${TEMP_SOURCE}" ] && [ -f "${TEMP_SOURCE}" ]; then
    rm -f "${TEMP_SOURCE}"
fi
