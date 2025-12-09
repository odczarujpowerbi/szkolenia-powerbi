createOrReplace

    table _HTML
        lineageTag: 12ee804d-ccc2-43e6-94ae-57dc2fd38d79

        measure '01. Podstawy DAX - Funkcje filtrujące' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Funkcje filtrujące</title>
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
            
            h2 {
                font-size: 1.4em;
                font-weight: 600;
                margin: 1.5em 0 0.8em 0;
                color: #2a2a2a;
            }
            
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                color: #444;
            }
            
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
            
            strong {
                font-weight: 600;
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
                margin: 1em 0 1em 1.5em;
            }
            
            li {
                margin: 0.5em 0;
                font-size: 1.05em;
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
</head>
<body>

<div class='container' id='viz_2aa7098d'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_2aa7098d' onclick='changePage_2aa7098d(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_2aa7098d'>1</span> z <span id='totalPages_2aa7098d'>2</span>
        </span>
        <button id='nextBtn_2aa7098d' onclick='changePage_2aa7098d(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>FILTER – Filtrowanie tabeli</h1>
        <p>Zwraca <strong>podzbiór tabeli</strong> spełniający warunek:</p>
        <pre><code><span class='dax-function'>FILTER</span>(\&lt;tabela\&gt;, \&lt;warunek\&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Wysokie Sprzedaże = 
        <span class='dax-function'>FILTER</span>(
            Sprzedaz,
            Sprzedaz[Kwota] \&gt; <span class='dax-number'>1000</span>
        )</code></pre>
        <p><strong>Użycie z SUMX:</strong></p>
        <pre><code>Suma Wysokich Sprzedaży = 
        <span class='dax-function'>SUMX</span>(
            <span class='dax-function'>FILTER</span>(Sprzedaz, Sprzedaz[Kwota] \&gt; <span class='dax-number'>1000</span>),
            Sprzedaz[Kwota]
        )</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>CALCULATE – Modyfikacja kontekstu filtrowania</h1>
        <pre><code><span class='dax-function'>CALCULATE</span>(\&lt;wyrażenie\&gt;, \&lt;filtr1\&gt;, \&lt;filtr2\&gt;, ...)</code></pre>
        <p><strong>CALCULATE</strong> to <strong>najważniejsza funkcja w DAX</strong>. Pozwala:</p>
        <ul>
        <li>Zmienić kontekst filtrowania</li>
        <li>Dodać nowe filtry</li>
        <li>Nadpisać istniejące filtry</li>
        <li>Stworzyć obliczenia w różnych kontekstach</li>
        </ul>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '2aa7098d';
    var containerId = 'viz_' + vizId;

    var currentPage_2aa7098d = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_2aa7098d'] = function(n) {
        if (n > totalPages) currentPage_2aa7098d = totalPages;
        if (n < 1) currentPage_2aa7098d = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_2aa7098d - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_2aa7098d;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_2aa7098d === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_2aa7098d === totalPages);
    };

    window['changePage_2aa7098d'] = function(n) {
        currentPage_2aa7098d += n;
        window['showPage_2aa7098d'](currentPage_2aa7098d);
    };

    // Inicjalizacja
    window['showPage_2aa7098d'](1);
})();
</script>

</body>
</html>

"
```
            lineageTag: ad5dc8b2-9a65-4d8b-bfb7-4a009505c8cd

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
            
            h2 {
                font-size: 1.4em;
                font-weight: 600;
                margin: 1.5em 0 0.8em 0;
                color: #2a2a2a;
            }
            
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                color: #444;
            }
            
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
            
            strong {
                font-weight: 600;
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
                margin: 1em 0 1em 1.5em;
            }
            
            li {
                margin: 0.5em 0;
                font-size: 1.05em;
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
        <pre><code><span class='dax-function'>SUMX</span>(\&lt;tabela\&gt;, \&lt;wyrażenie\&gt;)</code></pre>
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
        <pre><code><span class='dax-function'>AVERAGEX</span>(\&lt;tabela\&gt;, \&lt;wyrażenie\&gt;)</code></pre>
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
        <pre><code><span class='dax-function'>COUNTX</span>(\&lt;tabela\&gt;, \&lt;wyrażenie\&gt;)</code></pre>
        <p>Liczy ile razy wyrażenie zwróciło <strong>niepustą wartość</strong>.</p>
        <p><strong>Przykład:</strong></p>
        <pre><code>Liczba Zamówień Powyżej <span class='dax-number'>1000</span> = 
        <span class='dax-function'>COUNTX</span>(
            Sprzedaz,
            <span class='dax-function'>IF</span>(Sprzedaz[Kwota] \&gt; <span class='dax-number'>1000</span>, <span class='dax-number'>1</span>, <span class='dax-function'>BLANK</span>())
        )</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>MINX i MAXX – Minimum i maksimum z iteracją</h1>
        <pre><code><span class='dax-function'>MINX</span>(\&lt;tabela\&gt;, \&lt;wyrażenie\&gt;)
        <span class='dax-function'>MAXX</span>(\&lt;tabela\&gt;, \&lt;wyrażenie\&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Najwyższa Marża = 
        <span class='dax-function'>MAXX</span>(
            Sprzedaz,
            Sprzedaz[Przychód] - Sprzedaz[Koszt]
        )</code></pre>
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
})();
</script>

</body>
</html>

"
```
            lineageTag: d2524e36-e0bd-4f17-8b2b-897a382b6f3a

        measure '01. Podstawy DAX - Podstawowe funkcje agregujące' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Podstawowe funkcje agregujące</title>
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
            
            h2 {
                font-size: 1.4em;
                font-weight: 600;
                margin: 1.5em 0 0.8em 0;
                color: #2a2a2a;
            }
            
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                color: #444;
            }
            
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
            
            strong {
                font-weight: 600;
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
                margin: 1em 0 1em 1.5em;
            }
            
            li {
                margin: 0.5em 0;
                font-size: 1.05em;
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
</head>
<body>

<div class='container' id='viz_4b21e28b'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_4b21e28b' onclick='changePage_4b21e28b(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_4b21e28b'>1</span> z <span id='totalPages_4b21e28b'>7</span>
        </span>
        <button id='nextBtn_4b21e28b' onclick='changePage_4b21e28b(1)'>Następna →</button>
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
        <p>Liczy ile jest niepustych wartości w kolumnie:</p>
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
    var vizId = '4b21e28b';
    var containerId = 'viz_' + vizId;

    var currentPage_4b21e28b = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_4b21e28b'] = function(n) {
        if (n > totalPages) currentPage_4b21e28b = totalPages;
        if (n < 1) currentPage_4b21e28b = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_4b21e28b - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_4b21e28b;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_4b21e28b === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_4b21e28b === totalPages);
    };

    window['changePage_4b21e28b'] = function(n) {
        currentPage_4b21e28b += n;
        window['showPage_4b21e28b'](currentPage_4b21e28b);
    };

    // Inicjalizacja
    window['showPage_4b21e28b'](1);
})();
</script>

</body>
</html>

"
```
            lineageTag: a9dc686b-87ef-47cd-b2db-fc5263ac568a

        measure '01. Podstawy DAX - Podstawowe funkcje dat' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Podstawowe funkcje dat</title>
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
            
            h2 {
                font-size: 1.4em;
                font-weight: 600;
                margin: 1.5em 0 0.8em 0;
                color: #2a2a2a;
            }
            
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                color: #444;
            }
            
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
            
            strong {
                font-weight: 600;
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
                margin: 1em 0 1em 1.5em;
            }
            
            li {
                margin: 0.5em 0;
                font-size: 1.05em;
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
</head>
<body>

<div class='container' id='viz_923e2dba'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_923e2dba' onclick='changePage_923e2dba(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_923e2dba'>1</span> z <span id='totalPages_923e2dba'>4</span>
        </span>
        <button id='nextBtn_923e2dba' onclick='changePage_923e2dba(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>DATE – Tworzenie daty</h1>
        <pre><code><span class='dax-function'>DATE</span>(\&lt;rok\&gt;, \&lt;miesiąc\&gt;, \&lt;dzień\&gt;)</code></pre>
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
        <pre><code><span class='dax-function'>YEAR</span>(\&lt;data\&gt;)   <span class='dax-comment'>-- Rok</span>
        <span class='dax-function'>MONTH</span>(\&lt;data\&gt;)  <span class='dax-comment'>-- Miesiąc (1-12)</span>
        <span class='dax-function'>DAY</span>(\&lt;data\&gt;)    <span class='dax-comment'>-- Dzień (1-31)</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Rok Sprzedaży = <span class='dax-function'>YEAR</span>(Sprzedaz[Data])
        Miesiąc Sprzedaży = <span class='dax-function'>MONTH</span>(Sprzedaz[Data])</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>DATEDIFF – Różnica między datami</h1>
        <pre><code><span class='dax-function'>DATEDIFF</span>(\&lt;data_początkowa\&gt;, \&lt;data_końcowa\&gt;, \&lt;jednostka\&gt;)</code></pre>
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
    var vizId = '923e2dba';
    var containerId = 'viz_' + vizId;

    var currentPage_923e2dba = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_923e2dba'] = function(n) {
        if (n > totalPages) currentPage_923e2dba = totalPages;
        if (n < 1) currentPage_923e2dba = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_923e2dba - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_923e2dba;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_923e2dba === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_923e2dba === totalPages);
    };

    window['changePage_923e2dba'] = function(n) {
        currentPage_923e2dba += n;
        window['showPage_923e2dba'](currentPage_923e2dba);
    };

    // Inicjalizacja
    window['showPage_923e2dba'](1);
})();
</script>

</body>
</html>

"
```
            lineageTag: 27b59044-94af-42fd-9839-2b2ace5a140a

        measure '01. Podstawy DAX - Podstawowe funkcje logiczne' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Podstawowe funkcje logiczne</title>
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
            
            h2 {
                font-size: 1.4em;
                font-weight: 600;
                margin: 1.5em 0 0.8em 0;
                color: #2a2a2a;
            }
            
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                color: #444;
            }
            
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
            
            strong {
                font-weight: 600;
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
                margin: 1em 0 1em 1.5em;
            }
            
            li {
                margin: 0.5em 0;
                font-size: 1.05em;
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
</head>
<body>

<div class='container' id='viz_eae3bcf3'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_eae3bcf3' onclick='changePage_eae3bcf3(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_eae3bcf3'>1</span> z <span id='totalPages_eae3bcf3'>4</span>
        </span>
        <button id='nextBtn_eae3bcf3' onclick='changePage_eae3bcf3(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>IF – Warunek logiczny</h1>
        <p>Zwraca jedną wartość jeśli warunek jest prawdziwy, inną jeśli fałszywy:</p>
        <pre><code><span class='dax-function'>IF</span>(\&lt;warunek\&gt;, \&lt;wartość_jeśli_prawda\&gt;, \&lt;wartość_jeśli_fałsz\&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Kategoria Sprzedaży = 
        <span class='dax-function'>IF</span>(
            Sprzedaz[Kwota] \&gt; <span class='dax-number'>1000</span>,
            'Wysoka',
            'Niska'
        )</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>AND – Sprawdza czy wszystkie warunki są prawdziwe</h1>
        <pre><code><span class='dax-function'>AND</span>(\&lt;warunek1\&gt;, \&lt;warunek2\&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Czy VIP = 
        <span class='dax-function'>IF</span>(
            <span class='dax-function'>AND</span>(Klienci[Przychód] \&gt; <span class='dax-number'>50000</span>, Klienci[Lata Współpracy] \&gt; <span class='dax-number'>5</span>),
            'TAK',
            'NIE'
        )</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>OR – Sprawdza czy przynajmniej jeden warunek jest prawdziwy</h1>
        <pre><code><span class='dax-function'>OR</span>(\&lt;warunek1\&gt;, \&lt;warunek2\&gt;)</code></pre>
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
        <pre><code><span class='dax-function'>NOT</span>(\&lt;warunek\&gt;)</code></pre>
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
    var vizId = 'eae3bcf3';
    var containerId = 'viz_' + vizId;

    var currentPage_eae3bcf3 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_eae3bcf3'] = function(n) {
        if (n > totalPages) currentPage_eae3bcf3 = totalPages;
        if (n < 1) currentPage_eae3bcf3 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_eae3bcf3 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_eae3bcf3;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_eae3bcf3 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_eae3bcf3 === totalPages);
    };

    window['changePage_eae3bcf3'] = function(n) {
        currentPage_eae3bcf3 += n;
        window['showPage_eae3bcf3'](currentPage_eae3bcf3);
    };

    // Inicjalizacja
    window['showPage_eae3bcf3'](1);
})();
</script>

</body>
</html>

"
```
            lineageTag: 32b67f55-27e4-45fe-93e2-a231ccaa2b8c

        measure '01. Podstawy DAX - Podstawowe funkcje tekstowe' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Podstawowe funkcje tekstowe</title>
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
            
            h2 {
                font-size: 1.4em;
                font-weight: 600;
                margin: 1.5em 0 0.8em 0;
                color: #2a2a2a;
            }
            
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                color: #444;
            }
            
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
            
            strong {
                font-weight: 600;
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
                margin: 1em 0 1em 1.5em;
            }
            
            li {
                margin: 0.5em 0;
                font-size: 1.05em;
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
</head>
<body>

<div class='container' id='viz_caa8f251'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_caa8f251' onclick='changePage_caa8f251(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_caa8f251'>1</span> z <span id='totalPages_caa8f251'>4</span>
        </span>
        <button id='nextBtn_caa8f251' onclick='changePage_caa8f251(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>CONCATENATE – Łączenie tekstów</h1>
        <pre><code><span class='dax-function'>CONCATENATE</span>(\&lt;tekst1\&gt;, \&lt;tekst2\&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Pełna Nazwa = <span class='dax-function'>CONCATENATE</span>(Klienci[Imię], ' ' & Klienci[Nazwisko])</code></pre>
        <p><strong>Alternatywa (łatwiejsza):</strong></p>
        <pre><code>Pełna Nazwa = Klienci[Imię] & ' ' & Klienci[Nazwisko]</code></pre>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>LEFT, RIGHT, MID – Wyciąganie części tekstu</h1>
        <pre><code><span class='dax-function'>LEFT</span>(\&lt;tekst\&gt;, \&lt;liczba_znaków\&gt;)    <span class='dax-comment'>-- Pierwsze znaki od lewej</span>
        <span class='dax-function'>RIGHT</span>(\&lt;tekst\&gt;, \&lt;liczba_znaków\&gt;)   <span class='dax-comment'>-- Ostatnie znaki od prawej</span>
        <span class='dax-function'>MID</span>(\&lt;tekst\&gt;, \&lt;start\&gt;, \&lt;liczba\&gt;)   <span class='dax-comment'>-- Znaki ze środka</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Pierwsze <span class='dax-number'>3</span> Znaki = <span class='dax-function'>LEFT</span>(Produkty[Kod], <span class='dax-number'>3</span>)
        Ostatnie <span class='dax-number'>2</span> Znaki = <span class='dax-function'>RIGHT</span>(Produkty[Kod], <span class='dax-number'>2</span>)</code></pre>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h1>UPPER, LOWER – Zmiana wielkości liter</h1>
        <pre><code><span class='dax-function'>UPPER</span>(\&lt;tekst\&gt;)  <span class='dax-comment'>-- Wszystkie znaki WIELKIE</span>
        <span class='dax-function'>LOWER</span>(\&lt;tekst\&gt;)  <span class='dax-comment'>-- Wszystkie znaki małe</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Kategoria Wielkie Litery = <span class='dax-function'>UPPER</span>(Produkty[Kategoria])</code></pre>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h1>LEN – Długość tekstu</h1>
        <pre><code><span class='dax-function'>LEN</span>(\&lt;tekst\&gt;)</code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Długość Kodu = <span class='dax-function'>LEN</span>(Produkty[Kod Produktu])</code></pre>
        <p>---</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'caa8f251';
    var containerId = 'viz_' + vizId;

    var currentPage_caa8f251 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_caa8f251'] = function(n) {
        if (n > totalPages) currentPage_caa8f251 = totalPages;
        if (n < 1) currentPage_caa8f251 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_caa8f251 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_caa8f251;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_caa8f251 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_caa8f251 === totalPages);
    };

    window['changePage_caa8f251'] = function(n) {
        currentPage_caa8f251 += n;
        window['showPage_caa8f251'](currentPage_caa8f251);
    };

    // Inicjalizacja
    window['showPage_caa8f251'](1);
})();
</script>

</body>
</html>

"
```
            lineageTag: 5250fe48-bbc4-47a7-8670-8f14ef210709

        measure '01. Podstawy DAX - Wprowadzenie do CALCULATE' = ```
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
            
            h2 {
                font-size: 1.4em;
                font-weight: 600;
                margin: 1.5em 0 0.8em 0;
                color: #2a2a2a;
            }
            
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                color: #444;
            }
            
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
            
            strong {
                font-weight: 600;
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
                margin: 1em 0 1em 1.5em;
            }
            
            li {
                margin: 0.5em 0;
                font-size: 1.05em;
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
</head>
<body>

<div class='container' id='viz_a6296909'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_a6296909' onclick='changePage_a6296909(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_a6296909'>1</span> z <span id='totalPages_a6296909'>9</span>
        </span>
        <button id='nextBtn_a6296909' onclick='changePage_a6296909(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Czym jest kontekst filtrowania?</h1>
        <p><strong>Kontekst filtrowania</strong> to zbiór filtrów aktywnych w danym momencie obliczeń. Określa on <strong>jakie wiersze</strong> z tabel są brane pod uwagę.</p>
        <p><strong>Przykład:</strong> Jeśli w wizualizacji masz slicer ustawiony na 'Rok = 2024', to wszystkie miary widzą tylko dane z 2024 roku.</p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Podstawowe użycie CALCULATE</h1>
        <h2>Przykład 1: Dodanie filtra</h2>
        <pre><code>Sprzedaż w Warszawie = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(Sprzedaz[Kwota]),
            Klienci[Miasto] = 'Warszawa'
        )</code></pre>
        <p><strong>Co się dzieje:</strong></p>
        <ul>
        <li>Bierze <code>SUM(Sprzedaz[Kwota])</code></li>
        <li>Dodaje filtr: tylko dla miasta 'Warszawa'</li>
        <li>Zwraca sumę tylko dla Warszawy</li>
        </ul>

    </div>

    <!-- Strona 3 -->
    <div class='page'>
        <h2>Przykład 2: Wiele filtrów</h2>
        <pre><code>Sprzedaż VIP w <span class='dax-number'>2024</span> = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(Sprzedaz[Kwota]),
            Klienci[Kategoria] = 'VIP',
            <span class='dax-function'>YEAR</span>(Sprzedaz[Data]) = <span class='dax-number'>2024</span>
        )</code></pre>
        <p><strong>Filtry są łączone operatorem AND</strong> – muszą być <strong>oba</strong> spełnione.</p>

    </div>

    <!-- Strona 4 -->
    <div class='page'>
        <h2>Przykład 3: Nadpisanie istniejącego filtra</h2>
        <pre><code>Całkowita Sprzedaż = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(Sprzedaz[Kwota]),
            <span class='dax-function'>ALL</span>(Produkty[Kategoria])
        )</code></pre>
        <p><strong>Co robi <code>ALL</code>?</strong></p>
        <ul>
        <li>Usuwa filtry z kolumny <code>Produkty[Kategoria]</code></li>
        <li>Dzięki temu <code>Całkowita Sprzedaż</code> pokazuje sumę dla <strong>wszystkich kategorii</strong>, niezależnie od tego, co jest wybrane w slicerze</li>
        </ul>
        <p>_(Funkcje ALL, ALLEXCEPT, REMOVEFILTERS omówimy w bardziej zaawansowanym materiale)_</p>

    </div>

    <!-- Strona 5 -->
    <div class='page'>
        <h1>Kiedy używać CALCULATE?</h1>
        <p>✅ <strong>Używaj CALCULATE gdy:</strong></p>
        <ul>
        <li>Chcesz dodać <strong>dodatkowy filtr</strong> do obliczeń</li>
        <li>Chcesz <strong>nadpisać</strong> istniejący filtr</li>
        <li>Chcesz obliczyć wartość w <strong>innym kontekście</strong> niż aktualny (np. suma całkowita)</li>
        <li>Chcesz porównać wartości (np. sprzedaż bieżącego roku vs poprzedniego)</li>
        </ul>

    </div>

    <!-- Strona 6 -->
    <div class='page'>
        <h2>Przykład praktyczny: Udział w sprzedaży</h2>
        <pre><code>Udział w Sprzedaży = 
        <span class='dax-function'>DIVIDE</span>(
            <span class='dax-function'>SUM</span>(Sprzedaz[Kwota]),
            <span class='dax-function'>CALCULATE</span>(
                <span class='dax-function'>SUM</span>(Sprzedaz[Kwota]),
                <span class='dax-function'>ALL</span>(Produkty[Kategoria])
            )
        )</code></pre>
        <p><strong>Jak to działa:</strong></p>
        <ul>
        <li><strong>Licznik:</strong> Suma sprzedaży dla aktualnej kategorii (np. 'Elektronika')</li>
        <li><strong>Mianownik:</strong> Suma sprzedaży dla <strong>wszystkich</strong> kategorii (dzięki <code>ALL</code>)</li>
        <li><strong>Wynik:</strong> Procent sprzedaży danej kategorii względem całości</li>
        </ul>

    </div>

    <!-- Strona 7 -->
    <div class='page'>
        <h2>Przykład: Porównanie z poprzednim rokiem</h2>
        <pre><code>Sprzedaż Poprzedni Rok = 
        <span class='dax-function'>CALCULATE</span>(
            <span class='dax-function'>SUM</span>(Sprzedaz[Kwota]),
            <span class='dax-function'>SAMEPERIODLASTYEAR</span>(Kalendarz[Data])
        )</code></pre>
        <p><strong>Co się dzieje:</strong></p>
        <ul>
        <li><code>SAMEPERIODLASTYEAR</code> przesuwa kontekst dat o rok wstecz</li>
        <li>Dzięki temu <code>CALCULATE</code> oblicza sprzedaż dla <strong>tego samego okresu rok temu</strong></li>
        </ul>

    </div>

    <!-- Strona 8 -->
    <div class='page'>
        <h1>Kluczowe zasady CALCULATE</h1>
        <p>1. <strong>CALCULATE zmienia kontekst filtrowania</strong> – to jego główna rola</p>
        <p>2. <strong>Filtry w CALCULATE są stosowane jako AND</strong> – wszystkie muszą być spełnione</p>
        <p>3. <strong>CALCULATE może nadpisać istniejące filtry</strong> – nowy filtr zastępuje stary</p>
        <p>4. <strong>CALCULATE działa tylko w miarach</strong> – nie w kolumnach kalkulowanych (tam kontekst jest inny)</p>

    </div>

    <!-- Strona 9 -->
    <div class='page'>
        <h1>Podsumowanie CALCULATE</h1>
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
})();
</script>

</body>
</html>

"
```
            lineageTag: e70523bc-3341-42a8-838d-831b76562a58

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
            
            h2 {
                font-size: 1.4em;
                font-weight: 600;
                margin: 1.5em 0 0.8em 0;
                color: #2a2a2a;
            }
            
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                color: #444;
            }
            
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
            
            strong {
                font-weight: 600;
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
                margin: 1em 0 1em 1.5em;
            }
            
            li {
                margin: 0.5em 0;
                font-size: 1.05em;
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
        <p>| Typ                   | Przykład                           | Opis                    |</p>
        <p>| --------------------- | ---------------------------------- | ----------------------- |</p>
        <p>| <strong>Liczby całkowite</strong>  | <code>100</code>, <code>-50</code>                       | Integer                 |</p>
        <p>| <strong>Liczby dziesiętne</strong> | <code>123.45</code>, <code>0.99</code>                   | Decimal/Float           |</p>
        <p>| <strong>Tekst</strong>             | <code>'Warszawa'</code>, <code>'ABC'</code>              | String (w cudzysłowach) |</p>
        <p>| <strong>Data</strong>              | <code>DATE(2024, 12, 8)</code>                | Date                    |</p>
        <p>| <strong>Data i czas</strong>       | <code>DATETIME(2024, 12, 8, 14, 30, 0)</code> | DateTime                |</p>
        <p>| <strong>Logiczne</strong>          | <code>TRUE</code>, <code>FALSE</code>                    | Boolean                 |</p>
        <p>| <strong>Puste</strong>             | <code>BLANK()</code>                          | Null/Empty              |</p>

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
        \&lt;\&gt;  <span class='dax-comment'>-- Różne od</span>
        \&gt;   <span class='dax-comment'>-- Większe niż</span>
        \&lt;   <span class='dax-comment'>-- Mniejsze niż</span>
        \&gt;=  <span class='dax-comment'>-- Większe lub równe</span>
        \&lt;=  <span class='dax-comment'>-- Mniejsze lub równe</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Czy Duża Sprzedaż = 
        Sprzedaz[Kwota] \&gt; <span class='dax-number'>1000</span></code></pre>

    </div>

    <!-- Strona 9 -->
    <div class='page'>
        <h1>Operatory logiczne</h1>
        <pre><code>&&  <span class='dax-comment'>-- AND (i)</span>
        ||  <span class='dax-comment'>-- OR (lub)</span>
        NOT <span class='dax-comment'>-- NOT (negacja)</span></code></pre>
        <p><strong>Przykład:</strong></p>
        <pre><code>Czy Premium = 
        Klienci[Kategoria] = 'VIP' && Klienci[Przychód] \&gt; <span class='dax-number'>10000</span></code></pre>

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
})();
</script>

</body>
</html>

"
```
            lineageTag: 1d3ba538-c0d1-4292-a7a1-fcde90c273c6

        measure '02. DAX - Zmienne' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>02. DAX - Zmienne</title>
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
            
            h2 {
                font-size: 1.4em;
                font-weight: 600;
                margin: 1.5em 0 0.8em 0;
                color: #2a2a2a;
            }
            
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                color: #444;
            }
            
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
            
            strong {
                font-weight: 600;
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
                margin: 1em 0 1em 1.5em;
            }
            
            li {
                margin: 0.5em 0;
                font-size: 1.05em;
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
</head>
<body>

<div class='container' id='viz_41ce191a'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_41ce191a' onclick='changePage_41ce191a(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_41ce191a'>1</span> z <span id='totalPages_41ce191a'>4</span>
        </span>
        <button id='nextBtn_41ce191a' onclick='changePage_41ce191a(1)'>Następna →</button>
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
        <span class='dax-keyword'>VAR</span> NazwaZmiennej1 = \&lt;wyrażenie1\&gt;
        <span class='dax-keyword'>VAR</span> NazwaZmiennej2 = \&lt;wyrażenie2\&gt;
        <span class='dax-keyword'>VAR</span> NazwaZmiennej3 = \&lt;wyrażenie3\&gt;
        <span class='dax-keyword'>RETURN</span> \&lt;wynik_końcowy\&gt;</code></pre>
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
        <h1>Co się dzieje krok po kroku:</h1>
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
    var vizId = '41ce191a';
    var containerId = 'viz_' + vizId;

    var currentPage_41ce191a = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_41ce191a'] = function(n) {
        if (n > totalPages) currentPage_41ce191a = totalPages;
        if (n < 1) currentPage_41ce191a = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_41ce191a - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_41ce191a;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_41ce191a === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_41ce191a === totalPages);
    };

    window['changePage_41ce191a'] = function(n) {
        currentPage_41ce191a += n;
        window['showPage_41ce191a'](currentPage_41ce191a);
    };

    // Inicjalizacja
    window['showPage_41ce191a'](1);
})();
</script>

</body>
</html>

"
```
            lineageTag: 2abfe7c1-0b15-4b63-8b04-6c0870c42190

        measure '03. Test - Testowy dział' = ```
"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Testowy dział</title>
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
            
            h2 {
                font-size: 1.4em;
                font-weight: 600;
                margin: 1.5em 0 0.8em 0;
                color: #2a2a2a;
            }
            
            h3 {
                font-size: 1.1em;
                font-weight: 600;
                margin: 1.2em 0 0.6em 0;
                color: #444;
            }
            
            p {
                margin-bottom: 1em;
                font-size: 1.05em;
            }
            
            strong {
                font-weight: 600;
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
                margin: 1em 0 1em 1.5em;
            }
            
            li {
                margin: 0.5em 0;
                font-size: 1.05em;
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
</head>
<body>

<div class='container' id='viz_f51c1b72'>
    <!-- Nawigacja na górze -->
    <div class='navigation'>
        <button id='prevBtn_f51c1b72' onclick='changePage_f51c1b72(-1)'>← Poprzednia</button>
        <span class='page-indicator'>
            Strona <span id='currentPage_f51c1b72'>1</span> z <span id='totalPages_f51c1b72'>2</span>
        </span>
        <button id='nextBtn_f51c1b72' onclick='changePage_f51c1b72(1)'>Następna →</button>
    </div>

    <!-- Strona 1 -->
    <div class='page active'>
        <h1>Temat temat</h1>
        <p><img src='https://raw.githubusercontent.com/odczarujpowerbi/grafiki-do-szkolenia/main/Screenshot%202024-07-24%20at%2023.10.58.png' width='100%'></p>

    </div>

    <!-- Strona 2 -->
    <div class='page'>
        <h1>Nowa strona</h1>
        <p>Bez zdjęcia</p>

    </div>

</div>

<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = 'f51c1b72';
    var containerId = 'viz_' + vizId;

    var currentPage_f51c1b72 = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_f51c1b72'] = function(n) {
        if (n > totalPages) currentPage_f51c1b72 = totalPages;
        if (n < 1) currentPage_f51c1b72 = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_f51c1b72 - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_f51c1b72;
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_f51c1b72 === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_f51c1b72 === totalPages);
    };

    window['changePage_f51c1b72'] = function(n) {
        currentPage_f51c1b72 += n;
        window['showPage_f51c1b72'](currentPage_f51c1b72);
    };

    // Inicjalizacja
    window['showPage_f51c1b72'](1);
})();
</script>

</body>
</html>

"
```
            lineageTag: 1811e3b7-300a-4058-978e-992ecc7f5d0e

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

