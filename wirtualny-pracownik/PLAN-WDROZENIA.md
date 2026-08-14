# Plan wdrożenia i komunikacji — Wirtualny Pracownik AI (v2, Projectly-centric)

Ten plan rozwija dokumentację koncepcyjną (`Wirtualny_Pracownik_AI_Dokumentacja_Biznesowa_i_Techniczna.pdf`) o konkretne narzędzia, którymi realnie dysponujemy: **Projectly** (własna apka do zadań, API + MCP) jako główny kanał komunikacji, CRM przez MCP, Meta Ads (API + UI), Google Workspace, SharePoint, agent e-mailowy przez MCP, oraz bibliotekę skilli z botem, który sam je ulepsza.

Główny problem, który ten plan rozwiązuje: **administrator traci czas na ręczne zatwierdzanie każdego zadania.** Rozwiązaniem jest silnik walidacji z kilkoma niezależnymi walidatorami działającymi równolegle — administrator zatwierdza już tylko wyjątki (czerwone/sporne), nie każdą pojedynczą akcję.

## 1. Zasada nadrzędna: rezultat, nie instrukcja

Zadanie w Projectly opisuje **oczekiwany rezultat i kryteria akceptacji**, nie krok po kroku co robić. Planner AI sam dekomponuje zadanie na kroki, wybiera narzędzia i skrypty, wykonuje, a na końcu **sam ocenia własny wynik** względem kryteriów, zanim cokolwiek trafi do człowieka.

Minimalny kontrakt zadania (pole w Projectly lub JSON w treści/komentarzu):

```json
{
  "task_id": "PRJ-1042",
  "title": "Przygotuj raport sprzedaży Q3 w Power BI",
  "expected_result": "PBIP z zaktualizowanym modelem, 3 strony raportu, brak błędów walidacji",
  "acceptance_criteria": [
    "Model przechodzi walidację TMDL bez błędów krytycznych",
    "Każda strona ma zrzut ekranu bez elementów wychodzących poza obszar",
    "Dane zgadzają się z sumą kontrolną ze źródła"
  ],
  "risk_level_hint": "yellow",
  "max_ai_cost_usd": 3.0,
  "created_by": "pawel"
}
```

## 2. Komunikacja: Projectly jako jedyne źródło prawdy

- **Kanał główny i jedyny obowiązkowy:** komentarze na zadaniu w Projectly. Żadnego równoległego "prawdziwego" stanu w Discordzie czy mailu — Projectly to system rekordu.
- **Szablon komentarza po zakończeniu pracy** (zawsze ten sam format, żeby dało się go czytać w 10 sekund):

  ```
  ✅ / ⚠️ / ❌ [status]
  Co zrobiono: <2-4 zdania>
  Jak zweryfikowano: <lista walidatorów i wynik>
  Koszt: X USD | Czas: Y min
  Pliki/linki: <PR, screenshoty, raport>
  Wymaga decyzji: <tak/nie — jeśli tak, co konkretnie i dlaczego>
  ```

- **Status zadania w Projectly** odzwierciedla stan wewnętrzny runnera: `queued → planning → running → validating → (auto-approved | needs_approval) → done / failed`.
- **Decyzja człowieka** = komentarz lub zmiana statusu w Projectly, parsowany przez pollera jako `approve` / `reject` / `changes_requested`. Nie ma osobnego kanału do klikania "zatwierdź" — wszystko dzieje się tam, gdzie i tak żyje zadanie.
- Powiadomienie push/e-mail o pozycji "wymaga decyzji" jest opcjonalne — do dograć, jeśli Projectly nie powiadamia natywnie o nowych komentarzach/statusach.

## 3. Silnik walidacji i auto-zatwierdzania (rdzeń rozwiązania problemu)

Klasyfikacja ryzyka zostaje z oryginalnego dokumentu (zielone/żółte/czerwone), ale dochodzi **warstwa wielu niezależnych walidatorów głosujących nad żółtymi akcjami**, żeby człowiek nie musiał klikać za każdym razem.

```
              ┌─────────────────┐
 zadanie ───▶ │ risk_classifier  │
              └────────┬─────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼               ▼              ▼
    ZIELONE          ŻÓŁTE         CZERWONE
   auto, bez      3 walidatory    zawsze zadanie
   walidacji      równolegle      dla człowieka
        │               │         (sekcja 4)
        │        ┌──────┴──────┐
        │        ▼      ▼      ▼
        │     testy   wizualny  zgodność
        │   techniczne (vision)  z zakresem
        │        │      │      │
        │        └──────┼──────┘
        │               ▼
        │       ≥2/3 zgody? ──tak──▶ auto-approve,
        │               │            pełny log w Projectly
        │               nie
        │               ▼
        │          zadanie dla człowieka
        │          (sekcja 4, jak w czerwonych)
        ▼               ▼
     DONE           komentarz + status w Projectly
```

- **Zielone** (odczyt, screenshot, raport, draft) — zero walidacji, zapis do audytu i komentarz "na koniec dnia" zbiorczy, żeby nie zaśmiecać Projectly.
- **Żółte** (commit na gałęzi, aktualizacja CRM, draft maila, zmiana statusu) — walidatory głosują, próg 2 z 3 do auto-zatwierdzenia. Poniżej progu → zadanie dla człowieka (sekcja 4), dokładnie ten sam mechanizm co dla czerwonych.
- **Czerwone** (publikacja, budżet reklamowy, wysyłka masowa, usunięcie danych, nadanie roli) — **zawsze** trafiają do człowieka, niezależnie od wyniku walidatorów. To się nie zmienia względem oryginalnej dokumentacji — auto-zatwierdzanie dotyczy wyłącznie żółtych.
- Reguły klasyfikacji i progi trzymane w `approval_policy.yaml` — edytowalne bez zmiany kodu, żeby można było kręcić progiem "ile walidatorów musi się zgodzić" per typ zadania.
- Gdy walidatory się nie zgadzają albo mają niską pewność — to **nie jest błąd, to sygnał** do eskalacji, nie do zgadywania.
- **Zasada domyślna: agent radzi sobie sam.** Zadanie dla człowieka to wyjątek zarezerwowany dla decyzji, które faktycznie wymagają człowieka (autoryzacja czerwona, brakująca wiedza/dostęp, czynność prawna/fizyczna) — nie sposób na zrzucenie pracy, którą agent mógłby wykonać sam.

## 4. Obieg eskalacji: zadanie dla człowieka → komentarz → weryfikacja → kontynuacja

Kiedy agent trafia na czerwoną akcję albo żółtą bez zgody walidatorów, **nie zostawia samego komentarza z prośbą o decyzję — tworzy w Projectly osobne, dobrze opisane zadanie przypisane do konkretnej osoby** (Paweł albo wskazany pracownik). Człowiek wykonuje je jak każde inne zadanie, agent odbiera efekt i kontynuuje pracę przy najbliższym obiegu.

```
 agent napotyka        ┌──────────────────────────┐
 czerwoną akcję   ───▶ │ tworzy zadanie w Projectly│
 lub sporne żółte      │ przypisane człowiekowi:   │
                        │ - co jest potrzebne       │
                        │ - dlaczego (kontekst)     │
                        │ - screenshoty/diff/opcje  │
                        └────────────┬─────────────┘
                                     ▼
                         człowiek robi zadanie,
                         zostawia komentarz z wynikiem
                                     ▼
                     ┌───────────────────────────────┐
                     │ human_response_validator.py    │
                     │ czy komentarz odpowiada na to,  │
                     │ o co faktycznie proszono?       │
                     └──────┬────────────────┬────────┘
                            │ tak            │ nie
                            ▼                ▼
              agent tworzy sobie      agent dopytuje —
              zadanie-kontynuację     nowy komentarz z
              w Projectly z decyzją   konkretnym pytaniem,
              człowieka wbudowaną      zadanie zostaje otwarte
              w kontekst
                            ▼
              wykonanie przy najbliższym
              obiegu runnera (poller odbiera
              własne zadanie jak każde inne)
```

- **Zadanie, nie tylko komentarz.** Człowiek widzi je tam, gdzie i tak pracuje (Projectly), z priorytetem i kontekstem — nie musi pamiętać, żeby wrócić do wątku w komentarzach.
- **Weryfikacja odpowiedzi to osobny krok.** `human_response_validator.py` sprawdza, czy komentarz faktycznie rozstrzyga sprawę (np. jednoznaczne "zatwierdzam"/"nie" przy czerwonej akcji, konkretna wartość przy brakującej informacji) — jeśli nie, agent dopytuje zamiast zgadywać albo ruszać dalej na niejasnej podstawie. To ta sama zasada fail-closed co przy walidacji żółtych.
- **Kontynuacja to nowe zadanie agenta w Projectly**, nie automatyczny "resume" w tle — dzięki temu cały tok pracy (oryginalne zadanie → eskalacja → decyzja → kontynuacja) jest widoczny jako ciąg powiązanych zadań, a nie ukryty w logach.
- Runner podnosi zadanie-kontynuację na tych samych zasadach co każde inne — poller nie rozróżnia "swoich" i "cudzych" zadań, tylko sprawdza, do kogo są przypisane.

## 5. Bot jako asystent zadań ludzkich (proactive assist)

Poza własną kolejką agent cyklicznie **przegląda też zadania przypisane ludziom** w Projectly i szuka, gdzie może pomóc — nie po to, żeby przejmować ich pracę, tylko żeby ją skrócić.

| Sytuacja | Co robi agent | Efekt |
|---|---|---|
| Zadanie człowieka da się częściowo zautomatyzować | Wykonuje automatyzowalną część, zostawia komentarz "zrobiłem X, zostaje Ci Y" | Człowiekowi zostaje tylko to, czego naprawdę nie da się zautomatyzować |
| Zadanie wymaga researchu/przygotowania, ale decyzję/wykonanie musi podjąć człowiek | Przygotowuje opracowanie (research, draft, porównanie opcji) i dołącza jako komentarz/załącznik | Człowiek zaczyna od gotowego materiału zamiast białej kartki |
| Zadanie jest w pełni ludzkie (rozmowa, decyzja strategiczna, czynność fizyczna) | Nic nie robi automatycznie — najwyżej odnotowuje, że sprawdził i zadanie faktycznie wymaga człowieka | Brak fałszywych "usprawnień" tam, gdzie ich nie potrzeba |

- Agent **nie przejmuje właścicielstwa** zadania człowieka i nie oznacza go jako zakończone — dopisuje tylko efekt swojej pracy jako komentarz, decyzję o zamknięciu zostawia człowiekowi.
- To przeglądanie działa na tych samych zielonych zasadach co reszta odczytu — nie wymaga zatwierdzenia, bo nic nieodwracalnego się nie dzieje.
- Cel: **w większości przypadków agent daje sobie radę sam** (albo w pełni, albo dowożąc 80% pracy do zadania człowieka) — eskalacja z sekcji 4 zostaje dla przypadków, gdzie to faktycznie niemożliwe.

## 6. Integracje — kolejność wdrożenia i sposób podłączenia

| Integracja | Mechanizm | Ryzyko domyślne | Uwaga |
|---|---|---|---|
| Projectly | REST API + MCP | infra (bez ryzyka biznesowego) | Kolejka zadań, komentarze, status — rdzeń komunikacji |
| CRM | MCP | żółte (odczyt: zielone) | Zapis/zmiana rekordów przez walidatory; masowe operacje = czerwone |
| Meta Ads | API (główne) + Playwright (fallback UI) | budżet/publikacja = **zawsze czerwone** | API do odczytu i zmian w granicach limitu; UI tylko gdy brak API |
| Google Workspace | Google API (Docs/Sheets) | żółte | Tworzenie/aktualizacja plików roboczych |
| SharePoint | Microsoft Graph | żółte | Upload/aktualizacja artefaktów, audytu, raportów |
| Power BI | PBIP/TMDL + Desktop Bridge | odczyt: zielone, zmiana: żółte, publikacja: czerwone | Zgodnie z PBI-01/PBI-02 z dokumentacji bazowej |
| E-mail (wychodzący) | MCP → dedykowany agent mailowy | wysyłka = **zawsze czerwone** | Bot deleguje redakcję/wysyłkę do wyspecjalizowanego agenta przez MCP, nie wysyła bezpośrednio |
| E-mail (przychodzący) — intake | MCP/Graph, odczyt skrzynki | zielone (samo utworzenie zadania) | Bot czyta i klasyfikuje, tworzy zadanie w Projectly — patrz sekcja 11 |
| Dev tools (git, testy, deploy) | CLI/skrypty | commit na gałęzi: żółte, merge/deploy: czerwone | Standardowy flow branch → PR → decyzja |

## 7. Fazy wdrożenia

| Faza | Zakres | Rezultat | Czas |
|---|---|---|---|
| 0. Fundament komunikacji | Dostęp do Projectly API/MCP, kontrakt zadania, szkielet runnera + heartbeat | Runner potrafi odczytać i zaktualizować testowe zadanie | 2-3 dni |
| 1. Pętla end-to-end (bez ryzyka) | Poller → wykonanie prostego skryptu → komentarz w Projectly | Pełny cykl queued→done widoczny w Projectly, zero klikania | 3-5 dni |
| 2. Silnik walidacji i auto-zatwierdzania | risk_classifier, validator_pool (min. 3 walidatory), auto-approve żółtych | Administrator przestaje ręcznie zatwierdzać żółte zadania | 4-6 dni — **priorytet nr 1** |
| 2b. Obieg eskalacji i zadania dla ludzi | escalate_to_human.py, human_response_validator.py, continuation_task_creator.py (sekcja 4) | Czerwone/sporne trafiają jako opisane zadania, nie tylko komentarze; agent sam kontynuuje po decyzji | 3-5 dni — równolegle z Fazą 2 |
| 3. Screenshoty + Power BI | Wspólne narzędzie do zrzutów, PBI-01 (walidacja), PBI-02 (bezpieczna korekta) | Pierwszy pełny proces biznesowy działa end-to-end | 5-8 dni |
| 4. CRM + Meta Ads | Integracja API, walidatory specyficzne dla domeny | Odczyt i kontrolowane zmiany w CRM/kampaniach | 5-8 dni |
| 5. Google Workspace + SharePoint | Tworzenie plików, synchronizacja artefaktów | Bot samodzielnie produkuje i archiwizuje dokumenty | 3-5 dni |
| 6. E-mail przez agenta MCP | Most do dedykowanego agenta mailowego, walidator treści przed wysyłką | Bot przygotowuje maile, wysyłka zawsze z akceptacją | 2-4 dni |
| 7. Asystent zadań ludzkich | human_task_scanner.py, częściowa automatyzacja, przygotowywanie opracowań (sekcja 5) | Agent skraca zadania ludzi, nie tylko realizuje własne | 3-5 dni, po Fazie 2b |
| 8. Biblioteka skilli + bot ulepszający | Rejestr skilli, logowanie skuteczności, cykliczna analiza i propozycje poprawek | Skille poprawiają się same na podstawie danych z produkcji | Ciągłe, start równolegle z Fazą 2 |
| 9. Skille raportowe, porządkowanie danych i podsumowania | report_builder.py, data_tidy.py, source_schema_watcher.py, newsletter_drafter.py, digest_generator.py (sekcja 10) | Największy zmierzony koszt (INDEKA/DIVERSE firefighting, ~175h w próbce) zaczyna spadać | 5-8 dni — **priorytet nr 2** po silniku walidacji |
| 10. Intake — rozdzielanie zadań z maila i innych źródeł | email_intake_triage.py, task_routing_classifier.py, routing_confidence_check.py (sekcja 11) | Zadania powstają i trafiają do właściwej osoby/bota bez ręcznego zakładania w Projectly | 4-6 dni, po Fazie 9 |
| 11. Stabilizacja i metryki | KPI z dokumentacji bazowej (powtarzalność, koszt/zadanie, liczba eskalacji) | Decyzja: rozwijamy / iterujemy / zatrzymujemy | 4-8 dni |

## 8. Metryka sukcesu specyficzna dla tego problemu

Oprócz kryteriów z dokumentacji bazowej (rozdz. 13), dodatkowy KPI dla tego wdrożenia:

| KPI | Definicja | Cel |
|---|---|---|
| Ręczne zatwierdzenia / 100 zadań | Liczba żółtych zadań, które i tak trafiły do człowieka mimo silnika walidacji | Trend malejący, docelowo tylko czerwone + sporne |
| Zgodność walidatorów | Odsetek żółtych zadań, gdzie walidatory osiągnęły próg zgody bez eskalacji | Rosnący w miarę kalibracji progów |
| Czas do decyzji człowieka | Od utworzenia zadania dla człowieka do jego odpowiedzi w Projectly | Mierzony, nie musi maleć — ale nie powinien blokować kolejki |
| Dopytania po odpowiedzi człowieka | Odsetek przypadków, gdzie `human_response_validator.py` uznał komentarz za niewystarczający | Niski i stabilny — wysoki wskazywałby na źle sformułowane zadania dla ludzi |
| Wsparcie zadań ludzkich | Liczba zadań ludzi, gdzie agent wykonał część lub przygotował opracowanie | Rosnący — miara realnej odciążki, nie tylko własnej kolejki agenta |
| Godziny firefightingu danych (INDEKA/DIVERSE-owy wzorzec) | Godziny na "przepięcie"/"błąd w PQ"/"komunikacja o zmianach w pliku" wg raportu godzin | Malejący z miesiąca na miesiąc od wdrożenia Fazy 9 |
| Trafność auto-routingu zadań | Odsetek zadań z intake, których przypisanie nie wymagało ręcznej korekty | Rosnący w miarę kalibracji `task_routing_classifier.py` |

## 9. Bezpieczeństwo — bez zmian względem zasady nadrzędnej

Auto-zatwierdzanie żółtych **nie zmienia** zasady fail-closed z dokumentacji bazowej: jeśli agent nie jest pewny konta/aplikacji/rezultatu, to i tak zatrzymuje się i eskaluje — walidatory nie "przegłosowują" niepewności agenta, tylko potwierdzają jakość już wykonanej, jednoznacznej pracy. Czerwone pozostają zawsze poza automatycznym zatwierdzeniem, niezależnie od tego, ile walidatorów by się zgodziło.

## 10. Skille raportowe, porządkowanie danych i podsumowania

Wynik z analizy realnego raportu godzin (kwiecień-sierpień 2026): **ok. 175h w próbce to firefighting wokół danych** dla INDEKA i DIVERSE — powtarzający się wzorzec "właściciel pliku źródłowego (Michał/Wojtek/Paweł D.) zmienia strukturę bez ostrzeżenia → Power Query się wywala → godziny na ręczne przepinanie i wyjaśnianie, co się zmieniło". To największy pojedynczy koszt w całej próbce, większy niż jakikolwiek pojedynczy projekt klienta — stąd priorytet #2 zaraz po silniku walidacji.

**Biblioteka skilli raportowo-porządkowych** (szersza niż sam Power BI — Excel, Google Sheets, dowolne źródło):

- **Wykrywanie zmian struktury źródeł** (`source_schema_watcher.py`) — pilnuje plików źródłowych, wykrywa zmianę kolumny/arkusza/typu **zanim** odświeżenie się wywali, i sam tworzy zadanie dla właściciela pliku (obieg z sekcji 4) zamiast czekać, aż ktoś odkryje awarię.
- **Kontrakt struktury danych** (`data_contract_validator.py`) — lekki, uzgodniony szablon struktury pliku źródłowego per klient/proces, walidowany automatycznie przed każdym przepięciem.
- **Triage błędów Power Query** (skill, nie tylko skrypt) — wklejony błąd M/PQ dostaje klasyfikację przyczyny i gotową poprawkę, zamiast ręcznego dochodzenia za każdym razem od zera.
- **Budowa i porządkowanie raportów poza Power BI** (`report_builder.py`, `data_tidy.py`) — te same zasady co PBI-01/PBI-02 (rezultat + kryteria akceptacji, walidacja, ślad audytowy), zastosowane do raportów Excel/Google Sheets/dokumentów, które dziś Asia robi ręcznie (Kadry, Finansowy, Dane ruchy mag, raport na stronę).
- **Newsletter** (`newsletter_drafter.py`) — cykliczny draft z materiału źródłowego (zmiany produktowe, notatki, artykuły); człowiek redaguje i wysyła. Regularna, ustrukturyzowana praca — dobry pierwszy kandydat do sprawdzenia jakości draftów AI w praktyce.
- **Podsumowania** (`digest_generator.py`, `content_summarizer.py`) — bot potrafi generować: cykliczny digest aktywności z Projectly (przed Daily/Weekly, żeby skrócić lub częściowo zastąpić spotkanie), oraz streszczenia na żądanie dowolnego długiego materiału (maile, notatki ze spotkań, raporty) do szybkiego przeglądu przez człowieka.

## 11. Intake — automatyczne tworzenie i rozdzielanie zadań z maila i innych źródeł

Dziś zadania w Projectly zakłada człowiek ręcznie. Docelowo agent **czyta wejście (mail, i pluggable inne źródła) i sam zakłada dobrze opisane zadanie**, rozdzielając je do właściwej osoby lub do własnej kolejki — analogicznie do tego, jak już rozdziela pracę między siebie a ludzi (sekcje 4-5).

```
  mail / inne źródło ──▶ email_intake_triage.py
  (Teams, CRM, formularz)      │
                                 ▼
                     klasyfikacja: typ pracy +
                     projekt/klient (słowa kluczowe:
                     INDEKA, DIVERSE, AXL, Magnapharm...)
                                 │
                     ┌───────────┴───────────┐
                     ▼                       ▼
           routing_confidence_check.py   niska pewność
           wysoka pewność                       │
                     │                          ▼
                     ▼                zadanie trafia do wspólnej
        auto-tworzy zadanie w         puli z adnotacją "do
        Projectly, przypisane do      ręcznego przypisania"
        właściwej osoby lub bota      (fail-closed, jak wszędzie indziej)
```

- **Rozdzielanie po właścicielu projektu/klienta** (`task_routing_classifier.py`): dopasowanie po słowach kluczowych i historii (np. INDEKA → Asia, Magnapharm → Kacper, Okołosprzedażowe → Karol), z domyślnym przypisaniem do bota, jeśli praca jest w pełni automatyzowalna.
- **Ten sam wzorzec dla innych źródeł** (`other_source_intake.py`) — Teams, CRM, formularz zgłoszeniowy — każde źródło to osobny adapter wpinający się w tę samą klasyfikację i routing, nie osobna logika.
- **Niska pewność klasyfikacji nie jest zgadywana** — zgodnie z zasadą fail-closed z reszty dokumentu, niepewne przypadki trafiają do wspólnej puli z adnotacją, nie są przypisywane na siłę do przypadkowej osoby.
- To domyka pętlę z sekcji 1: zadanie od początku (jego powstanie) do końca (self-review, komentarz, ewentualna eskalacja) przechodzi przez Projectly bez ręcznego zakładania na wejściu.
