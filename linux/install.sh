#!/usr/bin/env bash
# ==============================================================================
# Mongolian Keyboard Layout Suite - Linux (XKB) Installer
# Author: Tsengel (tsengel@tsengel.de)
# Part of "Mongolian for All" / tsengel.de Language Foundation
# ==============================================================================

set -euo pipefail

XKB_SYMBOLS_DIR="/usr/share/X11/xkb/symbols"
TARGET_FILE="${XKB_SYMBOLS_DIR}/mn"
BACKUP_FILE="${XKB_SYMBOLS_DIR}/mn.orig.backup"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

LAYOUT_CHOICE="${1:-}"

echo "=========================================================="
echo "🇲🇳 Mongolian Keyboard Layout Suite - Linux Installer"
echo "Author: Tsengel (tsengel.de)"
echo "=========================================================="

if [ -z "${LAYOUT_CHOICE}" ]; then
    echo "Select layout to install:"
    echo "  1) Modern Ergonomic & DevOps (Recommended: Q=Ө, W=Ү, brackets [ ] preserved)"
    echo "  2) Classic Tsengel Layout (Brackets [=ө, ]=ү)"
    echo "  3) Classical Mongolian Script (Худам Монгол бичиг)"
    read -rp "Enter choice [1-3, default 1]: " user_sel
    case "${user_sel}" in
        2) LAYOUT_CHOICE="classic" ;;
        3) LAYOUT_CHOICE="bichig" ;;
        *) LAYOUT_CHOICE="ergonomic" ;;
    esac
fi

case "${LAYOUT_CHOICE}" in
    classic)
        SOURCE_FILE="${SCRIPT_DIR}/mn-custom"
        LAYOUT_NAME="Classic Tsengel Layout"
        ;;
    bichig)
        SOURCE_FILE="${SCRIPT_DIR}/mn-bichig"
        LAYOUT_NAME="Classical Mongol Bichig (Худам Монгол бичиг)"
        ;;
    *)
        SOURCE_FILE="${SCRIPT_DIR}/mn-ergonomic"
        LAYOUT_NAME="Modern Ergonomic & DevOps (Q=Ө, W=Ү)"
        ;;
esac

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

echo "2. Installing ${LAYOUT_NAME} to ${TARGET_FILE}..."
sudo cp "${SOURCE_FILE}" "${TARGET_FILE}"
sudo chmod 644 "${TARGET_FILE}"

echo "3. Clearing XKB cache..."
if [ -d "/var/lib/xkb" ]; then
    sudo rm -rf /var/lib/xkb/*.xkm 2>/dev/null || true
fi

echo ""
echo "✅ Installation completed successfully!"
echo "   Active layout: ${LAYOUT_NAME}"
echo "----------------------------------------------------------"
echo "To activate immediately:"
echo "  - In Terminal (X11): setxkbmap mn"
echo "  - In GNOME / Ubuntu: Settings -> Keyboard -> Input Sources -> Add 'Mongolian'"
echo "  - If layout does not update immediately, log out and log back in."
echo ""
echo "To revert:"
echo "  Run: ./uninstall.sh"
echo "=========================================================="
