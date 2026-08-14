# Checklist przed startem pilotażu

Zbiera w jednym miejscu decyzje otwarte, rozproszone dziś po `PLAN-WDROZENIA.md`, `SKRYPTY.md`, `ZESPOL-BOTOW.md` i pierwotnej dokumentacji koncepcyjnej, plus kilka tematów, które nigdzie jeszcze nie padły. Nic z tego nie jest kodem — to decyzje i ustalenia, które trzeba zamknąć przed, nie po, uruchomieniu pierwszej linijki.

## 1. Rejestr decyzji z dokumentacji bazowej — wciąż otwarty

Załącznik D oryginalnego dokumentu koncepcyjnego (`Wirtualny_Pracownik_AI_Dokumentacja_Biznesowa_i_Techniczna.pdf`) zawiera te pytania od sierpnia — żadne nie zostało jeszcze formalnie zamknięte w tej rozmowie:

| ID | Decyzja | Odpowiedzialny |
|---|---|---|
| D-01 | Który konkretny komputer i czy obsługuje 32 GB RAM | Właściciel projektu |
| D-02 | Które 3 procesy mają najwyższą wartość i najniższy poziom ryzyka | Biznes + techniczny |
| D-03 | Czy istniejący plan Claude zapewnia potrzebną funkcję interaktywną | Właściciel projektu |
| D-04 | Który workspace Power BI i które repo są sandboxem | Power BI owner |
| D-05 | Jaka retencja screenshotów i logów jest akceptowalna | Właściciel danych |
| D-06 | Które działania są zielone, żółte i czerwone (pierwsza wersja `approval_policy.yaml`) | Właściciele procesów |
| D-07 | Kto odbiera alerty i zatwierdza działania poza godzinami | Zespół |

## 2. Integracje ze statusem "do doprecyzowania"

- **System transakcyjny (sprzedaż)** — `PLAN-WDROZENIA.md` sekcja 6 zaznacza mechanizm API jako "do doprecyzowania po stronie systemu". Bez tego `sales_report_builder.py` (sekcja 18/kategoria P) nie ma się o co oprzeć.
- **Social media (widoczność w sieci)** — które konkretnie platformy (i czy mają API, czy trzeba scrapować/UI) też jeszcze nie ustalone.

## 3. Tematy, które jeszcze nie padły w żadnym dokumencie

- **RODO / zgodność prawna.** Dane realnych klientów (INDEKA, DIVERSE, AXL, Magnapharm) będą przechodzić przez API modeli AI (Anthropic, OpenRouter). Warto zweryfikować warunki przetwarzania danych z dostawcami **przed** tym, jak realne dane klientów zaczną tam trafiać — nie po fakcie.
- **Zespół i zarządzanie zmianą.** Asia, Kacper, Karol i Michał będą mieli swoją pracę analizowaną (`task_retro_auditor.py` czyta ich historię zadań), a część ich zadań przejmie bot (`human_task_partial_executor.py`, intake). Warto ich o tym poinformować zawczasu — bot czytający czyjąś pracę bez wyjaśnienia po co budzi niepokój szybciej niż cokolwiek technicznego w tym planie.
- **Środowisko testowe vs produkcyjne.** Pierwsze uruchomienia PBI-01/PBI-02 dotyczą żywych projektów klientów (INDEKA, DIVERSE). Czy istnieje piaskownica/kopia projektu do testów, czy pierwsze uruchomienie dzieje się od razu na prawdziwym repo?
- **Kopie zapasowe samego komputera pilotażowego.** Awaria dysku na jedynej maszynie oznacza utratę nie tylko konfiguracji, ale całego audytu i historii decyzji (`events.jsonl`, `state_store.py` — podstawa trybu rozmowy z sekcji 14). Potrzebny backup poza tą jedną maszyną, nie tylko lokalny snapshot.
- **Projectly jako pojedynczy punkt awarii.** Cały system (kolejka, komunikacja, audyt) stoi na jednej aplikacji. Co się dzieje przy przestoju Projectly — runner czeka bezczynnie, czy ma lokalną kolejkę zapasową?
- **Prowizjonowanie dostępów.** Osiem integracji (Projectly, CRM, Meta Ads, Google Workspace, SharePoint, inFakt, Search Console/Analytics, social media) to sama w sobie realna praca administracyjna — kto i kiedy zakłada konta/klucze/tokeny, zanim faza wdrożenia, która ich potrzebuje, w ogóle się zacznie.
- **Koszt miesięczny — realna liczba, nie tylko zasada.** `PLAN-WDROZENIA.md` sekcja 3 rekomenduje policzenie kosztu (zadania/dzień × wywołania × koszt tokenów) przed wdrożeniem silnika walidacji na produkcję — to wciąż rekomendacja, nie policzona liczba.

## 4. Przypomnienie zakresu — najważniejsze

Po tej serii rozmów plan urósł do: silnika walidacji, obiegu eskalacji, asystenta zadań ludzkich, bibliotek skilli raportowych, intake z maila, harmonogramu i równoległości, zasady "ma zdanie", trybu rozmowy, podsumowań głos/wideo, cyklicznego retro-audytu, kill switcha, cotygodniowych raportów biznesowych z bounded red, oraz całego zespołu botów-ról z agentem strategicznym.

**Pilotaż to nadal tylko Fazy 0-2 (opcjonalnie +3) z `PLAN-WDROZENIA.md`:** fundament komunikacji z Projectly, pętla end-to-end bez ryzyka, silnik walidacji i auto-zatwierdzania, ewentualnie pierwszy proces Power BI/INDEKA. Wszystko powyżej (Fazy 4+, cały `ZESPOL-BOTOW.md`) czeka na dowód, że ten najmniejszy możliwy kawałek działa stabilnie na produkcji przez kilka tygodni. Łatwo to zgubić z oczu przy tylu już zaprojektowanych warstwach — ten dokument ma o tym przypominać.
