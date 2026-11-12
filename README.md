# 🇲🇳 Бүх Нийтийн Монгол Гарын Байрлал
### Universal Mongolian Keyboard Layout Suite (Linux • macOS • Windows • Web)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20|%20macOS%20|%20Windows%20|%20Web-green.svg)]()
[![Editions](https://img.shields.io/badge/Editions-Ergonomic%20|%20Classic%20|%20Bichig-purple.svg)]()
[![Author: Tsengel](https://img.shields.io/badge/Author-Tsengel%20(tsengel.de)-red.svg)](https://tsengel.de)

> **"Монгол хэлээр бичих нь хэзээ ч адармаатай, удаан байх ёсгүй."**  
> Дэлхий даяарх бүх монголчууд, гадаад дахь диаспора, инженерүүд, програмистууд ямар ч комьпютер дээр (US QWERTY болон German QWERTZ товчлуурт) монгол кирилл болон худам монгол бичгээр хурдан, эргономик, алдаагүй бичих нэгдсэн гарын стандарт.

---

## 🗺️ Гарын Байршлын Зураглалууд (Up-to-Date Layout Maps)

### 1. Modern Ergonomic & DevOps Edition (Шинэ Эргономик Хувилбар)
> **Зөвлөмж**: `Q = Ө`, `W = Ү`. Бүх эгшгүүд гарын үндсэн хэсэгт багтсан тул 10 хуруугаар маш хурдан шивнэ. Кодчилол, терминалын `{ } [ ] | \` хаалтууд байрандаа хадгалагдсан.

![Mongolian Modern Ergonomic Layout](docs/images/layout-ergonomic-normal.png)

### 2. AltGr Өргөтгөл Давхарга (AltGr / Option Layer: ₮, « », —, \u202F)
> Баруун `Alt` (AltGr) эсвэл Mac-ийн `Option` товчлуураар албан ёсны Төгрөгийн тэмдэгт (**`₮`**), хашилт (**`« »`**), урт зураас (**`—`**), болон Монгол бичгийн дагаврын сул зай (**`\u202F` NNBSP**) шууд гарна.

![Mongolian Ergonomic AltGr Layout](docs/images/layout-ergonomic-altgr.png)

### 3. Classic Tsengel Edition (2021 Анхны Хувилбар)
> Эгшгийн эрэмбээр `[` $\rightarrow$ `ө`, `]` $\rightarrow$ `ү`, `Q` $\rightarrow$ `ъ`, `W` $\rightarrow$ `ь` тохируулсан хувилбар.

![Mongolian Classic Layout](docs/images/layout-classic-normal.png)

### 4. Classical Mongol Bichig Edition (Худам Монгол Бичиг)
> Кирилл үсгийн байрлалтай 100% ижил дадлаар Худам монгол бичгээр шивнэ: `Q` = `ᠥ`, `W` = `ᠦ`, `E` = `ᠡ`, `O` = `ᠣ`, `U` = `ᠤ`, `I` = `ᠢ`, `A` = `ᠠ`. Тоонууд дээр сонгодог цифрүүд (`᠐ ᠑ ᠒ ᠓ ᠔ ᠕ ᠖ ᠗ ᠘ ᠙`) байрлана.

![Classical Mongol Bichig Layout](docs/images/layout-bichig.png)

---

## ⌨️ Үсэг ба Тэмдэгтүүдийн Харьцуулсан Хүснэгт (Keymap Reference)

| Товчлуур | Ergonomic (Шинэ) | Classic (2021) | Shift + Товчлуур (Ergo) | AltGr (Баруун Alt) |
|:---:|:---:|:---:|:---:|:---:|
| `Q` | **ө** (Feminine O) | **ъ** | **Ө** | **ъ** (Хатуугийн тэмдэг) |
| `W` | **ү** (Feminine U) | **ь** | **Ү** | **ь** (Зөөлний тэмдэг) |
| `E` | **э** | **э** | **Э** | € (Евро) |
| `T` | **т** | **т** | **Т** | **₮ (ТӨГРӨГ \u20AE)** |
| `Y` | **й** | **е** | **Й** | **е** |
| `[` | **[** (Кодын хаалт) | **ө** | **{** (Кодын хаалт) | **«** (Зүүн хашилт) |
| `]` | **]** (Кодын хаалт) | **ү** | **}** (Кодын хаалт) | **»** (Баруун хашилт) |
| `\` | **\\** (Кодын зураас) | **й** | **\|** (Кодын Pipe) | ¦ |
| `;` | **;** | **щ** | **:** | **щ** |
| `'` | **ы** | **ы** | **Ы** | **'** / **"** |
| `4` | 4 | 4 | $ | **₮ (Төгрөг)** |
| `-` | - | - | _ | **— (Em-dash урт зураас)** |
| `Space` | Зай | Зай | Зай | **\u202F (NNBSP бичгийн зай)** |

---

## 🚀 Суулгах Заавар (Installation Guides)

### 🐧 1. Linux (Ubuntu, Debian, Fedora, Arch)
Линукс систем дээр нэг тушаалаар **3 хувилбарыг бүгдийг нь нэгэн зэрэг** системд суулгана:

```bash
cd linux
sudo ./install.sh
```

Суулгасны дараа та дараах 3 хувилбарыг шууд ашиглах боломжтой болно:
1. **Үндсэн (Default)**: `Mongolian (Ergonomic & DevOps)` (`Q=Ө, W=Ү`)
2. **Classic**: `Mongolian (Classic Tsengel)` (`[=ө, ]=ү`)
3. **Монгол бичиг**: `Mongolian Script (Bichig)` (Худам монгол бичиг)

* **Шууд шилжүүлэх (Terminal / X11)**:
  - `setxkbmap mn` (Ergonomic үндсэн хувилбар)
  - `setxkbmap mn -variant classic` (Classic хувилбар)
  - `setxkbmap mn -variant bichig` (Худам монгол бичиг)
* **График орчин (GNOME / KDE / Ubuntu)**:
  - `Settings` $\rightarrow$ `Keyboard` $\rightarrow$ `Input Sources` $\rightarrow$ `Add 'Mongolian'` (3 хувилбараас хүссэнээ нэмээд `Win + Space`-ээр шилжинэ).
* **Буцааж анхны төлөвт оруулах**: `cd linux && sudo ./uninstall.sh`.

---

### 🍏 2. macOS (Apple OS X / macOS)
macOS-д зориулсан native `.keylayout`, `.icns` дүрс, болон монгол бичгийн фонтууд багтсан:

* **Finder дээр**: `macos/install.command` дээр хоёр товшиж ажиллуулна (нууц үг шаардахгүй).
* **Terminal дээр**:
  ```bash
  cd macos
  ./install.sh
  ```
* **Идэвхжүүлэх**:
  1. `System Settings` $\rightarrow$ `Keyboard` $\rightarrow$ `Text Input` (Input Sources) $\rightarrow$ `Edit`.
  2. `+` товч дарж `Mongolian` хэсгээс сонгоно:
     - `Mongolian Cyrillic Ergonomic (Tsengel)` (Шинэ Ergonomic хувилбар)
     - `Mongolian Cyrillic Qwerty (Dusal)` (Classic хувилбар)
     - `Mongolian Script Qwerty (Dusal)` (Худам монгол бичиг)
  3. Хэрэв шууд гарч ирэхгүй бол системээс нэг удаа Log Out хийж дахин нэвтэрнэ.

---

### 🪟 3. Windows (Windows 7 / 10 / 11)

#### А. Classic Edition (Бэлэн багцалсан суулгац)
* **US QWERTY гар дээр**: `windows/us-qwerty/setup.exe` дээр товшиж суулгана.
* **German QWERTZ гар дээр**: `windows/de-qwertz/setup.exe` дээр товшиж суулгана.
* **PowerShell тушаалаар суулгах**:
  ```powershell
  cd windows
  .\install.ps1 -Base us    # Англи суурьтай Windows гар
  .\install.ps1 -Base de    # Герман суурьтай Windows гар
  ```

#### Б. Modern Ergonomic Edition (`Q=Ө, W=Ү`)
* [windows/Mongolian-Ergonomic.klc](windows/Mongolian-Ergonomic.klc) эх файлыг [Microsoft Keyboard Layout Creator (MSKLC)](https://www.microsoft.com/en-us/download/details.aspx?id=102134) программд нээж `Project -> Build DLL and Setup Package` дарж өөрийн системд суулгана.

---

## 🔒 Аюулгүй Байдлын Шалгалт (Cryptographic Integrity & SHA-256)

Windows суулгацын файлуудыг татаж авахдаа эх хувьтайгаа 100% тохирч буйг дараах шалгах нийлбэрээр (SHA-256) баталгаажуулж болно:

```text
15ce2f9346c044e1cd1692c44fa3636824de5b4b4a59951928394dd27a1d50f1  windows/us-qwerty/setup.exe
76ccc495ebb4bb607cac1131d2f37e2f5f5e1e3608ee158f1b1d99383d61106f  windows/us-qwerty/Mongol_amd64.msi
9f319ac0df4249b3513e4addfbfad1c529cd954de446e9935c114ec43ee5a385  windows/us-qwerty/Mongol_i386.msi
2e41d84f25911b39ddeb54b4920659103e10059431fc84300250ad2fb93ca757  windows/de-qwertz/setup.exe
3f99b4924801ae77c77a1aaea9b802f4e08d3127e7d2df04b3041516f01141c4  windows/de-qwertz/mongolis_amd64.msi
0bdc67fdb550119c6a461415432aee7cc15fe71954a938f6547704d75439e385  windows/de-qwertz/mongolis_i386.msi
```

---

## 🌐 Вэб Туршигч (Interactive Web Visualizer)
Та юу ч суулгахгүйгээр хөтөч дээрээ шууд гарын тохиргоог туршиж, DevOps кодчилол шалгаж үзэж болно:
```bash
xdg-open web/index.html
```

---

## 📂 Төслийн Бүтэц (Repository Structure)

```
mn-keyboard-layout/
├── README.md               # Дэлгэрэнгүй баталгаажсан гарын авлага
├── LICENSE                 # Apache License 2.0
├── index.html              # Вэб гар руу чиглүүлэгч үндсэн хуудас
├── .github/workflows/      # GitHub Pages автомат нийтлэгч workflow
├── docs/images/            # Шинэчлэгдсэн вектор ба PNG гарын зургууд
│   ├── layout-ergonomic-normal.png
│   ├── layout-ergonomic-altgr.png
│   ├── layout-classic-normal.png
│   └── layout-bichig.png
├── linux/                  # Линукс XKB тохиргоонууд ба суулгагч
│   ├── mn-ergonomic        # Modern Ergonomic (Q=Ө, W=Ү)
│   ├── mn-custom           # Classic Tsengel layout
│   ├── mn-bichig           # Classical Mongol Bichig
│   ├── install.sh          # Сонголттой автомат суулгагч
│   └── uninstall.sh
├── macos/                  # macOS .keylayout, .icns дүрсүүд ба суулгагч
│   ├── MongolianCyrillicErgonomic.keylayout
│   ├── MongolianCyrillicErgonomic.icns
│   ├── MongolianScriptQwertyDusal.keylayout
│   ├── install.command     # Хоёр товшиж суулгах Finder скрипт
│   ├── install.sh
│   └── fonts/              # Classical Mongolian OpenType фонтууд
├── windows/                # Windows MSI суулгацууд ба MSKLC .klc эх кодууд
│   ├── Mongolian-Ergonomic.klc
│   ├── install.ps1
│   ├── us-qwerty/          # Pre-compiled setup.exe & MSI (US QWERTY)
│   └── de-qwertz/          # Pre-compiled setup.exe & MSI (German QWERTZ)
└── web/                    # Онлайн интерактив туршилтын веб апп
    └── index.html
```

---

## 🤝 Зохиогч & Нээлттэй Эрх (Author & License)

Энэхүү төсөл нь дэлхий даяарх бүх монголчуудад нээлттэй [MIT License](LICENSE) эрхтэй.
* Төслийн зохиогч: **Цэнгэл (Tsengel)** — [tsengel.de](https://tsengel.de)
* Санал хүсэлт, сайжруулалтыг GitHub Issue болон Pull Request-ээр хүлээн авна.

*Монголын үрс маш олон болж, мэдлэгийг харамгүй хуваалцан хамтдаа хөгжих болтугай! 🇲🇳*
