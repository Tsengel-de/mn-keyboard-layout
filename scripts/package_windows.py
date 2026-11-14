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

def build_nsis_installer():
    print("Building Windows NSIS Installer...")
    cmd = ["makensis", "installer.nsi"]
    subprocess.run(cmd, cwd=WINDOWS_DIR, check=True)

    exe_canonical = os.path.join(DOWNLOADS_DIR, "Mongolian-Keyboard-Windows-Setup.exe")
    exe_v103 = os.path.join(DOWNLOADS_DIR, "Mongolian-Keyboard-Windows-Setup-v1.0.3.exe")
    if os.path.exists(exe_canonical):
        shutil.copy2(exe_canonical, exe_v103)
        print(f"  Copied to {exe_v103}")

def create_windows_zip():
    zip_canonical = os.path.join(DOWNLOADS_DIR, "Mongolian-Keyboard-Windows.zip")
    zip_v103 = os.path.join(DOWNLOADS_DIR, "Mongolian-Keyboard-Windows-v1.0.3.zip")

    print(f"Creating Windows ZIP: {zip_canonical}...")
    with zipfile.ZipFile(zip_canonical, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(WINDOWS_DIR):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, REPO_DIR)
                zipf.write(full_path, rel_path)

    shutil.copy2(zip_canonical, zip_v103)
    print(f"  Copied to {zip_v103}")

def main():
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)
    build_nsis_installer()
    create_windows_zip()
    print("✅ Windows packages successfully built!")

if __name__ == "__main__":
    main()
