## O projekcie

Narzędzie CLI automatyzujące proces tworzenia eleganciej dokumentacji technicznej dla prezentacji Power BI. Projekt rozwiązuje problem rozproszonych materiałów szkoleniowych, łącząc treści merytoryczne z interaktywnymi dashboardami w spójną całość.

## Struktura projektu

Zautomatyzowany pipeline, który:
1. **Pobiera surowe materiały** - pliki Markdown z merytoryczną treścią
	- Pliki .md z materiałami merytorycznymi znajdują się w folderze **Theory**
	- Formatowanie tych plików obejmuje bogaty zestaw formatowania markdown
2. **Przetwarza przez AI** - redaguje i ulepsza treść zachowując wartość merytoryczną
	- AI musi przygotować tekst do wersji strawnej dla HTML
	- Krok do zastąpienia - efektywność pracy AI jest niska i może zostać zalgorytmizowana (pandoc?)
3. **Generuje HTML** - konwertuje do formatu HTML z gotowym CSS i JS
	- Template znajduje się odpowiednio w [[CSS - Niebieski|Template/CSS]] i [[JS|Template/JS]]
	- Znak `---` Symbolizuje oddzielną stronę, która jest paginowana przez `JS`
4. **Integruje z Power BI** - tworzy miary w tabeli `_HTML`, a następnie wyświetla na wizualizacji interpretującej wartości dokumentów html
	- Gotowe miary trafiają do folder **Output**, przykładowo [[1. Podstawy DAX.html]]



# szkolenia-powerbi
