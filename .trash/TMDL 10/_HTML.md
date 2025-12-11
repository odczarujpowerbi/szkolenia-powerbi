createOrReplace

    table _HTML
        lineageTag: 608d0041-52ce-40b7-a893-6d01791467e4

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
        <pre><code>DAX
        EVALUATE
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
            lineageTag: f7b864da-e172-4f12-a2b6-de4a8104593e

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
        <p>Dzięki temu kliknięcie na element jednej wizualizacji (np. kolumnę na wykresie) automatycznie przefiltruje pozostałe wizualizacje na stronie raportu.</p>

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
        <pre><code>DAX
        // Wersja polska
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
            lineageTag: e33b0c1c-cbf4-4c24-a9f4-e6ce699f3ae1

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
        <pre><code>DAX
        Suma Sprzedaży = <span class='dax-function'>SUM</span>(Sprzedaz[Kwota])</code></pre>
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
        <pre><code>DAX
        Średnia Cena = <span class='dax-function'>AVERAGE</span>(Produkty[Cena])</code></pre>
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
        <pre><code>DAX
        Liczba Transakcji = <span class='dax-function'>COUNT</span>(Sprzedaz[ID Transakcji])</code></pre>
        <p><strong>Uwaga:</strong> COUNT liczy tylko wartości <strong>niepuste</strong> (pomija BLANK).</p>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>COUNTA – Liczba wartości niepustych (dowolny typ)</h1>
        <p>Podobnie jak COUNT, ale działa na <strong>wszystkich typach danych</strong> (tekst, liczby, daty):</p>
        <pre><code>DAX
        Liczba Produktów = <span class='dax-function'>COUNTA</span>(Sprzedaz[Nazwa Produktu])</code></pre>

    </div>

    <!-- Strona 5 -->
    <div class='page'>
        <h1>COUNTROWS – Liczba wierszy w tabeli</h1>
        <p>Liczy wszystkie wiersze w tabeli (nawet jeśli mają puste wartości):</p>
        <pre><code>DAX
        Liczba Zamówień = <span class='dax-function'>COUNTROWS</span>(Sprzedaz)</code></pre>
        <p><strong>Różnica COUNT vs COUNTROWS:</strong></p>
        <ul>
        <li><code>COUNT</code> – liczy niepuste wartości w <strong>konkretnej kolumnie</strong></li>
        <li><code>COUNTROWS</code> – liczy <strong>wszystkie wiersze w tabeli</strong></li>
        </ul>

    </div>

    <!-- Strona 6 -->
    <div class='page'>
        <h1>MIN i MAX – Minimum i maksimum</h1>
        <pre><code>DAX
        Najniższa Cena = <span class='dax-function'>MIN</span>(Sprzedaz[Cena])
        Najwyższa Cena = <span class='dax-function'>MAX</span>(Sprzedaz[Cena])</code></pre>

    </div>

    <!-- Strona 7 -->
    <div class='page'>
        <h1>DISTINCTCOUNT – Liczba unikalnych wartości</h1>
        <p>Liczy ile jest <strong>unikalnych</strong> (niepowtarzających się) wartości:</p>
        <pre><code>DAX
        Liczba Unikalnych Klientów = <span class='dax-function'>DISTINCTCOUNT</span>(Sprzedaz[Ilość])</code></pre>
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
            lineageTag: 02295f31-edde-4046-a785-e3d4f8206fdf

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
        <pre><code>DAX
        <span class='dax-function'>DATE</span>(&lt;rok&gt;, &lt;miesiąc&gt;, &lt;dzień&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Data Bazowa = <span class='dax-function'>DATE</span>(<span class='dax-number'>2024</span>, <span class='dax-number'>1</span>, <span class='dax-number'>1</span>)</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>TODAY i NOW – Dzisiejsza data</h1>
        <pre><code>DAX
        <span class='dax-function'>TODAY</span>()     <span class='dax-comment'>-- Dzisiejsza data (bez godziny)</span>
        <span class='dax-function'>NOW</span>()       <span class='dax-comment'>-- Dzisiejsza data i godzina</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Aktualna Data = <span class='dax-function'>TODAY</span>()</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>YEAR, MONTH, DAY – Wyciąganie składników daty</h1>
        <pre><code>DAX
        <span class='dax-function'>YEAR</span>(&lt;data&gt;)   <span class='dax-comment'>-- Rok</span>
        <span class='dax-function'>MONTH</span>(&lt;data&gt;)  <span class='dax-comment'>-- Miesiąc (1-12)</span>
        <span class='dax-function'>DAY</span>(&lt;data&gt;)    <span class='dax-comment'>-- Dzień (1-31)</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Rok Sprzedaży = <span class='dax-function'>YEAR</span>(Sprzedaz[Data Sprzedaży])
        Miesiąc Sprzedaży = <span class='dax-function'>MONTH</span>(Sprzedaz[Data Sprzedaży])</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>DATEDIFF – Różnica między datami</h1>
        <pre><code>DAX
        <span class='dax-function'>DATEDIFF</span>(&lt;data_początkowa&gt;, &lt;data_końcowa&gt;, &lt;jednostka&gt;)</code></pre>
        <p><strong>Jednostki:</strong> DAY, MONTH, YEAR, QUARTER</p>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Dni Od Zamówienia = 
        <span class='dax-function'>DATEDIFF</span>(Sprzedaz[Data Sprzedaży], <span class='dax-function'>TODAY</span>(), DAY)</code></pre>

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
            lineageTag: e76ddde1-24d5-42c4-b874-b7be796ef37a

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
        <pre><code>DAX
        <span class='dax-function'>IF</span>(&lt;warunek&gt;, &lt;wartość_jeśli_prawda&gt;, &lt;wartość_jeśli_fałsz&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Kategoria Sprzedaży = 
        <span class='dax-function'>IF</span>(
            Sprzedaz[Wartość Netto] &gt; <span class='dax-number'>1000</span>,
            'Wysoka',
            'Niska'
        )</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>AND – Sprawdza czy wszystkie warunki są prawdziwe</h1>
        <pre><code>DAX
        <span class='dax-function'>AND</span>(&lt;warunek1&gt;, &lt;warunek2&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Czy Duże Zamówienie = 
        <span class='dax-function'>IF</span>(
            <span class='dax-function'>AND</span>(Sprzedaż[Wartość Sprzedaży] &gt; <span class='dax-number'>1000</span>, Sprzedaż[Ilość] &gt; <span class='dax-number'>50</span>),
            'TAK',
            'NIE'
        )</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>OR – Sprawdza czy przynajmniej jeden warunek jest prawdziwy</h1>
        <pre><code>DAX
        <span class='dax-function'>OR</span>(&lt;warunek1&gt;, &lt;warunek2&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Napoje w Centralnej Polsce = 
        <span class='dax-function'>IF</span>(
            <span class='dax-function'>OR</span>(Sprzedaz[Kategoria] = 'NAPOJE', Sprzedaz[Region] = 'Centralna Polska'),
            'TAK',
            'NIE'
        )</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>NOT – Negacja warunku</h1>
        <pre><code>DAX
        <span class='dax-function'>NOT</span>(&lt;warunek&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Czy nie napój = 
        <span class='dax-function'>IF</span>(
            <span class='dax-function'>NOT</span>(Sprzedaz[Kategoria] = 'NAPOJE'),
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
            lineageTag: ec56a874-77d5-482b-8d4d-3fd7cc70c4fc

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
        <pre><code>DAX
        <span class='dax-function'>CONCATENATE</span>(&lt;tekst1&gt;, &lt;tekst2&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Pełna Nazwa = <span class='dax-function'>CONCATENATE</span>(Sprzedaz[Kategoria], ' - ', Sprzedaz[Nazwa Produktu])</code></pre>
        <p><strong>Alternatywa</strong></p>
        <pre><code>DAX
        Pełna Nazwa = Sprzedaz[Kategoria] & ' - ' & Sprzedaz[Nazwa Produktu]</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>LEFT, RIGHT, MID – Wyciąganie części tekstu</h1>
        <pre><code>DAX
        <span class='dax-function'>LEFT</span>(&lt;tekst&gt;, &lt;liczba_znaków&gt;)    <span class='dax-comment'>-- Pierwsze znaki od lewej</span>
        <span class='dax-function'>RIGHT</span>(&lt;tekst&gt;, &lt;liczba_znaków&gt;)   <span class='dax-comment'>-- Ostatnie znaki od prawej</span>
        <span class='dax-function'>MID</span>(&lt;tekst&gt;, &lt;start&gt;, &lt;liczba&gt;)   <span class='dax-comment'>-- Znaki ze środka</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Pierwsze <span class='dax-number'>3</span> Znaki = <span class='dax-function'>LEFT</span>(Sprzedaz[Kategoria], <span class='dax-number'>3</span>)
        Ostatnie <span class='dax-number'>2</span> Znaki = <span class='dax-function'>RIGHT</span>(Sprzedaz[Kategoria], <span class='dax-number'>2</span>)</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>UPPER, LOWER – Zmiana wielkości liter</h1>
        <pre><code>DAX
        <span class='dax-function'>UPPER</span>(&lt;tekst&gt;)  <span class='dax-comment'>-- Wszystkie znaki WIELKIE</span>
        <span class='dax-function'>LOWER</span>(&lt;tekst&gt;)  <span class='dax-comment'>-- Wszystkie znaki małe</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Kategoria Wielkie Litery = <span class='dax-function'>UPPER</span>(Sprzedaz[Kategoria])</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>LEN – Długość tekstu</h1>
        <pre><code>DAX
        <span class='dax-function'>LEN</span>(&lt;tekst&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Długość Kodu = <span class='dax-function'>LEN</span>(Sprzedaz[Kategoria])</code></pre>
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
            lineageTag: 82b9c5c4-430b-4e68-9818-e33e7551d1fc

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
        <pre><code>DAX
        Sprzedaz[Cena]</code></pre>
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
        <pre><code>DAX
        'Tabela Sprzedaży'[Kwota Netto]
        'Dane-Produktów'[Nazwa Produktu]
        '<span class='dax-number'>2024</span> Wyniki'[Przychód]
        Produkty[Cena (netto)]</code></pre>
        <p><strong>Przykład błędny:</strong></p>
        <pre><code>DAX
        Tabela Sprzedaży[Kwota Netto]  <span class='dax-comment'>-- ❌ Błąd składni!</span></code></pre>
        <p><strong>Przykład poprawny:</strong></p>
        <pre><code>DAX
        'Tabela Sprzedaży'[Kwota Netto]  <span class='dax-comment'>-- ✅ Działa</span></code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>Odwoływanie się do miar</h2>
        <p>Miary (measures) odwołujesz się <strong>bez nazwy tabeli</strong>, tylko w nawiasach kwadratowych:</p>
        <pre><code>DAX
        [Suma Sprzedaży]
        [Średnia Cena]
        [Liczba Klientów]</code></pre>
        <p>Możesz też użyć pełnej notacji z nazwą tabeli, ale nie jest to wymagane:</p>
        <pre><code>DAX
        Sprzedaz[Suma Sprzedaży]  <span class='dax-comment'>-- Działa, ale zwykle niepotrzebne</span></code></pre>

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
        <pre><code>DAX
        +   <span class='dax-comment'>-- Dodawanie</span>
        -   <span class='dax-comment'>-- Odejmowanie</span>
        *   <span class='dax-comment'>-- Mnożenie</span>
        /   <span class='dax-comment'>-- Dzielenie</span>
        ^   <span class='dax-comment'>-- Potęgowanie</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Marża = 
        Sprzedaz[Wartość Netto] - Sprzedaz[Koszty Netto]</code></pre>

    </div>

    <!-- Strona 7 -->
    <div class='page'>
        <h1>Operatory porównania</h1>
        <pre><code>DAX
        =   <span class='dax-comment'>-- Równe</span>
        &lt;&gt;  <span class='dax-comment'>-- Różne od</span>
        &gt;   <span class='dax-comment'>-- Większe niż</span>
        &lt;   <span class='dax-comment'>-- Mniejsze niż</span>
        &gt;=  <span class='dax-comment'>-- Większe lub równe</span>
        &lt;=  <span class='dax-comment'>-- Mniejsze lub równe</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Czy Duża Sprzedaż = 
        Sprzedaz[Cena] &gt; <span class='dax-number'>1000</span></code></pre>

    </div>

    <!-- Strona 8 -->
    <div class='page'>
        <h1>Operatory logiczne</h1>
        <pre><code>DAX
        &&  <span class='dax-comment'>-- AND (i)</span>
        ||  <span class='dax-comment'>-- OR (lub)</span>
        NOT <span class='dax-comment'>-- NOT (negacja)</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Czy Premium = 
        Sprzedaz[Kategoria] = 'VIP' && Klienci[Przychód] &gt; <span class='dax-number'>10000</span></code></pre>

    </div>

    <!-- Strona 9 -->
    <div class='page'>
        <h1>Operator łączenia tekstów</h1>
        <pre><code>DAX
        &   <span class='dax-comment'>-- Konkatenacja (łączenie tekstów)</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Pełna Nazwa = 
        Sprzedaz[Kategoria] & ' - ' & Sprzedaz[Nazwa Produktu]</code></pre>
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
            lineageTag: 1c2f320d-38bd-4a7e-aab5-3aff7af7e363

        measure '01a. Gaps' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DAX Gaps</title>
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #333;
        background: transparent;
        padding: 20px;
    }
    
    .container {
        max-width: 900px;
        margin: 0 auto;
        background: transparent;
        padding: 40px;
    }
    
    h3 {
        font-size: 26px;
        line-height: 36px;
        font-weight: 600;
        padding-top: 14px;
        padding-bottom: 6px;
        margin-bottom: 1em;
        color: #6b1718;
        border-bottom: 2px solid #6b1718;
    }
    
    .task-description {
        font-size: 1.1em;
        margin: 20px 0;
    }
    
    .code-container {
        background: #f8f9fa;
        border: 2px solid #e1e4e8;
        border-radius: 6px;
        padding: 25px;
        margin: 30px 0;
        font-family: 'Courier New', monospace;
        font-size: 1.05em;
        line-height: 1.8;
    }
    
    .drop-zone {
        display: inline-block;
        min-width: 180px;
        height: 36px;
        background: white;
        border: 2px dashed #6b1718;
        border-radius: 4px;
        padding: 6px 12px;
        margin: 0 4px;
        vertical-align: middle;
        text-align: center;
        transition: all 0.2s;
    }
    
    .drop-zone.drag-over {
        background: #ffe6e6;
        border-color: #380c0c;
    }
    
    .drop-zone.filled {
        background: #d4edda;
        border: 2px solid #28a745;
        border-style: solid;
    }
    
    .functions-title {
        font-size: 1em;
        margin: 30px 0 15px 0;
        color: #333;
    }
    
    .function-chip {
        display: inline-block;
        background: #6b1718;
        color: white;
        padding: 10px 20px;
        margin: 8px;
        border-radius: 20px;
        cursor: grab;
        font-family: 'Courier New', monospace;
        font-size: 1em;
        font-weight: 500;
        transition: all 0.2s;
        user-select: none;
    }
    
    .function-chip:hover {
        background: #380c0c;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(107, 23, 24, 0.3);
    }
    
    .function-chip:active {
        cursor: grabbing;
    }
    
    .function-chip.used {
        opacity: 0.3;
        cursor: not-allowed;
        pointer-events: none;
    }
    
    .button-group {
        margin-top: 30px;
        display: flex;
        gap: 15px;
        align-items: center;
    }
    
    button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 14px 32px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.05em;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    button:hover {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    button.reset-btn {
        background: #6b1718;
        padding: 8px 16px;
        font-size: 0.9em;
    }
    
    button.reset-btn:hover {
        background: #380c0c;
    }
    
    .feedback {
        margin-top: 25px;
        padding: 20px;
        border-radius: 6px;
        display: none;
        font-size: 1.05em;
    }
    
    .feedback.show {
        display: block;
        animation: slideDown 0.3s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .feedback.correct {
        background: #d4edda;
        border-left: 4px solid #28a745;
        color: #155724;
    }
    
    .feedback.incorrect {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        color: #721c24;
    }
    
    .hint-box {
        background: #fafafa;
        border-left: 4px solid #ccc;
        padding: 15px;
        margin: 20px 0;
        border-radius: 4px;
        color: #121212;
        font-size: 0.95em;
    }
    .pagination {
        display: flex;
        align-items: center;
        justify-content: space-between; 
        gap: 20px;
        margin: 30px auto; 
        padding: 20px;
        border-radius: 6px;
    	max-width: 900px;
        border-bottom: 1px solid #e0e0e0;
        width: 100%;
    }
    
    .page-info {
        font-weight: 600;
        color: #666666; 
    }
    
    .nav-button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1em;
        transition: all 0.2s;
    }
    
    .nav-button:hover:not(:disabled) {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .page {
        display: none;
    }
    
    .page.active {
        display: block;
    }
    </style>
</head>
<body>

<div class='pagination'>
    <button class='nav-button' id='prevBtn' onclick='prevPage()'>← Poprzednie</button>
    <span class='page-info'>Zadanie <span id='currentPage'>1</span> z <span id='totalPages'>6</span></span>
    <button class='nav-button' id='nextBtn' onclick='nextPage()'>Następne →</button>
</div>

<div class='page active' data-page='1'>
<div class='container'>
    <div class='task-description'>
        <h3>Odwoływanie się do kolumn</h3>
        Jak prawidłowo odwołać się do kolumny Kwota w tabeli Sprzedaz w języku DAX?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Sprzedaz.Kwota'>Sprzedaz.Kwota</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='[Kwota]'>[Kwota]</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Sprzedaz[Kwota]'>Sprzedaz[Kwota]</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Kwota'>Kwota</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Suma Sprzedaży = SUM(<div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        W DAX używamy nawiasów kwadratowych, a nie kropki. Format to: NazwaTabeli[NazwaKolumny].
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='2'>
<div class='container'>
    <div class='task-description'>
        <h3>Nazwy z apostrofami</h3>
        Masz tabelę o nazwie Tabela Sprzedaży (ze spacją) i kolumnę Kwota Netto. Jak prawidłowo się do niej odwołać?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Tabela Sprzedaży[Kwota Netto]'>Tabela Sprzedaży[Kwota Netto]</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='´Tabela Sprzedaży´[Kwota Netto]'>´Tabela Sprzedaży´[Kwota Netto]</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='[Kwota Netto]'>[Kwota Netto]</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='[Tabela Sprzedaży][Kwota Netto]'>[Tabela Sprzedaży][Kwota Netto]</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Suma = SUM(<div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Gdy nazwa zawiera spacje, musisz ją ująć w specjalne znaki.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='3'>
<div class='container'>
    <div class='task-description'>
        <h3>Funkcja agregująca SUM</h3>
        Chcesz obliczyć sumę wszystkich wartości w kolumnie Kwota z tabeli Sprzedaz. Która funkcja jest odpowiednia?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='AVERAGE'>AVERAGE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUM'>SUM</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='COUNT'>COUNT</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUMX'>SUMX</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Suma Sprzedaży = <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(Sprzedaz[Kwota])</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Szukasz podstawowej funkcji agregującej, której nazwa w języku angielskim oznacza suma.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='4'>
<div class='container'>
    <div class='task-description'>
        <h3>Funkcja IF</h3>
        Chcesz utworzyć kategorię sprzedaży: jeśli kwota > 1000, to Wysoka, w przeciwnym razie Niska. Jak uzupełnić formułę?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='IF'>IF</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CASE'>CASE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='″Wysoka″'>″Wysoka″</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='″Niska″'>″Niska″</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Kategoria =</div>
        <div><div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(</div>
        <div>    Sprzedaz[Kwota] > 1000,</div>
        <div>    <div class='drop-zone' data-slot='1' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>,</div>
        <div>    <div class='drop-zone' data-slot='2' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        W DAX funkcja warunkowa to po prostu IF z trzema parametrami: warunek, co zwrócić gdy prawda, co zwrócić gdy fałsz.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='5'>
<div class='container'>
    <div class='task-description'>
        <h3>Funkcja SUMX</h3>
        Chcesz obliczyć sumę wartości zamówień (Ilość × Cena) dla każdego wiersza. Którą funkcję powinieneś użyć?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUM'>SUM</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUMX'>SUMX</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CALCULATE'>CALCULATE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='TOTALX'>TOTALX</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Suma Wartości =</div>
        <div><div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(</div>
        <div>    Sprzedaz,</div>
        <div>    Sprzedaz[Ilość] * Sprzedaz[Cena]</div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Potrzebujesz funkcji iteracyjnej (z końcówką X), która sumuje wyniki obliczeń dla każdego wiersza.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='6'>
<div class='container'>
    <div class='task-description'>
        <h3>Operator łączenia tekstów</h3>
        Chcesz połączyć imię i nazwisko klienta ze spacją pomiędzy. Jaki operator użyć?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='+'>+</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='&'>&</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='!'>!</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CONCAT'>CONCAT</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Pełna Nazwa =</div>
        <div>Klienci[Imię] <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div> Klienci[Nazwisko]</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 6;
    const slotsPerPage = [1, 1, 1, 3, 1, 1];
    let slots = new Array(slotsPerPage[0]).fill('');
    const correctSolutions = [['Sprzedaz[Kwota]'], ['Tabela z apostrofem[Kwota Netto]'], ['SUM'], ['IF', 'Wysoka', 'Niska'], ['SUMX'], ['&']];
    const correctFeedback = ['\u2705 Brawo! Rozwi\u0105zanie poprawne!\nW DAX zawsze odwo\u0142ujesz si\u0119 do kolumn poprzez nazw\u0119 tabeli i nazw\u0119 kolumny w nawiasach kwadratowych: Tabela[Kolumna]. To zapobiega niejednoznaczno\u015bci gdy masz kolumny o tych samych nazwach w r\u00f3\u017cnych tabelach.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nGdy nazwa tabeli lub kolumny zawiera spacje, znaki specjalne lub polskie znaki, musisz uj\u0105\u0107 j\u0105 w apostrofy. Poprawna sk\u0142adnia to: nazwa z apostrofem. Nazwa kolumny w tym przypadku nie wymaga apostrof\u00f3w, bo jest ju\u017c w nawiasach kwadratowych.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nFunkcja SUM() sumuje wszystkie warto\u015bci w kolumnie. Pomija warto\u015bci puste (BLANK) i uwzgl\u0119dnia aktualny kontekst filtrowania. To podstawowa funkcja agreguj\u0105ca w DAX.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nFunkcja IF() w DAX ma sk\u0142adni\u0119: `IF(warunek, warto\u015b\u0107_je\u015bli_prawda, warto\u015b\u0107_je\u015bli_fa\u0142sz).` W tym przypadku: `IF(Sprzedaz[Kwota] > 1000, \u2033Wysoka\u2033, \u2033Niska\u2033).`', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nSUMX() to funkcja iteracyjna, kt\u00f3ra dla ka\u017cdego wiersza tabeli oblicza wyra\u017cenie, a potem sumuje wyniki. Sk\u0142adnia: SUMX(tabela, wyra\u017cenie). W tym przypadku dla ka\u017cdego wiersza mno\u017cy Ilo\u015b\u0107 \u00d7 Cena, a nast\u0119pnie sumuje wszystkie wyniki.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nOperator ampersand w DAX s\u0142u\u017cy do \u0142\u0105czenia (konkatenacji) tekst\u00f3w. Poprawna sk\u0142adnia: `Klienci[Imi\u0119] &  Klienci[Nazwisko].` Mo\u017cesz \u0142\u0105czy\u0107 dowoln\u0105 liczb\u0119 element\u00f3w tekstowych u\u017cywaj\u0105c tego operatora.'];
    const incorrectFeedback = [{}, {}, {}, {}, {}, {}];

    function drag(event) {
            event.dataTransfer.setData('function', event.target.getAttribute('data-function'));
        }
    
        function allowDrop(event) {
            event.preventDefault();
            event.target.classList.add('drag-over');
        }
    
        function dragLeave(event) {
            event.target.classList.remove('drag-over');
        }
    
        function drop(event) {
            event.preventDefault();
            event.target.classList.remove('drag-over');
    
            const functionName = event.dataTransfer.getData('function');
            const slotIndex = parseInt(event.target.getAttribute('data-slot'));
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            if (slots[slotIndex]) {
                const chips = activePage.querySelectorAll('.function-chip');
                for (let i = 0; i < chips.length; i++) {
                    if (chips[i].getAttribute('data-function') === slots[slotIndex]) {
                        chips[i].classList.remove('used');
                        break;
                    }
                }
            }
    
            slots[slotIndex] = functionName;
            event.target.textContent = functionName;
            event.target.classList.add('filled');
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                if (chips[i].getAttribute('data-function') === functionName) {
                    chips[i].classList.add('used');
                    break;
                }
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function checkSolution() {
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const feedback = activePage.querySelector('.feedback');
            if (!feedback) return;
    
            if (slots.includes('')) {
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = 'Niekompletne! Musisz wypełnić wszystkie miejsca w kodzie.';
                return;
            }
    
            const currentPageNum = parseInt(activePage.getAttribute('data-page'));
            const pageIndex = currentPageNum - 1;
            const isCorrect = checkCurrentPageSolution(pageIndex);
    
            if (isCorrect) {
                feedback.className = 'feedback show correct';
                feedback.innerHTML = correctFeedback[pageIndex];
            } else {
                const userAnswer = slots.join(',');
                const incorrectMessages = incorrectFeedback[pageIndex];
    
                for (const pattern in incorrectMessages) {
                    if (pattern === userAnswer) {
                        feedback.className = 'feedback show incorrect';
                        feedback.innerHTML = incorrectMessages[pattern];
                        return;
                    }
    
                    if (pattern.includes('*')) {
                        const regexPattern = '^' + pattern.replace(/\*/g, '.*') + '$';
                        const regex = new RegExp(regexPattern);
                        if (regex.test(userAnswer)) {
                            feedback.className = 'feedback show incorrect';
                            feedback.innerHTML = incorrectMessages[pattern];
                            return;
                        }
                    }
                }
    
                const defaultMessage = incorrectMessages['default'];
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = defaultMessage || '❌ <strong>Niepoprawne rozwiązanie.</strong> Spróbuj ponownie!';
            }
        }
    
        function checkCurrentPageSolution(pageIndex) {
            const solution = correctSolutions[pageIndex];
            for (let i = 0; i < solution.length; i++) {
                if (slots[i] !== solution[i]) {
                    return false;
                }
            }
            return true;
        }
    
        function resetTask() {
            slots.fill('');
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const zones = activePage.querySelectorAll('.drop-zone');
            for (let i = 0; i < zones.length; i++) {
                zones[i].textContent = '';
                zones[i].classList.remove('filled');
            }
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                chips[i].classList.remove('used');
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function showPage(pageNumber) {
            const pages = document.querySelectorAll('.page');
            for (let i = 0; i < pages.length; i++) {
                pages[i].classList.remove('active');
            }
    
            for (let i = 0; i < pages.length; i++) {
                if (parseInt(pages[i].getAttribute('data-page')) === pageNumber) {
                    pages[i].classList.add('active');
                    break;
                }
            }
    
            currentPage = pageNumber;
            const pageIndex = currentPage - 1;
            document.getElementById('currentPage').textContent = currentPage;
    
            document.getElementById('prevBtn').disabled = (currentPage === 1);
            document.getElementById('nextBtn').disabled = (currentPage === totalPages);
    
            slots = new Array(slotsPerPage[pageIndex]).fill('');
    
            resetTask();
        }
    
        function nextPage() {
            if (currentPage < totalPages) {
                showPage(currentPage + 1);
            }
        }
    
        function prevPage() {
            if (currentPage > 1) {
                showPage(currentPage - 1);
            }
        }
    
        document.addEventListener('DOMContentLoaded', function() {
            showPage(1);
        });
</script>

</body>
</html>

"
```
            lineageTag: c9571088-8138-4170-b13a-97f4c1623935

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
                background: #e5e5e5;
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
                background: #6b1718;
            }
    
            .check-button:hover:not(:disabled) {
                background: #380c0c;
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
                A) `Kolumna[Tabela]`
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) `[Kolumna]`
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) `Tabela[Kolumna]`
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) `Kolumna.Tabela`
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
                A) `Tabela[Miara]`
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) `[Miara]`
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) `Miara()`
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
            <p><strong>Czym różni się `COUNT` od `COUNTROWS`?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) `COUNT` liczy kolumny, `COUNTROWS` liczy wiersze
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) `COUNT` liczy niepuste wartości w kolumnie, `COUNTROWS` liczy wszystkie wiersze tabeli
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Nie ma różnicy
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) `COUNT` jest szybsze niż `COUNTROWS`
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Co robi funkcja `DISTINCTCOUNT`?</strong></p>
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
        'DAX to skrót od Data Analysis Expressions - język formuł używany w Power BI, Excel Power Pivot i Analysis Services.',
        'W DAX zawsze używamy składni `Tabela[Kolumna`], gdzie nazwa tabeli jest przed nawiasem kwadratowym, a nazwa kolumny wewnątrz.',
        'Do miar można odwoływać się zarówno przez `[Nazwa Miary]` jak i przez `Tabela[Nazwa Miary]`. Pierwsza składnia jest częściej używana i krótsza.',
        '`SUM(Tabela[Kolumna])` sumuje wszystkie wartości w kolumnie, pomijając wartości puste (BLANK) i uwzględniając aktualny kontekst filtrowania.',
        '`COUNT` liczy niepuste wartości numeryczne w konkretnej kolumnie, podczas gdy `COUNTROWS` liczy wszystkie wiersze w tabeli (nawet jeśli mają puste wartości).',
        '`DISTINCTCOUNT` liczy ile jest unikalnych (niepowtarzających się) wartości. Np. dla {1, 2, 2, 3, 3, 3} zwróci 3.'
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
            lineageTag: 810a2b7a-929b-47df-9b4b-1129609d656a

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
        <pre><code>DAX
        Cena Jednostkowa =
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
        <pre><code>DAX
        // ✅ W KOLUMNACH - bezpośrednie odwołania do kolumn
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
        <pre><code>DAX
        Sprzedaż Netto = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto])</code></pre>
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
        <pre><code>DAX
        // ❌ ZŁE - nie zadziała w miarze
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
            lineageTag: c933e729-cdd6-496a-8228-aacba7a02a9c

        measure '02. Miary vs Kolumny kalkulowane - Nazewnictwo' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Nazewnictwo</title>
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

<div class='container' id='viz_3876560f'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_3876560f' onclick='changePage_3876560f(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_3876560f'>1</span> z <span id='totalPages_3876560f'>5</span>
        </span>
        <button id='nextBtn_3876560f' onclick='changePage_3876560f(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Dlaczego konwencje są ważne?</h1>
        <p>W małych modelach danych nazewnictwo może wydawać się nieistotne, ale wraz z rozrostem projektu:</p>
        <ul>
        <li><strong>Trudniej znaleźć</strong> właściwą tabelę lub miarę</li>
        <li><strong>Ciężko rozróżnić</strong> tabele faktów od wymiarów</li>
        <li><strong>Problemy z konserwacją</strong> modelu przez innych użytkowników</li>
        <li><strong>Wolniejsza praca</strong> z modelem</li>
        </ul>
        <p>Dobra konwencja nazewnicza to <strong>fundament profesjonalnego modelu danych</strong>.</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Tabele faktów (Fact Tables)</h1>
        <p><strong>Charakterystyka:</strong></p>
        <ul>
        <li>Zawierają <strong>zdarzenia biznesowe</strong> (transakcje, zamówienia, faktury)</li>
        <li>Mają <strong>wiele wierszy</strong> (setki tysięcy, miliony)</li>
        <li>Zawierają <strong>wartości numeryczne</strong> do agregacji</li>
        <li>Łączą się z tabelami wymiarów przez <strong>klucze obce</strong></li>
        </ul>
        <p><strong>Konwencja nazewnicza:</strong></p>
        <pre><code>Przykłady:
        ✅ Fakt_Sprzedaz
        ✅ fSprzedaz
        ✅ F_Sprzedaz</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Tabele wymiarów (Dimension Tables)</h1>
        <p><strong>Charakterystyka:</strong></p>
        <ul>
        <li>Zawierają <strong>atrybuty opisowe</strong> (nazwy, kategorie, opisy)</li>
        <li>Mają <strong>relatywnie mało wierszy</strong> (dziesiątki, tysiące)</li>
        <li>Służą do <strong>filtrowania i grupowania</strong></li>
        <li>Łączą się z faktami przez <strong>klucz główny</strong></li>
        </ul>
        <p><strong>Konwencja nazewnicza:</strong></p>
        <pre><code>Przykłady:
        ✅ Dim_Produkty
        ✅ D_Produkty
        ✅ dProdukty</code></pre>
        <h1>Tabela kalendarzowa (Date Table)</h1>
        <p><strong>Charakterystyka:</strong></p>
        <ul>
        <li><strong>Jedna data = jeden wiersz</strong></li>
        <li>Zawiera wszystkie daty w zakresie analizy <strong>bez luk</strong></li>
        <li>Zawiera atrybuty czasowe (rok, kwartał, miesiąc, dzień tygodnia)</li>
        <li><strong>Kluczowa</strong> dla funkcji Time Intelligence</li>
        </ul>
        <p><strong>Konwencja nazewnicza:</strong></p>
        <pre><code>Pojedyncza nazwa
        Przykłady:
        ✅ dKalendarz
        ✅ dDaty
        ✅ D_Data
        ✅ DimData</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>Tabele pomocnicze (Helper Tables)</h1>
        <p><strong>Charakterystyka:</strong></p>
        <ul>
        <li>Tabele <strong>bez relacji</strong> z resztą modelu</li>
        <li>Służą do <strong>parametryzacji</strong> miar</li>
        <li>Używane z funkcjami <code>SELECTEDVALUE()</code> lub <code>SWITCH()</code></li>
        </ul>
        <p><strong>Konwencja nazewnicza:</strong></p>
        <pre><code>Prefix: Parametr_ lub P_
        Przykłady:
        ✅ Param_Waluty
        ✅ P_Waluty
        ✅ pWaluty</code></pre>

    </div>

    <!-- Strona 5 -->
    <div class='page'>
        <h1>Tabele z miarami (Measure Tables)</h1>
        <p><strong>Charakterystyka:</strong></p>
        <ul>
        <li><strong>Pusta tabela</strong> (0 wierszy)</li>
        <li>Służy <strong>tylko do organizacji miar</strong></li>
        <li>Łatwiejsza nawigacja w modelu</li>
        </ul>
        <p><strong>Konwencja nazewnicza:</strong></p>
        <pre><code>Prefix: _Miary lub ikona
        Przykłady:
        ✅ _Miary
        ✅ _Measures
        ✅ _Miary_Sprzedaz</code></pre>
        <p><strong>Jak stworzyć:</strong></p>
        <pre><code>_Miary = <span class='dax-function'>BLANK</span>()</code></pre>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '3876560f';
    var containerId = 'viz_' + vizId;

    var currentPage_3876560f = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_3876560f'] = function(n) {
        if (n > totalPages) currentPage_3876560f = totalPages;
        if (n < 1) currentPage_3876560f = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_3876560f - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_3876560f;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_3876560f === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_3876560f === totalPages);
    };

    window['changePage_3876560f'] = function(n) {
        currentPage_3876560f += n;
        window['showPage_3876560f'](currentPage_3876560f);
    };

    // Inicjalizacja
    window['showPage_3876560f'](1);

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
            lineageTag: 20c0dccc-7132-4c5b-ad16-7c10d57f6078

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
        <pre><code>DAX
        // ❌ ZŁE - kolumna kalkulowana (niepotrzebnie zajmuje pamięć)
        Suma Wartości Kolumna = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto])

        // ✅ DOBRE - miara (dynamiczna, nie zajmuje pamięci)
        Suma Wartości Miara = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto])</code></pre>
        <h2>Błąd 2: Próba mnożenia kolumn w miarze</h2>
        <pre><code>DAX
        // ❌ ZŁE - nie zadziała w miarze
        Wartość Brutto = Sprzedaż[Wartość netto] * <span class='dax-number'>1.23</span>

        // ✅ DOBRE - agreguj najpierw
        Wartość Brutto = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto]) * <span class='dax-number'>1.23</span></code></pre>
        <h2>Błąd 3: Zapominanie o agregacji w miarach</h2>
        <pre><code>DAX
        // ❌ ZŁE - w miarze musisz agregować
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
            lineageTag: cd48894d-b84a-4ec7-8c1e-e3ae183a6906

        measure '02. Miary vs Kolumny kalkulowane - Rola modelu' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Rola modelu</title>
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

<div class='container' id='viz_5e9ccb2a'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_5e9ccb2a' onclick='changePage_5e9ccb2a(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_5e9ccb2a'>1</span> z <span id='totalPages_5e9ccb2a'>3</span>
        </span>
        <button id='nextBtn_5e9ccb2a' onclick='changePage_5e9ccb2a(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Czym jest model danych w Power BI?</h1>
        <p><strong>Model danych</strong> to:</p>
        <ul>
        <li><strong>Struktura relacji</strong> między tabelami</li>
        <li><strong>Schemat gwiazdowy</strong> (star schema) lub <strong>schemat płatka śniegu</strong> (snowflake schema)</li>
        <li><strong>Logiczna warstwa</strong> między danymi źródłowymi a wizualizacjami</li>
        <li><strong>Fundament</strong> dla szybkich i poprawnych obliczeń DAX</li>
        </ul>
        <h1>Schemat gwiazdowy (Star Schema)</h1>
        <h2>Charakterystyka</h2>
        <p><strong>Centrum:</strong> Tabela faktów (Fakt_Sprzedaz)  </p>
        <p><strong>Ramiona:</strong> Tabele wymiarów (Produkty, Klienci, Kalendarz)</p>
        <pre><code>    Kalendarz
                ↓
        Produkty → Fakt_Sprzedaz ← Klienci
                ↓
            Regiony</code></pre>
        <h2>Zalety schematu gwiazdowego:</h2>
        <p>✅ <strong>Prosty i czytelny</strong>  </p>
        <p>✅ <strong>Szybkie zapytania</strong> (mniej złączeń)  </p>
        <p>✅ <strong>Łatwa rozbudowa</strong>  </p>
        <p>✅ <strong>Intuicyjny dla użytkowników</strong>  </p>
        <p>✅ <strong>Optymalny dla Power BI</strong></p>
        <h2>Zasady:</h2>
        <ul>
        <li>Tabele wymiarów <strong>nie łączą się</strong> między sobą</li>
        <li>Wszystkie wymiary łączą się <strong>bezpośrednio z faktami</strong></li>
        <li><strong>Jeden fakt = jeden wiersz transakcji</strong></li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Schemat płatka śniegu (Snowflake Schema)</h1>
        <h2>Charakterystyka</h2>
        <p>Tabele wymiarów są <strong>znormalizowane</strong> (podzielone na pod-tabele)</p>
        <pre><code>                    Kalendarz
                                ↓
        Producent → Kategoria → Produkty → Fakt_Sprzedaz ← Klienci → Miasta → Regiony</code></pre>
        <h2>Wady w Power BI:</h2>
        <p>❌ <strong>Wolniejsze zapytania</strong> (więcej złączeń)  </p>
        <p>❌ <strong>Bardziej skomplikowany</strong>  </p>
        <p>❌ <strong>Cięższy w utrzymaniu</strong>  </p>
        <p>❌ <strong>Mniej intuicyjny</strong></p>
        <h2>Kiedy używać:</h2>
        <ul>
        <li>Gdy <strong>musisz</strong> zaoszczędzić pamięć (rzadkie w Power BI)</li>
        <li>Gdy dane przychodzą z systemu źródłowego w tej strukturze</li>
        <li><strong>Zalecenie:</strong> Zazwyczaj lepiej <strong>spłaszczyć</strong> do gwiazdy w Power Query</li>
        </ul>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Najlepsze praktyki modelowania</h1>
        <h2>1. Jeden kierunek filtrowania</h2>
        <pre><code>✅ DOBRE:
        Produkty (<span class='dax-number'>1</span>) → (∞) Fakt_Sprzedaz
        Filtr płynie: Produkty → Fakty

        ❌ ZŁE:
        Produkty (<span class='dax-number'>1</span>) ↔ (∞) Fakt_Sprzedaz
        Dwukierunkowy filtr (unikaj!)</code></pre>
        <h2>2. Tabela kalendarzowa</h2>
        <pre><code>Kalendarz = 
        <span class='dax-function'>ADDCOLUMNS</span>(
            <span class='dax-function'>CALENDAR</span>(<span class='dax-function'>DATE</span>(<span class='dax-number'>2020</span>,<span class='dax-number'>1</span>,<span class='dax-number'>1</span>), <span class='dax-function'>DATE</span>(<span class='dax-number'>2025</span>,<span class='dax-number'>12</span>,<span class='dax-number'>31</span>)),
            'Rok', <span class='dax-function'>YEAR</span>([Date]),
            'Miesiac', <span class='dax-function'>FORMAT</span>([Date], 'YYYY-MM'),
            'Kwartal', 'Q' & <span class='dax-function'>QUARTER</span>([Date]),
            'Dzien Tygodnia', <span class='dax-function'>FORMAT</span>([Date], 'dddd', 'pl-PL')
        )</code></pre>
        <p><strong>Relacja:</strong></p>
        <pre><code>Kalendarz[Data] (<span class='dax-number'>1</span>) → (∞) Fakt_Sprzedaz[Data]</code></pre>
        <p><strong>Oznacz jako tabelę dat:</strong></p>
        <ul>
        <li>Prawy przycisk na <code>Kalendarz</code> → <strong>Oznacz jako tabelę dat</strong></li>
        <li>Wybierz kolumnę <code>Data</code></li>
        </ul>
        <h2>3. Unikaj kolumn kalkulowanych w faktach</h2>
        <pre><code>❌ ZŁE (zajmuje pamięć):
        Marza PLN = Fakt_Sprzedaz[Wartosc] - Fakt_Sprzedaz[Koszt]
        (milion wierszy × wartość = dużo pamięci)

        ✅ <span class='dax-function'>DOBRE</span> (obliczane dynamicznie):
        Marza PLN = <span class='dax-function'>SUM</span>(Fakt_Sprzedaz[Wartosc]) - <span class='dax-function'>SUM</span>(Fakt_Sprzedaz[Koszt])
        (miara, <span class='dax-number'>0</span> bajtów pamięci)</code></pre>
        <h2>4. Zachowaj klucze numeryczne</h2>
        <pre><code>✅ DOBRE:
        ID_Produktu: <span class='dax-number'>1</span>, <span class='dax-number'>2</span>, <span class='dax-number'>3</span>, <span class='dax-number'>4</span>
        Typ danych: Liczba całkowita

        ❌ ZŁE:
        ID_Produktu: 'PROD001', 'PROD002'
        Typ danych: Tekst (wolniejsze złączenia)</code></pre>
        <h2>5. Usuń zbędne kolumny</h2>
        <p><strong>W Power Query przed załadowaniem:</strong></p>
        <ul>
        <li>Usuń kolumny, które <strong>nie są używane</strong></li>
        <li>Usuń duplikaty kluczy w wymiarach</li>
        <li>Usuń kolumny z danymi wrażliwymi</li>
        </ul>
        <h2>6. Role-playing dimensions</h2>
        <p><strong>Problem:</strong> Jedna tabela Kalendarz, wiele dat w faktach</p>
        <pre><code>Fakt_Zamowienia:
        - Data_Zamowienia
        - Data_Wysylki
        - Data_Platnosci</code></pre>
        <p><strong>Rozwiązanie:</strong> Nieaktywne relacje + USERELATIONSHIP</p>
        <pre><code>Sprzedaz wg Daty Wysylki = 
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaz Netto],
            <span class='dax-function'>USERELATIONSHIP</span>(Fakt_Zamowienia[Data_Wysylki], Kalendarz[Data])
        )</code></pre>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '5e9ccb2a';
    var containerId = 'viz_' + vizId;

    var currentPage_5e9ccb2a = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_5e9ccb2a'] = function(n) {
        if (n > totalPages) currentPage_5e9ccb2a = totalPages;
        if (n < 1) currentPage_5e9ccb2a = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_5e9ccb2a - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_5e9ccb2a;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_5e9ccb2a === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_5e9ccb2a === totalPages);
    };

    window['changePage_5e9ccb2a'] = function(n) {
        currentPage_5e9ccb2a += n;
        window['showPage_5e9ccb2a'](currentPage_5e9ccb2a);
    };

    // Inicjalizacja
    window['showPage_5e9ccb2a'](1);

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
            lineageTag: db299c87-535e-40fd-a6bf-53c0baff7115

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
        <pre><code>DAX
        // Pracujesz na JEDNYM wierszu naraz
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
        <pre><code>DAX
        // ❌ To nie zadziała:
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
        <ul>
        <li>Więcej w dziale o <strong>Iteratorach</strong></li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Praktyczny przykład różnicy</h1>
        <h2>Scenariusz: Obliczenie marży</h2>
        <p><strong>Tabela Sprzedaż:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Kategoria</th>
              <th>Wartość netto</th>
              <th>Koszt</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>NAPOJE</td>
              <td>1000</td>
              <td>600</td>
            </tr>
            <tr>
              <td>WINA</td>
              <td>2000</td>
              <td>1400</td>
            </tr>
            <tr>
              <td>PRZEKĄSKI</td>
              <td>500</td>
              <td>350</td>
            </tr>
          </tbody>
        </table>
        <h2>Jako kolumna kalkulowana:</h2>
        <pre><code>DAX
        Marża PLN = Sprzedaż[Wartość netto] - Sprzedaż[Koszt]</code></pre>
        <p><strong>Wynik w tabeli:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Kategoria</th>
              <th>Wartość netto</th>
              <th>Koszt</th>
              <th>Marża PLN</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>NAPOJE</td>
              <td>1000</td>
              <td>600</td>
              <td><strong>400</strong></td>
            </tr>
            <tr>
              <td>WINA</td>
              <td>2000</td>
              <td>1400</td>
              <td><strong>600</strong></td>
            </tr>
            <tr>
              <td>PRZEKĄSKI</td>
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
        <pre><code>DAX
        Marża PLN = <span class='dax-function'>SUM</span>(Sprzedaż[Wartość netto]) - <span class='dax-function'>SUM</span>(Sprzedaż[Koszt])</code></pre>
        <p><strong>Wynik na wizualizacji:</strong></p>
        <ul>
        <li>Bez filtrów: <strong>1150</strong> (suma wszystkich marż)</li>
        <li>Dla napojów: <strong>400</strong></li>
        <li>Dla win: <strong>600</strong></li>
        <li>Według produktu: suma marż w każdej kategorii</li>
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
            lineageTag: 11754834-f589-43bd-aa96-153276a78a74

        measure '02. Miary vs Kolumny kalkulowane - Tipy' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Tipy</title>
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

<div class='container' id='viz_e4198c50'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_e4198c50' onclick='changePage_e4198c50(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_e4198c50'>1</span> z <span id='totalPages_e4198c50'>3</span>
        </span>
        <button id='nextBtn_e4198c50' onclick='changePage_e4198c50(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Wydajność modelu</h1>
        <h2>Optymalizacja pamięci</h2>
        <p><strong>1. Zmień typy danych:</strong></p>
        <pre><code>❌ Tekst: '<span class='dax-number'>123</span>' (<span class='dax-number'>8</span> bajtów)
        ✅ Liczba całkowita: <span class='dax-number'>123</span> (<span class='dax-number'>2</span>-<span class='dax-number'>4</span> bajty)</code></pre>
        <p><strong>2. Usuń zbędne kolumny:</strong></p>
        <ul>
        <li>W Power Query: Usuń kolumny przed Load</li>
        <li>Mniejszy model = szybsze odświeżanie</li>
        </ul>
        <p><strong>3. Używaj kolumn całkowitych zamiast dziesiętnych:</strong></p>
        <pre><code>❌ Decimal: <span class='dax-number'>123.45</span> (<span class='dax-number'>8</span> bajtów)
        ✅ Integer: <span class='dax-number'>123</span> (<span class='dax-number'>2</span>-<span class='dax-number'>4</span> bajty)</code></pre>
        <p><strong>4. Kompresja kolumn tekstowych:</strong></p>
        <ul>
        <li>Power BI automatycznie kompresuje powtarzające się wartości</li>
        <li>Kolumny z małą kardynalnością (mało unikalnych wartości) zajmują mniej pamięci</li>
        </ul>
        <h2>Optymalizacja wydajności zapytań</h2>
        <p><strong>1. Minimalizuj liczbę relacji:</strong></p>
        <pre><code>✅ Star Schema: <span class='dax-number'>1</span> złączenie (Wymiar → Fakt)
        ❌ Snowflake: <span class='dax-number'>2</span>-<span class='dax-number'>3</span> złączenia (Wymiar → Pod-wymiar → Fakt)</code></pre>
        <p><strong>2. Używaj miar zamiast kolumn kalkulowanych:</strong></p>
        <pre><code>❌ Kolumna: <span class='dax-number'>1</span> <span class='dax-number'>000</span> <span class='dax-number'>000</span> wierszy × <span class='dax-number'>8</span> bajtów = <span class='dax-number'>8</span> MB
        ✅ Miara: <span class='dax-number'>0</span> bajtów (obliczana na żądanie)</code></pre>
        <p><strong>3. Agreguj dane w Power Query gdy możliwe:</strong></p>
        <pre><code>Jeśli potrzebujesz tylko sum miesięcznych,
        zagreguj dane już w Power Query
        zamiast trzymać codzienne szczegóły</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Checklist profesjonalnego modelu</h1>
        <h2>Struktura:</h2>
        <ul>
        <li>[ ] Schemat gwiazdowy (star schema)</li>
        <li>[ ] Jedna tabela kalendarzowa oznaczona jako tabela dat</li>
        <li>[ ] Wszystkie relacje typu 1:∞ (jeden do wielu)</li>
        <li>[ ] Jednokierunkowe filtrowanie (wymiar → fakt)</li>
        <li>[ ] Klucze numeryczne zamiast tekstowych</li>
        <li>[ ] Brak duplikatów kluczy w wymiarach</li>
        </ul>
        <h2>Nazewnictwo:</h2>
        <ul>
        <li>[ ] Konsekwentne nazwy tabel (Fakt_, Dim_, Kalendarz)</li>
        <li>[ ] Konsekwentne nazwy kluczy (ID_Produktu)</li>
        <li>[ ] Opisowe nazwy miar (Sprzedaz Netto, Sprzedaz YTD)</li>
        <li>[ ] Tabela _Miary dla organizacji miar</li>
        <li>[ ] Miary pomocnicze z prefiksem <code>_</code></li>
        </ul>
        <h2>Wydajność:</h2>
        <ul>
        <li>[ ] Optymalne typy danych (Integer zamiast Decimal)</li>
        <li>[ ] Usunięte zbędne kolumny</li>
        <li>[ ] Miary zamiast kolumn kalkulowanych dla agregacji</li>
        <li>[ ] Brak niepotrzebnych relacji dwukierunkowych</li>
        </ul>
        <h2>Dokumentacja:</h2>
        <ul>
        <li>[ ] Opisy tabel (Właściwości → Opis)</li>
        <li>[ ] Opisy miar w komentarzach DAX</li>
        <li>[ ] Nazwy miar zgodne z konwencją biznesową</li>
        </ul>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Podsumowanie</h1>
        <p>✅ <strong>Model danych</strong> = fundament każdego raportu Power BI  </p>
        <p>✅ <strong>Schemat gwiazdowy</strong> = preferowany w Power BI  </p>
        <p>✅ <strong>Konwencje nazewnicze</strong> = łatwiejsza praca w zespole  </p>
        <p>✅ <strong>Optymalizacja</strong> = szybsze odświeżanie i zapytania  </p>
        <p>✅ <strong>Dokumentacja</strong> = łatwiejsze utrzymanie</p>
        <p>💡 <strong>Pamiętaj:</strong> Dobry model danych to 80% sukcesu w Power BI. Reszta to tylko DAX i wizualizacje!</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'e4198c50';
    var containerId = 'viz_' + vizId;

    var currentPage_e4198c50 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_e4198c50'] = function(n) {
        if (n > totalPages) currentPage_e4198c50 = totalPages;
        if (n < 1) currentPage_e4198c50 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_e4198c50 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_e4198c50;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_e4198c50 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_e4198c50 === totalPages);
    };

    window['changePage_e4198c50'] = function(n) {
        currentPage_e4198c50 += n;
        window['showPage_e4198c50'](currentPage_e4198c50);
    };

    // Inicjalizacja
    window['showPage_e4198c50'](1);

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
            lineageTag: a47f3119-56d0-420e-87d6-751930c59182

        measure '02a. Gaps' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DAX Gaps</title>
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #333;
        background: transparent;
        padding: 20px;
    }
    
    .container {
        max-width: 900px;
        margin: 0 auto;
        background: transparent;
        padding: 40px;
    }
    
    h3 {
        font-size: 26px;
        line-height: 36px;
        font-weight: 600;
        padding-top: 14px;
        padding-bottom: 6px;
        margin-bottom: 1em;
        color: #6b1718;
        border-bottom: 2px solid #6b1718;
    }
    
    .task-description {
        font-size: 1.1em;
        margin: 20px 0;
    }
    
    .code-container {
        background: #f8f9fa;
        border: 2px solid #e1e4e8;
        border-radius: 6px;
        padding: 25px;
        margin: 30px 0;
        font-family: 'Courier New', monospace;
        font-size: 1.05em;
        line-height: 1.8;
    }
    
    .drop-zone {
        display: inline-block;
        min-width: 180px;
        height: 36px;
        background: white;
        border: 2px dashed #6b1718;
        border-radius: 4px;
        padding: 6px 12px;
        margin: 0 4px;
        vertical-align: middle;
        text-align: center;
        transition: all 0.2s;
    }
    
    .drop-zone.drag-over {
        background: #ffe6e6;
        border-color: #380c0c;
    }
    
    .drop-zone.filled {
        background: #d4edda;
        border: 2px solid #28a745;
        border-style: solid;
    }
    
    .functions-title {
        font-size: 1em;
        margin: 30px 0 15px 0;
        color: #333;
    }
    
    .function-chip {
        display: inline-block;
        background: #6b1718;
        color: white;
        padding: 10px 20px;
        margin: 8px;
        border-radius: 20px;
        cursor: grab;
        font-family: 'Courier New', monospace;
        font-size: 1em;
        font-weight: 500;
        transition: all 0.2s;
        user-select: none;
    }
    
    .function-chip:hover {
        background: #380c0c;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(107, 23, 24, 0.3);
    }
    
    .function-chip:active {
        cursor: grabbing;
    }
    
    .function-chip.used {
        opacity: 0.3;
        cursor: not-allowed;
        pointer-events: none;
    }
    
    .button-group {
        margin-top: 30px;
        display: flex;
        gap: 15px;
        align-items: center;
    }
    
    button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 14px 32px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.05em;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    button:hover {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    button.reset-btn {
        background: #6b1718;
        padding: 8px 16px;
        font-size: 0.9em;
    }
    
    button.reset-btn:hover {
        background: #380c0c;
    }
    
    .feedback {
        margin-top: 25px;
        padding: 20px;
        border-radius: 6px;
        display: none;
        font-size: 1.05em;
    }
    
    .feedback.show {
        display: block;
        animation: slideDown 0.3s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .feedback.correct {
        background: #d4edda;
        border-left: 4px solid #28a745;
        color: #155724;
    }
    
    .feedback.incorrect {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        color: #721c24;
    }
    
    .hint-box {
        background: #fafafa;
        border-left: 4px solid #ccc;
        padding: 15px;
        margin: 20px 0;
        border-radius: 4px;
        color: #121212;
        font-size: 0.95em;
    }
    .pagination {
        display: flex;
        align-items: center;
        justify-content: space-between; 
        gap: 20px;
        margin: 30px auto; 
        padding: 20px;
        border-radius: 6px;
    	max-width: 900px;
        border-bottom: 1px solid #e0e0e0;
        width: 100%;
    }
    
    .page-info {
        font-weight: 600;
        color: #666666; 
    }
    
    .nav-button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1em;
        transition: all 0.2s;
    }
    
    .nav-button:hover:not(:disabled) {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .page {
        display: none;
    }
    
    .page.active {
        display: block;
    }
    </style>
</head>
<body>

<div class='pagination'>
    <button class='nav-button' id='prevBtn' onclick='prevPage()'>← Poprzednie</button>
    <span class='page-info'>Zadanie <span id='currentPage'>1</span> z <span id='totalPages'>6</span></span>
    <button class='nav-button' id='nextBtn' onclick='nextPage()'>Następne →</button>
</div>

<div class='page active' data-page='1'>
<div class='container'>
    <div class='task-description'>
        <h3>Kolumna kalkulowana - kontekst</h3>
        Tworzysz kolumnę kalkulowaną, która ma obliczyć marżę jako różnicę ceny i kosztu. Jak napisać formułę?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUM(Sprzedaż[Cena]) - SUM(Sprzedaż[Koszt])'>SUM(Sprzedaż[Cena]) - SUM(Sprzedaż[Koszt])</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Sprzedaż[Cena] - Sprzedaż[Koszt]'>Sprzedaż[Cena] - Sprzedaż[Koszt]</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CALCULATE(Sprzedaż[Cena] - Sprzedaż[Koszt])'>CALCULATE(Sprzedaż[Cena] - Sprzedaż[Koszt])</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUMX(Sprzedaż, Sprzedaż[Cena] - Sprzedaż[Koszt])'>SUMX(Sprzedaż, Sprzedaż[Cena] - Sprzedaż[Koszt])</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Marża PLN = <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        W kolumnach kalkulowanych myślisz wierszami - możesz traktować kolumny jak zmienne i bezpośrednio je dodawać, odejmować, mnożyć.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='2'>
<div class='container'>
    <div class='task-description'>
        <h3>Miara - funkcje agregujące</h3>
        Chcesz utworzyć miarę obliczającą marżę (przychód minus koszt). Jak to zrobić?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Sprzedaż[Wartość netto] - Sprzedaż[Koszt]'>Sprzedaż[Wartość netto] - Sprzedaż[Koszt]</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUM(Sprzedaż[Wartość netto]) - SUM(Sprzedaż[Koszt])'>SUM(Sprzedaż[Wartość netto]) - SUM(Sprzedaż[Koszt])</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUMX(Sprzedaż, [Wartość netto] - [Koszt])'>SUMX(Sprzedaż, [Wartość netto] - [Koszt])</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='AVERAGE(Sprzedaż[Wartość netto] - Sprzedaż[Koszt])'>AVERAGE(Sprzedaż[Wartość netto] - Sprzedaż[Koszt])</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Marża PLN = <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        W miarach myślisz agregacją - musisz najpierw zsumować każdą kolumnę osobno, a dopiero potem odjąć te sumy od siebie.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='3'>
<div class='container'>
    <div class='task-description'>
        <h3>Kiedy kolumna, a kiedy miara?</h3>
        Chcesz utworzyć obliczenie Kategoria wiekowa klienta na podstawie daty urodzenia. Co powinieneś użyć?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Kolumnę kalkulowaną'>Kolumnę kalkulowaną</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Miarę'>Miarę</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Tabelę kalkulowaną'>Tabelę kalkulowaną</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ParametrWhat-If'>ParametrWhat-If</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>-- Chcę móc filtrować klientów według kategorii wiekowej w slicerze</div>
        <div>-- Wartość ma być stała dla każdego klienta</div>
        <div></div>
        <div>Rozwiązanie: <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Potrzebujesz wartości, którą można użyć do filtrowania i grupowania. Zastanów się: miary mogą być używane w slicerach?
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='4'>
<div class='container'>
    <div class='task-description'>
        <h3>Przechowywanie w pamięci</h3>
        Które obliczenie NIE jest przechowywane w modelu i nie zajmuje miejsca w pamięci?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Kolumna kalkulowana'>Kolumna kalkulowana</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Miara'>Miara</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Kolumna z Power Query'>Kolumna z Power Query</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Tabela kalkulowana'>Tabela kalkulowana</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>-- To obliczenie jest wykonywane na żądanie podczas wyświetlania:</div>
        <div>Odpowiedź: <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Szukasz typu obliczeń, który reaguje dynamicznie na filtry i działa na żądanie podczas wyświetlania raportu.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='5'>
<div class='container'>
    <div class='task-description'>
        <h3>Błąd - mnożenie kolumn w miarze</h3>
        Próbujesz utworzyć miarę obliczającą wartość zamówień. Co jest nie tak z tym kodem?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Brak funkcji agregującej'>Brak funkcji agregującej</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Złe nazwy kolumn'>Złe nazwy kolumn</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Brak operatora mnożenia'>Brak operatora mnożenia</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Użyto CALCULATE zamiast SUMX'>Użyto CALCULATE zamiast SUMX</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Wartość Zamówień = Sprzedaż[Ilość] * Sprzedaż[Cena]</div>
        <div></div>
        <div>Problem: <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Zastanów się: w miarach możesz bezpośrednio wykonywać operacje na kolumnach jak w Excelu? Czego brakuje w porównaniu do składni kolumn kalkulowanych?
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='6'>
<div class='container'>
    <div class='task-description'>
        <h3>Złota zasada</h3>
        Która zasada pomaga zdecydować, czy użyć kolumny czy miary?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Jeśli używasz SUM/AVERAGE/COUNT → prawdopodobnie miara'>Jeśli używasz SUM/AVERAGE/COUNT → prawdopodobnie miara</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Zawsze używaj miar dla oszczędności pamięci'>Zawsze używaj miar dla oszczędności pamięci</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Zawsze używaj kolumn dla szybkości obliczeń'>Zawsze używaj kolumn dla szybkości obliczeń</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Jeśli dane się zmieniają → użyj miary'>Jeśli dane się zmieniają → użyj miary</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>-- Zasada decyzyjna:</div>
        <div><div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Kluczem jest obecność funkcji agregujących w formule. Zastanów się, czy w wyrażeniu pojawia się SUM(), AVERAGE(), COUNT() lub podobne.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 6;
    const slotsPerPage = [1, 1, 1, 1, 1, 1];
    let slots = new Array(slotsPerPage[0]).fill('');
    const correctSolutions = [['Sprzeda\u017c[Cena] - Sprzeda\u017c[Koszt]'], ['SUM(Sprzeda\u017c[Warto\u015b\u0107 netto]) - SUM(Sprzeda\u017c[Koszt])'], ['Kolumn\u0119 kalkulowan\u0105'], ['Miara'], ['Brak funkcji agreguj\u0105cej'], ['Je\u015bli u\u017cywasz SUM/AVERAGE/COUNT \u2192 prawdopodobnie miara']];
    const correctFeedback = ['\u2705 Brawo! Rozwi\u0105zanie poprawne!\nW kolumnach kalkulowanych mo\u017cesz bezpo\u015brednio odwo\u0142ywa\u0107 si\u0119 do kolumn i wykonywa\u0107 operacje matematyczne jak w Excelu: `Sprzeda\u017c[Cena] - Sprzeda\u017c[Koszt]`. Kolumny dzia\u0142aj\u0105 w kontek\u015bcie wiersza - formu\u0142a oblicza si\u0119 dla ka\u017cdego wiersza osobno. Nie potrzebujesz funkcji agreguj\u0105cych.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nW miarach MUSISZ najpierw zagregowa\u0107 kolumny funkcjami jak `SUM()`, `AVERAGE()`, `COUNT()`, a dopiero potem wykonywa\u0107 operacje matematyczne. Poprawnie: `SUM(Sprzeda\u017c[Warto\u015b\u0107 netto]) - SUM(Sprzeda\u017c[Koszt])`. Miary dzia\u0142aj\u0105 w kontek\u015bcie filtr\u00f3w, a nie kontek\u015bcie wiersza.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nKategoria wiekowa to warto\u015b\u0107, kt\u00f3r\u0105 chcesz u\u017cywa\u0107 do filtrowania i grupowania - idealne zastosowanie dla kolumny kalkulowanej. Kolumna zostanie obliczona dla ka\u017cdego klienta osobno podczas od\u015bwie\u017cania danych i b\u0119dzie dost\u0119pna w slicerach. Warto\u015b\u0107 zale\u017cy tylko od danych w wierszu (data urodzenia), wi\u0119c kolumna jest w\u0142a\u015bciwym wyborem.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nMiary NIE s\u0105 przechowywane w modelu - s\u0105 obliczane dynamicznie w momencie wy\u015bwietlania wizualizacji. To oszcz\u0119dza pami\u0119\u0107 i pozwala na elastyczne reagowanie na filtry. Kolumny kalkulowane, kolumny z Power Query i tabele kalkulowane s\u0105 wszystkie przechowywane w modelu i zajmuj\u0105 miejsce.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nW miarach NIE MO\u017bESZ bezpo\u015brednio mno\u017cy\u0107 kolumn - brakuje funkcji agreguj\u0105cej. To cz\u0119sty b\u0142\u0105d pocz\u0105tkuj\u0105cych. Poprawne rozwi\u0105zania to:\n- `SUMX(Sprzeda\u017c, Sprzeda\u017c[Ilo\u015b\u0107] * Sprzeda\u017c[Cena])` - oblicz dla ka\u017cdego wiersza, potem zsumuj\n- Lub stw\u00f3rz kolumn\u0119 kalkulowan\u0105 z tym mno\u017ceniem i u\u017cyj `SUM()` na tej kolumnie', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nZ\u0142ota zasada: **Je\u015bli w formule u\u017cywasz funkcji agreguj\u0105cej (`SUM`, `AVERAGE`, `COUNT`, itp.), prawie zawsze powiniene\u015b tworzy\u0107 MIAR\u0118, nie kolumn\u0119.** Je\u015bli mo\u017cesz napisa\u0107 formu\u0142\u0119 bez agregacji, tylko prostym odwo\u0142aniem do kolumn (jak w Excelu), prawdopodobnie potrzebujesz KOLUMNY.'];
    const incorrectFeedback = [{'SUM(Sprzeda\u017c[Cena]) - SUM(Sprzeda\u017c[Koszt])': '\u274c **Niepoprawne!**\nFunkcje agreguj\u0105ce jak `SUM()` s\u0105 dla miar, nie dla kolumn kalkulowanych. W kolumnie masz kontekst wiersza - pracujesz na pojedynczym wierszu, wi\u0119c bezpo\u015brednio odwo\u0142ujesz si\u0119 do kolumn bez agregacji.', 'CALCULATE': '\u274c **Niepoprawne!**\n`CALCULATE()` s\u0142u\u017cy do modyfikowania kontekstu filtr\u00f3w w miarach. W kolumnach kalkulowanych nie potrzebujesz tej funkcji - po prostu odwo\u0142ujesz si\u0119 bezpo\u015brednio do kolumn.', 'SUMX': '\u274c **Niepoprawne!**\n`SUMX()` to funkcja iteracyjna u\u017cywana g\u0142\u00f3wnie w miarach. W kolumnie kalkulowanej ju\u017c jeste\u015b w kontek\u015bcie wiersza, wi\u0119c nie musisz iterowa\u0107 - po prostu odwo\u0142aj si\u0119 do kolumn bezpo\u015brednio.'}, {'Sprzeda\u017c[Warto\u015b\u0107 netto] - Sprzeda\u017c[Koszt]': '\u274c **Niepoprawne!**\nTo sk\u0142adnia dla kolumn kalkulowanych, nie dla miar. W miarach NIE MO\u017bESZ bezpo\u015brednio odejmowa\u0107 kolumn - musisz najpierw je zagregowa\u0107: `SUM(Sprzeda\u017c[Warto\u015b\u0107 netto]) - SUM(Sprzeda\u017c[Koszt])`.', 'SUMX': '\u274c **Niepoprawne!**\nCho\u0107 `SUMX()` mo\u017ce dzia\u0142a\u0107, to w tym przypadku jest zb\u0119dna komplikacja. Wystarczy prosta agregacja: `SUM(kolumna1) - SUM(kolumna2)`. `SUMX()` jest potrzebna gdy obliczenia trzeba wykona\u0107 wiersz po wierszu przed sumowaniem.', 'AVERAGE': '\u274c **Niepoprawne!**\n`AVERAGE()` oblicza \u015bredni\u0105, a nie sum\u0119. Do obliczenia mar\u017cy (r\u00f3\u017cnicy sum) u\u017cywamy `SUM()`.'}, {'Miar\u0119': '\u274c **Niepoprawne!**\nMiar NIE MO\u017bNA u\u017cywa\u0107 w slicerach ani do filtrowania wierszy. Miary s\u0105 dynamiczne i zale\u017c\u0105 od kontekstu filtr\u00f3w, a Ty potrzebujesz sta\u0142ej warto\u015bci dla ka\u017cdego klienta do filtrowania. To zadanie dla kolumny kalkulowanej.', 'Tabel\u0119 kalkulowan\u0105': '\u274c **Niepoprawne!**\nTabela kalkulowana tworzy ca\u0142\u0105 now\u0105 tabel\u0119. Ty potrzebujesz tylko nowej kolumny w istniej\u0105cej tabeli klient\u00f3w. Kolumna kalkulowana to prostsze i w\u0142a\u015bciwe rozwi\u0105zanie.', 'Parametr What-If': '\u274c **Niepoprawne!**\nParametry What-If s\u0142u\u017c\u0105 do tworzenia interaktywnych scenariuszy analitycznych (np. symulacji), nie do kategoryzacji danych wed\u0142ug cech sta\u0142ych jak wiek klienta.'}, {'Kolumna kalkulowana': '\u274c **Niepoprawne!**\nKolumny kalkulowane s\u0105 obliczane podczas od\u015bwie\u017cania danych i PRZECHOWYWANE w modelu. Zajmuj\u0105 miejsce w pami\u0119ci. To miara jest obliczana na \u017c\u0105danie i nie zajmuje miejsca.', 'Kolumna z Power Query': '\u274c **Niepoprawne!**\nKolumny utworzone w Power Query (czy to \u017ar\u00f3d\u0142owe, czy przekszta\u0142cone) s\u0105 \u0142adowane do modelu i PRZECHOWYWANE w pami\u0119ci. Tylko miary s\u0105 obliczane dynamicznie bez przechowywania.', 'Tabela kalkulowana': '\u274c **Niepoprawne!**\nTabele kalkulowane s\u0105 generowane podczas od\u015bwie\u017cania i PRZECHOWYWANE w modelu razem ze wszystkimi swoimi danymi. Zajmuj\u0105 miejsce w pami\u0119ci.'}, {'Z\u0142e nazwy kolumn': '\u274c **Niepoprawne!**\nNazwy kolumn s\u0105 poprawnie zapisane (`Tabela[Kolumna]`). Problem nie le\u017cy w sk\u0142adni nazw, ale w braku agregacji wymaganej w miarach.', 'Brak operatora mno\u017cenia': '\u274c **Niepoprawne!**\nOperator mno\u017cenia `*` jest obecny w kodzie. Problem le\u017cy gdzie indziej - w braku funkcji agreguj\u0105cej, kt\u00f3ra jest wymagana w miarach.', 'U\u017cyto CALCULATE zamiast SUMX': '\u274c **Niepoprawne!**\nW tym kodzie nie u\u017cyto ani CALCULATE, ani SUMX. Problem jest bardziej fundamentalny - brak jakiejkolwiek funkcji agreguj\u0105cej. W miarach nie mo\u017cna bezpo\u015brednio mno\u017cy\u0107 kolumn.'}, {'Zawsze u\u017cywaj miar dla oszcz\u0119dno\u015bci pami\u0119ci': '\u274c **Niepoprawne!**\nCho\u0107 miary oszcz\u0119dzaj\u0105 pami\u0119\u0107, nie zawsze s\u0105 w\u0142a\u015bciwym wyborem. Nie mo\u017cesz u\u017cywa\u0107 miar do filtrowania czy grupowania. Z\u0142ota zasada to: je\u015bli u\u017cywasz funkcji agreguj\u0105cych \u2192 miara, je\u015bli nie \u2192 kolumna.', 'Zawsze u\u017cywaj kolumn dla szybko\u015bci': '\u274c **Niepoprawne!**\nTo nie jest z\u0142ota zasada. Kolumny s\u0105 obliczane raz podczas od\u015bwie\u017cania, ale zajmuj\u0105 pami\u0119\u0107. Decyzja zale\u017cy od tego, czy potrzebujesz agregacji i jak chcesz u\u017cywa\u0107 oblicze\u0144 (filtrowanie vs warto\u015bci na wykresach).', 'Je\u015bli dane si\u0119 zmieniaj\u0105': '\u274c **Niepoprawne!**\nZmiany danych nie s\u0105 kryterium wyboru mi\u0119dzy kolumn\u0105 a miar\u0105. Oba typy oblicze\u0144 od\u015bwie\u017caj\u0105 si\u0119 wraz z danymi. Kluczowa r\u00f3\u017cnica to: czy u\u017cywasz agregacji i czy potrzebujesz filtrowa\u0107 wed\u0142ug tej warto\u015bci.'}];

    function drag(event) {
            event.dataTransfer.setData('function', event.target.getAttribute('data-function'));
        }
    
        function allowDrop(event) {
            event.preventDefault();
            event.target.classList.add('drag-over');
        }
    
        function dragLeave(event) {
            event.target.classList.remove('drag-over');
        }
    
        function drop(event) {
            event.preventDefault();
            event.target.classList.remove('drag-over');
    
            const functionName = event.dataTransfer.getData('function');
            const slotIndex = parseInt(event.target.getAttribute('data-slot'));
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            if (slots[slotIndex]) {
                const chips = activePage.querySelectorAll('.function-chip');
                for (let i = 0; i < chips.length; i++) {
                    if (chips[i].getAttribute('data-function') === slots[slotIndex]) {
                        chips[i].classList.remove('used');
                        break;
                    }
                }
            }
    
            slots[slotIndex] = functionName;
            event.target.textContent = functionName;
            event.target.classList.add('filled');
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                if (chips[i].getAttribute('data-function') === functionName) {
                    chips[i].classList.add('used');
                    break;
                }
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function checkSolution() {
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const feedback = activePage.querySelector('.feedback');
            if (!feedback) return;
    
            if (slots.includes('')) {
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = 'Niekompletne! Musisz wypełnić wszystkie miejsca w kodzie.';
                return;
            }
    
            const currentPageNum = parseInt(activePage.getAttribute('data-page'));
            const pageIndex = currentPageNum - 1;
            const isCorrect = checkCurrentPageSolution(pageIndex);
    
            if (isCorrect) {
                feedback.className = 'feedback show correct';
                feedback.innerHTML = correctFeedback[pageIndex];
            } else {
                const userAnswer = slots.join(',');
                const incorrectMessages = incorrectFeedback[pageIndex];
    
                for (const pattern in incorrectMessages) {
                    if (pattern === userAnswer) {
                        feedback.className = 'feedback show incorrect';
                        feedback.innerHTML = incorrectMessages[pattern];
                        return;
                    }
    
                    if (pattern.includes('*')) {
                        const regexPattern = '^' + pattern.replace(/\*/g, '.*') + '$';
                        const regex = new RegExp(regexPattern);
                        if (regex.test(userAnswer)) {
                            feedback.className = 'feedback show incorrect';
                            feedback.innerHTML = incorrectMessages[pattern];
                            return;
                        }
                    }
                }
    
                const defaultMessage = incorrectMessages['default'];
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = defaultMessage || '❌ <strong>Niepoprawne rozwiązanie.</strong> Spróbuj ponownie!';
            }
        }
    
        function checkCurrentPageSolution(pageIndex) {
            const solution = correctSolutions[pageIndex];
            for (let i = 0; i < solution.length; i++) {
                if (slots[i] !== solution[i]) {
                    return false;
                }
            }
            return true;
        }
    
        function resetTask() {
            slots.fill('');
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const zones = activePage.querySelectorAll('.drop-zone');
            for (let i = 0; i < zones.length; i++) {
                zones[i].textContent = '';
                zones[i].classList.remove('filled');
            }
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                chips[i].classList.remove('used');
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function showPage(pageNumber) {
            const pages = document.querySelectorAll('.page');
            for (let i = 0; i < pages.length; i++) {
                pages[i].classList.remove('active');
            }
    
            for (let i = 0; i < pages.length; i++) {
                if (parseInt(pages[i].getAttribute('data-page')) === pageNumber) {
                    pages[i].classList.add('active');
                    break;
                }
            }
    
            currentPage = pageNumber;
            const pageIndex = currentPage - 1;
            document.getElementById('currentPage').textContent = currentPage;
    
            document.getElementById('prevBtn').disabled = (currentPage === 1);
            document.getElementById('nextBtn').disabled = (currentPage === totalPages);
    
            slots = new Array(slotsPerPage[pageIndex]).fill('');
    
            resetTask();
        }
    
        function nextPage() {
            if (currentPage < totalPages) {
                showPage(currentPage + 1);
            }
        }
    
        function prevPage() {
            if (currentPage > 1) {
                showPage(currentPage - 1);
            }
        }
    
        document.addEventListener('DOMContentLoaded', function() {
            showPage(1);
        });
</script>

</body>
</html>

"
```
            lineageTag: b6f3fcf7-04c8-4b23-98fe-6eac87c38167

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
                background: #e5e5e5;
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
                background: #6b1718;
            }
    
            .check-button:hover:not(:disabled) {
                background: #380c0c;
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
                D) Tylko w funkcji `CALCULATE`
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
        'Kolumny kalkulowane są obliczane tylko raz - podczas ładowania lub odświeżania danych. Ich wartości są przechowywane w modelu danych.',
        'Miary są obliczane dynamicznie przy każdym odświeżeniu wizualizacji, reagując na aktualny kontekst filtrów i wyboru użytkownika.',
        'Kolumny kalkulowane przechowują wartość dla każdego wiersza w tabeli, co zajmuje pamięć. Miary nie przechowują danych - obliczają wyniki na żądanie.',
        'W kolumnach kalkulowanych musisz używać funkcji iteracyjnych (`SUMX`, `AVERAGEX`) zamiast zwykłych funkcji agregujących (`SUM`, `AVERAGE`), ponieważ kontekst wiersza wymaga iteracji.',
        'Miary domyślnie działają w kontekście filtru, reagując na filtry nałożone przez wizualizacje, slicery i inne filtry w raporcie.',
        'Możesz użyć miary w kolumnie kalkulowanej, ale miara będzie obliczona w kontekście wiersza dla każdego wiersza osobno.',
        'Miary są dynamiczne i automatycznie reagują na zmiany filtrów, co czyni je idealnym wyborem dla obliczeń zależnych od kontekstu użytkownika.'
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
            lineageTag: 66cce212-0612-4905-b38e-1be2a5ec066b

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
        <pre><code>DAX
        Sprzedaż Dni Robocze =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKalendarz[DzienTygodnia] &gt;= <span class='dax-number'>1</span> &&
            dKalendarz[DzienTygodnia] &lt;= <span class='dax-number'>5</span>
        )</code></pre>
        <p><strong>Warunek:</strong> <code>DzienTygodnia >= 1</code> <strong>I</strong> <code>DzienTygodnia <= 5</code></p>
        <p>Alternatywna składnia z funkcją AND():</p>
        <pre><code>DAX
        Sprzedaż Dni Robocze (Alternatywna) =
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
        <pre><code>DAX
        Sprzedaż Weekendy =
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż Netto],
            dKalendarz[DzienTygodnia] = <span class='dax-number'>6</span> ||
            dKalendarz[DzienTygodnia] = <span class='dax-number'>7</span>
        )</code></pre>
        <p><strong>Warunek:</strong> <code>DzienTygodnia = 6</code> <strong>LUB</strong> <code>DzienTygodnia = 7</code></p>
        <p>Alternatywna składnia z funkcją OR():</p>
        <pre><code>DAX
        Sprzedaż Weekendy (Alternatywna) =
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
        <pre><code>DAX
        // ✗ Nieeleganckie
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
        <pre><code>DAX
        Wysoka Sprzedaż Napojów =
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
            lineageTag: 88e42acd-ff47-4b50-abd8-2b8331f8c75a

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
            lineageTag: ee1e75bb-b7ba-418a-ac7f-f0fcb67aa20f

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
        <pre><code>DAX
        Sprzedaż Netto - Napoje =
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
        <pre><code>DAX
        Sprzedaż VIP w <span class='dax-number'>2024</span> = 
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
        <pre><code>DAX
        Sprzedaż Netto - Cały Okres = 
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
        <pre><code>DAX
        Sprzedaż Netto - Udział w Sprzedaży = <span class='dax-function'>DIVIDE</span>(
            [Sprzedaż Netto],
            [Sprzedaż Netto - Cały Okres],
            <span class='dax-function'>BLANK</span>() <span class='dax-comment'>-- jeżeli dzielenie przez 0, to zwróć wartość pustą</span>
        )</code></pre>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209173050.png?raw=true' width='100%'>
        <p><strong>Ciekawostka:</strong> Funkcję <code>REMOVEFILTERS()</code> można używać zamiennie z funkcją <code>ALL()</code>. W tym przypadku ich zastosowanie jest identyczne, natomiast <code>ALL()</code> ma dodatkowe funkcjonalności, o których później.</p>
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
            lineageTag: f194d9d5-a2af-49ce-a635-1a44c31a3099

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
        <p>W poprzednim rozdziale nauczyliśmy się, że miary obliczają się dynamicznie w zależności od kontekstu filtrów. Funkcja CALCULATE pozwala:</p>
        <p>✓ <strong>Nadpisać</strong> istniejące filtry ✓ <strong>Dodać</strong> nowe filtry ✓ <strong>Usunąć</strong> filtry ✓ <strong>Zmienić</strong> sposób działania kontekstu</p>
        <p><strong>Innymi słowy:</strong> CALCULATE daje Ci pełną kontrolę nad tym, na jakich danych oblicza się Twoja miara.</p>
        <h2>Podstawowa składnia</h2>
        <pre><code>DAX
        <span class='dax-function'>CALCULATE</span>(
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
        <p>W Power BI często określa się to terminami: kontekstu, filtra lub kontekstu filtra - można stosować je niemalże zamiennie</p>
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
            lineageTag: ce12fef8-1863-4281-8e42-36e76cdb5e13

        measure '03a. Gaps' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DAX Gaps</title>
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #333;
        background: transparent;
        padding: 20px;
    }
    
    .container {
        max-width: 900px;
        margin: 0 auto;
        background: transparent;
        padding: 40px;
    }
    
    h3 {
        font-size: 26px;
        line-height: 36px;
        font-weight: 600;
        padding-top: 14px;
        padding-bottom: 6px;
        margin-bottom: 1em;
        color: #6b1718;
        border-bottom: 2px solid #6b1718;
    }
    
    .task-description {
        font-size: 1.1em;
        margin: 20px 0;
    }
    
    .code-container {
        background: #f8f9fa;
        border: 2px solid #e1e4e8;
        border-radius: 6px;
        padding: 25px;
        margin: 30px 0;
        font-family: 'Courier New', monospace;
        font-size: 1.05em;
        line-height: 1.8;
    }
    
    .drop-zone {
        display: inline-block;
        min-width: 180px;
        height: 36px;
        background: white;
        border: 2px dashed #6b1718;
        border-radius: 4px;
        padding: 6px 12px;
        margin: 0 4px;
        vertical-align: middle;
        text-align: center;
        transition: all 0.2s;
    }
    
    .drop-zone.drag-over {
        background: #ffe6e6;
        border-color: #380c0c;
    }
    
    .drop-zone.filled {
        background: #d4edda;
        border: 2px solid #28a745;
        border-style: solid;
    }
    
    .functions-title {
        font-size: 1em;
        margin: 30px 0 15px 0;
        color: #333;
    }
    
    .function-chip {
        display: inline-block;
        background: #6b1718;
        color: white;
        padding: 10px 20px;
        margin: 8px;
        border-radius: 20px;
        cursor: grab;
        font-family: 'Courier New', monospace;
        font-size: 1em;
        font-weight: 500;
        transition: all 0.2s;
        user-select: none;
    }
    
    .function-chip:hover {
        background: #380c0c;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(107, 23, 24, 0.3);
    }
    
    .function-chip:active {
        cursor: grabbing;
    }
    
    .function-chip.used {
        opacity: 0.3;
        cursor: not-allowed;
        pointer-events: none;
    }
    
    .button-group {
        margin-top: 30px;
        display: flex;
        gap: 15px;
        align-items: center;
    }
    
    button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 14px 32px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.05em;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    button:hover {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    button.reset-btn {
        background: #6b1718;
        padding: 8px 16px;
        font-size: 0.9em;
    }
    
    button.reset-btn:hover {
        background: #380c0c;
    }
    
    .feedback {
        margin-top: 25px;
        padding: 20px;
        border-radius: 6px;
        display: none;
        font-size: 1.05em;
    }
    
    .feedback.show {
        display: block;
        animation: slideDown 0.3s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .feedback.correct {
        background: #d4edda;
        border-left: 4px solid #28a745;
        color: #155724;
    }
    
    .feedback.incorrect {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        color: #721c24;
    }
    
    .hint-box {
        background: #fafafa;
        border-left: 4px solid #ccc;
        padding: 15px;
        margin: 20px 0;
        border-radius: 4px;
        color: #121212;
        font-size: 0.95em;
    }
    .pagination {
        display: flex;
        align-items: center;
        justify-content: space-between; 
        gap: 20px;
        margin: 30px auto; 
        padding: 20px;
        border-radius: 6px;
    	max-width: 900px;
        border-bottom: 1px solid #e0e0e0;
        width: 100%;
    }
    
    .page-info {
        font-weight: 600;
        color: #666666; 
    }
    
    .nav-button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1em;
        transition: all 0.2s;
    }
    
    .nav-button:hover:not(:disabled) {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .page {
        display: none;
    }
    
    .page.active {
        display: block;
    }
    </style>
</head>
<body>

<div class='pagination'>
    <button class='nav-button' id='prevBtn' onclick='prevPage()'>← Poprzednie</button>
    <span class='page-info'>Zadanie <span id='currentPage'>1</span> z <span id='totalPages'>6</span></span>
    <button class='nav-button' id='nextBtn' onclick='nextPage()'>Następne →</button>
</div>

<div class='page active' data-page='1'>
<div class='container'>
    <div class='task-description'>
        <h3>Podstawowa składnia CALCULATE</h3>
        Chcesz obliczyć sprzedaż tylko dla kategorii NAPOJE. Jak uzupełnić funkcję CALCULATE?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CALCULATE'>CALCULATE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUM'>SUM</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='[Sprzedaż Netto]'>[Sprzedaż Netto]</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='dKategorie[Kategoria]'>dKategorie[Kategoria]</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Sprzedaż Napoje =</div>
        <div><div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(</div>
        <div>    <div class='drop-zone' data-slot='1' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>,</div>
        <div>    <div class='drop-zone' data-slot='2' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div> = ”NAPOJE”</div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Funkcja kluczowa w DAX do modyfikowania kontekstu ma w nazwie słowo oblicz (ang. calculate).
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='2'>
<div class='container'>
    <div class='task-description'>
        <h3>REMOVEFILTERS - usuwanie filtrów</h3>
        Chcesz obliczyć sprzedaż dla całego okresu, ignorując filtry kalendarzowe nałożone na wizualizację. Jakiej funkcji użyć?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ALL'>ALL</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='REMOVEFILTERS'>REMOVEFILTERS</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CLEARFILTERS'>CLEARFILTERS</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Obie: ALL i REMOVEFILTERS'>Obie: ALL i REMOVEFILTERS</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Sprzedaż Cały Okres =</div>
        <div>CALCULATE(</div>
        <div>    [Sprzedaż Netto],</div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(dKalendarz)</div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Materiał wspomina, że funkcja ALL ma nowszy odpowiednik o bardziej czytelnej nazwie. Czy tylko jedna z nich jest poprawna?
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='3'>
<div class='container'>
    <div class='task-description'>
        <h3>Operator IN - wiele wartości</h3>
        Chcesz policzyć sprzedaż dla kategorii NAPOJE lub SŁODYCZE. Jak najeleganciej to zapisać?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='dKategorie[Kategoria] = NAPOJE || dKategorie[Kategoria] = SŁODYCZE'>dKategorie[Kategoria] = NAPOJE || dKategorie[Kategoria] = SŁODYCZE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='dKategorie[Kategoria] IN {NAPOJE, SŁODYCZE}'>dKategorie[Kategoria] IN {NAPOJE, SŁODYCZE}</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='dKategorie[Kategoria] = {NAPOJE, SŁODYCZE}'>dKategorie[Kategoria] = {NAPOJE, SŁODYCZE}</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='OR(dKategorie[Kategoria] = NAPOJE, SŁODYCZE)'>OR(dKategorie[Kategoria] = NAPOJE, SŁODYCZE)</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Sprzedaż Napoje lub Słodycze =</div>
        <div>CALCULATE(</div>
        <div>    [Sprzedaż Netto],</div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Szukasz operatora, który w języku angielskim oznacza w (jako przynależność do zbioru). Wartości umieszczamy w nawiasach klamrowych.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='4'>
<div class='container'>
    <div class='task-description'>
        <h3>Łączenie filtrów - operator AND</h3>
        Chcesz policzyć sprzedaż dla kategorii NAPOJE tylko w dni robocze (DzienTygodnia od 1 do 5). Jak połączyć oba warunki?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='&&'>&&</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='||'>||</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='AND()'>AND()</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Zarówno && jak i AND()'>Zarówno && jak i AND()</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Sprzedaż Napoje Dni Robocze =</div>
        <div>CALCULATE(</div>
        <div>    [Sprzedaż Netto],</div>
        <div>    dKategorie[Kategoria] = NAPOJE <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
        <div>    dKalendarz[DzienTygodnia] >= 1 <div class='drop-zone' data-slot='1' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div> dKalendarz[DzienTygodnia] <= 5</div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Potrzebujesz operatora logicznego i - oba warunki muszą być prawdziwe. Szukasz dwóch znaków, które często w programowaniu oznaczają AND.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='5'>
<div class='container'>
    <div class='task-description'>
        <h3>Udział w sprzedaży całkowitej</h3>
        Chcesz obliczyć procent udziału sprzedaży w danym okresie w stosunku do całkowitej sprzedaży ze wszystkich okresów. Jaką funkcję użyć do usunięcia filtra daty?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ALLSELECTED(dKalendarz)'>ALLSELECTED(dKalendarz)</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='REMOVEFILTERS(dKalendarz)'>REMOVEFILTERS(dKalendarz)</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='FILTER(dKalendarz, TRUE())'>FILTER(dKalendarz, TRUE())</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CALCULATE(dKalendarz)'>CALCULATE(dKalendarz)</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Sprzedaż Cały Okres =</div>
        <div>CALCULATE(</div>
        <div>    [Sprzedaż Netto],</div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
        <div>)</div>
        <div></div>
        <div>Udział % =</div>
        <div>DIVIDE(</div>
        <div>    [Sprzedaż Netto],</div>
        <div>    [Sprzedaż Cały Okres]</div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Szukasz funkcji, która w nazwie ma usuń filtry lub wszystkie (ang. remove/all). Materiał wspomina dwie równoważne opcje.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='6'>
<div class='container'>
    <div class='task-description'>
        <h3>Kontekst filtrowania</h3>
        Co to jest kontekst filtrowania w Power BI?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Zbiór filtrów aktywnych w danym momencie obliczeń'>Zbiór filtrów aktywnych w danym momencie obliczeń</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Lista wszystkich tabel w modelu'>Lista wszystkich tabel w modelu</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Funkcja do filtrowania danych'>Funkcja do filtrowania danych</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Tryb edycji filtrów w wizualizacji'>Tryb edycji filtrów w wizualizacji</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>-- Gdy na wykres nałożysz kolumnę Kategoria,</div>
        <div>-- tworzy się <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>, który określa</div>
        <div>-- jakie wiersze są brane pod uwagę w obliczeniach</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Kontekst oznacza środowisko lub warunki. Kontekst filtrowania to warunki określające, które dane są aktualnie widoczne.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 6;
    const slotsPerPage = [3, 1, 2, 2, 1, 1];
    let slots = new Array(slotsPerPage[0]).fill('');
    const correctSolutions = [['CALCULATE', '[Sprzeda\u017c Netto]', 'dKategorie[Kategoria]'], ['Obie: ALL i REMOVEFILTERS'], ['dKategorie[Kategoria] IN {NAPOJE', 'S\u0141ODYCZE}'], ['&&', '&&'], ['REMOVEFILTERS(dKalendarz)'], ['Zbi\u00f3r filtr\u00f3w aktywnych w danym momencie oblicze\u0144']];
    const correctFeedback = ['\u2705 Brawo! Rozwi\u0105zanie poprawne!\nPodstawowa sk\u0142adnia CALCULATE to: `CALCULATE(<wyra\u017cenie/miara>, <filtr1>, <filtr2>, ...)`. W tym przypadku: `CALCULATE([Sprzeda\u017c Netto], dKategorie[Kategoria] = NAPOJE)`. Funkcja CALCULATE oblicza miar\u0119 z dodanym filtrem na kategori\u0119.', '\u2705 **Brawo! Rozwi\u0105zanie poprawne!**\nObie funkcje `ALL(dKalendarz)` i `REMOVEFILTERS(dKalendarz)` dzia\u0142aj\u0105 identycznie w kontek\u015bcie CALCULATE - usuwaj\u0105 filtry z tabeli. `REMOVEFILTERS()` jest nowsz\u0105, bardziej czyteln\u0105 wersj\u0105. Zaleca si\u0119 u\u017cywa\u0107 `REMOVEFILTERS()` ze wzgl\u0119du na jasno\u015b\u0107 nazwy, ale `ALL()` nadal dzia\u0142a.', '\u2705 **Brawo! Rozwi\u0105zanie poprawne!**\nOperator `IN` pozwala elegancko sprawdzi\u0107, czy warto\u015b\u0107 znajduje si\u0119 w zestawie: `dKategorie[Kategoria] IN {NAPOJE, S\u0141ODYCZE}`. To czytelniejsze i kr\u00f3tsze ni\u017c wielokrotne u\u017cycie operatora `||` (OR). Zestaw warto\u015bci ujmujemy w nawiasy klamrowe `{}`.', '\u2705 **Brawo! Rozwi\u0105zanie poprawne!**\nOperator `&&` \u0142\u0105czy warunki logiczne operatorem AND (i) - wszystkie musz\u0105 by\u0107 spe\u0142nione jednocze\u015bnie. Mo\u017cesz te\u017c u\u017cy\u0107 funkcji `AND()`, ale operator `&&` jest cz\u0119\u015bciej u\u017cywany i czytelniejszy w tego typu wyra\u017ceniach. Alternatywnie mo\u017cna te\u017c rozdzieli\u0107 filtry przecinkami w CALCULATE - dzia\u0142aj\u0105 wtedy jako AND.', '\u2705 **Brawo! Rozwi\u0105zanie poprawne!**\n`REMOVEFILTERS(dKalendarz)` usuwa wszystkie filtry z tabeli kalendarza, dzi\u0119ki czemu `[Sprzeda\u017c Ca\u0142y Okres]` pokazuje sum\u0119 dla wszystkich dat, niezale\u017cnie od kontekstu na\u0142o\u017conego na wizualizacj\u0119. Mo\u017cesz te\u017c u\u017cy\u0107 `ALL(dKalendarz)` - dzia\u0142a identycznie.', '\u2705 **Brawo! Rozwi\u0105zanie poprawne!**\nKontekst filtrowania (filter context) to zbi\u00f3r filtr\u00f3w aktywnych w danym momencie oblicze\u0144. Okre\u015bla on jakie wiersze z tabel s\u0105 brane pod uwag\u0119. Gdy naniesiesz kolumn\u0119 na wizualizacj\u0119, staje si\u0119 ona cz\u0119\u015bci\u0105 kontekstu filtrowania - miary s\u0105 obliczane osobno dla ka\u017cdej warto\u015bci tej kolumny.'];
    const incorrectFeedback = [{}, {}, {}, {}, {}, {}];

    function drag(event) {
            event.dataTransfer.setData('function', event.target.getAttribute('data-function'));
        }
    
        function allowDrop(event) {
            event.preventDefault();
            event.target.classList.add('drag-over');
        }
    
        function dragLeave(event) {
            event.target.classList.remove('drag-over');
        }
    
        function drop(event) {
            event.preventDefault();
            event.target.classList.remove('drag-over');
    
            const functionName = event.dataTransfer.getData('function');
            const slotIndex = parseInt(event.target.getAttribute('data-slot'));
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            if (slots[slotIndex]) {
                const chips = activePage.querySelectorAll('.function-chip');
                for (let i = 0; i < chips.length; i++) {
                    if (chips[i].getAttribute('data-function') === slots[slotIndex]) {
                        chips[i].classList.remove('used');
                        break;
                    }
                }
            }
    
            slots[slotIndex] = functionName;
            event.target.textContent = functionName;
            event.target.classList.add('filled');
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                if (chips[i].getAttribute('data-function') === functionName) {
                    chips[i].classList.add('used');
                    break;
                }
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function checkSolution() {
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const feedback = activePage.querySelector('.feedback');
            if (!feedback) return;
    
            if (slots.includes('')) {
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = 'Niekompletne! Musisz wypełnić wszystkie miejsca w kodzie.';
                return;
            }
    
            const currentPageNum = parseInt(activePage.getAttribute('data-page'));
            const pageIndex = currentPageNum - 1;
            const isCorrect = checkCurrentPageSolution(pageIndex);
    
            if (isCorrect) {
                feedback.className = 'feedback show correct';
                feedback.innerHTML = correctFeedback[pageIndex];
            } else {
                const userAnswer = slots.join(',');
                const incorrectMessages = incorrectFeedback[pageIndex];
    
                for (const pattern in incorrectMessages) {
                    if (pattern === userAnswer) {
                        feedback.className = 'feedback show incorrect';
                        feedback.innerHTML = incorrectMessages[pattern];
                        return;
                    }
    
                    if (pattern.includes('*')) {
                        const regexPattern = '^' + pattern.replace(/\*/g, '.*') + '$';
                        const regex = new RegExp(regexPattern);
                        if (regex.test(userAnswer)) {
                            feedback.className = 'feedback show incorrect';
                            feedback.innerHTML = incorrectMessages[pattern];
                            return;
                        }
                    }
                }
    
                const defaultMessage = incorrectMessages['default'];
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = defaultMessage || '❌ <strong>Niepoprawne rozwiązanie.</strong> Spróbuj ponownie!';
            }
        }
    
        function checkCurrentPageSolution(pageIndex) {
            const solution = correctSolutions[pageIndex];
            for (let i = 0; i < solution.length; i++) {
                if (slots[i] !== solution[i]) {
                    return false;
                }
            }
            return true;
        }
    
        function resetTask() {
            slots.fill('');
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const zones = activePage.querySelectorAll('.drop-zone');
            for (let i = 0; i < zones.length; i++) {
                zones[i].textContent = '';
                zones[i].classList.remove('filled');
            }
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                chips[i].classList.remove('used');
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function showPage(pageNumber) {
            const pages = document.querySelectorAll('.page');
            for (let i = 0; i < pages.length; i++) {
                pages[i].classList.remove('active');
            }
    
            for (let i = 0; i < pages.length; i++) {
                if (parseInt(pages[i].getAttribute('data-page')) === pageNumber) {
                    pages[i].classList.add('active');
                    break;
                }
            }
    
            currentPage = pageNumber;
            const pageIndex = currentPage - 1;
            document.getElementById('currentPage').textContent = currentPage;
    
            document.getElementById('prevBtn').disabled = (currentPage === 1);
            document.getElementById('nextBtn').disabled = (currentPage === totalPages);
    
            slots = new Array(slotsPerPage[pageIndex]).fill('');
    
            resetTask();
        }
    
        function nextPage() {
            if (currentPage < totalPages) {
                showPage(currentPage + 1);
            }
        }
    
        function prevPage() {
            if (currentPage > 1) {
                showPage(currentPage - 1);
            }
        }
    
        document.addEventListener('DOMContentLoaded', function() {
            showPage(1);
        });
</script>

</body>
</html>

"
```
            lineageTag: e9b38509-9a02-4b5c-a61a-9100bc5826b9

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
                background: #e5e5e5;
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
                background: #6b1718;
            }
    
            .check-button:hover:not(:disabled) {
                background: #380c0c;
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
            <p><strong>Do czego służy funkcja `CALCULATE`?</strong></p>
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
            <p><strong>Jaka jest podstawowa składnia funkcji `CALCULATE`?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) `CALCULATE(wyrażenie, filtr1, filtr2, ...)`
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) `CALCULATE(tabela, warunek)`
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) `CALCULATE(kolumna = wartość)`
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) `CALCULATE(miara + filtr)`
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Co zrobi `CALCULATE` bez żadnych filtrów:` CALCULATE([Suma Sprzedaży])`?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) Zwróci błąd
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) Zwróci wartość identyczną jak `[Suma Sprzedaży]`
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
                A) `CALCULATE([Suma], Produkty[Kategoria] = ″Elektronika″)`
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) `CALCULATE([Suma], FILTER(Produkty, ″Elektronika″))`
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) `CALCULATE([Suma] WHERE Kategoria = ″Elektronika″)`
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) `SUM(Produkty[Sprzedaż], ″Elektronika″)`
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 0)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Czy w `CALCULATE` możesz zastosować wiele filtrów jednocześnie?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) Nie, tylko jeden filtr na raz
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) Tak, `CALCULATE` nie ma zdefiniowanej liczby parametrów
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Tak, filtry są łączone operatorem `OR`
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
            <p><strong>Co robi funkcja `FILTER` w połączeniu z `CALCULATE`?</strong></p>
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
            <p><strong>Jaki będzie wynik: CALCULATE([Sprzedaż], Produkty[Cena] &gt; 100, Produkty[Kategoria] = ″AGD″)?</strong></p>
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
        '`CALCULATE` to najpotężniejsza funkcja w DAX, która pozwala modyfikować kontekst filtrów, w którym obliczana jest miara.',
        'Składnia to `CALCULATE` , gdzie wyrażenie to obliczana miara, a następne argumenty to filtry modyfikujące kontekst.',
        '`CALCULATE` bez dodatkowych filtrów zwróci tę samą wartość co samo wyrażenie. Jednak jest to przydatne, gdy chcemy przekształcić kontekst wiersza w kontekst filtru.',
        'Składnia to `CALCULATE([Miara], Tabela[Kolumna] = wartość).` Możemy też użyć `FILTER`, ale prostsza składnia jest bardziej czytelna dla pojedynczych warunków.',
        'CALCULATE może przyjmować wiele filtrów oddzielonych przecinkami. Wszystkie filtry są łączone operatorem AND (muszą być spełnione jednocześnie).',
        '`FILTER` zwraca tabelę zawierającą tylko te wiersze, które spełniają podany warunek. W `CALCULATE` używamy jej do bardziej złożonych warunków filtrowania.',
        'Oba filtry są łączone operatorem `AND`, więc wynik to sprzedaż produktów spełniających OBA warunki: kategoria = AGD ORAZ cena > 100.'
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
            lineageTag: f100e9be-2a6b-4999-907a-6d75ef122529

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
        <pre><code>DAX
        <span class='dax-function'>ALL</span>(tabela)
        <span class='dax-function'>ALL</span>(tabela[kolumna])
        <span class='dax-function'>ALL</span>(tabela[kolumna1], tabela[kolumna2], ...)</code></pre>
        <h2>Podstawowy przypadek - procent od całości</h2>
        <p>Użytkownik wybiera w slicerze kategorię 'Computers'. Chcesz pokazać:</p>
        <ul>
        <li>Sprzedaż Computers: 400 000 zł</li>
        <li>Sprzedaż całkowita: 1 000 000 zł (mimo filtru!)</li>
        <li>Udział: 40%</li>
        </ul>
        <pre><code>DAX
        Total fSprzedaż = <span class='dax-function'>SUM</span>(ffSprzedaż[fSprzedażAmount])

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
        <pre><code>DAX
        <span class='dax-function'>CALCULATE</span>(
        	[Total fSprzedaż],
        	<span class='dax-function'>ALL</span>(dProduct[ProductCategoryName])
        )</code></pre>
        <ul>
        <li> Usuwa <strong>WSZYSTKIE</strong> filtry z tabeli <strong>dProduct</strong></li>
        <li> Kolor, marka, podkategoria - wszystko zignorowane</li>
        </ul>
        <pre><code>DAX
        <span class='dax-function'>CALCULATE</span>(
        	[Total fSprzedaż],
        	 <span class='dax-function'>ALL</span>(dProduct)
         )</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>REMOVEFILTERS - nowszy odpowiednik ALL</h2>
        <p>Od 2019 roku mamy <code>REMOVEFILTERS</code>, który robi dokładnie to samo co <code>ALL</code> w kontekście <code>CALCULATE</code>:</p>
        <pre><code>DAX
        // Te dwie miary są identyczne:
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
        <pre><code>DAX
        // ALL jako funkcja tabelaryczna (zwraca tabelę bez filtrów)
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
            lineageTag: eef4bea6-909d-4c09-be4d-7e792fbe1822

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
        <pre><code>DAX
        // Podejście <span class='dax-number'>1</span>: wymieniasz wszystko co chcesz usunąć
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
        <pre><code>DAX
        // Podejście <span class='dax-number'>2</span>: ALLEXCEPT
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
        <pre><code>DAX
        // Udział produktu w swojej kategorii I kraju
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
            lineageTag: adc423b7-32ca-4cd5-be0b-ff679b9cc3f8

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
        <pre><code>DAX
        // Próba z ALL
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
        <pre><code>DAX
        fSprzedaż % with ALLSELECTED =
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
        <pre><code>DAX
        // Usuwa filtr wizualizacji tylko z kategorii
        <span class='dax-function'>CALCULATE</span>(
        	[Total fSprzedaż],
        	 <span class='dax-function'>ALLSELECTED</span>(dProduct[ProductCategoryName])
         )</code></pre>
        <pre><code>DAX
        // Usuwa filtr wizualizacji ze wszystkiego (produkty, czas, geografia...)
        <span class='dax-function'>CALCULATE</span>(
        	[Total fSprzedaż],
        	 <span class='dax-function'>ALLSELECTED</span>()
         )</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Porównanie ALL vs ALLSELECTED</h2>
        <pre><code>DAX
        Total fSprzedaż = <span class='dax-function'>SUM</span>(ffSprzedaż[fSprzedażAmount])

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
            lineageTag: bb8f8956-271e-4176-8ba8-ed02caf8d290

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
        <pre><code>DAX
        <span class='dax-function'>CROSSFILTER</span>(&lt;columnName1&gt;, &lt;columnName2&gt;, &lt;direction&gt;)</code></pre>
        <ul>
        <li><code>Both</code> — filtrowanie dwukierunkowe (filtry przechodzą w obu kierunkach, domyślnie jest jednokierunkowe).</li>
        <li><code>None</code> — wyłącza filtrowanie między tabelami.</li>
        <li><code>OneWay</code> — jednokierunkowe filtrowanie z Column1 do Column2 (domyślnie).</li>
        <li><code>OneWayReverse</code> — jednokierunkowe filtrowanie z Column2 do Column1.</li>
        </ul>
        <pre><code>DAX
        Filtruj w obie strony = 
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
            lineageTag: 9ac8b424-6784-4641-b209-d4a907de0424

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
        <pre><code>DAX
        fSprzedaż Computers =
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
        <pre><code>DAX
        fSprzedaż Computers Keep =
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
        <pre><code>DAX
        // Bez KEEPFILTERS - zawsze pokazuje Premium, nawet gdy wybrano 'Standard'
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
            lineageTag: 31625684-9a71-4368-9af1-43e219706baa

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
        <pre><code>DAX
        fSprzedaż
        ├─ Data Sprzedaży      → 'dKalendarz'[Data] (relacja aktywna)
        ├─ Data Fakturowania   → 'dKalendarz'[Data] (relacja nieaktywna)
        └─ Data Dostawy        → 'dKalendarz'[Data] (relacja nieaktywna)</code></pre>
        <img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/Pasted%20image%2020251209193536.png?raw=true' width='100%'>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Podstawowa składnia</h1>
        <pre><code>DAX
        <span class='dax-comment'>------- Miara używająca domyślnej relacji (Data Zamówienia)</span>
        Według Zamówienia = 
            <span class='dax-function'>SUM</span> ( fSprzedaż, fSprzedaż[Wartość Netto] )


        <span class='dax-comment'>------- Miara aktywująca relację </span>
        Według Faktury = 
        <span class='dax-function'>CALCULATE</span> (
            <span class='dax-function'>SUMX</span> ( fSprzedaż, fSprzedaż[Wartość Netto] ),
            <span class='dax-function'>USERELATIONSHIP</span> ( fSprzedaż[Data Fakturowania], 'dKalendarz'[Date] )
        )



        <span class='dax-comment'>------- Miara aktywująca relację</span>
        Według Dostawy = 
        <span class='dax-function'>CALCULATE</span> (
            <span class='dax-function'>SUMX</span> ( fSprzedaż, fSprzedaż[Wartość Netto] ),
            <span class='dax-function'>USERELATIONSHIP</span> ( fSprzedaż[Data Dostawy], 'dKalendarz'[Date] )
        )</code></pre>
        <p><strong>Kluczowe zasady:</strong></p>
        <ul>
        <li><code>USERELATIONSHIP</code> działa tylko wewnątrz <code>CALCULATE</code> lub <code>CALCULATETABLE</code></li>
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
            lineageTag: 06dc4031-5ef9-409a-9def-abd5007aa277

        measure '04a. Gaps' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DAX Gaps</title>
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #333;
        background: transparent;
        padding: 20px;
    }
    
    .container {
        max-width: 900px;
        margin: 0 auto;
        background: transparent;
        padding: 40px;
    }
    
    h3 {
        font-size: 26px;
        line-height: 36px;
        font-weight: 600;
        padding-top: 14px;
        padding-bottom: 6px;
        margin-bottom: 1em;
        color: #6b1718;
        border-bottom: 2px solid #6b1718;
    }
    
    .task-description {
        font-size: 1.1em;
        margin: 20px 0;
    }
    
    .code-container {
        background: #f8f9fa;
        border: 2px solid #e1e4e8;
        border-radius: 6px;
        padding: 25px;
        margin: 30px 0;
        font-family: 'Courier New', monospace;
        font-size: 1.05em;
        line-height: 1.8;
    }
    
    .drop-zone {
        display: inline-block;
        min-width: 180px;
        height: 36px;
        background: white;
        border: 2px dashed #6b1718;
        border-radius: 4px;
        padding: 6px 12px;
        margin: 0 4px;
        vertical-align: middle;
        text-align: center;
        transition: all 0.2s;
    }
    
    .drop-zone.drag-over {
        background: #ffe6e6;
        border-color: #380c0c;
    }
    
    .drop-zone.filled {
        background: #d4edda;
        border: 2px solid #28a745;
        border-style: solid;
    }
    
    .functions-title {
        font-size: 1em;
        margin: 30px 0 15px 0;
        color: #333;
    }
    
    .function-chip {
        display: inline-block;
        background: #6b1718;
        color: white;
        padding: 10px 20px;
        margin: 8px;
        border-radius: 20px;
        cursor: grab;
        font-family: 'Courier New', monospace;
        font-size: 1em;
        font-weight: 500;
        transition: all 0.2s;
        user-select: none;
    }
    
    .function-chip:hover {
        background: #380c0c;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(107, 23, 24, 0.3);
    }
    
    .function-chip:active {
        cursor: grabbing;
    }
    
    .function-chip.used {
        opacity: 0.3;
        cursor: not-allowed;
        pointer-events: none;
    }
    
    .button-group {
        margin-top: 30px;
        display: flex;
        gap: 15px;
        align-items: center;
    }
    
    button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 14px 32px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.05em;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    button:hover {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    button.reset-btn {
        background: #6b1718;
        padding: 8px 16px;
        font-size: 0.9em;
    }
    
    button.reset-btn:hover {
        background: #380c0c;
    }
    
    .feedback {
        margin-top: 25px;
        padding: 20px;
        border-radius: 6px;
        display: none;
        font-size: 1.05em;
    }
    
    .feedback.show {
        display: block;
        animation: slideDown 0.3s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .feedback.correct {
        background: #d4edda;
        border-left: 4px solid #28a745;
        color: #155724;
    }
    
    .feedback.incorrect {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        color: #721c24;
    }
    
    .hint-box {
        background: #fafafa;
        border-left: 4px solid #ccc;
        padding: 15px;
        margin: 20px 0;
        border-radius: 4px;
        color: #121212;
        font-size: 0.95em;
    }
    .pagination {
        display: flex;
        align-items: center;
        justify-content: space-between; 
        gap: 20px;
        margin: 30px auto; 
        padding: 20px;
        border-radius: 6px;
    	max-width: 900px;
        border-bottom: 1px solid #e0e0e0;
        width: 100%;
    }
    
    .page-info {
        font-weight: 600;
        color: #666666; 
    }
    
    .nav-button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1em;
        transition: all 0.2s;
    }
    
    .nav-button:hover:not(:disabled) {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .page {
        display: none;
    }
    
    .page.active {
        display: block;
    }
    </style>
</head>
<body>

<div class='pagination'>
    <button class='nav-button' id='prevBtn' onclick='prevPage()'>← Poprzednie</button>
    <span class='page-info'>Zadanie <span id='currentPage'>1</span> z <span id='totalPages'>6</span></span>
    <button class='nav-button' id='nextBtn' onclick='nextPage()'>Następne →</button>
</div>

<div class='page active' data-page='1'>
<div class='container'>
    <div class='task-description'>
        <h3>ALL vs REMOVEFILTERS</h3>
        Jaka jest różnica między `ALL` a `REMOVEFILTERS` w kontekście `CALCULATE`?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Brak różnicy - działają identycznie'>Brak różnicy - działają identycznie</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ALL usuwa wszystkie filtry, REMOVEFILTERS tylko niektóre'>ALL usuwa wszystkie filtry, REMOVEFILTERS tylko niektóre</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='REMOVEFILTERS jest szybsze'>REMOVEFILTERS jest szybsze</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ALL działa tylko na tabelach, REMOVEFILTERS tylko na kolumnach'>ALL działa tylko na tabelach, REMOVEFILTERS tylko na kolumnach</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>-- Te dwie miary są:</div>
        <div>CALCULATE([Sprzedaż], ALL(dProduct))</div>
        <div>CALCULATE([Sprzedaż], REMOVEFILTERS(dProduct))</div>
        <div></div>
        <div>Odpowiedź: <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Która funkcja jest łatwiejsza do zrozumienia w języku naturalnym? Co to sugeruje o ich funkcjonalności?
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='2'>
<div class='container'>
    <div class='task-description'>
        <h3>Zachowanie wybranych filtrów</h3>
        Chcesz usunąć wszystkie filtry z tabeli `dProdukt`, OPRÓCZ filtra na `Kategoria`. Jakiej funkcji użyć?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ALLEXCEPT'>ALLEXCEPT</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='KEEPFILTERS'>KEEPFILTERS</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='REMOVEFILTERSEXCEPT'>REMOVEFILTERSEXCEPT</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ALLBUT'>ALLBUT</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Sprzedaż per Kategoria =</div>
        <div>CALCULATE(</div>
        <div>    [Total Sprzedaż],</div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(dProdukt, dProdukt[Kategoria])</div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Szukasz funkcji, która w nazwie ma wszystkie oprócz (ang. all except). Materiał pokazuje przykład z ProductCategoryName.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='3'>
<div class='container'>
    <div class='task-description'>
        <h3>Filtry z slicerów</h3>
        Tworzysz wykres z udziałem procentowym kategorii. Użytkownik wybiera w slicerze 3 kategorie. Chcesz, żeby procenty sumowały się do 100% dla tych 3 wybranych kategorii. Jakiej funkcji użyć?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ALL'>ALL</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ALLSELECTED'>ALLSELECTED</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ALLEXCEPT'>ALLEXCEPT</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='REMOVEFILTERS'>REMOVEFILTERS</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Sprzedaż % =</div>
        <div>DIVIDE(</div>
        <div>    [Całkowita Sprzedaż],</div>
        <div>    CALCULATE([Całkowita Sprzedaż], <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(dProdukt[Kategoria]))</div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Szukasz funkcji, która pamięta co użytkownik wybrał (selected) w slicerach, ale ignoruje filtry z samej wizualizacji.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='4'>
<div class='container'>
    <div class='task-description'>
        <h3>Przecięcie filtrów</h3>
        Masz miarę ze stałym filtrem NAPOJE. Chcesz, żeby gdy użytkownik wybierze Cameras w slicerze, miara zwróciła BLANK (bo nie ma przecięcia). Jakiej funkcji użyć?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='KEEPFILTERS'>KEEPFILTERS</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='INTERSECT'>INTERSECT</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CROSSFILTER'>CROSSFILTER</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='FILTERINTERSECT'>FILTERINTERSECT</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Sprzedaż Computers Keep =</div>
        <div>CALCULATE(</div>
        <div>    [Total Sprzedaż],</div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(dProduct[ProductCategoryName] = ″NAPOJE″)</div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Szukasz funkcji, która mówi zachowaj (keep) istniejące filtry i znajdź część wspólną z nowym filtrem.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='5'>
<div class='container'>
    <div class='task-description'>
        <h3>Kierunek relacji</h3>
        Jakiej funkcji użyjesz do zmiany kierunku filtrowania relacji między tabelami?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CALCULATE'>CALCULATE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CROSSFILTER'>CROSSFILTER</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='FILTERX'>FILTERX</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='USERELATIONSHIP'>USERELATIONSHIP</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Miara =</div>
        <div>CALCULATE(</div>
        <div>    [Liczba Zamówień],</div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(</div>
        <div>        fSprzedaż[Data Dostawy],</div>
        <div>        dKalendarz[Data],</div>
        <div>        Both</div>
        <div>    )</div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Both, None, OneWay, OneWayReverse. To parametry określające kierunek czegoś. Czego?
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='6'>
<div class='container'>
    <div class='task-description'>
        <h3>Aktywacja relacji</h3>
        Masz tabelę sprzedaży z trzema datami: Data Zamówienia (relacja aktywna), Data Wysyłki, Data Dostawy (relacje nieaktywne). Chcesz policzyć sprzedaż według daty wysyłki. Jakiej funkcji użyć?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='USERELATIONSHIP'>USERELATIONSHIP</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ACTIVATERELATIONSHIP'>ACTIVATERELATIONSHIP</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SWITCHRELATION'>SWITCHRELATION</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='RELATEDTABLE'>RELATEDTABLE</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Sprzedaż by Data Dostawy =</div>
        <div>CALCULATE(</div>
        <div>    [Total Sprzedaż],</div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(</div>
        <div>        fSprzedaż[Data Dostawy],</div>
        <div>        dKalendarz[Data]</div>
        <div>    )</div>
        <div>)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Szukasz funkcji, która mówi użyj relacji (use relationship). Materiał pokazuje przykład z ShipmentDate i DeliveryDate.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 6;
    const slotsPerPage = [1, 1, 1, 1, 1, 1];
    let slots = new Array(slotsPerPage[0]).fill('');
    const correctSolutions = [['Brak r\u00f3\u017cnicy - dzia\u0142aj\u0105 identycznie'], ['ALLEXCEPT'], ['ALLSELECTED'], ['KEEPFILTERS'], ['Zmiany kierunku filtrowania relacji mi\u0119dzy tabelami'], ['USERELATIONSHIP']];
    const correctFeedback = ['\u2705 Brawo! Rozwi\u0105zanie poprawne!\nW kontek\u015bcie `CALCULATE` funkcje `ALL()` i `REMOVEFILTERS()` dzia\u0142aj\u0105 identycznie - obie usuwaj\u0105 filtry z tabeli lub kolumny. `REMOVEFILTERS()` zosta\u0142a wprowadzona w 2019 roku jako bardziej czytelna alternatywa. Zaleca si\u0119 u\u017cywa\u0107 `REMOVEFILTERS()` ze wzgl\u0119du na jasno\u015b\u0107 nazwy, ale `ALL()` nadal jest powszechnie stosowane. R\u00f3\u017cnica jest semantyczna, nie funkcjonalna.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\n`ALLEXCEPT()` usuwa wszystkie filtry z podanej tabeli OPR\u00d3CZ (except) wymienionych kolumn. Sk\u0142adnia: `ALLEXCEPT(tabela, kolumna1, kolumna2, ...)`. W tym przypadku `ALLEXCEPT(dProduct, dProduct[ProductCategoryName])` usuwa filtry ze wszystkich kolumn tabeli dProduct poza kategori\u0105 - dzi\u0119ki czemu mo\u017cesz policzy\u0107 sum\u0119 dla ca\u0142ej kategorii, ignoruj\u0105c filtry na produkty, marki, kolory itp.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\n`ALLSELECTED()` usuwa filtry z wizualizacji (wiersze/kolumny wykresu/tabeli), ale ZACHOWUJE filtry zewn\u0119trzne - slicery, filtry strony i raportu. Dzi\u0119ki temu mianownik uwzgl\u0119dnia tylko kategorie wybrane w slicerze, a procenty sumuj\u0105 si\u0119 do 100%. `ALL()` usun\u0119\u0142oby te\u017c filtr ze slicera, co da\u0142oby niepoprawne wyniki.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\n`KEEPFILTERS()` tworzy przeci\u0119cie (cz\u0119\u015b\u0107 wsp\u00f3ln\u0105) filtr\u00f3w zamiast nadpisywania. Gdy u\u017cytkownik wybierze Cameras w slicerze, a ty filtrujesz na Computers, przeci\u0119cie (Cameras) \u2229 (Computers) = \u2205 (zbi\u00f3r pusty) = BLANK. Bez `KEEPFILTERS()` filtr z `CALCULATE` nadpisa\u0142by wyb\u00f3r u\u017cytkownika i zawsze pokazywa\u0142by Computers.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\n`CROSSFILTER()` s\u0142u\u017cy do tymczasowej zmiany kierunku filtrowania relacji mi\u0119dzy tabelami w kontek\u015bcie danej miary. Mo\u017cliwe kierunki to: `Both` (dwukierunkowe), `None` (wy\u0142\u0105czone), `OneWay` (domy\u015blnie), `OneWayReverse` (odwr\u00f3cone). Pozwala to dynamicznie modyfikowa\u0107 przep\u0142yw filtr\u00f3w bez zmiany modelu danych.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\n`USERELATIONSHIP()` aktywuje nieaktywn\u0105 relacj\u0119 mi\u0119dzy tabelami na czas trwania obliczenia. Sk\u0142adnia: `USERELATIONSHIP(kolumna_z_tabeli_fakt\u00f3w, kolumna_z_tabeli_wymiaru)`. W modelu mo\u017ce by\u0107 wiele relacji mi\u0119dzy tymi samymi tabelami, ale tylko jedna aktywna domy\u015blnie. USERELATIONSHIP pozwala tymczasowo u\u017cy\u0107 innej relacji bez zmiany modelu.'];
    const incorrectFeedback = [{}, {}, {}, {}, {}, {}];

    function drag(event) {
            event.dataTransfer.setData('function', event.target.getAttribute('data-function'));
        }
    
        function allowDrop(event) {
            event.preventDefault();
            event.target.classList.add('drag-over');
        }
    
        function dragLeave(event) {
            event.target.classList.remove('drag-over');
        }
    
        function drop(event) {
            event.preventDefault();
            event.target.classList.remove('drag-over');
    
            const functionName = event.dataTransfer.getData('function');
            const slotIndex = parseInt(event.target.getAttribute('data-slot'));
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            if (slots[slotIndex]) {
                const chips = activePage.querySelectorAll('.function-chip');
                for (let i = 0; i < chips.length; i++) {
                    if (chips[i].getAttribute('data-function') === slots[slotIndex]) {
                        chips[i].classList.remove('used');
                        break;
                    }
                }
            }
    
            slots[slotIndex] = functionName;
            event.target.textContent = functionName;
            event.target.classList.add('filled');
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                if (chips[i].getAttribute('data-function') === functionName) {
                    chips[i].classList.add('used');
                    break;
                }
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function checkSolution() {
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const feedback = activePage.querySelector('.feedback');
            if (!feedback) return;
    
            if (slots.includes('')) {
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = 'Niekompletne! Musisz wypełnić wszystkie miejsca w kodzie.';
                return;
            }
    
            const currentPageNum = parseInt(activePage.getAttribute('data-page'));
            const pageIndex = currentPageNum - 1;
            const isCorrect = checkCurrentPageSolution(pageIndex);
    
            if (isCorrect) {
                feedback.className = 'feedback show correct';
                feedback.innerHTML = correctFeedback[pageIndex];
            } else {
                const userAnswer = slots.join(',');
                const incorrectMessages = incorrectFeedback[pageIndex];
    
                for (const pattern in incorrectMessages) {
                    if (pattern === userAnswer) {
                        feedback.className = 'feedback show incorrect';
                        feedback.innerHTML = incorrectMessages[pattern];
                        return;
                    }
    
                    if (pattern.includes('*')) {
                        const regexPattern = '^' + pattern.replace(/\*/g, '.*') + '$';
                        const regex = new RegExp(regexPattern);
                        if (regex.test(userAnswer)) {
                            feedback.className = 'feedback show incorrect';
                            feedback.innerHTML = incorrectMessages[pattern];
                            return;
                        }
                    }
                }
    
                const defaultMessage = incorrectMessages['default'];
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = defaultMessage || '❌ <strong>Niepoprawne rozwiązanie.</strong> Spróbuj ponownie!';
            }
        }
    
        function checkCurrentPageSolution(pageIndex) {
            const solution = correctSolutions[pageIndex];
            for (let i = 0; i < solution.length; i++) {
                if (slots[i] !== solution[i]) {
                    return false;
                }
            }
            return true;
        }
    
        function resetTask() {
            slots.fill('');
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const zones = activePage.querySelectorAll('.drop-zone');
            for (let i = 0; i < zones.length; i++) {
                zones[i].textContent = '';
                zones[i].classList.remove('filled');
            }
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                chips[i].classList.remove('used');
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function showPage(pageNumber) {
            const pages = document.querySelectorAll('.page');
            for (let i = 0; i < pages.length; i++) {
                pages[i].classList.remove('active');
            }
    
            for (let i = 0; i < pages.length; i++) {
                if (parseInt(pages[i].getAttribute('data-page')) === pageNumber) {
                    pages[i].classList.add('active');
                    break;
                }
            }
    
            currentPage = pageNumber;
            const pageIndex = currentPage - 1;
            document.getElementById('currentPage').textContent = currentPage;
    
            document.getElementById('prevBtn').disabled = (currentPage === 1);
            document.getElementById('nextBtn').disabled = (currentPage === totalPages);
    
            slots = new Array(slotsPerPage[pageIndex]).fill('');
    
            resetTask();
        }
    
        function nextPage() {
            if (currentPage < totalPages) {
                showPage(currentPage + 1);
            }
        }
    
        function prevPage() {
            if (currentPage > 1) {
                showPage(currentPage - 1);
            }
        }
    
        document.addEventListener('DOMContentLoaded', function() {
            showPage(1);
        });
</script>

</body>
</html>

"
```
            lineageTag: c38e4b3d-239f-46bc-9e0b-8b40c07aa2d3

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
                background: #e5e5e5;
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
                background: #6b1718;
            }
    
            .check-button:hover:not(:disabled) {
                background: #380c0c;
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
            <p><strong>Jaka jest różnica między `ALL(Tabela)` a `ALL(Tabela[Kolumna])`?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Nie ma różnicy
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) `ALL(Tabela)` usuwa filtry z całej tabeli, `ALL(Tabela[Kolumna])` tylko z jednej kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) `ALL(Tabela)` jest szybsze
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) `ALL(Tabela[Kolumna])` usuwa także relacje
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Jaka jest nowoczesna alternatywa dla funkcji `ALL`?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) `CLEARFILTERS`
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) `REMOVEFILTERS`
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) `DELETEFILTERS`
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) `NOFILTERS`
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>Co oblicza: `CALCULATE([Sprzedaż], ALL(Produkty))`?</strong></p>
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
                A) `[Sprzedaż] / SUM(Sprzedaż)`
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) `[Sprzedaż] / CALCULATE([Sprzedaż], ALL(Tabela))`
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) `DIVIDE([Sprzedaż], [Całkowita Sprzedaż])`
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) `Zarówno B jak i C (gdy [Całkowita Sprzedaż] używa ALL)`
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 3)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Co robi funkcja `ALLSELECTED`?</strong></p>
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
                D) To samo co `ALL`
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(5, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-5'></div>
    </div>

    <!-- Pytanie 7 -->
    <div class='page'>
        <h1>Pytanie 7</h1>
        <div class='question-box'>
            <p><strong>Kiedy używamy `KEEPFILTERS` w `CALCULATE`?</strong></p>
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
        '`ALL` usuwa filtry z tabeli lub kolumny. Mówisz silnikowi DAX: zignoruj wszelkie filtry nałożone na ten obiekt.',
        '`ALL(Tabela)` usuwa wszystkie filtry z całej tabeli, natomiast `ALL(Tabela[Kolumna])` usuwa filtry tylko z konkretnej kolumny, zachowując filtry na innych kolumnach.',
        '`REMOVEFILTERS` to nowoczesna alternatywa dla `ALL`, która ma bardziej czytelną nazwę i jasno pokazuje intencję - usunięcie filtrów.',
        '`ALL(Produkty)` usuwa wszystkie filtry z tabeli Produkty, więc `CALCULATE` zwróci sprzedaż dla WSZYSTKICH produktów, niezależnie od aktualnych filtrów.',
        'Procent obliczamy dzieląc wartość bieżącą przez wartość całkowitą (bez filtrów). Można to zrobić bezpośrednio lub przez osobną miarę.',
        '`ALLSELECTED` usuwa filtry wewnętrzne (z wizualizacji), ale zachowuje filtry zewnętrzne (slicery, filtry strony). Jest użyteczna do obliczeń typu ″procent od wybranego″.',
        '`KEEPFILTERS` sprawia, że nowy filtr jest DODAWANY do istniejących (`AND`), zamiast je NADPISYWAĆ. Przydatne gdy chcemy zawęzić, a nie zastąpić kontekst.'
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
            lineageTag: 0be1ae68-e15d-4918-9da0-9ff1d4bc50e9

        measure '05. DAX - Zaawansowane Kwerendy - Query View' = ```
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
        <pre><code>DAX
        <span class='dax-keyword'>VAR</span> A = <span class='dax-number'>1</span>
        <span class='dax-keyword'>VAR</span> B = <span class='dax-number'>5</span>
        A + B</code></pre>
        <p><strong>Status:</strong> ❌ <strong>To jest niepoprawne!</strong></p>
        <ul>
        <li>Zmienne <code>VAR</code> <strong>zawsze muszą być zakończone słowem kluczowym <code>RETURN</code></strong></li>
        <li>DAX nie wie, co ma zwrócić jako wynik</li>
        <li>Ten kod spowoduje błąd składniowy</li>
        </ul>
        <pre><code>DAX
        EVALUATE
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
        <pre><code>DAX
        EVALUATE
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
        <pre><code>DAX
        DEFINE MEASURE _Measures[Test] = 
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
            lineageTag: b5990823-d14d-4723-9cc4-27e90bf0ebe0

        measure '05. DAX - Zaawansowane Kwerendy' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>05. DAX - Zaawansowane Kwerendy</title>
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

<div class='container' id='viz_3d785b0e'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_3d785b0e' onclick='changePage_3d785b0e(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_3d785b0e'>1</span> z <span id='totalPages_3d785b0e'>4</span>
        </span>
        <button id='nextBtn_3d785b0e' onclick='changePage_3d785b0e(1)'>Następna →</button>
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
        <pre><code>DAX
        NazwaMiary = 
        <span class='dax-keyword'>VAR</span> NazwaZmiennej1 = &lt;wyrażenie1&gt;
        <span class='dax-keyword'>VAR</span> NazwaZmiennej2 = &lt;wyrażenie2&gt;
        <span class='dax-keyword'>VAR</span> NazwaZmiennej3 = &lt;wyrażenie3&gt;
        <span class='dax-keyword'>RETURN</span> &lt;wynik_końcowy&gt;</code></pre>
        <p><strong>Przykład prosty:</strong></p>
        <pre><code>DAX
        Całkowity Koszt = 
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
        <pre><code>DAX
        <span class='dax-function'>SUMX</span>(
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
        <pre><code>DAX
        Suma Odchyleń od Średniej = 
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
    var vizId = '3d785b0e';
    var containerId = 'viz_' + vizId;

    var currentPage_3d785b0e = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_3d785b0e'] = function(n) {
        if (n > totalPages) currentPage_3d785b0e = totalPages;
        if (n < 1) currentPage_3d785b0e = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_3d785b0e - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_3d785b0e;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_3d785b0e === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_3d785b0e === totalPages);
    };

    window['changePage_3d785b0e'] = function(n) {
        currentPage_3d785b0e += n;
        window['showPage_3d785b0e'](currentPage_3d785b0e);
    };

    // Inicjalizacja
    window['showPage_3d785b0e'](1);

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
            lineageTag: ee65b3b6-0881-4f55-8333-261c76faa87e

        measure '05a. Gaps' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DAX Gaps</title>
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #333;
        background: transparent;
        padding: 20px;
    }
    
    .container {
        max-width: 900px;
        margin: 0 auto;
        background: transparent;
        padding: 40px;
    }
    
    h3 {
        font-size: 26px;
        line-height: 36px;
        font-weight: 600;
        padding-top: 14px;
        padding-bottom: 6px;
        margin-bottom: 1em;
        color: #6b1718;
        border-bottom: 2px solid #6b1718;
    }
    
    .task-description {
        font-size: 1.1em;
        margin: 20px 0;
    }
    
    .code-container {
        background: #f8f9fa;
        border: 2px solid #e1e4e8;
        border-radius: 6px;
        padding: 25px;
        margin: 30px 0;
        font-family: 'Courier New', monospace;
        font-size: 1.05em;
        line-height: 1.8;
    }
    
    .drop-zone {
        display: inline-block;
        min-width: 180px;
        height: 36px;
        background: white;
        border: 2px dashed #6b1718;
        border-radius: 4px;
        padding: 6px 12px;
        margin: 0 4px;
        vertical-align: middle;
        text-align: center;
        transition: all 0.2s;
    }
    
    .drop-zone.drag-over {
        background: #ffe6e6;
        border-color: #380c0c;
    }
    
    .drop-zone.filled {
        background: #d4edda;
        border: 2px solid #28a745;
        border-style: solid;
    }
    
    .functions-title {
        font-size: 1em;
        margin: 30px 0 15px 0;
        color: #333;
    }
    
    .function-chip {
        display: inline-block;
        background: #6b1718;
        color: white;
        padding: 10px 20px;
        margin: 8px;
        border-radius: 20px;
        cursor: grab;
        font-family: 'Courier New', monospace;
        font-size: 1em;
        font-weight: 500;
        transition: all 0.2s;
        user-select: none;
    }
    
    .function-chip:hover {
        background: #380c0c;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(107, 23, 24, 0.3);
    }
    
    .function-chip:active {
        cursor: grabbing;
    }
    
    .function-chip.used {
        opacity: 0.3;
        cursor: not-allowed;
        pointer-events: none;
    }
    
    .button-group {
        margin-top: 30px;
        display: flex;
        gap: 15px;
        align-items: center;
    }
    
    button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 14px 32px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.05em;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    button:hover {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    button.reset-btn {
        background: #6b1718;
        padding: 8px 16px;
        font-size: 0.9em;
    }
    
    button.reset-btn:hover {
        background: #380c0c;
    }
    
    .feedback {
        margin-top: 25px;
        padding: 20px;
        border-radius: 6px;
        display: none;
        font-size: 1.05em;
    }
    
    .feedback.show {
        display: block;
        animation: slideDown 0.3s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .feedback.correct {
        background: #d4edda;
        border-left: 4px solid #28a745;
        color: #155724;
    }
    
    .feedback.incorrect {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        color: #721c24;
    }
    
    .hint-box {
        background: #fafafa;
        border-left: 4px solid #ccc;
        padding: 15px;
        margin: 20px 0;
        border-radius: 4px;
        color: #121212;
        font-size: 0.95em;
    }
    .pagination {
        display: flex;
        align-items: center;
        justify-content: space-between; 
        gap: 20px;
        margin: 30px auto; 
        padding: 20px;
        border-radius: 6px;
    	max-width: 900px;
        border-bottom: 1px solid #e0e0e0;
        width: 100%;
    }
    
    .page-info {
        font-weight: 600;
        color: #666666; 
    }
    
    .nav-button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1em;
        transition: all 0.2s;
    }
    
    .nav-button:hover:not(:disabled) {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .page {
        display: none;
    }
    
    .page.active {
        display: block;
    }
    </style>
</head>
<body>

<div class='pagination'>
    <button class='nav-button' id='prevBtn' onclick='prevPage()'>← Poprzednie</button>
    <span class='page-info'>Zadanie <span id='currentPage'>1</span> z <span id='totalPages'>6</span></span>
    <button class='nav-button' id='nextBtn' onclick='nextPage()'>Następne →</button>
</div>

<div class='page active' data-page='1'>
<div class='container'>
    <div class='task-description'>
        <h3>Deklaracja zmiennej VAR</h3>
        Chcesz utworzyć miarę z dwiema zmiennymi: Ilość i Cena, a następnie zwrócić ich iloczyn. Jak uzupełnić kod?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='VAR'>VAR</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='LET'>LET</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='DECLARE'>DECLARE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='RETURN'>RETURN</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Wartość =</div>
        <div><div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div> Ilość = 100</div>
        <div>VAR Cena = 25</div>
        <div><div class='drop-zone' data-slot='1' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div> Ilość * Cena</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='2'>
<div class='container'>
    <div class='task-description'>
        <h3>VAR w funkcjach iteracyjnych</h3>
        Co się dzieje ze zmiennymi VAR wewnątrz funkcji SUMX?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Są obliczane raz przed iteracją'>Są obliczane raz przed iteracją</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Są obliczane na nowo dla każdego wiersza'>Są obliczane na nowo dla każdego wiersza</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Są obliczane tylko dla pierwszego wiersza'>Są obliczane tylko dla pierwszego wiersza</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Wywołują błąd - VAR nie może być w SUMX'>Wywołują błąd - VAR nie może być w SUMX</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>SUMX(</div>
        <div>    {1, 2, 3},</div>
        <div>    VAR Kwadrat = [Value] * [Value]</div>
        <div>    RETURN Kwadrat</div>
        <div>)</div>
        <div></div>
        <div>-- Zmienna Kwadrat jest: <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='3'>
<div class='container'>
    <div class='task-description'>
        <h3>Zmienne VAR poza i wewnątrz iteracji</h3>
        Masz zmienną Średnia zadeklarowaną PRZED SUMX i zmienną Wartość WEWNĄTRZ SUMX. Która jest obliczana wielokrotnie?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Jednokrotnie'>Jednokrotnie</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Per Wiersz'>Per Wiersz</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Ani razu'>Ani razu</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Dwa razy'>Dwa razy</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>Suma Odchyleń =</div>
        <div>VAR Średnia = AVERAGE({1, 2, 3})  -- Obliczona: <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
        <div>RETURN</div>
        <div>    SUMX(</div>
        <div>        {1, 2, 3},</div>
        <div>        VAR Wartość = [Value]  -- Obliczona: <div class='drop-zone' data-slot='1' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
        <div>        RETURN Wartość - Średnia</div>
        <div>    )</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='4'>
<div class='container'>
    <div class='task-description'>
        <h3>Query View - słowo kluczowe EVALUATE</h3>
        Co jest wymagane na początku zapytania w DAX Query View?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='EVALUATE'>EVALUATE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SELECT'>SELECT</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='QUERY'>QUERY</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='BEGIN'>BEGIN</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div><div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
        <div>    ROW(Test, 1 + 1)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='5'>
<div class='container'>
    <div class='task-description'>
        <h3>DEFINE MEASURE w Query View</h3>
        Do czego służy DEFINE MEASURE w zapytaniu DAX?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SET'>SET</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='DEFINE MEASURE'>DEFINE MEASURE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='DEF'>DEF</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='EVALUATE'>EVALUATE</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div><div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div> _Measures[Test] =</div>
        <div>    VAR A = 1</div>
        <div>    VAR B = 5</div>
        <div>    RETURN A + B</div>
        <div></div>
        <div>EVALUATE</div>
        <div>    ROW(Wynik, [Test])</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='6'>
<div class='container'>
    <div class='task-description'>
        <h3>ROW - tworzenie jednoierszowej tabeli</h3>
        Query View zwraca tylko tabele, co tworzy tabelę z jednego wiersza
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='ROW'>ROW</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='EVALUATE'>EVALUATE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='DEFINE'>DEFINE</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>EVALUATE</div>
        <div>    VAR A = 1</div>
        <div>    VAR B = 5</div>
        <div>RETURN</div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(Suma, A + B)</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Materiał wyjaśnia: DAX potrafi zwracać wyłącznie wartości tabelaryczne. A + B zwraca pojedynczą wartość.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 6;
    const slotsPerPage = [2, 1, 2, 1, 1, 1];
    let slots = new Array(slotsPerPage[0]).fill('');
    const correctSolutions = [['VAR', 'RETURN'], ['S\u0105 obliczane na nowo dla ka\u017cdego wiersza'], ['Jednokrotnie', 'Per Wiersz'], ['EVALUATE'], ['DEFINE MEASURE'], ['ROW']];
    const correctFeedback = ['\u2705 Brawo! Rozwi\u0105zanie poprawne!\nW DAX zmienne deklarujesz s\u0142owem kluczowym `VAR`, a wynik zwracasz s\u0142owem `RETURN`. Ka\u017cda zmienna rozpoczyna si\u0119 od `VAR`. Sk\u0142adnia: `VAR nazwa = wyra\u017cenie`. Mo\u017ce by\u0107 wiele zmiennych VAR, ale tylko jedno RETURN na ko\u0144cu. RETURN okre\u015bla, co zostanie zwr\u00f3cone jako wynik miary.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nW funkcjach iteracyjnych jak `SUMX`, `FILTER`, `ADDCOLUMNS` zmienne VAR s\u0105 **obliczane w ka\u017cdej iteracji** z warto\u015bciami z aktualnego wiersza. Dla ka\u017cdego wiersza tabeli zmienna jest tworzona od nowa. To oznacza, \u017ce zmienne VAR wewn\u0105trz iteracji s\u0105 dynamiczne i dostosowuj\u0105 si\u0119 do kontekstu wiersza. W przyk\u0142adzie: dla 1 zwr\u00f3ci 1, dla 2 zwr\u00f3ci 4, dla 3 zwr\u00f3ci 9.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nZmienna `\u015arednia` jest PRZED SUMX, wi\u0119c obliczana **tylko raz** i ma sta\u0142\u0105 warto\u015b\u0107 (3). Zmienna `Warto\u015b\u0107` jest WEWN\u0104TRZ SUMX, wi\u0119c obliczana **dla ka\u017cdego wiersza** osobno (1, 2, 3). Zmienne poza iteracj\u0105 s\u0105 statyczne, zmienne wewn\u0105trz iteracji s\u0105 dynamiczne. To pozwala por\u00f3wnywa\u0107 ka\u017cdy wiersz (Warto\u015b\u0107) ze sta\u0142\u0105 (\u015arednia).', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nW Query View zapytania DAX musz\u0105 zaczyna\u0107 si\u0119 od s\u0142owa kluczowego `EVALUATE`. Po nim umieszczasz wyra\u017cenie zwracaj\u0105ce tabel\u0119 (np. `ROW()`, `SUMMARIZECOLUMNS()`, nazw\u0119 tabeli). Query View s\u0142u\u017cy do testowania zapyta\u0144 DAX bez tworzenia miar w modelu. `EVALUATE` m\u00f3wi silnikowi DAX: wykonaj to zapytanie i zwr\u00f3\u0107 wynik tabelaryczny.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\n`DEFINE MEASURE` tworzy **tymczasow\u0105 miar\u0119** dost\u0119pn\u0105 tylko w kontek\u015bcie tego zapytania - nie dodaje jej do modelu danych. To przydatne do testowania i prototypowania miar bez za\u015bmiecania modelu. Miara istnieje tylko podczas wykonywania zapytania i znika po jego zako\u0144czeniu. Po `DEFINE` nast\u0119puje `EVALUATE` z w\u0142a\u015bciwym zapytaniem u\u017cywaj\u0105cym zdefiniowanej miary.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nDAX w Query View (po `EVALUATE`) mo\u017ce zwraca\u0107 **tylko warto\u015bci tabelaryczne**. Wyra\u017cenie `A + B` zwraca pojedyncz\u0105 warto\u015b\u0107 (skalar), nie tabel\u0119. Funkcja `ROW()` tworzy sztuczn\u0105 tabel\u0119 z jednym wierszem i jedn\u0105 kolumn\u0105, dzi\u0119ki czemu mo\u017cemy zwr\u00f3ci\u0107 wynik skalara jako tabel\u0119. Sk\u0142adnia: `ROW(nazwa kolumny, warto\u015b\u0107)`.'];
    const incorrectFeedback = [{}, {}, {}, {}, {}, {}];

    function drag(event) {
            event.dataTransfer.setData('function', event.target.getAttribute('data-function'));
        }
    
        function allowDrop(event) {
            event.preventDefault();
            event.target.classList.add('drag-over');
        }
    
        function dragLeave(event) {
            event.target.classList.remove('drag-over');
        }
    
        function drop(event) {
            event.preventDefault();
            event.target.classList.remove('drag-over');
    
            const functionName = event.dataTransfer.getData('function');
            const slotIndex = parseInt(event.target.getAttribute('data-slot'));
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            if (slots[slotIndex]) {
                const chips = activePage.querySelectorAll('.function-chip');
                for (let i = 0; i < chips.length; i++) {
                    if (chips[i].getAttribute('data-function') === slots[slotIndex]) {
                        chips[i].classList.remove('used');
                        break;
                    }
                }
            }
    
            slots[slotIndex] = functionName;
            event.target.textContent = functionName;
            event.target.classList.add('filled');
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                if (chips[i].getAttribute('data-function') === functionName) {
                    chips[i].classList.add('used');
                    break;
                }
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function checkSolution() {
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const feedback = activePage.querySelector('.feedback');
            if (!feedback) return;
    
            if (slots.includes('')) {
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = 'Niekompletne! Musisz wypełnić wszystkie miejsca w kodzie.';
                return;
            }
    
            const currentPageNum = parseInt(activePage.getAttribute('data-page'));
            const pageIndex = currentPageNum - 1;
            const isCorrect = checkCurrentPageSolution(pageIndex);
    
            if (isCorrect) {
                feedback.className = 'feedback show correct';
                feedback.innerHTML = correctFeedback[pageIndex];
            } else {
                const userAnswer = slots.join(',');
                const incorrectMessages = incorrectFeedback[pageIndex];
    
                for (const pattern in incorrectMessages) {
                    if (pattern === userAnswer) {
                        feedback.className = 'feedback show incorrect';
                        feedback.innerHTML = incorrectMessages[pattern];
                        return;
                    }
    
                    if (pattern.includes('*')) {
                        const regexPattern = '^' + pattern.replace(/\*/g, '.*') + '$';
                        const regex = new RegExp(regexPattern);
                        if (regex.test(userAnswer)) {
                            feedback.className = 'feedback show incorrect';
                            feedback.innerHTML = incorrectMessages[pattern];
                            return;
                        }
                    }
                }
    
                const defaultMessage = incorrectMessages['default'];
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = defaultMessage || '❌ <strong>Niepoprawne rozwiązanie.</strong> Spróbuj ponownie!';
            }
        }
    
        function checkCurrentPageSolution(pageIndex) {
            const solution = correctSolutions[pageIndex];
            for (let i = 0; i < solution.length; i++) {
                if (slots[i] !== solution[i]) {
                    return false;
                }
            }
            return true;
        }
    
        function resetTask() {
            slots.fill('');
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const zones = activePage.querySelectorAll('.drop-zone');
            for (let i = 0; i < zones.length; i++) {
                zones[i].textContent = '';
                zones[i].classList.remove('filled');
            }
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                chips[i].classList.remove('used');
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function showPage(pageNumber) {
            const pages = document.querySelectorAll('.page');
            for (let i = 0; i < pages.length; i++) {
                pages[i].classList.remove('active');
            }
    
            for (let i = 0; i < pages.length; i++) {
                if (parseInt(pages[i].getAttribute('data-page')) === pageNumber) {
                    pages[i].classList.add('active');
                    break;
                }
            }
    
            currentPage = pageNumber;
            const pageIndex = currentPage - 1;
            document.getElementById('currentPage').textContent = currentPage;
    
            document.getElementById('prevBtn').disabled = (currentPage === 1);
            document.getElementById('nextBtn').disabled = (currentPage === totalPages);
    
            slots = new Array(slotsPerPage[pageIndex]).fill('');
    
            resetTask();
        }
    
        function nextPage() {
            if (currentPage < totalPages) {
                showPage(currentPage + 1);
            }
        }
    
        function prevPage() {
            if (currentPage > 1) {
                showPage(currentPage - 1);
            }
        }
    
        document.addEventListener('DOMContentLoaded', function() {
            showPage(1);
        });
</script>

</body>
</html>

"
```
            lineageTag: 6108a86d-e311-445d-addf-2553e4efcb63

        measure '05a. Quiz' = ```
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
                background: #e5e5e5;
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
                background: #6b1718;
            }
    
            .check-button:hover:not(:disabled) {
                background: #380c0c;
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
            <p><strong>Do czego służy słowo kluczowe `VAR` w DAX?</strong></p>
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
            <p><strong>Ile razy może wystąpić słowo `RETURN` w jednej mierze DAX?</strong></p>
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
            <p><strong>Co się stanie ze zmiennymi `VAR` wewnątrz funkcji iteracyjnej jak `SUMX`?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) Są obliczane tylko raz przed rozpoczęciem iteracji
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) Są obliczane na nowo w każdej iteracji dla aktualnego wiersza
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) Nie można używać `VAR` wewnątrz funkcji iteracyjnych
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
            <p><strong>Jakie są główne zalety używania zmiennych `VAR`?</strong></p>
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
            <p><strong>Co może zawierać zmienna `VAR`?</strong></p>
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
        'W jednej mierze może być tylko jedno `RETURN`, które zwraca końcowy wynik miary.',
        'Zmienne `VAR` wewnątrz funkcji iteracyjnych są obliczane na nowo w każdej iteracji, dostosowując się do aktualnego wiersza.',
        'Obliczenia: 2²=4, 3²=9, 4²=16. Suma: 4+9+16=29.',
        '`VAR` pomaga unikać powtarzania kodu, poprawia czytelność i wydajność miar (wartość obliczana tylko raz).',
        'Zmienna zadeklarowana przed funkcją iteracyjną jest obliczana tylko raz i jej wartość jest używana we wszystkich iteracjach.',
        'Zmienna `VAR` może zawierać liczby, teksty, tabele i wyniki obliczeń - jest bardzo wszechstronna.'
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
            lineageTag: 78fac8e5-22df-4449-b1d6-321d6f5f154d

        measure '06. Tworzenie zestawień tabelarycznych - Tworzenie Tabeli' = ```
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
        <p><strong>Podejście modern (<code>SUMMARIZECOLUMNS</code>):</strong></p>
        <ul>
        <li>Łączy grupowanie, dodawanie obliczeń i usuwanie pustych wierszy w jednej funkcji</li>
        <li>Krótsze, czytelniejsze, bezpieczniejsze</li>
        <li>Obecnie zalecany standard do raportów i zapytań w DAX</li>
        </ul>
        <pre><code>DAX
        <span class='dax-comment'>------- LEGACY  </span>
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
        <p><strong>Zalety <code>SUMMARIZECOLUMNS</code>:</strong></p>
        <ul>
        <li>Rozumie kontekst całego modelu danych</li>
        <li>Działa spójnie z modelem gwiazdy – automatycznie obsługuje kombinacje wymiarów</li>
        <li>Pozwala w jednym wyrażeniu pobierać dane z różnych tabel faktów</li>
        <li>Zwraca kompletny wynik w jednej tabeli</li>
        </ul>
        <p><strong>Problemy z <code>SUMMARIZE</code>:</strong></p>
        <ul>
        <li>Ogranicza się do jednej tabeli faktów</li>
        <li>Wymaga ręcznego tworzenia siatki kombinacji przez <code>CROSSJOIN</code></li>
        <li>Trzeba łączyć wyniki przez <code>NATURALLEFTOUTERJOIN</code></li>
        <li>Bardziej skomplikowane, mniej czytelne i podatne na błędy</li>
        </ul>
        <pre><code>DAX
        <span class='dax-comment'>------- RECOMMENDED  </span>
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
        <p><strong>Problem z <code>SUMMARIZECOLUMNS</code> bez miar:</strong></p>
        <ul>
        <li>Bez tabeli źródłowej generuje wszystkie możliwe kombinacje (jak <code>CROSSJOIN</code>)</li>
        <li>Może zwrócić wiele pustych kombinacji, które nie istnieją w danych</li>
        <li>Nie jest to zwykle pożądane zachowanie</li>
        </ul>
        <pre><code>DAX
        <span class='dax-comment'>------- RECOMMENDED  </span>
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
            lineageTag: 82713b9f-1be2-470d-bba8-cbbbcb0be0f5

        measure '06a. Gaps' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DAX Gaps</title>
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #333;
        background: transparent;
        padding: 20px;
    }
    
    .container {
        max-width: 900px;
        margin: 0 auto;
        background: transparent;
        padding: 40px;
    }
    
    h3 {
        font-size: 26px;
        line-height: 36px;
        font-weight: 600;
        padding-top: 14px;
        padding-bottom: 6px;
        margin-bottom: 1em;
        color: #6b1718;
        border-bottom: 2px solid #6b1718;
    }
    
    .task-description {
        font-size: 1.1em;
        margin: 20px 0;
    }
    
    .code-container {
        background: #f8f9fa;
        border: 2px solid #e1e4e8;
        border-radius: 6px;
        padding: 25px;
        margin: 30px 0;
        font-family: 'Courier New', monospace;
        font-size: 1.05em;
        line-height: 1.8;
    }
    
    .drop-zone {
        display: inline-block;
        min-width: 180px;
        height: 36px;
        background: white;
        border: 2px dashed #6b1718;
        border-radius: 4px;
        padding: 6px 12px;
        margin: 0 4px;
        vertical-align: middle;
        text-align: center;
        transition: all 0.2s;
    }
    
    .drop-zone.drag-over {
        background: #ffe6e6;
        border-color: #380c0c;
    }
    
    .drop-zone.filled {
        background: #d4edda;
        border: 2px solid #28a745;
        border-style: solid;
    }
    
    .functions-title {
        font-size: 1em;
        margin: 30px 0 15px 0;
        color: #333;
    }
    
    .function-chip {
        display: inline-block;
        background: #6b1718;
        color: white;
        padding: 10px 20px;
        margin: 8px;
        border-radius: 20px;
        cursor: grab;
        font-family: 'Courier New', monospace;
        font-size: 1em;
        font-weight: 500;
        transition: all 0.2s;
        user-select: none;
    }
    
    .function-chip:hover {
        background: #380c0c;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(107, 23, 24, 0.3);
    }
    
    .function-chip:active {
        cursor: grabbing;
    }
    
    .function-chip.used {
        opacity: 0.3;
        cursor: not-allowed;
        pointer-events: none;
    }
    
    .button-group {
        margin-top: 30px;
        display: flex;
        gap: 15px;
        align-items: center;
    }
    
    button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 14px 32px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.05em;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    button:hover {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    button.reset-btn {
        background: #6b1718;
        padding: 8px 16px;
        font-size: 0.9em;
    }
    
    button.reset-btn:hover {
        background: #380c0c;
    }
    
    .feedback {
        margin-top: 25px;
        padding: 20px;
        border-radius: 6px;
        display: none;
        font-size: 1.05em;
    }
    
    .feedback.show {
        display: block;
        animation: slideDown 0.3s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .feedback.correct {
        background: #d4edda;
        border-left: 4px solid #28a745;
        color: #155724;
    }
    
    .feedback.incorrect {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        color: #721c24;
    }
    
    .hint-box {
        background: #fafafa;
        border-left: 4px solid #ccc;
        padding: 15px;
        margin: 20px 0;
        border-radius: 4px;
        color: #121212;
        font-size: 0.95em;
    }
    .pagination {
        display: flex;
        align-items: center;
        justify-content: space-between; 
        gap: 20px;
        margin: 30px auto; 
        padding: 20px;
        border-radius: 6px;
    	max-width: 900px;
        border-bottom: 1px solid #e0e0e0;
        width: 100%;
    }
    
    .page-info {
        font-weight: 600;
        color: #666666; 
    }
    
    .nav-button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1em;
        transition: all 0.2s;
    }
    
    .nav-button:hover:not(:disabled) {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .page {
        display: none;
    }
    
    .page.active {
        display: block;
    }
    </style>
</head>
<body>

<div class='pagination'>
    <button class='nav-button' id='prevBtn' onclick='prevPage()'>← Poprzednie</button>
    <span class='page-info'>Zadanie <span id='currentPage'>1</span> z <span id='totalPages'>3</span></span>
    <button class='nav-button' id='nextBtn' onclick='nextPage()'>Następne →</button>
</div>

<div class='page active' data-page='1'>
<div class='container'>
    <div class='task-description'>
        <h3>Najlepsze praktyki tworzenia podsumowania</h3>
        Które podejście jest zalecane do tworzenia zestawień z miarami?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='`SUMMARIZE`'>`SUMMARIZE`</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='`SUMMARIZECOLUMNS`'>`SUMMARIZECOLUMNS`</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='`CROSSJOIN`'>`CROSSJOIN`</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='`VALUES`'>`VALUES`</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>-- Podejście modern (zalecane):</div>
        <div>EVALUATE</div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(</div>
        <div>        Product[Brand], Date[Year],</div>
        <div>        Sales, [Total Sales]</div>
        <div>    )</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Materiał wyraźnie nazywa jedno podejście MODERN a drugie LEGACY. Które jest zalecane?
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='2'>
<div class='container'>
    <div class='task-description'>
        <h3>Podsumowanie z tabelą źródłową</h3>
        Co się stanie gdy użyjesz SUMMARIZE z tabelą źródłową jako pierwszy parametr?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Zwróci tylko kombinacje istniejące w tej tabeli'>Zwróci tylko kombinacje istniejące w tej tabeli</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Zwróci wszystkie możliwe kombinacje (jak `CROSSJOIN`)'>Zwróci wszystkie możliwe kombinacje (jak `CROSSJOIN`)</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Spowoduje błąd'>Spowoduje błąd</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Zwróci pustą tabelę'>Zwróci pustą tabelę</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>EVALUATE</div>
        <div>    SUMMARIZE(</div>
        <div>        Sales,  -- <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
        <div>        Product[Brand],</div>
        <div>        Customer[Continent]</div>
        <div>    )</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Materiał mówi: zwraca tylko kombinacje występujące w danych faktycznych. Co to oznacza dla wyniku?
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='3'>
<div class='container'>
    <div class='task-description'>
        <h3>Zalecenia - SUMMARIZE vs SUMMARIZECOLUMNS</h3>
        Która zasada jest prawidłowa według materiału?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Grupowanie bez miar: SUMMARIZE z tabelą źródłową; z miarami: SUMMARIZECOLUMNS'>Grupowanie bez miar: SUMMARIZE z tabelą źródłową; z miarami: SUMMARIZECOLUMNS</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Zawsze używaj SUMMARIZECOLUMNS'>Zawsze używaj SUMMARIZECOLUMNS</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Zawsze używaj SUMMARIZE'>Zawsze używaj SUMMARIZE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Zależy od wydajności zapytania'>Zależy od wydajności zapytania</span>
    </div>

    <div class='code-container'>
        <div>DAX</div>
        <div>-- Zasada decyzyjna:</div>
        <div><div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div></div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Materiał kończy się sekcją Zasada: która jasno to definiuje. Co tam jest napisane?
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 3;
    const slotsPerPage = [1, 1, 1];
    let slots = new Array(slotsPerPage[0]).fill('');
    const correctSolutions = [['SUMMARIZECOLUMNS'], ['Zwr\u00f3ci tylko kombinacje istniej\u0105ce w tej tabeli'], ['Grupowanie bez miar: SUMMARIZE z tabel\u0105 \u017ar\u00f3d\u0142ow\u0105; z miarami: SUMMARIZECOLUMNS']];
    const correctFeedback = ['\u2705 Brawo! Rozwi\u0105zanie poprawne!\n`SUMMARIZECOLUMNS` to obecnie zalecany standard do tworzenia zestawie\u0144 tabelarycznych z miarami. \u0141\u0105czy grupowanie, obliczenia i automatyczne usuwanie pustych wierszy w jednej funkcji. Jest kr\u00f3tsze, czytelniejsze i bezpieczniejsze ni\u017c legacy approach z `SUMMARIZE` + `ADDCOLUMNS` + `FILTER`. Rozumie kontekst ca\u0142ego modelu danych i poprawnie obs\u0142uguje relacje.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nGdy pierwszy parametr `SUMMARIZE` to tabela fakt\u00f3w (np. Sales), funkcja zwraca tylko kombinacje wymiar\u00f3w rzeczywi\u015bcie wyst\u0119puj\u0105ce w tej tabeli. Filtruje automatycznie do istniej\u0105cych relacji. To jest po\u017c\u0105dane zachowanie - nie dostaniesz pustych kombinacji Brand-Continent, kt\u00f3re nie maj\u0105 transakcji. To g\u0142\u00f3wny przypadek u\u017cycia `SUMMARIZE` - proste grupowanie bez miar.', '\u2705 Brawo! Rozwi\u0105zanie poprawne!\nTo kluczowa zasada z materia\u0142u: **Do samego grupowania bez miar u\u017cywaj `SUMMARIZE` z tabel\u0105 \u017ar\u00f3d\u0142ow\u0105. Do grupowania z miarami u\u017cywaj `SUMMARIZECOLUMNS`.** SUMMARIZE z tabel\u0105 zwraca tylko istniej\u0105ce kombinacje (unika pustych wierszy). SUMMARIZECOLUMNS jest lepsze gdy dodajesz obliczenia - automatycznie usuwa puste wiersze i obs\u0142uguje wiele tabel fakt\u00f3w.'];
    const incorrectFeedback = [{}, {}, {}];

    function drag(event) {
            event.dataTransfer.setData('function', event.target.getAttribute('data-function'));
        }
    
        function allowDrop(event) {
            event.preventDefault();
            event.target.classList.add('drag-over');
        }
    
        function dragLeave(event) {
            event.target.classList.remove('drag-over');
        }
    
        function drop(event) {
            event.preventDefault();
            event.target.classList.remove('drag-over');
    
            const functionName = event.dataTransfer.getData('function');
            const slotIndex = parseInt(event.target.getAttribute('data-slot'));
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            if (slots[slotIndex]) {
                const chips = activePage.querySelectorAll('.function-chip');
                for (let i = 0; i < chips.length; i++) {
                    if (chips[i].getAttribute('data-function') === slots[slotIndex]) {
                        chips[i].classList.remove('used');
                        break;
                    }
                }
            }
    
            slots[slotIndex] = functionName;
            event.target.textContent = functionName;
            event.target.classList.add('filled');
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                if (chips[i].getAttribute('data-function') === functionName) {
                    chips[i].classList.add('used');
                    break;
                }
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function checkSolution() {
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const feedback = activePage.querySelector('.feedback');
            if (!feedback) return;
    
            if (slots.includes('')) {
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = 'Niekompletne! Musisz wypełnić wszystkie miejsca w kodzie.';
                return;
            }
    
            const currentPageNum = parseInt(activePage.getAttribute('data-page'));
            const pageIndex = currentPageNum - 1;
            const isCorrect = checkCurrentPageSolution(pageIndex);
    
            if (isCorrect) {
                feedback.className = 'feedback show correct';
                feedback.innerHTML = correctFeedback[pageIndex];
            } else {
                const userAnswer = slots.join(',');
                const incorrectMessages = incorrectFeedback[pageIndex];
    
                for (const pattern in incorrectMessages) {
                    if (pattern === userAnswer) {
                        feedback.className = 'feedback show incorrect';
                        feedback.innerHTML = incorrectMessages[pattern];
                        return;
                    }
    
                    if (pattern.includes('*')) {
                        const regexPattern = '^' + pattern.replace(/\*/g, '.*') + '$';
                        const regex = new RegExp(regexPattern);
                        if (regex.test(userAnswer)) {
                            feedback.className = 'feedback show incorrect';
                            feedback.innerHTML = incorrectMessages[pattern];
                            return;
                        }
                    }
                }
    
                const defaultMessage = incorrectMessages['default'];
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = defaultMessage || '❌ <strong>Niepoprawne rozwiązanie.</strong> Spróbuj ponownie!';
            }
        }
    
        function checkCurrentPageSolution(pageIndex) {
            const solution = correctSolutions[pageIndex];
            for (let i = 0; i < solution.length; i++) {
                if (slots[i] !== solution[i]) {
                    return false;
                }
            }
            return true;
        }
    
        function resetTask() {
            slots.fill('');
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const zones = activePage.querySelectorAll('.drop-zone');
            for (let i = 0; i < zones.length; i++) {
                zones[i].textContent = '';
                zones[i].classList.remove('filled');
            }
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                chips[i].classList.remove('used');
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function showPage(pageNumber) {
            const pages = document.querySelectorAll('.page');
            for (let i = 0; i < pages.length; i++) {
                pages[i].classList.remove('active');
            }
    
            for (let i = 0; i < pages.length; i++) {
                if (parseInt(pages[i].getAttribute('data-page')) === pageNumber) {
                    pages[i].classList.add('active');
                    break;
                }
            }
    
            currentPage = pageNumber;
            const pageIndex = currentPage - 1;
            document.getElementById('currentPage').textContent = currentPage;
    
            document.getElementById('prevBtn').disabled = (currentPage === 1);
            document.getElementById('nextBtn').disabled = (currentPage === totalPages);
    
            slots = new Array(slotsPerPage[pageIndex]).fill('');
    
            resetTask();
        }
    
        function nextPage() {
            if (currentPage < totalPages) {
                showPage(currentPage + 1);
            }
        }
    
        function prevPage() {
            if (currentPage > 1) {
                showPage(currentPage - 1);
            }
        }
    
        document.addEventListener('DOMContentLoaded', function() {
            showPage(1);
        });
</script>

</body>
</html>

"
```
            lineageTag: 255d367a-d2e5-41b6-b851-d24697d50c4d

        measure '06a. Quiz' = ```
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
                background: #e5e5e5;
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
                background: #6b1718;
            }
    
            .check-button:hover:not(:disabled) {
                background: #380c0c;
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
            <p><strong>Co zwraca funkcja `SUMMARIZECOLUMNS`?</strong></p>
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
            <p><strong>Jaka jest podstawowa składnia `SUMMARIZECOLUMNS`?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) SUMMARIZECOLUMNS(kolumna1, kolumna2, miara1, miara2)`
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) SUMMARIZECOLUMNS(tabela, kolumny, miary)
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) SUMMARIZECOLUMNS(kolumna1, kolumna2, ´Nazwa´, miara)
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
            <p><strong>Dlaczego `SUMMARIZE` jest uznawana za legacy (przestarzałą)?</strong></p>
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
            <p><strong>Czy w `SUMMARIZECOLUMNS` możesz dodać wiele miar?</strong></p>
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
            <p><strong>Do czego służy funkcja `ADDCOLUMNS`?</strong></p>
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
            <p><strong>Jaki jest wynik: `SUMMARIZECOLUMNS(Produkty[Kategoria], ´Suma´, [Sprzedaż])`?</strong></p>
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
        '`SUMMARIZECOLUMNS` to nowoczesne podejście zalecane przez Microsoft. Jest bardziej wydajna i łatwiejsza w użyciu niż legacy `SUMMARIZE`.',
        '`SUMMARIZECOLUMNS` zwraca tabelę zawierającą unikalne kombinacje wartości z wybranych kolumn oraz opcjonalnie obliczone agregacje dla każdej kombinacji.',
        'Składnia to: `SUMMARIZECOLUMNS(kolumna1, kolumna2, ..., ´Nazwa Miary´, [Wyrażenie], ...).` Najpierw kolumny grupujące, potem pary: nazwa i wyrażenie miary.',
        '`SUMMARIZE` ma nieoczywistą składnię i może dawać nieoczekiwane wyniki. `SUMMARIZECOLUMNS` jest szybsza, bardziej czytelna i zalecana przez Microsoft.',
        '`SUMMARIZECOLUMNS` może zawierać dowolną liczbę miar. Każda miara to para: `´Nazwa Miary´, [Wyrażenie Miary].`',
        '`ADDCOLUMNS` przyjmuje tabelę i dodaje do niej nowe kolumny kalkulowane. Składnia: `ADDCOLUMNS(tabela, ´Nowa Kolumna´, [Wyrażenie], ...)`.',
        'Funkcja zwróci tabelę z kolumną Kategoria (unikalne wartości) oraz kolumną Suma (sprzedaż zagregowana dla każdej kategorii).'
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
            lineageTag: 1d7a0726-1cdb-4f57-a87f-7f959bf90772

        measure '07. Iteratory - AVERAGEX' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>AVERAGEX</title>
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

<div class='container' id='viz_b6a01ed1'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_b6a01ed1' onclick='changePage_b6a01ed1(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_b6a01ed1'>1</span> z <span id='totalPages_b6a01ed1'>1</span>
        </span>
        <button id='nextBtn_b6a01ed1' onclick='changePage_b6a01ed1(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1><code>AVERAGEX</code> – Średnia z iteracją</h1>
        <p><code>AVERAGEX</code> jest szczególnie przydatna, gdy potrzebujesz średniej z obliczeń, a nie z gotowej kolumny. Zwróć uwagę na kluczową różnicę: AVERAGE(Sprzedaz[Marża]) obliczyłaby średnią z kolumny Marża (gdyby taka istniała), ale AVERAGEX pozwala obliczyć marżę dla każdego wiersza osobno, a dopiero potem uśrednić wyniki.</p>
        <pre><code>DAX
        <span class='dax-function'>AVERAGEX</span>(&lt;tabela&gt;, &lt;wyrażenie&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Średnia Marża = 
        <span class='dax-function'>AVERAGEX</span>(
            Sprzedaz,
            Sprzedaz[Wartość Netto] - Sprzedaz[Koszty Netto]
        )</code></pre>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'b6a01ed1';
    var containerId = 'viz_' + vizId;

    var currentPage_b6a01ed1 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_b6a01ed1'] = function(n) {
        if (n > totalPages) currentPage_b6a01ed1 = totalPages;
        if (n < 1) currentPage_b6a01ed1 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_b6a01ed1 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_b6a01ed1;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_b6a01ed1 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_b6a01ed1 === totalPages);
    };

    window['changePage_b6a01ed1'] = function(n) {
        currentPage_b6a01ed1 += n;
        window['showPage_b6a01ed1'](currentPage_b6a01ed1);
    };

    // Inicjalizacja
    window['showPage_b6a01ed1'](1);

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
            lineageTag: b5e86ed1-00a4-4733-b13f-21fc39235b51

        measure '07. Iteratory - COUNTX' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>COUNTX</title>
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

<div class='container' id='viz_ecdfcde9'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_ecdfcde9' onclick='changePage_ecdfcde9(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_ecdfcde9'>1</span> z <span id='totalPages_ecdfcde9'>1</span>
        </span>
        <button id='nextBtn_ecdfcde9' onclick='changePage_ecdfcde9(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1><code>COUNTX</code> – Liczenie z iteracją</h1>
        <p><code>COUNTX</code> różni się od <code>COUNT</code> tym, że możesz w niej zdefiniować warunek dla każdego wiersza. W przykładzie powyżej funkcja <code>IF</code> zwraca 1 lub <code>BLANK()</code> - <code>COUNTX</code> policzy tylko te wiersze, gdzie dostała wartość (nie <code>BLANK</code>). To pozwala na warunkowe liczenie bez używania <code>CALCULATE</code>.</p>
        <pre><code>DAX
        <span class='dax-function'>COUNTX</span>(&lt;tabela&gt;, &lt;wyrażenie&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <p>Liczy ile razy wyrażenie zwróciło <strong>niepustą wartość</strong>.</p>
        <pre><code>DAX
        Liczba Zamówień Powyżej <span class='dax-number'>1000</span> = 
        <span class='dax-function'>COUNTX</span>(
            Sprzedaz,
            <span class='dax-function'>IF</span>(Sprzedaz[Wartość Netto] &gt; <span class='dax-number'>1000</span>, <span class='dax-number'>1</span>, <span class='dax-function'>BLANK</span>())
        )</code></pre>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'ecdfcde9';
    var containerId = 'viz_' + vizId;

    var currentPage_ecdfcde9 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_ecdfcde9'] = function(n) {
        if (n > totalPages) currentPage_ecdfcde9 = totalPages;
        if (n < 1) currentPage_ecdfcde9 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_ecdfcde9 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_ecdfcde9;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_ecdfcde9 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_ecdfcde9 === totalPages);
    };

    window['changePage_ecdfcde9'] = function(n) {
        currentPage_ecdfcde9 += n;
        window['showPage_ecdfcde9'](currentPage_ecdfcde9);
    };

    // Inicjalizacja
    window['showPage_ecdfcde9'](1);

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
            lineageTag: a73fa168-373f-4251-a8a5-69e80da4a1aa

        measure '07. Iteratory - Funkcje iteracyjne (X-functions)' = ```
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
            Strona <span id='currentPage_6b285173'>1</span> z <span id='totalPages_6b285173'>2</span>
        </span>
        <button id='nextBtn_6b285173' onclick='changePage_6b285173(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Po co funkcje iteracyjne?</h1>
        <p>W Power BI często potrzebujemy wykonać obliczenia, które wymagają połączenia danych z różnych kolumn w tym samym wierszu. </p>
        <ul>
        <li><strong>Na przykład:</strong> chcemy obliczyć wartość sprzedaży mnożąc cenę przez ilość, albo marżę odejmując koszt od przychodu.</li>
        <li>Standardowe funkcje jak <code>SUM</code> czy <code>AVERAGE</code> tego nie potrafią - one po prostu sumują gotowe wartości z jednej kolumny. </li>
        <li>Dlatego DAX oferuje funkcje iteracyjne (X-functions), które potrafią 'przejść' przez każdy wiersz tabeli i wykonać dla niego własne obliczenie.</li>
        </ul>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Kluczowe wnioski</h1>
        <p>Funkcje iteracyjne przechodzą przez <strong>każdy wiersz tabeli</strong> i wykonują obliczenia dla każdego wiersza osobno.</p>
        <p><strong>Funkcje iteracyjne (<code>SUMX</code>, <code>AVERAGEX</code>):</strong></p>
        <ul>
        <li>Obliczają wyrażenie dla <strong>każdego wiersza</strong> osobno</li>
        <li>Dopiero potem wykonują agregację (sumę, średnią itp.)</li>
        </ul>
        <p><strong>Zwykłe funkcje agregujące (<code>SUM</code>, <code>AVERAGE</code>):</strong></p>
        <ul>
        <li>Najpierw sumują kolumnę</li>
        <li>Nie pozwalają na obliczenia wiersz po wierszu</li>
        </ul>
        <p>💡 <strong>Kiedy używać X-funkcji?</strong></p>
        <ul>
        <li>Gdy musisz <strong>pomnożyć/podzielić/dodać</strong> wartości z różnych kolumn w tym samym wierszu</li>
        <li>Gdy potrzebujesz <strong>warunkowych obliczeń</strong> dla każdego wiersza</li>
        <li>Gdy standardowa <code>SUM</code>/<code>AVERAGE</code> nie wystarcza</li>
        </ul>
        <p>---</p>

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
            lineageTag: b05536d0-17ae-460a-b5ed-e06633113e4c

        measure '07. Iteratory - MINX i MAXX' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>MINX i MAXX</title>
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

<div class='container' id='viz_df511ecb'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_df511ecb' onclick='changePage_df511ecb(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_df511ecb'>1</span> z <span id='totalPages_df511ecb'>1</span>
        </span>
        <button id='nextBtn_df511ecb' onclick='changePage_df511ecb(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1><code>MINX</code> i <code>MAXX</code> – Minimum i maksimum z iteracją</h1>
        <p>MINX i MAXX są często niedoceniane, ale potrafią rozwiązać problemy, z którymi zwykłe MIN i MAX sobie nie poradzą. Kluczowa różnica: MIN i MAX mogą znaleźć tylko najmniejszą lub największą wartość z gotowej kolumny. MINX i MAXX potrafią znaleźć ekstremalną wartość z obliczeń wykonanych dla każdego wiersza.</p>
        <pre><code>DAX
        <span class='dax-function'>MINX</span>(&lt;tabela&gt;, &lt;wyrażenie&gt;)
        <span class='dax-function'>MAXX</span>(&lt;tabela&gt;, &lt;wyrażenie&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>DAX
        Najwyższa Marża = 
        <span class='dax-function'>MAXX</span>(
            Sprzedaz,
            Sprzedaz[Wartość Netto] - Sprzedaz[Koszty Netto]
        )</code></pre>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'df511ecb';
    var containerId = 'viz_' + vizId;

    var currentPage_df511ecb = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_df511ecb'] = function(n) {
        if (n > totalPages) currentPage_df511ecb = totalPages;
        if (n < 1) currentPage_df511ecb = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_df511ecb - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_df511ecb;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_df511ecb === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_df511ecb === totalPages);
    };

    window['changePage_df511ecb'] = function(n) {
        currentPage_df511ecb += n;
        window['showPage_df511ecb'](currentPage_df511ecb);
    };

    // Inicjalizacja
    window['showPage_df511ecb'](1);

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
            lineageTag: 925b286f-b6ee-4736-9ced-f67122f05a2d

        measure '07. Iteratory - SUMX' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>SUMX</title>
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

<div class='container' id='viz_1f36501d'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_1f36501d' onclick='changePage_1f36501d(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_1f36501d'>1</span> z <span id='totalPages_1f36501d'>3</span>
        </span>
        <button id='nextBtn_1f36501d' onclick='changePage_1f36501d(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Jak działa SUMX?</h1>
        <p>SUMX iteruje po wierszach, więc poniższa funkcja kolejno</p>
        <ul>
        <li>Przemnoży <code>ilość </code> i <code>Cenę</code> - wynikiem będzie <code>Wartość Netto</code></li>
        <li>Zsumuje <code>Wartości Netto</code>, zależnie od kontekstu</li>
        </ul>
        <pre><code>DAX
        Wartość Zamówień = <span class='dax-function'>SUMX</span>(Sprzedaz, Sprzedaz[Cena] * Sprzedaz[Ilość])</code></pre>
        <h2>Proces iteracyjny krok po kroku:</h2>
        <table>
          <thead>
            <tr>
              <th>Iteracja</th>
              <th>KATEGORIA</th>
              <th>Cena</th>
              <th>Ilość</th>
              <th>Obliczenie (Cena × Ilość)</th>
              <th>Wynik wiersza</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>NAPOJE</td>
              <td>3000</td>
              <td>2</td>
              <td>3000 × 2</td>
              <td>6000</td>
            </tr>
            <tr>
              <td>2</td>
              <td>WINO</td>
              <td>50</td>
              <td>10</td>
              <td>50 × 10</td>
              <td>500</td>
            </tr>
            <tr>
              <td>3</td>
              <td>KULINARKA</td>
              <td>150</td>
              <td>5</td>
              <td>150 × 5</td>
              <td>750</td>
            </tr>
            <tr>
              <td>4</td>
              <td>PRZEKĄSKI</td>
              <td>800</td>
              <td>3</td>
              <td>800 × 3</td>
              <td>2400</td>
            </tr>
            <tr>
              <td><strong>SUMA</strong></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td><strong>9650</strong></td>
            </tr>
          </tbody>
        </table>
        <p><strong>Wynik końcowy:</strong> 9650 PLN</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Porównanie: <code>SUMX</code> vs zwykła <code>SUM</code></h1>
        <h2>❌ To NIE zadziała poprawnie:</h2>
        <pre><code>DAX
        Błędna Wartość = <span class='dax-function'>SUM</span>(Sprzedaz[Cena]) * <span class='dax-function'>SUM</span>(Sprzedaz[Ilość])</code></pre>
        <ul>
        <li>SUM(Cena) = 3000 + 50 + 150 + 800 = <strong>4000</strong></li>
        <li>SUM(Ilość) = 2 + 10 + 5 + 3 = <strong>20</strong></li>
        <li>Wynik: 4000 × 20 = <strong>80 000</strong> ❌ (Błędny!)</li>
        </ul>
        <h2>✅ To działa poprawnie:</h2>
        <pre><code>DAX
        Poprawna Wartość = <span class='dax-function'>SUMX</span>(Sprzedaz, Sprzedaz[Cena] * Sprzedaz[Ilość])</code></pre>
        <ul>
        <li>Wynik: <strong>9650</strong> ✅ (Poprawny!)</li>
        </ul>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>Ważna uwaga:</h1>
        <p><strong>Nie używaj X-funkcji tam, gdzie wystarczy zwykła agregacja.</strong> </p>
        <p>Jeśli po prostu chcesz zsumować wartości z jednej kolumny, użyj <code>SUM</code> - będzie znacznie szybsza. <code>X</code>-funkcje uruchamiaj się tylko wtedy, gdy musisz coś obliczyć <strong>w locie</strong> dla każdego wiersza. Każda niepotrzebna iteracja spowalnia raport.</p>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '1f36501d';
    var containerId = 'viz_' + vizId;

    var currentPage_1f36501d = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_1f36501d'] = function(n) {
        if (n > totalPages) currentPage_1f36501d = totalPages;
        if (n < 1) currentPage_1f36501d = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_1f36501d - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_1f36501d;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_1f36501d === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_1f36501d === totalPages);
    };

    window['changePage_1f36501d'] = function(n) {
        currentPage_1f36501d += n;
        window['showPage_1f36501d'](currentPage_1f36501d);
    };

    // Inicjalizacja
    window['showPage_1f36501d'](1);

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
            lineageTag: ffffd718-1ba9-4571-891c-69c929b5b71d

        measure '07a. Gaps' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DAX Gaps</title>
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #333;
        background: transparent;
        padding: 20px;
    }
    
    .container {
        max-width: 900px;
        margin: 0 auto;
        background: transparent;
        padding: 40px;
    }
    
    h3 {
        font-size: 26px;
        line-height: 36px;
        font-weight: 600;
        padding-top: 14px;
        padding-bottom: 6px;
        margin-bottom: 1em;
        color: #6b1718;
        border-bottom: 2px solid #6b1718;
    }
    
    .task-description {
        font-size: 1.1em;
        margin: 20px 0;
    }
    
    .code-container {
        background: #f8f9fa;
        border: 2px solid #e1e4e8;
        border-radius: 6px;
        padding: 25px;
        margin: 30px 0;
        font-family: 'Courier New', monospace;
        font-size: 1.05em;
        line-height: 1.8;
    }
    
    .drop-zone {
        display: inline-block;
        min-width: 180px;
        height: 36px;
        background: white;
        border: 2px dashed #6b1718;
        border-radius: 4px;
        padding: 6px 12px;
        margin: 0 4px;
        vertical-align: middle;
        text-align: center;
        transition: all 0.2s;
    }
    
    .drop-zone.drag-over {
        background: #ffe6e6;
        border-color: #380c0c;
    }
    
    .drop-zone.filled {
        background: #d4edda;
        border: 2px solid #28a745;
        border-style: solid;
    }
    
    .functions-title {
        font-size: 1em;
        margin: 30px 0 15px 0;
        color: #333;
    }
    
    .function-chip {
        display: inline-block;
        background: #6b1718;
        color: white;
        padding: 10px 20px;
        margin: 8px;
        border-radius: 20px;
        cursor: grab;
        font-family: 'Courier New', monospace;
        font-size: 1em;
        font-weight: 500;
        transition: all 0.2s;
        user-select: none;
    }
    
    .function-chip:hover {
        background: #380c0c;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(107, 23, 24, 0.3);
    }
    
    .function-chip:active {
        cursor: grabbing;
    }
    
    .function-chip.used {
        opacity: 0.3;
        cursor: not-allowed;
        pointer-events: none;
    }
    
    .button-group {
        margin-top: 30px;
        display: flex;
        gap: 15px;
        align-items: center;
    }
    
    button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 14px 32px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.05em;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    button:hover {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    button.reset-btn {
        background: #6b1718;
        padding: 8px 16px;
        font-size: 0.9em;
    }
    
    button.reset-btn:hover {
        background: #380c0c;
    }
    
    .feedback {
        margin-top: 25px;
        padding: 20px;
        border-radius: 6px;
        display: none;
        font-size: 1.05em;
    }
    
    .feedback.show {
        display: block;
        animation: slideDown 0.3s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .feedback.correct {
        background: #d4edda;
        border-left: 4px solid #28a745;
        color: #155724;
    }
    
    .feedback.incorrect {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        color: #721c24;
    }
    
    .hint-box {
        background: #fafafa;
        border-left: 4px solid #ccc;
        padding: 15px;
        margin: 20px 0;
        border-radius: 4px;
        color: #121212;
        font-size: 0.95em;
    }
    .pagination {
        display: flex;
        align-items: center;
        justify-content: space-between; 
        gap: 20px;
        margin: 30px auto; 
        padding: 20px;
        border-radius: 6px;
    	max-width: 900px;
        border-bottom: 1px solid #e0e0e0;
        width: 100%;
    }
    
    .page-info {
        font-weight: 600;
        color: #666666; 
    }
    
    .nav-button {
        background: #6b1718;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1em;
        transition: all 0.2s;
    }
    
    .nav-button:hover:not(:disabled) {
        background: #380c0c;
        transform: translateY(-1px);
    }
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .nav-button:disabled {
        background: #ccc;
        cursor: not-allowed;
        opacity: 0.5;
    }
    
    
    .page {
        display: none;
    }
    
    .page.active {
        display: block;
    }
    </style>
</head>
<body>

<div class='pagination'>
    <button class='nav-button' id='prevBtn' onclick='prevPage()'>← Poprzednie</button>
    <span class='page-info'>Zadanie <span id='currentPage'>1</span> z <span id='totalPages'>3</span></span>
    <button class='nav-button' id='nextBtn' onclick='nextPage()'>Następne →</button>
</div>

<div class='page active' data-page='1'>
<div class='container'>
    <div class='task-description'>
        <h3>Podstawowa składnia SUMX</h3>
        Które funkcje poprawnie uzupełniają składnię funkcji iteracyjnej obliczającej całkowitą wartość sprzedaży?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUM'>SUM</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUMX'>SUMX</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CALCULATE'>CALCULATE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='FILTER'>FILTER</span>
    </div>

    <div class='code-container'>
        <div>Wartosc Sprzedazy = </div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(</div>
        <div>        Sprzedaz,</div>
        <div>        Sprzedaz[Cena] * Sprzedaz[Ilosc]</div>
        <div>    )</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Funkcje iteracyjne w DAX kończą się literą `X`. Szukaj funkcji, która najpierw mnoży wartości w każdym wierszu, a potem je sumuje.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='2'>
<div class='container'>
    <div class='task-description'>
        <h3>Obliczanie marży z AVERAGEX</h3>
        Która funkcja pozwoli obliczyć średnią marżę dla każdego wiersza transakcji?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='AVERAGE'>AVERAGE</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='AVERAGEX'>AVERAGEX</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='SUMX'>SUMX</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='CALCULATE'>CALCULATE</span>
    </div>

    <div class='code-container'>
        <div>Srednia Marza = </div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(</div>
        <div>        Sprzedaz,</div>
        <div>        Sprzedaz[Wartosc Netto] - Sprzedaz[Koszty Netto]</div>
        <div>    )</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Potrzebujesz funkcji iteracyjnej, która obliczy różnicę dla każdego wiersza, a następnie zwróci średnią arytmetyczną tych wartości.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<div class='page' data-page='3'>
<div class='container'>
    <div class='task-description'>
        <h3>Warunkowe liczenie z COUNTX</h3>
        Która funkcja pozwoli policzyć zamówienia powyżej 1000 PLN wykonując sprawdzenie dla każdego wiersza?
    </div>

    <div>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='COUNT'>COUNT</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='COUNTX'>COUNTX</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='Sprzedaz'>Sprzedaz</span>
        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='COUNTROWS'>COUNTROWS</span>
    </div>

    <div class='code-container'>
        <div>Liczba Duzych Zamowien = </div>
        <div>    <div class='drop-zone' data-slot='0' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>(</div>
        <div>        <div class='drop-zone' data-slot='1' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>,</div>
        <div>        IF(Sprzedaz[Wartosc Netto] > 1000, 1, BLANK())</div>
        <div>    )</div>
    </div>

    <div class='button-group'>
        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>
        <button class='reset-btn' onclick='resetTask()'>Reset</button>
    </div>

    <div class='hint-box'>
        Potrzebujesz funkcji iteracyjnej, która liczy ile razy wyrażenie zwróciło niepustą wartość. Funkcja ta kończy się literą `X` i zaczyna od `COUNT`.
    </div>

    <div class='feedback' id='feedback'></div>
</div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 3;
    const slotsPerPage = [1, 1, 2];
    let slots = new Array(slotsPerPage[0]).fill('');
    const correctSolutions = [['SUMX'], ['AVERAGEX'], ['COUNTX', 'Sprzedaz']];
    const correctFeedback = ['\u2705Brawo! `SUMX` to funkcja iteracyjna, kt\u00f3ra przechodzi przez ka\u017cdy wiersz tabeli Sprzeda\u017c, mno\u017cy Cen\u0119 przez Ilo\u015b\u0107 dla ka\u017cdego wiersza osobno, a nast\u0119pnie sumuje wszystkie wyniki.', '\u2705Brawo! `AVERAGEX` iteruje przez ka\u017cdy wiersz tabeli Sprzeda\u017c, oblicza mar\u017c\u0119 dla ka\u017cdej transakcji odejmuj\u0105c Koszty od Warto\u015bci Netto, a nast\u0119pnie oblicza \u015bredni\u0105 z wszystkich wynik\u00f3w.', '\u2705Brawo! `COUNTX` iteruje przez ka\u017cdy wiersz tabeli Sprzeda\u017c, sprawdza warunek dla ka\u017cdego wiersza osobno i liczy ile razy wyra\u017cenie zwr\u00f3ci\u0142o niepust\u0105 warto\u015b\u0107. Gdy Warto\u015b\u0107 Netto przekracza 1000, funkcja IF zwraca 1, kt\u00f3re jest liczone.'];
    const incorrectFeedback = [{}, {}, {}];

    function drag(event) {
            event.dataTransfer.setData('function', event.target.getAttribute('data-function'));
        }
    
        function allowDrop(event) {
            event.preventDefault();
            event.target.classList.add('drag-over');
        }
    
        function dragLeave(event) {
            event.target.classList.remove('drag-over');
        }
    
        function drop(event) {
            event.preventDefault();
            event.target.classList.remove('drag-over');
    
            const functionName = event.dataTransfer.getData('function');
            const slotIndex = parseInt(event.target.getAttribute('data-slot'));
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            if (slots[slotIndex]) {
                const chips = activePage.querySelectorAll('.function-chip');
                for (let i = 0; i < chips.length; i++) {
                    if (chips[i].getAttribute('data-function') === slots[slotIndex]) {
                        chips[i].classList.remove('used');
                        break;
                    }
                }
            }
    
            slots[slotIndex] = functionName;
            event.target.textContent = functionName;
            event.target.classList.add('filled');
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                if (chips[i].getAttribute('data-function') === functionName) {
                    chips[i].classList.add('used');
                    break;
                }
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function checkSolution() {
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const feedback = activePage.querySelector('.feedback');
            if (!feedback) return;
    
            if (slots.includes('')) {
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = 'Niekompletne! Musisz wypełnić wszystkie miejsca w kodzie.';
                return;
            }
    
            const currentPageNum = parseInt(activePage.getAttribute('data-page'));
            const pageIndex = currentPageNum - 1;
            const isCorrect = checkCurrentPageSolution(pageIndex);
    
            if (isCorrect) {
                feedback.className = 'feedback show correct';
                feedback.innerHTML = correctFeedback[pageIndex];
            } else {
                const userAnswer = slots.join(',');
                const incorrectMessages = incorrectFeedback[pageIndex];
    
                for (const pattern in incorrectMessages) {
                    if (pattern === userAnswer) {
                        feedback.className = 'feedback show incorrect';
                        feedback.innerHTML = incorrectMessages[pattern];
                        return;
                    }
    
                    if (pattern.includes('*')) {
                        const regexPattern = '^' + pattern.replace(/\*/g, '.*') + '$';
                        const regex = new RegExp(regexPattern);
                        if (regex.test(userAnswer)) {
                            feedback.className = 'feedback show incorrect';
                            feedback.innerHTML = incorrectMessages[pattern];
                            return;
                        }
                    }
                }
    
                const defaultMessage = incorrectMessages['default'];
                feedback.className = 'feedback show incorrect';
                feedback.innerHTML = defaultMessage || '❌ <strong>Niepoprawne rozwiązanie.</strong> Spróbuj ponownie!';
            }
        }
    
        function checkCurrentPageSolution(pageIndex) {
            const solution = correctSolutions[pageIndex];
            for (let i = 0; i < solution.length; i++) {
                if (slots[i] !== solution[i]) {
                    return false;
                }
            }
            return true;
        }
    
        function resetTask() {
            slots.fill('');
    
            const activePage = document.querySelector('.page.active');
            if (!activePage) return;
    
            const zones = activePage.querySelectorAll('.drop-zone');
            for (let i = 0; i < zones.length; i++) {
                zones[i].textContent = '';
                zones[i].classList.remove('filled');
            }
    
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                chips[i].classList.remove('used');
            }
    
            const feedback = activePage.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }
    
        function showPage(pageNumber) {
            const pages = document.querySelectorAll('.page');
            for (let i = 0; i < pages.length; i++) {
                pages[i].classList.remove('active');
            }
    
            for (let i = 0; i < pages.length; i++) {
                if (parseInt(pages[i].getAttribute('data-page')) === pageNumber) {
                    pages[i].classList.add('active');
                    break;
                }
            }
    
            currentPage = pageNumber;
            const pageIndex = currentPage - 1;
            document.getElementById('currentPage').textContent = currentPage;
    
            document.getElementById('prevBtn').disabled = (currentPage === 1);
            document.getElementById('nextBtn').disabled = (currentPage === totalPages);
    
            slots = new Array(slotsPerPage[pageIndex]).fill('');
    
            resetTask();
        }
    
        function nextPage() {
            if (currentPage < totalPages) {
                showPage(currentPage + 1);
            }
        }
    
        function prevPage() {
            if (currentPage > 1) {
                showPage(currentPage - 1);
            }
        }
    
        document.addEventListener('DOMContentLoaded', function() {
            showPage(1);
        });
</script>

</body>
</html>

"
```
            lineageTag: 8d2c5742-6f0c-4db1-bc84-2622d4fc4676

        measure '07a. Quiz' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Funkcje iteracyjne w DAX</title>
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
                background: #e5e5e5;
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
                background: #6b1718;
            }
    
            .check-button:hover:not(:disabled) {
                background: #380c0c;
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
            <p><strong>Co jest kluczową cechą funkcji iteracyjnych takich jak `SUMX` czy `AVERAGEX`?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(0, 0)'>
                A) Najpierw sumują całą kolumnę, a potem wykonują obliczenia
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 1)'>
                B) Wykonują obliczenia dla każdego wiersza tabeli osobno, a następnie agregują wyniki
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 2)'>
                C) Działają tylko na kolumnach liczbowych
            </div>
            <div class='answer-option' onclick='selectAnswer(0, 3)'>
                D) Nie wymagają podania nazwy tabeli jako pierwszego argumentu
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(0, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-0'></div>
    </div>

    <!-- Pytanie 2 -->
    <div class='page'>
        <h1>Pytanie 2</h1>
        <div class='question-box'>
            <p><strong>Dlaczego wzór `SUM(Sprzedaz[Cena]) * SUM(Sprzedaz[Ilość])` daje błędny wynik dla obliczenia wartości zamówień?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(1, 0)'>
                A) Funkcja `SUM` nie obsługuje mnożenia
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 1)'>
                B) Brakuje kontekstu filtra w formule
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 2)'>
                C) Funkcja sumuje osobno ceny i ilości, a następnie mnoży sumy zamiast mnożyć wartości w każdym wierszu
            </div>
            <div class='answer-option' onclick='selectAnswer(1, 3)'>
                D) Należy użyć funkcji `CALCULATE` zamiast `SUM`
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(1, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-1'></div>
    </div>

    <!-- Pytanie 3 -->
    <div class='page'>
        <h1>Pytanie 3</h1>
        <div class='question-box'>
            <p><strong>Którą funkcję należy użyć do obliczenia średniej marży, gdy marża jest różnicą między Wartość Netto a Koszty Netto dla każdego wiersza?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(2, 0)'>
                A) `AVERAGE(Sprzedaz[Wartość Netto] - Sprzedaz[Koszty Netto])`
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 1)'>
                B) `AVERAGEX(Sprzedaz, Sprzedaz[Wartość Netto] - Sprzedaz[Koszty Netto])`
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 2)'>
                C) `SUMX(Sprzedaz, Sprzedaz[Wartość Netto] - Sprzedaz[Koszty Netto]) / COUNT(Sprzedaz[Wartość Netto])`
            </div>
            <div class='answer-option' onclick='selectAnswer(2, 3)'>
                D) `CALCULATE(AVERAGE(Sprzedaz[Wartość Netto] - Sprzedaz[Koszty Netto]))`
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(2, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-2'></div>
    </div>

    <!-- Pytanie 4 -->
    <div class='page'>
        <h1>Pytanie 4</h1>
        <div class='question-box'>
            <p><strong>W jakim przypadku powinieneś użyć funkcji iteracyjnej zamiast zwykłej funkcji agregującej?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(3, 0)'>
                A) Gdy chcesz policzyć sumę wartości z pojedynczej kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 1)'>
                B) Gdy musisz pomnożyć lub podzielić wartości z różnych kolumn w tym samym wierszu
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 2)'>
                C) Gdy potrzebujesz policzyć średnią z jednej kolumny
            </div>
            <div class='answer-option' onclick='selectAnswer(3, 3)'>
                D) Gdy chcesz znaleźć maksymalną wartość w kolumnie
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(3, 1)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-3'></div>
    </div>

    <!-- Pytanie 5 -->
    <div class='page'>
        <h1>Pytanie 5</h1>
        <div class='question-box'>
            <p><strong>Co zwróci funkcja `COUNTX(Sprzedaz, IF(Sprzedaz[Wartość Netto] &gt; 1000, 1, BLANK()))`?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(4, 0)'>
                A) Sumę wartości wszystkich zamówień powyżej 1000
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 1)'>
                B) Liczbę wierszy w tabeli `Sprzedaz`
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 2)'>
                C) Liczbę zamówień, których Wartość Netto przekracza 1000
            </div>
            <div class='answer-option' onclick='selectAnswer(4, 3)'>
                D) Wartość logiczną `TRUE` lub `FALSE`
            </div>
        </div>
        <button class='check-button' onclick='checkAnswer(4, 2)'>Sprawdź odpowiedź</button>
        <div class='feedback' id='feedback-4'></div>
    </div>

    <!-- Pytanie 6 -->
    <div class='page'>
        <h1>Pytanie 6</h1>
        <div class='question-box'>
            <p><strong>Jaka jest różnica między MAXX a zwykłą funkcją MAX?</strong></p>
        </div>
        <div class='answers'>
            <div class='answer-option' onclick='selectAnswer(5, 0)'>
                A) MAXX działa szybciej niż MAX
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 1)'>
                B) MAXX pozwala na obliczenie wyrażenia dla każdego wiersza przed znalezieniem maksimum, a MAX działa tylko na pojedynczej kolumnie
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 2)'>
                C) MAX zwraca wartość tekstową, a MAXX wartość liczbową
            </div>
            <div class='answer-option' onclick='selectAnswer(5, 3)'>
                D) MAXX wymaga użycia funkcji CALCULATE
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
    
    const correctAnswers = [1, 2, 1, 1, 2, 1];
    
    const explanations = [
        'Funkcje iteracyjne przechodzą przez każdy wiersz tabeli i wykonują obliczenia dla każdego wiersza osobno, a dopiero potem wykonują agregację. To odróżnia je od zwykłych funkcji agregujących.',
        '',
        '`AVERAGEX` iteruje przez każdy wiersz tabeli Sprzedaz, oblicza różnicę między Wartość Netto a Koszty Netto dla każdego wiersza, a następnie wyznacza średnią z tych wartości. Zwykła funkcja `AVERAGE` nie pozwala na takie obliczenia wiersz po wierszu.',
        'Funkcje iteracyjne są niezbędne gdy musisz wykonać obliczenia łączące wartości z różnych kolumn w tym samym wierszu, np. pomnożyć cenę przez ilość. Zwykłe funkcje agregujące nie pozwalają na takie operacje wiersz po wierszu.',
        '`COUNTX` iteruje przez wiersze tabeli `Sprzedaz` i liczy ile razy wyrażenie zwróciło niepustą wartość. Funkcja `IF` zwraca 1 gdy `Wartość Netto` jest większa niż 1000, w przeciwnym razie zwraca `BLANK`. W efekcie `COUNTX` zlicza ile zamówień ma wartość powyżej 1000.',
        'MAXX jest funkcją iteracyjną, która oblicza określone wyrażenie dla każdego wiersza tabeli, a następnie zwraca maksymalną wartość spośród tych obliczeń. MAX natomiast po prostu znajduje największą wartość w pojedynczej kolumnie bez możliwości wykonania obliczeń wiersz po wierszu.'
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
            lineageTag: d85b7b66-c233-4e6f-b168-caf83e5a9cdb

        measure '08. Time Intelligence - DATEADD' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DATEADD</title>
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

<div class='container' id='viz_0f635f43'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_0f635f43' onclick='changePage_0f635f43(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_0f635f43'>1</span> z <span id='totalPages_0f635f43'>3</span>
        </span>
        <button id='nextBtn_0f635f43' onclick='changePage_0f635f43(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Definicja</h1>
        <pre><code><span class='dax-function'>DATEADD</span>(&lt;dates&gt;, &lt;number_of_intervals&gt;, &lt;interval&gt;)</code></pre>
        <p>Przesuwa daty o określoną liczbę <strong>interwałów</strong> (dni, miesięcy, kwartałów, lat). Może przesuwać <strong>wstecz</strong> (wartość ujemna) lub <strong>wprzód</strong> (wartość dodatnia).</p>
        <p><strong>Interwały:</strong> DAY, MONTH, QUARTER, YEAR</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Zastosowanie</h1>
        <p><strong>Tabela źródłowa:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>Wartość</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Grudzien 2023</td>
              <td>1000</td>
            </tr>
            <tr>
              <td>Styczeń 2024</td>
              <td>3000</td>
            </tr>
            <tr>
              <td>Luty 2024</td>
              <td>2400</td>
            </tr>
            <tr>
              <td>Marzec 2024</td>
              <td>1800</td>
            </tr>
          </tbody>
        </table>
        <h2>Przykład 1: Miesiąc do miesiąca (MoM)</h2>
        <pre><code>Sprzedaż Poprzedni Miesiąc = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]),
            <span class='dax-function'>DATEADD</span>(Kalendarz[Data], -<span class='dax-number'>1</span>, MONTH)
        )</code></pre>
        <p><strong>Mapowanie okresów:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>Wartość dla DATEADD(-1, MONTH)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Styczeń 2024</td>
              <td>1000</td>
            </tr>
            <tr>
              <td>Luty 2024</td>
              <td>3000</td>
            </tr>
            <tr>
              <td>Marzec 2024</td>
              <td>2400</td>
            </tr>
            <tr>
              <td>Kwiecień 2024</td>
              <td>1800</td>
            </tr>
          </tbody>
        </table>
        <p><strong>Zmiana MoM:</strong></p>
        <pre><code>Zmiana MoM % = 
        <span class='dax-function'>DIVIDE</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]) - [Sprzedaż Poprzedni Miesiąc],
            [Sprzedaż Poprzedni Miesiąc]
        )</code></pre>
        <table>
          <thead>
            <tr>
              <th>Miesiąc</th>
              <th>Wartość</th>
              <th>Poprzedni</th>
              <th>Zmiana %</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Luty</td>
              <td>2400</td>
              <td>3000</td>
              <td>-20%</td>
            </tr>
            <tr>
              <td>Marzec</td>
              <td>1800</td>
              <td>2400</td>
              <td>-25%</td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Przykład 2: Dokładnie rok temu</h2>
        <pre><code>Sprzedaż Dokładnie Rok Temu = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]),
            <span class='dax-function'>DATEADD</span>(Kalendarz[Data], -<span class='dax-number'>1</span>, YEAR)
        )</code></pre>
        <p><strong>Mapowanie roczne:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Bieżąca data</th>
              <th>DATEADD(-1, YEAR) →</th>
              <th>Wartość rok temu</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2024-01-15</td>
              <td>2023-01-15</td>
              <td>2800</td>
            </tr>
            <tr>
              <td>2024-02-10</td>
              <td>2023-02-10</td>
              <td>2200</td>
            </tr>
            <tr>
              <td>2024-02-29</td>
              <td>2023-02-28</td>
              <td>1900</td>
            </tr>
          </tbody>
        </table>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '0f635f43';
    var containerId = 'viz_' + vizId;

    var currentPage_0f635f43 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_0f635f43'] = function(n) {
        if (n > totalPages) currentPage_0f635f43 = totalPages;
        if (n < 1) currentPage_0f635f43 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_0f635f43 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_0f635f43;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_0f635f43 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_0f635f43 === totalPages);
    };

    window['changePage_0f635f43'] = function(n) {
        currentPage_0f635f43 += n;
        window['showPage_0f635f43'](currentPage_0f635f43);
    };

    // Inicjalizacja
    window['showPage_0f635f43'](1);

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
            lineageTag: 1d37c019-b40f-42aa-af84-9b311eaa9165

        measure '08. Time Intelligence - DATESINPERIOD' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DATESINPERIOD</title>
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

<div class='container' id='viz_a9f5fb4f'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_a9f5fb4f' onclick='changePage_a9f5fb4f(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_a9f5fb4f'>1</span> z <span id='totalPages_a9f5fb4f'>4</span>
        </span>
        <button id='nextBtn_a9f5fb4f' onclick='changePage_a9f5fb4f(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Definicja</h1>
        <pre><code><span class='dax-function'>DATESINPERIOD</span>(&lt;dates&gt;, &lt;start_date&gt;, &lt;number_of_intervals&gt;, &lt;interval&gt;)</code></pre>
        <p>Zwraca <strong>okno przewijane</strong> dat rozpoczynające się od określonej daty i rozciągające się o zadaną liczbę interwałów wstecz lub wprzód.</p>
        <p><strong>Interwały:</strong> DAY, MONTH, QUARTER, YEAR</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Zastosowanie</h1>
        <p><strong>Tabela źródłowa:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>Wartość</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2024-02-08</td>
              <td>600</td>
            </tr>
            <tr>
              <td>2024-02-09</td>
              <td>800</td>
            </tr>
            <tr>
              <td>2024-02-10</td>
              <td>2400</td>
            </tr>
            <tr>
              <td>2024-02-14</td>
              <td>1100</td>
            </tr>
            <tr>
              <td>2024-02-15</td>
              <td>900</td>
            </tr>
          </tbody>
        </table>
        <h2>Przykład 1: Ostatnie 7 dni (Rolling 7 days)</h2>
        <pre><code>Sprzedaż Ostatnie <span class='dax-number'>7</span> Dni = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]),
            <span class='dax-function'>DATESINPERIOD</span>(
                Kalendarz[Data],
                <span class='dax-function'>MAX</span>(Kalendarz[Data]),
                -<span class='dax-number'>7</span>,
                DAY
            )
        )</code></pre>
        <p><strong>Okno przewijane (stan na 2024-02-15):</strong></p>
        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>Wartość</th>
              <th>W oknie 7 dni?</th>
              <th>Kumulacja</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2024-02-07</td>
              <td>500</td>
              <td>❌ >7 dni temu</td>
              <td>-</td>
            </tr>
            <tr>
              <td>2024-02-08</td>
              <td>600</td>
              <td>❌ >7 dni temu</td>
              <td>-</td>
            </tr>
            <tr>
              <td>2024-02-09</td>
              <td>800</td>
              <td>✅ Tak</td>
              <td>800</td>
            </tr>
            <tr>
              <td>2024-02-10</td>
              <td>2400</td>
              <td>✅ Tak</td>
              <td>3200</td>
            </tr>
            <tr>
              <td>2024-02-14</td>
              <td>1100</td>
              <td>✅ Tak</td>
              <td>4300</td>
            </tr>
            <tr>
              <td>2024-02-15</td>
              <td>900</td>
              <td>✅ Tak <strong>← Dziś</strong></td>
              <td><strong>5200</strong></td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Przykład 2: Ostatnie 3 miesiące</h2>
        <pre><code>Sprzedaż Ostatnie 3M = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]),
            <span class='dax-function'>DATESINPERIOD</span>(
                Kalendarz[Data],
                <span class='dax-function'>MAX</span>(Kalendarz[Data]),
                -<span class='dax-number'>3</span>,
                MONTH
            )
        )</code></pre>
        <p><strong>Okno 3 miesięcy (na 15.02.2024):</strong></p>
        <table>
          <thead>
            <tr>
              <th>Miesiąc</th>
              <th>Wartość</th>
              <th>W oknie 3M?</th>
              <th>Kumulacja</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>XI 2023</td>
              <td>4200</td>
              <td>❌</td>
              <td>-</td>
            </tr>
            <tr>
              <td>XII 2023</td>
              <td>5100</td>
              <td>✅</td>
              <td>5100</td>
            </tr>
            <tr>
              <td>I 2024</td>
              <td>6800</td>
              <td>✅</td>
              <td>11900</td>
            </tr>
            <tr>
              <td>II 2024 (do 15)</td>
              <td>4400</td>
              <td>✅</td>
              <td><strong>16300</strong></td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>Przykład 3: Średnia krocząca 30 dni</h2>
        <pre><code>Średnia 30D = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>AVERAGE</span>(fSprzedaz[Wartość]),
            <span class='dax-function'>DATESINPERIOD</span>(
                Kalendarz[Data],
                <span class='dax-function'>MAX</span>(Kalendarz[Data]),
                -<span class='dax-number'>30</span>,
                DAY
            )
        )</code></pre>
        <p><strong>Interpretacja:</strong> Wygładza wahania dzienne, pokazując trend</p>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'a9f5fb4f';
    var containerId = 'viz_' + vizId;

    var currentPage_a9f5fb4f = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_a9f5fb4f'] = function(n) {
        if (n > totalPages) currentPage_a9f5fb4f = totalPages;
        if (n < 1) currentPage_a9f5fb4f = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_a9f5fb4f - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_a9f5fb4f;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_a9f5fb4f === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_a9f5fb4f === totalPages);
    };

    window['changePage_a9f5fb4f'] = function(n) {
        currentPage_a9f5fb4f += n;
        window['showPage_a9f5fb4f'](currentPage_a9f5fb4f);
    };

    // Inicjalizacja
    window['showPage_a9f5fb4f'](1);

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
            lineageTag: 6f077e1d-5097-40ca-9b1e-014530cc8795

        measure '08. Time Intelligence - DATESYTD' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DATESYTD</title>
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

<div class='container' id='viz_21ff4c70'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_21ff4c70' onclick='changePage_21ff4c70(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_21ff4c70'>1</span> z <span id='totalPages_21ff4c70'>3</span>
        </span>
        <button id='nextBtn_21ff4c70' onclick='changePage_21ff4c70(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Definicja</h1>
        <pre><code><span class='dax-function'>DATESYTD</span>(&lt;dates&gt;, [&lt;year_end_date&gt;])</code></pre>
        <p>Zwraca wszystkie daty od <strong>początku roku</strong> do ostatniej daty w bieżącym kontekście filtra. Służy do tworzenia kumulacji rocznej (YTD - Year to Date).</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Zastosowanie</h1>
        <p><strong>Tabela źródłowa:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>Wartość</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2023-12-30</td>
              <td>3000</td>
            </tr>
            <tr>
              <td>2024-01-02</td>
              <td>500</td>
            </tr>
            <tr>
              <td>2024-01-03</td>
              <td>2400</td>
            </tr>
            <tr>
              <td>2024-01-04</td>
              <td>750</td>
            </tr>
            <tr>
              <td>2024-02-05</td>
              <td>100</td>
            </tr>
          </tbody>
        </table>
        <h2>Przykład 1: Sprzedaż YTD</h2>
        <pre><code>Sprzedaż YTD = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]),
            <span class='dax-function'>DATESYTD</span>(Kalendarz[Data])
        )</code></pre>
        <p><strong>Proces kumulacji</strong></p>
        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>Wartość</th>
              <th>W zakresie YTD?</th>
              <th>Kumulacja YTD</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2023-12-30</td>
              <td>3000</td>
              <td>❌ Przeszłość</td>
              <td>0</td>
            </tr>
            <tr>
              <td>2024-01-02</td>
              <td>500</td>
              <td>✅</td>
              <td>500</td>
            </tr>
            <tr>
              <td>2024-01-03</td>
              <td>2400</td>
              <td>✅</td>
              <td>2900</td>
            </tr>
            <tr>
              <td>2024-01-04</td>
              <td>750</td>
              <td>✅</td>
              <td>3650</td>
            </tr>
            <tr>
              <td>2024-01-05</td>
              <td>100</td>
              <td>✅ <strong>← Dziś</strong></td>
              <td><strong>3750</strong></td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Przykład 2: Porównanie bieżący vs poprzedni YTD</h2>
        <pre><code>Różnica YTD vs RR = 
        [Sprzedaż YTD] - [Sprzedaż YTD RR]</code></pre>
        <p><strong>Wyniki:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Data analizy</th>
              <th>YTD bieżący</th>
              <th>YTD rok temu</th>
              <th>Różnica</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>31.01.2024</td>
              <td>3500</td>
              <td>2800</td>
              <td>+700</td>
            </tr>
            <tr>
              <td>29.02.2024</td>
              <td>6650</td>
              <td>5000</td>
              <td>+1650</td>
            </tr>
          </tbody>
        </table>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '21ff4c70';
    var containerId = 'viz_' + vizId;

    var currentPage_21ff4c70 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_21ff4c70'] = function(n) {
        if (n > totalPages) currentPage_21ff4c70 = totalPages;
        if (n < 1) currentPage_21ff4c70 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_21ff4c70 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_21ff4c70;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_21ff4c70 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_21ff4c70 === totalPages);
    };

    window['changePage_21ff4c70'] = function(n) {
        currentPage_21ff4c70 += n;
        window['showPage_21ff4c70'](currentPage_21ff4c70);
    };

    // Inicjalizacja
    window['showPage_21ff4c70'](1);

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
            lineageTag: 82875a54-4b81-4a11-9644-f340535acc80

        measure '08. Time Intelligence - PARALLELPERIOD' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>PARALLELPERIOD</title>
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

<div class='container' id='viz_acb50efd'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_acb50efd' onclick='changePage_acb50efd(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_acb50efd'>1</span> z <span id='totalPages_acb50efd'>3</span>
        </span>
        <button id='nextBtn_acb50efd' onclick='changePage_acb50efd(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Definicja</h1>
        <pre><code><span class='dax-function'>PARALLELPERIOD</span>(&lt;dates&gt;, &lt;number_of_intervals&gt;, &lt;interval&gt;)</code></pre>
        <p>Zwraca <strong>równoległy okres</strong> przesunięty o określoną liczbę interwałów. W przeciwieństwie do <code>DATEADD</code>, zwraca <strong>pełny okres</strong> (np. cały miesiąc), nie poszczególne daty.</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Zastosowanie</h1>
        <h2>Przykład 1: Pełny miesiąc rok temu</h2>
        <pre><code>Sprzedaż Miesiąc RR = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]),
            <span class='dax-function'>PARALLELPERIOD</span>(Kalendarz[Data], -<span class='dax-number'>12</span>, MONTH)
        )</code></pre>
        <p><strong>Różnica vs DATEADD:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Funkcja</th>
              <th>Luty 2024 →</th>
              <th>Zwraca</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>DATEADD</td>
              <td>Luty 2023</td>
              <td>Tylko dni z lutego 2023 które mają odpowiednik</td>
            </tr>
            <tr>
              <td>PARALLELPERIOD</td>
              <td><strong>Cały</strong> luty 2023</td>
              <td>Wszystkie dni lutego 2023 (1-28.02.2023)</td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Przykład 2: Poprzedni kwartał pełny</h2>
        <pre><code>Sprzedaż Poprzedni Kwartał Pełny = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]),
            <span class='dax-function'>PARALLELPERIOD</span>(Kalendarz[Data], -<span class='dax-number'>1</span>, QUARTER)
        )</code></pre>
        <p><strong>Porównanie kwartałów:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Bieżący Q</th>
              <th>PARALLELPERIOD(-1, Q)</th>
              <th>Wartość</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Q2 2024</td>
              <td><strong>Cały</strong> Q1 2024</td>
              <td>24500</td>
            </tr>
            <tr>
              <td>Q3 2024</td>
              <td><strong>Cały</strong> Q2 2024</td>
              <td>27800</td>
            </tr>
          </tbody>
        </table>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'acb50efd';
    var containerId = 'viz_' + vizId;

    var currentPage_acb50efd = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_acb50efd'] = function(n) {
        if (n > totalPages) currentPage_acb50efd = totalPages;
        if (n < 1) currentPage_acb50efd = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_acb50efd - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_acb50efd;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_acb50efd === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_acb50efd === totalPages);
    };

    window['changePage_acb50efd'] = function(n) {
        currentPage_acb50efd += n;
        window['showPage_acb50efd'](currentPage_acb50efd);
    };

    // Inicjalizacja
    window['showPage_acb50efd'](1);

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
            lineageTag: 0dab08ff-b7fb-4e1a-9e08-eabb5aff4882

        measure '08. Time Intelligence - SAMEPERIODLASTYEAR' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>SAMEPERIODLASTYEAR</title>
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

<div class='container' id='viz_b3458b19'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_b3458b19' onclick='changePage_b3458b19(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_b3458b19'>1</span> z <span id='totalPages_b3458b19'>4</span>
        </span>
        <button id='nextBtn_b3458b19' onclick='changePage_b3458b19(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Definicja</h1>
        <pre><code><span class='dax-function'>SAMEPERIODLASTYEAR</span>(&lt;dates&gt;)</code></pre>
        <p>Zwraca ten sam okres, ale przesunięty dokładnie o <strong>1 rok wstecz</strong>. Działa dla dni, tygodni, miesięcy, kwartałów i lat.</p>
        <h1>Zastosowanie</h1>
        <p><strong>Tabela źródłowa:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>Wartość</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2024-01-15</td>
              <td>3000</td>
            </tr>
            <tr>
              <td>2024-02-10</td>
              <td>2400</td>
            </tr>
            <tr>
              <td>2023-01-15</td>
              <td>2800</td>
            </tr>
            <tr>
              <td>2023-02-10</td>
              <td>2200</td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h2>Przykład 1: Sprzedaż rok do roku (YoY)</h2>
        <pre><code>Sprzedaż RR = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]),
            <span class='dax-function'>SAMEPERIODLASTYEAR</span>(Kalendarz[Data])
        )</code></pre>
        <p><strong>Jak działa iteracja:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Bieżący okres</th>
              <th>Przesunięcie →</th>
              <th>Wartość RR</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2024-01-15</td>
              <td>→ 2023-01-15</td>
              <td>2800</td>
            </tr>
            <tr>
              <td>2024-02-10</td>
              <td>→ 2023-02-10</td>
              <td>2200</td>
            </tr>
            <tr>
              <td>Styczeń 2024</td>
              <td>→ Styczeń 2023</td>
              <td>2800</td>
            </tr>
            <tr>
              <td>Q1 2024</td>
              <td>→ Q1 2023</td>
              <td>5000</td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Przykład 2: Dynamika YoY w procentach</h2>
        <pre><code>Wzrost YoY % = 
        <span class='dax-function'>DIVIDE</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]) - [Sprzedaż RR],
            [Sprzedaż RR]
        )</code></pre>
        <p><strong>Wyniki:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Miesiąc</th>
              <th>Wartość 2024</th>
              <th>Wartość 2023</th>
              <th>Wzrost YoY %</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Styczeń</td>
              <td>3000</td>
              <td>2800</td>
              <td>+7,1%</td>
            </tr>
            <tr>
              <td>Luty</td>
              <td>2400</td>
              <td>2200</td>
              <td>+9,1%</td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>Przykład 3: Porównanie YTD rok do roku</h2>
        <pre><code>Sprzedaż YTD RR = 
        <span class='dax-function'>CALCULATE</span>(
            [Sprzedaż YTD],
            <span class='dax-function'>SAMEPERIODLASTYEAR</span>(Kalendarz[Data])
        )</code></pre>
        <p><strong>Porównanie kumulacji:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Okres</th>
              <th>YTD 2024</th>
              <th>YTD 2023</th>
              <th>Różnica</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Do 31.01</td>
              <td>3000</td>
              <td>2800</td>
              <td>+200</td>
            </tr>
            <tr>
              <td>Do 28.02</td>
              <td>5400</td>
              <td>5000</td>
              <td>+400</td>
            </tr>
          </tbody>
        </table>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'b3458b19';
    var containerId = 'viz_' + vizId;

    var currentPage_b3458b19 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_b3458b19'] = function(n) {
        if (n > totalPages) currentPage_b3458b19 = totalPages;
        if (n < 1) currentPage_b3458b19 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_b3458b19 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_b3458b19;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_b3458b19 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_b3458b19 === totalPages);
    };

    window['changePage_b3458b19'] = function(n) {
        currentPage_b3458b19 += n;
        window['showPage_b3458b19'](currentPage_b3458b19);
    };

    // Inicjalizacja
    window['showPage_b3458b19'](1);

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
            lineageTag: 38ec8fa2-63aa-43ba-a9ba-b20162ae7e81

        measure '08. Time Intelligence - Tabela porównawcza funkcji' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Tabela porównawcza funkcji</title>
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

<div class='container' id='viz_05473ef6'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_05473ef6' onclick='changePage_05473ef6(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_05473ef6'>1</span> z <span id='totalPages_05473ef6'>1</span>
        </span>
        <button id='nextBtn_05473ef6' onclick='changePage_05473ef6(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <table>
          <thead>
            <tr>
              <th>Funkcja</th>
              <th>Typ operacji</th>
              <th>Zakres</th>
              <th>Przykład użycia</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>SAMEPERIODLASTYEAR</strong></td>
              <td>Przesunięcie</td>
              <td>-1 rok (dokładnie)</td>
              <td>YoY</td>
            </tr>
            <tr>
              <td><strong>DATESYTD</strong></td>
              <td>Kumulacja</td>
              <td>1 stycznia → dziś</td>
              <td>YTD</td>
            </tr>
            <tr>
              <td><strong>DATEADD</strong></td>
              <td>Przesunięcie</td>
              <td>Dowolny interwał</td>
              <td>MoM, wczoraj</td>
            </tr>
            <tr>
              <td><strong>TOTALMTD</strong></td>
              <td>Kumulacja</td>
              <td>1. dzień miesiąca → dziś</td>
              <td>MTD</td>
            </tr>
            <tr>
              <td><strong>DATESINPERIOD</strong></td>
              <td>Okno przewijane</td>
              <td>Ostatnie N okresów</td>
              <td>Rolling 7D, 3M</td>
            </tr>
            <tr>
              <td><strong>TOTALYTD</strong></td>
              <td>Kumulacja</td>
              <td>1 stycznia → dziś</td>
              <td>YTD (skrócona)</td>
            </tr>
            <tr>
              <td><strong>PARALLELPERIOD</strong></td>
              <td>Przesunięcie pełnego okresu</td>
              <td>Cały okres równoległy</td>
              <td>Pełny miesiąc RR</td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '05473ef6';
    var containerId = 'viz_' + vizId;

    var currentPage_05473ef6 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_05473ef6'] = function(n) {
        if (n > totalPages) currentPage_05473ef6 = totalPages;
        if (n < 1) currentPage_05473ef6 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_05473ef6 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_05473ef6;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_05473ef6 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_05473ef6 === totalPages);
    };

    window['changePage_05473ef6'] = function(n) {
        currentPage_05473ef6 += n;
        window['showPage_05473ef6'](currentPage_05473ef6);
    };

    // Inicjalizacja
    window['showPage_05473ef6'](1);

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
            lineageTag: 8ec4ceab-cedb-455f-b9a4-00c36823a556

        measure '08. Time Intelligence - TOTALYTD' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>TOTALYTD</title>
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

<div class='container' id='viz_41750251'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_41750251' onclick='changePage_41750251(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_41750251'>1</span> z <span id='totalPages_41750251'>4</span>
        </span>
        <button id='nextBtn_41750251' onclick='changePage_41750251(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Definicja</h1>
        <pre><code><span class='dax-function'>TOTALYTD</span>(&lt;expression&gt;, &lt;dates&gt;, [&lt;filter&gt;], [&lt;year_end_date&gt;])</code></pre>
        <p>Oblicza <strong>kumulację od początku roku</strong> (Year to Date). Skrócona wersja <code>CALCULATE</code> + <code>DATESYTD</code>.</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Zastosowanie</h1>
        <h2>Przykład 1: Suma YTD</h2>
        <pre><code>Sprzedaż YTD = 
        <span class='dax-function'>TOTALYTD</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]),
            Kalendarz[Data]
        )</code></pre>
        <p>Identyczne działanie jak <code>CALCULATE(SUM(...), DATESYTD(...))</code> z poprzednich przykładów.</p>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Przykład 2: YTD z rokiem obrotowym</h2>
        <pre><code>Sprzedaż YTD Fiskalny = 
        <span class='dax-function'>TOTALYTD</span>(
            <span class='dax-function'>SUM</span>(fSprzedaz[Wartość]),
            Kalendarz[Data],
            ,
            '<span class='dax-number'>6</span>/<span class='dax-number'>30</span>'
        )</code></pre>
        <p><strong>Rok obrotowy:</strong> lipiec-czerwiec</p>
        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>YTD standardowy</th>
              <th>YTD fiskalny (lip-cze)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>31.08.2024</td>
              <td>45000</td>
              <td>3200</td>
            </tr>
            <tr>
              <td>31.12.2024</td>
              <td>85000</td>
              <td>42500</td>
            </tr>
          </tbody>
        </table>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>Przykład 3: Liczba transakcji YTD</h2>
        <pre><code>Transakcje YTD = 
        <span class='dax-function'>TOTALYTD</span>(
            <span class='dax-function'>COUNTROWS</span>(fSprzedaz),
            Kalendarz[Data]
        )</code></pre>
        <p><strong>Kumulacja liczby wierszy:</strong></p>
        <table>
          <thead>
            <tr>
              <th>Miesiąc</th>
              <th>Transakcje miesięczne</th>
              <th>Transakcje YTD</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Styczeń</td>
              <td>45</td>
              <td>45</td>
            </tr>
            <tr>
              <td>Luty</td>
              <td>52</td>
              <td>97</td>
            </tr>
            <tr>
              <td>Marzec</td>
              <td>48</td>
              <td>145</td>
            </tr>
          </tbody>
        </table>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '41750251';
    var containerId = 'viz_' + vizId;

    var currentPage_41750251 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_41750251'] = function(n) {
        if (n > totalPages) currentPage_41750251 = totalPages;
        if (n < 1) currentPage_41750251 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_41750251 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_41750251;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_41750251 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_41750251 === totalPages);
    };

    window['changePage_41750251'] = function(n) {
        currentPage_41750251 += n;
        window['showPage_41750251'](currentPage_41750251);
    };

    // Inicjalizacja
    window['showPage_41750251'](1);

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
            lineageTag: c3726f52-05d9-4178-ad7b-ed436be03aba

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

