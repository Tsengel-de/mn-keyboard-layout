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
echo "🇲🇳 Mongolian Keyboard Layout Suite - macOS Installer"
echo "=========================================================="

mkdir -p "${TARGET_LAYOUT_DIR}"
mkdir -p "${TARGET_FONT_DIR}"

echo "1. Installing Mongolian.bundle & standalone keylayouts to ${TARGET_LAYOUT_DIR}..."
cp -Rf "${SCRIPT_DIR}/Mongolian.bundle" "${TARGET_LAYOUT_DIR}/" || true
cp -f "${SCRIPT_DIR}"/*.keylayout "${TARGET_LAYOUT_DIR}/" 2>/dev/null || true
cp -f "${SCRIPT_DIR}"/*.icns "${TARGET_LAYOUT_DIR}/" 2>/dev/null || true

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
echo "  3. Add 'Mongolian Cyrillic Ergonomic (Tsengel)'."
echo "  4. If it does not appear immediately, log out and log back in."
echo "=========================================================="
