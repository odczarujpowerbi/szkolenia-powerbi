 *wystarczy edytować poniższy codeblock .json*
```json
{
    "assets": {
        "teoria": {
            "css": ["CSS - Teoria - Cherry.md"],
            "js": ["JS - Teoria.md"]
        },
        "quiz": {
            "css": ["CSS - Quiz - Cherry.md"],
            "js": ["JS - Quiz.md"]
        }
    },
    "generate_css_measures": true
}
```

> **Obecnie obsługuje**
> - `assets`: mapowanie typów treści (teoria, quiz) na pliki CSS i JS
>   - Każdy typ może mieć własne pliki CSS i JS z folderu `03. TEMPLATE`
>   - Dostępne pliki CSS i JS w folderze **03. TEMPLATE**
>   - Puste tablice `[]` oznaczają brak zewnętrznych assetów (użycie inline)
>
> - `generate_css_measures`: `true` (generuje osobne miary CSS*.html) lub `false` (wyłącza generowanie)