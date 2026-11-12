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
Official Apple `Mongolian.bundle` package with native DMG disk image:

* **Installation via Disk Image (.dmg — Recommended Drag & Drop)**:
  1. Double-click `Mongolian-Keyboard-macOS.dmg` to mount the disk (named **`Mongolian Keyboard`** in Finder sidebar under Locations).
  2. Double-click the **`Keyboard Layouts`** folder shortcut to open it in Finder.
  3. Drag and drop **`Mongolian.bundle`** into that opened folder (enter your Mac password or Touch ID if prompted).
  4. Return to the `Mongolian Keyboard` disk window, double-click the **`Fonts (System)`** folder shortcut.
  5. Drag and drop the font files from the **`Fonts`** folder into the opened `Fonts (System)` folder.
  6. In Finder's Locations sidebar, click **Eject (⏏️)** next to `Mongolian Keyboard` to unmount the disk.
* **Via Terminal (From source)**:
  ```bash
  cd macos
  ./install.sh
  ```
* **To Activate in macOS**:
  1. Open `System Settings` $\rightarrow$ `Keyboard` $\rightarrow$ `Text Input` (Input Sources) $\rightarrow$ click `Edit...`.
  2. Click `+` and search for `Mongolian`:
     - `Mongolian Cyrillic Ergonomic (Tsengel)` (Modern Ergonomic Q=Ө, W=Ү)
     - `Mongolian Cyrillic Qwerty (Dusal)` (Classic [=ө, ]=ү)
     - `Mongolian Script Qwerty (Dusal)` (Classical Mongolian script)
  3. Click `Add`. *(If the newly installed layouts do not appear immediately in the list, simply log out and log back in).*

---

### 🪟 3. Windows (Windows 7 / 10 / 11)

#### A. Standalone All-in-One Installer (Recommended ⭐)
* Download and run **[Mongolian-Keyboard-Windows-Setup.exe](https://mn.tsengel.de/downloads/Mongolian-Keyboard-Windows-Setup.exe)**.
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
# 🪟 Windows
72967d6b31fd4e7501a752ac4fcc0c5ef0819798725185b239b9fc1609dbc7e3  Mongolian-Keyboard-Windows-Setup.exe
6527ddc3d370cf7a775314b23f742ef196320f2700a4b63bdf3517a25496d8a2  Mongolian-Keyboard-Windows.zip

# 🍏 macOS
56ae08fe2a02ad7134ba6dc896f946eea065e93bfe5340852f724ec10d09242e  Mongolian-Keyboard-macOS.dmg
42faf9c4fc77ccca14ab57dcbb605f59c9d58dc3d370053b130c8509ce6a408e  Mongolian-Keyboard-macOS.zip

# 🐧 Linux
f80cf44cd61691ba742cec33de169d54e02f5625a87880dbdc2cbfd373a16aed  Mongolian-Keyboard-Linux.zip
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

