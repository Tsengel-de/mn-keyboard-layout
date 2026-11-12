# 🇲🇳 Universal Mongolian Keyboard Layout Suite
### For Linux • macOS • Windows • Web

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20|%20macOS%20|%20Windows%20|%20Web-green.svg)]()
[![Editions](https://img.shields.io/badge/Editions-Modern%20|%20Classic%20|%20Bichig-purple.svg)]()
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-ff5e5b?logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)
[![Author: Tsengel](https://img.shields.io/badge/Author-Tsengel%20(tsengel.de)-red.svg)](https://tsengel.de)

**Languages:** [🇲🇳 Монгол](README.md) • [🇬🇧 English](README.en.md) • [🇩🇪 Deutsch](README.de.md)

> **"Typing in Mongolian should never be slow, frustrating, or complicated."**  
> A unified, high-speed, ergonomic keyboard layout suite designed for Mongolians worldwide, diaspora communities, developers, and language learners typing on US QWERTY and German QWERTZ keyboards.

---

## 🗺️ Layout Diagrams

### 1. Modern Edition (Recommended ⭐)
> **Key concept**: `Q = Ө`, `W = Ү`. All Mongolian vowels are located directly on the central home/top rows for high-speed 10-finger typing. Standard programming and text brackets (`[ ]`, `{ }`, `\`, `|`) remain completely native without layout switching.

![Modern Ergonomic Layout](docs/images/layout-ergonomic-normal.png)

### 2. AltGr Extension Layer (₮, « », —, \u202F)
> Holding **Right Alt (AltGr)** or **macOS Option** gives instant access to official Mongolian typography: the Tugrik currency symbol (**`₮`**), official quotes (**`« »`**), em-dash (**`—`**), and the Narrow No-Break Space (**`\u202F` NNBSP**) for Classical script suffixes.

![AltGr Extension Layer](docs/images/layout-ergonomic-altgr.png)

### 3. Classic Edition (2021 Original)
> Vowel-paired layout where `[` $\rightarrow$ `ө`, `]` $\rightarrow$ `ү`, `Q` $\rightarrow$ `ъ`, `W` $\rightarrow$ `ь`.

![Classic Layout](docs/images/layout-classic-normal.png)

### 4. Traditional Script Edition (Classical Mongol Bichig)
> Matches Cyrillic finger habits with 100% muscle memory: `Q` = `ᠥ` (Ö), `W` = `ᠦ` (Ü), `E` = `ᠡ` (E), `O` = `ᠣ` (O), `U` = `ᠤ` (U), `I` = `ᠢ` (I), `A` = `ᠠ` (A). The number row directly types classical Mongolian numerals (`᠐ ᠑ ᠒ ᠓ ᠔ ᠕ ᠖ ᠗ ᠘ ᠙`).

![Classical Mongol Bichig Layout](docs/images/layout-bichig.png)

---

## ⌨️ Key Mapping Reference

| Key | Modern Edition | Classic Edition | Shift + Key (Modern) | AltGr (Right Alt) |
|:---:|:---:|:---:|:---:|:---:|
| `Q` | **ө** (Feminine O) | **ъ** | **Ө** | **ъ** (Hard sign) |
| `W` | **ү** (Feminine U) | **ь** | **Ү** | **ь** (Soft sign) |
| `E` | **э** | **э** | **Э** | € (Euro) |
| `T` | **т** | **т** | **Т** | **₮ (Tugrik \u20AE)** |
| `Y` | **й** | **е** | **Й** | **е** |
| `[` | **[** (Native bracket) | **ө** | **{** (Native brace) | **«** (Left angle quote) |
| `]` | **]** (Native bracket) | **ү** | **}** (Native brace) | **»** (Right angle quote) |
| `\` | **\\** (Native slash) | **й** | **\|** (Native pipe) | **\|** |
| `;` | **;** | **щ** | **:** | **щ** |
| `'` | **ы** | **ы** | **Ы** | **'** / **"** |
| `4` | 4 | 4 | $ | **₮ (Tugrik)** |
| `-` | - | - | _ | **— (Em-dash)** |
| `Space` | Space | Space | Space | **\u202F (NNBSP space)** |

---

## Installation Guides

### 🐧 1. Linux (Ubuntu, Debian, Fedora, Arch)
A single command installs **all 3 editions simultaneously** into system XKB:

```bash
cd linux
sudo ./install.sh
```

After installation, all 3 editions are available immediately:
1. **Default**: `Mongolian (Modern Ergonomic)` (`Q=Ө, W=Ү`)
2. **Classic**: `Mongolian (Classic Tsengel)` (`[=ө, ]=ү`)
3. **Bichig**: `Mongolian Script (Bichig)` (Classical Mongol Bichig)

* **Terminal Switch (X11)**:
  - `setxkbmap mn` (Modern Edition)
  - `setxkbmap mn -variant classic` (Classic Edition)
  - `setxkbmap mn -variant bichig` (Traditional Bichig)
* **Desktop (GNOME / KDE / Ubuntu)**:
  - Go to `Settings` $\rightarrow$ `Keyboard` $\rightarrow$ `Input Sources` $\rightarrow$ Add `Mongolian`. Toggle anytime with **`Win + Space`**.
* **To Revert**: `cd linux && sudo ./uninstall.sh`.

---

### 🍏 2. macOS (Apple OS X / macOS)
Official Apple-standard `Mongolian.bundle` and installer for macOS:

* **Installation via Virtual Disk (.dmg — Recommended One-Click Method)**:
  1. Double-click `Mongolian-Keyboard-macOS-v1.0.3.dmg` to open it.
  2. Open **`Keyboard Installer.app`** inside and drag **`Mongolian.bundle`** into its window.
  3. *(Manual installation)*: Open Finder, press **Cmd + Shift + G**, navigate to `~/Library/Keyboard Layouts`, and copy `Mongolian.bundle` or `MongolianCyrillicErgonomic.keylayout` into it.
  4. **CRITICAL: You MUST Log Out of macOS and log back in (or Restart your Mac)**. macOS only compiles and caches keyboard layouts into memory during user login.
* **To Activate in macOS**:
  1. Go to `System Settings` $\rightarrow$ `Keyboard` $\rightarrow$ `Text Input` (Input Sources) $\rightarrow$ click `Edit...` (or `+`).
  2. Under `Mongolian`, select **`Mongolian Cyrillic Ergonomic (Tsengel)`** and click `Add`.
  3. The bundle also provides `Mongolian (qwerty)` and `Mongolian (traditional)` (Classical Mongol Bichig).

---

### 🪟 3. Windows (Windows 7 / 10 / 11)

#### A. Standalone All-in-One Installer (Recommended ⭐)
* Download and run **[Mongolian-Keyboard-Windows-Setup-v1.0.3.exe](https://mn.tsengel.de/downloads/Mongolian-Keyboard-Windows-Setup-v1.0.3.exe)**.
* Select your physical keyboard type (US QWERTY or German QWERTZ) and install TrueType Mongolian script fonts in a single wizard.
* Switch anytime using `Win + Space`.

#### B. PowerShell & Source Archive
* For silent or scripted installations:
  ```powershell
  cd windows
  .\install.ps1 -Base us    # For US English keyboards
  .\install.ps1 -Base de    # For German keyboards
  ```
* You can also inspect or modify the source layout file [windows/Mongolian-Ergonomic.klc](windows/Mongolian-Ergonomic.klc) using [Microsoft Keyboard Layout Creator (MSKLC)](https://www.microsoft.com/en-us/download/details.aspx?id=102134).

---

## Cryptographic Checksums (SHA-256)

Verify the integrity and authenticity of all release download packages:

```text
# 🪟 Windows (v1.0.3)
72967d6b31fd4e7501a752ac4fcc0c5ef0819798725185b239b9fc1609dbc7e3  Mongolian-Keyboard-Windows-Setup-v1.0.3.exe
6527ddc3d370cf7a775314b23f742ef196320f2700a4b63bdf3517a25496d8a2  Mongolian-Keyboard-Windows-v1.0.3.zip

# 🍏 macOS (v1.0.3)
aef1846dcbb065d6d1613407c479d62672c6725eb420ff531337a7fb000d2d58  Mongolian-Keyboard-macOS-v1.0.3.dmg
e4b690864179df357b0f45db72c9bffaf461cf402af0541d194d57fa87c71626  Mongolian-Keyboard-macOS-v1.0.3.zip

# 🐧 Linux (v1.0.3)
f80cf44cd61691ba742cec33de169d54e02f5625a87880dbdc2cbfd373a16aed  Mongolian-Keyboard-Linux-v1.0.3.zip
438a636ad6b155865c22e6c6bd8020409ba9a8f1d8357cc6126acf40ffa4b8a4  install-linux.sh
```

---

## 🌐 Interactive Web Visualizer
Test the keyboard layout live in your browser without installing anything:
* **Live Web App:** [mn.tsengel.de](https://mn.tsengel.de) • [gar.tsengel.de](https://gar.tsengel.de) • [bichig.tsengel.de](https://bichig.tsengel.de)
* **Local Preview:**
```bash
xdg-open web/index.html
```

---

## Sources & Attribution

This project is built upon the invaluable heritage of earlier open-source efforts:
* **bachka-keyboard Projects (Predecessors by Tsengel/Bachka)**:
  - [mongolian-keyboard-layout-linux](https://github.com/bachka/mongolian-keyboard-layout-linux) — Original Linux XKB symbols foundation
  - [mongolian-kbl-english-kb](https://github.com/bachka/mongolian-kbl-english-kb) — Windows US QWERTY installer and MSKLC source
  - [mongolian-kbl-german-kb](https://github.com/bachka/mongolian-kbl-german-kb) — Windows German QWERTZ installer and MSKLC source
* **StudyMongolian.net (Study Mongolian)**:
  - [StudyMongolian.net](https://www.studymongolian.net/technical/mongolian-keyboard-for-macos/) — Modern macOS `Mongolian.bundle` architecture, MacBook ANSI/JIS keyboard support, and Classical script layout design.
* **SIL International**:
  - [SIL International / Ukelele](https://software.sil.org/ukelele/) — macOS Unicode keyboard layout standards and the `Keyboard Installer.app` utility.
* **Dusal.net (D. Dusal)**:
  - [Dusal.net / Dusal Bicheech](http://dusal.blogmn.net/99944/) — Pioneering work on Mongolian phonetic QWERTY layouts and macOS Classical Mongol Bichig keylayouts and fonts. Special thanks to D. Dusal for laying the groundwork for digital Mongolian typing.

---

## Support & Donation

If you find this keyboard suite helpful, you can support its development and infrastructure:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-ff5e5b?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)

---

## Author & License

This project is open-source under the [MIT License](LICENSE).
* Author: **Tsengel** — [tsengel.de](https://tsengel.de) (also [blog.tsengel.de](https://blog.tsengel.de))
* Contributions, feedback, and improvements are welcome via GitHub Issues and Pull Requests.

