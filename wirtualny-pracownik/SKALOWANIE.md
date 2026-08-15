# Skalowanie i przenośność — inne komputery, inne firmy

`ZESPOL-BOTOW.md` opisuje wiele ról **wewnątrz jednej firmy**. Ten dokument opisuje inną oś: jak ten sam system łatwo skopiować na nowy komputer (lokalny lub zdalny) i, docelowo, na inną firmę — bez przepisywania kodu. Najtaniej wprowadzić te zasady **teraz**, przed napisaniem 67 skryptów z `SKRYPTY.md` z zaszytymi na sztywno założeniami — retrofit po fakcie byłby znacznie droższy.

## 1. Dobra wiadomość: koordynacja już jest chmurowa

Cała komunikacja między komponentami idzie przez Projectly, OneDrive i API zewnętrzne — żadna część architektury nie zakłada wspólnej sieci lokalnej. **Zdalny komputer działa bez przeróbek**, o ile ma dostęp do internetu i własne poświadczenia. To efekt uboczny wcześniejszych decyzji (Projectly jako jedyne źródło prawdy, OneDrive jako magazyn skilli), nie coś, co trzeba dodawać.

## 2. Rozdział: rdzeń (engine) vs konfiguracja firmy vs stan lokalny

Trzy warstwy, które muszą zostać rozdzielone fizycznie (osobne pliki/foldery), nie tylko pojęciowo:

| Warstwa | Co zawiera | Gdzie żyje | Czy różni się między firmami |
|---|---|---|---|
| Rdzeń (engine) | `runner_loop.py`, `risk_classifier.py`, `validator_pool.py`, cała reszta `SKRYPTY.md` — logika, nie dane | Jedno repo Git, wersjonowane | Nie — identyczny kod dla każdego wdrożenia |
| Konfiguracja firmy | `approval_policy.yaml`, mapowania klient→osoba/bot w `task_routing_classifier.py`, nazwy ról z `role_registry.py`, lista integracji i kluczy | Osobny plik/pakiet konfiguracyjny per firma | Tak — to jest to, co się wymienia przy kopiowaniu |
| Stan lokalny | `events.jsonl`, `state_store.py`, cache, logi, heartbeat | Na danym komputerze | Tak — zawsze lokalne, nigdy nie kopiowane między maszynami |

Dziś `task_routing_classifier.py` (PLAN-WDROZENIA.md sekcja 11) ma częściowo zaszyte na sztywno mapowania (INDEKA → Asia, Magnapharm → Kacper) — do przeniesienia do pliku konfiguracyjnego (`clients_routing.yaml` czy podobny) przed pierwszym wdrożeniem u innej firmy.

## 3. Jedna izolowana instancja na firmę — nie multi-tenant w jednym środowisku

Kuszące jest zbudowanie jednego wspólnego systemu obsługującego wiele firm naraz. **Odradzane wprost** — głównie z powodu RODO (`PRZED-PILOTAZEM.md` punkt o zgodności prawnej): dane klienta A nie mogą dzielić audytu/kontekstu z klientem B. Zamiast tego:

- Ten sam kod (rdzeń), **osobna instancja per firma**: osobny workspace Projectly, osobne klucze API, osobny folder skilli na OneDrive, osobny `cost_tracker.py` i `kill_switch.py`.
- To też prostszy model, gdyby to kiedyś stało się usługą sprzedawaną dalej (Clickless robi to już dla klientów w innym kontekście) — "każdy klient dostaje swoją instancję", nie dzielony system z ryzykiem przecieku między klientami.

## 4. Bootstrap nowego komputera

Dziś dołączenie nowego komputera-pracownika to nieopisany, ręczny proces. Potrzebny jeden powtarzalny skrypt/checklist:

1. Nowy komputer uruchamia skrypt instalacyjny — pobiera rdzeń z Git, pakiet konfiguracji firmy, klucze z bezpiecznego źródła.
2. Rejestruje się w `role_registry.py` (jaka rola: dev/marketing/admin/inne) i w Projectly.
3. Uruchamia `skill_sync_puller.py` (`ZESPOL-BOTOW.md` sekcja 4) — pobiera skille pasujące do swojej roli.
4. Startuje `runner_loop.py`, zapisuje pierwszy heartbeat.

Bez tego każde nowe stanowisko to ręczna, niepowtarzalna robota administracyjna — dokładnie ten sam problem co "prowizjonowanie dostępów" z `PRZED-PILOTAZEM.md`, tylko pomnożony przez liczbę komputerów.

## 5. Klucze API per wdrożenie, nie jeden globalny

Przy wielu komputerach i firmach jeden wspólny klucz API to: wąskie gardło (współdzielony limit), brak możliwości rozliczenia kosztu per klient, i większe ryzyko przy wycieku (jeden klucz kompromituje wszystko). Klucze API — minimum per firma, docelowo per rola — skalują się razem z flotą i pozwalają realnie mierzyć koszt per wdrożenie (`cost_tracker.py`).

## 6. Pakowanie skilli: kod generyczny + konfiguracja do wypełnienia

Żeby skill zbudowany dla jednej firmy (np. `pbip_validate.py`, `source_schema_watcher.py`) dało się przenieść do innej, paczka skilla dzieli się na:

- **Logikę** (uniwersalną — jak sprawdzić PBIP, jak wykryć zmianę schematu) — bez zmian między firmami.
- **Konfigurację** (mapowania klientów, ścieżki plików, progi ryzyka specyficzne dla tej firmy) — pusty szablon do wypełnienia przy wdrożeniu.

Dzięki temu biblioteka skilli (`SKRYPTY.md`) staje się realnym produktem/IP wielokrotnego użytku, nie kodem zrośniętym z jedną firmą.

## 7. Wersjonowanie floty

Gdy komputerów/firm przybędzie, `skill_registry.py` musi wiedzieć nie tylko "jakie skille są dostępne", ale **który komputer ma którą wersję którego skilla**. Bez tego częściowy rollout (jeden komputer ze starą wersją, drugi z nową) rozjedzie się po cichu — dopisać wersję skilla do heartbeatu/statusu, żeby było to widoczne w digestach i w trybie rozmowy (`PLAN-WDROZENIA.md` sekcja 14).

## Kiedy to robić

Punkty 1-2 (rozdział warstw, izolacja per firma) — **od razu, w Fazie 0**, bo zmiana tego po napisaniu kodu jest znacznie droższa niż zaprojektowanie tego od początku. Punkty 3-7 (bootstrap, klucze per wdrożenie, pakowanie skilli, wersjonowanie floty) — dopiero gdy realnie pojawi się drugi komputer albo druga firma, nie wcześniej. Budowanie pełnej automatyzacji instalacji dla floty, która jeszcze nie istnieje, byłoby dokładnie tym rodzajem przedwczesnego skalowania, przed którym ostrzegałem przy ocenie realności całego planu.
