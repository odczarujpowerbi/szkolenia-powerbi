# Szkielet Fazy 0-1 — działający, przetestowany kod

To nie jest pseudokod ani dokumentacja — to realny, uruchomiony i przetestowany szkielet pętli runnera z `PLAN-WDROZENIA.md` (Faza 0: fundament, Faza 1: pętla end-to-end, Faza 2: pierwszy krok silnika walidacji — klasyfikacja ryzyka i routing już działają).

## Co realnie działa już teraz

- `runner_loop.py` — pobiera zadania (z mocka lub prawdziwego Projectly), klasyfikuje ryzyko (`risk_classifier.py`), rozdziela do właściciela (`task_router.py`), zapisuje stan i historię zdarzeń (`state_store.py`), pisze heartbeat, sprawdza kill switch.
- `watchdog.py` — wykrywa nieaktualny heartbeat.
- Kill switch — plik `runs/STOP.flag` zatrzymuje runner bez podejmowania akcji (PLAN-WDROZENIA.md sekcja 17).
- Klasyfikacja ryzyka i routing to **czysty Python bez AI** (sekcja 12) — deterministyczne, testowalne bez żadnego klucza API.

## Czego celowo brakuje (i dlaczego)

- **Prawdziwe połączenie z Projectly** (`projectly_client.py`) — endpointy/autoryzacja Projectly nie są znane z tej sesji. Domyślnie działa `MockProjectlyClient` (czyta `mock_data/sample_tasks.json`). Ustaw `PROJECTLY_API_KEY` w środowisku i dopisz metody `ProjectlyClient`, żeby przejść na prawdziwe dane.
- **`validator_pool.py` i sam model AI** — ten szkielet klasyfikuje ryzyko i pokazuje, co by się stało dalej, ale nie woła jeszcze żadnego modelu ani walidatorów wizualnych/technicznych. To następny krok Fazy 2.
- **Workery** (Power BI, CRM, Meta Ads...) — jeszcze nie podłączone. `runner_loop.py` dziś tylko klasyfikuje i komentuje, nie wykonuje realnej pracy w tych systemach.

## Jak uruchomić lokalnie (bez żadnych kluczy, na dowolnym Pythonie 3.9+)

```bash
pip install -r requirements.txt
python runner_loop.py            # jeden przebieg na mock_data/sample_tasks.json
python runner_loop.py --loop      # ciągła pętla co 30s (Ctrl+C żeby zatrzymać)
python watchdog.py                # sprawdza świeżość heartbeat.json
touch runs/STOP.flag && python runner_loop.py   # test kill switcha — runner nic nie robi
```

Stan zapisuje się w `runs/state.db` (SQLite), heartbeat w `runs/heartbeat.json` — folder `runs/` jest w `.gitignore`, bo to stan lokalny, nie kod (`SKALOWANIE.md` sekcja 2: rdzeń vs stan lokalny).

## Konfiguracja firmy — osobno od kodu

`config/approval_policy.yaml` i `config/clients_routing.yaml` to "konfiguracja firmy" w rozumieniu `SKALOWANIE.md` sekcja 2 — edytowalne bez zmiany kodu, to jest wymieniane przy kopiowaniu do innej firmy. `approval_policy.yaml` ma celowo **pustą** listę `bounded_red` — nie dodawaj tam nic, dopóki zwykły tryb czerwony nie przepracował na produkcji kilku tygodni (sekcja 3).

## Następny krok

Ten kod jest gotowy, żeby lokalny Claude Code (albo inny agent) na docelowym komputerze go przejął i dokończył: podłączył prawdziwe Projectly, dodał `validator_pool.py` z realnym wywołaniem modelu, i pierwszy worker (najlepiej PBI-01 — walidacja PBIP, zgodnie z priorytetem z `PLAN-WDROZENIA.md`).
