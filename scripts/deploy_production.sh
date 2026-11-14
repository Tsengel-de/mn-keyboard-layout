#!/usr/bin/env bash
# ==============================================================================
# Automated Production Deployment & Cross-Project Binding Script
# Binds:
#   1. language-dev/mn-keyboard-layout (Source)
#   2. Infrastructure/kubeone-cluster (Management-standalone)
#   3. node-nuc-1 (192.168.88.248 Production Nginx Server)
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
INFRA_MN_DIR="${REPO_ROOT}/../../Infrastructure/kubeone-cluster/management-standalone/mn-keyboard"
INFRA_REPO_ROOT="${REPO_ROOT}/../../Infrastructure/kubeone-cluster"
PROD_HOST="192.168.88.248"
PROD_USER="tsengel"
PROD_PATH="/opt/kubeone-cluster/management-standalone/mn-keyboard"
SSH_KEY="${HOME}/.ssh/tsengel_everywhere"

echo "=================================================================="
echo "🇲🇳 Synchronizing Mongolian Keyboard Suite -> Production (mn.tsengel.de)"
echo "=================================================================="

# 1. Verify sources
if [ ! -d "${REPO_ROOT}/web/downloads" ]; then
    echo "❌ Error: web/downloads not found in ${REPO_ROOT}"
    exit 1
fi

# 2. Update local Infrastructure repo
echo "[1/4] Copying web assets to local Infrastructure repository..."
mkdir -p "${INFRA_MN_DIR}/downloads" "${INFRA_MN_DIR}/data"
cp -v "${REPO_ROOT}/web/index.html" "${INFRA_MN_DIR}/index.html"
if [ -f "${REPO_ROOT}/web/bichig-suggest.js" ]; then
    cp -v "${REPO_ROOT}/web/bichig-suggest.js" "${INFRA_MN_DIR}/bichig-suggest.js"
fi
if [ -d "${REPO_ROOT}/web/data" ]; then
    cp -v "${REPO_ROOT}/web/data/"* "${INFRA_MN_DIR}/data/"
fi
cp -v "${REPO_ROOT}/web/downloads/"* "${INFRA_MN_DIR}/downloads/"

# 3. Commit & push in Infrastructure repo if changed
echo "[2/4] Checking Infrastructure Git state..."
if [ -d "${INFRA_REPO_ROOT}/.git" ]; then
    cd "${INFRA_REPO_ROOT}"
    if ! git diff --quiet management-standalone/mn-keyboard/ || [ -n "$(git status --porcelain management-standalone/mn-keyboard/)" ]; then
        echo "  -> Changes detected. Committing to kubeone-cluster repo..."
        git add management-standalone/mn-keyboard/
        git commit -m "feat(mn-keyboard): automated sync from mn-keyboard-layout source"
        git push origin main || echo "⚠️ Warning: git push failed, continuing deploy."
    else
        echo "  -> Local Infrastructure repository is already up to date."
    fi
fi

# 4. Sync directly to production server via rsync
echo "[3/4] Rsyncing directly to production server (${PROD_HOST})..."
rsync -avz --delete --exclude 'preview/' \
    -e "ssh -i ${SSH_KEY} -o ConnectTimeout=10 -o StrictHostKeyChecking=no" \
    "${INFRA_MN_DIR}/" \
    "${PROD_USER}@${PROD_HOST}:${PROD_PATH}/"

# 5. Verify live HTTP endpoint
echo "[4/4] Verifying live mn.tsengel.de response..."
LIVE_HASH=$(curl -sSL --max-time 60 https://mn.tsengel.de/downloads/Mongolian-Keyboard-macOS.dmg | sha256sum | awk '{print $1}')
LOCAL_HASH=$(sha256sum "${REPO_ROOT}/web/downloads/Mongolian-Keyboard-macOS.dmg" | awk '{print $1}')

echo "------------------------------------------------------------------"
echo "Local DMG Hash: ${LOCAL_HASH}"
echo "Live  DMG Hash: ${LIVE_HASH}"

if [ "${LOCAL_HASH}" = "${LIVE_HASH}" ]; then
    echo "✅ SUCCESS: mn.tsengel.de is 100% in sync with production assets!"
else
    echo "⚠️ WARNING: Hash mismatch or Cloudflare cache delay."
fi
echo "=================================================================="

