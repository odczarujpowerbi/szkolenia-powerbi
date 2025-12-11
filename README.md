## O projekcie

Narzędzie CLI automatyzujące proces tworzenia eleganckiej dokumentacji technicznej dla prezentacji Power BI. Projekt rozwiązuje problem rozproszonych materiałów szkoleniowych, łącząc treści merytoryczne z interaktywnymi dashboardami w spójną całość.

## Struktura projektu

Zautomatyzowany pipeline, który:
1. **Pobiera surowe materiały** - pliki Markdown z merytoryczną treścią
	- Pliki .md z materiałami merytorycznymi znajdują się w folderze [[300. INPUTS/300. INPUTS|300. INPUTS]]
	- Formatowanie tych plików obejmuje bogaty zestaw formatowania markdown
	- Każdy plik posiada frontmatter z właściwością `type` (teoria/quiz/gaps)

2. **Przetwarza algorytmicznie** - konwertuje Markdown do HTML z zachowaniem struktury
	- Realizowane przez skrypt `convert_md_to_powerbi.py`
	- Obsługa różnych typów treści (teoria/quiz/gaps) na podstawie frontmatter
	- Możliwość uruchomienia z Obsidian przez plugin Shell Commands: `Execute: Py Convert`, skrót klawiszowy: `ctrl + shift + 2`

3. **Generuje HTML** - konwertuje do formatu HTML z gotowym CSS i JS
	- Konfiguracja mapowania CSS/JS znajduje się w [[config|config.md]]
	- Zasoby (CSS/JS) znajdują się w folderze [[100. RESOURCES/100. RESOURCES|100. RESOURCES]]
		- Template CSS dla teorii: [[100. RESOURCES/CSS - Teoria - Cherry|CSS - Teoria - Cherry]] i [[100. RESOURCES/CSS - Teoria - Blue|CSS - Teoria - Blue]]
		- Template CSS dla quizów: [[100. RESOURCES/CSS - Quiz - Cherry|CSS - Quiz - Cherry]] i [[CSS - Quiz - Blue|CSS - Quiz - Blue]]
		- Template CSS dla gaps: [[100. RESOURCES/CSS - Gaps - Cherry|CSS - Gaps - Cherry]]
		- Template JS dla teorii: [[100. RESOURCES/JS - Teoria|JS - Teoria]]
		- Template JS dla quizów: [[100. RESOURCES/JS - Quiz|JS - Quiz]]
		- Template JS dla gaps: [[100. RESOURCES/JS - Gaps|JS - Gaps]]
	- Template dostępne w folderze [[000. TEMPLATES]] oraz pod komendą `Templates: Insert Template`, skrót klawiszowy: `ctrl + shift + 1`

4. **Integruje z Power BI** - tworzy miary w tabeli `_HTML`, a następnie wyświetla na wizualizacji interpretującej wartości dokumentów html
	- Gotowe miary trafiają do folderu [[400. OUTPUTS/400. OUTPUTS|400. OUTPUTS]]
	- Każda miara to osobny plik `.html`
	- Generowany jest gotowy plik `TMDL` ze wszystkimi miarami: [[400. OUTPUTS/TMDL/_HTML|_HTML.md]]
	- Dodatkowo, w [[_Parametr]] dostępny jest tabela kalkulowana/parametr pola dla utworzonych miar

## Foldery

- **[[000. TEMPLATES/000. TEMPLATES|000. TEMPLATES]]** - szablony Obsidian i inne wzorce
	- Szablony notatek dla różnych typów treści
	- Wzorce struktury dla teorii i quizów
	- Dostępne przez komendę `Templates: Insert Template` (`ctrl + shift + 1`)

- **[[100. RESOURCES/100. RESOURCES|100. RESOURCES]]** - zasoby CSS i JS dla różnych typów treści
	- Pliki CSS: Teoria (Cherry, Blue), Quiz (Cherry, Blue), Gaps (Cherry)
	- Pliki JS: Teoria, Quiz, Gaps
	- Wykorzystywane przez `convert_md_to_powerbi.py` według konfiguracji w `config.md`

- **[[200. DRAFTS/200. DRAFTS|200. DRAFTS]]** - wersje robocze materiałów
	- Nieukończone materiały szkoleniowe
	- Notatki do przyszłego opracowania
	- Eksperymentalne treści przed finalną wersją

- **[[300. INPUTS/300. INPUTS|300. INPUTS]]** - pliki źródłowe Markdown (teoria, quizy, gaps)
	- Gotowe materiały szkoleniowe w formacie Markdown
	- Pliki z frontmatter określającym typ (teoria/quiz/gaps)
	- Źródło dla procesu konwersji do HTML

- **[[400. OUTPUTS/400. OUTPUTS|400. OUTPUTS]]** - wygenerowane pliki HTML i TMDL
	- Pliki `.html` - miary Power BI gotowe do importu
	- Folder `TMDL/` - definicje miar w formacie TMDL
	- `_HTML.md` - plik TMDL ze wszystkimi miarami
	- `_Parametr.md` - tabela kalkulowana z metadanymi miar

- **[[500. ARCHIVE/500. ARCHIVE|500. ARCHIVE]]** - zarchiwizowane materiały
	- Stare wersje materiałów szkoleniowych
	- Nieaktualne treści zachowane dla historii
	- Backup poprzednich iteracji projektu

