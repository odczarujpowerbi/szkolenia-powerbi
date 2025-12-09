createOrReplace

    table _HTML
        lineageTag: 2f3b66d4-f70d-4c54-9722-0f806c551f1c

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
                background: #df4a16;
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
                background: #df7a16;
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
                color: #df4a16;
                border-bottom: 2px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
                color: #df4a16;
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
                border-left: 3px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
            lineageTag: 99923b5c-b809-4745-9bf4-49ef1b8610ce

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
                background: #df4a16;
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
                background: #df7a16;
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
                color: #df4a16;
                border-bottom: 2px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
                color: #df4a16;
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
                border-left: 3px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
        <li>Zaznacz następujące opcje:</li>
        </ol>
        <p>   - <strong>Obliczenia wizualne</strong> - pozwala na tworzenie bardziej zaawansowanych wizualizacji</p>
        <p>   - <strong>Nowe wizualizacje</strong> - daje dostęp do najnowszych typów wizualizacji</p>
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
        <li>Wybierz odpowiedni język - zalecany jest Angielski ze względu na:</li>
        </ol>
        <p>	- Prostszą integrację z AI</p>
        <p>	- Spójność nazewnictwa z dokumentacją Microsoft Learn</p>
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
            lineageTag: c8fc8bcf-a315-4ec1-b663-f9d7784fbe28

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
                background: #df4a16;
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
                background: #df7a16;
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
                color: #df4a16;
                border-bottom: 2px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
                color: #df4a16;
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
                border-left: 3px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
            lineageTag: 5ddd701a-079a-49ba-b83f-b8582e226a44

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
                background: #df4a16;
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
                background: #df7a16;
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
                color: #df4a16;
                border-bottom: 2px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
                color: #df4a16;
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
                border-left: 3px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
            lineageTag: 59546fa0-92f2-4b94-8b79-e139764db14a

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
                background: #df4a16;
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
                background: #df7a16;
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
                color: #df4a16;
                border-bottom: 2px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
                color: #df4a16;
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
                border-left: 3px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
            lineageTag: f1300f69-239c-4903-a142-a3cc7f657aea

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
                background: #df4a16;
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
                background: #df7a16;
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
                color: #df4a16;
                border-bottom: 2px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
                color: #df4a16;
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
                border-left: 3px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
            lineageTag: 93a2c7a5-2b84-4323-b7d3-3e6ec7810efc

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
                background: #df4a16;
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
                background: #df7a16;
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
                color: #df4a16;
                border-bottom: 2px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
                color: #df4a16;
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
                border-left: 3px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
            lineageTag: 643bb5ad-3170-4b36-9561-a48322a892a0

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
                background: #df4a16;
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
                background: #df7a16;
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
                color: #df4a16;
                border-bottom: 2px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
                color: #df4a16;
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
                border-left: 3px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
            Strona <span id='currentPage_bb3ff736'>1</span> z <span id='totalPages_bb3ff736'>10</span>
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
        <h2>Podstawowa składnia: NazwaTabeli[NazwaKolumny]</h2>
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
        <h2>Nazwy z apostrofami (gdy zawierają spacje lub znaki specjalne)</h2>
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
        <h2>Odwoływanie się do miar: [NazwaMiary]</h2>
        <p>Miary (measures) odwołujesz się <strong>bez nazwy tabeli</strong>, tylko w nawiasach kwadratowych:</p>
        <pre><code>[Suma Sprzedaży]
        [Średnia Cena]
        [Liczba Klientów]</code></pre>
        <p>Możesz też użyć pełnej notacji z nazwą tabeli, ale nie jest to wymagane:</p>
        <pre><code>Sprzedaz[Suma Sprzedaży]  <span class='dax-comment'>-- Działa, ale zwykle niepotrzebne</span></code></pre>

    </div>

    <!-- Strona 5 -->
    <div class='page'>
        <h2>Pełna nazwa tabeli (gdy jest w innym modelu)</h2>
        <p>Jeśli pracujesz z wieloma modelami danych, możesz użyć pełnej ścieżki:</p>
        <pre><code>'Nazwa Modelu'[Nazwa Tabeli][Nazwa Kolumny]</code></pre>
        <p>W większości przypadków wystarczy standardowa notacja <code>Tabela[Kolumna]</code>.</p>

    </div>

    <!-- Strona 6 -->
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

    <!-- Strona 7 -->
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

    <!-- Strona 8 -->
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

    <!-- Strona 9 -->
    <div class='page'>
        <h1>Operatory logiczne</h1>
        <pre><code>&&  <span class='dax-comment'>-- AND (i)</span>
        ||  <span class='dax-comment'>-- OR (lub)</span>
        NOT <span class='dax-comment'>-- NOT (negacja)</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Czy Premium = 
        Klienci[Kategoria] = 'VIP' && Klienci[Przychód] &gt; <span class='dax-number'>10000</span></code></pre>

    </div>

    <!-- Strona 10 -->
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
            lineageTag: 5505276e-a13b-4bcf-99d8-be9707fafed9

        measure '02. Wprowadzenie do CALCULATE - Wprowadzenie do CALCULATE' = ```
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
                background: #df4a16;
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
                background: #df7a16;
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
                color: #df4a16;
                border-bottom: 2px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
                color: #df4a16;
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
                border-left: 3px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
            Strona <span id='currentPage_a6296909'>1</span> z <span id='totalPages_a6296909'>11</span>
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

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Użycie <code>CALCULATE</code></h1>
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

    <!-- Strona 4 -->
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

    <!-- Strona 5 -->
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

    </div>

    <!-- Strona 6 -->
    <div class='page'>
        <h1>Operatory logiczne w <code>CALCULATE</code></h1>
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

    <!-- Strona 7 -->
    <div class='page'>
        <h2>Operator AND (<code>&&</code>)</h2>
        <p>Używamy gdy <strong>wszystkie</strong> warunki muszą być spełnione jednocześnie.</p>
        <p><strong>Przykład: Sprzedaż w dni robocze</strong></p>
        <p>Załóżmy, że w tabeli dKalendarz mamy kolumnę <code>DzienTygodnia</code> (dzień tygodnia: 1 = poniedziałek, ..., 7 = niedziela).</p>
        <pre><code>Sprzedaż Dni Robocze =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKalendarz[DzienTygodnia] &gt;= <span class='dax-number'>1</span> && dKalendarz[DzienTygodnia] &lt;= <span class='dax-number'>5</span>
        )</code></pre>
        <p><strong>Warunek:</strong> <code>DzienTygodnia >= 1</code> <strong>I</strong> <code>DzienTygodnia <= 5</code></p>
        <p>Alternatywna składnia z funkcją AND():</p>
        <pre><code>Sprzedaż Dni Robocze (Alternatywna) =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            <span class='dax-function'>AND</span>(dKalendarz[DzienTygodnia] &gt;= <span class='dax-number'>1</span>, dKalendarz[DzienTygodnia] &lt;= <span class='dax-number'>5</span>)
        )</code></pre>

    </div>

    <!-- Strona 8 -->
    <div class='page'>
        <h2>Operator OR (<code>||</code>)</h2>
        <p>Używamy gdy <strong>przynajmniej jeden</strong> z warunków musi być spełniony.</p>
        <p><strong>Przykład: Sprzedaż w weekendy</strong></p>
        <pre><code>Sprzedaż Weekendy =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKalendarz[DzienTygodnia] = <span class='dax-number'>6</span> || dKalendarz[DzienTygodnia] = <span class='dax-number'>7</span>
        )</code></pre>
        <p><strong>Warunek:</strong> <code>DzienTygodnia = 6</code> <strong>LUB</strong> <code>DzienTygodnia = 7</code></p>
        <p>Alternatywna składnia z funkcją OR():</p>
        <pre><code>Sprzedaż Weekendy (Alternatywna) =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            <span class='dax-function'>OR</span>(dKalendarz[DzienTygodnia] = <span class='dax-number'>6</span>, dKalendarz[DzienTygodnia] = <span class='dax-number'>7</span>)
        )</code></pre>

    </div>

    <!-- Strona 9 -->
    <div class='page'>
        <h2>Operator IN - eleganckie sprawdzanie wielu wartości</h2>
        <p>Zamiast pisać wielokrotnie OR, użyj operatora <code>IN</code>:</p>
        <pre><code>// ✗ Nieeleganckie
        Sprzedaż Napoje lub Słodycze =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKategorie[Kategoria] = 'NAPOJE' || dKategorie[Kategoria] = 'SŁODYCZE'
        )

        // ✓ Eleganckie
        Sprzedaż Napoje lub Słodycze =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKategorie[Kategoria] IN {'NAPOJE', 'SŁODYCZE'}
        )</code></pre>
        <p><strong>Operator IN</strong> sprawdza, czy wartość znajduje się w podanym zestawie.</p>

    </div>

    <!-- Strona 10 -->
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

    </div>

    <!-- Strona 11 -->
    <div class='page'>
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
            lineageTag: a77a37b9-a271-48c0-850c-fce1a139192d

        measure '03. DAX - Zmienne' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>03. DAX - Zmienne</title>
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
                background: #df4a16;
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
                background: #df7a16;
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
                color: #df4a16;
                border-bottom: 2px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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
                color: #df4a16;
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
                border-left: 3px solid #df4a16;
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
                border-left: 3px solid #df4a16;
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

<div class='container' id='viz_8c2a7e79'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_8c2a7e79' onclick='changePage_8c2a7e79(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_8c2a7e79'>1</span> z <span id='totalPages_8c2a7e79'>4</span>
        </span>
        <button id='nextBtn_8c2a7e79' onclick='changePage_8c2a7e79(1)'>Następna →</button>
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

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '8c2a7e79';
    var containerId = 'viz_' + vizId;

    var currentPage_8c2a7e79 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_8c2a7e79'] = function(n) {
        if (n > totalPages) currentPage_8c2a7e79 = totalPages;
        if (n < 1) currentPage_8c2a7e79 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_8c2a7e79 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_8c2a7e79;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_8c2a7e79 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_8c2a7e79 === totalPages);
    };

    window['changePage_8c2a7e79'] = function(n) {
        currentPage_8c2a7e79 += n;
        window['showPage_8c2a7e79'](currentPage_8c2a7e79);
    };

    // Inicjalizacja
    window['showPage_8c2a7e79'](1);

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
            lineageTag: 606e3815-2711-4fe5-a047-3726f631a2a3

        measure 'CSS - Czerwony' = ```
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
            background: #df4a16;
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
            background: #df7a16;
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
            color: #df4a16;
            border-bottom: 2px solid #df4a16;
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
            border-left: 3px solid #df4a16;
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
            color: #df4a16;
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
            border-left: 3px solid #df4a16;
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
            border-left: 3px solid #df4a16;
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
            lineageTag: 98f37c8f-81a0-455a-94c1-408208f3dca1

        measure 'CSS - Niebieski' = ```
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
            lineageTag: dfd58cd8-54a0-4352-b8e2-d0a5606f2532

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

