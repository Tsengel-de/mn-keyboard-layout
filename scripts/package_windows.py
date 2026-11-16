#!/usr/bin/env python3
"""
Package Windows NSIS installer and ZIP distribution
"""

import os
import shutil
import subprocess
import zipfile

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WINDOWS_DIR = os.path.join(REPO_DIR, "windows")
DOWNLOADS_DIR = os.path.join(REPO_DIR, "web", "downloads")

def get_version():
    nsi_path = os.path.join(WINDOWS_DIR, "installer.nsi")
    with open(nsi_path, "r", encoding="utf-8") as f:
        for line in f:
            if "PRODUCT_VERSION" in line:
                parts = line.strip().split()
                if len(parts) >= 3:
                    return parts[2].replace('"', '')
    return "1.0.4"

def build_nsis_installer():
    version = get_version()
    print(f"Building Windows NSIS Installer (v{version})...")
    cmd = ["makensis", "installer.nsi"]
    subprocess.run(cmd, cwd=WINDOWS_DIR, check=True)

    exe_canonical = os.path.join(DOWNLOADS_DIR, "Mongolian-Keyboard-Windows-Setup.exe")
    exe_ver = os.path.join(DOWNLOADS_DIR, f"Mongolian-Keyboard-Windows-Setup-v{version}.exe")
    if os.path.exists(exe_canonical):
        shutil.copy2(exe_canonical, exe_ver)
        print(f"  Copied to {exe_ver}")

def create_windows_zip():
    version = get_version()
    zip_canonical = os.path.join(DOWNLOADS_DIR, "Mongolian-Keyboard-Windows.zip")
    zip_ver = os.path.join(DOWNLOADS_DIR, f"Mongolian-Keyboard-Windows-v{version}.zip")

    print(f"Creating Windows ZIP (v{version}): {zip_canonical}...")
    with zipfile.ZipFile(zip_canonical, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(WINDOWS_DIR):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, REPO_DIR)
                zipf.write(full_path, rel_path)

    shutil.copy2(zip_canonical, zip_ver)
    print(f"  Copied to {zip_ver}")

def main():
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)
    build_nsis_installer()
    create_windows_zip()
    print("✅ Windows packages successfully built!")

if __name__ == "__main__":
    main()

