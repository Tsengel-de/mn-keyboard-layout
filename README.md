# 🇲🇳 Бүх Нийтийн Монгол Гарын Байрлал
### Universal Mongolian Keyboard Layout Suite (Linux • macOS • Windows • Web)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20|%20macOS%20|%20Windows%20|%20Web-green.svg)]()
[![Editions](https://img.shields.io/badge/Editions-Cyrillic%20|%20Traditional%20Script-purple.svg)]()
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-ff5e5b?logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)
[![Author: Tsengel](https://img.shields.io/badge/Author-Tsengel%20(tsengel.de)-red.svg)](https://tsengel.de)

**Хэл сонгох / Languages:** [🇲🇳 Монгол](README.md) • [🇬🇧 English](README.en.md) • [🇩🇪 Deutsch](README.de.md)

> [!IMPORTANT]
> 🌿 **Арилжааны бус • Нийтийн хүртээл**  
> **Нийтийн тусын тулд сайн дураар бүтээв.**  
> **Хүн бүхэнд нээлттэй** — Энэ бүтээлээс хэн ч мөнгө олдоггүй, хэнээс ч төлбөр шаарддаггүй. Зөвхөн Монголчуудынхаа дижитал бичиглэлийг хөнгөвчлөхөд зориулан зохиогч хувийн чөлөөт цагаараа бэлтгэсэн нээлттэй бүтээл юм.

> **"Монгол хэлээр бичих нь хэзээ ч адармаатай, удаан байх ёсгүй."**  
> Дэлхий даяарх бүх монголчууд, гадаад дахь диаспора, инженерүүд, програмистууд ямар ч комьпютер дээр (US QWERTY болон German QWERTZ товчлуурт) монгол кирилл болон худам монгол бичгээр хурдан, эргономик, алдаагүй бичих нэгдсэн гарын стандарт.

---

## 🗺️ Гарын Байршлын Зураглалууд (All Layers Illustrated)

### 1. Үндсэн үе (Base Layer — Бүх 35 крилл үсэг шууд байрлана)
> **Зарчим**: Ямар ч Option/AltGr дарах шаардлагагүй. `Q = ъ`, `W = ь`, `Y = е`, `[ = ө`, `] = ү`, `; = щ`, `' = ы`, `\ = й`, `` ` = ё `` шууд 1-р үе дээр байрлана.

![Mongolian Cyrillic Base Layer](docs/images/layout-cyrillic-normal.png)

### 2. Shift үе (Shift Layer — Том үсгүүд ба тусгай тэмдэгтүүд)
> Том үсгүүд (**`Ө, Ү, Ъ, Ь, Е, Щ, Ы, Й, Ё`**) болон туслах тэмдэгтүүд.

![Mongolian Cyrillic Shift Layer](docs/images/layout-cyrillic-shift.png)

### 3. AltGr / Option өргөтгөл үе (AltGr / Option Layer — Програмист & Албан тэмдэгтүүд)
> Баруун `Alt` (AltGr) эсвэл Mac-ийн `Option` товчлуураар кодын хаалтууд (**`[ ] { } \ | ; : ' "`**), Төгрөгийн тэмдэгт (**`₮`**), Евро (**`€`**), албан хашилт (**`« »`**), болон урт зураас (**`—`**) шууд гарна.

![Mongolian Cyrillic AltGr Layer](docs/images/layout-cyrillic-altgr.png)

### 4. Худам Монгол Бичиг (Classical Mongol Bichig — Bachka Phonetic Logic)
> Кирилл үсгийн байрлалтай 100% ижил логикоор Худам монгол бичгээр шивнэ: `[` = **ᠥ (Ö)**, `]` = **ᠦ (Ü)**, `E` = **ᠡ (E)**, `O` = **ᠣ (O)**, `U` = **ᠤ (U)**, `I` = **ᠢ (I)**, `A` = **ᠠ (A)**, `N` = **ᠨ (N)**, `Shift+N` = **ᠩ (Ag/Ng)**. Тоон товчлуурууд дээр монгол бичгийн сонгодог цифрүүд (᠐-᠙) шууд гарна. `Shift + Space` = **NNBSP** (`\u202F`).

![Classical Mongol Bichig Layout](docs/images/layout-bichig.png)

---

## ⌨️ Үсэг ба Тэмдэгтүүдийн Харьцуулсан Хүснэгт (Keymap Reference)

| Товчлуур | Үндсэн (Base) | Shift (Том үсэг) | AltGr / Option (3-р үе) | Тэмдэглэл |
|:---:|:---:|:---:|:---:|:---|
| `Q` | **ъ** | **Ъ** | `'` | Үндсэн давхарга дээр шууд |
| `W` | **ь** | **Ь** | `` ` `` | Үндсэн давхарга дээр шууд |
| `E` | **э** | **Э** | `€` | Евро тэмдэг |
| `R` | **р** | **Р** | `®` | Баталгаажсан |
| `T` | **т** | **Т** | **₮ (U+20AE)** | Төгрөг |
| `Y` | **е** | **Е** | `™` | **"е / Е" товч энд байна!** |
| `[` | **ө** | **Ө** | `[` | **Ө / Ө үндсэн товч дээр, [ нь AltGr** |
| `]` | **ү** | **Ү** | `]` | **Ү / Ү үндсэн товч дээр, ] нь AltGr** |
| `;` | **щ** | **Щ** | `:` | **Щ / Щ үндсэн товч дээр, : нь AltGr** |
| `'` | **ы** | **Ы** | `…` | **Ы / Ы үндсэн товч дээр, … нь AltGr** |
| `\` | **й** | **Й** | `\` | **Й / Й үндсэн товч дээр, \ нь AltGr** |
| `` ` `` | **ё** | **Ё** | `~` | **Ё / Ё үндсэн товч дээр** |
| `G` | **г** | **Г** | `{` | Нээх их хаалт |
| `K` | **к** | **К** | `}` | Хаах их хаалт |
| `D` | **д** | **Д** | `«` | Монгол нээх хашилт |
| `F` | **ф** | **Ф** | `»` | Монгол хаах хашилт |
| `4` | 4 | $ | **₮** | Төгрөг |
| `-` | - | _ | **—** | Em-dash урт зураас |
| `,` | **ч** | **Ч** | `,` | **Ч / Ч үндсэн товч дээр, Таслал нь AltGr** |
| `.` | **ю** | **Ю** | `.` | **Ю / Ю үндсэн товч дээр, Цэг нь AltGr** |
| `/` | **я** | **Я** | `?` | **Я / Я үндсэн товч дээр, Асуулт нь AltGr** |
| `Space` | Зай | Зай | `\u202F` | **NNBSP (Бичгийн нарийн зай)** |

---

## Суулгах Заавар (Installation Guides)

### 🐧 1. Linux (Ubuntu, Debian, Fedora, Arch)
Линукс систем дээр нэг тушаалаар **Хоёр гарыг (Кирилл ба Монгол бичиг)** хамтад нь системд суулгана:

```bash
cd linux
sudo ./install.sh
```

Суулгасны дараа та дараах хоёр гарыг шууд ашиглана:
1. **Үндсэн (Default)**: `Mongolian Cyrillic (Bachka)` — Бүх 35 үсэг үндсэн товч дээр (`Q=ъ, W=ь, Y=е, [=ө, ]=ү`)
2. **Монгол бичиг**: `Mongolian Script (Traditional)` — Bachka авианы дагуу (`[=ᠥ, ]=ᠦ, A=ᠠ, E=ᠡ...`)

* **Шууд шилжүүлэх (Terminal / X11)**:
  - `setxkbmap mn` (Монгол Кирилл)
  - `setxkbmap mn -variant bichig` (Худам Монгол бичиг)
* **График орчин (GNOME / Ubuntu / KDE)**:
  - `Settings` $\rightarrow$ `Keyboard` $\rightarrow$ `Input Sources` $\rightarrow$ `Add 'Mongolian'` нэмээд **`Super + Space`** (Win + Space)-ээр шилжинэ.
* **Буцааж анхны төлөвт оруулах**: `cd linux && sudo ./uninstall.sh`.

---

### 🍏 2. macOS (Apple OS X / macOS)
macOS-д зориулсан Apple албан ёсны стандартын `Mongolian.bundle` болон суулгагч:

* **Виртуал дискээр суулгах (.dmg — Drag & Drop хамгийн хялбар арга)**:
  1. `Mongolian-Keyboard-macOS-v1.0.3.dmg` файлыг давхар товшиж нээнэ.
  2. Цонхон доторх **`Keyboard Installer.app`**-ийг нээгээд **`Mongolian.bundle`**-ийг цонх руу нь чирж тавина.
  3. *(Гараар суулгах бол)*: Finder нээгээд **Cmd + Shift + G** даран `~/Library/Keyboard Layouts` орж `Mongolian.bundle` эсвэл `MongolianCyrillicErgonomic.keylayout` файлыг хуулна.
  4. **ЧУХАЛ: Системээс заавал нэг удаа Log Out хийж дахин нэвтэрнэ (эсвэл компьютерээ Restart хийнэ)**. Учир нь macOS нь шинэ гарын драйверийг зөвхөн хэрэглэгч системд нэвтрэх үед санах ойд ачаалдаг.
* **macOS дээр шинэ гараа идэвхжүүлэх**:
  1. `System Settings` $\rightarrow$ `Keyboard` $\rightarrow$ `Text Input` (Input Sources) $\rightarrow$ `Edit...` (эсвэл `+`) товшино.
  2. `Mongolian` хэсгээс **`Mongolian Cyrillic Ergonomic (Tsengel)`**-ийг сонгож `Add` дарна.
  3. Мөн уг багцад `Mongolian (qwerty)` болон `Mongolian (traditional)` (Худам монгол бичиг) багтсан.

---

### 🪟 3. Windows (Windows 7 / 10 / 11)

#### А. Бие даасан бүрэн суулгагч (Single All-in-One Installer - Зөвлөмж болгох)
* **[Mongolian-Keyboard-Windows-Setup-v1.0.3.exe](https://mn.tsengel.de/downloads/Mongolian-Keyboard-Windows-Setup-v1.0.3.exe)** файлыг татаж аваад ажиллуулна.
* Суулгах явцдаа өөрийн гарны төрөл (US QWERTY эсвэл German QWERTZ) болон Монгол бичгийн TrueType фонтуудыг сонгон нэг товшилтоор суулгана.
* Суусны дараа `Win + Space` дараад шууд Монгол гарыг сонгон бичнэ.

#### Б. PowerShell скрипт эсвэл MSI эх сан
* Хэрэв консолоор суулгахыг хүсвэл:
  ```powershell
  cd windows
  .\install.ps1 -Base us    # Англи суурьтай Windows гар
  .\install.ps1 -Base de    # Герман суурьтай Windows гар
  ```
* Мөн [windows/Mongolian-Ergonomic.klc](windows/Mongolian-Ergonomic.klc) эх файлыг [Microsoft Keyboard Layout Creator (MSKLC)](https://www.microsoft.com/en-us/download/details.aspx?id=102134) программд нээж хүссэнээрээ өөрчлөх боломжтой.

---

## Аюулгүй Байдлын Шалгалт (Cryptographic Integrity & SHA-256)

Бүх системийн суулгацын файлуудыг татаж авахдаа эх хувьтайгаа 100% тохирч, вирусгүй цэвэр болохыг дараах шалгах нийлбэрээр (SHA-256) баталгаажуулж болно:

```text
# 🪟 Windows (v1.0.3)
bf75103822f53bcd22e8bd7832743b16c6af9ea840e3dcc953604f04d0651ab0  Mongolian-Keyboard-Windows-Setup-v1.0.3.exe
3aeb1527f9b1b77ef6a0e6f74137be12ad974f88d891084f5bba100895b64f46  Mongolian-Keyboard-Windows-v1.0.3.zip

# 🍏 macOS (v1.0.3)
968a5019f5f3a5c563a842918b138a0a07f9f81df43bd94accf4e28194fcdbc3  Mongolian-Keyboard-macOS-v1.0.3.dmg
1ba0275e3dff0d96a9b74da437b83850bb65ca035a277d699e0154138e9fa177  Mongolian-Keyboard-macOS-v1.0.3.zip

# 🐧 Linux (v1.0.3)
784e3b695436c832d0475b16d08475a9b7568fd80b6cac653a95936dd341cb4e  Mongolian-Keyboard-Linux-v1.0.3.zip
dd0abeaab27594f7555d2e7812f80376a4e56f0d1e8a2be65b2f24e70eade16d  install-linux.sh
```

---

## 🌐 Вэб Туршигч (Interactive Web Visualizer)
Та юу ч суулгахгүйгээр хөтөч дээрээ шууд гарын тохиргоог туршиж, DevOps кодчилол шалгаж үзэж болно:
* **Шууд турших (Live Web App):** [mn.tsengel.de](https://mn.tsengel.de) • [gar.tsengel.de](https://gar.tsengel.de) • [bichig.tsengel.de](https://bichig.tsengel.de)
* **Локалоор нээх:**
```bash
xdg-open web/index.html
```

---

## 📂 Төслийн Бүтэц (Repository Structure)

```
mn-keyboard-layout/
├── README.md               # Дэлгэрэнгүй баталгаажсан гарын авлага
├── LICENSE                 # MIT License
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
├── macos/                  # macOS Mongolian.bundle, .dmg ба эх файлууд
│   ├── Mongolian.bundle/   # Apple Native Keyboard Layout Bundle
│   ├── MongolianCyrillicErgonomic.keylayout
│   ├── MongolianCyrillicErgonomic.icns
│   ├── Mongolian.bundle/   # macOS албан ёсны гарын багц
│   ├── install.sh          # Terminal суулгагч
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

## Эх Сурвалж ба Талархал (Sources & Attribution)

Энэхүү 100% үнэ төлбөргүй, олон нийтийн нээлттэй бүтээл нь өмнөх үеийн нээлттэй эхийн шийдлүүд болон туршлага дээр тулгуурлан хөгжүүлэгдсэн:
* **bachka-keyboard ажлууд (Predecessor by Tsengel/Bachka)**:
  - [mongolian-keyboard-layout-linux](https://github.com/bachka/mongolian-keyboard-layout-linux) — Анхны Linux XKB layout суурь
  - [mongolian-kbl-english-kb](https://github.com/bachka/mongolian-kbl-english-kb) — Windows US QWERTY суулгац ба MSKLC эх код
  - [mongolian-kbl-german-kb](https://github.com/bachka/mongolian-kbl-german-kb) — Windows German QWERTZ суулгац ба MSKLC эх код
* **StudyMongolian.net (Study Mongolian)**:
  - [StudyMongolian.net](https://www.studymongolian.net/technical/mongolian-keyboard-for-macos/) — macOS-ийн орчин үеийн `Mongolian.bundle` архитектур, MacBook ANSI/JIS олон гарын дэмжлэг, болон худам монгол бичгийн байрлалын бүтэц.
* **SIL International**:
  - [SIL International / Ukelele](https://software.sil.org/ukelele/) — macOS Unicode гарын драйверын стандарт болон нэг товшилтоор суулгагч `Keyboard Installer.app` хэрэгсэл.
* **Dusal.net (Д. Дусал)**:
  - [Dusal.net](http://dusal.blogmn.net/99944/) — Худам монгол бичгийн `cmdashitseden.ttf` фонтын эх сурвалж.

---

## Санаачилгыг Дэмжих (Support & Contribution)

Энэ нь ямар нэг санхүүжилтгүй, зохиогчийн чөлөөт цагаараа нийтийн тусын тулд хөгжүүлж буй **100% үнэ төлбөргүй, ашгийн бус нээлттэй бүтээл** юм. Хэрэв энэхүү гарын байрлал таны ажил, амьдралд бодитой тус болж байгаа бол серверийн түрээс, домэйн болон дэд бүтцийн зардлыг хуваалцан дэмжих боломжтой:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Дэмжих-ff5e5b?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)

---

## Зохиогч & Нээлттэй Эрх (Author & License)

Энэхүү бүтээл нь дэлхий даяарх бүх монголчуудад үнэ төлбөргүй, нээлттэй [MIT License](LICENSE) эрхтэй.
* Санаачлагч ба зохиогч: **Цэнгэл (Tsengel / Bachka)** — [tsengel.de](https://tsengel.de) (мөн [blog.tsengel.de](https://blog.tsengel.de))
* Санал хүсэлт, сайжруулалтыг GitHub Issue болон Pull Request-ээр хүлээн авна.

*Монголын үрс маш олон болж, мэдлэгийг харамгүй хуваалцан хамтдаа хөгжих болтугай! 🇲🇳*
