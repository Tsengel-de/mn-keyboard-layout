# 🇲🇳 Universal Mongolian Keyboard Layout Suite
### For Linux • macOS • Windows • Web

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20|%20macOS%20|%20Windows%20|%20Web-green.svg)]()
[![Editions](https://img.shields.io/badge/Editions-Modern%20|%20Classic%20|%20Bichig-purple.svg)]()
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
Includes native `.keylayout` files, menu bar `.icns` flag icons, and traditional OpenType fonts:

* **In Finder**: Double-click `macos/install.command` (no admin password required).
* **In Terminal**:
  ```bash
  cd macos
  ./install.sh
  ```
* **To Activate**:
  1. Open `System Settings` $\rightarrow$ `Keyboard` $\rightarrow$ `Text Input` (Input Sources) $\rightarrow$ `Edit`.
  2. Click `+` and select under `Mongolian`:
     - `Mongolian Cyrillic Ergonomic (Tsengel)` (Modern Edition)
     - `Mongolian Cyrillic Qwerty (Dusal)` (Classic Edition)
     - `Mongolian Script Qwerty (Dusal)` (Classical Bichig)
  3. If they don't appear immediately, log out and log back in.

---

### 🪟 3. Windows (Windows 7 / 10 / 11)

#### A. Classic Edition (Pre-compiled Installers)
* **US QWERTY Keyboards**: Run `windows/us-qwerty/setup.exe`.
* **German QWERTZ Keyboards**: Run `windows/de-qwertz/setup.exe`.
* **PowerShell One-Liner**:
  ```powershell
  cd windows
  .\install.ps1 -Base us    # For US English keyboards
  .\install.ps1 -Base de    # For German keyboards
  ```

#### B. Modern Edition (`Q=Ө, W=Ү`)
* Open [windows/Mongolian-Ergonomic.klc](windows/Mongolian-Ergonomic.klc) in [Microsoft Keyboard Layout Creator (MSKLC)](https://www.microsoft.com/en-us/download/details.aspx?id=102134) and click `Project -> Build DLL and Setup Package`.

---

## Cryptographic Checksums (SHA-256)

Verify the integrity of Windows installer binaries:

```text
15ce2f9346c044e1cd1692c44fa3636824de5b4b4a59951928394dd27a1d50f1  windows/us-qwerty/setup.exe
76ccc495ebb4bb607cac1131d2f37e2f5f5e1e3608ee158f1b1d99383d61106f  windows/us-qwerty/Mongol_amd64.msi
9f319ac0df4249b3513e4addfbfad1c529cd954de446e9935c114ec43ee5a385  windows/us-qwerty/Mongol_i386.msi
2e41d84f25911b39ddeb54b4920659103e10059431fc84300250ad2fb93ca757  windows/de-qwertz/setup.exe
3f99b4924801ae77c77a1aaea9b802f4e08d3127e7d2df04b3041516f01141c4  windows/de-qwertz/mongolis_amd64.msi
0bdc67fdb550119c6a461415432aee7cc15fe71954a938f6547704d75439e385  windows/de-qwertz/mongolis_i386.msi
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
* **Dusal.net (D. Dusal)**:
  - [Dusal.net / Dusal Bicheech](http://dusal.blogmn.net/99944/) — Pioneering work on Mongolian phonetic QWERTY layouts and macOS Classical Mongol Bichig keylayouts and fonts. Special thanks to D. Dusal for laying the groundwork for digital Mongolian typing.

---

## Author & License

This project is open-source under the [MIT License](LICENSE).
* Author: **Tsengel** — [tsengel.de](https://tsengel.de) (also [blog.tsengel.de](https://blog.tsengel.de))
* Contributions, feedback, and improvements are welcome via GitHub Issues and Pull Requests.

