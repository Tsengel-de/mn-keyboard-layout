# 🇲🇳 Universelles mongolisches Tastaturlayout
### Für Linux • macOS • Windows • Web

[![Lizenz: MIT](https://img.shields.io/badge/Lizenz-MIT-blue.svg)](LICENSE)
[![Plattform](https://img.shields.io/badge/Plattform-Linux%20|%20macOS%20|%20Windows%20|%20Web-green.svg)]()
[![Editionen](https://img.shields.io/badge/Editionen-Modern%20|%20Klassisch%20|%20Bichig-purple.svg)]()
[![Autor: Tsengel](https://img.shields.io/badge/Autor-Tsengel%20(tsengel.de)-red.svg)](https://tsengel.de)

**Sprachen:** [🇲🇳 Монгол](README.md) • [🇬🇧 English](README.en.md) • [🇩🇪 Deutsch](README.de.md)

> **„Auf Mongolisch zu tippen sollte niemals mühsam, langsam oder frustrierend sein.“**  
> Eine einheitliche, ergonomische Hochgeschwindigkeits-Tastatursuite für Mongolinnen und Mongolen weltweit, Diaspora-Gemeinschaften, Entwickler und Sprachbegeisterte – optimiert für US-QWERTY- und deutsche QWERTZ-Tastaturen.

---

## 🗺️ Layout-Übersichten

### 1. Moderne Edition (Empfohlen ⭐)
> **Grundprinzip**: `Q = Ө`, `W = Ү`. Alle mongolischen Vokale befinden sich direkt in den zentralen Grund- und Oberreihen für flüssiges Zehnfingerschreiben. Programmier- und Textklammern (`[ ]`, `{ }`, `\`, `|`) bleiben vollständig nativ erreichbar, ohne das Tastaturlayout umschalten zu müssen.

![Modernes ergonomisches Layout](docs/images/layout-ergonomic-normal.png)

### 2. AltGr-Erweiterungsebene (₮, « », —, \u202F)
> Das Halten der **rechten Alt-Taste (AltGr)** bzw. der **macOS Wahltaste (Option)** bietet sofortigen Zugriff auf die offizielle mongolische Typografie: das Tugrik-Währungssymbol (**`₮`**), typografische Anführungszeichen (**`« »`**), den Gedankenstrich (**`—`**) sowie das schmale geschützte Leerzeichen (**`\u202F` NNBSP**) für grammatikalische Suffixe der traditionellen Schrift.

![AltGr-Erweiterungsebene](docs/images/layout-ergonomic-altgr.png)

### 3. Klassische Edition (Original von 2021)
> Phonetisches Layout mit Vokalpaarung: `[` $\rightarrow$ `ө`, `]` $\rightarrow$ `ү`, `Q` $\rightarrow$ `ъ`, `W` $\rightarrow$ `ь`.

![Klassisches Layout](docs/images/layout-classic-normal.png)

### 4. Traditionelle mongolische Schrift (Hudam Mongol Bichig)
> Nutzt dieselben Fingergewohnheiten wie das kyrillische Layout mit 100% übereinstimmendem Muskelgedächtnis: `Q` = `ᠥ` (Ö), `W` = `ᠦ` (Ü), `E` = `ᠡ` (E), `O` = `ᠣ` (O), `U` = `ᠤ` (U), `I` = `ᠢ` (I), `A` = `ᠠ` (A). Die Ziffernreihe tippt direkt die traditionellen mongolischen Ziffern (`᠐ ᠑ ᠒ ᠓ ᠔ ᠕ ᠖ ᠗ ᠘ ᠙`).

![Traditionelle mongolische Schrift](docs/images/layout-bichig.png)

---

## ⌨️ Tastenbelegung & Referenztabelle

| Taste | Moderne Edition | Klassische Edition | Umschalt + Taste (Modern) | AltGr (Rechte Alt-Taste) |
|:---:|:---:|:---:|:---:|:---:|
| `Q` | **ө** (Weiches O) | **ъ** | **Ө** | **ъ** (Härtezeichen) |
| `W` | **ү** (Weiches U) | **ь** | **Ү** | **ь** (Weichheitszeichen) |
| `E` | **э** | **э** | **Э** | € (Euro) |
| `T` | **т** | **т** | **Т** | **₮ (Tugrik \u20AE)** |
| `Y` | **й** | **е** | **Й** | **е** |
| `[` | **[** (Eckige Klammer) | **ө** | **{** (Geschweifte Klammer) | **«** (Anführungszeichen links) |
| `]` | **]** (Eckige Klammer) | **ү** | **}** (Geschweifte Klammer) | **»** (Anführungszeichen rechts) |
| `\` | **\\** (Backslash) | **й** | **\|** (Pipe-Symbol) | **\|** |
| `;` | **;** | **щ** | **:** | **щ** |
| `'` | **ы** | **ы** | **Ы** | **'** / **"** |
| `4` | 4 | 4 | $ | **₮ (Tugrik)** |
| `-` | - | - | _ | **— (Gedankenstrich)** |
| `Leertaste` | Leerzeichen | Leerzeichen | Leerzeichen | **\u202F (NNBSP Suffix-Leerzeichen)** |

---

## Installationsanleitungen

### 🐧 1. Linux (Ubuntu, Debian, Fedora, Arch)
Ein einziger Befehl installiert **alle 3 Editionen gleichzeitig** in das systemweite XKB-Verzeichnis:

```bash
cd linux
sudo ./install.sh
```

Nach der Installation stehen alle 3 Editionen sofort zur Verfügung:
1. **Standard**: `Mongolian (Modern Ergonomic)` (`Q=Ө, W=Ү`)
2. **Klassisch**: `Mongolian (Classic Tsengel)` (`[=ө, ]=ү`)
3. **Bichig**: `Mongolian Script (Bichig)` (Traditionelle mongolische Schrift)

* **Terminal-Umschaltung (X11)**:
  - `setxkbmap mn` (Moderne Edition)
  - `setxkbmap mn -variant classic` (Klassische Edition)
  - `setxkbmap mn -variant bichig` (Traditionelle Schrift)
* **Desktop (GNOME / KDE / Ubuntu)**:
  - Öffnen Sie `Einstellungen` $\rightarrow$ `Tastatur` $\rightarrow$ `Eingabequellen` $\rightarrow$ `+` (Hinzufügen) $\rightarrow$ `Mongolisch`. Umschalten jederzeit mit **`Super (Win) + Leertaste`**.
* **Deinstallation / Wiederherstellung**: `cd linux && sudo ./uninstall.sh`.

---

### 🍏 2. macOS (Apple OS X / macOS)
Enthält native `.keylayout`-Dateien, Menüleisten-Icons (`.icns`) mit mongolischer Flagge und traditionelle OpenType-Schriftarten:

* **Im Finder**: Doppelklick auf `macos/install.command` (kein Administratorpasswort erforderlich).
* **Im Terminal**:
  ```bash
  cd macos
  ./install.sh
  ```
* **Aktivierung in macOS**:
  1. Öffnen Sie `Systemeinstellungen` $\rightarrow$ `Tastatur` $\rightarrow$ `Texteingabe` (Eingabequellen) $\rightarrow$ `Bearbeiten`.
  2. Klicken Sie auf `+` und wählen Sie unter `Mongolisch`:
     - `Mongolian Cyrillic Ergonomic (Tsengel)` (Moderne Edition)
     - `Mongolian Cyrillic Qwerty (Dusal)` (Klassische Edition)
     - `Mongolian Script Qwerty (Dusal)` (Traditionelle Schrift)
  3. Falls die Layouts nicht sofort in der Liste erscheinen, melden Sie sich einmal kurz ab und wieder an.

---

### 🪟 3. Windows (Windows 7 / 10 / 11)

#### A. Klassische Edition (Vorkompilierte Installationsprogramme)
* **US-QWERTY-Tastaturen**: Führen Sie `windows/us-qwerty/setup.exe` aus.
* **Deutsche QWERTZ-Tastaturen**: Führen Sie `windows/de-qwertz/setup.exe` aus.
* **Automatisierte PowerShell-Installation**:
  ```powershell
  cd windows
  .\install.ps1 -Base us    # Für US-Englisch Tastaturen
  .\install.ps1 -Base de    # Für deutsche Tastaturen
  ```

#### B. Moderne Edition (`Q=Ө, W=Ү`)
* Öffnen Sie [windows/Mongolian-Ergonomic.klc](windows/Mongolian-Ergonomic.klc) im kostenlosen [Microsoft Keyboard Layout Creator (MSKLC)](https://www.microsoft.com/en-us/download/details.aspx?id=102134) und wählen Sie `Project -> Build DLL and Setup Package`.

---

## Kryptografische Prüfsummen (SHA-256)

Überprüfen Sie die Integrität der Binärdateien für Windows:

```text
15ce2f9346c044e1cd1692c44fa3636824de5b4b4a59951928394dd27a1d50f1  windows/us-qwerty/setup.exe
76ccc495ebb4bb607cac1131d2f37e2f5f5e1e3608ee158f1b1d99383d61106f  windows/us-qwerty/Mongol_amd64.msi
9f319ac0df4249b3513e4addfbfad1c529cd954de446e9935c114ec43ee5a385  windows/us-qwerty/Mongol_i386.msi
2e41d84f25911b39ddeb54b4920659103e10059431fc84300250ad2fb93ca757  windows/de-qwertz/setup.exe
3f99b4924801ae77c77a1aaea9b802f4e08d3127e7d2df04b3041516f01141c4  windows/de-qwertz/mongolis_amd64.msi
0bdc67fdb550119c6a461415432aee7cc15fe71954a938f6547704d75439e385  windows/de-qwertz/mongolis_i386.msi
```

---

## 🌐 Interaktiver Web-Visualisierer
Testen Sie das Tastaturlayout direkt und interaktiv im Webbrowser, ganz ohne Installation:
* **Live-Webanwendung:** [mn.tsengel.de](https://mn.tsengel.de) • [gar.tsengel.de](https://gar.tsengel.de) • [bichig.tsengel.de](https://bichig.tsengel.de)
* **Lokale Vorschau:**
```bash
xdg-open web/index.html
```

---

## Quellen & Danksagung (Sources & Attribution)

Dieses Projekt baut auf der wertvollen Vorarbeit früherer Open-Source-Initiativen auf:
* **bachka-keyboard Projekte (Vorgängerprojekte von Tsengel/Bachka)**:
  - [mongolian-keyboard-layout-linux](https://github.com/bachka/mongolian-keyboard-layout-linux) — Ursprüngliche Linux-XKB-Layout-Basis
  - [mongolian-kbl-english-kb](https://github.com/bachka/mongolian-kbl-english-kb) — Windows US-QWERTY-Installer und MSKLC-Quellcode
  - [mongolian-kbl-german-kb](https://github.com/bachka/mongolian-kbl-german-kb) — Windows deutsche QWERTZ-Installer und MSKLC-Quellcode
* **Dusal.net (D. Dusal)**:
  - [Dusal.net / Dusal Bicheech](http://dusal.blogmn.net/99944/) — Pionierarbeit bei phonetischen mongolischen Tastaturlayouts und macOS-Keylayouts/Schriften für die traditionelle mongolische Schrift. Herzlichen Dank an D. Dusal für die Grundlagen der digitalen mongolischen Tastaturbelegung.

---

## Autor & Lizenz

Dieses Projekt ist Open-Source unter der [MIT-Lizenz](LICENSE).
* Autor: **Tsengel** — [tsengel.de](https://tsengel.de) (sowie [blog.tsengel.de](https://blog.tsengel.de))
* Beiträge, Verbesserungsvorschläge und Feedback sind via GitHub Issues und Pull Requests herzlich willkommen.

