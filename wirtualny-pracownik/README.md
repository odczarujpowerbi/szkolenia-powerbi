# Wirtualny pracownik AI

Wirtualny pracownik działający niezależnie od laptopów zespołu: cyklicznie pobiera zadania, uruchamia skrypty, obsługuje aplikacje webowe i desktopowe (w tym Power BI), waliduje wyniki i zostawia pełny ślad audytowy.

> **Status:** folder tymczasowy w repo `szkolenia-powerbi` — docelowo projekt zostanie przeniesiony do osobnego repozytorium (`odczarujpowerbi/wirtualny-pracownik`), gdy integracja GitHub uzyska uprawnienia do tworzenia nowych repozytoriów.
>
> Pełna dokumentacja koncepcyjna (biznesowa i techniczna, v1.0, 6 sierpnia 2026): `Wirtualny_Pracownik_AI_Dokumentacja_Biznesowa_i_Techniczna.pdf` (przekazana przez właściciela projektu, nie dołączona do repo).

## Rekomendacja: pilotaż najpierw

Rozpocząć od 2–4 tygodniowego pilotażu na jednym, używanym komputerze z Windows, zamiast budować od razu pełną platformę. Dopiero po potwierdzeniu powtarzalności rozdzielać system na wyspecjalizowane workery i nadawać szersze uprawnienia.

## Stack (wersja podstawowa – pilotaż)

- **System:** Windows 11 Pro, stały dostęp do zasilania i internetu, dedykowany komputer (nie do codziennej pracy).
- **Runner / AI:** Python + Harmonogram zadań Windows; Anthropic API jako główna pętla agenta (limit pilotażowy 20 USD), OpenRouter jako fallback modeli.
- **Wykonanie zadań:** PowerShell 7, Git, Power BI Desktop (PBIP/PBIR/TMDL) + Desktop Bridge, Playwright + automatyzacja Windows UI.
- **Kolejka zadań:** foldery OneDrive/SharePoint + pliki JSON (01_Inbox → 02_Queued → 03_Running → 04_Needs_Approval → 05_Completed/06_Failed).
- **Audyt:** `status.json`, `events.jsonl`, screenshoty, logi stdout/stderr, `costs.json`, raport końcowy — osobny folder per zadanie (`TASK-000142\...`).
- **Zdalny dostęp:** Tailscale + Pulpit zdalny (bez publikowania RDP do internetu).
- **Powiadomienia:** webhook Discord (start, błąd, oczekiwanie na decyzję, zakończenie).
- **Repozytoria:** kod i PBIP wersjonowane w GitHubie, poza folderem synchronizowanym przez OneDrive; agent nie zapisuje bezpośrednio do `main` — zawsze branch + pull request do akceptacji.

## Kluczowe zasady

- AI planuje, interpretuje i ocenia rezultat; skrypty i dedykowane narzędzia wykonują powtarzalne czynności. Klikanie po ekranie dopiero, gdy brak stabilnego API/CLI.
- Hierarchia metod wykonania: **1. API/MCP → 2. pliki/CLI/skrypt → 3. automatyzacja UI → 4. computer use (screenshoty)**.
- Zasada fail closed: przy niepewności co do aplikacji/konta/rezultatu agent nie wykonuje działania nieodwracalnego — zapisuje stan i prosi o decyzję.
- Klasyfikacja działań: **zielone** (odczyt, automatycznie) / **żółte** (zmiana, automatycznie w granicach polityki) / **czerwone** (publikacja, budżet, dane — wymaga jawnej akceptacji człowieka).
- Sekrety nigdy w repo/logach/screenshotach; maskowanie pól password/token/api_key/authorization/cookie.

## Pierwsze procesy pilotażowe

| ID | Proces | Autonomia |
|---|---|---|
| PBI-01 | Walidacja istniejącego PBIP (screenshoty stron, lista błędów, raport) | Odczyt – automatyczny |
| PBI-02 | Bezpieczna korekta raportu (gałąź, test, PR) | Zmiana – akceptacja przed merge |
| WEB-01 | Kontrola jednej aplikacji webowej (Playwright) | Odczyt – automatyczny |
| SCRIPT-01 | Uruchomienie skryptu cyklicznego | Automatyczny |
| OPS-01 | PAUSE / RESUME / przejęcie zdalne | Człowiek w pętli |

## TODO

- [ ] Wybrać konkretny komputer (min. 4 rdzenie/16 GB RAM, docelowo 32 GB przy Power BI + przeglądarka równolegle)
- [ ] Wybrać 3 pierwsze procesy o najwyższej wartości i niskim ryzyku
- [ ] Skonfigurować katalogi `C:\AIWorker\` (app/repos/workspace/runs/cache/logs/secrets) i strukturę OneDrive `AI Worker\`
- [ ] Ustalić repo GitHub i workspace Power BI jako sandbox pilotażu
- [ ] Skonfigurować Anthropic API (limit 20 USD) + OpenRouter jako fallback
- [ ] Zaimplementować runner (task.json → status.json → events.jsonl → Discord)
- [ ] Przetestować PAUSE/RESUME i wznowienie po restarcie
- [ ] Po potwierdzeniu kryteriów odbioru: przenieść folder do docelowego repozytorium `odczarujpowerbi/wirtualny-pracownik`
