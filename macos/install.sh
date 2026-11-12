#!/usr/bin/env bash
# ==============================================================================
# Mongolian Custom & Classical Script Keyboard Layout - macOS Installer
# Part of "Mongolian for All" / tsengel.de Language Foundation
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_LAYOUT_DIR="${HOME}/Library/Keyboard Layouts"
TARGET_FONT_DIR="${HOME}/Library/Fonts"

echo "=========================================================="
echo "🇲🇳 Mongolian Keyboard Layout & Classical Script - macOS Installer"
echo "=========================================================="

mkdir -p "${TARGET_LAYOUT_DIR}"
mkdir -p "${TARGET_FONT_DIR}"

echo "1. Installing Keyboard Layouts to ${TARGET_LAYOUT_DIR}..."
cp -v "${SCRIPT_DIR}"/*.keylayout "${TARGET_LAYOUT_DIR}/" || true
cp -v "${SCRIPT_DIR}/icons/"*.icns "${TARGET_LAYOUT_DIR}/" || true

echo "2. Installing Classical Mongolian Fonts to ${TARGET_FONT_DIR}..."
if [ -d "${SCRIPT_DIR}/fonts" ]; then
    cp -v "${SCRIPT_DIR}/fonts/"*.ttf "${TARGET_FONT_DIR}/" || true
fi

echo ""
echo "✅ Installation completed successfully!"
echo "----------------------------------------------------------"
echo "To activate on macOS:"
echo "  1. Open System Settings -> Keyboard -> Text Input (Input Sources) -> Edit."
echo "  2. Click '+' and select 'Mongolian' (or look under 'Others')."
echo "  3. Add:"
echo "     - 'Mongolian Cyrillic Qwerty (Dusal)'"
echo "     - 'Mongolian Cyrillic Standard (Dusal)'"
echo "     - 'Mongolian Script Qwerty (Dusal)' (for Classical Mongol Bichig)"
echo "  4. If they do not appear immediately, log out and log back in."
echo "=========================================================="

