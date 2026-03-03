createOrReplace

    table _HTML
        lineageTag: ef39d3bc-2ed3-4762-8fb8-ed4b9fd9a071

        measure '01. UI - Wstęp' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Wstęp</title>
    <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
    
            body {
                font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                font-size: 16px;
                font-weight: 400;
                line-height: 1.7;
                color: #333;
                background: transparent;
                padding: 20px;
            }
    
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: transparent;
                padding: 40px;
            }
    
            .navigation {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 40px;
                padding-bottom: 20px;
                border-bottom: 1px solid #e1e4e8;
            }
    
            button {
                background: #6b1718;
                color: white;
                border: none;
                padding: 12px 28px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 1em;
                font-weight: 500;
                transition: background 0.2s;
            }
    
            button:hover {
                background: #380c0c;
            }
    
            button:disabled {
                background: #ccc;
                cursor: not-allowed;
            }
    
            .page-indicator {
                color: #666;
                font-size: 1em;
            }
    
            .page {
                display: none;
                min-height: 500px;
            }
    
            .page.active {
                display: block;
                animation: fadeIn 0.3s ease-in;
            }
    
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
    
            h1 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin-bottom: 1em;
                color: #6b1718;
                border-bottom: 2px solid #6b1718;
            }
    
            h2 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin: 1.5em 0 0.8em 0;
                color: #1a1a1a;
                border-bottom: 2px solid #1a1a1a;
            }
    
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                padding-bottom: 5px;
                color: #444;
                border-bottom: 1px solid #999;
            }
    
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            code {
                background: #f5f5f5;
                padding: 3px 7px;
                border-radius: 3px;
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            pre code {
                background: none;
                padding: 0;
                color: #24292e;
                font-size: 1em;
                line-height: 1.6;
            }
    
            .dax-keyword {
                color: #6b1718;
                font-weight: 600;
            }
    
            .dax-function {
                color: #6f42c1;
            }
    
            .dax-number {
                color: #005cc5;
            }
    
            .dax-comment {
                color: #6a737d;
                font-style: italic;
            }
    
            ul, ol {
                margin: 0.3em 0;
                padding-left: 1.8em;
            }
    
            li {
                margin: 0;
                padding-left: 0.2em;
                font-size: 1.05em;
                line-height: 1.6;
            }
    
            ol {
                list-style-type: decimal;
            }
    
            ol li::marker {
                color: #999;
                font-weight: 400;
            }
    
            ul li::marker {
                color: #999;
            }
    
            ul ul, ol ol, ul ol, ol ul {
                margin: 0.2em 0;
                padding-left: 1.5em;
            }
    
            blockquote {
                border-left: 3px solid #6b1718;
                background: #f8f9fa;
                padding: 14px 18px;
                margin: 1em 0;
                color: #555;
                font-style: italic;
            }
    
            blockquote p {
                margin: 0;
            }
    
            .iteration-box {
                border-left: 3px solid #6b1718;
                padding: 14px 18px;
                margin: 0.8em 0;
            }
    
            .result-box {
                background: #f5f5f5;
                border-left: 3px solid #999;
                padding: 14px 18px;
                margin: 0.8em 0;
                font-weight: 500;
                color: #555;
                font-size: 1.05em;
            }
        </style>
</head>
<body>

<div class='container' id='viz_2adb3687'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_2adb3687' onclick='changePage_2adb3687(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_2adb3687'>1</span> z <span id='totalPages_2adb3687'>3</span>
        </span>
        <button id='nextBtn_2adb3687' onclick='changePage_2adb3687(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Sekcja 1</h1>
        <p>Power Query to narzędzie w Power BI umożliwiające pobieranie danych z dziesiątek różnych źródeł – od plików lokalnych (Excel, CSV, JSON), przez bazy danych (SQL Server, MySQL, Oracle), aż po usługi online (SharePoint, OneDrive) i API REST.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303144240.png?raw=true' width='100%'>
        <h1>Sekcja 2</h1>
        <p>Po pobraniu danych można je przechowywać na kilka sposobów: w trybie <strong>Import</strong> dane są ładowane do modelu semantycznego i odświeżane cyklicznie, natomiast <strong>DirectQuery/LiveConnect</strong> pozwala odpytywać źródło na bieżąco bez lokalnego kopiowania danych. Istnieje również tryb <strong>Push</strong> oraz integracja ze <strong>Stream Analytics</strong>, która obsługuje dane napływające w czasie rzeczywistym. </p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303144257.png?raw=true' width='100%'>
        <p>Centralnym elementem jest <strong>Model Semantyczny</strong>, który integruje wszystkie te źródła i tryby połączeń, umożliwiając budowanie wydajnych modeli w oparciu o strukturę gwiazdy. Dzięki temu Power BI elastycznie obsługuje każdy scenariusz – od małych plików po duże, live‛owe bazy danych produkcyjne.</p>
        <h1>Przede wszystkim - jakość danych</h1>
        <p>Power Query oferuje wbudowany podgląd jakości danych dla każdej kolumny – widać od razu rozkład wartości, procent błędów i pustych komórek, co pozwala błyskawicznie ocenić stan surowych danych bez pisania kodu. Jeden rzut okiem wystarcza, by zrozumieć, co należy <strong>na pewno</strong> trzeba zrobić z danymi. Pytania, na które odpowiada ten widok:</p>
        <ul>
        <li>Czy kolumna może być kluczem głównym? (Distinct = Unique)</li>
        <li>Czy dane są kompletne? (ile % wartości jest pustych?)</li>
        <li>Czy w kolumnie są błędy? (np. błędny typ)</li>
        <li>Jaki jest rozkład wartości? (czy dane są równomiernie rozłożone czy mocno skośne?)</li>
        <li>Czy są anomalie i outliery? (wartości odstające widoczne na histogramie)</li>
        <li>Ile unikalnych wartości zawiera kolumna? (przydatne przy kolumnach kategorialnych)</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303144311.png?raw=true' width='100%'>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Transformacja danych</h1>
        <p>Transformacje wykonuje się intuicyjnie z poziomu interfejsu graficznego: filtrowanie wierszy według złożonych warunków, sortowanie, zmiana typów danych czy dzielenie kolumn po separatorze to kwestia kilku kliknięć. Nowe kolumny obliczeniowe – w tym formuły czy warunki IF…ELSE – tworzy się przez dedykowane okna dialogowe, bez potrzeby ręcznego pisania kodu. </p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303144626.png?raw=true' width='100%'>
        <h2>Co można zrobić?</h2>
        <p><strong>Czyszczenie i standaryzacja danych</strong></p>
        <ul>
        <li>Usuń lub zastąp błędy i wartości null konkretną wartością (0, ”Brak”, itd.)</li>
        <li>Wypełnij puste komórki wartością z wiersza powyżej/poniżej (Fill Down/Up)</li>
        <li>Zastąp wartości – standaryzuj dane (”PL” → ”Polska”, ”M” → ”Mężczyzna”)</li>
        <li>Przytnij białe znaki, zmień wielkość liter, wyodrębnij fragmenty tekstu</li>
        <li>Zmień typy danych – tekst, liczba, data, wartość logiczna</li>
        </ul>
        <p><strong>Filtrowanie, sortowanie i agregacja</strong></p>
        <ul>
        <li>Filtruj wiersze po dowolnych warunkach (AND/OR, tekst, liczby, daty, nulle)</li>
        <li>Sortuj po wielu kolumnach jednocześnie z zachowaniem priorytetów</li>
        <li>Grupuj dane jak GROUP BY w SQL – SUM, COUNT, MIN, MAX, AVERAGE po jednej lub wielu kolumnach</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303144704.png?raw=true' width='100%'>
        <p><strong>Dodawanie i przekształcanie kolumn</strong></p>
        <ul>
        <li>Kolumny warunkowe (IF…ELSE IF…ELSE) – bez pisania kodu, przez okno dialogowe</li>
        <li>Kolumny niestandardowe – własne formuły w języku M z odwołaniem do innych kolumn</li>
        <li>Kolumny z przykładów – podajesz oczekiwany wynik, Power Query sam generuje formułę (AI)</li>
        <li>Funkcje datowe – wyodrębnij rok, miesiąc, kwartał, dzień tygodnia, oblicz różnice dat</li>
        <li>Pivot / Unpivot – obróć wartości w kolumny lub spłaszcz szeroką tabelę do formatu długiego</li>
        </ul>
        <p><strong>Łączenie i restrukturyzacja tabel</strong></p>
        <ul>
        <li>Merge (JOIN) – łącz tabele jak w SQL: Left, Inner, Full Outer, Anti Join po jednym lub wielu kluczach</li>
        <li>Append (UNION) – dołączaj tabele o tej samej strukturze w jedną</li>
        <li>Split Column – dziel tekst po separatorze lub liczbie znaków, na kolumny lub wiersze</li>
        <li>Transpozycja, promowanie nagłówków – restrukturyzuj orientację tabeli jednym kliknięciem</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303144645.png?raw=true' width='100%'>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Kontrola transformacji i edytor zaawansowany</h1>
        <p>Power Query rejestruje każdą wykonaną operację jako osobny, nazwany krok – dzięki temu masz pełny wgląd w to, co dzieje się z danymi na każdym etapie procesu. To nie tylko wygoda, ale też potężne narzędzie do debugowania i eksperymentowania bez ryzyka utraty pracy.</p>
        <ul>
        <li>Kliknij dowolny krok – zobaczysz dokładnie jak wyglądały dane w tym miejscu procesu</li>
        <li>Edytuj, usuń lub wstaw krok w dowolnym miejscu sekwencji bez psucia całości</li>
        <li>Błyskawicznie znajdziesz etap, na którym coś poszło nie tak</li>
        <li>Cofnięcie do poprzedniego stanu to jedno kliknięcie – eksperymentuj bez obaw</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303145812.png?raw=true' width='100%'>
        <h2>Edytor Zaawansowany</h2>
        <p>Interfejs graficzny Power Query pokrywa zdecydowaną większość codziennych potrzeb – ale gdy zajdzie potrzeba wyjścia poza to co da się wyklikać, z pomocą przychodzi Edytor Zaawansowany i język M. Każda operacja wykonana w UI jest w tle zapisywana właśnie jako kod M, co oznacza że możesz płynnie przechodzić między oboma światami.</p>
        <ul>
        <li>Pełna elastyczność – parametryzacja zapytań, funkcje własne, dynamiczne ścieżki plików, pętle</li>
        <li>Złożone transformacje warunkowe i wywołania API niedostępne z poziomu UI</li>
        <li>Kod M jest czytelny i dobrze udokumentowany – łatwo go modyfikować i rozbudowywać</li>
        <li>Nie umiesz kodować? Opisz transformację chatbotowi – wklej gotowy kod M bezpośrednio do edytora</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303145823.png?raw=true' width='100%'>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '2adb3687';
    var containerId = 'viz_' + vizId;

    var currentPage_2adb3687 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_2adb3687'] = function(n) {
        if (n > totalPages) currentPage_2adb3687 = totalPages;
        if (n < 1) currentPage_2adb3687 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_2adb3687 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_2adb3687;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_2adb3687 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_2adb3687 === totalPages);
    };

    window['changePage_2adb3687'] = function(n) {
        currentPage_2adb3687 += n;
        window['showPage_2adb3687'](currentPage_2adb3687);
    };

    // Inicjalizacja
    window['showPage_2adb3687'](1);

    // Funkcjonalność powiększania obrazów
    var images = container.querySelectorAll('img');
    images.forEach(function(img) {
        img.style.cursor = 'pointer';
        img.style.transition = 'transform 0.3s ease';

        img.addEventListener('click', function() {
            if (this.classList.contains('zoomed')) {
                // Pomniejsz obraz
                this.classList.remove('zoomed');
                this.style.position = '';
                this.style.top = '';
                this.style.left = '';
                this.style.transform = '';
                this.style.width = '100%';
                this.style.maxWidth = '';
                this.style.maxHeight = '';
                this.style.zIndex = '';
                this.style.backgroundColor = '';
                this.style.padding = '';
                this.style.boxShadow = '';
            } else {
                // Powiększ obraz
                this.classList.add('zoomed');
                this.style.position = 'fixed';
                this.style.top = '50%';
                this.style.left = '50%';
                this.style.transform = 'translate(-50%, -50%)';
                this.style.width = 'auto';
                this.style.maxWidth = '95vw';
                this.style.maxHeight = '95vh';
                this.style.zIndex = '9999';
                this.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
                this.style.padding = '10px';
                this.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
            }
        });
    });
})();
</script>

</body>
</html>

"
```
            lineageTag: 1d451156-c8ca-4405-9f07-0e5fcf011642

        measure '02. Działania na tabelach - Rozdział - to będzie osobna miara' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Rozdział - to będzie osobna miara</title>
    <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
    
            body {
                font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                font-size: 16px;
                font-weight: 400;
                line-height: 1.7;
                color: #333;
                background: transparent;
                padding: 20px;
            }
    
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: transparent;
                padding: 40px;
            }
    
            .navigation {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 40px;
                padding-bottom: 20px;
                border-bottom: 1px solid #e1e4e8;
            }
    
            button {
                background: #6b1718;
                color: white;
                border: none;
                padding: 12px 28px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 1em;
                font-weight: 500;
                transition: background 0.2s;
            }
    
            button:hover {
                background: #380c0c;
            }
    
            button:disabled {
                background: #ccc;
                cursor: not-allowed;
            }
    
            .page-indicator {
                color: #666;
                font-size: 1em;
            }
    
            .page {
                display: none;
                min-height: 500px;
            }
    
            .page.active {
                display: block;
                animation: fadeIn 0.3s ease-in;
            }
    
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
    
            h1 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin-bottom: 1em;
                color: #6b1718;
                border-bottom: 2px solid #6b1718;
            }
    
            h2 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin: 1.5em 0 0.8em 0;
                color: #1a1a1a;
                border-bottom: 2px solid #1a1a1a;
            }
    
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                padding-bottom: 5px;
                color: #444;
                border-bottom: 1px solid #999;
            }
    
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            code {
                background: #f5f5f5;
                padding: 3px 7px;
                border-radius: 3px;
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            pre code {
                background: none;
                padding: 0;
                color: #24292e;
                font-size: 1em;
                line-height: 1.6;
            }
    
            .dax-keyword {
                color: #6b1718;
                font-weight: 600;
            }
    
            .dax-function {
                color: #6f42c1;
            }
    
            .dax-number {
                color: #005cc5;
            }
    
            .dax-comment {
                color: #6a737d;
                font-style: italic;
            }
    
            ul, ol {
                margin: 0.3em 0;
                padding-left: 1.8em;
            }
    
            li {
                margin: 0;
                padding-left: 0.2em;
                font-size: 1.05em;
                line-height: 1.6;
            }
    
            ol {
                list-style-type: decimal;
            }
    
            ol li::marker {
                color: #999;
                font-weight: 400;
            }
    
            ul li::marker {
                color: #999;
            }
    
            ul ul, ol ol, ul ol, ol ul {
                margin: 0.2em 0;
                padding-left: 1.5em;
            }
    
            blockquote {
                border-left: 3px solid #6b1718;
                background: #f8f9fa;
                padding: 14px 18px;
                margin: 1em 0;
                color: #555;
                font-style: italic;
            }
    
            blockquote p {
                margin: 0;
            }
    
            .iteration-box {
                border-left: 3px solid #6b1718;
                padding: 14px 18px;
                margin: 0.8em 0;
            }
    
            .result-box {
                background: #f5f5f5;
                border-left: 3px solid #999;
                padding: 14px 18px;
                margin: 0.8em 0;
                font-weight: 500;
                color: #555;
                font-size: 1.05em;
            }
        </style>
</head>
<body>

<div class='container' id='viz_de38cd6a'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_de38cd6a' onclick='changePage_de38cd6a(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_de38cd6a'>1</span> z <span id='totalPages_de38cd6a'>2</span>
        </span>
        <button id='nextBtn_de38cd6a' onclick='changePage_de38cd6a(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Łączenie wertykalne - APPEND</h1>
        <p>Gdy te same dane przychodzą z wielu miejsc – osobne pliki na każdy miesiąc, arkusze na każdy oddział, raporty z różnych systemów – Append pozwala skleić je w jedną spójną tabelę. Działa jak UNION ALL w SQL: wiersze z kolejnych tabel są po prostu doklejane na dół.</p>
        <ul>
        <li>Łącz dowolną liczbę tabel o tej samej strukturze w jedną</li>
        <li>Kolumny są dopasowywane po nazwie – brakujące uzupełniane nullami</li>
        <li>Idealne do automatyzacji – dodaj nowy plik do folderu, dane pojawią się same po odświeżeniu</li>
        <li></li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303152152.png?raw=true' width='100%'>
        <h1>Łączenie horyzontalne - MERGE</h1>
        <p>Merge łączy dwie tabele na podstawie wspólnego klucza, wzbogacając jedną tabelę o kolumny z drugiej. Np. tabela sprzedaży + tabela klientów → pełny obraz transakcji z danymi nabywcy.</p>
        <ul>
        <li>Dostępne tryby: Left, Right, Inner, Full Outer, Left Anti, Right Anti Join</li>
        <li>Scalanie po jednej kolumnie kluczowej jednocześnie</li>
        <li>Wynik rozwijasz do wybranych kolumn – bierzesz tylko to, czego potrzebujesz</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303151207.png?raw=true' width='100%'>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Przekształcanie struktury tabeli</h1>
        <p>Pivot i Unpivot rozwiązują jeden z najczęstszych problemów z danymi – niedopasowanie struktury tabeli do potrzeb analizy.</p>
        <p><strong>Pivot</strong> – unikalne wartości z jednej kolumny stają się nagłówkami nowych kolumn. Np. kolumna ”Miesiąc” z wartościami Styczeń/Luty/Marzec → trzy osobne kolumny z wartościami sprzedaży</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303151901.png?raw=true' width='100%'>
        <p><strong>Unpivot</strong> – odwrotność: wiele kolumn spłaszczanych do dwóch – ”Atrybut” i ”Wartość”. Niezbędne przy pracy z danymi eksportowanymi z Excela w formacie szerokiej tabeli</p>
        <p>Oba są kluczowe przy przygotowaniu danych do modelu – Power BI wymaga danych w formacie długim (unpivoted)</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303151916.png?raw=true' width='100%'>
        <p>Transpose to operacja, która zamienia wiersze na kolumny i kolumny na wiersze – cała tabela zostaje obrócona o 90 stopni. Brzmi podobnie do Unpivot, ale to coś innego: Unpivot zmienia strukturę danych, Transpose zmienia wyłącznie ich orientację.</p>
        <p>Najczęstszy scenariusz to dane eksportowane z systemów lub Excela, gdzie nagłówki kolumn zostały zapisane w pierwszej kolumnie zamiast w pierwszym wierszu – po Transpose struktura wraca do normy i można dalej pracować z danymi standardowo.</p>
        <ul>
        <li>Jeden klik – cała tabela obrócona natychmiast</li>
        <li>Po Transpose zazwyczaj należy od razu użyć ”Use First Row as Headers” aby przywrócić nagłówki</li>
        <li>Przydatne przy importach z systemów finansowych, raportów księgowych i eksportów SAP gdzie dane często mają niestandardową orientację</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303151950.png?raw=true' width='100%'>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'de38cd6a';
    var containerId = 'viz_' + vizId;

    var currentPage_de38cd6a = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_de38cd6a'] = function(n) {
        if (n > totalPages) currentPage_de38cd6a = totalPages;
        if (n < 1) currentPage_de38cd6a = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_de38cd6a - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_de38cd6a;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_de38cd6a === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_de38cd6a === totalPages);
    };

    window['changePage_de38cd6a'] = function(n) {
        currentPage_de38cd6a += n;
        window['showPage_de38cd6a'](currentPage_de38cd6a);
    };

    // Inicjalizacja
    window['showPage_de38cd6a'](1);

    // Funkcjonalność powiększania obrazów
    var images = container.querySelectorAll('img');
    images.forEach(function(img) {
        img.style.cursor = 'pointer';
        img.style.transition = 'transform 0.3s ease';

        img.addEventListener('click', function() {
            if (this.classList.contains('zoomed')) {
                // Pomniejsz obraz
                this.classList.remove('zoomed');
                this.style.position = '';
                this.style.top = '';
                this.style.left = '';
                this.style.transform = '';
                this.style.width = '100%';
                this.style.maxWidth = '';
                this.style.maxHeight = '';
                this.style.zIndex = '';
                this.style.backgroundColor = '';
                this.style.padding = '';
                this.style.boxShadow = '';
            } else {
                // Powiększ obraz
                this.classList.add('zoomed');
                this.style.position = 'fixed';
                this.style.top = '50%';
                this.style.left = '50%';
                this.style.transform = 'translate(-50%, -50%)';
                this.style.width = 'auto';
                this.style.maxWidth = '95vw';
                this.style.maxHeight = '95vh';
                this.style.zIndex = '9999';
                this.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
                this.style.padding = '10px';
                this.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
            }
        });
    });
})();
</script>

</body>
</html>

"
```
            lineageTag: f73676a1-427a-4042-83e6-162ad8b67869

        measure '03. Język M - Wstęp' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Wstęp</title>
    <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
    
            body {
                font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                font-size: 16px;
                font-weight: 400;
                line-height: 1.7;
                color: #333;
                background: transparent;
                padding: 20px;
            }
    
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: transparent;
                padding: 40px;
            }
    
            .navigation {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 40px;
                padding-bottom: 20px;
                border-bottom: 1px solid #e1e4e8;
            }
    
            button {
                background: #6b1718;
                color: white;
                border: none;
                padding: 12px 28px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 1em;
                font-weight: 500;
                transition: background 0.2s;
            }
    
            button:hover {
                background: #380c0c;
            }
    
            button:disabled {
                background: #ccc;
                cursor: not-allowed;
            }
    
            .page-indicator {
                color: #666;
                font-size: 1em;
            }
    
            .page {
                display: none;
                min-height: 500px;
            }
    
            .page.active {
                display: block;
                animation: fadeIn 0.3s ease-in;
            }
    
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
    
            h1 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin-bottom: 1em;
                color: #6b1718;
                border-bottom: 2px solid #6b1718;
            }
    
            h2 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin: 1.5em 0 0.8em 0;
                color: #1a1a1a;
                border-bottom: 2px solid #1a1a1a;
            }
    
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                padding-bottom: 5px;
                color: #444;
                border-bottom: 1px solid #999;
            }
    
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            code {
                background: #f5f5f5;
                padding: 3px 7px;
                border-radius: 3px;
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            pre code {
                background: none;
                padding: 0;
                color: #24292e;
                font-size: 1em;
                line-height: 1.6;
            }
    
            .dax-keyword {
                color: #6b1718;
                font-weight: 600;
            }
    
            .dax-function {
                color: #6f42c1;
            }
    
            .dax-number {
                color: #005cc5;
            }
    
            .dax-comment {
                color: #6a737d;
                font-style: italic;
            }
    
            ul, ol {
                margin: 0.3em 0;
                padding-left: 1.8em;
            }
    
            li {
                margin: 0;
                padding-left: 0.2em;
                font-size: 1.05em;
                line-height: 1.6;
            }
    
            ol {
                list-style-type: decimal;
            }
    
            ol li::marker {
                color: #999;
                font-weight: 400;
            }
    
            ul li::marker {
                color: #999;
            }
    
            ul ul, ol ol, ul ol, ol ul {
                margin: 0.2em 0;
                padding-left: 1.5em;
            }
    
            blockquote {
                border-left: 3px solid #6b1718;
                background: #f8f9fa;
                padding: 14px 18px;
                margin: 1em 0;
                color: #555;
                font-style: italic;
            }
    
            blockquote p {
                margin: 0;
            }
    
            .iteration-box {
                border-left: 3px solid #6b1718;
                padding: 14px 18px;
                margin: 0.8em 0;
            }
    
            .result-box {
                background: #f5f5f5;
                border-left: 3px solid #999;
                padding: 14px 18px;
                margin: 0.8em 0;
                font-weight: 500;
                color: #555;
                font-size: 1.05em;
            }
        </style>
</head>
<body>

<div class='container' id='viz_2adb3687'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_2adb3687' onclick='changePage_2adb3687(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_2adb3687'>1</span> z <span id='totalPages_2adb3687'>2</span>
        </span>
        <button id='nextBtn_2adb3687' onclick='changePage_2adb3687(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Język M – co to jest i skąd się bierze?</h1>
        <p>Każda operacja wykonana w interfejsie graficznym Power Query ma swoje odzwierciedlenie w kodzie – tym kodem jest właśnie język M. Nie musisz go znać, żeby korzystać z Power Query, ale rozumienie jego podstaw otwiera zupełnie nowy poziom możliwości.</p>
        <p>M jest językiem funkcyjnym – opisujesz _co chcesz uzyskać_, a nie _jak to zrobić_ krok po kroku. Każde zapytanie to blok <code>let ... in</code>, gdzie między <code>let</code> a <code>in</code> definiujesz kolejne kroki transformacji oddzielone przecinkami, a po <code>in</code> wskazujesz który krok ma być wynikiem końcowym.</p>
        <pre><code>let
            Źródło = Excel.Workbook(...),
            #'Zmieniono typ' = Table.TransformColumnTypes(Źródło, ...),
            #'Przefiltrowane wiersze' = Table.SelectRows(#'Zmieniono typ', ...)
        in
            #'Przefiltrowane wiersze'</code></pre>
        <p>Kilka kluczowych rzeczy o składni:</p>
        <ul>
        <li>Każdy krok to <code>NazwaKroku = operacja(poprzedniKrok, ...)</code> – każdy krok odwołuje się do poprzedniego</li>
        <li>Kroki oddzielone są <strong>przecinkami</strong> – brak przecinka po ostatnim kroku przed <code>in</code></li>
        <li>Nazwy kroków ze spacjami lub polskimi znakami muszą być opakowane w <code>#”...”</code> – stąd charakterystyczne <code>#”Zmieniono typ”</code> generowane automatycznie przez UI</li>
        <li>Język M jest <strong>case-sensitive</strong> – <code>table</code> to nie to samo co <code>Table</code></li>
        <li>Kod M generuje się automatycznie podczas pracy w UI – możesz zacząć od klikania i tylko podglądać co powstaje w tle</li>
        <li>Nie umiesz kodować? Opisz transformację chatbotowi – wklej gotowy kod M bezpośrednio do edytora</li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Co przechowuje PQ?</h1>
        <p>Power Query nie jest magazynem danych – jest magazynem instrukcji. To fundamentalna rzecz, którą warto zrozumieć: Power Query przechowuje wyłącznie opis operacji do wykonania, a nie same dane. Dane fizycznie żyją w modelu semantycznym Power BI – Power Query jest tylko potokiem, przez który przepływają podczas odświeżania.</p>
        <p>To co widzisz w oknie Power Query – podgląd tabeli z wierszami i kolumnami – to nie są ”Twoje dane”. To jest wynik wykonania zapytania na próbce danych, wygenerowany wyłącznie po to, żebyś mógł zobaczyć efekt transformacji. Po zamknięciu edytora ten podgląd znika.</p>
        <p>Każda tabela w Power Query to osobne, choć może być zależne, zapytanie. Z tego wynika ważna konsekwencja:</p>
        <ul>
        <li>Jeśli masz dwie tabele oparte na tym samym źródle – Power Query odpyta to źródło <strong>dwukrotnie</strong>, osobno dla każdego zapytania</li>
        <li>Dane z jednego zapytania <strong>nie są współdzielone</strong> z drugim, nawet jeśli zapytania są identyczne</li>
        <li>Przy wielu tabelach opartych na tym samym źródle czas odświeżania rośnie liniowo – każde zapytanie to osobne połączenie ze źródłem</li>
        <li>Rozwiązaniem jest <strong>zapytanie bazowe</strong> – jedno zapytanie pobierające dane ze źródła, z którego kolejne zapytania dziedziczą przez referencję, a nie przez ponowne połączenie</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303201734.png?raw=true' width='100%'>
        <p><strong>Podgląd danych w edytorze – cache lokalny</strong></p>
        <p>Jest jednak jeden wyjątek od reguły ”Power Query nie przechowuje danych”. Podczas pracy w edytorze Power Query zapisuje tymczasowy cache podglądu lokalnie na dysku komputera. Dzięki temu po ponownym otwarciu edytora widzisz dane w tabelach natychmiast – bez konieczności ponownego odpytywania źródła.</p>
        <p>To wygodne, ale może prowadzić do nieporozumień:</p>
        <ul>
        <li>Podgląd w edytorze może pokazywać <strong>nieaktualne dane</strong> – cache nie jest odświeżany automatycznie przy każdym otwarciu</li>
        <li>Jeśli źródło danych zmieniło się od ostatniego pobrania, edytor nadal pokaże stary podgląd</li>
        <li>Cache można ręcznie odświeżyć przyciskiem <strong>Refresh Preview</strong> – dopiero wtedy Power Query ponownie odpyta źródło</li>
        <li>Cache podglądu to wyłącznie narzędzie deweloperskie – nie ma żadnego wpływu na dane ładowane do modelu Power BI podczas właściwego odświeżania raportu</li>
        </ul>
        <p>Dlatego warto pamiętać: to co widzisz w edytorze podczas pracy, niekoniecznie odzwierciedla aktualny stan źródła danych.</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '2adb3687';
    var containerId = 'viz_' + vizId;

    var currentPage_2adb3687 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_2adb3687'] = function(n) {
        if (n > totalPages) currentPage_2adb3687 = totalPages;
        if (n < 1) currentPage_2adb3687 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_2adb3687 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_2adb3687;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_2adb3687 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_2adb3687 === totalPages);
    };

    window['changePage_2adb3687'] = function(n) {
        currentPage_2adb3687 += n;
        window['showPage_2adb3687'](currentPage_2adb3687);
    };

    // Inicjalizacja
    window['showPage_2adb3687'](1);

    // Funkcjonalność powiększania obrazów
    var images = container.querySelectorAll('img');
    images.forEach(function(img) {
        img.style.cursor = 'pointer';
        img.style.transition = 'transform 0.3s ease';

        img.addEventListener('click', function() {
            if (this.classList.contains('zoomed')) {
                // Pomniejsz obraz
                this.classList.remove('zoomed');
                this.style.position = '';
                this.style.top = '';
                this.style.left = '';
                this.style.transform = '';
                this.style.width = '100%';
                this.style.maxWidth = '';
                this.style.maxHeight = '';
                this.style.zIndex = '';
                this.style.backgroundColor = '';
                this.style.padding = '';
                this.style.boxShadow = '';
            } else {
                // Powiększ obraz
                this.classList.add('zoomed');
                this.style.position = 'fixed';
                this.style.top = '50%';
                this.style.left = '50%';
                this.style.transform = 'translate(-50%, -50%)';
                this.style.width = 'auto';
                this.style.maxWidth = '95vw';
                this.style.maxHeight = '95vh';
                this.style.zIndex = '9999';
                this.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
                this.style.padding = '10px';
                this.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
            }
        });
    });
})();
</script>

</body>
</html>

"
```
            lineageTag: b8ddd9ae-b7a9-4558-bb3a-fc0866b9ed9f

        measure '04. Edytowanie kodu M - Przykład 1 - Kolumna warunkowa' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Przykład 1 - Kolumna warunkowa</title>
    <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
    
            body {
                font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                font-size: 16px;
                font-weight: 400;
                line-height: 1.7;
                color: #333;
                background: transparent;
                padding: 20px;
            }
    
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: transparent;
                padding: 40px;
            }
    
            .navigation {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 40px;
                padding-bottom: 20px;
                border-bottom: 1px solid #e1e4e8;
            }
    
            button {
                background: #6b1718;
                color: white;
                border: none;
                padding: 12px 28px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 1em;
                font-weight: 500;
                transition: background 0.2s;
            }
    
            button:hover {
                background: #380c0c;
            }
    
            button:disabled {
                background: #ccc;
                cursor: not-allowed;
            }
    
            .page-indicator {
                color: #666;
                font-size: 1em;
            }
    
            .page {
                display: none;
                min-height: 500px;
            }
    
            .page.active {
                display: block;
                animation: fadeIn 0.3s ease-in;
            }
    
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
    
            h1 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin-bottom: 1em;
                color: #6b1718;
                border-bottom: 2px solid #6b1718;
            }
    
            h2 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin: 1.5em 0 0.8em 0;
                color: #1a1a1a;
                border-bottom: 2px solid #1a1a1a;
            }
    
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                padding-bottom: 5px;
                color: #444;
                border-bottom: 1px solid #999;
            }
    
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            code {
                background: #f5f5f5;
                padding: 3px 7px;
                border-radius: 3px;
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            pre code {
                background: none;
                padding: 0;
                color: #24292e;
                font-size: 1em;
                line-height: 1.6;
            }
    
            .dax-keyword {
                color: #6b1718;
                font-weight: 600;
            }
    
            .dax-function {
                color: #6f42c1;
            }
    
            .dax-number {
                color: #005cc5;
            }
    
            .dax-comment {
                color: #6a737d;
                font-style: italic;
            }
    
            ul, ol {
                margin: 0.3em 0;
                padding-left: 1.8em;
            }
    
            li {
                margin: 0;
                padding-left: 0.2em;
                font-size: 1.05em;
                line-height: 1.6;
            }
    
            ol {
                list-style-type: decimal;
            }
    
            ol li::marker {
                color: #999;
                font-weight: 400;
            }
    
            ul li::marker {
                color: #999;
            }
    
            ul ul, ol ol, ul ol, ol ul {
                margin: 0.2em 0;
                padding-left: 1.5em;
            }
    
            blockquote {
                border-left: 3px solid #6b1718;
                background: #f8f9fa;
                padding: 14px 18px;
                margin: 1em 0;
                color: #555;
                font-style: italic;
            }
    
            blockquote p {
                margin: 0;
            }
    
            .iteration-box {
                border-left: 3px solid #6b1718;
                padding: 14px 18px;
                margin: 0.8em 0;
            }
    
            .result-box {
                background: #f5f5f5;
                border-left: 3px solid #999;
                padding: 14px 18px;
                margin: 0.8em 0;
                font-weight: 500;
                color: #555;
                font-size: 1.05em;
            }
        </style>
</head>
<body>

<div class='container' id='viz_7a830c0c'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_7a830c0c' onclick='changePage_7a830c0c(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_7a830c0c'>1</span> z <span id='totalPages_7a830c0c'>4</span>
        </span>
        <button id='nextBtn_7a830c0c' onclick='changePage_7a830c0c(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Tworzenie nowej kwerendy i odwołanie do tabeli</h1>
        <p>Na początek utwórzmy nową kwerendę ”New Query”, żeby utworzyć obiekt, w którym będziemy pisać kod M.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303184759.png?raw=true' width='100%'>
        <p>W utworzonym obiekcie możemy od razu zadeklarować odwołanie do istniejącej tabeli o nazwie <code>tabela_sprzedazy</code> — wystarczy przypisać ją do jedynego kroku w bloku <code>let...in</code>. Zauważ, że ten sam krok jest jednocześnie zwracany, ponieważ pojawia się po słowie kluczowym <code>in</code>.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303184728.png?raw=true' width='100%'>
        <h1>Dodawanie kolumn przez interfejs użytkownika</h1>
        <p>Załóżmy, że chcemy policzyć rabaty naliczane dla klientów w odpowiednich okresach. Jeżeli wartość transakcji przekroczy określony próg w danym miesiącu (np. 1500 zł), chcemy oznaczyć, że przy następnej transakcji klient otrzyma rabat na ten sam zakup. Niestety, nasza tabela zawiera jedynie podstawowe informacje: datę, nazwę klienta, cenę oraz liczbę transakcji.</p>
        <p>Korzystając z interfejsu Power Query, możemy dodać nowe kolumny: Sprzedaży, Kosztów, Zysku i Rabatu. Można to zrobić na dwa sposoby — używając wstążki ”Add Column” lub przycisku w lewym górnym rogu tabeli.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303185041.png?raw=true' width='100%'>
        <p>Po prawej stronie modułu ”Custom Column” dostępne są już nazwy kolumn — możemy je dodawać do edytora zamiast ręcznie przepisywać. Wystarczy dopisać jedynie operację, którą chcemy wykonać. W tym przypadku jest to iloczyn, czyli znak <code>*</code>.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303193152.png?raw=true' width='100%'>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Edycja kodu w Advanced Editorze</h1>
        <p>Dodawanie wielu kolumn przez interfejs może być żmudne. Dlatego warto uruchomić Advanced Editor i po prostu skopiować istniejący krok.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303185401.png?raw=true' width='100%'>
        <p>Dzięki skopiowaniu mamy już <strong>szkielet</strong> operacji dodania nowej kolumny. Dostosujmy go teraz do naszego przykładu — obliczenia kosztu. Na poniższym obrazie dobrze widać, za co odpowiadają kolejne elementy kodu. Na zielono oznaczone są komentarze (znak <code>//</code> wyłącza kod w danej linii, od miejsca wystąpienia do końca wiersza).</p>
        <p>Aby dodać nową kolumnę, należy edytować:</p>
        <ul>
        <li><strong>Nazwę nowego kroku</strong> — dowolna nazwa, która pomaga zrozumieć sekwencję kroków bez zagłębiania się w kod.</li>
        <li><strong>Obiekt i metodę</strong> — można je traktować jako dwuczłonową nazwę funkcji. Pierwszy człon odwołuje się do obiektu (np. <code>Table</code>), a drugi do akcji (np. <code>AddColumn</code>).</li>
        <li><strong>Pierwszy argument</strong> — dla metod tabelarycznych jest to zazwyczaj nazwa poprzedniego kroku. Ponieważ kroki są sekwencyjne (od góry do dołu), w 99% przypadków pierwszym argumentem jest krok bezpośrednio poprzedzający.</li>
        <li><strong>Nazwę kolumny</strong> — po prostu nazwa nowej kolumny 🙂</li>
        <li><strong>Operację</strong> — słowo kluczowe <code>each</code> oznacza, że działamy na poziomie pojedynczych wierszy. Odwołując się do nazw kolumn, sięgamy do konkretnych wartości w tabeli (analogicznie do komórek w Excelu). <code>each</code> można rozumieć jako ”<strong>dla każdego</strong> wiersza”.</li>
        </ul>
        <p>> <strong>⚠️ Ważne!</strong> Początkujący często o tym zapominają — jeżeli dodajesz nowy krok, musisz zaktualizować nazwę, do której odwołuje się następny krok. Dotyczy to również nazwy zwracanej przez <code>in</code>.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303190856.png?raw=true' width='100%'>
        <h1>Naliczanie rabatu — kolumna warunkowa</h1>
        <p>Mamy już obliczony Zysk. Pora napisać formułę dla ”Conditional Column” z użyciem edytora UI.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303191159.png?raw=true' width='100%'>
        <p>Jest jednak pewne ograniczenie — w edytorze jako ”Output” można zwrócić wyłącznie:</p>
        <ul>
        <li>wartości statyczne (”na sztywno”),</li>
        <li>całe kolumny,</li>
        <li>parametr.</li>
        </ul>
        <p>Żadna z tych opcji nie pozwoli na dynamiczne wygenerowanie wartości w stylu ”10% Michał K.”.</p>
        <h1>Column From Examples — AI w służbie kodu M</h1>
        <p>Zacznijmy od utworzenia osobnej kolumny. Tym razem użyjemy funkcji ”Column From Examples” z opcją ”From Selection”. Aktywuje to wbudowany model AI, który generuje kod M na podstawie zaznaczonych danych. Pamiętaj, że przed użyciem tej opcji musisz <strong>zaznaczyć kolumny</strong>, które Cię interesują — w tym przypadku imię i nazwisko klienta.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303191921.png?raw=true' width='100%'>
        <p>Wystarczy ręcznie wpisać kilka przykładowych wartości, aby algorytm ”załapał”, o co nam chodzi. Wpisanie samego ”Dorota N.” może nie wystarczyć — algorytm znajdzie imię ”Dorota”, ale nie domyśli się od razu, że ”N.” pochodzi od pierwszej litery nazwiska, i prawdopodobnie przypisze ”N.” wszystkim wierszom. Dopiero wpisanie drugiego przykładu, np. ”Łukasz Z.”, daje mu wystarczający kontekst, aby wywnioskować: ”aha, to pierwsza litera z kolumny z nazwiskiem, zakończona kropką”.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303195625.png?raw=true' width='100%'>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Łączenie kolumny warunkowej z dynamiczną wartością</h1>
        <p>Teraz najlepsza część! Mając gotowy kod generujący nową kolumnę, możemy go skopiować i wkleić jako wartość zwracaną przez kolumnę warunkową.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303192519.png?raw=true' width='100%'>
        <p>I gotowe! Nie znając wszystkich funkcji Power Query — operując jedynie na szkielecie kodu — jesteśmy w stanie tworzyć naprawdę zaawansowaną logikę biznesową.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303192422.png?raw=true' width='100%'>
        <h1>Łączenie warunków — operator <code>and</code></h1>
        <p>Co jeśli chcemy zawęzić logikę rabatu do konkretnego roku? Wystarczy rozszerzyć warunek o dodatkowe kryterium, łącząc je operatorem <code>and</code>:</p>
        <pre><code>and Date.Year([Data Sprzedaży]) = 2023</code></pre>
        <p>Operator <code>and</code> sprawia, że rabat zostanie przyznany tylko wtedy, gdy <strong>oba</strong> warunki są spełnione jednocześnie — czyli zysk przekracza 1500 zł <strong>oraz</strong> transakcja pochodzi z roku 2023.</p>
        <p>Do wyciągnięcia roku z kolumny z datą służy funkcja <code>Date.Year()</code>, która przyjmuje jako argument wartość typu <code>date</code> i zwraca liczbę całkowitą. Analogicznie działają <code>Date.Month()</code> oraz <code>Date.Day()</code> — przydatne, gdy chcesz filtrować dane np. po kwartałach czy konkretnych dniach.</p>
        <p>Jeśli chcesz, żeby wystarczył <strong>jeden</strong> z warunków zamiast oba, zamień <code>and</code> na <code>or</code>.</p>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>Zanim zaczniesz — kilka przydatnych wskazówek</h1>
        <ul>
        <li>Edytor stara się podpowiadać podczas pisania kodu — wystarczy wpisać np. <code>Table</code>, aby wyświetlić listę wszystkich dostępnych metod dla obiektu tabeli.</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303194543.png?raw=true' width='100%'>
        <ul>
        <li>Po najechaniu kursorem na metodę w kodzie możesz zobaczyć podgląd jej składni.</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303194547.png?raw=true' width='100%'>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '7a830c0c';
    var containerId = 'viz_' + vizId;

    var currentPage_7a830c0c = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_7a830c0c'] = function(n) {
        if (n > totalPages) currentPage_7a830c0c = totalPages;
        if (n < 1) currentPage_7a830c0c = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_7a830c0c - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_7a830c0c;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_7a830c0c === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_7a830c0c === totalPages);
    };

    window['changePage_7a830c0c'] = function(n) {
        currentPage_7a830c0c += n;
        window['showPage_7a830c0c'](currentPage_7a830c0c);
    };

    // Inicjalizacja
    window['showPage_7a830c0c'](1);

    // Funkcjonalność powiększania obrazów
    var images = container.querySelectorAll('img');
    images.forEach(function(img) {
        img.style.cursor = 'pointer';
        img.style.transition = 'transform 0.3s ease';

        img.addEventListener('click', function() {
            if (this.classList.contains('zoomed')) {
                // Pomniejsz obraz
                this.classList.remove('zoomed');
                this.style.position = '';
                this.style.top = '';
                this.style.left = '';
                this.style.transform = '';
                this.style.width = '100%';
                this.style.maxWidth = '';
                this.style.maxHeight = '';
                this.style.zIndex = '';
                this.style.backgroundColor = '';
                this.style.padding = '';
                this.style.boxShadow = '';
            } else {
                // Powiększ obraz
                this.classList.add('zoomed');
                this.style.position = 'fixed';
                this.style.top = '50%';
                this.style.left = '50%';
                this.style.transform = 'translate(-50%, -50%)';
                this.style.width = 'auto';
                this.style.maxWidth = '95vw';
                this.style.maxHeight = '95vh';
                this.style.zIndex = '9999';
                this.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
                this.style.padding = '10px';
                this.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
            }
        });
    });
})();
</script>

</body>
</html>

"
```
            lineageTag: a429faf6-5101-407b-a39d-630b11cc6748

        measure '05. Bufforwanie Tabel - Przykład 2' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Przykład 2</title>
    <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
    
            body {
                font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                font-size: 16px;
                font-weight: 400;
                line-height: 1.7;
                color: #333;
                background: transparent;
                padding: 20px;
            }
    
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: transparent;
                padding: 40px;
            }
    
            .navigation {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 40px;
                padding-bottom: 20px;
                border-bottom: 1px solid #e1e4e8;
            }
    
            button {
                background: #6b1718;
                color: white;
                border: none;
                padding: 12px 28px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 1em;
                font-weight: 500;
                transition: background 0.2s;
            }
    
            button:hover {
                background: #380c0c;
            }
    
            button:disabled {
                background: #ccc;
                cursor: not-allowed;
            }
    
            .page-indicator {
                color: #666;
                font-size: 1em;
            }
    
            .page {
                display: none;
                min-height: 500px;
            }
    
            .page.active {
                display: block;
                animation: fadeIn 0.3s ease-in;
            }
    
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
    
            h1 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin-bottom: 1em;
                color: #6b1718;
                border-bottom: 2px solid #6b1718;
            }
    
            h2 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin: 1.5em 0 0.8em 0;
                color: #1a1a1a;
                border-bottom: 2px solid #1a1a1a;
            }
    
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                padding-bottom: 5px;
                color: #444;
                border-bottom: 1px solid #999;
            }
    
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            code {
                background: #f5f5f5;
                padding: 3px 7px;
                border-radius: 3px;
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            pre code {
                background: none;
                padding: 0;
                color: #24292e;
                font-size: 1em;
                line-height: 1.6;
            }
    
            .dax-keyword {
                color: #6b1718;
                font-weight: 600;
            }
    
            .dax-function {
                color: #6f42c1;
            }
    
            .dax-number {
                color: #005cc5;
            }
    
            .dax-comment {
                color: #6a737d;
                font-style: italic;
            }
    
            ul, ol {
                margin: 0.3em 0;
                padding-left: 1.8em;
            }
    
            li {
                margin: 0;
                padding-left: 0.2em;
                font-size: 1.05em;
                line-height: 1.6;
            }
    
            ol {
                list-style-type: decimal;
            }
    
            ol li::marker {
                color: #999;
                font-weight: 400;
            }
    
            ul li::marker {
                color: #999;
            }
    
            ul ul, ol ol, ul ol, ol ul {
                margin: 0.2em 0;
                padding-left: 1.5em;
            }
    
            blockquote {
                border-left: 3px solid #6b1718;
                background: #f8f9fa;
                padding: 14px 18px;
                margin: 1em 0;
                color: #555;
                font-style: italic;
            }
    
            blockquote p {
                margin: 0;
            }
    
            .iteration-box {
                border-left: 3px solid #6b1718;
                padding: 14px 18px;
                margin: 0.8em 0;
            }
    
            .result-box {
                background: #f5f5f5;
                border-left: 3px solid #999;
                padding: 14px 18px;
                margin: 0.8em 0;
                font-weight: 500;
                color: #555;
                font-size: 1.05em;
            }
        </style>
</head>
<body>

<div class='container' id='viz_e8d6168a'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_e8d6168a' onclick='changePage_e8d6168a(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_e8d6168a'>1</span> z <span id='totalPages_e8d6168a'>4</span>
        </span>
        <button id='nextBtn_e8d6168a' onclick='changePage_e8d6168a(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h2>Filtrowanie sprzedaży do aktywnych sklepów raportujących</h2>
        <p>Kierownicy sklepów chcą widzieć w raporcie Power BI <strong>tylko te sklepy, które zostały zatwierdzone do raportowania</strong> — czyli nowo otwarte lub tymczasowo wyłączone oddziały nie powinny zaburzać analiz. Tabela <code>sklep_raportowania</code> pełni rolę ”białej listy” sklepów aktywnych.</p>
        <p>Do podstawowej kwerendy:</p>
        <pre><code>let
            Source = tabela_sprzedazy
        in
            Source</code></pre>
        <p>Dodajmy nowy krok, który pobierze listę sklepów - wartości z kolumny <code>Whitelist Sklepów</code> tabeli <code>sklepy_raportowanie</code></p>
        <pre><code>let
            Source = tabela_sprzedazy,
            AktywneSklepyLista = sklepy_raportowanie[Whitelist Sklepów]
        in
            AktywneSklepyLista</code></pre>
        <p>Teraz wystarczy dodać prostą formułę, która sprawdza czy wartość z listy zawiera się w wartości z tabeli.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303204222.png?raw=true' width='100%'>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>Bez buffera — wolno</h2>
        <pre><code>let
            Source = tabela_sprzedazy,
            AktywneSklepyLista = sklepy_raportowanie[Whitelist Sklepów],  // odczyt przy KAŻDYM wierszu

            #'Dodaj flagę' = Table.AddColumn(Source, 'Aktywny w raporcie', 
                each List.Contains(AktywneSklepyLista, [Nazwa Sklepu])
            )
        in
            #'Dodaj flagę'</code></pre>
        <p><code>List.Contains</code> odpytuje <code>sklep_raportowania</code> dla każdego wiersza <code>tabela_sprzedazy</code> — przy 100k wierszach to 100k odczytów.</p>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Z List.Buffer — szybko</h2>
        <pre><code>let
            Source = tabela_sprzedazy,
            AktywneSklepyLista = List.Buffer(sklepy_raportowanie[Whitelist Sklepów]),  // raz do pamięci

            #'Dodaj flagę' = Table.AddColumn(Source, 'Aktywny w raporcie', 
                each List.Contains(AktywneSklepyLista, [Nazwa Sklepu])
            )
        in
            #'Dodaj flagę'</code></pre>
        <p>Jedna zmiana — <code>List.Buffer</code> — a lista <code>Whitelist Sklepów</code> jest wczytywana <strong>raz do pamięci</strong> i re-używana dla każdego wiersza.</p>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>Dlaczego to ma sens w Power BI?</h2>
        <p>Kolumna <code>Aktywny w raporcie</code> jako <code>true/false</code> jest w modelu użyteczna — kierownik może w raporcie <strong>samodzielnie przełączać</strong> widok między wszystkimi sklepami a tylko aktywnymi, bez konieczności tworzenia dwóch osobnych miar w DAX. Buffer sprawia, że ta kolumna nie spowalnia odświeżania.</p>
        <p>Natomiast, jeżeli chciałbym po prostu odfiltrować wiersze dynamicznie - w takim przypadku lepiej dokonać operacji <code>Merge</code> na obu tabelach za pomocą <code>INNER JOIN</code> - to nic innego jak znalezienie wartości wspólnych dla obu tabel :). Taka metoda jest na tylne popularna, że ten rodzaj tabeli ma nawet swoją własną nazwę - <strong>junk dimension</strong> (wymiar śmietnikowy). To tabela, która grupuje w sobie różne flagi i wskaźniki o niskiej kardynalności, które nie pasują do żadnego innego wymiaru — zamiast tworzyć osobną tabelę dla każdej flagi, zbieramy je wszystkie w jednym miejscu. </p>
        <p>Częstym scenariuszem jest również, że taka tabela później trafia do samego modelu. Wtedy, tabela typu JUNK DIMENSION filtruje standardowy DIMENSION, a następnie FACT TABLE.</p>
        <p>Fascynujące, jak Power BI potrafi zaoferować masę sposobów na ten sam problem. Natomiast, każdy z tych sposobów ma swoje wady i zalety. O metodzie decyduje przede wszystkim problem biznesowy, w dalszej kolejności technologia (wielkość tabel, kardynalność, częstość aktualizacji).</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'e8d6168a';
    var containerId = 'viz_' + vizId;

    var currentPage_e8d6168a = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_e8d6168a'] = function(n) {
        if (n > totalPages) currentPage_e8d6168a = totalPages;
        if (n < 1) currentPage_e8d6168a = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_e8d6168a - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_e8d6168a;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_e8d6168a === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_e8d6168a === totalPages);
    };

    window['changePage_e8d6168a'] = function(n) {
        currentPage_e8d6168a += n;
        window['showPage_e8d6168a'](currentPage_e8d6168a);
    };

    // Inicjalizacja
    window['showPage_e8d6168a'](1);

    // Funkcjonalność powiększania obrazów
    var images = container.querySelectorAll('img');
    images.forEach(function(img) {
        img.style.cursor = 'pointer';
        img.style.transition = 'transform 0.3s ease';

        img.addEventListener('click', function() {
            if (this.classList.contains('zoomed')) {
                // Pomniejsz obraz
                this.classList.remove('zoomed');
                this.style.position = '';
                this.style.top = '';
                this.style.left = '';
                this.style.transform = '';
                this.style.width = '100%';
                this.style.maxWidth = '';
                this.style.maxHeight = '';
                this.style.zIndex = '';
                this.style.backgroundColor = '';
                this.style.padding = '';
                this.style.boxShadow = '';
            } else {
                // Powiększ obraz
                this.classList.add('zoomed');
                this.style.position = 'fixed';
                this.style.top = '50%';
                this.style.left = '50%';
                this.style.transform = 'translate(-50%, -50%)';
                this.style.width = 'auto';
                this.style.maxWidth = '95vw';
                this.style.maxHeight = '95vh';
                this.style.zIndex = '9999';
                this.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
                this.style.padding = '10px';
                this.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
            }
        });
    });
})();
</script>

</body>
</html>

"
```
            lineageTag: 501cf140-f6a2-41cc-81da-33d9f75a457f

        measure '06. Akumulacja progów - Przykład 3' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Przykład 3</title>
    <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
    
            body {
                font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                font-size: 16px;
                font-weight: 400;
                line-height: 1.7;
                color: #333;
                background: transparent;
                padding: 20px;
            }
    
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: transparent;
                padding: 40px;
            }
    
            .navigation {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 40px;
                padding-bottom: 20px;
                border-bottom: 1px solid #e1e4e8;
            }
    
            button {
                background: #6b1718;
                color: white;
                border: none;
                padding: 12px 28px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 1em;
                font-weight: 500;
                transition: background 0.2s;
            }
    
            button:hover {
                background: #380c0c;
            }
    
            button:disabled {
                background: #ccc;
                cursor: not-allowed;
            }
    
            .page-indicator {
                color: #666;
                font-size: 1em;
            }
    
            .page {
                display: none;
                min-height: 500px;
            }
    
            .page.active {
                display: block;
                animation: fadeIn 0.3s ease-in;
            }
    
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
    
            h1 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin-bottom: 1em;
                color: #6b1718;
                border-bottom: 2px solid #6b1718;
            }
    
            h2 {
                font-size: 26px;
                line-height: 36px;
                font-weight: 600;
                padding-top: 14px;
                padding-bottom: 6px;
                margin: 1.5em 0 0.8em 0;
                color: #1a1a1a;
                border-bottom: 2px solid #1a1a1a;
            }
    
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                padding-bottom: 5px;
                color: #444;
                border-bottom: 1px solid #999;
            }
    
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            code {
                background: #f5f5f5;
                padding: 3px 7px;
                border-radius: 3px;
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            pre code {
                background: none;
                padding: 0;
                color: #24292e;
                font-size: 1em;
                line-height: 1.6;
            }
    
            .dax-keyword {
                color: #6b1718;
                font-weight: 600;
            }
    
            .dax-function {
                color: #6f42c1;
            }
    
            .dax-number {
                color: #005cc5;
            }
    
            .dax-comment {
                color: #6a737d;
                font-style: italic;
            }
    
            ul, ol {
                margin: 0.3em 0;
                padding-left: 1.8em;
            }
    
            li {
                margin: 0;
                padding-left: 0.2em;
                font-size: 1.05em;
                line-height: 1.6;
            }
    
            ol {
                list-style-type: decimal;
            }
    
            ol li::marker {
                color: #999;
                font-weight: 400;
            }
    
            ul li::marker {
                color: #999;
            }
    
            ul ul, ol ol, ul ol, ol ul {
                margin: 0.2em 0;
                padding-left: 1.5em;
            }
    
            blockquote {
                border-left: 3px solid #6b1718;
                background: #f8f9fa;
                padding: 14px 18px;
                margin: 1em 0;
                color: #555;
                font-style: italic;
            }
    
            blockquote p {
                margin: 0;
            }
    
            .iteration-box {
                border-left: 3px solid #6b1718;
                padding: 14px 18px;
                margin: 0.8em 0;
            }
    
            .result-box {
                background: #f5f5f5;
                border-left: 3px solid #999;
                padding: 14px 18px;
                margin: 0.8em 0;
                font-weight: 500;
                color: #555;
                font-size: 1.05em;
            }
        </style>
</head>
<body>

<div class='container' id='viz_f2afad41'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_f2afad41' onclick='changePage_f2afad41(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_f2afad41'>1</span> z <span id='totalPages_f2afad41'>2</span>
        </span>
        <button id='nextBtn_f2afad41' onclick='changePage_f2afad41(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Narastające progi rabatowe z <code>List.Accumulate</code></h1>
        <p>Analitycy sprzedaży chcą przyznawać klientom rabaty na podstawie <strong>łącznej wartości zakupów w danym miesiącu</strong> — im więcej klient wydał, tym wyższy rabat otrzymuje na kolejną transakcję. Progi są konfigurowalne i trzymane w osobnej tabeli <code>progi_rabatowe</code>.</p>
        <p>Do podstawowej kwerendy:</p>
        <pre><code>let
            Source = tabela_sprzedazy
        in
            Source</code></pre>
        <p>Dodajmy listę progów z tabeli <code>progi_rabatowe</code>, która zawiera kolumnę <code>Próg</code> z wartościami np. <code>{500, 1000, 2000, 5000}</code>:</p>
        <pre><code>let
            Source = tabela_sprzedazy,
            ListaProgow = progi_rabatowe[Próg]
        in
            ListaProgow</code></pre>
        <p>Teraz dla każdego wiersza chcemy sprawdzić, <strong>który próg został przekroczony</strong> — czyli iterować po liście progów i zatrzymać się na ostatnim przekroczonym.</p>
        <p><strong>Bez <code>List.Accumulate</code> — niewygodnie</strong></p>
        <p>Można by to zrobić zagnieżdżonymi <code>if...then...else</code>, ale przy 4+ progach kod staje się nieczytelny i nieelastyczny — każda zmiana progu wymaga edycji kodu.</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <p><strong>Z <code>List.Accumulate</code> — elegancko</strong></p>
        <pre><code>let
            Source = tabela_sprzedazy,
            ListaProgow = List.Buffer(progi_rabatowe[Próg]),

            #'Dodaj rabat' = Table.AddColumn(Source, 'Kwota Rabatu',
                each List.Accumulate(
                    ListaProgow,
                    0,
                    (stan, prog) =&gt; if ([Ilość] * [Cena Jednostkowa]) &gt;= prog then prog * 0.05 else stan
                )
            )
        in
            #'Dodaj rabat'</code></pre>
        <p><code>List.Accumulate</code> przechodzi po każdym progu i aktualizuje <code>stan</code> — na końcu iteracji <code>stan</code> zawiera <strong>najwyższy przekroczony próg</strong>. Jeśli klient nie przekroczył żadnego, zwracane jest <code>0</code>.</p>
        <p><strong>Dlaczego to ma sens w Power BI?</strong></p>
        <p>Kolumna <code>Próg Rabatowy</code> trafia do modelu jako liczba — można na jej podstawie stworzyć prostą miarę DAX przypisującą konkretny procent rabatu. Co ważniejsze, progi są zarządzane przez tabelę <code>progi_rabatowe</code>, którą biznes może aktualizować <strong>bez ingerencji w kod Power Query</strong>.</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'f2afad41';
    var containerId = 'viz_' + vizId;

    var currentPage_f2afad41 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_f2afad41'] = function(n) {
        if (n > totalPages) currentPage_f2afad41 = totalPages;
        if (n < 1) currentPage_f2afad41 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_f2afad41 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_f2afad41;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_f2afad41 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_f2afad41 === totalPages);
    };

    window['changePage_f2afad41'] = function(n) {
        currentPage_f2afad41 += n;
        window['showPage_f2afad41'](currentPage_f2afad41);
    };

    // Inicjalizacja
    window['showPage_f2afad41'](1);

    // Funkcjonalność powiększania obrazów
    var images = container.querySelectorAll('img');
    images.forEach(function(img) {
        img.style.cursor = 'pointer';
        img.style.transition = 'transform 0.3s ease';

        img.addEventListener('click', function() {
            if (this.classList.contains('zoomed')) {
                // Pomniejsz obraz
                this.classList.remove('zoomed');
                this.style.position = '';
                this.style.top = '';
                this.style.left = '';
                this.style.transform = '';
                this.style.width = '100%';
                this.style.maxWidth = '';
                this.style.maxHeight = '';
                this.style.zIndex = '';
                this.style.backgroundColor = '';
                this.style.padding = '';
                this.style.boxShadow = '';
            } else {
                // Powiększ obraz
                this.classList.add('zoomed');
                this.style.position = 'fixed';
                this.style.top = '50%';
                this.style.left = '50%';
                this.style.transform = 'translate(-50%, -50%)';
                this.style.width = 'auto';
                this.style.maxWidth = '95vw';
                this.style.maxHeight = '95vh';
                this.style.zIndex = '9999';
                this.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
                this.style.padding = '10px';
                this.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
            }
        });
    });
})();
</script>

</body>
</html>

"
```
            lineageTag: fc5fcc9e-d2f3-462f-9b6f-444db0e27aae

        partition _HTML = m
            mode: import
            source =
                    let
                        Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [HTML = _t]),
                        #"Removed Columns" = Table.RemoveColumns(Source,{"HTML"})
                    in
                        #"Removed Columns"

        annotation PBI_ResultType = Table

        annotation PBI_NavigationStepName = Navigation

