# Instrukcja wdrożenia — krok po kroku

Ten dokument jest dla osoby, która fizycznie usiądzie przy komputerze i uruchomi na nim Wirtualnego Pracownika — niekoniecznie dla osoby technicznej. Czytaj po kolei, od góry, nie przeskakuj kroków. Każdy krok mówi: co robisz, dlaczego, i po czym poznasz, że się udało.

Jeśli w którymś miejscu coś nie zadziała tak, jak opisano — zatrzymaj się, skopiuj cały komunikat błędu (na czerwono/w konsoli) i prześlij go osobie technicznej albo do Claude Code, zamiast zgadywać dalej.

## Zanim zaczniesz — czego będziesz potrzebować

- **Komputer** — Windows 11, minimum 16 GB RAM (lepiej 32 GB), stały dostęp do prądu i internetu. To ma być komputer dedykowany, nie ten, na którym ktoś pracuje codziennie.
- **Karta płatnicza** — do założenia konta z dostępem do API Anthropic (płatność za realne zużycie, z ustawionym limitem — patrz Krok 4).
- **Dostęp do internetu w trakcie całej instalacji.**
- **Lista kont i haseł do zebrania** — zanim zaczniesz, dobrze mieć pod ręką dostęp do: konta Anthropic (API), konta Projectly, konta Microsoft 365 (mail), konta Google, Zoho CRM, zanfia.com, GitHub, MailerLite. Nie wszystkie są potrzebne od razu — w Kroku 4 jest jasno napisane, co jest obowiązkowe na start, a co można dograć później.

## Krok 1 — Przygotowanie komputera

1. Zainstaluj/zaktualizuj Windows 11 do najnowszej wersji.
2. Podłącz komputer na stałe do prądu (nie na baterii) i do internetu — najlepiej kablem, nie Wi-Fi, jeśli to możliwe.
3. Wyłącz usypianie komputera: **Ustawienia → System → Zasilanie → Ekran i uśpienie → nigdy** (dla trybu podłączonego do zasilania).
4. Utwórz dwa konta użytkownika Windows: jedno zwykłe (standardowe) — to będzie konto, na którym pracuje bot — i jedno administratora, używane tylko do instalacji. Nie loguj się na koncie bota jako administrator na co dzień.

**Po czym poznasz, że ten krok się udał:** komputer jest włączony, podłączony do prądu i internetu, ekran się nie wygasza, są dwa konta użytkownika widoczne na ekranie logowania.

## Krok 2 — Instalacja programów

Instaluj w tej kolejności. Każdy program pobierasz z oficjalnej strony, klikasz "Dalej"/"Next" z ustawieniami domyślnymi, chyba że napisano inaczej.

| # | Program | Skąd pobrać | Uwaga przy instalacji |
|---|---|---|---|
| 1 | Git | [git-scm.com](https://git-scm.com/download/win) | Ustawienia domyślne wystarczą |
| 2 | Python 3.11 lub nowszy | [python.org/downloads](https://www.python.org/downloads/windows/) | **WAŻNE:** na pierwszym ekranie instalatora zaznacz "Add python.exe to PATH", zanim klikniesz Install |
| 3 | Node.js (wersja LTS) | [nodejs.org](https://nodejs.org/) | Potrzebny do Claude Code (krok niżej) |
| 4 | Power BI Desktop | Microsoft Store albo [powerbi.microsoft.com](https://powerbi.microsoft.com/desktop/) | Potrzebne dopiero, gdy dojdziemy do automatyzacji raportów Power BI — możesz zainstalować teraz albo później |

Po instalacji Node.js, zainstaluj Claude Code — otwórz **Wiersz polecenia** (wpisz w wyszukiwarce Windows "cmd") i wklej:

```
npm install -g @anthropic-ai/claude-code
```

**Jak sprawdzić, czy wszystko się zainstalowało:** otwórz Wiersz polecenia i po kolei wpisz poniższe komendy — każda powinna pokazać numer wersji, nie komunikat błędu:

```
git --version
python --version
node --version
claude --version
```

Jeśli którakolwiek komenda pokazuje błąd typu "nie jest rozpoznawana jako polecenie" — ten program nie zainstalował się poprawnie albo trzeba zrestartować komputer, żeby zmiany się zastosowały. Zrestartuj i spróbuj ponownie, zanim przejdziesz dalej.

## Krok 3 — Pobranie projektu

Wybierz jedną z dwóch opcji.

**Opcja A — prościej, jednorazowo:** wejdź na stronę repozytorium na GitHubie, kliknij zielony przycisk **Code → Download ZIP**, rozpakuj pobrany plik do `C:\AIWorker\`.

**Opcja B — wygodniej na później** (łatwiejsze aktualizacje): otwórz Wiersz polecenia i wpisz:

```
git clone <adres repozytorium> C:\AIWorker
```

(adres repozytorium dostaniesz od osoby, która Cię wdraża).

**Po czym poznasz, że się udało:** folder `C:\AIWorker\wirtualny-pracownik\app\` istnieje i widać w nim pliki takie jak `runner_loop.py`, `README.md`.

## Krok 4 — Zebranie i wpisanie dostępów (kluczy)

To najważniejszy krok do zrobienia uważnie — te dane działają jak hasła. **Nigdy nie wysyłaj ich mailem, na czacie ani nikomu nie pokazuj zrzutu ekranu z nimi.**

1. W folderze `C:\AIWorker\wirtualny-pracownik\app\` znajdź plik `.env.example`. Skopiuj go i zmień nazwę kopii na `.env` (bez ".example" na końcu).
2. Otwórz plik `.env` Notatnikiem (kliknij prawym przyciskiem → Otwórz za pomocą → Notatnik).
3. Wpisz klucze w odpowiednich miejscach, po znaku `=`, bez spacji i bez cudzysłowów.

| Klucz w pliku `.env` | Skąd go wziąć | Czy obowiązkowy na start |
|---|---|---|
| `ANTHROPIC_API_KEY` | Załóż konto na [console.anthropic.com](https://console.anthropic.com), zakładka "API Keys", stwórz nowy klucz. Ustaw tam też miesięczny limit wydatków (zalecane: zacznij od małej kwoty, np. 20 USD) | **Tak, obowiązkowy** |
| `PROJECTLY_API_KEY` / `PROJECTLY_BASE_URL` | Z ustawień konta w Projectly | **Tak, obowiązkowy** |
| Reszta (Zoho CRM, Google, MailerLite, zanfia.com...) | Osobno dla każdej usługi — pełna lista i status w pliku `config/integrations.yaml` w tym samym folderze | Nie od razu — dograj, gdy dana funkcja zacznie być używana |

**Po czym poznasz, że się udało:** plik `.env` istnieje (nie `.env.example`), ma wpisany przynajmniej klucz Anthropic i dane do Projectly.

## Krok 5 — Pierwsze uruchomienie i test

1. Otwórz Wiersz polecenia.
2. Przejdź do folderu projektu:
   ```
   cd C:\AIWorker\wirtualny-pracownik\app
   ```
3. Zainstaluj wymagane biblioteki Pythona:
   ```
   pip install -r requirements.txt
   ```
4. Uruchom test dymny (sprawdza, czy wszystko działa, zanim cokolwiek zacznie robić prawdziwą pracę):
   ```
   python bootstrap_smoke_test.py
   ```

**Czego się spodziewać:** na ekranie pojawi się kilka linijek z zielonymi ✅, a na końcu napis:

```
Wszystkie testy przeszły. Komputer gotowy do rejestracji (bootstrap_register.py).
```

Jeśli zamiast tego widzisz czerwony błąd — zatrzymaj się tutaj i skopiuj cały komunikat do osoby technicznej.

## Krok 6 — Nadanie temu komputerowi roli

Ten komputer musi wiedzieć, czym się zajmuje (np. sprawami deweloperskimi, marketingiem). W Wierszu polecenia (w tym samym folderze) wpisz:

```
python bootstrap_register.py dev
```

(zamiast `dev` wpisz właściwą rolę — dostępne role są wypisane, jeśli wpiszesz samo `python bootstrap_register.py` bez niczego po nim).

**Po czym poznasz, że się udało:** na ekranie pojawi się "Zarejestrowano komputer jako rola '...'" i krótkie podsumowanie statusu.

## Krok 7 — Gdzie wgrywać nowe umiejętności (skille)

Nowe umiejętności bota (np. jak dobrze pracować z konkretnym narzędziem) trzymane są w folderze na OneDrive — np. `AI Worker\Skills\`. Żeby dodać nową umiejętność: wrzuć jej folder do tego miejsca na OneDrive. Komputer sam sprawdza ten folder co jakiś czas i pobiera nowości — nie trzeba nic więcej robić ręcznie.

Lista umiejętności, które są już zaplanowane (część gotowa, część czeka na napisanie), jest w pliku `config/skills_manifest.yaml`.

## Krok 8 — Uruchomienie na stałe (żeby działało bez Ciebie)

Żeby program uruchamiał się sam po restarcie komputera i działał w tle:

1. Otwórz **Harmonogram zadań** (wpisz w wyszukiwarce Windows "Harmonogram zadań" / "Task Scheduler").
2. Kliknij **Utwórz zadanie podstawowe** (Create Basic Task).
3. Nazwa: np. "Wirtualny Pracownik — Runner".
4. Wyzwalacz: **Przy uruchomieniu komputera** (When the computer starts).
5. Akcja: **Uruchom program** (Start a program).
6. W polu "Program/skrypt" wpisz: `python`
7. W polu "Argumenty" wpisz: `runner_loop.py --loop`
8. W polu "Rozpocznij w" wpisz: `C:\AIWorker\wirtualny-pracownik\app`
9. Zapisz zadanie.

**Po czym poznasz, że się udało:** po restarcie komputera, po kilku minutach, w Projectly pojawia się wpis statusu ("status na żywo") dla tego komputera.

## Krok 9 — Jak sprawdzić, że wszystko działa na żywo

Otwórz Projectly. Powinieneś widzieć:
- Nowe zadania testowe przechodzące przez statusy (od "queued" do "done" albo "needs_approval").
- Komentarze zostawiane przy zadaniach z podsumowaniem, co bot zrobił.
- Wpis "status na żywo" dla tego komputera, aktualizowany co 1-2 minuty.

Jeśli nic się nie dzieje przez dłuższy czas — sprawdź Krok 8 (czy zadanie w Harmonogramie faktycznie wystartowało) i plik `.env` (czy klucze są poprawnie wpisane).

## Krok 10 — Bezpieczeństwo: jak natychmiast wszystko zatrzymać

Jeśli coś wygląda niepokojąco (bot robi coś, czego nie powinien, albo zwyczajnie chcesz przerwać na chwilę) — otwórz Wiersz polecenia w folderze `app` i wpisz:

```
python kill_switch.py stop
```

To natychmiast zatrzymuje wszystkie działania, bez wykonywania kolejnych akcji, dopóki sam nie odblokujesz komendą:

```
python kill_switch.py resume
```

Nie musisz się bać używać tego zbyt często — to jest dokładnie po to, żeby dawało się bezpiecznie zatrzymać w każdej chwili.

## Checklist końcowy

- [ ] Komputer przygotowany (prąd, internet, usypianie wyłączone, dwa konta użytkownika)
- [ ] Zainstalowane: Git, Python, Node.js, Claude Code (Power BI Desktop w miarę potrzeby)
- [ ] Projekt pobrany do `C:\AIWorker\`
- [ ] Plik `.env` utworzony i wypełniony (minimum: Anthropic + Projectly)
- [ ] `pip install -r requirements.txt` wykonane bez błędów
- [ ] `python bootstrap_smoke_test.py` pokazuje "Wszystkie testy przeszły"
- [ ] Komputer zarejestrowany z właściwą rolą (`bootstrap_register.py`)
- [ ] Folder skilli na OneDrive znaleziony i znany
- [ ] Zadanie w Harmonogramie zadań Windows utworzone i przetestowane (restart komputera)
- [ ] W Projectly widać status na żywo i przetworzone zadania
- [ ] Wiadomo, jak i kiedy użyć `kill_switch.py stop`
