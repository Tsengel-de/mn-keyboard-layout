; ==============================================================================
; Universal Mongolian Keyboard Layout Suite - Windows NSIS Installer
; Author: Tsengel (tsengel.de | tsengel@tsengel.de)
; License: MIT
; ==============================================================================

Unicode true
SetCompressor /SOLID lzma

!include "MUI2.nsh"
!include "x64.nsh"
!include "Sections.nsh"
!include "LogicLib.nsh"
!include "WinMessages.nsh"

; ------------------------------------------------------------------------------
; General Definitions
; ------------------------------------------------------------------------------
!define PRODUCT_NAME "Universal Mongolian Keyboard Layout Suite"
!define PRODUCT_NAME_SHORT "Mongolian Keyboard"
!define PRODUCT_VERSION "1.0.0"
!define PRODUCT_PUBLISHER "Tsengel (tsengel.de)"
!define PRODUCT_WEB_SITE "https://mn.tsengel.de"
!define REG_UNINSTALL "Software\Microsoft\Windows\CurrentVersion\Uninstall\MongolianKeyboardSuite"
!define REG_APP "Software\Tsengel\MongolianKeyboard"

Name "${PRODUCT_NAME}"
OutFile "../web/downloads/Mongolian-Keyboard-Windows-Setup.exe"
InstallDir "$PROGRAMFILES64\MongolianKeyboard"
InstallDirRegKey HKLM "${REG_APP}" "Install_Dir"
RequestExecutionLevel admin

; ------------------------------------------------------------------------------
; Interface Settings
; ------------------------------------------------------------------------------
!define MUI_ABORTWARNING
!define MUI_ICON "mongol.ico"
!define MUI_UNICON "mongol.ico"

; ------------------------------------------------------------------------------
; Pages
; ------------------------------------------------------------------------------
; Installer Pages
!define MUI_WELCOMEPAGE_TITLE "🇲🇳 ${PRODUCT_NAME}"
!define MUI_WELCOMEPAGE_TEXT "Энэхүү суулгагч нь Windows системд зориулсан Монгол гарын байрлал (Кирилл & Бичиг) болон шаардлагатай фонтуудыг автоматаар суулгана.$\r$\n$\r$\nЗохиогч: ${PRODUCT_PUBLISHER}$\r$\nВеб: ${PRODUCT_WEB_SITE}$\r$\n$\r$\nҮргэлжлүүлэхийн тулд 'Next' товчийг дарна уу."
!insertmacro MUI_PAGE_WELCOME

!insertmacro MUI_PAGE_LICENSE "../LICENSE"
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES

!define MUI_FINISHPAGE_TITLE "✅ Суулгалт амжилттай дууслаа!"
!define MUI_FINISHPAGE_TEXT "Монгол гарын байрлал таны компьютерт амжилттай суулаа.$\r$\n$\r$\nГарын байрлал хооронд шилжихдээ 'Win + Space' товчийг дарж Монгол гарыг сонгоно уу.$\r$\n$\r$\nКод бичихэд шаардлагатай { } [ ] \ | ~ зэрэг тэмдэгтүүдийг AltGr горимоор шууд бичих боломжтой."
!insertmacro MUI_PAGE_FINISH

; Uninstaller Pages
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

; Languages
!insertmacro MUI_LANGUAGE "English"

; ------------------------------------------------------------------------------
; Variables
; ------------------------------------------------------------------------------
Var RadioState

; ------------------------------------------------------------------------------
; Sections
; ------------------------------------------------------------------------------
Section "Монгол гар (АНУ / US QWERTY суурьтай)" SecUS
  DetailPrint "Extracting US QWERTY Keyboard Layout package..."
  InitPluginsDir
  SetOutPath "$PLUGINSDIR\us"
  File /r "us-qwerty\*.*"

  ${If} ${RunningX64}
    DetailPrint "Installing 64-bit Mongolian Keyboard Layout (US QWERTY)..."
    ExecWait '"$SYSDIR\msiexec.exe" /i "$PLUGINSDIR\us\Mongol_amd64.msi" /quiet /norestart' $0
  ${Else}
    DetailPrint "Installing 32-bit Mongolian Keyboard Layout (US QWERTY)..."
    ExecWait '"$SYSDIR\msiexec.exe" /i "$PLUGINSDIR\us\Mongol_i386.msi" /quiet /norestart' $0
  ${EndIf}

  DetailPrint "Installation result code: $0"
  WriteRegDWORD HKLM "${REG_APP}" "InstalledUS" 1
SectionEnd

Section /o "Монгол гар (Герман / DE QWERTZ суурьтай)" SecDE
  DetailPrint "Extracting DE QWERTZ Keyboard Layout package..."
  InitPluginsDir
  SetOutPath "$PLUGINSDIR\de"
  File /r "de-qwertz\*.*"

  ${If} ${RunningX64}
    DetailPrint "Installing 64-bit Mongolian Keyboard Layout (DE QWERTZ)..."
    ExecWait '"$SYSDIR\msiexec.exe" /i "$PLUGINSDIR\de\mongolis_amd64.msi" /quiet /norestart' $0
  ${Else}
    DetailPrint "Installing 32-bit Mongolian Keyboard Layout (DE QWERTZ)..."
    ExecWait '"$SYSDIR\msiexec.exe" /i "$PLUGINSDIR\de\mongolis_i386.msi" /quiet /norestart' $0
  ${EndIf}

  DetailPrint "Installation result code: $0"
  WriteRegDWORD HKLM "${REG_APP}" "InstalledDE" 1
SectionEnd

Section "Монгол бичгийн фонтууд (TrueType Fonts)" SecFonts
  DetailPrint "Installing Mongolian Script TrueType Fonts..."
  SetOutPath "$FONTS"
  File "fonts\cmdashitseden.ttf"
  File "fonts\MongolianScript.ttf"
  File "fonts\mnglartaat.ttf"
  File "fonts\mnglartotf.ttf"
  File "fonts\mngltitleaat.ttf"
  File "fonts\mngltitleotf.ttf"
  File "fonts\mnglwhiteaat.ttf"
  File "fonts\mnglwhiteotf.ttf"
  File "fonts\mnglwritingaat.ttf"
  File "fonts\mnglwritingotf.ttf"

  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "CM Dashitseden (TrueType)" "cmdashitseden.ttf"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "MongolianScript (TrueType)" "MongolianScript.ttf"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Art AAT (TrueType)" "mnglartaat.ttf"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Art OTF (TrueType)" "mnglartotf.ttf"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Title AAT (TrueType)" "mngltitleaat.ttf"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Title OTF (TrueType)" "mngltitleotf.ttf"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian White AAT (TrueType)" "mnglwhiteaat.ttf"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian White OTF (TrueType)" "mnglwhiteotf.ttf"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Writing AAT (TrueType)" "mnglwritingaat.ttf"
  WriteRegStr HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Writing OTF (TrueType)" "mnglwritingotf.ttf"

  SendMessage ${HWND_BROADCAST} ${WM_FONTCHANGE} 0 0 /TIMEOUT=2000
  WriteRegDWORD HKLM "${REG_APP}" "InstalledFonts" 1
SectionEnd

Section "-Post"
  SetOutPath "$INSTDIR"
  File "mongol.ico"

  WriteUninstaller "$INSTDIR\uninstall.exe"

  WriteRegStr HKLM "${REG_APP}" "Install_Dir" "$INSTDIR"
  WriteRegStr HKLM "${REG_UNINSTALL}" "DisplayName" "${PRODUCT_NAME}"
  WriteRegStr HKLM "${REG_UNINSTALL}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr HKLM "${REG_UNINSTALL}" "Publisher" "${PRODUCT_PUBLISHER}"
  WriteRegStr HKLM "${REG_UNINSTALL}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr HKLM "${REG_UNINSTALL}" "HelpLink" "https://github.com/Tsengel-de/mn-keyboard-layout"
  WriteRegStr HKLM "${REG_UNINSTALL}" "DisplayIcon" "$INSTDIR\mongol.ico"
  WriteRegStr HKLM "${REG_UNINSTALL}" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegStr HKLM "${REG_UNINSTALL}" "QuietUninstallString" '"$INSTDIR\uninstall.exe" /S'
  WriteRegDWORD HKLM "${REG_UNINSTALL}" "NoModify" 1
  WriteRegDWORD HKLM "${REG_UNINSTALL}" "NoRepair" 1
SectionEnd

; ------------------------------------------------------------------------------
; Descriptions
; ------------------------------------------------------------------------------
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SecUS} "АНУ / Олон улсын стандарт (US QWERTY) гарт зориулсан Монгол гарын байрлал (Q=Ө, W=Ү / AltGr тэмдэгтүүд)."
  !insertmacro MUI_DESCRIPTION_TEXT ${SecDE} "Герман стандарт (DE QWERTZ) гарт зориулсан Монгол гарын байрлал."
  !insertmacro MUI_DESCRIPTION_TEXT ${SecFonts} "Монгол бичгээр зөв унших, бичихэд шаардлагатай TrueType фонтууд."
!insertmacro MUI_FUNCTION_DESCRIPTION_END

; ------------------------------------------------------------------------------
; Callback Functions
; ------------------------------------------------------------------------------
Function .onInit
  StrCpy $RadioState ${SecUS}
FunctionEnd

Function .onSelChange
  !insertmacro StartRadioButtons $RadioState
    !insertmacro RadioButton ${SecUS}
    !insertmacro RadioButton ${SecDE}
  !insertmacro EndRadioButtons
FunctionEnd

; ------------------------------------------------------------------------------
; Uninstaller Section
; ------------------------------------------------------------------------------
Section "Uninstall"
  DetailPrint "Uninstalling Mongolian Keyboard Layout Suite..."

  ReadRegDWORD $0 HKLM "${REG_APP}" "InstalledUS"
  ${If} $0 == 1
    DetailPrint "Uninstalling US QWERTY Keyboard Layout MSI..."
    ExecWait '"$SYSDIR\msiexec.exe" /x {7F1B3916-A8A5-4716-8FCB-C3193E9DBAB3} /quiet /norestart'
  ${EndIf}

  ReadRegDWORD $0 HKLM "${REG_APP}" "InstalledDE"
  ${If} $0 == 1
    DetailPrint "Uninstalling DE QWERTZ Keyboard Layout MSI..."
    ExecWait '"$SYSDIR\msiexec.exe" /x {BEB1FF3B-994B-47F7-BB2C-77DAB9DF311C} /quiet /norestart'
  ${EndIf}

  ReadRegDWORD $0 HKLM "${REG_APP}" "InstalledFonts"
  ${If} $0 == 1
    DetailPrint "Removing TrueType Fonts..."
    DeleteRegValue HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "CM Dashitseden (TrueType)"
    DeleteRegValue HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "MongolianScript (TrueType)"
    DeleteRegValue HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Art AAT (TrueType)"
    DeleteRegValue HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Art OTF (TrueType)"
    DeleteRegValue HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Title AAT (TrueType)"
    DeleteRegValue HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Title OTF (TrueType)"
    DeleteRegValue HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian White AAT (TrueType)"
    DeleteRegValue HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian White OTF (TrueType)"
    DeleteRegValue HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Writing AAT (TrueType)"
    DeleteRegValue HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" "Mongolian Writing OTF (TrueType)"
    Delete "$FONTS\cmdashitseden.ttf"
    Delete "$FONTS\MongolianScript.ttf"
    Delete "$FONTS\mnglartaat.ttf"
    Delete "$FONTS\mnglartotf.ttf"
    Delete "$FONTS\mngltitleaat.ttf"
    Delete "$FONTS\mngltitleotf.ttf"
    Delete "$FONTS\mnglwhiteaat.ttf"
    Delete "$FONTS\mnglwhiteotf.ttf"
    Delete "$FONTS\mnglwritingaat.ttf"
    Delete "$FONTS\mnglwritingotf.ttf"
    SendMessage ${HWND_BROADCAST} ${WM_FONTCHANGE} 0 0 /TIMEOUT=2000
  ${EndIf}

  Delete "$INSTDIR\uninstall.exe"
  Delete "$INSTDIR\mongol.ico"
  RMDir "$INSTDIR"

  DeleteRegKey HKLM "${REG_UNINSTALL}"
  DeleteRegKey HKLM "${REG_APP}"
SectionEnd
