# Instrukcja użycia konwertera Markdown → Power BI HTML

## Przegląd

Skrypt `convert_md_to_powerbi.py` automatyzuje proces konwersji plików Markdown na miary Power BI z HTML. Zastępuje ręczne przetwarzanie przez AI, zapewniając:

- ✅ **Spójność** - identyczny format dla wszystkich plików
- ✅ **Szybkość** - konwersja w sekundach zamiast minut
- ✅ **Skalowalność** - łatwe przetwarzanie wielu plików
- ✅ **Powtarzalność** - deterministyczne wyniki

## Wymagania

- Python 3.6+
- Pliki źródłowe w folderze `Theory/`
- Pliki template w folderze `Template/` (CSS.md, JS.md)

## Struktura projektu

```
odczarujpowerbi/
├── Theory/                      # Pliki źródłowe .md
│   ├── 1. Podstawy DAX.md
│   └── 2. DAX - Zmienne.md
├── Template/                    # Szablony CSS i JS
│   ├── CSS.md
│   └── JS.md
├── Output/                      # Wygenerowane miary Power BI (w vaulcie)
│   ├── 1. Podstawy DAX.html
│   └── 2. DAX - Zmienne.html
├── convert_md_to_powerbi.py     # Skrypt konwersji
└── USAGE.md                     # Instrukcja (ten plik)
```

## Użycie

### Podstawowe użycie

```bash
cd odczarujpowerbi
python convert_md_to_powerbi.py
```

Skrypt automatycznie:
1. Wczyta wszystkie pliki .md z `Theory/`
2. Wczyta templates z `Template/`
3. Wygeneruje miary Power BI w `Output/`

### Przykładowy output

```
=== Konwersja plikow Markdown -> Power BI HTML ===

Zrodlo: C:\...\odczarujpowerbi\Theory
Output: C:\...\odczarujpowerbi\Output

[OK] Skonwertowano: 1. Podstawy DAX
[OK] Skonwertowano: 2. DAX - Zmienne

=== Zakonczono! Wygenerowano 2 miar. ===
```

## Ważne zmiany dla Power BI

### Escapowanie znaków specjalnych
Skrypt automatycznie escapuje znaki specjalne dla kompatybilności z Power BI DAX:

- `<` → `\&lt;` (w treści, np. placeholdery `<wyrażenie1>`)
- `>` → `\&gt;` (w treści)
- Tagi HTML (`<div>`, `<span>` itp.) pozostają bez zmian

### Format wcięć
- Użycie **normalnych spacji** (4 spacje = 1 poziom wcięcia)
- Brak encji HTML `&nbsp;` dla lepszej czytelności

### Format outputu
- Rozszerzenie: `.html` (wcześniej `.md`)
- Lokalizacja: `Output/` w vaulcie Obsidian (wcześniej `../output/`)

## Format plików źródłowych

### Struktura Markdown

Pliki źródłowe w `Theory/` powinny używać następującego formatowania:

#### Separator stron
```markdown
---
```
Dzieli dokument na oddzielne strony (paginacja).

#### Nagłówki
```markdown
## Główny nagłówek         → <h1>
### Podtytuł               → <h2>
### Iteracja 1: [Value] = 1  → <h3> w <div class='iteration-box'>
```

#### Formatowanie inline
```markdown
**Bold text**              → <strong>Bold text</strong>
`inline code`              → <code>inline code</code>
```

#### Bloki kodu DAX
````markdown
```dax
VAR Suma = 100
RETURN Suma
```
````

Automatycznie dodawane jest podświetlanie składni:
- `VAR`, `RETURN` → `<span class='dax-keyword'>`
- `SUMX`, `FILTER` → `<span class='dax-function'>`
- `100`, `3.14` → `<span class='dax-number'>`
- `-- komentarz` → `<span class='dax-comment'>`

#### Listy
```markdown
- Element 1
- Element 2
- Element 3
```

#### Specjalne elementy

**Iteration box** (automatycznie wykrywane):
```markdown
### Iteracja 1: [Value] = 1
- `Kwadrat` = 1 × 1 = **1**
- RETURN zwraca: **1**
```
→ `<div class='iteration-box'>`

**Result box**:
```markdown
Wynik: **2500**
```
lub
```markdown
SUMX dodaje wszystkie wartości: **14**
```
lub
```markdown
### Suma końcowa:
SUMX dodaje wszystkie odchylenia: **-3**
```
→ `<div class='result-box'>`

## Format wyjściowy

Wygenerowane pliki w `Output/` mają format miary Power BI:

```
NazwaMiary =

"

<!DOCTYPE html>
<html lang='pl'>
<head>
    <meta charset='UTF-8'>
    <title>...</title>
    <style>
        /* CSS inline */
    </style>
</head>
<body>
    <div class='container'>
        <div class='navigation'>...</div>
        <div class='page active'>...</div>
        <div class='page'>...</div>
    </div>
    <script>
        /* JavaScript dla nawigacji */
    </script>
</body>
</html>

"
```

**Kluczowe cechy formatu:**
- Cały HTML w jednym stringu DAX (w cudzysłowach)
- Znaki `<` i `>` w placeholderach escapowane jako `\&lt;` i `\&gt;`
- Normalne spacje (4 spacje) zamiast `&nbsp;`
- Gotowe do skopiowania do Power BI Desktop

