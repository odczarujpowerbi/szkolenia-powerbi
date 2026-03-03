createOrReplace

    table _HTML
        lineageTag: 1f129d25-e7fb-4d69-8468-fabac5e8d996

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
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020260303145812.png|693?raw=true' width='100%'>
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
            lineageTag: d0ef8eaf-fcb6-41e6-9108-f6a6e44543e2

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
            lineageTag: f41305ef-595a-4db8-bcb8-e1f4fcff2f60

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
        <p>Każda tabela w Power Query to osobne, niezależne zapytanie. Z tego wynika ważna konsekwencja:</p>
        <ul>
        <li>Jeśli masz dwie tabele oparte na tym samym źródle – Power Query odpyta to źródło <strong>dwukrotnie</strong>, osobno dla każdego zapytania</li>
        <li>Dane z jednego zapytania <strong>nie są współdzielone</strong> z drugim, nawet jeśli zapytania są identyczne</li>
        <li>Przy wielu tabelach opartych na tym samym źródle czas odświeżania rośnie liniowo – każde zapytanie to osobne połączenie ze źródłem</li>
        <li>Rozwiązaniem jest <strong>zapytanie bazowe</strong> – jedno zapytanie pobierające dane ze źródła, z którego kolejne zapytania dziedziczą przez referencję, a nie przez ponowne połączenie</li>
        </ul>
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
            lineageTag: 63e88cbe-31cf-4b77-8ff1-72415cf5f0f6

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

