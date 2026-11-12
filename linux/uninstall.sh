#!/usr/bin/env bash
# ==============================================================================
# Mongolian Custom Keyboard Layout - Linux (XKB) Uninstaller / Restore
# ==============================================================================

set -euo pipefail

XKB_SYMBOLS_DIR="/usr/share/X11/xkb/symbols"
TARGET_FILE="${XKB_SYMBOLS_DIR}/mn"
BACKUP_FILE="${XKB_SYMBOLS_DIR}/mn.orig.backup"

echo "=========================================================="
echo "🇲🇳 Restoring Default Mongolian Linux Keyboard Layout"
echo "=========================================================="

if [ -f "${BACKUP_FILE}" ]; then
    echo "Restoring from backup: ${BACKUP_FILE} -> ${TARGET_FILE}"
    sudo cp "${BACKUP_FILE}" "${TARGET_FILE}"
    sudo chmod 644 "${TARGET_FILE}"
    if [ -d "/var/lib/xkb" ]; then
        sudo rm -rf /var/lib/xkb/*.xkm 2>/dev/null || true
    fi
    echo "✅ Reverted to default system layout."
else
    echo "⚠️  No backup file found at ${BACKUP_FILE}."
    echo "   Re-installing xkb-data package might be required to restore defaults:"
    echo "   sudo apt-get --reinstall install xkb-data"
fi

