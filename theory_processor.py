#!/usr/bin/env python3
"""
Moduł do przetwarzania plików typu 'teoria'
Obsługuje tradycyjny format z sekcjami H1 i stronami rozdzielonymi '---'
"""

import hashlib
from text_utils import escape_quotes_for_dax


def split_by_h1(content):
    """Dzieli zawartość Markdown na sekcje po nagłówkach H1 (#)

    Returns:
        List[(title, content)] - lista tupli (tytuł sekcji, treść sekcji)
    """
    lines = content.split('\n')
    sections = []
    current_section_title = None
    current_section_lines = []

    for line in lines:
        # Sprawdź czy linia to nagłówek H1
        if line.startswith('# ') and not line.startswith('## '):
            # Zapisz poprzednią sekcję (jeśli istnieje)
            if current_section_title is not None or current_section_lines:
                section_content = '\n'.join(current_section_lines).strip()
                if section_content:
                    sections.append((current_section_title, section_content))

            # Rozpocznij nową sekcję
            current_section_title = line[2:].strip()  # Usuń '# ' z początku
            current_section_lines = []
        else:
            current_section_lines.append(line)

    # Zapisz ostatnią sekcję
    if current_section_title is not None or current_section_lines:
        section_content = '\n'.join(current_section_lines).strip()
        if section_content:
            sections.append((current_section_title, section_content))

    return sections


def create_powerbi_measure(title, pages, css, js):
    """Tworzy miarę Power BI w formacie HTML

    Args:
        title: str - tytuł miary
        pages: list[str] - lista stron HTML
        css: str - zawartość CSS (może być pusta)
        js: str - zawartość JS (może być pusta)

    Returns:
        str: kompletna miara Power BI w formacie DAX
    """

    # Zachowaj pełną nazwę z numeracją dla łatwiejszej segregacji
    # Np. "2. DAX - Zmienne" pozostaje jako "2. DAX - Zmienne"

    # Generuj unikalny ID dla tej wizualizacji (dla izolacji funkcji JS)
    unique_id = hashlib.md5(title.encode()).hexdigest()[:8]

    html_parts = []

    # DOCTYPE i HTML header
    html_parts.append("<!DOCTYPE html>\n")
    html_parts.append("<html lang='pl'>\n")
    html_parts.append("<head>\n")
    html_parts.append("    <meta charset='UTF-8'>\n")
    html_parts.append("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    html_parts.append(f"    <title>{title}</title>\n")

    # CSS - tylko jeśli jest niepusty
    if css.strip():
        for line in css.split('\n'):
            html_parts.append(f"    {line}\n")

    html_parts.append("</head>\n")
    html_parts.append("<body>\n\n")

    # Container i nawigacja (z unikalnymi nazwami funkcji onclick)
    html_parts.append(f"<div class='container' id='viz_{unique_id}'>\n")
    html_parts.append("    <!-- Nawigacja na górze -->\n")
    html_parts.append("    <div class='navigation'>\n")
    html_parts.append(f"        <button id='prevBtn_{unique_id}' onclick='changePage_{unique_id}(-1)'>← Poprzednia</button>\n")
    html_parts.append("        <span class='page-indicator'>\n")
    html_parts.append(f"            Strona <span id='currentPage_{unique_id}'>1</span> z <span id='totalPages_{unique_id}'>")
    html_parts.append(str(len(pages)))
    html_parts.append("</span>\n")
    html_parts.append("        </span>\n")
    html_parts.append(f"        <button id='nextBtn_{unique_id}' onclick='changePage_{unique_id}(1)'>Następna →</button>\n")
    html_parts.append("    </div>\n\n")

    # Pages
    for idx, page_content in enumerate(pages):
        page_class = "page active" if idx == 0 else "page"
        html_parts.append(f"    <!-- Strona {idx + 1} -->\n")
        html_parts.append(f"    <div class='{page_class}'>\n")

        # Dodaj zawartość strony z wcięciami
        for line in page_content.split('\n'):
            if line.strip():
                html_parts.append(f"        {line}\n")
            else:
                html_parts.append("\n")

        html_parts.append("    </div>\n\n")

    html_parts.append("</div>\n\n")

    # JavaScript - tylko jeśli jest niepusty
    if js.strip():
        js_with_id = js.replace('{{UNIQUE_ID}}', unique_id)
        for line in js_with_id.split('\n'):
            html_parts.append(f"{line}\n")

    html_parts.append("\n</body>\n")
    html_parts.append("</html>\n")

    # Złóż HTML w całość
    html_content = ''.join(html_parts)

    # KRYTYCZNE: Zamień wszystkie cudzysłowy " na apostrofy '
    # W DAX string jest otoczony ", więc wewnętrzne " zamykają string przedwcześnie
    html_content = escape_quotes_for_dax(html_content)

    # Formatuj jako miara Power BI (zachowaj pełną nazwę z numeracją)
    measure = f'{title} = \n\n"\n\n{html_content}\n"\n'

    return measure
