# Szkielet Fazy 0-2 — działający, przetestowany kod

To nie jest pseudokod ani dokumentacja — to realny, uruchomiony i przetestowany szkielet: fundament (Faza 0), pętla end-to-end (Faza 1), silnik walidacji i obieg eskalacji (Fazy 2-2b), plus struktura walidacji PBIP (Faza 3, bez zrzutów ekranu — patrz niżej) i bootstrap nowego komputera (`SKALOWANIE.md`).

## Co realnie działa i jest przetestowane

| Moduł | Co robi | Test |
|---|---|---|
| `state_store.py` | Stan zadań + historia zdarzeń w SQLite, przeżywa restart | ✅ |
| `heartbeat.py` / `watchdog.py` | Zapis i wykrywanie nieaktualnego heartbeatu | ✅ |
| `kill_switch.py` | Globalny STOP.flag, blokuje runner bez podejmowania akcji | ✅ |
| `risk_classifier.py` | Klasyfikacja zielone/żółte/czerwone z `approval_policy.yaml`, fail-closed dla nieznanych akcji | ✅ |
| `task_router.py` | Routing po słowach kluczowych z `clients_routing.yaml`, niska pewność → `unassigned_pool` | ✅ |
| `validators.py` + `validator_pool.py` | 3 walidatory równolegle (technical/scope/visual), próg zgody z polityki | ✅ |
| `validators.py::_call_vision_model` | Realne wywołanie modelu wizyjnego (pakiet `anthropic`) przy podanym zrzucie i kluczu | ⚠️ napisane i gałęzie bez klucza przetestowane; sama rozmowa z modelem nietestowana — brak klucza w tej sesji |
| `escalation.py` | Tworzy zadanie dla człowieka (nie tylko komentarz), sprawdza jednoznaczność odpowiedzi, tworzy kontynuację | ✅ |
| `bounded_red_executor.py` | Sprawdza granicę liczbową bounded red — bez wpisu w polityce zawsze odmawia (bezpieczny domyślny stan) | ✅ |
| `cost_tracker.py` | Sumuje koszt dzienny, wyzwala kill switch po przekroczeniu limitu | ✅ |
| `secret_scanner.py` | Maskuje sekrety wg wzorca pola i kształtu klucza | ✅ |
| `live_status_publisher.py` | Buduje i publikuje status na żywo (kolejka, koszt, zdrowie) | ✅ |
| `skill_registry.py` / `skill_usage_logger.py` | Rejestr skilli z wersją, log użycia | ✅ |
| `pbip_validate.py` | Waliduje strukturę PBIP (JSON, TMDL) bez Power BI Desktop | ✅ (na syntetycznym przykładzie w `mock_data/sample_pbip/`) |
| `validator_prompt.py` | Wykrywa próby wstrzyknięcia instrukcji w treści zewnętrznej (heurystyka regex + opcjonalnie lokalny model przez Ollamę) — sprawdzane PRZED klasyfikacją, wykrycie zawsze eskaluje | ✅ heurystyka; opcjonalny lokalny model gracefully pomijany, gdy niedostępny |
| `runner_loop.py` | Spina wszystko: klasyfikacja → routing → walidacja/eskalacja → status → koszt | ✅ (`python runner_loop.py`) |
| `bootstrap_register.py` / `bootstrap_smoke_test.py` | Rejestracja roli i test dymny nowego komputera | ✅ |
| `bootstrap_install.ps1` | Przygotowanie systemu Windows i klon repo | ⚠️ napisany wg specyfikacji, **nie testowany na prawdziwym Windows** z tej sesji |

## Czego celowo brakuje (uczciwie, nie udawane)

- **Prawdziwe połączenie z Projectly** (`projectly_client.py`) — endpointy/autoryzacja nie są znane z tej sesji. Domyślnie `MockProjectlyClient` (czyta/pisze pliki w `mock_data/` i `runs/`). Ustaw `PROJECTLY_API_KEY` + `PROJECTLY_BASE_URL`, dopisz metody `ProjectlyClient`.
- **Realne wywołanie modelu w `validator_visual.py`** — kod jest napisany i wywoła prawdziwy model, jeśli podasz `ANTHROPIC_API_KEY` i zrzut ekranu; bez nich zwraca `approved=False` z jasnym wyjaśnieniem, zgodnie z fail-closed. Sama rozmowa z modelem nietestowana z tej sesji (brak klucza) — zweryfikuj na docelowej maszynie z prawdziwym zrzutem.
- **Prawdziwe workery** (Power BI Desktop Bridge + zrzuty, CRM, Meta Ads, SharePoint...) — `runner_loop.py` dziś tylko klasyfikuje i komentuje (`execution_result` to zaślepka), nie wykonuje realnej pracy w tych systemach. `pbip_validate.py` sprawdza tylko warstwę plikową — zrzuty stron wymagają Desktop Bridge na prawdziwym Windows z Power BI Desktop.
- **`bootstrap_install.ps1`** — napisany wiernie wg `SKALOWANIE.md`, ale nieprzetestowany (środowisko budowy to Linux bez dostępu do docelowego Windows). Sprawdź krok po kroku przy pierwszym użyciu.

## Jak uruchomić lokalnie (Python 3.9+, zero kluczy API na start)

```bash
pip install -r requirements.txt
cp .env.example .env   # uzupełnij prawdziwe klucze, gdy będą znane — .env jest w .gitignore
python runner_loop.py                     # jeden przebieg na mock_data/sample_tasks.json
python runner_loop.py --loop               # ciągła pętla co 30s (Ctrl+C żeby zatrzymać)
python bootstrap_smoke_test.py             # pełny test dymny (cykl + heartbeat + kill switch)
python bootstrap_register.py dev           # rejestracja roli
python pbip_validate.py mock_data/sample_pbip   # walidacja przykładowego PBIP
```

Stan w `runs/state.db`, heartbeat w `runs/heartbeat.json` — folder `runs/` jest w `.gitignore` (stan lokalny, nie kod — `SKALOWANIE.md` sekcja 2).

## Co jeszcze będzie potrzebne (pakiety i narzędzia wg fazy)

`requirements.txt` ma dziś tylko to, czego kod faktycznie używa (PyYAML, python-dotenv, anthropic). Reszta jest tam wypisana w komentarzu, żeby nie instalować pakietów, których jeszcze nic nie używa (ten sam problem co przedwczesny rozrost zakresu, tylko na poziomie zależności) — dodawaj je, gdy realnie piszesz danego workera:

| Faza / worker | Pakiety Python | Poza-pythonowe (system/konto) |
|---|---|---|
| Już teraz | PyYAML, python-dotenv, anthropic | — |
| Prawdziwe Projectly (`projectly_client.py`) | `requests` (albo SDK Projectly, jeśli istnieje) | Klucz API Projectly, dokumentacja endpointów |
| Power BI (Faza 3, zrzuty stron) | — (Bridge to nie pakiet pip) | **Power BI Desktop**, ewentualnie Tabular Editor/DAX Studio (opcjonalnie, do pracy nad modelem) |
| Screenshoty/diff (`screenshot_diff.py`) | `Pillow` | — |
| Przeglądarka (Meta Ads UI fallback, CRM UI) | `playwright` + `playwright install chromium` | — |
| Dane/raporty (`data_tidy.py`, `report_builder.py`, watcher schematu) | `pandas`, `openpyxl` | — |
| Google Workspace / Search Console / Analytics | `google-api-python-client`, `google-auth-oauthlib` | Konto serwisowe Google Cloud z odpowiednimi scope'ami |
| SharePoint / Microsoft Graph | `msal` | Rejestracja aplikacji w Azure AD (Microsoft Entra) |
| inFakt | `requests` | Dedykowane konto bota w inFakt, klucz API |
| Orkiestrator / Claude Code na docelowej maszynie | — (osobny CLI, nie pakiet pip) | Node.js (Claude Code jest dystrybuowany przez npm), klucz Anthropic API |
| Zdalny dostęp administracyjny | — | Tailscale (dokumentacja bazowa rozdz. 10.1) |

## Konfiguracja firmy — osobno od kodu

`config/approval_policy.yaml`, `config/clients_routing.yaml`, `config/skills_manifest.yaml`, `config/integrations.yaml` to "konfiguracja firmy" (`SKALOWANIE.md` sekcja 2) — edytowalne bez zmiany kodu, wymieniane przy kopiowaniu do innej firmy. `approval_policy.yaml` ma celowo **pustą** listę `bounded_red` — nie dodawaj tam nic, dopóki zwykły tryb czerwony nie przepracował na produkcji kilku tygodni (sekcja 3 planu).

`config/integrations.yaml` to jeden, konsolidowany rejestr wszystkich dostępnych kont/połączeń (Microsoft 365, Google, Zoho CRM, Projectly, zanfia.com, GitHub, OneDrive, Miro, MailerLite, TikTok Ads, lokalny model Hermes...) — mechanizm, poziom dostępu i uwagi, **nigdy klucze/tokeny** (te w lokalnym magazynie sekretów/`.env`).

**Ważne rozróżnienie: rejestracja w `integrations.yaml` ≠ istniejący konektor.** Dla większości nowych integracji jest dziś tylko wpis w tym pliku, nie ma jeszcze skryptu, który się z nimi łączy — `SKRYPTY.md` (kategorie F, H, I, O, P) oznacza je jawnie jako "nie napisany jeszcze": `zoho_crm_client.py`, `microsoft_graph_mail_client.py`, `google_workspace_client.py`, `mailerlite_client.py`, `zanfia_client.py`, `miro_read_client.py`. Do każdego z nich potrzebny będzie też **skill** (wiedza jak dobrze z tego korzystać, nie tylko hydraulika) — planowane skille wypisane w `config/skills_manifest.yaml` ze statusem `"planned"`.

## Instalacja na docelowym komputerze (Windows)

Pełna specyfikacja: `../SKALOWANIE.md` sekcja 4. Skrót:

```powershell
.\bootstrap_install.ps1 -RepoUrl "https://github.com/<org>/<repo>.git"
# ustaw zmienne środowiskowe (patrz .env.example)
python bootstrap_register.py dev
python bootstrap_smoke_test.py
```

## Następny krok

Ten kod jest gotowy, żeby lokalny Claude Code (albo inny agent) na docelowym komputerze go przejął i dokończył: podłączył prawdziwe Projectly i klucze, dodał realne wywołanie modelu w `validator_visual.py`, i pierwszy prawdziwy worker (najlepiej dalsza część PBI-01 — zrzuty stron przez Desktop Bridge, skoro walidacja struktury już działa).
