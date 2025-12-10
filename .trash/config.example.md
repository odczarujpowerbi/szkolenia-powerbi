# Przykładowa konfiguracja dla convert_md_to_powerbi.py

Ten plik pokazuje wszystkie dostępne opcje konfiguracji.

## Nowy format z mapowaniem CSS/JS dla typów

```json
{
    "assets": {
        "teoria": {
            "css": ["CSS - Czerwony.md"],
            "js": ["JS.md"]
        },
        "quiz": {
            "css": [],
            "js": []
        }
    },
    "generate_css_measures": true
}
```

## Opis opcji

- **assets**: Mapowanie typów treści (`teoria`, `quiz`) na pliki CSS i JS
  - Każdy typ może mieć własne pliki CSS i JS
  - Puste tablice `[]` oznaczają brak zewnętrznych asset