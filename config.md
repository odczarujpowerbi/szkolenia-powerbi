 *wystarczy edytować poniższy codeblock .json*
```json
{
  "css_files": ["CSS - Czerwony.md"],
  "js_files": ["JS.md"],
  "generate_css_measures": true
}
```

> **Obecnie obsługuje**
> - `css_files`: podawanie pojedynczego pliku `["CSS.md"]`, wielu plików `["CSS1.md", "CSS2.md"]`, lub pustym `[]` (nie osadza CSS w HTML)
> 
> - `js_files`: podawanie pojedynczego pliku `["JS.md"]`, wielu plików `["JS1.md", "JS2.md"]`, lub pustym `[]` (nie osadza JS w HTML)
> 
> - `generate_css_measures`: `true` (generuje osobne miary CSS*.html) lub `false` (wyłącza generowanie)