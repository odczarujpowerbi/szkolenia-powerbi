createOrReplace

    table _HTML
        lineageTag: d05772c9-547e-434c-8592-cd50b9b51a70

        measure '00. Konfiguracja Power BI - Główne widoki Power BI Desktop' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Główne widoki Power BI Desktop</title>
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

<div class='container' id='viz_5dc96cd3'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_5dc96cd3' onclick='changePage_5dc96cd3(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_5dc96cd3'>1</span> z <span id='totalPages_5dc96cd3'>6</span>
        </span>
        <button id='nextBtn_5dc96cd3' onclick='changePage_5dc96cd3(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Widoki Power BI Desktop</h1>
        <p>Power BI Desktop oferuje pięć głównych widoków, z których każdy służy do różnych celów. Znajomość tych widoków jest kluczowa dla efektywnej pracy z narzędziem.</p>
        <h2>1. Widok Raport (Report View)</h2>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209155301.png?raw=true' width='100%'>
        <p><strong>Zastosowanie:</strong> Tworzenie i projektowanie wizualizacji danych.</p>
        <p>W tym widoku:</p>
        <ul>
        <li>Tworzysz wykresy, tabele, karty i inne wizualizacje</li>
        <li>Układasz elementy na stronach raportu</li>
        <li>Konfigurujesz formatowanie wizualizacji</li>
        <li>Ustawiasz interakcje między obiektami</li>
        </ul>
        <p><strong>Przykład użycia:</strong></p>
        <p>Stworzenie wykresu słupkowego pokazującego sumę sprzedaży (Price × Quantity) według kategorii z tabeli fDemo.</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>2. Widok Dane (Data View)</h2>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209155324.png?raw=true' width='100%'>
        <p><strong>Zastosowanie:</strong> Podgląd i weryfikacja danych w tabelach.</p>
        <p>W tym widoku:</p>
        <ul>
        <li>Przeglądasz zawartość tabel</li>
        <li>Weryfikujesz poprawność danych</li>
        <li>Tworzysz kolumny kalkulowane</li>
        <li>Sprawdzasz wyniki transformacji</li>
        </ul>
        <p><strong>Przykład użycia:</strong></p>
        <p>Sprawdzenie, czy wszystkie produkty z tabeli fDemo mają przypisane wartości w kolumnach Price, Quantity i Category.</p>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>3. Widok Model (Model View)</h2>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209155620.png?raw=true' width='100%'>
        <p><strong>Zastosowanie:</strong> Zarządzanie relacjami między tabelami i strukturą modelu danych.</p>
        <p>W tym widoku:</p>
        <ul>
        <li>Tworzysz relacje między tabelami</li>
        <li>Zarządzasz kluczami głównymi i obcymi</li>
        <li>Organizujesz tabele w grupy tematyczne</li>
        <li>Definiujesz hierarchie wymiarów</li>
        </ul>
        <p><strong>Przykład użycia:</strong></p>
        <p>W przypadku rozbudowy modelu o tabelę wymiarową 'DimCategory' można by tutaj utworzyć relację między fDemo[Category] a DimCategory[CategoryName].</p>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>4. Widok DAX Query (DAX Query View)</h2>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209155746.png?raw=true' width='100%'>
        <p><strong>Zastosowanie:</strong> Testowanie zapytań DAX bez tworzenia miar w modelu.</p>
        <p>W tym widoku:</p>
        <ul>
        <li>Piszesz i testujesz zapytania DAX (podobnie jak SQL)</li>
        <li>Szybko weryfikujesz wyniki wyrażeń</li>
        <li>Eksplorujesz dane bez wpływu na model</li>
        <li>Uczysz się składni DAX</li>
        </ul>
        <p><strong>Przykład zapytania:</strong></p>
        <pre><code>EVALUATE
        <span class='dax-function'>SUMMARIZECOLUMNS</span>(
            fDemo[Category],
            'Total Sales', <span class='dax-function'>SUMX</span>(fDemo, fDemo[Price] * fDemo[Quantity])
        )
        ORDER BY [Total Sales] DESC</code></pre>
        <p>To zapytanie zwróci zestawienie sprzedaży według kategorii, posortowane malejąco.</p>

    </div>

    <!-- Strona 5 -->
    <div class='page'>
        <h2>5. Widok TMDL (Tabular Model Definition Language)</h2>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209161608.png?raw=true' width='100%'>
        <p><strong>Zastosowanie:</strong> Edycja modelu danych w formie tekstowej (dla zaawansowanych użytkowników).</p>
        <p>W tym widoku:</p>
        <ul>
        <li>Przeglądasz definicję modelu w postaci kodu</li>
        <li>Możesz edytować właściwości obiektów</li>
        <li>Przydatne do wersjonowania modelu (Git)</li>
        <li>Umożliwia zaawansowane operacje masowe</li>
        </ul>
        <p><strong>Uwaga:</strong> Ten widok jest przeznaczony dla zaawansowanych użytkowników i programistów, którzy chcą zarządzać modelem jako kodem.</p>

    </div>

    <!-- Strona 6 -->
    <div class='page'>
        <h1>Podsumowanie</h1>
        <p>Prawidłowe przygotowanie środowiska Power BI to fundament efektywnej pracy:</p>
        <p>✓ Włącz niezbędne funkcje w wersji zapoznawczej</p>
        <p>✓ Skonfiguruj ustawienia Power Query (wyłącz auto-detekcję typów)</p>
        <p>✓ Ustaw właściwą wersję językową</p>
        <p>✓ Poznaj wszystkie pięć widoków Power BI Desktop</p>
        <p>Znajomość tych elementów pozwoli Ci sprawnie poruszać się po środowisku i skupić się na budowaniu efektywnych rozwiązań analitycznych.</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '5dc96cd3';
    var containerId = 'viz_' + vizId;

    var currentPage_5dc96cd3 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_5dc96cd3'] = function(n) {
        if (n > totalPages) currentPage_5dc96cd3 = totalPages;
        if (n < 1) currentPage_5dc96cd3 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_5dc96cd3 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_5dc96cd3;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_5dc96cd3 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_5dc96cd3 === totalPages);
    };

    window['changePage_5dc96cd3'] = function(n) {
        currentPage_5dc96cd3 += n;
        window['showPage_5dc96cd3'](currentPage_5dc96cd3);
    };

    // Inicjalizacja
    window['showPage_5dc96cd3'](1);

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
            lineageTag: 032c0ae7-280b-4e1e-9a1d-d0090528dc47

        measure '00. Konfiguracja Power BI - Przygotowanie środowiska Power BI' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Przygotowanie środowiska Power BI</title>
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

<div class='container' id='viz_905d5ea6'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_905d5ea6' onclick='changePage_905d5ea6(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_905d5ea6'>1</span> z <span id='totalPages_905d5ea6'>4</span>
        </span>
        <button id='nextBtn_905d5ea6' onclick='changePage_905d5ea6(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Ustawienia programu Power BI</h1>
        <p>Przed rozpoczęciem pracy z Power BI Desktop warto odpowiednio skonfigurować środowisko pracy. Prawidłowe ustawienia programu umożliwiają dostęp do nowych funkcji oraz optymalizują sposób pracy z danymi.</p>
        <h2>Włączenie funkcji w wersji zapoznawczej (Preview Features)</h2>
        <p>Power BI regularnie wprowadza nowe funkcje, które na początku dostępne są jako wersje zapoznawcze. Aby je włączyć:</p>
        <ol>
        <li>Otwórz <strong>Plik</strong> → <strong>Opcje i ustawienia</strong> → <strong>Opcje</strong></li>
        <li>Przejdź do sekcji <strong>Funkcje w wersji zapoznawczej</strong> (Preview features)</li>
        <li>Zaznacz następujące opcje:
        <ul>
        <li><strong>Obliczenia wizualne</strong> - pozwala na tworzenie bardziej zaawansowanych wizualizacji</li>
        <li><strong>Nowe wizualizacje</strong> - daje dostęp do najnowszych typów wizualizacji</li>
        </ul>
        </li>
        </ol>
        <p><strong>Uwaga:</strong> Po włączeniu funkcji w wersji zapoznawczej konieczne jest ponowne uruchomienie Power BI Desktop.</p>
        <p><img src='https://raw.githubusercontent.com/odczarujpowerbi/grafiki-do-szkolenia/main/PowerBI - Ustawienia - Preview Features.gif' width='100%'></p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>Konfiguracja ustawień raportu- włączenie interakcji między obiektami na raporcie</h2>
        <p>Interakcje między wizualizacjami pozwalają na dynamiczne filtrowanie danych. Aby włączyć tę funkcję:</p>
        <ol>
        <li>Przejdź do widoku <strong>Raport</strong></li>
        <li>Kliknij <strong>Plik</strong> → <strong>Opcje i ustawienia</strong> → <strong>Opcje</strong></li>
        <li>W sekcji <strong>BIEŻĄCY PLIK</strong> → <strong>Ustawienia raportu</strong></li>
        <li>Upewnij się, że opcja dotycząca interakcji wizualizacji jest włączona</li>
        </ol>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209170359.png?raw=true' width='100%'>
        <p>> Dzięki temu kliknięcie na element jednej wizualizacji (np. kolumnę na wykresie) automatycznie przefiltruje pozostałe wizualizacje na stronie raportu.</p>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Ustawienia Power Query-  wyłączenie automatycznego wykrywania typów kolumn</h2>
        <p>Automatyczne wykrywanie typów danych przez Power Query może czasem prowadzić do błędów lub niepożądanych konwersji. Zaleca się wyłączenie tej opcji i ręczne kontrolowanie typów danych:</p>
        <ol>
        <li>Otwórz <strong>Plik</strong> → <strong>Opcje i ustawienia</strong> → <strong>Opcje</strong></li>
        <li>Przejdź do sekcji <strong>BIEŻĄCY PLIK</strong> → <strong>Ładowanie danych</strong></li>
        <li>Odznacz opcję <strong>Automatycznie wykrywaj typy kolumn i nagłówki dla źródeł nieustrukturyzowanych</strong></li>
        </ol>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209170441.png?raw=true' width='100%'>
        <p>Dzięki temu będziesz mieć pełną kontrolę nad tym, jakie typy danych są przypisywane do poszczególnych kolumn.</p>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>Ustawienie wersji językowej</h2>
        <p>Wersja językowa Power BI wpływa na separatory dziesiętne, daty oraz niektóre funkcje DAX:</p>
        <ol>
        <li>Otwórz <strong>Plik</strong> → <strong>Opcje i ustawienia</strong> → <strong>Opcje</strong></li>
        <li>Przejdź do sekcji <strong>GLOBALNE</strong> → <strong>Ustawienia regionalne</strong></li>
        <li>Wybierz odpowiedni język - zalecany jest Angielski ze względu na:
        <ul>
        <li>Prostszą integrację z AI</li>
        <li>Spójność nazewnictwa z dokumentacją Microsoft Learn</li>
        </ul>
        </li>
        </ol>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209170514.png?raw=true' width='100%'>
        <p><strong>Uwaga:</strong></p>
        <ul>
        <li>W polskiej wersji separator dziesiętny to przecinek (<code>,</code>), a separator argumentów to średnik (<code>;</code>)</li>
        <li>W angielskiej wersji separator dziesiętny to kropka (<code>.</code>), a separator argumentów to przecinek (<code>,</code>)</li>
        </ul>
        <p>Przykład różnic w składni DAX:</p>
        <pre><code>// Wersja polska
        Suma wartości = <span class='dax-function'>SUMX</span>(fDemo; fDemo[Price] * fDemo[Quantity])

        // Wersja angielska
        Suma wartości = <span class='dax-function'>SUMX</span>(fDemo, fDemo[Price] * fDemo[Quantity])</code></pre>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '905d5ea6';
    var containerId = 'viz_' + vizId;

    var currentPage_905d5ea6 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_905d5ea6'] = function(n) {
        if (n > totalPages) currentPage_905d5ea6 = totalPages;
        if (n < 1) currentPage_905d5ea6 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_905d5ea6 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_905d5ea6;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_905d5ea6 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_905d5ea6 === totalPages);
    };

    window['changePage_905d5ea6'] = function(n) {
        currentPage_905d5ea6 += n;
        window['showPage_905d5ea6'](currentPage_905d5ea6);
    };

    // Inicjalizacja
    window['showPage_905d5ea6'](1);

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
            lineageTag: 1f6406b4-98a6-473b-aae2-347ea21addaa

        measure '00. Quiz - test' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Nazwa Quizu</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>3</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Która funkcja jest zalecana do tworzenia zestawień tabelarycznych?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) ZŁA
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) ZŁA
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) POPRAWNA
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) ZŁA
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Treść pytania 2</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) POPRAWNA
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) ZŁA
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) ZŁA
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) ZŁA
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/2</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 3;
    const totalQuestions = 2;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [2, 0];
    
    const explanations = [
        'wyjaśnienie',
        'wyjaśnienie'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: 02f3a3a1-8365-4b69-b559-258fc72e2f4e

        measure '01. Podstawy DAX - Funkcje agregujące' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Funkcje agregujące</title>
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

<div class='container' id='viz_0faeee3d'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_0faeee3d' onclick='changePage_0faeee3d(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_0faeee3d'>1</span> z <span id='totalPages_0faeee3d'>7</span>
        </span>
        <button id='nextBtn_0faeee3d' onclick='changePage_0faeee3d(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>SUM – Suma wartości</h1>
        <p>Sumuje wszystkie wartości w kolumnie:</p>
        <pre><code>Suma Sprzedaży = <span class='dax-function'>SUM</span>(Sprzedaz[Kwota])</code></pre>
        <p><strong>Jak działa:</strong></p>
        <ul>
        <li>Dodaje wszystkie liczby w kolumnie <code>Sprzedaz[Kwota]</code></li>
        <li>Pomija wartości <code>BLANK()</code> (puste)</li>
        <li>Uwzględnia aktualny kontekst filtrowania</li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>AVERAGE – Średnia</h1>
        <p>Oblicza średnią arytmetyczną:</p>
        <pre><code>Średnia Cena = <span class='dax-function'>AVERAGE</span>(Produkty[Cena])</code></pre>
        <p><strong>Jak działa:</strong></p>
        <ul>
        <li>Sumuje wszystkie wartości i dzieli przez ich liczbę</li>
        <li>Pomija wartości puste</li>
        </ul>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>COUNT – Liczba wartości niepustych</h1>
        <p>Liczy ile jest niepustych wartości <strong>numerycznych</strong> w kolumnie:</p>
        <pre><code>Liczba Transakcji = <span class='dax-function'>COUNT</span>(Sprzedaz[ID Transakcji])</code></pre>
        <p><strong>Uwaga:</strong> COUNT liczy tylko wartości <strong>niepuste</strong> (pomija BLANK).</p>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>COUNTA – Liczba wartości niepustych (dowolny typ)</h1>
        <p>Podobnie jak COUNT, ale działa na <strong>wszystkich typach danych</strong> (tekst, liczby, daty):</p>
        <pre><code>Liczba Produktów = <span class='dax-function'>COUNTA</span>(Produkty[Nazwa])</code></pre>

    </div>

    <!-- Strona 5 -->
    <div class='page'>
        <h1>COUNTROWS – Liczba wierszy w tabeli</h1>
        <p>Liczy wszystkie wiersze w tabeli (nawet jeśli mają puste wartości):</p>
        <pre><code>Liczba Zamówień = <span class='dax-function'>COUNTROWS</span>(Zamowienia)</code></pre>
        <p><strong>Różnica COUNT vs COUNTROWS:</strong></p>
        <ul>
        <li><code>COUNT</code> – liczy niepuste wartości w <strong>konkretnej kolumnie</strong></li>
        <li><code>COUNTROWS</code> – liczy <strong>wszystkie wiersze w tabeli</strong></li>
        </ul>

    </div>

    <!-- Strona 6 -->
    <div class='page'>
        <h1>MIN i MAX – Minimum i maksimum</h1>
        <pre><code>Najniższa Cena = <span class='dax-function'>MIN</span>(Produkty[Cena])
        Najwyższa Cena = <span class='dax-function'>MAX</span>(Produkty[Cena])</code></pre>

    </div>

    <!-- Strona 7 -->
    <div class='page'>
        <h1>DISTINCTCOUNT – Liczba unikalnych wartości</h1>
        <p>Liczy ile jest <strong>unikalnych</strong> (niepowtarzających się) wartości:</p>
        <pre><code>Liczba Unikalnych Klientów = <span class='dax-function'>DISTINCTCOUNT</span>(Sprzedaz[ID Klienta])</code></pre>
        <p><strong>Przykład:</strong> Jeśli kolumna zawiera: <code>{1, 2, 2, 3, 3, 3}</code>, to <code>DISTINCTCOUNT</code> zwróci <strong>3</strong>.</p>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '0faeee3d';
    var containerId = 'viz_' + vizId;

    var currentPage_0faeee3d = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_0faeee3d'] = function(n) {
        if (n > totalPages) currentPage_0faeee3d = totalPages;
        if (n < 1) currentPage_0faeee3d = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_0faeee3d - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_0faeee3d;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_0faeee3d === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_0faeee3d === totalPages);
    };

    window['changePage_0faeee3d'] = function(n) {
        currentPage_0faeee3d += n;
        window['showPage_0faeee3d'](currentPage_0faeee3d);
    };

    // Inicjalizacja
    window['showPage_0faeee3d'](1);

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
            lineageTag: 309b8534-b60b-43dc-a8a3-24e322bf6073

        measure '01. Podstawy DAX - Funkcje dat' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Funkcje dat</title>
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

<div class='container' id='viz_5bcb381d'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_5bcb381d' onclick='changePage_5bcb381d(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_5bcb381d'>1</span> z <span id='totalPages_5bcb381d'>4</span>
        </span>
        <button id='nextBtn_5bcb381d' onclick='changePage_5bcb381d(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>DATE – Tworzenie daty</h1>
        <pre><code><span class='dax-function'>DATE</span>(&lt;rok&gt;, &lt;miesiąc&gt;, &lt;dzień&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Data Bazowa = <span class='dax-function'>DATE</span>(<span class='dax-number'>2024</span>, <span class='dax-number'>1</span>, <span class='dax-number'>1</span>)</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>TODAY i NOW – Dzisiejsza data</h1>
        <pre><code><span class='dax-function'>TODAY</span>()     <span class='dax-comment'>-- Dzisiejsza data (bez godziny)</span>
        <span class='dax-function'>NOW</span>()       <span class='dax-comment'>-- Dzisiejsza data i godzina</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Aktualna Data = <span class='dax-function'>TODAY</span>()</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>YEAR, MONTH, DAY – Wyciąganie składników daty</h1>
        <pre><code><span class='dax-function'>YEAR</span>(&lt;data&gt;)   <span class='dax-comment'>-- Rok</span>
        <span class='dax-function'>MONTH</span>(&lt;data&gt;)  <span class='dax-comment'>-- Miesiąc (1-12)</span>
        <span class='dax-function'>DAY</span>(&lt;data&gt;)    <span class='dax-comment'>-- Dzień (1-31)</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Rok Sprzedaży = <span class='dax-function'>YEAR</span>(Sprzedaz[Data])
        Miesiąc Sprzedaży = <span class='dax-function'>MONTH</span>(Sprzedaz[Data])</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>DATEDIFF – Różnica między datami</h1>
        <pre><code><span class='dax-function'>DATEDIFF</span>(&lt;data_początkowa&gt;, &lt;data_końcowa&gt;, &lt;jednostka&gt;)</code></pre>
        <p><strong>Jednostki:</strong> DAY, MONTH, YEAR, QUARTER</p>
        <p><strong>Przykład:</strong></p>
        <pre><code>Dni Od Zamówienia = 
        <span class='dax-function'>DATEDIFF</span>(Zamowienia[Data Zamówienia], <span class='dax-function'>TODAY</span>(), DAY)</code></pre>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '5bcb381d';
    var containerId = 'viz_' + vizId;

    var currentPage_5bcb381d = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_5bcb381d'] = function(n) {
        if (n > totalPages) currentPage_5bcb381d = totalPages;
        if (n < 1) currentPage_5bcb381d = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_5bcb381d - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_5bcb381d;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_5bcb381d === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_5bcb381d === totalPages);
    };

    window['changePage_5bcb381d'] = function(n) {
        currentPage_5bcb381d += n;
        window['showPage_5bcb381d'](currentPage_5bcb381d);
    };

    // Inicjalizacja
    window['showPage_5bcb381d'](1);

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
            lineageTag: 086ec33d-d8f5-4aca-bbed-33113d031f6d

        measure '01. Podstawy DAX - Funkcje iteracyjne (X-functions)' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Funkcje iteracyjne (X-functions)</title>
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

<div class='container' id='viz_6b285173'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_6b285173' onclick='changePage_6b285173(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_6b285173'>1</span> z <span id='totalPages_6b285173'>4</span>
        </span>
        <button id='nextBtn_6b285173' onclick='changePage_6b285173(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <p>Funkcje iteracyjne przechodzą przez <strong>każdy wiersz tabeli</strong> i wykonują obliczenia dla każdego wiersza osobno.</p>
        <h1>SUMX – Suma z iteracją</h1>
        <pre><code><span class='dax-function'>SUMX</span>(&lt;tabela&gt;, &lt;wyrażenie&gt;)</code></pre>
        <p>Dla każdego wiersza tabeli oblicza wyrażenie, potem sumuje wyniki.</p>
        <p><strong>Przykład:</strong></p>
        <pre><code>Suma Wartości Zamówień = 
        <span class='dax-function'>SUMX</span>(
            Sprzedaz,
            Sprzedaz[Ilość] * Sprzedaz[Cena]
        )</code></pre>
        <p><strong>Co się dzieje:</strong></p>
        <ul>
        <li>Dla każdego wiersza w tabeli <code>Sprzedaz</code> mnoży <code>Ilość * Cena</code></li>
        <li>Potem sumuje wszystkie wyniki</li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>AVERAGEX – Średnia z iteracją</h1>
        <pre><code><span class='dax-function'>AVERAGEX</span>(&lt;tabela&gt;, &lt;wyrażenie&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Średnia Marża = 
        <span class='dax-function'>AVERAGEX</span>(
            Sprzedaz,
            Sprzedaz[Przychód] - Sprzedaz[Koszt]
        )</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>COUNTX – Liczenie z iteracją</h1>
        <pre><code><span class='dax-function'>COUNTX</span>(&lt;tabela&gt;, &lt;wyrażenie&gt;)</code></pre>
        <p>Liczy ile razy wyrażenie zwróciło <strong>niepustą wartość</strong>.</p>
        <p><strong>Przykład:</strong></p>
        <pre><code>Liczba Zamówień Powyżej <span class='dax-number'>1000</span> = 
        <span class='dax-function'>COUNTX</span>(
            Sprzedaz,
            <span class='dax-function'>IF</span>(Sprzedaz[Kwota] &gt; <span class='dax-number'>1000</span>, <span class='dax-number'>1</span>, <span class='dax-function'>BLANK</span>())
        )</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>MINX i MAXX – Minimum i maksimum z iteracją</h1>
        <pre><code><span class='dax-function'>MINX</span>(&lt;tabela&gt;, &lt;wyrażenie&gt;)
        <span class='dax-function'>MAXX</span>(&lt;tabela&gt;, &lt;wyrażenie&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Najwyższa Marża = 
        <span class='dax-function'>MAXX</span>(
            Sprzedaz,
            Sprzedaz[Przychód] - Sprzedaz[Koszt]
        )</code></pre>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '6b285173';
    var containerId = 'viz_' + vizId;

    var currentPage_6b285173 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_6b285173'] = function(n) {
        if (n > totalPages) currentPage_6b285173 = totalPages;
        if (n < 1) currentPage_6b285173 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_6b285173 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_6b285173;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_6b285173 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_6b285173 === totalPages);
    };

    window['changePage_6b285173'] = function(n) {
        currentPage_6b285173 += n;
        window['showPage_6b285173'](currentPage_6b285173);
    };

    // Inicjalizacja
    window['showPage_6b285173'](1);

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
            lineageTag: 0fb9c395-0704-4fef-9879-8be960a461bb

        measure '01. Podstawy DAX - Funkcje logiczne' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Funkcje logiczne</title>
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

<div class='container' id='viz_a487a00b'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_a487a00b' onclick='changePage_a487a00b(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_a487a00b'>1</span> z <span id='totalPages_a487a00b'>4</span>
        </span>
        <button id='nextBtn_a487a00b' onclick='changePage_a487a00b(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>IF – Warunek logiczny</h1>
        <p>Zwraca jedną wartość jeśli warunek jest prawdziwy, inną jeśli fałszywy:</p>
        <pre><code><span class='dax-function'>IF</span>(&lt;warunek&gt;, &lt;wartość_jeśli_prawda&gt;, &lt;wartość_jeśli_fałsz&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Kategoria Sprzedaży = 
        <span class='dax-function'>IF</span>(
            Sprzedaz[Kwota] &gt; <span class='dax-number'>1000</span>,
            'Wysoka',
            'Niska'
        )</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>AND – Sprawdza czy wszystkie warunki są prawdziwe</h1>
        <pre><code><span class='dax-function'>AND</span>(&lt;warunek1&gt;, &lt;warunek2&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Czy VIP = 
        <span class='dax-function'>IF</span>(
            <span class='dax-function'>AND</span>(Klienci[Przychód] &gt; <span class='dax-number'>50000</span>, Klienci[Lata Współpracy] &gt; <span class='dax-number'>5</span>),
            'TAK',
            'NIE'
        )</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>OR – Sprawdza czy przynajmniej jeden warunek jest prawdziwy</h1>
        <pre><code><span class='dax-function'>OR</span>(&lt;warunek1&gt;, &lt;warunek2&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Czy Promocja = 
        <span class='dax-function'>IF</span>(
            <span class='dax-function'>OR</span>(Produkty[Kategoria] = 'Elektronika', Produkty[Wyprzedaż] = TRUE),
            'TAK',
            'NIE'
        )</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>NOT – Negacja warunku</h1>
        <pre><code><span class='dax-function'>NOT</span>(&lt;warunek&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Czy Nieaktywny = 
        <span class='dax-function'>IF</span>(
            <span class='dax-function'>NOT</span>(Klienci[Status] = 'Aktywny'),
            'TAK',
            'NIE'
        )</code></pre>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'a487a00b';
    var containerId = 'viz_' + vizId;

    var currentPage_a487a00b = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_a487a00b'] = function(n) {
        if (n > totalPages) currentPage_a487a00b = totalPages;
        if (n < 1) currentPage_a487a00b = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_a487a00b - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_a487a00b;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_a487a00b === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_a487a00b === totalPages);
    };

    window['changePage_a487a00b'] = function(n) {
        currentPage_a487a00b += n;
        window['showPage_a487a00b'](currentPage_a487a00b);
    };

    // Inicjalizacja
    window['showPage_a487a00b'](1);

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
            lineageTag: 96560f59-7e62-466c-b577-75398c880bbc

        measure '01. Podstawy DAX - Funkcje tekstowe' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Funkcje tekstowe</title>
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

<div class='container' id='viz_ea79c585'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_ea79c585' onclick='changePage_ea79c585(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_ea79c585'>1</span> z <span id='totalPages_ea79c585'>4</span>
        </span>
        <button id='nextBtn_ea79c585' onclick='changePage_ea79c585(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>CONCATENATE – Łączenie tekstów</h1>
        <pre><code><span class='dax-function'>CONCATENATE</span>(&lt;tekst1&gt;, &lt;tekst2&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Pełna Nazwa = <span class='dax-function'>CONCATENATE</span>(Klienci[Imię], ' ' & Klienci[Nazwisko])</code></pre>
        <p><strong>Alternatywa (łatwiejsza):</strong></p>
        <pre><code>Pełna Nazwa = Klienci[Imię] & ' ' & Klienci[Nazwisko]</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>LEFT, RIGHT, MID – Wyciąganie części tekstu</h1>
        <pre><code><span class='dax-function'>LEFT</span>(&lt;tekst&gt;, &lt;liczba_znaków&gt;)    <span class='dax-comment'>-- Pierwsze znaki od lewej</span>
        <span class='dax-function'>RIGHT</span>(&lt;tekst&gt;, &lt;liczba_znaków&gt;)   <span class='dax-comment'>-- Ostatnie znaki od prawej</span>
        <span class='dax-function'>MID</span>(&lt;tekst&gt;, &lt;start&gt;, &lt;liczba&gt;)   <span class='dax-comment'>-- Znaki ze środka</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Pierwsze <span class='dax-number'>3</span> Znaki = <span class='dax-function'>LEFT</span>(Produkty[Kod], <span class='dax-number'>3</span>)
        Ostatnie <span class='dax-number'>2</span> Znaki = <span class='dax-function'>RIGHT</span>(Produkty[Kod], <span class='dax-number'>2</span>)</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>UPPER, LOWER – Zmiana wielkości liter</h1>
        <pre><code><span class='dax-function'>UPPER</span>(&lt;tekst&gt;)  <span class='dax-comment'>-- Wszystkie znaki WIELKIE</span>
        <span class='dax-function'>LOWER</span>(&lt;tekst&gt;)  <span class='dax-comment'>-- Wszystkie znaki małe</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Kategoria Wielkie Litery = <span class='dax-function'>UPPER</span>(Produkty[Kategoria])</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>LEN – Długość tekstu</h1>
        <pre><code><span class='dax-function'>LEN</span>(&lt;tekst&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Długość Kodu = <span class='dax-function'>LEN</span>(Produkty[Kod Produktu])</code></pre>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'ea79c585';
    var containerId = 'viz_' + vizId;

    var currentPage_ea79c585 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_ea79c585'] = function(n) {
        if (n > totalPages) currentPage_ea79c585 = totalPages;
        if (n < 1) currentPage_ea79c585 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_ea79c585 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_ea79c585;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_ea79c585 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_ea79c585 === totalPages);
    };

    window['changePage_ea79c585'] = function(n) {
        currentPage_ea79c585 += n;
        window['showPage_ea79c585'](currentPage_ea79c585);
    };

    // Inicjalizacja
    window['showPage_ea79c585'](1);

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
            lineageTag: 66244334-f9b0-4e5c-8e9d-a1f269dfc177

        measure '01. Podstawy DAX' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>01. Podstawy DAX</title>
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

<div class='container' id='viz_bb3ff736'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_bb3ff736' onclick='changePage_bb3ff736(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_bb3ff736'>1</span> z <span id='totalPages_bb3ff736'>9</span>
        </span>
        <button id='nextBtn_bb3ff736' onclick='changePage_bb3ff736(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Czym jest DAX?</h1>
        <p><strong>DAX (Data Analysis Expressions)</strong> to język formuł używany w Power BI, Excel Power Pivot i Analysis Services do tworzenia:</p>
        <ul>
        <li><strong>Miar</strong> (measures) – dynamicznych obliczeń</li>
        <li><strong>Kolumn kalkulowanych</strong> – stałych wartości w tabelach</li>
        <li><strong>Tabel kalkulowanych</strong> – nowych tabel powstałych z obliczeń</li>
        </ul>
        <p>DAX pozwala na analizę danych, tworzenie raportów i budowanie zaawansowanej logiki biznesowej.</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Odwoływanie się do tabel i kolumn</h1>
        <h2>Podstawowa składnia</h2>
        <p>W DAX zawsze odwołujesz się do kolumn poprzez <strong>nazwę tabeli</strong> i <strong>nazwę kolumny</strong> w nawiasach kwadratowych:</p>
        <pre><code>Sprzedaz[Kwota]
        Produkty[Kategoria]
        Klienci[Miasto]</code></pre>
        <p><strong>Zasady:</strong></p>
        <ul>
        <li>Nazwa tabeli <strong>przed</strong> nawiasem kwadratowym</li>
        <li>Nazwa kolumny <strong>w</strong> nawiasach kwadratowych</li>
        <li>To zapobiega niejednoznaczności gdy masz kolumny o tych samych nazwach w różnych tabelach</li>
        </ul>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Nazwy z apostrofami</h2>
        <p>Jeśli nazwa tabeli lub kolumny zawiera:</p>
        <ul>
        <li>Spacje</li>
        <li>Znaki specjalne (np. <code>-</code>, <code>#</code>, <code>%</code>)</li>
        <li>Polskie znaki</li>
        </ul>
        <p>Musisz ująć je w <strong>apostrofy</strong> <code>'</code>:</p>
        <pre><code>'Tabela Sprzedaży'[Kwota Netto]
        'Dane-Produktów'[Nazwa Produktu]
        '<span class='dax-number'>2024</span> Wyniki'[Przychód]
        Produkty[Cena (netto)]</code></pre>
        <p><strong>Przykład błędny:</strong></p>
        <pre><code>Tabela Sprzedaży[Kwota Netto]  <span class='dax-comment'>-- ❌ Błąd składni!</span></code></pre>
        <p><strong>Przykład poprawny:</strong></p>
        <pre><code>'Tabela Sprzedaży'[Kwota Netto]  <span class='dax-comment'>-- ✅ Działa</span></code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>Odwoływanie się do miar</h2>
        <p>Miary (measures) odwołujesz się <strong>bez nazwy tabeli</strong>, tylko w nawiasach kwadratowych:</p>
        <pre><code>[Suma Sprzedaży]
        [Średnia Cena]
        [Liczba Klientów]</code></pre>
        <p>Możesz też użyć pełnej notacji z nazwą tabeli, ale nie jest to wymagane:</p>
        <pre><code>Sprzedaz[Suma Sprzedaży]  <span class='dax-comment'>-- Działa, ale zwykle niepotrzebne</span></code></pre>

    </div>

    <!-- Strona 5 -->
    <div class='page'>
        <h1>Typy danych w DAX</h1>
        <p>DAX obsługuje kilka podstawowych typów danych:</p>
        <table>
          <thead>
            <tr>
              <th>Typ</th>
              <th>Przykład</th>
              <th>Opis</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Liczby całkowite</strong></td>
              <td><code>100</code>, <code>-50</code></td>
              <td>Integer</td>
            </tr>
            <tr>
              <td><strong>Liczby dziesiętne</strong></td>
              <td><code>123.45</code>, <code>0.99</code></td>
              <td>Decimal/Float</td>
            </tr>
            <tr>
              <td><strong>Tekst</strong></td>
              <td><code>'Warszawa'</code>, <code>'ABC'</code></td>
              <td>String (w cudzysłowach)</td>
            </tr>
            <tr>
              <td><strong>Data</strong></td>
              <td><code>DATE(2024, 12, 8)</code></td>
              <td>Date</td>
            </tr>
            <tr>
              <td><strong>Data i czas</strong></td>
              <td><code>DATETIME(2024, 12, 8, 14, 30, 0)</code></td>
              <td>DateTime</td>
            </tr>
            <tr>
              <td><strong>Logiczne</strong></td>
              <td><code>TRUE</code>, <code>FALSE</code></td>
              <td>Boolean</td>
            </tr>
            <tr>
              <td><strong>Puste</strong></td>
              <td><code>BLANK()</code></td>
              <td>Null/Empty</td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 6 -->
    <div class='page'>
        <h1>Operatory matematyczne</h1>
        <pre><code>+   <span class='dax-comment'>-- Dodawanie</span>
        -   <span class='dax-comment'>-- Odejmowanie</span>
        *   <span class='dax-comment'>-- Mnożenie</span>
        /   <span class='dax-comment'>-- Dzielenie</span>
        ^   <span class='dax-comment'>-- Potęgowanie</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Marża = 
        Sprzedaz[Przychód] - Sprzedaz[Koszt]</code></pre>

    </div>

    <!-- Strona 7 -->
    <div class='page'>
        <h1>Operatory porównania</h1>
        <pre><code>=   <span class='dax-comment'>-- Równe</span>
        &lt;&gt;  <span class='dax-comment'>-- Różne od</span>
        &gt;   <span class='dax-comment'>-- Większe niż</span>
        &lt;   <span class='dax-comment'>-- Mniejsze niż</span>
        &gt;=  <span class='dax-comment'>-- Większe lub równe</span>
        &lt;=  <span class='dax-comment'>-- Mniejsze lub równe</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Czy Duża Sprzedaż = 
        Sprzedaz[Kwota] &gt; <span class='dax-number'>1000</span></code></pre>

    </div>

    <!-- Strona 8 -->
    <div class='page'>
        <h1>Operatory logiczne</h1>
        <pre><code>&&  <span class='dax-comment'>-- AND (i)</span>
        ||  <span class='dax-comment'>-- OR (lub)</span>
        NOT <span class='dax-comment'>-- NOT (negacja)</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Czy Premium = 
        Klienci[Kategoria] = 'VIP' && Klienci[Przychód] &gt; <span class='dax-number'>10000</span></code></pre>

    </div>

    <!-- Strona 9 -->
    <div class='page'>
        <h1>Operator łączenia tekstów</h1>
        <pre><code>&   <span class='dax-comment'>-- Konkatenacja (łączenie tekstów)</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Pełna Nazwa = 
        Klienci[Imię] & ' ' & Klienci[Nazwisko]</code></pre>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'bb3ff736';
    var containerId = 'viz_' + vizId;

    var currentPage_bb3ff736 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_bb3ff736'] = function(n) {
        if (n > totalPages) currentPage_bb3ff736 = totalPages;
        if (n < 1) currentPage_bb3ff736 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_bb3ff736 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_bb3ff736;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_bb3ff736 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_bb3ff736 === totalPages);
    };

    window['changePage_bb3ff736'] = function(n) {
        currentPage_bb3ff736 += n;
        window['showPage_bb3ff736'](currentPage_bb3ff736);
    };

    // Inicjalizacja
    window['showPage_bb3ff736'](1);

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
            lineageTag: ce2b57d5-22b4-47af-92c9-ace981794c7d

        measure '01. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: Podstawy DAX</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>7</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Co oznacza skrót DAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Data Analysis eXpressions
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Dynamic Analytics eXtension
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Database Analysis eXtended
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) Data Application eXtension
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Jak prawidłowo odwołać się do kolumny w DAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Kolumna[Tabela]
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) [Kolumna]
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) Tabela[Kolumna]
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) Kolumna.Tabela
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Jak odwołać się do miary (measure) w DAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) Tabela[Miara]
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) [Miara]
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) Miara()
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) Obie odpowiedzi A i B są poprawne
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 3)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Która funkcja sumuje wartości z kolumny?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) SUMX()
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) SUM()
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) TOTAL()
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) AGGREGATE()
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Czym różni się COUNT od COUNTROWS?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) COUNT liczy kolumny, COUNTROWS liczy wiersze
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) COUNT liczy niepuste wartości w kolumnie, COUNTROWS liczy wszystkie wiersze tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Nie ma różnicy
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) COUNT jest szybsze niż COUNTROWS
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Co robi funkcja DISTINCTCOUNT?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) Liczy wszystkie wartości w kolumnie
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Liczy unikalne (niepowtarzające się) wartości
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Usuwa duplikaty z tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) Zwraca liczbę różnych tabel
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/6</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 7;
    const totalQuestions = 6;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [0, 2, 3, 1, 1, 1];
    
    const explanations = [
        'Prawidłowa odpowiedź: A. DAX to skrót od Data Analysis Expressions - język formuł używany w Power BI, Excel Power Pivot i Analysis Services.',
        'Prawidłowa odpowiedź: C. W DAX zawsze używamy składni Tabela[Kolumna], gdzie nazwa tabeli jest przed nawiasem kwadratowym, a nazwa kolumny wewnątrz.',
        'Prawidłowa odpowiedź: D. Do miar można odwoływać się zarówno przez [Nazwa Miary] jak i przez Tabela[Nazwa Miary]. Pierwsza składnia jest częściej używana i krótsza.',
        'Prawidłowa odpowiedź: B. SUM(Tabela[Kolumna]) sumuje wszystkie wartości w kolumnie, pomijając wartości puste (BLANK) i uwzględniając aktualny kontekst filtrowania.',
        'Prawidłowa odpowiedź: B. COUNT liczy niepuste wartości numeryczne w konkretnej kolumnie, podczas gdy COUNTROWS liczy wszystkie wiersze w tabeli (nawet jeśli mają puste wartości).',
        'Prawidłowa odpowiedź: B. DISTINCTCOUNT liczy ile jest unikalnych (niepowtarzających się) wartości. Np. dla {1, 2, 2, 3, 3, 3} zwróci 3.'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: 3ca26386-0c00-488d-9696-9720b97f2ea3

        measure '01a. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: Podstawy DAX</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>7</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Co oznacza skrót DAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Data Analysis eXpressions
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Dynamic Analytics eXtension
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Database Analysis eXtended
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) Data Application eXtension
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Jak prawidłowo odwołać się do kolumny w DAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Kolumna[Tabela]
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) [Kolumna]
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) Tabela[Kolumna]
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) Kolumna.Tabela
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Jak odwołać się do miary (measure) w DAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) Tabela[Miara]
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) [Miara]
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) Miara()
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) Obie odpowiedzi A i B są poprawne
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 3)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Która funkcja sumuje wartości z kolumny?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) SUMX()
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) SUM()
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) TOTAL()
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) AGGREGATE()
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Czym różni się COUNT od COUNTROWS?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) COUNT liczy kolumny, COUNTROWS liczy wiersze
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) COUNT liczy niepuste wartości w kolumnie, COUNTROWS liczy wszystkie wiersze tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Nie ma różnicy
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) COUNT jest szybsze niż COUNTROWS
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Co robi funkcja DISTINCTCOUNT?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) Liczy wszystkie wartości w kolumnie
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Liczy unikalne (niepowtarzające się) wartości
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Usuwa duplikaty z tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) Zwraca liczbę różnych tabel
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/6</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 7;
    const totalQuestions = 6;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [0, 2, 3, 1, 1, 1];
    
    const explanations = [
        'Prawidłowa odpowiedź: A. DAX to skrót od Data Analysis Expressions - język formuł używany w Power BI, Excel Power Pivot i Analysis Services.',
        'Prawidłowa odpowiedź: C. W DAX zawsze używamy składni Tabela[Kolumna], gdzie nazwa tabeli jest przed nawiasem kwadratowym, a nazwa kolumny wewnątrz.',
        'Prawidłowa odpowiedź: D. Do miar można odwoływać się zarówno przez [Nazwa Miary] jak i przez Tabela[Nazwa Miary]. Pierwsza składnia jest częściej używana i krótsza.',
        'Prawidłowa odpowiedź: B. SUM(Tabela[Kolumna]) sumuje wszystkie wartości w kolumnie, pomijając wartości puste (BLANK) i uwzględniając aktualny kontekst filtrowania.',
        'Prawidłowa odpowiedź: B. COUNT liczy niepuste wartości numeryczne w konkretnej kolumnie, podczas gdy COUNTROWS liczy wszystkie wiersze w tabeli (nawet jeśli mają puste wartości).',
        'Prawidłowa odpowiedź: B. DISTINCTCOUNT liczy ile jest unikalnych (niepowtarzających się) wartości. Np. dla {1, 2, 2, 3, 3, 3} zwróci 3.'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: f81d8b81-5c91-4c9c-8eee-8b1b49796356

        measure '02. Miary vs Kolumny kalkulowane - Kolumny vs. Miary' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Kolumny vs. Miary</title>
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

<div class='container' id='viz_cd2ce545'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_cd2ce545' onclick='changePage_cd2ce545(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_cd2ce545'>1</span> z <span id='totalPages_cd2ce545'>3</span>
        </span>
        <button id='nextBtn_cd2ce545' onclick='changePage_cd2ce545(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Dwa podejścia do DAX</h1>
        <p>Jedną z najważniejszych rzeczy do zrozumienia w DAX jest różnica między <strong>miarami</strong> a <strong>kolumnami kalkulowanymi</strong>. Choć obie używają formuł DAX, działają zupełnie inaczej i wymagają <strong>odmiennego podejścia do pisania kodu</strong>.</p>
        <h1>Kolumny kalkulowane (Calculated Columns)</h1>
        <p><strong>Kolumna kalkulowana</strong> to nowa kolumna dodana do tabeli, której wartość jest obliczana <strong>wiersz po wierszu</strong> (tzw. kontekst wiersza) w momencie odświeżania danych.</p>
        <h2>Charakterystyka kolumn kalkulowanych:</h2>
        <ul>
        <li>Obliczane <strong>podczas ładowania/odświeżania danych</strong></li>
        <li>Wartość obliczana <strong>dla każdego wiersza</strong> w tabeli</li>
        <li>Wynik jest <strong>przechowywany</strong> w modelu (zajmuje miejsce w pamięci)</li>
        <li>Można ich używać do <strong>filtrowania</strong>, <strong>grupowania</strong> lub <strong>sortowania</strong></li>
        <li>Używają <strong>kontekstu wiersza</strong> (row context)</li>
        </ul>
        <h2>Przykład kolumny kalkulowanej:</h2>
        <pre><code>Cena Jednostkowa =
        Sprzedaż[Wartość netto] / Sprzedaż[Ilość]</code></pre>
        <p><strong>Co się dzieje:</strong></p>
        <ul>
        <li>Formuła jest obliczana <strong>dla każdego wiersza</strong> w tabeli Sprzedaż</li>
        <li>Jeśli masz 1000 wierszy, otrzymasz 1000 wartości</li>
        <li>Wartości są zapisane w modelu i widoczne w widoku danych</li>
        <li>Możesz użyć tej kolumny w slicerach, filtrach lub do sortowania</li>
        </ul>
        <h2>Podejście do pisania DAX w kolumnach</h2>
        <p><strong>W kolumnach możesz operować na kolumnach jak na zmiennych:</strong></p>
        <pre><code>// ✅ W KOLUMNACH - bezpośrednie odwołania do kolumn
        Marża PLN = Sprzedaż[Wartość netto] - Sprzedaż[Koszt]

        Marża % = 
        <span class='dax-function'>DIVIDE</span>(
            Sprzedaż[Wartość netto] - Sprzedaż[Koszt],
            Sprzedaż[Wartość netto]
        )

        Cena z VAT = Sprzedaż[Cena netto] * <span class='dax-number'>1.23</span>

        Kategoria cenowa = 
        <span class='dax-function'>IF</span>(
            Sprzedaż[Wartość netto] &gt; <span class='dax-number'>1000</span>,
            'Premium',
            'Standard'
        )</code></pre>
        <p><strong>Możesz:</strong></p>
        <ul>
        <li>✓ Odwoływać się bezpośrednio do kolumn: <code>Tabela[Kolumna]</code></li>
        <li>✓ Używać standardowych operatorów: <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code></li>
        <li>✓ Mnożyć, dzielić, dodawać kolumny jak w Excelu</li>
        <li>✓ Używać funkcji logicznych: <code>IF</code>, <code>SWITCH</code></li>
        <li>✓ Odwoływać się do innych kolumn kalkulowanych w tej samej tabeli</li>
        </ul>
        <p><strong>Kiedy używać kolumn kalkulowanych:</strong></p>
        <ul>
        <li>Potrzebujesz wartości do <strong>filtrowania</strong> lub <strong>grupowania</strong></li>
        <li>Chcesz <strong>posortować</strong> dane według obliczonej wartości</li>
        <li>Wartość zależy <strong>tylko od danych w bieżącym wierszu</strong></li>
        <li>Przykład: kategoria cenowa produktu, wiek klienta, dzień tygodnia, rabat procentowy</li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Miary (Measures)</h1>
        <p><strong>Miara</strong> to formuła, która oblicza się <strong>dynamicznie</strong> w zależności od kontekstu filtrów w raporcie.</p>
        <h2>Charakterystyka miar:</h2>
        <ul>
        <li>Obliczane <strong>w momencie wyświetlania</strong> w wizualizacji</li>
        <li>Nie są przechowywane w modelu (nie zajmują miejsca)</li>
        <li>Wynik zależy od <strong>kontekstu filtrów</strong> na wizualizacji</li>
        <li><strong>Nie można</strong> ich użyć do filtrowania wierszy</li>
        <li>Używają <strong>kontekstu filtrów</strong> (filter context)</li>
        </ul>
        <h2>Przykład miary:</h2>
        <pre><code>Sprzedaż Netto = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto])</code></pre>
        <p><strong>Co się dzieje:</strong></p>
        <ul>
        <li>Formuła oblicza sumę <strong>w zależności od kontekstu</strong></li>
        <li>Na wykresie według kategorii: pokaże sumę dla każdej kategorii</li>
        <li>Na wykresie według regionu: pokaże sumę dla każdego regionu</li>
        <li>Bez filtrów: pokaże sumę całkowitą</li>
        <li>Wartość <strong>nie jest przechowywana</strong>, tylko obliczana na żądanie</li>
        </ul>
        <h2>Podejście do pisania DAX w miarach</h2>
        <p><strong>W miarach MUSISZ używać funkcji agregujących:</strong></p>
        <pre><code>// ❌ ZŁE - nie zadziała w miarze
        Marża PLN = Sprzedaż[Wartość netto] - Sprzedaż[Koszt]

        // ✅ DOBRE - w miarach używamy funkcji agregujących
        Marża PLN = 
        <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto]) - <span class='dax-function'>SUM</span>(Sprzedaż[Koszt])

        // ❌ ZŁE - próba mnożenia kolumn
        Wartość z VAT = Sprzedaż[Wartość netto] * <span class='dax-number'>1.23</span>

        // ✅ DOBRE - suma z mnożnikiem
        Wartość z VAT = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto]) * <span class='dax-number'>1.23</span>

        // ❌ ZŁE - bezpośrednie dzielenie kolumn
        Marża % = 
        (Sprzedaż[Wartość netto] - Sprzedaż[Koszt]) / Sprzedaż[Wartość netto]

        // ✅ DOBRE - dzielenie zagregowanych wartości
        Marża % = 
        <span class='dax-function'>DIVIDE</span>(
            <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto]) - <span class='dax-function'>SUM</span>(Sprzedaż[Koszt]),
            <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto])
        )</code></pre>
        <p><strong>W miarach:</strong></p>
        <ul>
        <li>❌ <strong>NIE MOŻESZ</strong> bezpośrednio mnożyć/dzielić kolumn</li>
        <li>❌ <strong>NIE MOŻESZ</strong> używać <code>Tabela[Kolumna]</code> bez funkcji agregującej</li>
        <li>✅ <strong>MUSISZ</strong> najpierw zagregować: <code>SUM()</code>, <code>AVERAGE()</code>, <code>COUNT()</code>, itp.</li>
        <li>✅ Dopiero <strong>zagregowane wartości</strong> możesz mnożyć, dzielić, dodawać</li>
        </ul>
        <p><strong>Kiedy używać miar:</strong></p>
        <ul>
        <li>Potrzebujesz <strong>agregacji</strong> (suma, średnia, liczba)</li>
        <li>Wynik ma zależeć od <strong>filtrów w raporcie</strong></li>
        <li>Chcesz <strong>dynamicznych obliczeń</strong> (procent udziału, porównania okresów)</li>
        <li>Przykład: suma sprzedaży, średnia wartość, liczba transakcji</li>
        </ul>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Porównanie: Kolumna kalkulowana vs Miara</h1>
        <table>
          <thead>
            <tr>
              <th>Aspekt</th>
              <th>Kolumna kalkulowana</th>
              <th>Miara</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Kiedy obliczana</strong></td>
              <td>Podczas odświeżania danych</td>
              <td>Podczas wyświetlania wizualizacji</td>
            </tr>
            <tr>
              <td><strong>Kontekst</strong></td>
              <td>Kontekst wiersza (row context)</td>
              <td>Kontekst filtrów (filter context)</td>
            </tr>
            <tr>
              <td><strong>Składnia DAX</strong></td>
              <td>Bezpośrednie odwołania do kolumn</td>
              <td>Wymagane funkcje agregujące</td>
            </tr>
            <tr>
              <td><strong>Operacje na kolumnach</strong></td>
              <td>Możesz mnożyć/dzielić kolumny bezpośrednio</td>
              <td>Musisz najpierw zagregować, potem mnożyć/dzielić</td>
            </tr>
            <tr>
              <td><strong>Przechowywanie</strong></td>
              <td>Tak - zajmuje miejsce w pamięci</td>
              <td>Nie - obliczana na żądanie</td>
            </tr>
            <tr>
              <td><strong>Użycie w slicerach</strong></td>
              <td>Tak</td>
              <td>Nie</td>
            </tr>
            <tr>
              <td><strong>Użycie w wizualizacjach</strong></td>
              <td>Jako pole do grupowania</td>
              <td>Jako wartość do agregacji</td>
            </tr>
            <tr>
              <td><strong>Ikona w Power BI</strong></td>
              <td>Ikona tabeli (⚏)</td>
              <td>Ikona kalkulatora (fx)</td>
            </tr>
          </tbody>
        </table>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'cd2ce545';
    var containerId = 'viz_' + vizId;

    var currentPage_cd2ce545 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_cd2ce545'] = function(n) {
        if (n > totalPages) currentPage_cd2ce545 = totalPages;
        if (n < 1) currentPage_cd2ce545 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_cd2ce545 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_cd2ce545;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_cd2ce545 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_cd2ce545 === totalPages);
    };

    window['changePage_cd2ce545'] = function(n) {
        currentPage_cd2ce545 += n;
        window['showPage_cd2ce545'](currentPage_cd2ce545);
    };

    // Inicjalizacja
    window['showPage_cd2ce545'](1);

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
            lineageTag: ef6eac26-da7a-4d2c-9d65-448389c996e0

        measure '02. Miary vs Kolumny kalkulowane - Pułapki' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Pułapki</title>
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

<div class='container' id='viz_8c56120f'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_8c56120f' onclick='changePage_8c56120f(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_8c56120f'>1</span> z <span id='totalPages_8c56120f'>3</span>
        </span>
        <button id='nextBtn_8c56120f' onclick='changePage_8c56120f(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Najczęstsze błędy początkujących</h1>
        <h2>Błąd 1: Tworzenie kolumny zamiast miary dla agregacji</h2>
        <pre><code>// ❌ ZŁE - kolumna kalkulowana (niepotrzebnie zajmuje pamięć)
        Suma Wartości Kolumna = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto])

        // ✅ DOBRE - miara (dynamiczna, nie zajmuje pamięci)
        Suma Wartości Miara = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto])</code></pre>
        <h2>Błąd 2: Próba mnożenia kolumn w miarze</h2>
        <pre><code>// ❌ ZŁE - nie zadziała w miarze
        Wartość Brutto = Sprzedaż[Wartość netto] * <span class='dax-number'>1.23</span>

        // ✅ DOBRE - agreguj najpierw
        Wartość Brutto = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto]) * <span class='dax-number'>1.23</span>

        // ✅ ALBO użyj SUMX dla wiersz-po-wierszu
        Wartość Brutto = <span class='dax-function'>SUMX</span>(Sprzedaż, Sprzedaż[Wartość netto] * <span class='dax-number'>1.23</span>)</code></pre>
        <h2>Błąd 3: Zapominanie o agregacji w miarach</h2>
        <pre><code>// ❌ ZŁE - w miarze musisz agregować
        Średnia Cena = Sprzedaż[Wartość netto] / Sprzedaż[Ilość]

        // ✅ DOBRE opcja <span class='dax-number'>1</span> - zagregowane dzielenie
        Średnia Cena = 
        <span class='dax-function'>DIVIDE</span>(
            <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto]),
            <span class='dax-function'>SUM</span>(Sprzedaż[Ilość])
        )

        // ✅ DOBRE opcja <span class='dax-number'>2</span> - iteracyjne obliczenie średniej
        Średnia Cena = 
        <span class='dax-function'>AVERAGEX</span>(
            Sprzedaż,
            <span class='dax-function'>DIVIDE</span>(Sprzedaż[Wartość netto], Sprzedaż[Ilość])
        )</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Kiedy używać czego? - Decyzja</h1>
        <p><strong>Użyj kolumny kalkulowanej gdy:</strong></p>
        <ul>
        <li>✓ Potrzebujesz wartości do <strong>filtrowania</strong> (slicer, filtr)</li>
        <li>✓ Chcesz <strong>grupować</strong> według obliczonej wartości</li>
        <li>✓ Wartość zależy tylko od <strong>bieżącego wiersza</strong></li>
        <li>✓ Możesz zapisać DAX <strong>bez funkcji agregujących</strong></li>
        <li>✓ Przykład: 'Kategoria wiekowa klienta', 'Dzień tygodnia sprzedaży', 'Rabat kwotowy'</li>
        </ul>
        <p><strong>Użyj miary gdy:</strong></p>
        <ul>
        <li>✓ Potrzebujesz <strong>agregacji</strong> (suma, średnia, liczba)</li>
        <li>✓ Wynik ma być <strong>dynamiczny</strong> (zależny od filtrów)</li>
        <li>✓ Chcesz <strong>oszczędzić pamięć</strong> w modelu</li>
        <li>✓ W formule używasz <code>SUM()</code>, <code>AVERAGE()</code>, <code>COUNT()</code>, itp.</li>
        <li>✓ Przykład: 'Suma sprzedaży', 'Liczba transakcji', 'Średnia wartość', '% udział'</li>
        </ul>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Złota zasada</h1>
        <p>> <strong>Jeśli w formule używasz funkcji agregującej (<code>SUM</code>, <code>AVERAGE</code>, <code>COUNT</code>, itp.), prawie zawsze powinieneś tworzyć MIARĘ, nie kolumnę.</strong></p>
        <p>> <strong>Jeśli możesz napisać formułę bez agregacji, tylko prostym odwołaniem do kolumn (jak w Excelu), prawdopodobnie potrzebujesz KOLUMNY.</strong></p>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '8c56120f';
    var containerId = 'viz_' + vizId;

    var currentPage_8c56120f = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_8c56120f'] = function(n) {
        if (n > totalPages) currentPage_8c56120f = totalPages;
        if (n < 1) currentPage_8c56120f = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_8c56120f - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_8c56120f;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_8c56120f === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_8c56120f === totalPages);
    };

    window['changePage_8c56120f'] = function(n) {
        currentPage_8c56120f += n;
        window['showPage_8c56120f'](currentPage_8c56120f);
    };

    // Inicjalizacja
    window['showPage_8c56120f'](1);

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
            lineageTag: 7550482b-cf2e-42e7-9772-76298a761ff7

        measure '02. Miary vs Kolumny kalkulowane - Różnice podejśc' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Różnice podejśc</title>
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

<div class='container' id='viz_f700bd9f'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_f700bd9f' onclick='changePage_f700bd9f(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_f700bd9f'>1</span> z <span id='totalPages_f700bd9f'>2</span>
        </span>
        <button id='nextBtn_f700bd9f' onclick='changePage_f700bd9f(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Kluczowa różnica w podejściu do DAX</h1>
        <h2>W kolumnach: 'Myśl wierszami'</h2>
        <pre><code>// Pracujesz na JEDNYM wierszu naraz
        // Możesz traktować kolumny jak zmienne

        Rabat Kwotowy = Sprzedaż[Cena] * Sprzedaż[Procent rabatu]

        Wartość końcowa = Sprzedaż[Cena] - Sprzedaż[Rabat Kwotowy]

        Kategoria = 
        <span class='dax-function'>SWITCH</span>(
            <span class='dax-function'>TRUE</span>(),
            Sprzedaż[Wartość] &lt; <span class='dax-number'>100</span>, 'Niska',
            Sprzedaż[Wartość] &lt; <span class='dax-number'>500</span>, 'Średnia',
            'Wysoka'
        )</code></pre>
        <h2>W miarach: 'Myśl agregacją'</h2>
        <p>Najprościej mówiąc, w miarach:</p>
        <ul>
        <li>Pracujesz na ZBIORZE wierszy</li>
        <li>Musisz najpierw zagregować, potem obliczać</li>
        </ul>
        <pre><code>// ❌ To nie zadziała:
        Rabat Kwotowy = Sprzedaż[Cena] * Sprzedaż[Procent rabatu]

        // ✅ Tak trzeba:
        Rabat Kwotowy = <span class='dax-function'>SUMX</span>(Sprzedaż, Sprzedaż[Cena] * Sprzedaż[Procent rabatu])
        // lub
        Rabat Kwotowy = <span class='dax-function'>SUM</span>(Sprzedaż[Cena]) * <span class='dax-function'>AVERAGE</span>(Sprzedaż[Procent rabatu])</code></pre>
        <p><strong>Uwaga!</strong></p>
        <ul>
        <li>Licząc z <code>SUMX</code> obliczasz: (1000 × 10%) + (2000 × 5%) + (500 × 20%) = 100 + 100 + 100 = <strong>300</strong></li>
        <li>Natomiast z <code>SUM</code> i <code>AVERAGE</code>: (1000 + 2000 + 500) × (10%, 5%, 20%) / 3 = <strong>408</strong></li>
        </ul>
        <p>	- W pierwszym przypadku otrzymujemy sumę kwoty rabatów, a w drugim kwotę dla przeciętnego rabatu</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Praktyczny przykład różnicy</h1>
        <h2>Scenariusz: Obliczenie marży</h2>
        <p><strong>Tabela Sprzedaż:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Produkt</th>
              <th>Wartość netto</th>
              <th>Koszt</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>A</td>
              <td>1000</td>
              <td>600</td>
            </tr>
            <tr>
              <td>B</td>
              <td>2000</td>
              <td>1400</td>
            </tr>
            <tr>
              <td>C</td>
              <td>500</td>
              <td>350</td>
            </tr>
          </tbody>
        </table>
        <h2>Jako kolumna kalkulowana:</h2>
        <pre><code>Marża PLN = Sprzedaż[Wartość netto] - Sprzedaż[Koszt]</code></pre>
        <p><strong>Wynik w tabeli:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Produkt</th>
              <th>Wartość netto</th>
              <th>Koszt</th>
              <th>Marża PLN</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>A</td>
              <td>1000</td>
              <td>600</td>
              <td><strong>400</strong></td>
            </tr>
            <tr>
              <td>B</td>
              <td>2000</td>
              <td>1400</td>
              <td><strong>600</strong></td>
            </tr>
            <tr>
              <td>C</td>
              <td>500</td>
              <td>350</td>
              <td><strong>150</strong></td>
            </tr>
          </tbody>
        </table>
        <ul>
        <li>Obliczona dla <strong>każdego wiersza</strong> osobno</li>
        <li>Wartości zapisane w modelu</li>
        <li>Możesz filtrować: 'pokaż produkty gdzie Marża PLN > 500'</li>
        </ul>
        <h2>Jako miara:</h2>
        <pre><code>Marża PLN = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto]) - <span class='dax-function'>SUM</span>(Sprzedaż[Koszt])</code></pre>
        <p><strong>Wynik na wizualizacji:</strong></p>
        <ul>
        <li>Bez filtrów: <strong>1150</strong> (suma wszystkich marż)</li>
        <li>Dla produktu A: <strong>400</strong></li>
        <li>Dla produktu B: <strong>600</strong></li>
        <li>Według kategorii: suma marż w każdej kategorii</li>
        <li>Obliczana <strong>dynamicznie</strong> według kontekstu</li>
        <li>Nie zajmuje miejsca w pamięci</li>
        <li><strong>Nie możesz</strong> filtrować wierszy według tej wartości</li>
        </ul>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'f700bd9f';
    var containerId = 'viz_' + vizId;

    var currentPage_f700bd9f = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_f700bd9f'] = function(n) {
        if (n > totalPages) currentPage_f700bd9f = totalPages;
        if (n < 1) currentPage_f700bd9f = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_f700bd9f - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_f700bd9f;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_f700bd9f === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_f700bd9f === totalPages);
    };

    window['changePage_f700bd9f'] = function(n) {
        currentPage_f700bd9f += n;
        window['showPage_f700bd9f'](currentPage_f700bd9f);
    };

    // Inicjalizacja
    window['showPage_f700bd9f'](1);

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
            lineageTag: 1f1217f1-2550-484a-8d3e-b26c221b5af9

        measure '02. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: Miary vs Kolumny kalkulowane</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>8</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Kiedy są obliczane kolumny kalkulowane?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Przy każdym odświeżeniu wizualizacji
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Tylko raz przy ładowaniu danych
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Gdy użytkownik zmieni filtr
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) W momencie tworzenia raportu
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Kiedy są obliczane miary (measures)?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Tylko raz przy ładowaniu danych
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) Dynamicznie przy każdym odświeżeniu wizualizacji
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) Co godzinę automatycznie
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) Nigdy - są predefiniowane
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Która struktura zajmuje więcej miejsca w pamięci?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) Miary
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) Kolumny kalkulowane
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) Obie zajmują tyle samo
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) Zależy od typu danych
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Czy w kolumnie kalkulowanej możesz użyć funkcji agregujących jak SUM()?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) Tak, bez ograniczeń
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) Nie, to spowoduje błąd
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) Tak, ale musisz użyć funkcji iteracyjnych jak SUMX()
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) Tylko w połączeniu z CALCULATE
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Jaki kontekst domyślnie działa w miarach?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) Kontekst wiersza
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) Kontekst filtru
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Kontekst całej tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Brak kontekstu
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Czy możesz użyć miary w formule kolumny kalkulowanej?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) Tak, zawsze
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Nie, to niemożliwe
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Tak, ale wartość miary będzie obliczona w kontekście wiersza
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) Tylko w funkcji CALCULATE
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Co jest lepszym wyborem dla obliczeń, które muszą reagować na filtry użytkownika?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(6, 0)'>
                A) Kolumna kalkulowana
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 1)'>
                B) Miara
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 2)'>
                C) Obie są równie dobre
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 3)'>
                D) Kolumna fizyczna w źródle danych
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(6, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-6'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/7</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 8;
    const totalQuestions = 7;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [1, 1, 1, 2, 1, 2, 1];
    
    const explanations = [
        'Prawidłowa odpowiedź: B. Kolumny kalkulowane są obliczane tylko raz - podczas ładowania lub odświeżania danych. Ich wartości są przechowywane w modelu danych.',
        'Prawidłowa odpowiedź: B. Miary są obliczane dynamicznie przy każdym odświeżeniu wizualizacji, reagując na aktualny kontekst filtrów i wyboru użytkownika.',
        'Prawidłowa odpowiedź: B. Kolumny kalkulowane przechowują wartość dla każdego wiersza w tabeli, co zajmuje pamięć. Miary nie przechowują danych - obliczają wyniki na żądanie.',
        'Prawidłowa odpowiedź: C. W kolumnach kalkulowanych musisz używać funkcji iteracyjnych (SUMX, AVERAGEX) zamiast zwykłych funkcji agregujących (SUM, AVERAGE), ponieważ kontekst wiersza wymaga iteracji.',
        'Prawidłowa odpowiedź: B. Miary domyślnie działają w kontekście filtru, reagując na filtry nałożone przez wizualizacje, slicery i inne filtry w raporcie.',
        'Prawidłowa odpowiedź: C. Możesz użyć miary w kolumnie kalkulowanej, ale miara będzie obliczona w kontekście wiersza dla każdego wiersza osobno.',
        'Prawidłowa odpowiedź: B. Miary są dynamiczne i automatycznie reagują na zmiany filtrów, co czyni je idealnym wyborem dla obliczeń zależnych od kontekstu użytkownika.'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: 230f8130-477d-447b-ac75-8b7a33273656

        measure '02a. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: Miary vs Kolumny kalkulowane</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>8</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Kiedy są obliczane kolumny kalkulowane?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Przy każdym odświeżeniu wizualizacji
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Tylko raz przy ładowaniu danych
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Gdy użytkownik zmieni filtr
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) W momencie tworzenia raportu
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Kiedy są obliczane miary (measures)?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Tylko raz przy ładowaniu danych
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) Dynamicznie przy każdym odświeżeniu wizualizacji
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) Co godzinę automatycznie
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) Nigdy - są predefiniowane
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Która struktura zajmuje więcej miejsca w pamięci?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) Miary
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) Kolumny kalkulowane
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) Obie zajmują tyle samo
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) Zależy od typu danych
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Czy w kolumnie kalkulowanej możesz użyć funkcji agregujących jak SUM()?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) Tak, bez ograniczeń
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) Nie, to spowoduje błąd
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) Tak, ale musisz użyć funkcji iteracyjnych jak SUMX()
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) Tylko w połączeniu z CALCULATE
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Jaki kontekst domyślnie działa w miarach?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) Kontekst wiersza
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) Kontekst filtru
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Kontekst całej tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Brak kontekstu
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Czy możesz użyć miary w formule kolumny kalkulowanej?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) Tak, zawsze
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Nie, to niemożliwe
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Tak, ale wartość miary będzie obliczona w kontekście wiersza
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) Tylko w funkcji CALCULATE
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Co jest lepszym wyborem dla obliczeń, które muszą reagować na filtry użytkownika?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(6, 0)'>
                A) Kolumna kalkulowana
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 1)'>
                B) Miara
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 2)'>
                C) Obie są równie dobre
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 3)'>
                D) Kolumna fizyczna w źródle danych
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(6, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-6'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/7</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 8;
    const totalQuestions = 7;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [1, 1, 1, 2, 1, 2, 1];
    
    const explanations = [
        'Prawidłowa odpowiedź: B. Kolumny kalkulowane są obliczane tylko raz - podczas ładowania lub odświeżania danych. Ich wartości są przechowywane w modelu danych.',
        'Prawidłowa odpowiedź: B. Miary są obliczane dynamicznie przy każdym odświeżeniu wizualizacji, reagując na aktualny kontekst filtrów i wyboru użytkownika.',
        'Prawidłowa odpowiedź: B. Kolumny kalkulowane przechowują wartość dla każdego wiersza w tabeli, co zajmuje pamięć. Miary nie przechowują danych - obliczają wyniki na żądanie.',
        'Prawidłowa odpowiedź: C. W kolumnach kalkulowanych musisz używać funkcji iteracyjnych (SUMX, AVERAGEX) zamiast zwykłych funkcji agregujących (SUM, AVERAGE), ponieważ kontekst wiersza wymaga iteracji.',
        'Prawidłowa odpowiedź: B. Miary domyślnie działają w kontekście filtru, reagując na filtry nałożone przez wizualizacje, slicery i inne filtry w raporcie.',
        'Prawidłowa odpowiedź: C. Możesz użyć miary w kolumnie kalkulowanej, ale miara będzie obliczona w kontekście wiersza dla każdego wiersza osobno.',
        'Prawidłowa odpowiedź: B. Miary są dynamiczne i automatycznie reagują na zmiany filtrów, co czyni je idealnym wyborem dla obliczeń zależnych od kontekstu użytkownika.'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: 811dd5e3-7c05-47d7-8227-fe5c00b956d6

        measure '03. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: Wprowadzenie do CALCULATE</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>8</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Do czego służy funkcja CALCULATE?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Do obliczania sum i średnich
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Do modyfikowania kontekstu filtrów
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Do tworzenia kalkulowanych kolumn
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) Do formatowania liczb
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Jaka jest podstawowa składnia funkcji CALCULATE?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) CALCULATE(wyrażenie, filtr1, filtr2, ...)
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) CALCULATE(tabela, warunek)
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) CALCULATE(kolumna = wartość)
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) CALCULATE(miara + filtr)
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Co zrobi CALCULATE bez żadnych filtrów: CALCULATE([Suma Sprzedaży])?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) Zwróci błąd
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) Zwróci wartość identyczną jak [Suma Sprzedaży]
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) Usunie wszystkie filtry
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) Zastosuje filtr dla całej tabeli
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Jak obliczyć sprzedaż tylko dla kategorii 'Elektronika'?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) CALCULATE([Suma], Produkty[Kategoria] = 'Elektronika')
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) CALCULATE([Suma], FILTER(Produkty, 'Elektronika'))
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) CALCULATE([Suma] WHERE Kategoria = 'Elektronika')
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) SUM(Produkty[Sprzedaż], 'Elektronika')
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Czy w CALCULATE możesz zastosować wiele filtrów jednocześnie?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) Nie, tylko jeden filtr na raz
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) Tak, filtry są łączone operatorem AND
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Tak, filtry są łączone operatorem OR
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Tak, ale maksymalnie 3 filtry
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Co robi funkcja FILTER w połączeniu z CALCULATE?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) Usuwa filtry z tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Tworzy tabelę z wierszami spełniającymi warunek
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Agreguje wartości
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) Sortuje dane
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Jaki będzie wynik: CALCULATE([Sprzedaż], Produkty[Cena] &gt; 100, Produkty[Kategoria] = 'AGD')?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(6, 0)'>
                A) Sprzedaż produktów z kategorii AGD
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 1)'>
                B) Sprzedaż produktów droższych niż 100
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 2)'>
                C) Sprzedaż produktów z kategorii AGD, które kosztują więcej niż 100
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 3)'>
                D) Błąd składni
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(6, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-6'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/7</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 8;
    const totalQuestions = 7;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [1, 0, 1, 0, 1, 1, 2];
    
    const explanations = [
        'Prawidłowa odpowiedź: B. CALCULATE to najpotężniejsza funkcja w DAX, która pozwala modyfikować kontekst filtrów, w którym obliczana jest miara.',
        'Prawidłowa odpowiedź: A. Składnia to CALCULATE(wyrażenie, filtr1, filtr2, ...), gdzie wyrażenie to obliczana miara, a następne argumenty to filtry modyfikujące kontekst.',
        'Prawidłowa odpowiedź: B. CALCULATE bez dodatkowych filtrów zwróci tę samą wartość co samo wyrażenie. Jednak jest to przydatne, gdy chcemy przekształcić kontekst wiersza w kontekst filtru.',
        'Prawidłowa odpowiedź: A. Składnia to CALCULATE([Miara], Tabela[Kolumna] = wartość). Możemy też użyć FILTER, ale prostsza składnia jest bardziej czytelna dla pojedynczych warunków.',
        'Prawidłowa odpowiedź: B. CALCULATE może przyjmować wiele filtrów oddzielonych przecinkami. Wszystkie filtry są łączone operatorem AND (muszą być spełnione jednocześnie).',
        'Prawidłowa odpowiedź: B. FILTER zwraca tabelę zawierającą tylko te wiersze, które spełniają podany warunek. W CALCULATE używamy jej do bardziej złożonych warunków filtrowania.',
        'Prawidłowa odpowiedź: C. Oba filtry są łączone operatorem AND, więc wynik to sprzedaż produktów spełniających OBA warunki: kategoria = AGD ORAZ cena > 100.'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: 78ff4446-fa91-4fb0-a631-8d8f2f5d9819

        measure '03. Wprowadzenie do CALCULATE - Operatory logiczne w `CALCULATE`' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Operatory logiczne w `CALCULATE`</title>
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

<div class='container' id='viz_b9c59316'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_b9c59316' onclick='changePage_b9c59316(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_b9c59316'>1</span> z <span id='totalPages_b9c59316'>5</span>
        </span>
        <button id='nextBtn_b9c59316' onclick='changePage_b9c59316(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <p>Często potrzebujesz zastosować wiele warunków jednocześnie. DAX oferuje kilka sposobów na łączenie warunków.</p>
        <h2>Operatory logiczne w DAX</h2>
        <table>
          <thead>
            <tr>
              <th>Operator</th>
              <th>Znaczenie</th>
              <th>Przykład</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>=</code></td>
              <td>Równe</td>
              <td><code>dKategorie[Kategoria] = 'NAPOJE'</code></td>
            </tr>
            <tr>
              <td><code><></code></td>
              <td>Różne od</td>
              <td><code>dKategorie[Kategoria] <> 'NAPOJE'</code></td>
            </tr>
            <tr>
              <td><code>></code></td>
              <td>Większe niż</td>
              <td><code>fSprzedaz[Kwota] > 50</code></td>
            </tr>
            <tr>
              <td><code>>=</code></td>
              <td>Większe lub równe</td>
              <td><code>fSprzedaz[Kwota] >= 50</code></td>
            </tr>
            <tr>
              <td><code><</code></td>
              <td>Mniejsze niż</td>
              <td><code>fSprzedaz[Kwota] < 100</code></td>
            </tr>
            <tr>
              <td><code><=</code></td>
              <td>Mniejsze lub równe</td>
              <td><code>fSprzedaz[Kwota] <= 100</code></td>
            </tr>
            <tr>
              <td><code>&&</code></td>
              <td>Logiczne AND (i)</td>
              <td><code>fSprzedaz[Kwota] > 50 && fSprzedaz[Kwota] < 100</code></td>
            </tr>
            <tr>
              <td>`\</td>
              <td>`</td>
              <td>Logiczne OR (lub)</td>
              <td>`dKategorie[Kategoria] = 'NAPOJE' \</td>
              <td>dKategorie[Kategoria] = 'SŁODYCZE'`</td>
            </tr>
            <tr>
              <td><code>IN</code></td>
              <td>W zestawie wartości</td>
              <td><code>dKategorie[Kategoria] IN {'NAPOJE', 'SŁODYCZE'}</code></td>
            </tr>
            <tr>
              <td><code>&</code></td>
              <td>Łączenie tekstu</td>
              <td><code>'Kategoria: ' & dKategorie[Kategoria]</code></td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>Operator AND (<code>&&</code>)</h2>
        <p>Używamy gdy <strong>wszystkie</strong> warunki muszą być spełnione jednocześnie.</p>
        <p><strong>Przykład: Sprzedaż w dni robocze</strong></p>
        <p>Załóżmy, że w tabeli dKalendarz mamy kolumnę <code>DzienTygodnia</code> (dzień tygodnia: 1 = poniedziałek, ..., 7 = niedziela).</p>
        <pre><code>Sprzedaż Dni Robocze =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKalendarz[DzienTygodnia] &gt;= <span class='dax-number'>1</span> &&
            dKalendarz[DzienTygodnia] &lt;= <span class='dax-number'>5</span>
        )</code></pre>
        <p><strong>Warunek:</strong> <code>DzienTygodnia >= 1</code> <strong>I</strong> <code>DzienTygodnia <= 5</code></p>
        <p>Alternatywna składnia z funkcją AND():</p>
        <pre><code>Sprzedaż Dni Robocze (Alternatywna) =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            <span class='dax-function'>AND</span>(
        	    dKalendarz[DzienTygodnia] &gt;= <span class='dax-number'>1</span>,
        	    dKalendarz[DzienTygodnia] &lt;= <span class='dax-number'>5</span>
             )
        )</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Operator OR (<code>||</code>)</h2>
        <p>Używamy gdy <strong>przynajmniej jeden</strong> z warunków musi być spełniony.</p>
        <p><strong>Przykład: Sprzedaż w weekendy</strong></p>
        <pre><code>Sprzedaż Weekendy =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKalendarz[DzienTygodnia] = <span class='dax-number'>6</span> ||
            dKalendarz[DzienTygodnia] = <span class='dax-number'>7</span>
        )</code></pre>
        <p><strong>Warunek:</strong> <code>DzienTygodnia = 6</code> <strong>LUB</strong> <code>DzienTygodnia = 7</code></p>
        <p>Alternatywna składnia z funkcją OR():</p>
        <pre><code>Sprzedaż Weekendy (Alternatywna) =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            <span class='dax-function'>OR</span>(
        	    dKalendarz[DzienTygodnia] = <span class='dax-number'>6</span>,
        	    dKalendarz[DzienTygodnia] = <span class='dax-number'>7</span>
            )
        )</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>Operator IN - eleganckie sprawdzanie wielu wartości</h2>
        <p>Zamiast pisać wielokrotnie OR, użyj operatora <code>IN</code>:</p>
        <pre><code>// ✗ Nieeleganckie
        Sprzedaż Napoje lub Słodycze =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKategorie[Kategoria] = 'NAPOJE' ||
            dKategorie[Kategoria] = 'SŁODYCZE'
        )

        // ✓ Eleganckie
        Sprzedaż Napoje lub Słodycze =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKategorie[Kategoria] IN
             {'NAPOJE', 'SŁODYCZE'}
        )</code></pre>
        <p><strong>Operator IN</strong> sprawdza, czy wartość znajduje się w podanym zestawie.</p>

    </div>

    <!-- Strona 5 -->
    <div class='page'>
        <h2>Łączenie operatorów AND i OR</h2>
        <p>Możesz łączyć różne operatory:</p>
        <pre><code>Wysoka Sprzedaż Napojów =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKategorie[Kategoria] = 'NAPOJE' &&
            fSprzedaz[Kwota] &gt;= <span class='dax-number'>100</span>
        )</code></pre>
        <p><strong>Warunek:</strong> Kategoria = 'NAPOJE' <strong>I</strong> Kwota >= 100</p>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'b9c59316';
    var containerId = 'viz_' + vizId;

    var currentPage_b9c59316 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_b9c59316'] = function(n) {
        if (n > totalPages) currentPage_b9c59316 = totalPages;
        if (n < 1) currentPage_b9c59316 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_b9c59316 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_b9c59316;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_b9c59316 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_b9c59316 === totalPages);
    };

    window['changePage_b9c59316'] = function(n) {
        currentPage_b9c59316 += n;
        window['showPage_b9c59316'](currentPage_b9c59316);
    };

    // Inicjalizacja
    window['showPage_b9c59316'](1);

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
            lineageTag: db01c54b-f07f-4eab-bea8-1fc95e419a38

        measure '03. Wprowadzenie do CALCULATE - PODSUMOWANIE' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>PODSUMOWANIE</title>
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

<div class='container' id='viz_1f337895'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_1f337895' onclick='changePage_1f337895(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_1f337895'>1</span> z <span id='totalPages_1f337895'>1</span>
        </span>
        <button id='nextBtn_1f337895' onclick='changePage_1f337895(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Podsumowanie <code>CALCULATE</code></h1>
        <p><strong>CALCULATE</strong> to fundament zaawansowanych obliczeń w DAX:</p>
        <ul>
        <li>Pozwala tworzyć <strong>dynamiczne miary</strong></li>
        <li>Umożliwia <strong>porównania</strong> między różnymi okresami/kategoriami</li>
        <li>Daje kontrolę nad <strong>kontekstem filtrowania</strong></li>
        <li>Jest podstawą funkcji time intelligence (SAMEPERIODLASTYEAR, DATEADD, itd.)</li>
        </ul>
        <p><strong>Zapamiętaj:</strong> Jeśli chcesz obliczyć coś w <strong>innym kontekście</strong> niż aktualny, prawdopodobnie potrzebujesz <strong>CALCULATE</strong>.</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '1f337895';
    var containerId = 'viz_' + vizId;

    var currentPage_1f337895 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_1f337895'] = function(n) {
        if (n > totalPages) currentPage_1f337895 = totalPages;
        if (n < 1) currentPage_1f337895 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_1f337895 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_1f337895;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_1f337895 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_1f337895 === totalPages);
    };

    window['changePage_1f337895'] = function(n) {
        currentPage_1f337895 += n;
        window['showPage_1f337895'](currentPage_1f337895);
    };

    // Inicjalizacja
    window['showPage_1f337895'](1);

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
            lineageTag: d01ecf62-408c-4802-ac16-4fcaafc79e84

        measure '03. Wprowadzenie do CALCULATE - Użycie `CALCULATE`' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Użycie `CALCULATE`</title>
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

<div class='container' id='viz_603da463'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_603da463' onclick='changePage_603da463(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_603da463'>1</span> z <span id='totalPages_603da463'>3</span>
        </span>
        <button id='nextBtn_603da463' onclick='changePage_603da463(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h2>Przykład 1: Dodanie filtra</h2>
        <pre><code>Sprzedaż Netto - Napoje =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKategorie[Kategoria] = 'NAPOJE'
        )</code></pre>
        <p><strong>Co się dzieje:</strong></p>
        <ul>
        <li>Bierze miarę <code>[Sprzedaż Netto]</code></li>
        <li>Dodaje filtr: tylko dla kategorii 'NAPOJE'</li>
        <li>Zwraca sumę tylko dla napojów <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209172007.png?raw=true' width='100%'></li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>Przykład 2: Wiele filtrów</h2>
        <pre><code>Sprzedaż VIP w <span class='dax-number'>2024</span> = 
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKlienci[Kategoria] = 'VIP',
            <span class='dax-function'>YEAR</span>(dKalendarz[Data]) = <span class='dax-number'>2024</span>
        )</code></pre>
        <p><strong>Filtry są łączone operatorem AND</strong> – muszą być <strong>oba</strong> spełnione.</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209172247.png?raw=true' width='100%'>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Przykład 3: Nadpisanie istniejącego filtra</h2>
        <p>A co jeżeli chcemy policzyć udział sprzedaży w sprzedaży ogółem?</p>
        <ul>
        <li>Jeżeli nałożymy na wizualizację kolumnę, tworzy ona kontekst filtra/kolumny</li>
        <li>Do pozbycia się kontekstu służy funkcja <code>REMOVEFILTERS()</code></li>
        </ul>
        <pre><code>Sprzedaż Netto - Cały Okres = 
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto], 
            <span class='dax-function'>REMOVEFILTERS</span>(dKalendarz)
        )</code></pre>
        <p><strong>Co robi <code>REMOVEFILTERS</code>?</strong></p>
        <ul>
        <li>Usuwa filtry z tabeli <code>dKalendarz</code></li>
        <li>Dzięki temu <code>Sprzedaż Netto - Cały Okres</code> pokazuje sumę dla <strong>wszystkich dni</strong>, niezależnie od tego, jaki kontekst <strong>Kalendarza</strong> zostanie nałożony na wizualizację</li>
        </ul>
        <p>Teraz wystarczy napisać miarę, która podzieli jedną wartość przez drugą.</p>
        <pre><code>Sprzedaż Netto - Udział w Sprzedaży = <span class='dax-function'>DIVIDE</span>(
            [Sprzedaż Netto],
            [Sprzedaż Netto - Cały Okres],
            <span class='dax-function'>BLANK</span>() <span class='dax-comment'>-- jeżeli dzielenie przez 0, to zwróć wartość pustą</span>
        )</code></pre>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209173050.png?raw=true' width='100%'>
        <p>> <strong>Ciekawostka:</strong> Funkcję <code>REMOVEFILTERS()</code> można używać zamiennie z funkcją <code>ALL()</code>. W tym przypadku ich zastosowanie jest identyczne, natomiast <code>ALL()</code> ma dodatkowe funkcjonalności, o których później.</p>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '603da463';
    var containerId = 'viz_' + vizId;

    var currentPage_603da463 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_603da463'] = function(n) {
        if (n > totalPages) currentPage_603da463 = totalPages;
        if (n < 1) currentPage_603da463 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_603da463 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_603da463;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_603da463 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_603da463 === totalPages);
    };

    window['changePage_603da463'] = function(n) {
        currentPage_603da463 += n;
        window['showPage_603da463'](currentPage_603da463);
    };

    // Inicjalizacja
    window['showPage_603da463'](1);

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
            lineageTag: 72e5f12c-391a-4989-9279-39e163a7d7c1

        measure '03. Wprowadzenie do CALCULATE - Wprowadzenie do CALCULATE' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Wprowadzenie do CALCULATE</title>
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

<div class='container' id='viz_a6296909'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_a6296909' onclick='changePage_a6296909(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_a6296909'>1</span> z <span id='totalPages_a6296909'>2</span>
        </span>
        <button id='nextBtn_a6296909' onclick='changePage_a6296909(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Czym jest <code>CALCULATE</code> i dlaczego jest najważniejsza w DAX</h1>
        <p><strong>CALCULATE</strong> to najpotężniejsza funkcja w języku DAX. Pozwala ona <strong>modyfikować kontekst filtrów</strong>, w którym obliczana jest miara.</p>
        <h2>Dlaczego <code>CALCULATE</code> jest tak ważna?</h2>
        <p>W poprzednim rozdziale nauczyliśmy się, że miary obliczają się dynamicznie w zależności od kontekstu filtrów. Funkcja CALCULATE pozwala:</p>
        <p>✓ <strong>Nadpisać</strong> istniejące filtry ✓ <strong>Dodać</strong> nowe filtry ✓ <strong>Usunąć</strong> filtry ✓ <strong>Zmienić</strong> sposób działania kontekstu</p>
        <p><strong>Innymi słowy:</strong> CALCULATE daje Ci pełną kontrolę nad tym, na jakich danych oblicza się Twoja miara.</p>
        <h2>Podstawowa składnia</h2>
        <pre><code><span class='dax-function'>CALCULATE</span>(
            &lt;wyrażenie&gt;,
            &lt;filtr1&gt;,
            &lt;filtr2&gt;,
            ...
        )</code></pre>
        <ul>
        <li><strong>wyrażenie</strong> - miara lub wyrażenie do obliczenia</li>
        <li><strong>filtr1, filtr2, ...</strong> - filtry, które mają być zastosowane</li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Czym jest kontekst filtrowania?</h1>
        <p><strong>Kontekst filtrowania</strong> to zbiór filtrów aktywnych w danym momencie obliczeń. Określa on <strong>jakie wiersze</strong> z tabel są brane pod uwagę.</p>
        <p><strong>Przykład:</strong> Jeśli na wizualizację naniesiesz kolumnę <code>Rok - Miesiac</code> i miarę <code>Sprzedaż Netto</code>, to</p>
        <ul>
        <li><code>Rok - Miesiac</code> staję się <strong>kontekstem filtrowania</strong></li>
        <li>Więc miara <code>Sprzedaż Netto</code> jest obliczana <strong>w kontekście kolumn</strong> <code>Rok - Miesiac</code> <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209173843.png?raw=true' width='100%'></li>
        </ul>
        <p>> W Power BI często określa się to terminami: kontekstu, filtra lub kontekstu filtra - można stosować je niemalże zamiennie</p>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'a6296909';
    var containerId = 'viz_' + vizId;

    var currentPage_a6296909 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_a6296909'] = function(n) {
        if (n > totalPages) currentPage_a6296909 = totalPages;
        if (n < 1) currentPage_a6296909 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_a6296909 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_a6296909;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_a6296909 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_a6296909 === totalPages);
    };

    window['changePage_a6296909'] = function(n) {
        currentPage_a6296909 += n;
        window['showPage_a6296909'](currentPage_a6296909);
    };

    // Inicjalizacja
    window['showPage_a6296909'](1);

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
            lineageTag: b1ae6915-fa59-42a8-aab2-32f250aa68f1

        measure '03a. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: Wprowadzenie do CALCULATE</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>8</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Do czego służy funkcja CALCULATE?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Do obliczania sum i średnich
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Do modyfikowania kontekstu filtrów
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Do tworzenia kalkulowanych kolumn
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) Do formatowania liczb
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Jaka jest podstawowa składnia funkcji CALCULATE?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) CALCULATE(wyrażenie, filtr1, filtr2, ...)
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) CALCULATE(tabela, warunek)
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) CALCULATE(kolumna = wartość)
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) CALCULATE(miara + filtr)
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Co zrobi CALCULATE bez żadnych filtrów: CALCULATE([Suma Sprzedaży])?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) Zwróci błąd
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) Zwróci wartość identyczną jak [Suma Sprzedaży]
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) Usunie wszystkie filtry
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) Zastosuje filtr dla całej tabeli
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Jak obliczyć sprzedaż tylko dla kategorii 'Elektronika'?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) CALCULATE([Suma], Produkty[Kategoria] = 'Elektronika')
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) CALCULATE([Suma], FILTER(Produkty, 'Elektronika'))
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) CALCULATE([Suma] WHERE Kategoria = 'Elektronika')
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) SUM(Produkty[Sprzedaż], 'Elektronika')
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Czy w CALCULATE możesz zastosować wiele filtrów jednocześnie?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) Nie, tylko jeden filtr na raz
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) Tak, filtry są łączone operatorem AND
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Tak, filtry są łączone operatorem OR
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Tak, ale maksymalnie 3 filtry
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Co robi funkcja FILTER w połączeniu z CALCULATE?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) Usuwa filtry z tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Tworzy tabelę z wierszami spełniającymi warunek
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Agreguje wartości
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) Sortuje dane
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Jaki będzie wynik: CALCULATE([Sprzedaż], Produkty[Cena] &gt; 100, Produkty[Kategoria] = 'AGD')?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(6, 0)'>
                A) Sprzedaż produktów z kategorii AGD
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 1)'>
                B) Sprzedaż produktów droższych niż 100
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 2)'>
                C) Sprzedaż produktów z kategorii AGD, które kosztują więcej niż 100
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 3)'>
                D) Błąd składni
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(6, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-6'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/7</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 8;
    const totalQuestions = 7;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [1, 0, 1, 0, 1, 1, 2];
    
    const explanations = [
        'Prawidłowa odpowiedź: B. CALCULATE to najpotężniejsza funkcja w DAX, która pozwala modyfikować kontekst filtrów, w którym obliczana jest miara.',
        'Prawidłowa odpowiedź: A. Składnia to CALCULATE(wyrażenie, filtr1, filtr2, ...), gdzie wyrażenie to obliczana miara, a następne argumenty to filtry modyfikujące kontekst.',
        'Prawidłowa odpowiedź: B. CALCULATE bez dodatkowych filtrów zwróci tę samą wartość co samo wyrażenie. Jednak jest to przydatne, gdy chcemy przekształcić kontekst wiersza w kontekst filtru.',
        'Prawidłowa odpowiedź: A. Składnia to CALCULATE([Miara], Tabela[Kolumna] = wartość). Możemy też użyć FILTER, ale prostsza składnia jest bardziej czytelna dla pojedynczych warunków.',
        'Prawidłowa odpowiedź: B. CALCULATE może przyjmować wiele filtrów oddzielonych przecinkami. Wszystkie filtry są łączone operatorem AND (muszą być spełnione jednocześnie).',
        'Prawidłowa odpowiedź: B. FILTER zwraca tabelę zawierającą tylko te wiersze, które spełniają podany warunek. W CALCULATE używamy jej do bardziej złożonych warunków filtrowania.',
        'Prawidłowa odpowiedź: C. Oba filtry są łączone operatorem AND, więc wynik to sprzedaż produktów spełniających OBA warunki: kategoria = AGD ORAZ cena > 100.'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: 7e4904ce-6699-4189-9a85-a404e799fa9f

        measure '04. Modyfikowanie Kontekstu - ALL i REMOVEFILTERS - usuwanie filtrów' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>ALL i REMOVEFILTERS - usuwanie filtrów</title>
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

<div class='container' id='viz_624e3a9b'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_624e3a9b' onclick='changePage_624e3a9b(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_624e3a9b'>1</span> z <span id='totalPages_624e3a9b'>3</span>
        </span>
        <button id='nextBtn_624e3a9b' onclick='changePage_624e3a9b(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h2>Czym jest ALL?</h2>
        <p>ALL usuwa filtry z tabeli lub kolumny. Mówisz silnikowi DAX: 'zignoruj wszelkie filtry, które użytkownik (lub inne miary) nałożył na ten obiekt'.</p>
        <pre><code><span class='dax-function'>ALL</span>(tabela)
        <span class='dax-function'>ALL</span>(tabela[kolumna])
        <span class='dax-function'>ALL</span>(tabela[kolumna1], tabela[kolumna2], ...)</code></pre>
        <h2>Podstawowy przypadek - procent od całości</h2>
        <p>Użytkownik wybiera w slicerze kategorię 'Computers'. Chcesz pokazać:</p>
        <ul>
        <li>Sprzedaż Computers: 400 000 zł</li>
        <li>Sprzedaż całkowita: 1 000 000 zł (mimo filtru!)</li>
        <li>Udział: 40%</li>
        </ul>
        <pre><code>Total fSprzedaż = <span class='dax-function'>SUM</span>(ffSprzedaż[fSprzedażAmount])

        Total fSprzedaż All Categories = 
        <span class='dax-function'>CALCULATE</span>(
            [Total fSprzedaż],
            <span class='dax-function'>ALL</span>(dProduct[ProductCategoryName])
        )

        fSprzedaż % = <span class='dax-function'>DIVIDE</span>([Total fSprzedaż], [Total fSprzedaż All Categories])</code></pre>
        <p>Co się dzieje:</p>
        <table>
          <thead>
            <tr>
              <th>Kontekst użytkownika</th>
              <th>[Total fSprzedaż]</th>
              <th>[Total fSprzedaż All Categories]</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Computers</td>
              <td>400 000 zł</td>
              <td>1 000 000 zł</td>
            </tr>
            <tr>
              <td>Cameras</td>
              <td>250 000 zł</td>
              <td>1 000 000 zł</td>
            </tr>
            <tr>
              <td>TV</td>
              <td>350 000 zł</td>
              <td>1 000 000 zł</td>
            </tr>
          </tbody>
        </table>
        <p><code>ALL(dProduct[ProductCategoryName])</code> mówi: 'usuń filtr z kategorii, ale zostaw inne filtry (np. na roku, kraju)'.</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>ALL na całej tabeli vs na kolumnie</h2>
        <ul>
        <li>Usuwa filtr <strong>TYLKO</strong> z kategorii</li>
        <li>Filtr na kraju, roku itp. nadal działa</li>
        </ul>
        <pre><code><span class='dax-function'>CALCULATE</span>(
        	[Total fSprzedaż],
        	<span class='dax-function'>ALL</span>(dProduct[ProductCategoryName])
        )</code></pre>
        <ul>
        <li> Usuwa <strong>WSZYSTKIE</strong> filtry z tabeli <strong>dProduct</strong></li>
        <li> Kolor, marka, podkategoria - wszystko zignorowane</li>
        </ul>
        <pre><code><span class='dax-function'>CALCULATE</span>(
        	[Total fSprzedaż],
        	 <span class='dax-function'>ALL</span>(dProduct)
         )</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>REMOVEFILTERS - nowszy odpowiednik ALL</h2>
        <p>Od 2019 roku mamy <code>REMOVEFILTERS</code>, który robi dokładnie to samo co <code>ALL</code> w kontekście <code>CALCULATE</code>:</p>
        <pre><code>// Te dwie miary są identyczne:
        <span class='dax-function'>CALCULATE</span>(
        	[Total fSprzedaż],
        	 <span class='dax-function'>ALL</span>(dProduct)
         )
        <span class='dax-function'>CALCULATE</span>(
        	[Total fSprzedaż],
        	 <span class='dax-function'>REMOVEFILTERS</span>(dProduct)
        )</code></pre>
        <p>Dlaczego <code>REMOVEFILTERS</code> jest lepszy?</p>
        <ol>
        <li>Nazwa jasno mówi co robi (usuwa filtry, nie 'wszystko')</li>
        <li><code>ALL</code> ma podwójne znaczenie - jako modyfikator filtra i jako funkcja tabelaryczna</li>
        <li>Czytelność kodu</li>
        </ol>
        <pre><code>// ALL jako funkcja tabelaryczna (zwraca tabelę bez filtrów)
        All Products Table = <span class='dax-function'>ALL</span>(dProduct)

        // ALL jako modyfikator w <span class='dax-function'>CALCULATE</span> (usuwa filtry)
        fSprzedaż Without Filter = <span class='dax-function'>CALCULATE</span>([Total fSprzedaż], <span class='dax-function'>ALL</span>(dProduct))

        // REMOVEFILTERS - jednoznaczne, tylko modyfikator
        fSprzedaż Without Filter = <span class='dax-function'>CALCULATE</span>([Total fSprzedaż], <span class='dax-function'>REMOVEFILTERS</span>(dProduct))</code></pre>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '624e3a9b';
    var containerId = 'viz_' + vizId;

    var currentPage_624e3a9b = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_624e3a9b'] = function(n) {
        if (n > totalPages) currentPage_624e3a9b = totalPages;
        if (n < 1) currentPage_624e3a9b = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_624e3a9b - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_624e3a9b;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_624e3a9b === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_624e3a9b === totalPages);
    };

    window['changePage_624e3a9b'] = function(n) {
        currentPage_624e3a9b += n;
        window['showPage_624e3a9b'](currentPage_624e3a9b);
    };

    // Inicjalizacja
    window['showPage_624e3a9b'](1);

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
            lineageTag: 6a7e8f5a-1060-4a0d-a0a4-eba605c4b320

        measure '04. Modyfikowanie Kontekstu - ALLEXCEPT' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>ALLEXCEPT</title>
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

<div class='container' id='viz_c3f109de'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_c3f109de' onclick='changePage_c3f109de(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_c3f109de'>1</span> z <span id='totalPages_c3f109de'>3</span>
        </span>
        <button id='nextBtn_c3f109de' onclick='changePage_c3f109de(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h2>Problem, który rozwiązuje ALLEXCEPT</h2>
        <p>Wyobraź sobie tabelę dProduct z kolumnami: ProductKey, ProductName, ProductCategoryName, ProductSubcategoryName, BrandName, Color, UnitPrice.</p>
        <p>Chcesz policzyć udział produktu w swojej kategorii. Potrzebujesz usunąć filtry z produktu, ale ZACHOWAĆ filtr kategorii.</p>
        <pre><code>// Podejście <span class='dax-number'>1</span>: wymieniasz wszystko co chcesz usunąć
        fSprzedaż Category Total v1 =
        <span class='dax-function'>CALCULATE</span>(
            [Total fSprzedaż],
            <span class='dax-function'>ALL</span>(
                dProduct[ProductKey],
                dProduct[ProductName],
                dProduct[ProductSubcategoryName],
                dProduct[BrandName],
                dProduct[Color],
                dProduct[UnitPrice]
            )
        )</code></pre>
        <p>Działa, ale jest nieczytelne i łatwo o pomyłkę. A co jeśli ktoś doda nową kolumnę do tabeli?</p>
        <pre><code>// Podejście <span class='dax-number'>2</span>: ALLEXCEPT
        fSprzedaż Category Total v2 =
        <span class='dax-function'>CALCULATE</span>(
            [Total fSprzedaż],
            <span class='dax-function'>ALLEXCEPT</span>(dProduct, dProduct[ProductCategoryName])
        )</code></pre>
        <p><code>ALLEXCEPT</code> mówi: 'usuń wszystkie filtry z dProduct OPRÓCZ filtra na ProductCategoryName'.</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>Wizualizacja działania</h2>
        <p>Raport pokazuje produkty w kategorii 'Computers':</p>
        <table>
          <thead>
            <tr>
              <th>Produkt</th>
              <th>[Total fSprzedaż]</th>
              <th>[fSprzedaż Category Total]</th>
              <th>Udział</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Laptop A</td>
              <td>150 000 zł</td>
              <td>400 000 zł</td>
              <td>37.5%</td>
            </tr>
            <tr>
              <td>Laptop B</td>
              <td>120 000 zł</td>
              <td>400 000 zł</td>
              <td>30.0%</td>
            </tr>
            <tr>
              <td>Desktop C</td>
              <td>130 000 zł</td>
              <td>400 000 zł</td>
              <td>32.5%</td>
            </tr>
          </tbody>
        </table>
        <p>Gdy użytkownik przełączy na kategorię 'Cameras':</p>
        <table>
          <thead>
            <tr>
              <th>Produkt</th>
              <th>[Total fSprzedaż]</th>
              <th>[fSprzedaż Category Total]</th>
              <th>Udział</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Camera X</td>
              <td>100 000 zł</td>
              <td>250 000 zł</td>
              <td>40.0%</td>
            </tr>
            <tr>
              <td>Camera Y</td>
              <td>150 000 zł</td>
              <td>250 000 zł</td>
              <td>60.0%</td>
            </tr>
          </tbody>
        </table>
        <p>Filtr kategorii jest respektowany - total zmienia się z 400 000 na 250 000.</p>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>ALLEXCEPT z wieloma kolumnami</h2>
        <p>Możesz zachować filtry na wielu kolumnach:</p>
        <pre><code>// Udział produktu w swojej kategorii I kraju
        fSprzedaż Category Country Total =
        <span class='dax-function'>CALCULATE</span>(
            [Total fSprzedaż],
            <span class='dax-function'>ALLEXCEPT</span>(
                dProduct,
                dProduct[ProductCategoryName]
            ),
            <span class='dax-function'>ALLEXCEPT</span>(
                dGeography,
                dGeography[RegionCountryName]
            )
        )</code></pre>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'c3f109de';
    var containerId = 'viz_' + vizId;

    var currentPage_c3f109de = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_c3f109de'] = function(n) {
        if (n > totalPages) currentPage_c3f109de = totalPages;
        if (n < 1) currentPage_c3f109de = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_c3f109de - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_c3f109de;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_c3f109de === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_c3f109de === totalPages);
    };

    window['changePage_c3f109de'] = function(n) {
        currentPage_c3f109de += n;
        window['showPage_c3f109de'](currentPage_c3f109de);
    };

    // Inicjalizacja
    window['showPage_c3f109de'](1);

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
            lineageTag: e1d34450-55d7-48c6-824e-5e0ef2c3a013

        measure '04. Modyfikowanie Kontekstu - ALLSELECTED' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>ALLSELECTED</title>
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

<div class='container' id='viz_adeb3b9a'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_adeb3b9a' onclick='changePage_adeb3b9a(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_adeb3b9a'>1</span> z <span id='totalPages_adeb3b9a'>3</span>
        </span>
        <button id='nextBtn_adeb3b9a' onclick='changePage_adeb3b9a(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <p>Masz raport z tabelą pokazującą sprzedaż po kategoriach. Użytkownik wybiera w slicerze trzy kategorie: Computers, Cameras, TV. Chce widzieć udział każdej z tych trzech w ich łącznej sumie.</p>
        <pre><code>// Próba z ALL
        fSprzedaż % with ALL =
        <span class='dax-function'>DIVIDE</span>(
            [Total fSprzedaż],
            <span class='dax-function'>CALCULATE</span>([Total fSprzedaż], <span class='dax-function'>ALL</span>(dProduct[ProductCategoryName]))
        )</code></pre>
        <p>Problem: ALL usuwa WSZYSTKIE filtry z kategorii - czyli ignoruje też slicer. Mianownik to sprzedaż wszystkich kategorii w bazie (także Audio, Games, itd.), nie tylko trzech wybranych.</p>
        <table>
          <thead>
            <tr>
              <th>Kategoria</th>
              <th>[Total fSprzedaż]</th>
              <th>Mianownik (ALL)</th>
              <th>%</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Computers</td>
              <td>400 000 zł</td>
              <td>2 000 000 zł</td>
              <td>20%</td>
            </tr>
            <tr>
              <td>Cameras</td>
              <td>250 000 zł</td>
              <td>2 000 000 zł</td>
              <td>12.5%</td>
            </tr>
            <tr>
              <td>TV</td>
              <td>350 000 zł</td>
              <td>2 000 000 zł</td>
              <td>17.5%</td>
            </tr>
            <tr>
              <td><strong>Suma</strong></td>
              <td><strong>1 000 000 zł</strong></td>
              <td></td>
              <td><strong>50%</strong> ← nie sumuje się do 100%!</td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>ALLSELECTED - rozwiązanie</h2>
        <p>ALLSELECTED usuwa filtry z wizualizacji (tabeli, wykresu), ale ZACHOWUJE filtry zewnętrzne (slicery, filtry strony/raportu).</p>
        <pre><code>fSprzedaż % with ALLSELECTED =
        <span class='dax-function'>DIVIDE</span>(
            [Total fSprzedaż],
            <span class='dax-function'>CALCULATE</span>([Total fSprzedaż], <span class='dax-function'>ALLSELECTED</span>(dProduct[ProductCategoryName]))
        )</code></pre>
        <p>Teraz mianownik to suma tylko dla kategorii wybranych w slicerze:</p>
        <table>
          <thead>
            <tr>
              <th>Kategoria</th>
              <th>[Total fSprzedaż]</th>
              <th>Mianownik (ALLSELECTED)</th>
              <th>%</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Computers</td>
              <td>400 000 zł</td>
              <td>1 000 000 zł</td>
              <td>40%</td>
            </tr>
            <tr>
              <td>Cameras</td>
              <td>250 000 zł</td>
              <td>1 000 000 zł</td>
              <td>25%</td>
            </tr>
            <tr>
              <td>TV</td>
              <td>350 000 zł</td>
              <td>1 000 000 zł</td>
              <td>35%</td>
            </tr>
            <tr>
              <td><strong>Suma</strong></td>
              <td><strong>1 000 000 zł</strong></td>
              <td></td>
              <td><strong>100%</strong> ✓</td>
            </tr>
          </tbody>
        </table>
        <h2>ALLSELECTED bez argumentów</h2>
        <p>Możesz użyć ALLSELECTED() bez podawania tabeli/kolumny - wtedy usuwa filtry wizualizacji ze WSZYSTKICH tabel:</p>
        <pre><code>// Usuwa filtr wizualizacji tylko z kategorii
        <span class='dax-function'>CALCULATE</span>(
        	[Total fSprzedaż],
        	 <span class='dax-function'>ALLSELECTED</span>(dProduct[ProductCategoryName])
         )</code></pre>
        <pre><code>// Usuwa filtr wizualizacji ze wszystkiego (produkty, czas, geografia...)
        <span class='dax-function'>CALCULATE</span>(
        	[Total fSprzedaż],
        	 <span class='dax-function'>ALLSELECTED</span>()
         )</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Porównanie ALL vs ALLSELECTED</h2>
        <pre><code>Total fSprzedaż = <span class='dax-function'>SUM</span>(ffSprzedaż[fSprzedażAmount])

        // Ignoruje WSZYSTKO - zawsze pełna baza
        Grand Total ALL =
        <span class='dax-function'>CALCULATE</span>([Total fSprzedaż], <span class='dax-function'>ALL</span>(dProduct))

        // Ignoruje wizualizację, respektuje slicery
        Grand Total ALLSELECTED =
        <span class='dax-function'>CALCULATE</span>([Total fSprzedaż], <span class='dax-function'>ALLSELECTED</span>(dProduct))</code></pre>
        <p>Scenariusz: Slicer = 'Computers', tabela pokazuje podkategorie:</p>
        <table>
          <thead>
            <tr>
              <th>Podkategoria</th>
              <th>[Total fSprzedaż]</th>
              <th>[Grand Total ALL]</th>
              <th>[Grand Total ALLSELECTED]</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Laptops</td>
              <td>200 000 zł</td>
              <td>2 000 000 zł</td>
              <td>400 000 zł</td>
            </tr>
            <tr>
              <td>Desktops</td>
              <td>150 000 zł</td>
              <td>2 000 000 zł</td>
              <td>400 000 zł</td>
            </tr>
            <tr>
              <td>Tablets</td>
              <td>50 000 zł</td>
              <td>2 000 000 zł</td>
              <td>400 000 zł</td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
        <ul>
        <li>ALL daje całą bazę (2 mln)</li>
        <li>ALLSELECTED daje sumę dla 'Computers' (400k) - respektuje fragmentator</li>
        </ul>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'adeb3b9a';
    var containerId = 'viz_' + vizId;

    var currentPage_adeb3b9a = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_adeb3b9a'] = function(n) {
        if (n > totalPages) currentPage_adeb3b9a = totalPages;
        if (n < 1) currentPage_adeb3b9a = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_adeb3b9a - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_adeb3b9a;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_adeb3b9a === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_adeb3b9a === totalPages);
    };

    window['changePage_adeb3b9a'] = function(n) {
        currentPage_adeb3b9a += n;
        window['showPage_adeb3b9a'](currentPage_adeb3b9a);
    };

    // Inicjalizacja
    window['showPage_adeb3b9a'](1);

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
            lineageTag: 6ed7d07a-6bca-4363-8700-e46b6678d589

        measure '04. Modyfikowanie Kontekstu - CROSSFILTER' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>CROSSFILTER</title>
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

<div class='container' id='viz_06e680c7'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_06e680c7' onclick='changePage_06e680c7(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_06e680c7'>1</span> z <span id='totalPages_06e680c7'>2</span>
        </span>
        <button id='nextBtn_06e680c7' onclick='changePage_06e680c7(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <p>Umożliwia tymczasową zmianę kierunku filtrowania relacji w kontekście danego wyrażenia DAX.</p>
        <pre><code><span class='dax-function'>CROSSFILTER</span>(&lt;columnName1&gt;, &lt;columnName2&gt;, &lt;direction&gt;)</code></pre>
        <ul>
        <li><code>Both</code> — filtrowanie dwukierunkowe (filtry przechodzą w obu kierunkach, domyślnie jest jednokierunkowe).</li>
        <li><code>None</code> — wyłącza filtrowanie między tabelami.</li>
        <li><code>OneWay</code> — jednokierunkowe filtrowanie z Column1 do Column2 (domyślnie).</li>
        <li><code>OneWayReverse</code> — jednokierunkowe filtrowanie z Column2 do Column1.</li>
        </ul>
        <pre><code>Filtruj w obie strony = 
        	<span class='dax-function'>CALCULATE</span>(
        		[Distinct Count of ProductKey],
        		 <span class='dax-function'>CROSSFILTER</span>(
        			FactInternetfSprzedaż[ProductKey],
        			DimProduct[ProductKey],
        			Both
        		)
        	)</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Zastosowanie</h1>
        <p>Funkcja CROSSFILTER służy do dynamicznego modyfikowania kierunku przepływu filtru między tabelami w ramach pojedynczej miary lub wyrażenia DAX, bez konieczności zmiany ustawień relacji w modelu danych. Jest szczególnie przydatna, gdy standardowy kierunek filtrowania relacji nie wystarcza do osiągnięcia zamierzonego wyniku analitycznego, ale nie chcemy na stałe zmieniać modelu (np. włączać dwukierunkowego filtrowania wszędzie, co mogłoby pogorszyć wydajność).</p>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251210001950.png?raw=true' width='100%'>
        <p><strong>Typowe zastosowania:</strong></p>
        <ul>
        <li>Tymczasowe włączenie filtrowania dwukierunkowego dla specyficznych obliczeń</li>
        <li>Całkowite wyłączenie filtrowania między tabelami w kontekście danej miary</li>
        <li>Odwrócenie kierunku filtrowania relacji dla konkretnych analiz</li>
        </ul>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '06e680c7';
    var containerId = 'viz_' + vizId;

    var currentPage_06e680c7 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_06e680c7'] = function(n) {
        if (n > totalPages) currentPage_06e680c7 = totalPages;
        if (n < 1) currentPage_06e680c7 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_06e680c7 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_06e680c7;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_06e680c7 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_06e680c7 === totalPages);
    };

    window['changePage_06e680c7'] = function(n) {
        currentPage_06e680c7 += n;
        window['showPage_06e680c7'](currentPage_06e680c7);
    };

    // Inicjalizacja
    window['showPage_06e680c7'](1);

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
            lineageTag: f19571f5-ec2f-4392-9977-c897074b1aee

        measure '04. Modyfikowanie Kontekstu - KEEPFILTERS' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>KEEPFILTERS</title>
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

<div class='container' id='viz_de834375'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_de834375' onclick='changePage_de834375(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_de834375'>1</span> z <span id='totalPages_de834375'>4</span>
        </span>
        <button id='nextBtn_de834375' onclick='changePage_de834375(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h2>Problem: CALCULATE nadpisuje filtry</h2>
        <p>Domyślnie filtr w CALCULATE <strong>zastępuje</strong> istniejący filtr na tej samej kolumnie:</p>
        <pre><code>fSprzedaż Computers =
        <span class='dax-function'>CALCULATE</span>(
            [Total fSprzedaż],
            dProduct[ProductCategoryName] = 'Computers'
        )</code></pre>
        <p>Co się stanie, gdy użytkownik wybierze w slicerze 'Cameras'?</p>
        <table>
          <thead>
            <tr>
              <th>Kontekst użytkownika</th>
              <th>[Total fSprzedaż]</th>
              <th>[fSprzedaż Computers]</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>(brak filtra)</td>
              <td>1 000 000 zł</td>
              <td>400 000 zł</td>
            </tr>
            <tr>
              <td>Cameras</td>
              <td>250 000 zł</td>
              <td>400 000 zł</td>
            </tr>
            <tr>
              <td>Computers</td>
              <td>400 000 zł</td>
              <td>400 000 zł</td>
            </tr>
          </tbody>
        </table>
        <p>Filtr z CALCULATE wygrywa - nadpisuje wybór użytkownika. Czasem tego chcesz, czasem nie.</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>KEEPFILTERS - przecięcie filtrów</h2>
        <p>KEEPFILTERS mówi: 'nie nadpisuj, tylko znajdź część wspólną'.</p>
        <pre><code>fSprzedaż Computers Keep =
        <span class='dax-function'>CALCULATE</span>(
            [Total fSprzedaż],
            <span class='dax-function'>KEEPFILTERS</span>(dProduct[ProductCategoryName] = 'Computers')
        )</code></pre>
        <p>Teraz:</p>
        <table>
          <thead>
            <tr>
              <th>Kontekst użytkownika</th>
              <th>[fSprzedaż Computers]</th>
              <th>[fSprzedaż Computers Keep]</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>(brak filtra)</td>
              <td>400 000 zł</td>
              <td>400 000 zł</td>
            </tr>
            <tr>
              <td>Cameras</td>
              <td>400 000 zł</td>
              <td><strong>BLANK</strong></td>
            </tr>
            <tr>
              <td>Computers</td>
              <td>400 000 zł</td>
              <td>400 000 zł</td>
            </tr>
          </tbody>
        </table>
        <p>Gdy użytkownik wybiera 'Cameras', KEEPFILTERS szuka przecięcia: (Cameras) ∩ (Computers) = zbiór pusty = BLANK.</p>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Praktyczny przypadek dla KEEPFILTERS</h2>
        <p>Masz raport z podziałem na segmenty klientów. Chcesz pokazać sprzedaż 'Premium' tylko gdy użytkownik patrzy na segment Premium (nie na siłę):</p>
        <pre><code>// Bez KEEPFILTERS - zawsze pokazuje Premium, nawet gdy wybrano 'Standard'
        fSprzedaż Premium - Wrong =
        	<span class='dax-function'>CALCULATE</span>([Total fSprzedaż], dCustomer[Segment] = 'Premium')

        // Z KEEPFILTERS - pokazuje Premium tylko gdy kontekst to Premium
        fSprzedaż Premium - Correct =
        <span class='dax-function'>CALCULATE</span>([Total fSprzedaż], <span class='dax-function'>KEEPFILTERS</span>(dCustomer[Segment] = 'Premium'))</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>Kiedy używać KEEPFILTERS?</h2>
        <p>Rzadko - ale są scenariusze:</p>
        <ol>
        <li>Walidacja danych (pokaż wartość tylko gdy kontekst się zgadza)</li>
        <li>Warunkowe KPI (np. 'cel' ma sens tylko dla konkretnego regionu)</li>
        <li>Unikanie 'wyciekania' danych do innych kontekstów</li>
        </ol>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'de834375';
    var containerId = 'viz_' + vizId;

    var currentPage_de834375 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_de834375'] = function(n) {
        if (n > totalPages) currentPage_de834375 = totalPages;
        if (n < 1) currentPage_de834375 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_de834375 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_de834375;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_de834375 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_de834375 === totalPages);
    };

    window['changePage_de834375'] = function(n) {
        currentPage_de834375 += n;
        window['showPage_de834375'](currentPage_de834375);
    };

    // Inicjalizacja
    window['showPage_de834375'](1);

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
            lineageTag: 88900145-6ec9-491a-b952-83dd7be37742

        measure '04. Modyfikowanie Kontekstu - USERELATIONSHIP' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>USERELATIONSHIP</title>
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

<div class='container' id='viz_b61f34a7'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_b61f34a7' onclick='changePage_b61f34a7(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_b61f34a7'>1</span> z <span id='totalPages_b61f34a7'>2</span>
        </span>
        <button id='nextBtn_b61f34a7' onclick='changePage_b61f34a7(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <p><strong>USERELATIONSHIP</strong> aktywuje nieaktywną relację między tabelami na czas trwania obliczenia. W modelu Power BI między dwiema tabelami może istnieć wiele relacji, ale tylko jedna może być aktywna domyślnie.</p>
        <h2>Typowy scenariusz</h2>
        <p>Najczęstszy przypadek to tabela faktów z wieloma kolumnami dat powiązanymi z jedną tabelą kalendarza:</p>
        <pre><code>fSprzedaż
        ├─ Data Sprzedaży      → 'dKalendarz'[Data] (relacja aktywna)
        ├─ Data Fakturowania   → 'dKalendarz'[Data] (relacja nieaktywna)
        └─ Data Dostawy        → 'dKalendarz'[Data] (relacja nieaktywna)</code></pre>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209193536.png?raw=true' width='100%'>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Podstawowa składnia</h1>
        <pre><code><span class='dax-comment'>------- Miara używająca domyślnej relacji (OrderDate)</span>
        fSprzedaż Amount = 
            <span class='dax-function'>SUMX</span> ( fSprzedaż, fSprzedaż[Quantity] * fSprzedaż[Unit Price] )

        <span class='dax-comment'>------- Miara aktywująca relację ShipmentDate</span>
        fSprzedaż Amount by Shipment = 
        <span class='dax-function'>CALCULATE</span> (
            <span class='dax-function'>SUMX</span> ( fSprzedaż, fSprzedaż[Quantity] * fSprzedaż[Unit Price] ),
            <span class='dax-function'>USERELATIONSHIP</span> ( fSprzedaż[ShipmentDate], 'Calendar'[Date] )
        )

        <span class='dax-comment'>------- Miara aktywująca relację DeliveryDate</span>
        fSprzedaż Amount by Delivery = 
        <span class='dax-function'>CALCULATE</span> (
            <span class='dax-function'>SUMX</span> ( fSprzedaż, fSprzedaż[Quantity] * fSprzedaż[Unit Price] ),
            <span class='dax-function'>USERELATIONSHIP</span> ( fSprzedaż[DeliveryDate], 'Calendar'[Date] )
        )</code></pre>
        <p><strong>Kluczowe zasady:</strong></p>
        <ul>
        <li>USERELATIONSHIP działa tylko wewnątrz CALCULATE lub CALCULATETABLE</li>
        <li>Pierwszym parametrem jest kolumna z tabeli faktów (strona 'wiele')</li>
        <li>Drugim parametrem jest kolumna z tabeli wymiaru (strona 'jeden')</li>
        <li>Relacja musi fizycznie istnieć w modelu (być zdefiniowana, choć nieaktywna)</li>
        </ul>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'b61f34a7';
    var containerId = 'viz_' + vizId;

    var currentPage_b61f34a7 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_b61f34a7'] = function(n) {
        if (n > totalPages) currentPage_b61f34a7 = totalPages;
        if (n < 1) currentPage_b61f34a7 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_b61f34a7 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_b61f34a7;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_b61f34a7 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_b61f34a7 === totalPages);
    };

    window['changePage_b61f34a7'] = function(n) {
        currentPage_b61f34a7 += n;
        window['showPage_b61f34a7'](currentPage_b61f34a7);
    };

    // Inicjalizacja
    window['showPage_b61f34a7'](1);

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
            lineageTag: 51e6c83d-f9b0-4130-8787-e7a91c9717d6

        measure '04. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: Modyfikowanie Kontekstu</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>8</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Do czego służy funkcja ALL?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Do sumowania wszystkich wartości
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Do usuwania filtrów z tabeli lub kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Do wybierania wszystkich kolumn
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) Do agregacji danych
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Jaka jest różnica między ALL(Tabela) a ALL(Tabela[Kolumna])?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Nie ma różnicy
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) ALL(Tabela) usuwa filtry z całej tabeli, ALL(Tabela[Kolumna]) tylko z jednej kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) ALL(Tabela) jest szybsze
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) ALL(Tabela[Kolumna]) usuwa także relacje
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Jaka jest nowoczesna alternatywa dla funkcji ALL?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) CLEARFILTERS
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) REMOVEFILTERS
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) DELETEFILTERS
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) NOFILTERS
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Co oblicza: CALCULATE([Sprzedaż], ALL(Produkty))?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) Sprzedaż dla wybranego produktu
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) Sprzedaż dla wszystkich produktów (ignorując filtry na tabeli Produkty)
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) Sumę wszystkich sprzedaży w bazie
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) Błąd składni
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Jak obliczyć procent sprzedaży względem całości?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) [Sprzedaż] / SUM(Sprzedaż)
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) [Sprzedaż] / CALCULATE([Sprzedaż], ALL(Tabela))
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) DIVIDE([Sprzedaż], [Całkowita Sprzedaż])
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Zarówno B jak i C (gdy [Całkowita Sprzedaż] używa ALL)
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 3)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Co robi funkcja ALLSELECTED?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) Usuwa wszystkie filtry
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Zachowuje tylko filtry z slicerów i zewnętrznych filtrów
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Wybiera wszystkie kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) To samo co ALL
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Kiedy używamy KEEPFILTERS w CALCULATE?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(6, 0)'>
                A) Aby dodać filtr bez nadpisywania istniejących
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 1)'>
                B) Aby usunąć wszystkie filtry
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 2)'>
                C) Aby zachować tylko filtry dat
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 3)'>
                D) Jest to przestarzała funkcja
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(6, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-6'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/7</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 8;
    const totalQuestions = 7;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [1, 1, 1, 1, 3, 1, 0];
    
    const explanations = [
        'Prawidłowa odpowiedź: B. ALL usuwa filtry z tabeli lub kolumny. Mówisz silnikowi DAX: 'zignoruj wszelkie filtry nałożone na ten obiekt'.',
        'Prawidłowa odpowiedź: B. ALL(Tabela) usuwa wszystkie filtry z całej tabeli, natomiast ALL(Tabela[Kolumna]) usuwa filtry tylko z konkretnej kolumny, zachowując filtry na innych kolumnach.',
        'Prawidłowa odpowiedź: B. REMOVEFILTERS to nowoczesna alternatywa dla ALL, która ma bardziej czytelną nazwę i jasno pokazuje intencję - usunięcie filtrów.',
        'Prawidłowa odpowiedź: B. ALL(Produkty) usuwa wszystkie filtry z tabeli Produkty, więc CALCULATE zwróci sprzedaż dla WSZYSTKICH produktów, niezależnie od aktualnych filtrów.',
        'Prawidłowa odpowiedź: D. Procent obliczamy dzieląc wartość bieżącą przez wartość całkowitą (bez filtrów). Można to zrobić bezpośrednio lub przez osobną miarę.',
        'Prawidłowa odpowiedź: B. ALLSELECTED usuwa filtry wewnętrzne (z wizualizacji), ale zachowuje filtry zewnętrzne (slicery, filtry strony). Jest użyteczna do obliczeń typu 'procent od wybranego'.',
        'Prawidłowa odpowiedź: A. KEEPFILTERS sprawia, że nowy filtr jest DODAWANY do istniejących (AND), zamiast je NADPISYWAĆ. Przydatne gdy chcemy zawęzić, a nie zastąpić kontekst.'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: c1f64660-2ff5-4878-8e9a-37047f919560

        measure '04a. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: Modyfikowanie Kontekstu</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>8</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Do czego służy funkcja ALL?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Do sumowania wszystkich wartości
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Do usuwania filtrów z tabeli lub kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Do wybierania wszystkich kolumn
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) Do agregacji danych
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Jaka jest różnica między ALL(Tabela) a ALL(Tabela[Kolumna])?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Nie ma różnicy
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) ALL(Tabela) usuwa filtry z całej tabeli, ALL(Tabela[Kolumna]) tylko z jednej kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) ALL(Tabela) jest szybsze
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) ALL(Tabela[Kolumna]) usuwa także relacje
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Jaka jest nowoczesna alternatywa dla funkcji ALL?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) CLEARFILTERS
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) REMOVEFILTERS
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) DELETEFILTERS
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) NOFILTERS
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Co oblicza: CALCULATE([Sprzedaż], ALL(Produkty))?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) Sprzedaż dla wybranego produktu
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) Sprzedaż dla wszystkich produktów (ignorując filtry na tabeli Produkty)
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) Sumę wszystkich sprzedaży w bazie
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) Błąd składni
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Jak obliczyć procent sprzedaży względem całości?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) [Sprzedaż] / SUM(Sprzedaż)
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) [Sprzedaż] / CALCULATE([Sprzedaż], ALL(Tabela))
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) DIVIDE([Sprzedaż], [Całkowita Sprzedaż])
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Zarówno B jak i C (gdy [Całkowita Sprzedaż] używa ALL)
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 3)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Co robi funkcja ALLSELECTED?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) Usuwa wszystkie filtry
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Zachowuje tylko filtry z slicerów i zewnętrznych filtrów
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Wybiera wszystkie kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) To samo co ALL
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Kiedy używamy KEEPFILTERS w CALCULATE?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(6, 0)'>
                A) Aby dodać filtr bez nadpisywania istniejących
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 1)'>
                B) Aby usunąć wszystkie filtry
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 2)'>
                C) Aby zachować tylko filtry dat
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 3)'>
                D) Jest to przestarzała funkcja
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(6, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-6'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/7</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 8;
    const totalQuestions = 7;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [1, 1, 1, 1, 3, 1, 0];
    
    const explanations = [
        'Prawidłowa odpowiedź: B. ALL usuwa filtry z tabeli lub kolumny. Mówisz silnikowi DAX: 'zignoruj wszelkie filtry nałożone na ten obiekt'.',
        'Prawidłowa odpowiedź: B. ALL(Tabela) usuwa wszystkie filtry z całej tabeli, natomiast ALL(Tabela[Kolumna]) usuwa filtry tylko z konkretnej kolumny, zachowując filtry na innych kolumnach.',
        'Prawidłowa odpowiedź: B. REMOVEFILTERS to nowoczesna alternatywa dla ALL, która ma bardziej czytelną nazwę i jasno pokazuje intencję - usunięcie filtrów.',
        'Prawidłowa odpowiedź: B. ALL(Produkty) usuwa wszystkie filtry z tabeli Produkty, więc CALCULATE zwróci sprzedaż dla WSZYSTKICH produktów, niezależnie od aktualnych filtrów.',
        'Prawidłowa odpowiedź: D. Procent obliczamy dzieląc wartość bieżącą przez wartość całkowitą (bez filtrów). Można to zrobić bezpośrednio lub przez osobną miarę.',
        'Prawidłowa odpowiedź: B. ALLSELECTED usuwa filtry wewnętrzne (z wizualizacji), ale zachowuje filtry zewnętrzne (slicery, filtry strony). Jest użyteczna do obliczeń typu 'procent od wybranego'.',
        'Prawidłowa odpowiedź: A. KEEPFILTERS sprawia, że nowy filtr jest DODAWANY do istniejących (AND), zamiast je NADPISYWAĆ. Przydatne gdy chcemy zawęzić, a nie zastąpić kontekst.'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: 16a3bcac-ec44-482d-bf0b-cea74494d515

        measure '05. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: Tworzenie zestawień tabelarycznych</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>8</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Która funkcja jest zalecana do tworzenia zestawień tabelarycznych?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) SUMMARIZE
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) SUMMARIZECOLUMNS
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) GROUPBY
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) AGGREGATE
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Co zwraca funkcja SUMMARIZECOLUMNS?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Liczbę wierszy w tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) Tabelę z unikalnymi kombinacjami kolumn i opcjonalnymi agregacjami
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) Tylko unikalne wartości z jednej kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) Posortowaną tabelę
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Jaka jest podstawowa składnia SUMMARIZECOLUMNS?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) SUMMARIZECOLUMNS(kolumna1, kolumna2, miara1, miara2)
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) SUMMARIZECOLUMNS(tabela, kolumny, miary)
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) SUMMARIZECOLUMNS(kolumna1, kolumna2, 'Nazwa', miara)
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) SUMMARIZECOLUMNS(grupa, agregacja)
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Dlaczego SUMMARIZE jest uznawana za legacy (przestarzałą)?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) Jest wolniejsza i ma nieoczywistą składnię
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) Nie działa w nowych wersjach Power BI
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) Została całkowicie usunięta z DAX
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) Wymaga licencji Premium
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Czy w SUMMARIZECOLUMNS możesz dodać wiele miar?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) Nie, tylko jedną miarę
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) Tak, maksymalnie 3 miary
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Tak, dowolną liczbę miar (jako pary: nazwa, wyrażenie)
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Tylko jeśli używasz funkcji ADDCOLUMNS
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Do czego służy funkcja ADDCOLUMNS?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) Do dodawania kolumn do istniejącej tabeli na podstawie obliczeń
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Do sumowania kolumn
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Do łączenia tabel
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) Do filtrowania kolumn
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Jaki jest wynik: SUMMARIZECOLUMNS(Produkty[Kategoria], 'Suma', [Sprzedaż])?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(6, 0)'>
                A) Listę wszystkich kategorii
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 1)'>
                B) Tabelę z unikalnymi kategoriami i sumą sprzedaży dla każdej
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 2)'>
                C) Sumę sprzedaży dla wszystkich kategorii
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 3)'>
                D) Błąd składni
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(6, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-6'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/7</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 8;
    const totalQuestions = 7;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [1, 1, 2, 0, 2, 0, 1];
    
    const explanations = [
        'Prawidłowa odpowiedź: B. SUMMARIZECOLUMNS to nowoczesne podejście zalecane przez Microsoft. Jest bardziej wydajna i łatwiejsza w użyciu niż legacy SUMMARIZE.',
        'Prawidłowa odpowiedź: B. SUMMARIZECOLUMNS zwraca tabelę zawierającą unikalne kombinacje wartości z wybranych kolumn oraz opcjonalnie obliczone agregacje dla każdej kombinacji.',
        'Prawidłowa odpowiedź: C. Składnia to: SUMMARIZECOLUMNS(kolumna1, kolumna2, ..., 'Nazwa Miary', [Wyrażenie], ...). Najpierw kolumny grupujące, potem pary: nazwa i wyrażenie miary.',
        'Prawidłowa odpowiedź: A. SUMMARIZE ma nieoczywistą składnię i może dawać nieoczekiwane wyniki. SUMMARIZECOLUMNS jest szybsza, bardziej czytelna i zalecana przez Microsoft.',
        'Prawidłowa odpowiedź: C. SUMMARIZECOLUMNS może zawierać dowolną liczbę miar. Każda miara to para: 'Nazwa Miary', [Wyrażenie Miary].',
        'Prawidłowa odpowiedź: A. ADDCOLUMNS przyjmuje tabelę i dodaje do niej nowe kolumny kalkulowane. Składnia: ADDCOLUMNS(tabela, 'Nowa Kolumna', [Wyrażenie], ...).',
        'Prawidłowa odpowiedź: B. Funkcja zwróci tabelę z kolumną Kategoria (unikalne wartości) oraz kolumną Suma (sprzedaż zagregowana dla każdej kategorii).'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: 0f885a64-166a-44f1-8863-bfbf4d3c7a5b

        measure '05. Tworzenie zestawień tabelarycznych - Tworzenie Tabeli' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Tworzenie Tabeli</title>
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

<div class='container' id='viz_746dab9c'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_746dab9c' onclick='changePage_746dab9c(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_746dab9c'>1</span> z <span id='totalPages_746dab9c'>3</span>
        </span>
        <button id='nextBtn_746dab9c' onclick='changePage_746dab9c(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>SUMMARIZE vs SUMMARIZECOLUMNS</h1>
        <p><strong>Podejście legacy (<code>SUMMARIZE</code>):</strong></p>
        <ul>
        <li>Wymaga dodatkowego <code>ADDCOLUMNS</code> do obliczenia miar</li>
        <li>Trzeba ręcznie filtrować puste wiersze przez <code>FILTER</code> + <code>NOT</code> <code>ISBLANK</code></li>
        <li>Bardziej rozwlekłe i podatne na błędy kontekstowe</li>
        <li><code>SUMMARIZE</code> może dać niespodziewane wyniki bez <code>ADDCOLUMNS</code></li>
        </ul>
        <p><strong>Podejście modern (SUMMARIZECOLUMNS):</strong></p>
        <ul>
        <li>Łączy grupowanie, dodawanie obliczeń i usuwanie pustych wierszy w jednej funkcji</li>
        <li>Krótsze, czytelniejsze, bezpieczniejsze</li>
        <li>Obecnie zalecany standard do raportów i zapytań w DAX</li>
        </ul>
        <pre><code><span class='dax-comment'>------- LEGACY  </span>
        EVALUATE  
            <span class='dax-function'>FILTER</span> (  
                <span class='dax-function'>ADDCOLUMNS</span> (  
                    <span class='dax-function'>SUMMARIZE</span> ( Sales, 'Product'[Brand], 'Date'[Year] ),  
                    'Sales', <span class='dax-function'>CALCULATE</span> ( <span class='dax-function'>SUMX</span> ( Sales, Sales[Quantity] * Sales[Unit Price] ) )  
                ),  
                NOT <span class='dax-function'>ISBLANK</span> ( [Sales] )  
            )  

        <span class='dax-comment'>------- MODERN  </span>
        EVALUATE  
            <span class='dax-function'>SUMMARIZECOLUMNS</span> (  
                'Product'[Brand], 'Date'[Year],  
                'Sales', <span class='dax-function'>CALCULATE</span> ( <span class='dax-function'>SUMX</span> ( Sales, Sales[Quantity] * Sales[Unit Price] ) )  
            )</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Praca z wieloma tabelami faktów</h1>
        <p><strong>Zalety SUMMARIZECOLUMNS:</strong></p>
        <ul>
        <li>Rozumie kontekst całego modelu danych</li>
        <li>Działa spójnie z modelem gwiazdy – automatycznie obsługuje kombinacje wymiarów</li>
        <li>Pozwala w jednym wyrażeniu pobierać dane z różnych tabel faktów</li>
        <li>Zwraca kompletny wynik w jednej tabeli</li>
        </ul>
        <p><strong>Problemy z SUMMARIZE:</strong></p>
        <ul>
        <li>Ogranicza się do jednej tabeli faktów</li>
        <li>Wymaga ręcznego tworzenia siatki kombinacji przez <code>CROSSJOIN</code></li>
        <li>Trzeba łączyć wyniki przez <code>NATURALLEFTOUTERJOIN</code></li>
        <li>Bardziej skomplikowane, mniej czytelne i podatne na błędy</li>
        </ul>
        <pre><code><span class='dax-comment'>------- RECOMMENDED  </span>
        EVALUATE  
            <span class='dax-function'>SUMMARIZECOLUMNS</span> (  
                'Product'[Category],  
                Store[Country],  
                'Sales', <span class='dax-function'>CALCULATE</span> ( <span class='dax-function'>SUMX</span> ( Sales, Sales[Quantity] * Sales[Net Price] ) ),  
                'Purchases', <span class='dax-function'>CALCULATE</span> ( <span class='dax-function'>SUMX</span> ( Purchase, Purchase[Quantity] * Purchase[Unit Cost] ) )   
            )  

        <span class='dax-comment'>------- PROBLEMATIC  </span>
        EVALUATE  
            <span class='dax-keyword'>VAR</span> S =   
                <span class='dax-function'>ADDCOLUMNS</span> (  
                    <span class='dax-function'>SUMMARIZE</span> ( Sales, 'Product'[Category], Store[Country] ),  
                    'Sales', <span class='dax-function'>CALCULATE</span> ( <span class='dax-function'>SUMX</span> ( Sales, Sales[Quantity] * Sales[Net Price] ) )   
                )  
            <span class='dax-keyword'>VAR</span> P =   
                <span class='dax-function'>ADDCOLUMNS</span> (  
                    <span class='dax-function'>SUMMARIZE</span> ( Purchase, 'Product'[Category], Store[Country] ),  
                    'Purchase', <span class='dax-function'>CALCULATE</span> ( <span class='dax-function'>SUMX</span> ( Purchase, Purchase[Quantity] * Purchase[Unit Cost] ) )   
                )  
            <span class='dax-keyword'>VAR</span> G =   
                <span class='dax-function'>CROSSJOIN</span>( <span class='dax-function'>VALUES</span> ( 'Product'[Category] ), <span class='dax-function'>VALUES</span> ( Store[Country] ) )  
        <span class='dax-keyword'>RETURN</span>  
            <span class='dax-function'>NATURALLEFTOUTERJOIN</span> ( <span class='dax-function'>NATURALLEFTOUTERJOIN</span> ( G, P ), S )</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Kiedy używać SUMMARIZE zamiast SUMMARIZECOLUMNS</h1>
        <p><strong>Gdy potrzebujesz tylko istniejących kombinacji:</strong></p>
        <ul>
        <li><code>SUMMARIZE</code> z tabelą źródłową zwraca tylko kombinacje występujące w danych faktycznych</li>
        <li>Filtruje automatycznie do rzeczywistych relacji w tabeli Sales</li>
        <li>To najczęściej oczekiwane zachowanie w raportach</li>
        </ul>
        <p><strong>Problem z SUMMARIZECOLUMNS bez miar:</strong></p>
        <ul>
        <li>Bez tabeli źródłowej generuje wszystkie możliwe kombinacje (jak <code>CROSSJOIN</code>)</li>
        <li>Może zwrócić wiele pustych kombinacji, które nie istnieją w danych</li>
        <li>Nie jest to zwykle pożądane zachowanie</li>
        </ul>
        <pre><code><span class='dax-comment'>------- RECOMMENDED  </span>
        EVALUATE  
            <span class='dax-function'>SUMMARIZE</span> (  
                'Sales',  
                'Product'[Brand],  
                Customer[Continent],  
                'Date'[Date]  
            )  

        <span class='dax-comment'>------- PROBLEMATIC  </span>
        EVALUATE  
            <span class='dax-function'>SUMMARIZECOLUMNS</span> (  
                'Product'[Brand],  
                Customer[Continent],  
                'Date'[Date]  
            )  

        <span class='dax-comment'>-- Równoważne z:  </span>
        EVALUATE  
            <span class='dax-function'>CROSSJOIN</span> (  
                <span class='dax-function'>VALUES</span> ( 'Product'[Brand] ),  
                <span class='dax-function'>VALUES</span> ( Customer[Continent] ),  
                <span class='dax-function'>VALUES</span> ( 'Date'[Date] )   
            )</code></pre>
        <p><strong>Zasada:</strong> Do samego grupowania bez miar używaj <code>SUMMARIZE</code> z tabelą źródłową. Do grupowania z miarami używaj <code>SUMMARIZECOLUMNS</code>.</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '746dab9c';
    var containerId = 'viz_' + vizId;

    var currentPage_746dab9c = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_746dab9c'] = function(n) {
        if (n > totalPages) currentPage_746dab9c = totalPages;
        if (n < 1) currentPage_746dab9c = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_746dab9c - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_746dab9c;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_746dab9c === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_746dab9c === totalPages);
    };

    window['changePage_746dab9c'] = function(n) {
        currentPage_746dab9c += n;
        window['showPage_746dab9c'](currentPage_746dab9c);
    };

    // Inicjalizacja
    window['showPage_746dab9c'](1);

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
            lineageTag: 4fab4be6-c214-416d-aaf0-081bb0ae9da6

        measure '05a. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: Tworzenie zestawień tabelarycznych</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>8</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Która funkcja jest zalecana do tworzenia zestawień tabelarycznych?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) SUMMARIZE
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) SUMMARIZECOLUMNS
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) GROUPBY
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) AGGREGATE
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Co zwraca funkcja SUMMARIZECOLUMNS?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Liczbę wierszy w tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) Tabelę z unikalnymi kombinacjami kolumn i opcjonalnymi agregacjami
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) Tylko unikalne wartości z jednej kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) Posortowaną tabelę
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Jaka jest podstawowa składnia SUMMARIZECOLUMNS?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) SUMMARIZECOLUMNS(kolumna1, kolumna2, miara1, miara2)
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) SUMMARIZECOLUMNS(tabela, kolumny, miary)
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) SUMMARIZECOLUMNS(kolumna1, kolumna2, 'Nazwa', miara)
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) SUMMARIZECOLUMNS(grupa, agregacja)
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Dlaczego SUMMARIZE jest uznawana za legacy (przestarzałą)?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) Jest wolniejsza i ma nieoczywistą składnię
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) Nie działa w nowych wersjach Power BI
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) Została całkowicie usunięta z DAX
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) Wymaga licencji Premium
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Czy w SUMMARIZECOLUMNS możesz dodać wiele miar?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) Nie, tylko jedną miarę
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) Tak, maksymalnie 3 miary
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Tak, dowolną liczbę miar (jako pary: nazwa, wyrażenie)
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Tylko jeśli używasz funkcji ADDCOLUMNS
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Do czego służy funkcja ADDCOLUMNS?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) Do dodawania kolumn do istniejącej tabeli na podstawie obliczeń
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Do sumowania kolumn
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Do łączenia tabel
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) Do filtrowania kolumn
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Jaki jest wynik: SUMMARIZECOLUMNS(Produkty[Kategoria], 'Suma', [Sprzedaż])?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(6, 0)'>
                A) Listę wszystkich kategorii
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 1)'>
                B) Tabelę z unikalnymi kategoriami i sumą sprzedaży dla każdej
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 2)'>
                C) Sumę sprzedaży dla wszystkich kategorii
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 3)'>
                D) Błąd składni
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(6, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-6'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/7</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 8;
    const totalQuestions = 7;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [1, 1, 2, 0, 2, 0, 1];
    
    const explanations = [
        'Prawidłowa odpowiedź: B. SUMMARIZECOLUMNS to nowoczesne podejście zalecane przez Microsoft. Jest bardziej wydajna i łatwiejsza w użyciu niż legacy SUMMARIZE.',
        'Prawidłowa odpowiedź: B. SUMMARIZECOLUMNS zwraca tabelę zawierającą unikalne kombinacje wartości z wybranych kolumn oraz opcjonalnie obliczone agregacje dla każdej kombinacji.',
        'Prawidłowa odpowiedź: C. Składnia to: SUMMARIZECOLUMNS(kolumna1, kolumna2, ..., 'Nazwa Miary', [Wyrażenie], ...). Najpierw kolumny grupujące, potem pary: nazwa i wyrażenie miary.',
        'Prawidłowa odpowiedź: A. SUMMARIZE ma nieoczywistą składnię i może dawać nieoczekiwane wyniki. SUMMARIZECOLUMNS jest szybsza, bardziej czytelna i zalecana przez Microsoft.',
        'Prawidłowa odpowiedź: C. SUMMARIZECOLUMNS może zawierać dowolną liczbę miar. Każda miara to para: 'Nazwa Miary', [Wyrażenie Miary].',
        'Prawidłowa odpowiedź: A. ADDCOLUMNS przyjmuje tabelę i dodaje do niej nowe kolumny kalkulowane. Składnia: ADDCOLUMNS(tabela, 'Nowa Kolumna', [Wyrażenie], ...).',
        'Prawidłowa odpowiedź: B. Funkcja zwróci tabelę z kolumną Kategoria (unikalne wartości) oraz kolumną Suma (sprzedaż zagregowana dla każdej kategorii).'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: ab596e10-6bfa-4efb-a63e-11255b42bf1c

        measure '06. DAX - Zaawansowane Kwerendy - Query View' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Query View</title>
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

<div class='container' id='viz_69087c0f'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_69087c0f' onclick='changePage_69087c0f(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_69087c0f'>1</span> z <span id='totalPages_69087c0f'>4</span>
        </span>
        <button id='nextBtn_69087c0f' onclick='changePage_69087c0f(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <p><strong>Query View</strong> to specjalny tryb w Power BI Desktop (dostępny w External Tools lub przez DAX Studio), który pozwala wykonywać zapytania DAX bezpośrednio na modelu danych. W przeciwieństwie do zwykłych miar, które działają w kontekście wizualizacji, Query View umożliwia pisanie zapytań tabelarycznych z użyciem słowa kluczowego <code>EVALUATE</code> oraz definiowanie tymczasowych miar i zmiennych za pomocą <code>DEFINE</code>. Jest to narzędzie programistyczne do testowania logiki DAX, debugowania obliczeń i eksploracji danych bez konieczności tworzenia wizualizacji.</p>
        <h2>VAR bez RETURN (błąd składniowy)</h2>
        <pre><code><span class='dax-keyword'>VAR</span> A = <span class='dax-number'>1</span>
        <span class='dax-keyword'>VAR</span> B = <span class='dax-number'>5</span>
        A + B</code></pre>
        <p><strong>Status:</strong> ❌ <strong>To jest niepoprawne!</strong></p>
        <ul>
        <li>Zmienne <code>VAR</code> <strong>zawsze muszą być zakończone słowem kluczowym <code>RETURN</code></strong></li>
        <li>DAX nie wie, co ma zwrócić jako wynik</li>
        <li>Ten kod spowoduje błąd składniowy</li>
        </ul>
        <pre><code>EVALUATE
            <span class='dax-keyword'>VAR</span> A = <span class='dax-number'>1</span>
            <span class='dax-keyword'>VAR</span> B = <span class='dax-number'>5</span>
        <span class='dax-keyword'>RETURN</span>
        A + B</code></pre>
        <p><strong>Status:</strong> ❌ <strong>Blisko, ale wciąż źle!</strong></p>
        <ul>
        <li>DAX potrafi zwracać wyłącznie wartości tabelaryczne. A + B zwraca pojedynczą wartość</li>
        <li>Należy utworzyć 'sztuczną' tabelę (np. z funkcją <code>ROW()</code>), albo podsumować według istniejących kolumn za pomocą <code>SUMMARIZECOLUMNS()</code> ``</li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>VAR z RETURN w zapytaniu EVALUATE</h2>
        <pre><code>EVALUATE
            <span class='dax-keyword'>VAR</span> A = <span class='dax-number'>1</span>
            <span class='dax-keyword'>VAR</span> B = <span class='dax-number'>5</span>
        <span class='dax-keyword'>RETURN</span>
            <span class='dax-function'>ROW</span>('Test', A + B)</code></pre>
        <p><strong>Status:</strong> ✅ <strong>Poprawne</strong></p>
        <ul>
        <li>Zmienne <code>A</code> i <code>B</code> są tworzone <strong>przed</strong> wykonaniem właściwego zapytania</li>
        <li><code>RETURN</code> zwraca tabelę z jednym wierszem i jedną kolumną o nazwie 'Test'</li>
        <li>Wartość w kolumnie to wynik <code>A + B</code> = 6</li>
        </ul>
        <p><strong>Wynik zapytania:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Test</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>6</td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>VAR wewnątrz definicji miary</h2>
        <pre><code>DEFINE MEASURE _Measures[Test] = 
            <span class='dax-keyword'>VAR</span> A = <span class='dax-number'>1</span>
            <span class='dax-keyword'>VAR</span> B = <span class='dax-number'>5</span>
        <span class='dax-keyword'>RETURN</span>
            A + B

        EVALUATE
            <span class='dax-function'>ROW</span>('Test', [Test])</code></pre>
        <p><strong>Status:</strong> ✅ <strong>Poprawne</strong></p>
        <ul>
        <li>Zmienne <code>VAR</code> są zdefiniowane <strong>wewnątrz miary</strong> <code>[Test]</code></li>
        <li>Za każdym razem gdy miara jest wywoływana, zmienne są tworzone na nowo</li>
        <li>Miara zwraca wartość <code>A + B</code> = 6</li>
        <li><code>EVALUATE</code> wywołuje miarę i wyświetla jej wynik w tabeli</li>
        </ul>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>Zastosowanie</h1>
        <p>Query View i zapytania DAX znajdują zastosowanie w kilku kluczowych scenariuszach:</p>
        <ul>
        <li><strong>Testowanie i debugowanie</strong> – szybkie sprawdzanie logiki DAX bez tworzenia wizualizacji</li>
        <li><strong>Eksploracja modelu danych</strong> – przeglądanie zawartości tabel, relacji i wyników obliczeń</li>
        <li><strong>Prototypowanie miar</strong> – testowanie skomplikowanych formuł przed wdrożeniem do raportu</li>
        <li><strong>Analiza wydajności</strong> – mierzenie czasu wykonania zapytań i optymalizacja modelu</li>
        <li><strong>Eksport danych</strong> – pobieranie wyników zapytań do dalszej analizy w innych narzędziach</li>
        <li><strong>Dokumentacja</strong> – tworzenie przykładów działania miar dla zespołu lub klientów</li>
        </ul>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209181932.png?raw=true' width='100%'>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '69087c0f';
    var containerId = 'viz_' + vizId;

    var currentPage_69087c0f = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_69087c0f'] = function(n) {
        if (n > totalPages) currentPage_69087c0f = totalPages;
        if (n < 1) currentPage_69087c0f = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_69087c0f - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_69087c0f;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_69087c0f === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_69087c0f === totalPages);
    };

    window['changePage_69087c0f'] = function(n) {
        currentPage_69087c0f += n;
        window['showPage_69087c0f'](currentPage_69087c0f);
    };

    // Inicjalizacja
    window['showPage_69087c0f'](1);

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
            lineageTag: 3b2696e7-a8c1-4bb7-b540-6fc5c0bf90b1

        measure '06. DAX - Zaawansowane Kwerendy' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>06. DAX - Zaawansowane Kwerendy</title>
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

<div class='container' id='viz_1a47b3ad'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_1a47b3ad' onclick='changePage_1a47b3ad(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_1a47b3ad'>1</span> z <span id='totalPages_1a47b3ad'>4</span>
        </span>
        <button id='nextBtn_1a47b3ad' onclick='changePage_1a47b3ad(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Czym są VAR i RETURN?</h1>
        <p><strong>VAR</strong> i <strong>RETURN</strong> to kluczowe słowa w języku DAX, które pozwalają na tworzenie <strong>zmiennych</strong> i <strong>zwracanie wyników</strong> w miarach i kolumnach kalkulowanych.</p>
        <h2>VAR (Variable)</h2>
        <ul>
        <li>Służy do <strong>deklarowania zmiennych</strong> i przechowywania w nich wartości</li>
        <li>Zmienne mogą zawierać: liczby, teksty, tabele, wyniki obliczeń</li>
        <li>Zmienne są <strong>obliczane tylko raz</strong> i przechowują swoją wartość</li>
        <li>Pomagają <strong>unikać powtarzania</strong> tego samego kodu</li>
        <li>Poprawiają <strong>czytelność</strong> i <strong>wydajność</strong> miar</li>
        </ul>
        <h2>RETURN</h2>
        <ul>
        <li><strong>Zwraca wynik</strong> całego wyrażenia DAX</li>
        <li>W mierze/kolumnie może być <strong>tylko jedno RETURN</strong></li>
        <li>To, co umieścisz po RETURN, stanie się <strong>końcowym wynikiem</strong></li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Podstawowa składnia</h1>
        <pre><code>NazwaMiary = 
        <span class='dax-keyword'>VAR</span> NazwaZmiennej1 = &lt;wyrażenie1&gt;
        <span class='dax-keyword'>VAR</span> NazwaZmiennej2 = &lt;wyrażenie2&gt;
        <span class='dax-keyword'>VAR</span> NazwaZmiennej3 = &lt;wyrażenie3&gt;
        <span class='dax-keyword'>RETURN</span> &lt;wynik_końcowy&gt;</code></pre>
        <p><strong>Przykład prosty:</strong></p>
        <pre><code>Całkowity Koszt = 
        <span class='dax-keyword'>VAR</span> IloscSztuk = <span class='dax-number'>100</span>
        <span class='dax-keyword'>VAR</span> CenaJednostkowa = <span class='dax-number'>25</span>
        <span class='dax-keyword'>VAR</span> Koszt = IloscSztuk * CenaJednostkowa
        <span class='dax-keyword'>RETURN</span> Koszt</code></pre>
        <div class='result-box'>
        Wynik: <strong>2500</strong>
        </div>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Jak to działa w funkcjach iteracyjnych (SUMX, FILTER, itd.)?</h1>
        <p>W funkcjach iteracyjnych jak <strong>SUMX</strong>, <strong>FILTER</strong>, <strong>ADDCOLUMNS</strong> zmienne VAR są <strong>przetwarzane w każdej iteracji</strong>:</p>
        <p><strong>Zasada:</strong> Dla każdego wiersza tabeli, zmienne VAR są <strong>obliczane na nowo</strong> z wartościami z aktualnego wiersza.</p>
        <pre><code><span class='dax-function'>SUMX</span>(
            {<span class='dax-number'>1</span>, <span class='dax-number'>2</span>, <span class='dax-number'>3</span>},  <span class='dax-comment'>-- Iterujemy po wartościach 1, 2, 3</span>
            <span class='dax-keyword'>VAR</span> Kwadrat = [Value] * [Value] <span class='dax-comment'>-- [Value] to domyślna nazwa utworzonej kolumny</span>
            <span class='dax-keyword'>RETURN</span> Kwadrat
        )</code></pre>
        <h1>Kroki algorytmu:</h1>
        <div class='iteration-box'>
        <h3>Iteracja 1: [Value] = 1</h3>
        <ul>
        <li><code>Kwadrat</code> = 1 × 1 = <strong>1</strong></li>
        <li>RETURN zwraca: <strong>1</strong></li>
        </ul>
        </div>
        <div class='iteration-box'>
        <h3>Iteracja 2: [Value] = 2</h3>
        <ul>
        <li><code>Kwadrat</code> = 2 × 2 = <strong>4</strong></li>
        <li>RETURN zwraca: <strong>4</strong></li>
        </ul>
        </div>
        <div class='iteration-box'>
        <h3>Iteracja 3: [Value] = 3</h3>
        <ul>
        <li><code>Kwadrat</code> = 3 × 3 = <strong>9</strong></li>
        <li>RETURN zwraca: <strong>9</strong></li>
        </ul>
        </div>
        <div class='result-box'>
        SUMX dodaje wszystkie zwrócone wartości: 1 + 4 + 9 = <strong>14</strong>
        </div>
        <p>W każdej iteracji zmienna <code>Kwadrat</code> jest <strong>tworzona od nowa</strong> z nową wartością! Nie jest to ta sama zmienna — każda iteracja ma własny 'kontekst wiersza' i własne wartości zmiennych.</p>
        <p><strong>To oznacza:</strong></p>
        <ul>
        <li>Zmienne VAR wewnątrz iteracji są <strong>dynamiczne</strong></li>
        <li>Dostosowują się do <strong>aktualnego wiersza</strong> w tabeli</li>
        <li>Pozwalają na <strong>elastyczne obliczenia</strong> dla każdego elementu z osobna</li>
        </ul>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>Odchylenie od średniej</h1>
        <pre><code>Suma Odchyleń od Średniej = 
        <span class='dax-keyword'>VAR</span> Srednia = <span class='dax-function'>AVERAGE</span>({<span class='dax-number'>1</span>, <span class='dax-number'>2</span>, <span class='dax-number'>3</span>, <span class='dax-number'>4</span>, <span class='dax-number'>5</span>})  <span class='dax-comment'>-- Obliczona raz: 3</span>
        <span class='dax-keyword'>RETURN</span>
            <span class='dax-function'>SUMX</span>(
                {<span class='dax-number'>1</span>, <span class='dax-number'>2</span>, <span class='dax-number'>3</span>},
                <span class='dax-keyword'>VAR</span> Wartosc = [Value]
                <span class='dax-keyword'>VAR</span> Odchylenie = Wartosc - Srednia  <span class='dax-comment'>-- Używamy zmiennej spoza iteracji!</span>
                <span class='dax-keyword'>RETURN</span> Odchylenie
            )</code></pre>
        <h2>Co się dzieje krok po kroku:</h2>
        <div class='iteration-box'>
        <h3>Przed iteracją:</h3>
        <ul>
        <li><code>Srednia</code> = (1 + 2 + 3) / 3 = 2 ← obliczone <strong>tylko raz</strong></li>
        </ul>
        </div>
        <div class='iteration-box'>
        <h3>Iteracja 1: [Value] = 1</h3>
        <ul>
        <li><code>Wartosc</code> = 1</li>
        <li><code>Odchylenie</code> = 1 - 3 = <strong>-2</strong></li>
        <li>RETURN zwraca: <strong>-2</strong></li>
        </ul>
        </div>
        <div class='iteration-box'>
        <h3>Iteracja 2: [Value] = 2</h3>
        <ul>
        <li><code>Wartosc</code> = 2</li>
        <li><code>Odchylenie</code> = 2 - 3 = <strong>-1</strong></li>
        <li>RETURN zwraca: <strong>-1</strong></li>
        </ul>
        </div>
        <div class='iteration-box'>
        <h3>Iteracja 3: [Value] = 3</h3>
        <ul>
        <li><code>Wartosc</code> = 3</li>
        <li><code>Odchylenie</code> = 3 - 3 = <strong>0</strong></li>
        <li>RETURN zwraca: <strong>0</strong></li>
        </ul>
        </div>
        <div class='result-box'>
        <h3>Suma końcowa:</h3>
        <p>SUMX dodaje wszystkie odchylenia: (-2) + (-1) + 0 = <strong>-3</strong></p>
        </div>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '1a47b3ad';
    var containerId = 'viz_' + vizId;

    var currentPage_1a47b3ad = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_1a47b3ad'] = function(n) {
        if (n > totalPages) currentPage_1a47b3ad = totalPages;
        if (n < 1) currentPage_1a47b3ad = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_1a47b3ad - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_1a47b3ad;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_1a47b3ad === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_1a47b3ad === totalPages);
    };

    window['changePage_1a47b3ad'] = function(n) {
        currentPage_1a47b3ad += n;
        window['showPage_1a47b3ad'](currentPage_1a47b3ad);
    };

    // Inicjalizacja
    window['showPage_1a47b3ad'](1);

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
            lineageTag: 6556237a-7331-4f51-b7b5-ad104af5c0df

        measure '06. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: DAX - Zaawansowane Kwerendy (VAR i RETURN)</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>8</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Do czego służy słowo kluczowe VAR w DAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Do zwracania wyniku miary
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Do deklarowania zmiennych i przechowywania wartości
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Do iteracji po wierszach tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) Do filtrowania danych
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Ile razy może wystąpić słowo RETURN w jednej mierze DAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Dowolnie wiele razy
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) Tylko raz
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) Co najmniej dwa razy
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) RETURN nie jest wymagane w miarach
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Co się stanie ze zmiennymi VAR wewnątrz funkcji iteracyjnej jak SUMX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) Są obliczane tylko raz przed rozpoczęciem iteracji
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) Są obliczane na nowo w każdej iteracji dla aktualnego wiersza
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) Nie można używać VAR wewnątrz funkcji iteracyjnych
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) Zachowują wartość z poprzedniej iteracji
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Jaki będzie wynik tego kodu?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) 9
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) 24
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) 29
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) 16
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Jakie są główne zalety używania zmiennych VAR?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) Tylko poprawa czytelności kodu
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) Unikanie powtarzania kodu, poprawa czytelności i wydajności
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Tylko poprawa wydajności
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Zmienne są wymagane przez DAX
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Kiedy zmienna zadeklarowana PRZED funkcją iteracyjną jest obliczana?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) W każdej iteracji na nowo
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Tylko raz przed rozpoczęciem iteracji
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Po zakończeniu wszystkich iteracji
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) Nigdy, jest to błąd składni
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Co może zawierać zmienna VAR?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(6, 0)'>
                A) Tylko liczby
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 1)'>
                B) Tylko teksty i liczby
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 2)'>
                C) Liczby, teksty, tabele i wyniki obliczeń
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 3)'>
                D) Tylko wyniki funkcji agregujących
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(6, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-6'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/7</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 8;
    const totalQuestions = 7;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [1, 1, 1, 2, 1, 1, 2];
    
    const explanations = [
        'Prawidłowa odpowiedź: B. VAR służy do deklarowania zmiennych i przechowywania w nich wartości (liczb, tekstów, tabel, wyników obliczeń).',
        'Prawidłowa odpowiedź: B. W jednej mierze może być tylko jedno RETURN, które zwraca końcowy wynik miary.',
        'Prawidłowa odpowiedź: B. Zmienne VAR wewnątrz funkcji iteracyjnych są obliczane na nowo w każdej iteracji, dostosowując się do aktualnego wiersza.',
        'Prawidłowa odpowiedź: C (29). Obliczenia: 2²=4, 3²=9, 4²=16. Suma: 4+9+16=29.',
        'Prawidłowa odpowiedź: B. VAR pomaga unikać powtarzania kodu, poprawia czytelność i wydajność miar (wartość obliczana tylko raz).',
        'Prawidłowa odpowiedź: B. Zmienna zadeklarowana przed funkcją iteracyjną jest obliczana tylko raz i jej wartość jest używana we wszystkich iteracjach.',
        'Prawidłowa odpowiedź: C. Zmienna VAR może zawierać liczby, teksty, tabele i wyniki obliczeń - jest bardzo wszechstronna.'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: 17dd7ac3-7912-4fbd-89f3-4dbf4d2f12cb

        measure '06a. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Quiz: DAX - Zaawansowane Kwerendy (VAR i RETURN)</title>
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
    
            .question-box {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 20px;
                margin: 1.5em 0;
                border-radius: 3px;
            }
    
            .question-box p {
                margin: 0;
                font-size: 1.05em;
                color: #1a1a1a;
            }
    
            .answers {
                margin-top: 1.5em;
            }
    
            .answer-option {
                background: white;
                border: 2px solid #e1e4e8;
                padding: 15px 20px;
                margin: 10px 0;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 1.05em;
            }
    
            .answer-option:hover {
                border-color: #6b1718;
                background: #fef5f5;
            }
    
            .answer-option.selected {
                border-color: #6b1718;
                background: #ffe5e6;
            }
    
            .answer-option.correct {
                border-color: #ccc;
                background: #d4edda;
            }
    
            .answer-option.incorrect {
                border-color: #b82b4e;
                background: #f8d7da;
            }
    
            .feedback {
                margin-top: 1.5em;
                padding: 15px 20px;
                border-radius: 4px;
                display: none;
                font-size: 1.05em;
            }
    
            .feedback.show {
                display: block;
            }
    
            .feedback.correct {
                background: #d4edda;
                border-left: 3px solid #28a745;
                color: #155724;
            }
    
            .feedback.incorrect {
                background: #f8d7da;
                border-left: 3px solid #b82b4e;
                color: #721c24;
            }
    
            .check-button {
                margin-top: 1.5em;
                background: #121212;
            }
    
            .check-button:hover:not(:disabled) {
                background: #111111;
            }
    
            .check-button:disabled {
                background: #ccc;
            }
    
            pre {
                background: #f8f9fa;
                border-left: 3px solid #6b1718;
                padding: 18px;
                margin: 1em 0;
                overflow-x: auto;
                border-radius: 3px;
            }
    
            code {
                font-family: 'Fira Code', 'Courier New', monospace;
                font-size: 0.95em;
                color: #b82b4e;
            }
    
            .score-box {
                background: #6b1718;
                color: white;
                padding: 20px;
                border-radius: 4px;
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 2em;
            }
    
            .summary-item {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 4px;
                border-left: 3px solid #ccc;
            }
    
            .summary-item.correct {
                border-left-color: #28a745;
            }
    
            .summary-item.incorrect {
                border-left-color: #b82b4e;
            }
    
            strong {
                font-weight: 700;
                color: #1a1a1a;
            }
    
            p {
                margin-bottom: 1em;
            }
    </style>
</head>
<body>

<div class='container'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>8</span>
        </span>
        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>
    </div>

    <!-- Pytanie 1 -->
    <div class='page active'>
        <h1>Pytanie 1</h1>
        <div class='question-box'>
            <p><strong>Do czego służy słowo kluczowe VAR w DAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Do zwracania wyniku miary
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Do deklarowania zmiennych i przechowywania wartości
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Do iteracji po wierszach tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) Do filtrowania danych
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Ile razy może wystąpić słowo RETURN w jednej mierze DAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Dowolnie wiele razy
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) Tylko raz
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) Co najmniej dwa razy
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) RETURN nie jest wymagane w miarach
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Co się stanie ze zmiennymi VAR wewnątrz funkcji iteracyjnej jak SUMX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) Są obliczane tylko raz przed rozpoczęciem iteracji
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) Są obliczane na nowo w każdej iteracji dla aktualnego wiersza
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) Nie można używać VAR wewnątrz funkcji iteracyjnych
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) Zachowują wartość z poprzedniej iteracji
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Jaki będzie wynik tego kodu?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) 9
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) 24
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) 29
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) 16
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Jakie są główne zalety używania zmiennych VAR?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) Tylko poprawa czytelności kodu
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) Unikanie powtarzania kodu, poprawa czytelności i wydajności
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Tylko poprawa wydajności
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Zmienne są wymagane przez DAX
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Kiedy zmienna zadeklarowana PRZED funkcją iteracyjną jest obliczana?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) W każdej iteracji na nowo
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) Tylko raz przed rozpoczęciem iteracji
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) Po zakończeniu wszystkich iteracji
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) Nigdy, jest to błąd składni
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Co może zawierać zmienna VAR?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(6, 0)'>
                A) Tylko liczby
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 1)'>
                B) Tylko teksty i liczby
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 2)'>
                C) Liczby, teksty, tabele i wyniki obliczeń
            </div>
            <div class='answer-option' onclick='selectAnswer(6, 3)'>
                D) Tylko wyniki funkcji agregujących
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(6, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-6'></div>
    </div>

    <!-- Podsumowanie quizu -->
    <div class='page'>
        <h1>Podsumowanie quizu</h1>
        <div class='score-box' id='finalScore'>
            Twój wynik: <span id='scoreText'>0/7</span> (<span id='percentText'>0%</span>)
        </div>
        <div id='summaryContent'></div>
        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 8;
    const totalQuestions = 7;
    
    const userAnswers = new Array(totalQuestions).fill(null);
    const answeredQuestions = new Array(totalQuestions).fill(false);
    
    const correctAnswers = [1, 1, 1, 2, 1, 1, 2];
    
    const explanations = [
        'Prawidłowa odpowiedź: B. VAR służy do deklarowania zmiennych i przechowywania w nich wartości (liczb, tekstów, tabel, wyników obliczeń).',
        'Prawidłowa odpowiedź: B. W jednej mierze może być tylko jedno RETURN, które zwraca końcowy wynik miary.',
        'Prawidłowa odpowiedź: B. Zmienne VAR wewnątrz funkcji iteracyjnych są obliczane na nowo w każdej iteracji, dostosowując się do aktualnego wiersza.',
        'Prawidłowa odpowiedź: C (29). Obliczenia: 2²=4, 3²=9, 4²=16. Suma: 4+9+16=29.',
        'Prawidłowa odpowiedź: B. VAR pomaga unikać powtarzania kodu, poprawia czytelność i wydajność miar (wartość obliczana tylko raz).',
        'Prawidłowa odpowiedź: B. Zmienna zadeklarowana przed funkcją iteracyjną jest obliczana tylko raz i jej wartość jest używana we wszystkich iteracjach.',
        'Prawidłowa odpowiedź: C. Zmienna VAR może zawierać liczby, teksty, tabele i wyniki obliczeń - jest bardzo wszechstronna.'
    ];
    
    document.getElementById('totalPages').textContent = totalPages;
    
        function selectAnswer(questionIndex, answerIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            answers.forEach(a => a.classList.remove('selected'));
            answers[answerIndex].classList.add('selected');
            userAnswers[questionIndex] = answerIndex;
        }
    
        function checkAnswer(questionIndex, correctIndex) {
            if (answeredQuestions[questionIndex]) return;
    
            const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
            const feedback = document.getElementById('feedback-' + questionIndex);
            const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');
    
            if (userAnswers[questionIndex] === null) {
                feedback.className = 'feedback show incorrect';
                feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
                return;
            }
    
            answeredQuestions[questionIndex] = true;
            checkBtn.disabled = true;
    
            const isCorrect = userAnswers[questionIndex] === correctIndex;
    
            answers.forEach((answer, index) => {
                answer.style.cursor = 'default';
                if (index === correctIndex) {
                    answer.classList.add('correct');
                } else if (index === userAnswers[questionIndex]) {
                    answer.classList.add('incorrect');
                }
            });
    
            feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
            feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];
    
            if (questionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    changePage(1);
                }, 2500);
            } else {
                setTimeout(() => {
                    showSummary();
                    changePage(1);
                }, 2500);
            }
        }
    
        function showSummary() {
            let correctCount = 0;
            for (let i = 0; i < totalQuestions; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    correctCount++;
                }
            }
    
            const percentage = Math.round((correctCount / totalQuestions) * 100);
            document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
            document.getElementById('percentText').textContent = percentage + '%';
    
            let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
            for (let i = 0; i < totalQuestions; i++) {
                const isCorrect = userAnswers[i] === correctAnswers[i];
                summaryHTML += `
                    <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                        <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                        <small>${explanations[i]}</small>
                    </div>
                `;
            }
    
            document.getElementById('summaryContent').innerHTML = summaryHTML;
        }
    
        function restartQuiz() {
            userAnswers.fill(null);
            answeredQuestions.fill(false);
            currentPage = 1;
    
            document.querySelectorAll('.page').forEach((page, index) => {
                if (index < totalQuestions) {
                    const answers = page.querySelectorAll('.answer-option');
                    answers.forEach(a => {
                        a.className = 'answer-option';
                        a.style.cursor = 'pointer';
                    });
                    const feedback = page.querySelector('.feedback');
                    feedback.className = 'feedback';
                    const checkBtn = page.querySelector('.check-button');
                    checkBtn.disabled = false;
                }
            });
    
            showPage(1);
        }
    
        function showPage(n) {
            const pages = document.querySelectorAll('.page');
    
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
    
            pages.forEach(page => page.classList.remove('active'));
            pages[currentPage - 1].classList.add('active');
    
            document.getElementById('currentPage').textContent = currentPage;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
    
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    
        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }
    
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
        });
    
        showPage(1);
</script>

</body>
</html>

"
```
            lineageTag: 09781396-d304-486e-b7ec-23cf8e404843

        measure '300. INPUTS - 300. INPUTS Overview' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>300. INPUTS Overview</title>
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

<div class='container' id='viz_14143fab'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_14143fab' onclick='changePage_14143fab(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_14143fab'>1</span> z <span id='totalPages_14143fab'>1</span>
        </span>
        <button id='nextBtn_14143fab' onclick='changePage_14143fab(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <pre><code>type: folder_brief_live</code></pre>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '14143fab';
    var containerId = 'viz_' + vizId;

    var currentPage_14143fab = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_14143fab'] = function(n) {
        if (n > totalPages) currentPage_14143fab = totalPages;
        if (n < 1) currentPage_14143fab = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_14143fab - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_14143fab;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_14143fab === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_14143fab === totalPages);
    };

    window['changePage_14143fab'] = function(n) {
        currentPage_14143fab += n;
        window['showPage_14143fab'](currentPage_14143fab);
    };

    // Inicjalizacja
    window['showPage_14143fab'](1);

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
            lineageTag: f1ba7940-3988-4980-a537-aaf69d53d5ca

        measure 'CSS - Quiz - Blue' = ```
"
<style>
* {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            font-size: 16px;
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
            background: #0066cc;
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
            background: #0052a3;
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
            font-size: 1.8em;
            font-weight: 600;
            margin-bottom: 1em;
            color: #1a1a1a;
        }

        .question-box {
            background: #f8f9fa;
            border-left: 3px solid #0066cc;
            padding: 20px;
            margin: 1.5em 0;
            border-radius: 3px;
        }

        .answers {
            margin-top: 1.5em;
        }

        .answer-option {
            background: white;
            border: 2px solid #e1e4e8;
            padding: 15px 20px;
            margin: 10px 0;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 1.05em;
        }

        .answer-option:hover {
            border-color: #0066cc;
            background: #f0f7ff;
        }

        .answer-option.selected {
            border-color: #0066cc;
            background: #e6f2ff;
        }

        .answer-option.correct {
            border-color: #28a745;
            background: #d4edda;
        }

        .answer-option.incorrect {
            border-color: #dc3545;
            background: #f8d7da;
        }

        .feedback {
            margin-top: 1.5em;
            padding: 15px 20px;
            border-radius: 4px;
            display: none;
            font-size: 1.05em;
        }

        .feedback.show {
            display: block;
        }

        .feedback.correct {
            background: #d4edda;
            border-left: 3px solid #28a745;
            color: #155724;
        }

        .feedback.incorrect {
            background: #f8d7da;
            border-left: 3px solid #dc3545;
            color: #721c24;
        }

        .check-button {
            margin-top: 1.5em;
            background: #28a745;
        }

        .check-button:hover:not(:disabled) {
            background: #218838;
        }

        .check-button:disabled {
            background: #ccc;
        }

        pre {
            background: #f8f9fa;
            border-left: 3px solid #0066cc;
            padding: 18px;
            margin: 1em 0;
            overflow-x: auto;
            border-radius: 3px;
        }

        code {
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
        }

        .score-box {
            background: #0066cc;
            color: white;
            padding: 20px;
            border-radius: 4px;
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 2em;
        }

        .summary-item {
            background: #f8f9fa;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 3px solid #ccc;
        }

        .summary-item.correct {
            border-left-color: #28a745;
        }

        .summary-item.incorrect {
            border-left-color: #dc3545;
        }
</style>
"
```
            lineageTag: 942ac9f7-633d-4536-99f3-c3e67a44a1ca

        measure 'CSS - Quiz - Cherry' = ```
"
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

        .question-box {
            background: #f8f9fa;
            border-left: 3px solid #6b1718;
            padding: 20px;
            margin: 1.5em 0;
            border-radius: 3px;
        }

        .question-box p {
            margin: 0;
            font-size: 1.05em;
            color: #1a1a1a;
        }

        .answers {
            margin-top: 1.5em;
        }

        .answer-option {
            background: white;
            border: 2px solid #e1e4e8;
            padding: 15px 20px;
            margin: 10px 0;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 1.05em;
        }

        .answer-option:hover {
            border-color: #6b1718;
            background: #fef5f5;
        }

        .answer-option.selected {
            border-color: #6b1718;
            background: #ffe5e6;
        }

        .answer-option.correct {
            border-color: #ccc;
            background: #d4edda;
        }

        .answer-option.incorrect {
            border-color: #b82b4e;
            background: #f8d7da;
        }

        .feedback {
            margin-top: 1.5em;
            padding: 15px 20px;
            border-radius: 4px;
            display: none;
            font-size: 1.05em;
        }

        .feedback.show {
            display: block;
        }

        .feedback.correct {
            background: #d4edda;
            border-left: 3px solid #28a745;
            color: #155724;
        }

        .feedback.incorrect {
            background: #f8d7da;
            border-left: 3px solid #b82b4e;
            color: #721c24;
        }

        .check-button {
            margin-top: 1.5em;
            background: #121212;
        }

        .check-button:hover:not(:disabled) {
            background: #111111;
        }

        .check-button:disabled {
            background: #ccc;
        }

        pre {
            background: #f8f9fa;
            border-left: 3px solid #6b1718;
            padding: 18px;
            margin: 1em 0;
            overflow-x: auto;
            border-radius: 3px;
        }

        code {
            font-family: 'Fira Code', 'Courier New', monospace;
            font-size: 0.95em;
            color: #b82b4e;
        }

        .score-box {
            background: #6b1718;
            color: white;
            padding: 20px;
            border-radius: 4px;
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 2em;
        }

        .summary-item {
            background: #f8f9fa;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 3px solid #ccc;
        }

        .summary-item.correct {
            border-left-color: #28a745;
        }

        .summary-item.incorrect {
            border-left-color: #b82b4e;
        }

        strong {
            font-weight: 700;
            color: #1a1a1a;
        }

        p {
            margin-bottom: 1em;
        }
</style>
"
```
            lineageTag: e9469831-7008-4ecb-b3f5-f6b4b4888539

        measure 'CSS - Quiz- Cherry' = ```
"
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

        .question-box {
            background: #f8f9fa;
            border-left: 3px solid #6b1718;
            padding: 20px;
            margin: 1.5em 0;
            border-radius: 3px;
        }

        .question-box p {
            margin: 0;
            font-size: 1.05em;
            color: #1a1a1a;
        }

        .answers {
            margin-top: 1.5em;
        }

        .answer-option {
            background: white;
            border: 2px solid #e1e4e8;
            padding: 15px 20px;
            margin: 10px 0;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 1.05em;
        }

        .answer-option:hover {
            border-color: #6b1718;
            background: #fef5f5;
        }

        .answer-option.selected {
            border-color: #6b1718;
            background: #ffe5e6;
        }

        .answer-option.correct {
            border-color: #ccc;
            background: #d4edda;
        }

        .answer-option.incorrect {
            border-color: #b82b4e;
            background: #f8d7da;
        }

        .feedback {
            margin-top: 1.5em;
            padding: 15px 20px;
            border-radius: 4px;
            display: none;
            font-size: 1.05em;
        }

        .feedback.show {
            display: block;
        }

        .feedback.correct {
            background: #d4edda;
            border-left: 3px solid #28a745;
            color: #155724;
        }

        .feedback.incorrect {
            background: #f8d7da;
            border-left: 3px solid #b82b4e;
            color: #721c24;
        }

        .check-button {
            margin-top: 1.5em;
            background: #121212;
        }

        .check-button:hover:not(:disabled) {
            background: #111111;
        }

        .check-button:disabled {
            background: #ccc;
        }

        pre {
            background: #f8f9fa;
            border-left: 3px solid #6b1718;
            padding: 18px;
            margin: 1em 0;
            overflow-x: auto;
            border-radius: 3px;
        }

        code {
            font-family: 'Fira Code', 'Courier New', monospace;
            font-size: 0.95em;
            color: #b82b4e;
        }

        .score-box {
            background: #6b1718;
            color: white;
            padding: 20px;
            border-radius: 4px;
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 2em;
        }

        .summary-item {
            background: #f8f9fa;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 3px solid #ccc;
        }

        .summary-item.correct {
            border-left-color: #28a745;
        }

        .summary-item.incorrect {
            border-left-color: #b82b4e;
        }

        strong {
            font-weight: 700;
            color: #1a1a1a;
        }

        p {
            margin-bottom: 1em;
        }
</style>
"
```
            lineageTag: 5c9c8d2c-5676-4795-a86c-0fcca2f08e06

        measure 'CSS - Teoria - Blue' = ```
"
<style>
<style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
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
            background: #0066cc;
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
            background: #0052a3;
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
            color: #1a1a1a;
            border-bottom: 2px solid #1a1a1a;
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
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
            color: #d73a49;
        }
        
        pre {
            background: #f8f9fa;
            border-left: 3px solid #0066cc;
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
            color: #0066cc;
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
            border-left: 3px solid #0066cc;
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
            border-left: 3px solid #0066cc;
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
</style>
"
```
            lineageTag: 9a8c54a0-04cf-4527-bfeb-62764f2c9ac5

        measure 'CSS - Teoria - Cherry' = ```
"
<style>
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
</style>
"
```
            lineageTag: 6dc0df61-c1cd-4af8-abd8-d293c107a713

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

