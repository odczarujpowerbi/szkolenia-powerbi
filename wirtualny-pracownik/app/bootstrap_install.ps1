# Krok 1-2 bootstrapu (SKALOWANIE.md sekcja 4): przygotowanie systemu i
# instalacja zależności. Uruchamiane raz, ręcznie, na nowym komputerze
# Windows, jako administrator.
#
# UWAGA: ten skrypt NIE był testowany na prawdziwym Windows z tej sesji
# (środowisko budowy to Linux, bez dostępu do docelowej maszyny) — sprawdź
# krok po kroku przy pierwszym użyciu, zamiast ufać mu w ciemno.
#
# Użycie (PowerShell jako administrator):
#   .\bootstrap_install.ps1 -RepoUrl "https://github.com/<org>/<repo>.git"

param(
    [Parameter(Mandatory = $true)]
    [string]$RepoUrl,

    [string]$InstallPath = "C:\AIWorker",

    [switch]$SkipSystemChecks
)

$ErrorActionPreference = "Stop"

Write-Host "=== 1. Sprawdzenie systemu ===" -ForegroundColor Cyan

if (-not $SkipSystemChecks) {
    $ram_gb = [math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 1)
    Write-Host "RAM: $ram_gb GB"
    if ($ram_gb -lt 16) {
        Write-Warning "RAM poniżej zalecanego minimum 16 GB (dokumentacja bazowa rozdz. 4.1). Kontynuuję, ale odnotuj to."
    }

    # Wyłączenie uśpienia/hibernacji — dedykowany komputer ma działać 24/7.
    powercfg /change standby-timeout-ac 0
    powercfg /change hibernate-timeout-ac 0
    Write-Host "Uśpienie i hibernacja wyłączone (zasilanie z sieci)."
}

Write-Host "=== 2. Instalacja zależności ===" -ForegroundColor Cyan

function Test-CommandExists($name) {
    return $null -ne (Get-Command $name -ErrorAction SilentlyContinue)
}

if (-not (Test-CommandExists "git")) {
    Write-Error "Git nie jest zainstalowany. Zainstaluj z https://git-scm.com/download/win i uruchom ten skrypt ponownie."
    exit 1
}

if (-not (Test-CommandExists "python")) {
    Write-Error "Python nie jest zainstalowany. Zainstaluj Python 3.11+ z https://www.python.org/downloads/windows/ (zaznacz 'Add to PATH') i uruchom ten skrypt ponownie."
    exit 1
}

Write-Host "Git i Python znalezione."

Write-Host "=== 3. Klonowanie rdzenia (kod, ten sam dla każdego wdrożenia) ===" -ForegroundColor Cyan

$appPath = Join-Path $InstallPath "app"
if (Test-Path $appPath) {
    Write-Warning "$appPath już istnieje — pomijam klonowanie. Usuń ręcznie, jeśli chcesz świeżą kopię."
} else {
    New-Item -ItemType Directory -Path $InstallPath -Force | Out-Null
    git clone $RepoUrl $InstallPath
}

Write-Host "=== 4. Instalacja zależności Python ===" -ForegroundColor Cyan
Push-Location (Join-Path $InstallPath "wirtualny-pracownik\app")
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Pop-Location

Write-Host "`n=== Gotowe ===" -ForegroundColor Green
Write-Host "Dalsze kroki (SKALOWANIE.md sekcja 4, punkty 3-9):"
Write-Host "  1. Utwórz dedykowane konto standardowe dla bota (osobne od administratora)."
Write-Host "  2. Ustaw zmienne środowiskowe: ANTHROPIC_API_KEY, PROJECTLY_API_KEY, PROJECTLY_BASE_URL."
Write-Host "  3. Uruchom: python bootstrap_register.py <rola>"
Write-Host "  4. Uruchom: python bootstrap_smoke_test.py"
Write-Host "  5. Zarejestruj runner_loop.py w Harmonogramie zadań Windows (uruchamianie przy starcie systemu)."
