#!/usr/bin/env python3
"""
Package macOS DMG and ZIP distributions with 1:1 Bachka mn-custom Dual-Layout Suite
"""

import os
import shutil
import subprocess
import tempfile
import zipfile

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MACOS_DIR = os.path.join(REPO_DIR, "macos")
BUNDLE_DIR = os.path.join(MACOS_DIR, "Mongolian.bundle")
INSTALLER_APP = os.path.join(MACOS_DIR, "Keyboard Installer.app")
FONTS_DIR = os.path.join(MACOS_DIR, "fonts")
DOWNLOADS_DIR = os.path.join(REPO_DIR, "web", "downloads")

README_TEXT = """🇲🇳 Монгол гарын байрлал (macOS) - Суулгах заавар
Хувилбар: Bachka mn-custom & Mongolian Script (All-in-One Dual-Layout)

Хамгийн хялбар арга:
1. "Keyboard Installer.app"-ийг давхар товшиж нээнэ.
2. "Mongolian.bundle"-ийг уг Installer цонх руу чирч тавина.
3. ЧУХАЛ: Системээс заавал 1 удаа гарч (Log out) дахин орно (эсвэл компьютерээ дахин ачаална/restart).
4. System Settings -> Keyboard -> Input Sources руу орж "+" товч дарна.
5. "Mongolian" (эсвэл "Others") дотроос:
   - "Mongolian Cyrillic (Bachka)"
   - "Mongolian Script (Bachka)"
   сонгож Add дарна.
6. Хооронд нь Ctrl + Space эсвэл Globe 🌐 товчоор шууд шилжинэ.

Гараар суулгах арга:
- Finder-ийн Go цэснээс "Go to Folder" (Command + Shift + G) дарж:
  ~/Library/Keyboard Layouts/
  гэж бичээд "Mongolian.bundle" эсвэл .keylayout файлуудыг хуулна.
- Фонтуудыг ~/Library/Fonts/ хавтас руу хуулна.
- Заавал 1 удаа Log Out эсвэл Restart хийнэ.
"""

def make_dist_folder(target_dir):
    os.makedirs(target_dir, exist_ok=True)

    # 1. Copy Keyboard Installer.app
    shutil.copytree(INSTALLER_APP, os.path.join(target_dir, "Keyboard Installer.app"))

    # 2. Copy Mongolian.bundle
    shutil.copytree(BUNDLE_DIR, os.path.join(target_dir, "Mongolian.bundle"))

    # 3. Copy standalone keylayouts and icons
    for f in os.listdir(MACOS_DIR):
        if f.endswith(".keylayout") or f.endswith(".icns"):
            shutil.copy2(os.path.join(MACOS_DIR, f), target_dir)

    # 4. Copy Fonts
    fonts_dest = os.path.join(target_dir, "Fonts")
    shutil.copytree(FONTS_DIR, fonts_dest)

    # 5. Write Readme
    with open(os.path.join(target_dir, "01-Суулгах Заавар (ReadMe).txt"), "w", encoding="utf-8") as f:
        f.write(README_TEXT)

def create_dmg(source_dir, output_dmg):
    print(f"Creating DMG: {output_dmg}...")
    cmd = [
        "genisoimage",
        "-V", "Mongolian Keyboard",
        "-D", "-R",
        "-apple",
        "-no-pad",
        "-o", output_dmg,
        source_dir
    ]
    subprocess.run(cmd, check=True)

def create_zip(source_dir, output_zip):
    print(f"Creating ZIP: {output_zip}...")
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, source_dir)
                zipf.write(full_path, rel_path)

def main():
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        dist_dir = os.path.join(tmpdir, "dmg_root")
        make_dist_folder(dist_dir)

        # Output DMG paths
        dmg_canonical = os.path.join(DOWNLOADS_DIR, "Mongolian-Keyboard-macOS.dmg")
        dmg_v103 = os.path.join(DOWNLOADS_DIR, "Mongolian-Keyboard-macOS-v1.0.3.dmg")

        # Output ZIP paths
        zip_canonical = os.path.join(DOWNLOADS_DIR, "Mongolian-Keyboard-macOS.zip")
        zip_v103 = os.path.join(DOWNLOADS_DIR, "Mongolian-Keyboard-macOS-v1.0.3.zip")

        # Build DMG
        create_dmg(dist_dir, dmg_canonical)
        shutil.copy2(dmg_canonical, dmg_v103)

        # Build ZIP
        create_zip(dist_dir, zip_canonical)
        shutil.copy2(zip_canonical, zip_v103)

    print("✅ macOS packages successfully built!")

if __name__ == "__main__":
    main()
