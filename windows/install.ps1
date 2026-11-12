# ==============================================================================
# Mongolian Keyboard Layout Suite - Windows PowerShell Installer
# Author: Tsengel (tsengel.de)
# ==============================================================================

[CmdletBinding()]
param (
    [ValidateSet("us", "de")]
    [string]$Base = "us"
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "🇲🇳 Mongolian Keyboard Layout Suite - Windows Installer" -ForegroundColor Cyan
Write-Host "Author: Tsengel (tsengel.de)" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

if ($Base -eq "de") {
    $TargetDir = Join-Path $ScriptDir "de-qwertz"
    $Installer = Join-Path $TargetDir "setup.exe"
    Write-Host "Selected Base: German (QWERTZ)" -ForegroundColor Yellow
} else {
    $TargetDir = Join-Path $ScriptDir "us-qwerty"
    $Installer = Join-Path $TargetDir "setup.exe"
    Write-Host "Selected Base: US English (QWERTY)" -ForegroundColor Yellow
}

if (-not (Test-Path $Installer)) {
    Write-Error "Installer not found at: $Installer"
    exit 1
}

Write-Host "`n1. Launching Windows Setup..." -ForegroundColor Green
Write-Host "   Path: $Installer"

try {
    Start-Process -FilePath $Installer -Wait
    Write-Host "`n✅ Installation completed!" -ForegroundColor Green
    Write-Host "----------------------------------------------------------"
    Write-Host "To switch layouts in Windows 10 / 11:"
    Write-Host "  Press: Win + Space"
    Write-Host "----------------------------------------------------------"
} catch {
    Write-Error "Setup failed with error: $_"
}

