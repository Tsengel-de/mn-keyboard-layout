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

if [ ! -f "${SOURCE_FILE}" ]; then
    echo "❌ Error: Source file ${SOURCE_FILE} not found!" >&2
    exit 1
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

echo "3. Clearing XKB cache..."
if [ -d "/var/lib/xkb" ]; then
    sudo rm -rf /var/lib/xkb/*.xkm 2>/dev/null || true
fi

echo ""
echo "✅ All 3 layouts installed simultaneously!"
echo "----------------------------------------------------------"
echo "Installed Variants:"
echo "  1) Default:  Mongolian (Modern Ergonomic: Q=Ө, W=Ү)"
echo "  2) Classic:  Mongolian (Classic Tsengel: [=ө, ]=ү)"
echo "  3) Bichig:   Mongolian Script (Худам Монгол бичиг)"
echo ""
echo "Quick Switch via Terminal (X11):"
echo "  - setxkbmap mn                    # Modern Ergonomic (Default)"
echo "  - setxkbmap mn -variant classic   # Classic Tsengel"
echo "  - setxkbmap mn -variant bichig    # Classical Mongol Bichig"
echo ""
echo "In GNOME / Ubuntu / Fedora Settings:"
echo "  Settings -> Keyboard -> Input Sources -> Add 'Mongolian'"
echo "  (All 3 variants are ready to select and switch with Win + Space)"
echo ""
echo "To revert:"
echo "  Run: ./uninstall.sh"
echo "=========================================================="
