#!/usr/bin/env python3
"""
Build macOS Keyboard Layouts and Mongolian.bundle
Generates 1:1 Bachka mn-custom Dual-Layout Suite:
  1. Mongolian Cyrillic (Bachka)
  2. Mongolian Script (Bachka)
"""

import os
import shutil
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MACOS_DIR = os.path.join(REPO_DIR, "macos")
BUNDLE_DIR = os.path.join(MACOS_DIR, "Mongolian.bundle")
RES_DIR = os.path.join(BUNDLE_DIR, "Contents", "Resources")
DATA_FONTS_DIR = os.path.join(REPO_DIR, "data", "fonts")
MACOS_FONTS_DIR = os.path.join(MACOS_DIR, "fonts")
WINDOWS_FONTS_DIR = os.path.join(REPO_DIR, "windows", "fonts")

# Bachka mn-custom Cyrillic Mapping
CYRILLIC_KEYS = {
    # Number Row
    50: ("ё", "Ё", "~", "`", "Ё"),
    18: ("1", "!", "№", "¡", "1"),
    19: ("2", "@", "²", "™", "2"),
    20: ("3", "#", "³", "£", "3"),
    21: ("4", "$", "₮", "¢", "4"),
    23: ("5", "%", "€", "‰", "5"),
    22: ("6", "^", "¼", "^", "6"),
    26: ("7", "&", "½", "&", "7"),
    28: ("8", "*", "¾", "*", "8"),
    25: ("9", "(", "‘", "(", "9"),
    29: ("0", ")", "’", ")", "0"),
    27: ("-", "_", "—", "–", "-"),
    24: ("=", "+", "×", "÷", "="),

    # Top Row
    12: ("ъ", "Ъ", "'", '"', "Ъ"),      # Q
    13: ("ь", "Ь", "`", "~", "Ь"),      # W
    14: ("э", "Э", "€", "€", "Э"),      # E
    15: ("р", "Р", "®", "®", "Р"),      # R
    17: ("т", "Т", "₮", "₮", "Т"),      # T
    16: ("е", "Е", "™", "™", "Е"),      # Y (Bachka: "е" is here!)
    32: ("у", "У", "„", "„", "У"),      # U
    34: ("и", "И", "“", "“", "И"),      # I
    31: ("о", "О", "”", "”", "О"),      # O
    35: ("п", "П", ";", ":", "П"),      # P
    33: ("ө", "Ө", "[", "{", "Ө"),      # [ (Bachka: "ө" is here!)
    30: ("ү", "Ү", "]", "}", "Ү"),      # ] (Bachka: "ү" is here!)
    42: ("й", "Й", "\\", "|", "Й"),     # \ (Bachka: "й" is here!)

    # Home Row
    0:  ("а", "А", "µ", "µ", "А"),      # A
    1:  ("с", "С", "£", "£", "С"),      # S
    2:  ("д", "Д", "«", "«", "Д"),      # D
    3:  ("ф", "Ф", "»", "»", "Ф"),      # F
    5:  ("г", "Г", "{", "{", "Г"),      # G
    4:  ("х", "Х", "<", "<", "Х"),      # H
    38: ("ж", "Ж", ">", ">", "Ж"),      # J
    40: ("к", "К", "}", "}", "К"),      # K
    37: ("л", "Л", "№", "№", "Л"),      # L
    41: ("щ", "Щ", ":", ";", "Щ"),      # ; (Bachka: "щ" is here!)
    39: ("ы", "Ы", "…", '"', "Ы"),      # ' (Bachka: "ы" is here!)

    # Bottom Row
    6:  ("з", "З", "—", "—", "З"),      # Z
    7:  ("ш", "Ш", "–", "–", "Ш"),      # X
    8:  ("ц", "Ц", "©", "©", "Ц"),      # C
    9:  ("в", "В", "√", "√", "В"),      # V
    11: ("б", "Б", "•", "•", "Б"),      # B
    45: ("н", "Н", "<", "≤", "Н"),      # N
    46: ("м", "М", ">", "≥", "М"),      # M
    43: ("ч", "Ч", ",", "<", "Ч"),      # , (Bachka: "ч" is here!)
    47: ("ю", "Ю", ".", ">", "Ю"),      # . (Bachka: "ю" is here!)
    44: ("я", "Я", "?", "/", "Я"),      # / (Bachka: "я" is here!)

    # Space & ISO
    49: (" ", " ", "\u00A0", "\u00A0", " "),
    10: ("/", "|", "\\", "\\", "/"),
}

# Classical Mongolian Script (Tsengel Phonetics)
SCRIPT_KEYS = {
    # Number Row: classical digits
    50: ("\u1804", "\u1800", "~", "`", "\u1804"),  # ` -> ᠄ (colon), Birga (᠀)
    18: ("\u1811", "!", "1", "¡", "\u1811"),        # ᠑
    19: ("\u1812", "@", "2", "™", "\u1812"),        # ᠒
    20: ("\u1813", "#", "3", "£", "\u1813"),        # ᠓
    21: ("\u1814", "$", "4", "₮", "\u1814"),        # ᠔
    23: ("\u1815", "%", "5", "€", "\u1815"),        # ᠕
    22: ("\u1816", "^", "6", "^", "\u1816"),        # ᠖
    26: ("\u1817", "&", "7", "&", "\u1817"),        # ᠗
    28: ("\u1818", "*", "8", "*", "\u1818"),        # ᠘
    25: ("\u1819", "(", "9", "(", "\u1819"),        # ᠙
    29: ("\u1810", ")", "0", ")", "\u1810"),        # ᠐
    27: ("-", "_", "—", "–", "-"),
    24: ("=", "+", "×", "÷", "="),

    # Top Row
    12: ("\u180b", "\u180e", "'", '"', "\u180b"),  # Q = FVS1, Shift = MVS
    13: ("\u180c", "\u180d", "`", "~", "\u180c"),  # W = FVS2, Shift = FVS3
    14: ("\u1821", "\u1821", "\u180e", "€", "\u1821"), # E = ᠡ, AltGr = MVS
    15: ("\u1837", "\u1837", "®", "®", "\u1837"),  # R = ᠷ
    17: ("\u1832", "\u1832", "₮", "₮", "\u1832"),  # T = ᠲ
    16: ("\u1836", "\u1836", "™", "™", "\u1836"),  # Y = ᠶ
    32: ("\u1824", "\u1824", "„", "„", "\u1824"),  # U = ᠤ
    34: ("\u1822", "\u1822", "“", "“", "\u1822"),  # I = ᠢ
    31: ("\u1823", "\u1823", "”", "”", "\u1823"),  # O = ᠣ
    35: ("\u182b", "\u182b", ";", ":", "\u182b"),  # P = ᠫ
    33: ("\u1825", "\u1825", "[", "{", "\u1825"),  # [ = ᠥ (Ö)
    30: ("\u1826", "\u1826", "]", "}", "\u1826"),  # ] = ᠦ (Ü)
    42: ("\\", "|", "\u180a", "\u180a", "\\"),     # \ = Nirugu

    # Home Row
    0:  ("\u1820", "\u1820", "µ", "µ", "\u1820"),  # A = ᠠ
    1:  ("\u1830", "\u1830", "£", "£", "\u1830"),  # S = ᠰ
    2:  ("\u1833", "\u1833", "\u1808", "\u1808", "\u1833"), # D = ᠳ, AltGr = ᠈
    3:  ("\u1839", "\u1839", "\u1809", "\u1809", "\u1839"), # F = ᠹ, AltGr = ᠉
    5:  ("\u182d", "\u182d", "{", "{", "\u182d"),  # G = ᠭ
    4:  ("\u182c", "\u182c", "<", "<", "\u182c"),  # H = ᠬ
    38: ("\u1835", "\u1835", ">", ">", "\u1835"),  # J = ᠵ
    40: ("\u183a", "\u183a", "}", "}", "\u183a"),  # K = ᠺ
    37: ("\u182f", "\u182f", "№", "№", "\u182f"),  # L = ᠯ
    41: (";", ":", "\u1804", ";", ";"),            # ; = ;, Shift = :, AltGr = ᠄
    39: ("'", '"', "\u180e", '"', "'"),            # ' = ', Shift = ", AltGr = MVS

    # Bottom Row
    6:  ("\u1835", "\u183d", "—", "—", "\u1835"),  # Z = ᠵ (native Mongolian J/Z), Shift = ᠽ (Ali Gali)
    7:  ("\u1831", "\u1831", "–", "–", "\u1831"),  # X = ᠱ
    8:  ("\u183c", "\u183c", "©", "©", "\u183c"),  # C = ᠼ
    9:  ("\u1838", "\u1838", "√", "√", "\u1838"),  # V = ᠸ
    11: ("\u182a", "\u182a", "•", "•", "\u182a"),  # B = ᠪ
    45: ("\u1828", "\u1829", "<", "≤", "\u1828"),  # N = ᠨ, Shift+N = ᠩ
    46: ("\u182e", "\u182e", ">", "≥", "\u182e"),  # M = ᠮ
    43: ("\u1834", ",", "\u1802", "<", "\u1834"),  # , = ᠴ (Ch), Shift = ,, AltGr = ᠂
    47: ("\u1803", ".", "\u1803", ">", "\u1803"),  # . = ᠃ (Tseg), Shift = .
    44: ("/", "?", "\u1816", "/", "/"),            # / = /

    # Space & ISO
    49: (" ", "\u202f", "\u202f", "\u202f", " "),  # Shift+Space = NNBSP (\u202F)
    10: ("/", "|", "\\", "\\", "/"),
}

def escape_xml_attr(val):
    if val == "&":
        return "&amp;"
    elif val == "<":
        return "&#x003C;"
    elif val == ">":
        return "&#x003E;"
    elif val == '"':
        return "&#x0022;"
    return val

def generate_keylayout_xml(template_path, name, layout_id, key_dict):
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace keyboard tag attributes
    content = re.sub(
        r'<keyboard group="126" id=".*?" name=".*?" maxout="1">',
        f'<keyboard group="126" id="{layout_id}" name="{name}" maxout="1">',
        content
    )

    # Process keymaps 0, 1, 2, 3, 4
    # Map index 0: Normal
    # Map index 1: Shift
    # Map index 2: Option
    # Map index 3: Shift+Option
    # Map index 4: Caps

    for map_idx in range(5):
        pattern = rf'(<keyMap index="{map_idx}">)(.*?)(</keyMap>)'
        m = re.search(pattern, content, re.DOTALL)
        if not m:
            continue
        
        map_body = m.group(2)
        # Replace keys in this map
        for code, values in key_dict.items():
            val = values[map_idx]
            escaped = escape_xml_attr(val)
            key_pattern = rf'<key code="{code}" output=".*?"/>'
            if re.search(key_pattern, map_body):
                map_body = re.sub(key_pattern, f'<key code="{code}" output="{escaped}"/>', map_body)
            else:
                # If key was an action or not present, replace or append
                alt_pattern = rf'<key code="{code}" action=".*?"/>'
                if re.search(alt_pattern, map_body):
                    map_body = re.sub(alt_pattern, f'<key code="{code}" output="{escaped}"/>', map_body)
                else:
                    map_body += f'\n            <key code="{code}" output="{escaped}"/>'
        
        content = content[:m.start(2)] + map_body + content[m.end(2):]

    return content

def main():
    print("🚀 Building macOS Dual-Layout Suite (Tsengel mn-custom)...")
    template_candidates = [
        os.path.join(RES_DIR, "Mongolian (Cyrillic - Tsengel).keylayout"),
        os.path.join(RES_DIR, "Mongolian Cyrillic (Bachka).keylayout"),
        os.path.join(RES_DIR, "MongolianCyrillicErgonomic.keylayout"),
        os.path.join(MACOS_DIR, "Mongolian Cyrillic (Bachka).keylayout"),
        os.path.join(MACOS_DIR, "MongolianCyrillicErgonomic.keylayout"),
    ]
    template_path = None
    for cand in template_candidates:
        if os.path.exists(cand):
            template_path = cand
            break
    if not template_path:
        raise FileNotFoundError("Could not find base keylayout template.")

    # 1. Generate Mongolian (Cyrillic - Tsengel)
    cyrillic_name = "Mongolian (Cyrillic - Tsengel)"
    cyrillic_xml = generate_keylayout_xml(template_path, cyrillic_name, "-13215", CYRILLIC_KEYS)

    # 2. Generate Mongolian Script (Traditional - Tsengel)
    script_name = "Mongolian Script (Traditional - Tsengel)"
    script_xml = generate_keylayout_xml(template_path, script_name, "-13216", SCRIPT_KEYS)

    # Write bundle resources
    cyrillic_res_path = os.path.join(RES_DIR, f"{cyrillic_name}.keylayout")
    script_res_path = os.path.join(RES_DIR, f"{script_name}.keylayout")
    with open(cyrillic_res_path, "w", encoding="utf-8") as f:
        f.write(cyrillic_xml)
    with open(script_res_path, "w", encoding="utf-8") as f:
        f.write(script_xml)

    # Write standalone keylayouts in macos/
    cyrillic_standalone = os.path.join(MACOS_DIR, f"{cyrillic_name}.keylayout")
    script_standalone = os.path.join(MACOS_DIR, f"{script_name}.keylayout")
    with open(cyrillic_standalone, "w", encoding="utf-8") as f:
        f.write(cyrillic_xml)
    with open(script_standalone, "w", encoding="utf-8") as f:
        f.write(script_xml)

    # Copy icons
    src_cyr_icon = os.path.join(RES_DIR, "Mongolian.icns")
    src_script_icon = os.path.join(RES_DIR, "Mongolian (traditional).icns")

    shutil.copy2(src_cyr_icon, os.path.join(RES_DIR, f"{cyrillic_name}.icns"))
    shutil.copy2(src_cyr_icon, os.path.join(MACOS_DIR, f"{cyrillic_name}.icns"))

    shutil.copy2(src_script_icon, os.path.join(RES_DIR, f"{script_name}.icns"))
    shutil.copy2(src_script_icon, os.path.join(MACOS_DIR, f"{script_name}.icns"))

    # Remove obsolete files from bundle and macos/
    obsolete_files = [
        os.path.join(RES_DIR, "Mongolian (qwerty).keylayout"),
        os.path.join(RES_DIR, "Mongolian (qwerty).icns"),
        os.path.join(RES_DIR, "Mongolian (traditional).keylayout"),
        os.path.join(RES_DIR, "MongolianCyrillicErgonomic.keylayout"),
        os.path.join(RES_DIR, "MongolianCyrillicErgonomic.icns"),
        os.path.join(RES_DIR, "Mongolian Cyrillic (Bachka).keylayout"),
        os.path.join(RES_DIR, "Mongolian Cyrillic (Bachka).icns"),
        os.path.join(RES_DIR, "Mongolian Script (Bachka).keylayout"),
        os.path.join(RES_DIR, "Mongolian Script (Bachka).icns"),
        os.path.join(MACOS_DIR, "MongolianCyrillicErgonomic.keylayout"),
        os.path.join(MACOS_DIR, "MongolianCyrillicErgonomic.icns"),
        os.path.join(MACOS_DIR, "Mongolian Cyrillic (Bachka).keylayout"),
        os.path.join(MACOS_DIR, "Mongolian Cyrillic (Bachka).icns"),
        os.path.join(MACOS_DIR, "Mongolian Script (Bachka).keylayout"),
        os.path.join(MACOS_DIR, "Mongolian Script (Bachka).icns"),
    ]
    for obs in obsolete_files:
        if os.path.exists(obs):
            os.remove(obs)
            print(f"  Removed obsolete: {os.path.basename(obs)}")

    # Update Info.plist
    info_plist_path = os.path.join(BUNDLE_DIR, "Contents", "Info.plist")
    info_plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>English</string>
	<key>CFBundleIdentifier</key>
	<string>org.sil.ukelele.keyboardlayout.mongolian</string>
	<key>CFBundleName</key>
	<string>Mongolian</string>
	<key>CFBundleShortVersionString</key>
	<string>2.2</string>
	<key>CFBundleVersion</key>
	<string>2.2</string>
	<key>CFBundlePackageType</key>
	<string>BNDL</string>

	<key>KLInfo_{cyrillic_name}</key>
	<dict>
		<key>TICapsLockLanguageSwitchCapable</key>
		<false/>
		<key>TISIconIsTemplate</key>
		<false/>
		<key>TISInputSourceID</key>
		<string>org.sil.ukelele.keyboardlayout.mongolian.cyrillic</string>
		<key>TISIntendedLanguage</key>
		<string>mn-Cyrl</string>
	</dict>

	<key>KLInfo_{script_name}</key>
	<dict>
		<key>TICapsLockLanguageSwitchCapable</key>
		<false/>
		<key>TISIconIsTemplate</key>
		<false/>
		<key>TISInputSourceID</key>
		<string>org.sil.ukelele.keyboardlayout.mongolian.script</string>
		<key>TISIntendedLanguage</key>
		<string>mn-Mong</string>
	</dict>
</dict>
</plist>
"""
    with open(info_plist_path, "w", encoding="utf-8") as f:
        f.write(info_plist_content)

    # Update en.lproj/InfoPlist.strings
    en_strings_path = os.path.join(RES_DIR, "en.lproj", "InfoPlist.strings")
    en_strings_content = f""""{cyrillic_name}" = "{cyrillic_name}";
"{script_name}" = "{script_name}";
"""
    with open(en_strings_path, "w", encoding="utf-8") as f:
        f.write(en_strings_content)

    # Update mn.lproj/InfoPlist.strings
    mn_strings_path = os.path.join(RES_DIR, "mn.lproj", "InfoPlist.strings")
    mn_strings_content = f""""{cyrillic_name}" = "Монгол Кирилл (Цэнгэл)";
"{script_name}" = "Худам Монгол бичиг (Цэнгэл)";
"""
    with open(mn_strings_path, "w", encoding="utf-8") as f:
        f.write(mn_strings_content)

    # Update version.plist
    ver_plist_path = os.path.join(BUNDLE_DIR, "Contents", "version.plist")
    ver_plist_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>BuildVersion</key>
	<string>2.2</string>
	<key>CFBundleShortVersionString</key>
	<string>2.2</string>
	<key>CFBundleVersion</key>
	<string>2.2</string>
	<key>ProjectName</key>
	<string>Mongolian</string>
	<key>SourceVersion</key>
	<string>2.2</string>
</dict>
</plist>
"""
    with open(ver_plist_path, "w", encoding="utf-8") as f:
        f.write(ver_plist_content)

    # Sync Fonts
    os.makedirs(MACOS_FONTS_DIR, exist_ok=True)
    os.makedirs(WINDOWS_FONTS_DIR, exist_ok=True)
    for font_file in os.listdir(DATA_FONTS_DIR):
        if font_file.endswith(".ttf"):
            src = os.path.join(DATA_FONTS_DIR, font_file)
            shutil.copy2(src, os.path.join(MACOS_FONTS_DIR, font_file))
            shutil.copy2(src, os.path.join(WINDOWS_FONTS_DIR, font_file))
            print(f"  Synced font: {font_file}")

    print("✅ macOS layouts and fonts successfully updated!")

if __name__ == "__main__":
    main()

