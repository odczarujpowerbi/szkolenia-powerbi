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
   auto, bez      3 walidatory    zawsze do
   walidacji      równolegle      Projectly
        │               │         (decyzja
        │        ┌──────┴──────┐  człowieka)
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
        │          eskalacja do Projectly
        │          jako "wymaga decyzji"
        ▼               ▼
     DONE           komentarz + status w Projectly
```

- **Zielone** (odczyt, screenshot, raport, draft) — zero walidacji, zapis do audytu i komentarz "na koniec dnia" zbiorczy, żeby nie zaśmiecać Projectly.
- **Żółte** (commit na gałęzi, aktualizacja CRM, draft maila, zmiana statusu) — walidatory głosują, próg 2 z 3 do auto-zatwierdzenia. Poniżej progu → eskalacja.
- **Czerwone** (publikacja, budżet reklamowy, wysyłka masowa, usunięcie danych, nadanie roli) — **zawsze** czeka na człowieka, niezależnie od wyniku walidatorów. To się nie zmienia względem oryginalnej dokumentacji — auto-zatwierdzanie dotyczy wyłącznie żółtych.
- Reguły klasyfikacji i progi trzymane w `approval_policy.yaml` — edytowalne bez zmiany kodu, żeby można było kręcić progiem "ile walidatorów musi się zgodzić" per typ zadania.
- Gdy walidatory się nie zgadzają albo mają niską pewność — to **nie jest błąd, to sygnał** do eskalacji, nie do zgadywania.

## 4. Integracje — kolejność wdrożenia i sposób podłączenia

| Integracja | Mechanizm | Ryzyko domyślne | Uwaga |
|---|---|---|---|
| Projectly | REST API + MCP | infra (bez ryzyka biznesowego) | Kolejka zadań, komentarze, status — rdzeń komunikacji |
| CRM | MCP | żółte (odczyt: zielone) | Zapis/zmiana rekordów przez walidatory; masowe operacje = czerwone |
| Meta Ads | API (główne) + Playwright (fallback UI) | budżet/publikacja = **zawsze czerwone** | API do odczytu i zmian w granicach limitu; UI tylko gdy brak API |
| Google Workspace | Google API (Docs/Sheets) | żółte | Tworzenie/aktualizacja plików roboczych |
| SharePoint | Microsoft Graph | żółte | Upload/aktualizacja artefaktów, audytu, raportów |
| Power BI | PBIP/TMDL + Desktop Bridge | odczyt: zielone, zmiana: żółte, publikacja: czerwone | Zgodnie z PBI-01/PBI-02 z dokumentacji bazowej |
| E-mail | MCP → dedykowany agent mailowy | wysyłka = **zawsze czerwone** | Bot deleguje redakcję/wysyłkę do wyspecjalizowanego agenta przez MCP, nie wysyła bezpośrednio |
| Dev tools (git, testy, deploy) | CLI/skrypty | commit na gałęzi: żółte, merge/deploy: czerwone | Standardowy flow branch → PR → decyzja |

## 5. Fazy wdrożenia

| Faza | Zakres | Rezultat | Czas |
|---|---|---|---|
| 0. Fundament komunikacji | Dostęp do Projectly API/MCP, kontrakt zadania, szkielet runnera + heartbeat | Runner potrafi odczytać i zaktualizować testowe zadanie | 2-3 dni |
| 1. Pętla end-to-end (bez ryzyka) | Poller → wykonanie prostego skryptu → komentarz w Projectly | Pełny cykl queued→done widoczny w Projectly, zero klikania | 3-5 dni |
| 2. Silnik walidacji i auto-zatwierdzania | risk_classifier, validator_pool (min. 3 walidatory), auto-approve żółtych, eskalacja czerwonych | Administrator przestaje ręcznie zatwierdzać żółte zadania | 4-6 dni — **priorytet nr 1** |
| 3. Screenshoty + Power BI | Wspólne narzędzie do zrzutów, PBI-01 (walidacja), PBI-02 (bezpieczna korekta) | Pierwszy pełny proces biznesowy działa end-to-end | 5-8 dni |
| 4. CRM + Meta Ads | Integracja API, walidatory specyficzne dla domeny | Odczyt i kontrolowane zmiany w CRM/kampaniach | 5-8 dni |
| 5. Google Workspace + SharePoint | Tworzenie plików, synchronizacja artefaktów | Bot samodzielnie produkuje i archiwizuje dokumenty | 3-5 dni |
| 6. E-mail przez agenta MCP | Most do dedykowanego agenta mailowego, walidator treści przed wysyłką | Bot przygotowuje maile, wysyłka zawsze z akceptacją | 2-4 dni |
| 7. Biblioteka skilli + bot ulepszający | Rejestr skilli, logowanie skuteczności, cykliczna analiza i propozycje poprawek | Skille poprawiają się same na podstawie danych z produkcji | Ciągłe, start równolegle z Fazą 2 |
| 8. Stabilizacja i metryki | KPI z dokumentacji bazowej (powtarzalność, koszt/zadanie, liczba eskalacji) | Decyzja: rozwijamy / iterujemy / zatrzymujemy | 4-8 dni |

## 6. Metryka sukcesu specyficzna dla tego problemu

Oprócz kryteriów z dokumentacji bazowej (rozdz. 13), dodatkowy KPI dla tego wdrożenia:

| KPI | Definicja | Cel |
|---|---|---|
| Ręczne zatwierdzenia / 100 zadań | Liczba żółtych zadań, które i tak trafiły do człowieka mimo silnika walidacji | Trend malejący, docelowo tylko czerwone + sporne |
| Zgodność walidatorów | Odsetek żółtych zadań, gdzie walidatory osiągnęły próg zgody bez eskalacji | Rosnący w miarę kalibracji progów |
| Czas do decyzji człowieka | Od eskalacji czerwonej do odpowiedzi w Projectly | Mierzony, nie musi maleć — ale nie powinien blokować kolejki |

## 7. Bezpieczeństwo — bez zmian względem zasady nadrzędnej

Auto-zatwierdzanie żółtych **nie zmienia** zasady fail-closed z dokumentacji bazowej: jeśli agent nie jest pewny konta/aplikacji/rezultatu, to i tak zatrzymuje się i eskaluje — walidatory nie "przegłosowują" niepewności agenta, tylko potwierdzają jakość już wykonanej, jednoznacznej pracy. Czerwone pozostają zawsze poza automatycznym zatwierdzeniem, niezależnie od tego, ile walidatorów by się zgodziło.
