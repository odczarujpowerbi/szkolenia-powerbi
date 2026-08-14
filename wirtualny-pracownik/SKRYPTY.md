# Katalog skryptów Python — Wirtualny Pracownik AI

Pomysły na skrypty pogrupowane wg domeny. Każdy skrypt ma jasno określony cel, wyzwalacz i poziom ryzyka (zielone/żółte/czerwone wg `PLAN-WDROZENIA.md`). To jest lista robocza do rozbicia na zadania implementacyjne — nie gotowy kod.

## A. Core / orkiestracja

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `runner_loop.py` | Główna pętla: pobiera zadania, kolejkuje, uruchamia workery, aktualizuje stan | Usługa ciągła / Harmonogram zadań Windows | infra |
| `task_router.py` | Klasyfikuje zadanie z Projectly na typ i wymagany worker (Power BI / CRM / Ads / pliki / mail / dev) | Po pobraniu zadania | infra |
| `state_store.py` | Trzyma stan zadania (SQLite/JSON) niezależnie od modelu AI — pozwala wznowić po restarcie | Każda zmiana stanu | infra |
| `heartbeat.py` | Zapisuje `heartbeat.json` co 30-60s | Cyklicznie w tle | infra |
| `watchdog.py` | Wykrywa brak heartbeat, restartuje runner lub eskaluje do Projectly | Cyklicznie, niezależny proces | infra |

## B. Projectly (komunikacja i zadania)

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `projectly_poller.py` | Odpytuje API/MCP Projectly o nowe/przypisane zadania i komentarze-decyzje | Cyklicznie (np. co 30-60s) | infra |
| `projectly_reporter.py` | Dopisuje komentarz z podsumowaniem wg szablonu z planu wdrożenia | Po zakończeniu każdego zadania | zielone |
| `projectly_self_review.py` | LLM-judge: porównuje rezultat z `acceptance_criteria` zadania, ocenia pass/fail, dopisuje ocenę | Przed poproszeniem o akceptację | zielone |
| `projectly_status_sync.py` | Mapuje wewnętrzny status runnera na status zadania w Projectly | Przy każdej zmianie stanu | infra |
| `projectly_decision_parser.py` | Parsuje odpowiedź człowieka (komentarz/status) na `approve`/`reject`/`changes_requested` | Po wykryciu nowego komentarza na eskalowanym zadaniu | infra |

## C. Walidacja i auto-zatwierdzanie (priorytet — rozwiązuje problem z czasem admina)

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `risk_classifier.py` | Klasyfikuje planowaną akcję jako zielona/żółta/czerwona wg `approval_policy.yaml` | Przed wykonaniem każdej akcji | infra |
| `approval_policy.yaml` + `policy_loader.py` | Deklaratywne reguły ryzyka i progów auto-akceptacji, edytowalne bez zmiany kodu | Wczytywane przy starcie runnera | infra |
| `validator_pool.py` | Uruchamia równolegle N niezależnych walidatorów dla żółtej akcji i zbiera głosy | Po wykonaniu żółtej akcji, przed zatwierdzeniem | infra |
| `validator_technical.py` | Walidator: testy techniczne/skrypt sprawdzający (kod wyjścia, dane kontrolne) | Wywoływany przez `validator_pool.py` | infra |
| `validator_visual.py` (`vision_reviewer.py`) | Walidator: ocena zrzutu ekranu przez model AI (czy wygląda poprawnie, brak błędów wizualnych) | Wywoływany przez `validator_pool.py` | infra |
| `validator_scope.py` | Walidator: czy akcja mieści się w zadeklarowanym zakresie zadania i limicie kosztu | Wywoływany przez `validator_pool.py` | infra |
| `auto_approve_yellow.py` | Jeśli głosy walidatorów ≥ próg z polityki — auto-zatwierdza, loguje kto/co zatwierdziło | Po zebraniu głosów z `validator_pool.py` | żółte |
| `escalate_to_human.py` | Dla czerwonych i spornych żółtych: tworzy w Projectly osobne zadanie przypisane człowiekowi (nie tylko komentarz) — z kontekstem, uzasadnieniem i linkami do screenshotów/diffów (patrz PLAN-WDROZENIA.md sekcja 4) | Gdy akcja czerwona lub walidatory bez zgody | infra |
| `human_response_validator.py` | Sprawdza, czy komentarz człowieka na eskalowanym zadaniu faktycznie rozstrzyga sprawę (jednoznaczna decyzja/wartość), czy trzeba dopytać | Po nowym komentarzu na zadaniu-eskalacji | infra |
| `continuation_task_creator.py` | Po pozytywnej weryfikacji odpowiedzi człowieka — tworzy w Projectly nowe zadanie-kontynuację dla agenta z decyzją człowieka wbudowaną w kontekst | Po `human_response_validator.py` (wynik: wystarczające) | infra |

## D. Screenshoty i weryfikacja wizualna

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `screenshot_capture.py` | Uniwersalny zrzut (pełny ekran / okno / element), wspólny dla wszystkich workerów | Wywoływany przez workery Power BI/Ads/CRM | zielone |
| `screenshot_diff.py` | Porównanie ze zrzutem bazowym (perceptual diff), oznacza odchylenia | Po każdej zmianie wizualnej | zielone |
| `screenshot_annotate.py` | Nakłada opis/znaczniki błędów na zrzut do raportu końcowego | Przed dołączeniem do raportu | zielone |

## E. Power BI

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `pbip_validate.py` | Otwiera PBIP, uruchamia walidację schematów PBIR/TMDL, generuje raport (PBI-01) | Zadanie typu `powerbi_validation` | zielone |
| `pbip_screenshot_all_pages.py` | Przez Desktop Bridge robi zrzuty wszystkich stron raportu | Część `pbip_validate.py` | zielone |
| `pbip_edit_tmdl.py` | Kontrolowana edycja modelu/miar (TMDL) na osobnej gałęzi (PBI-02) | Zadanie typu `powerbi_fix` | żółte |
| `pbi_service_check.py` | REST API: status odświeżenia, dostęp, workspace | Zadanie cykliczne / na żądanie | zielone |

## F. CRM (przez MCP)

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `crm_sync_task.py` | Odczyt/zapis rekordów CRM powiązanych z zadaniem (np. status leada) | Zadanie typu `crm_update` | żółte (odczyt: zielone) |
| `crm_report_generator.py` | Generuje podsumowania na podstawie zapytań CRM (np. COQL) do wykorzystania w innych zadaniach | Zadanie cykliczne / na żądanie | zielone |

## G. Meta Ads

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `meta_ads_api_client.py` | Odczyt kampanii i kontrolowane zmiany przez Marketing API w granicach limitu | Zadanie typu `ads_check` / `ads_adjust` | żółte (budżet: **czerwone**) |
| `meta_ads_ui_fallback.py` | Playwright dla funkcji niedostępnych w API — stan kampanii, zrzut, weryfikacja | Gdy API nie pokrywa potrzeby | żółte |

## H. E-mail i inny agent (przez MCP)

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `mcp_email_agent_bridge.py` | Łączy się przez MCP z dedykowanym agentem mailowym, przekazuje kontekst i prosi o draft | Zadanie typu `email_draft` | żółte |
| `email_draft_reviewer.py` | Walidator treści/odbiorcy/załączników przed przekazaniem do wysyłki | Przed wysyłką | infra (blokuje do czerwonej akceptacji) |

## I. Google Workspace i SharePoint

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `google_docs_writer.py` | Tworzy/aktualizuje pliki Google Docs/Sheets przez API | Zadanie typu `google_file` | żółte |
| `sharepoint_sync.py` | Microsoft Graph: upload/aktualizacja plików i folderów, archiwizacja artefaktów | Po zakończeniu każdego zadania z artefaktami | zielone |

## J. Skille i samodoskonalenie

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `skill_registry.py` | Rejestr dostępnych skilli/narzędzi z metadanymi (opis, ryzyko, kontrakt wejścia/wyjścia) | Wczytywany przez plannera przy starcie | infra |
| `skill_usage_logger.py` | Loguje użycie skilli/skryptów i skutek (sukces/porażka/czas/koszt) | Po każdym użyciu skilla | zielone |
| `skill_improver_bot.py` | Cyklicznie analizuje logi z `skill_usage_logger.py`, proponuje poprawki do skilli/promptów, tworzy PR z propozycją (nie wdraża sam) | Harmonogram, np. raz w tygodniu | żółte (PR), nie merge |

## K. Monitoring, koszty, bezpieczeństwo

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `cost_tracker.py` | Sumuje koszt AI per zadanie/dzień, alarm po przekroczeniu limitu | Po każdym wywołaniu modelu | infra |
| `secret_scanner.py` | Skanuje logi/artefakty pod kątem sekretów przed zapisem/synchronizacją | Przed `sharepoint_sync.py` / commitem | infra |

## L. Asystent zadań ludzkich (proactive assist — patrz PLAN-WDROZENIA.md sekcja 5)

| Skrypt | Cel | Wyzwalacz | Ryzyko |
|---|---|---|---|
| `human_task_scanner.py` | Cyklicznie przegląda zadania przypisane ludziom (nie tylko agentowi) w Projectly i klasyfikuje, gdzie agent może pomóc | Harmonogram, np. co godzinę | zielone |
| `human_task_partial_executor.py` | Wykonuje automatyzowalną część zadania człowieka, dopisuje komentarz "zrobiłem X, zostaje Ci Y" | Gdy `human_task_scanner.py` znajdzie automatyzowalną część | żółte (jak natywne ryzyko wykonanej czynności) |
| `human_task_briefing.py` | Przygotowuje opracowanie/research/draft ułatwiające człowiekowi wykonanie w pełni ludzkiego zadania, dołącza jako komentarz/załącznik | Gdy zadanie wymaga researchu, ale decyzję/wykonanie musi podjąć człowiek | zielone |
