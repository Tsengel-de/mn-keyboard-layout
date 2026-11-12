# 🇲🇳 Universelles mongolisches Tastaturlayout
### Für Linux • macOS • Windows • Web

[![Lizenz: MIT](https://img.shields.io/badge/Lizenz-MIT-blue.svg)](LICENSE)
[![Plattform](https://img.shields.io/badge/Plattform-Linux%20|%20macOS%20|%20Windows%20|%20Web-green.svg)]()
[![Editionen](https://img.shields.io/badge/Editionen-Modern%20|%20Klassisch%20|%20Bichig-purple.svg)]()
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-ff5e5b?logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)
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
Offizielles Apple `Mongolian.bundle`-Paket mit virtuellem DMG-Installationsimage:

* **Installation über Disk Image (.dmg — Empfohlenes Drag & Drop)**:
  1. Öffnen Sie `Mongolian-Keyboard-macOS.dmg` per Doppelklick (wird als **`Mongolian Keyboard`** in der Finder-Seitenleiste unter Orte gemountet).
  2. Öffnen Sie die Verknüpfung **`Keyboard Layouts`** per Doppelklick im Finder.
  3. Ziehen Sie **`Mongolian.bundle`** in den geöffneten Ordner (Mac-Passwort oder Touch ID eingeben falls verlangt).
  4. Gehen Sie zurück zum Fenster `Mongolian Keyboard` und öffnen Sie **`Fonts (System)`** per Doppelklick.
  5. Ziehen Sie die Schriftarten aus **`Fonts`** in den geöffneten Ordner `Fonts (System)`.
  6. Klicken Sie im Finder neben `Mongolian Keyboard` auf **Auswerfen (⏏️ / Eject)**, um das Disk-Image zu trennen.
* **Im Terminal (Aus Quellcode)**:
  ```bash
  cd macos
  ./install.sh
  ```
* **Aktivierung in macOS**:
  1. Öffnen Sie `Systemeinstellungen` $\rightarrow$ `Tastatur` $\rightarrow$ `Texteingabe` (Eingabequellen) $\rightarrow$ `Bearbeiten...`.
  2. Klicken Sie auf `+` und suchen Sie nach `Mongolisch`:
     - `Mongolian Cyrillic Ergonomic (Tsengel)` (Moderne Ergonomie Q=Ө, W=Ү)
     - `Mongolian Cyrillic Qwerty (Dusal)` (Klassisch [=ө, ]=ү)
     - `Mongolian Script Qwerty (Dusal)` (Traditionelle mongolische Schrift)
  3. Klicken Sie auf `Hinzufügen`. *(Falls die Tastaturlayouts nicht sofort in der Liste erscheinen, melden Sie sich einmal kurz ab und wieder an).*

---

### 🪟 3. Windows (Windows 7 / 10 / 11)

#### A. Eigenständiger All-in-One-Installer (Empfohlen ⭐)
* Laden Sie **[Mongolian-Keyboard-Windows-Setup.exe](https://mn.tsengel.de/downloads/Mongolian-Keyboard-Windows-Setup.exe)** herunter und führen Sie die Datei aus.
* Wählen Sie im Installationsassistenten Ihren Tastaturtyp (US QWERTY oder Deutsch QWERTZ) sowie die TrueType-Schriftarten für die traditionelle Schrift aus.
* Wechseln Sie jederzeit mit `Win + Leertaste`.

#### B. PowerShell & Quellarchiv
* Für eine skriptgestützte Installation:
  ```powershell
  cd windows
  .\install.ps1 -Base us    # Für US-Englisch Tastaturen
  .\install.ps1 -Base de    # Für deutsche Tastaturen
  ```
* Das MSKLC-Quelllayout [windows/Mongolian-Ergonomic.klc](windows/Mongolian-Ergonomic.klc) kann zudem mit dem [Microsoft Keyboard Layout Creator (MSKLC)](https://www.microsoft.com/en-us/download/details.aspx?id=102134) angepasst werden.

---

## Kryptografische Prüfsummen (SHA-256)

Überprüfen Sie die Integrität und Sicherheit aller Installationspakete:

```text
# 🪟 Windows
72967d6b31fd4e7501a752ac4fcc0c5ef0819798725185b239b9fc1609dbc7e3  Mongolian-Keyboard-Windows-Setup.exe
6527ddc3d370cf7a775314b23f742ef196320f2700a4b63bdf3517a25496d8a2  Mongolian-Keyboard-Windows.zip

# 🍏 macOS
ae1ef0c9be107a5f5cb9a59a0752f56d0b5eebece0b1272471ff0f49bf7f7bd5  Mongolian-Keyboard-macOS.dmg
7d4a4f05fae5d8c0e1df4a6ee544a36d41cc43c01e9e632731af8e9c5d16e1f8  Mongolian-Keyboard-macOS.zip

# 🐧 Linux
f80cf44cd61691ba742cec33de169d54e02f5625a87880dbdc2cbfd373a16aed  Mongolian-Keyboard-Linux.zip
438a636ad6b155865c22e6c6bd8020409ba9a8f1d8357cc6126acf40ffa4b8a4  install-linux.sh
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

## Unterstützung (Support & Spenden)

Wenn dieses Tastaturpaket für Sie nützlich ist, können Sie die Weiterentwicklung und Infrastruktur gerne unterstützen:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Unterstützen-ff5e5b?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)

---

## Autor & Lizenz

Dieses Projekt ist Open-Source unter der [MIT-Lizenz](LICENSE).
* Autor: **Tsengel** — [tsengel.de](https://tsengel.de) (sowie [blog.tsengel.de](https://blog.tsengel.de))
* Beiträge, Verbesserungsvorschläge und Feedback sind via GitHub Issues und Pull Requests herzlich willkommen.

