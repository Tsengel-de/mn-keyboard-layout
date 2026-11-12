#!/usr/bin/env bash
# ==============================================================================
# Mongolian Custom Keyboard Layout - Linux (XKB) Installer
# Author: Tsengel (tsengel@tsengel.de)
# Part of "Mongolian for All" / tsengel.de Language Foundation
# ==============================================================================

set -euo pipefail

XKB_SYMBOLS_DIR="/usr/share/X11/xkb/symbols"
TARGET_FILE="${XKB_SYMBOLS_DIR}/mn"
BACKUP_FILE="${XKB_SYMBOLS_DIR}/mn.orig.backup"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_FILE="${SCRIPT_DIR}/mn-custom"

echo "=========================================================="
echo "🇲🇳 Mongolian Custom Keyboard Layout - Linux Installer"
echo "=========================================================="

if [ ! -f "${SOURCE_FILE}" ]; then
    echo "❌ Error: Source file ${SOURCE_FILE} not found!" >&2
    exit 1
fi

if [ ! -d "${XKB_SYMBOLS_DIR}" ]; then
    echo "❌ Error: XKB directory ${XKB_SYMBOLS_DIR} not found. Is X11/XKB installed?" >&2
    exit 1
fi

echo "1. Checking existing backup..."
if [ -f "${TARGET_FILE}" ] && [ ! -f "${BACKUP_FILE}" ]; then
    echo "   Creating original backup: ${BACKUP_FILE}"
    sudo cp "${TARGET_FILE}" "${BACKUP_FILE}"
elif [ -f "${BACKUP_FILE}" ]; then
    echo "   Original backup already exists at: ${BACKUP_FILE}"
fi

echo "2. Installing custom Mongolian layout to ${TARGET_FILE}..."
sudo cp "${SOURCE_FILE}" "${TARGET_FILE}"
sudo chmod 644 "${TARGET_FILE}"

echo "3. Clearing XKB cache..."
if [ -d "/var/lib/xkb" ]; then
    sudo rm -rf /var/lib/xkb/*.xkm 2>/dev/null || true
fi

echo ""
echo "✅ Installation completed successfully!"
echo "----------------------------------------------------------"
echo "To activate:"
echo "  - In GNOME / Ubuntu: Settings -> Keyboard -> Add 'Mongolian'"
echo "  - In Terminal (X11): setxkbmap mn"
echo "  - If layout does not update immediately, log out and log back in."
echo ""
echo "To revert:"
echo "  Run: ./uninstall.sh"
echo "=========================================================="

