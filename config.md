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
        },
        "gaps": {
            "css": ["CSS - Gaps - Cherry.md"],
            "js": ["JS - Gaps.md"]
        }
    },
    "generate_css_measures": false
}
```

> **Obecnie obsługuje**
> - `assets`: mapowanie typów treści (teoria, quiz, gaps) na pliki CSS i JS
> 	  - Każdy typ może mieć własne pliki CSS i JS z folderu `100. RESOURCES`
> 	  - Dostępne pliki CSS i JS w folderze **100. RESOURCES**
> 	  - Puste tablice `[]` oznaczają brak zewnętrznych assetów (użycie inline)
> - `generate_css_measures`: `true` (generuje osobne miary CSS*.html) lub `false` (wyłącza generowanie)