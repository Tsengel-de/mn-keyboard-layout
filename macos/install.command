#!/bin/sh
# ==============================================================================
# Mongolian Keyboard Layout Suite - macOS Auto Installer
# Author: Tsengel (tsengel.de)
# ==============================================================================

here="$(dirname "$0")"
cd "$here"

TARGET_LAYOUT_DIR="$HOME/Library/Keyboard Layouts"
TARGET_FONT_DIR="$HOME/Library/Fonts"

echo "=========================================================="
echo "🇲🇳 Installing Mongolian Keyboards & Fonts on macOS..."
echo "=========================================================="

mkdir -p "$TARGET_LAYOUT_DIR"
mkdir -p "$TARGET_FONT_DIR"

echo "1. Installing Keyboard Layouts to $TARGET_LAYOUT_DIR..."
cp -f ./*.keylayout "$TARGET_LAYOUT_DIR/" 2>/dev/null || true
cp -f ./*.icns "$TARGET_LAYOUT_DIR/" 2>/dev/null || true
cp -f ./icons/*.icns "$TARGET_LAYOUT_DIR/" 2>/dev/null || true

echo "2. Installing Classical Mongolian Fonts to $TARGET_FONT_DIR..."
if [ -d "./fonts" ]; then
    cp -f ./fonts/*.ttf "$TARGET_FONT_DIR/" 2>/dev/null || true
fi

echo ""
echo "✅ Installation completed successfully!"
echo "----------------------------------------------------------"
echo "To activate:"
echo "  1. Open System Settings -> Keyboard -> Text Input (Input Sources) -> Edit"
echo "  2. Click '+' and add 'Mongolian Cyrillic Ergonomic (Tsengel)'"
echo "     or 'Mongolian Script Qwerty (Dusal)' for Classical Bichig"
echo "  3. If they do not appear immediately, log out and log back in."
echo "=========================================================="
