#!/usr/bin/env python3
"""
Konwerter plików Markdown do miar Power BI z HTML
Automatyzuje proces tworzenia dokumentacji technicznej dla prezentacji Power BI
"""

import re
import os
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import uuid
import argparse
import json


def read_template(template_path, start_marker, end_marker):
    """Czyta template CSS lub JS z pliku markdown

    Args:
        template_path: ścieżka do pliku .md
        start_marker: nieużywane (zachowane dla kompatybilności wstecznej)
        end_marker: nieużywane (zachowane dla kompatybilności wstecznej)

    Returns:
        str: zawartość pierwszego bloku kodu z pliku markdown
    """
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Wyciągnij zawartość między znacznikami kodu
    match = re.search(rf'```\w+\s*\n(.*?)```', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def load_templates(template_dir, css_files=None, js_files=None):
    """Wczytuje pliki CSS i JS z folderu Template

    Args:
        template_dir: Path - folder z templateami
        css_files: list[str] | None - lista nazw plików CSS (None = ['CSS.md'])
        js_files: list[str] | None - lista nazw plików JS (None = ['JS.md'])

    Returns:
        tuple(str, str): (połączona zawartość CSS, połączona zawartość JS)
    """
    # Domyślne wartości
    if css_files is None:
        css_files = ['CSS.md']
    if js_files is None:
        js_files = ['JS.md']

    # Wczytaj wszystkie pliki CSS
    css_parts = []
    for css_file in css_files:
        if not css_file:  # Pomiń puste stringi
            continue
        css_path = template_dir / css_file
        if css_path.exists():
            content = read_template(css_path, '```css', '```')
            if content:
                css_parts.append(content)
                print(f"[OK] Wczytano CSS: {css_file}")
        else:
            print(f"[WARNING] Nie znaleziono pliku CSS: {css_file}")

    # Wczytaj wszystkie pliki JS
    js_parts = []
    for js_file in js_files:
        if not js_file:  # Pomiń puste stringi
            continue
        js_path = template_dir / js_file
        if js_path.exists():
            content = read_template(js_path, '```js', '```')
            if content:
                js_parts.append(content)
                print(f"[OK] Wczytano JS: {js_file}")
        else:
            print(f"[WARNING] Nie znaleziono pliku JS: {js_file}")

    # Połącz zawartość (z separatorem dla czytelności)
    css = '\n\n'.join(css_parts) if css_parts else ''
    js = '\n\n'.join(js_parts) if js_parts else ''

    return css, js


def highlight_dax_syntax(code):
    """Dodaje podświetlanie składni DAX"""
    lines = code.split('\n')
    result = []

    for line in lines:
        # Najpierw sprawdź czy linia zawiera komentarz
        if '--' in line:
            # Podziel na część przed i po komentarzu
            parts = line.split('--', 1)
            before_comment = parts[0]
            comment = '--' + parts[1] if len(parts) > 1 else ''

            # Przetworz część przed komentarzem
            processed_before = before_comment
            # Keywords
            for keyword in ['VAR', 'RETURN']:
                processed_before = re.sub(rf'\b({keyword})\b', r"<span class='dax-keyword'>\1</span>", processed_before)
            # Functions
            processed_before = re.sub(r'\b([A-Z][A-Z0-9_]+)(?=\s*\()', r"<span class='dax-function'>\1</span>", processed_before)
            # Numbers
            processed_before = re.sub(r'\b(\d+(?:\.\d+)?)\b', r"<span class='dax-number'>\1</span>", processed_before)

            # Dodaj przetworzony komentarz
            result.append(processed_before + f"<span class='dax-comment'>{comment}</span>")
        else:
            # Brak komentarza, przetwórz całą linię
            processed_line = line
            # Keywords
            for keyword in ['VAR', 'RETURN']:
                processed_line = re.sub(rf'\b({keyword})\b', r"<span class='dax-keyword'>\1</span>", processed_line)
            # Functions
            processed_line = re.sub(r'\b([A-Z][A-Z0-9_]+)(?=\s*\()', r"<span class='dax-function'>\1</span>", processed_line)
            # Numbers
            processed_line = re.sub(r'\b(\d+(?:\.\d+)?)\b', r"<span class='dax-number'>\1</span>", processed_line)

            result.append(processed_line)

    return '\n'.join(result)


def escape_html(text):
    """Escape specjalnych znaków HTML dla Power BI DAX"""
    # W DAX stringach trzeba escapować < i > jako &lt; i &gt;
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text


def process_inline_markdown(text):
    """Przetwarza inline markdown (bold, code, itp)"""
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    # Inline code (ale nie bloki kodu)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

    # Obsidian image embeds: ![[filename.png]] -> <img src='https://github.com/...' width='100%'>
    def replace_obsidian_image(match):
        filename = match.group(1)
        # Zakoduj spacje jako %20
        encoded_filename = filename.replace(' ', '%20')

        # Rozróżnij GIF i PNG/inne formaty
        if filename.lower().endswith('.gif'):
            # GIF używa raw.githubusercontent.com/grafiki-do-szkolenia
            return f"<img src='https://raw.githubusercontent.com/odczarujpowerbi/grafiki-do-szkolenia/main/{encoded_filename}' width='100%'>"
        else:
            # PNG i inne używają github.com/szkolenia-powerbi/blob/main/bin + ?raw=true
            return f"<img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/{encoded_filename}?raw=true' width='100%'>"

    text = re.sub(r'!\[\[(.*?)\]\]', replace_obsidian_image, text)

    return text


def convert_markdown_to_html(md_content):
    """Konwertuje zawartość markdown pojedynczej strony na HTML"""
    lines = md_content.strip().split('\n')
    html_lines = []
    in_code_block = False
    in_list = False
    code_block = []
    code_lang = None

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.strip().startswith('```'):
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False

            if not in_code_block:
                in_code_block = True
                code_lang = line.strip()[3:].strip() or 'dax'
                code_block = []
            else:
                # Zakończ blok kodu
                in_code_block = False
                code_content = '\n'.join(code_block)

                if code_lang == 'dax':
                    code_content = highlight_dax_syntax(code_content)

                html_lines.append(f"<pre><code>{code_content}</code></pre>\n")
                code_block = []
                code_lang = None
            i += 1
            continue

        if in_code_block:
            code_block.append(escape_html(line))
            i += 1
            continue

        # Standalone images: ![[filename.png]]
        if line.strip().startswith('![[') and line.strip().endswith(']]'):
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False

            # Wyciągnij nazwę pliku
            filename = line.strip()[3:-2]  # Usuń ![[ i ]]
            # Zakoduj spacje jako %20
            encoded_filename = filename.replace(' ', '%20')

            # Rozróżnij GIF i PNG/inne formaty
            if filename.lower().endswith('.gif'):
                # GIF używa raw.githubusercontent.com/grafiki-do-szkolenia
                html_lines.append(f"<img src='https://raw.githubusercontent.com/odczarujpowerbi/grafiki-do-szkolenia/main/{encoded_filename}' width='100%'>\n")
            else:
                # PNG i inne używają github.com/szkolenia-powerbi/blob/main/bin + ?raw=true
                html_lines.append(f"<img src='https://github.com/odczarujpowerbi/szkolenia-powerbi/blob/main/bin/{encoded_filename}?raw=true' width='100%'>\n")
            i += 1
            continue

        # Markdown tables: | col1 | col2 |
        if line.strip().startswith('|') and '|' in line.strip()[1:]:
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False

            # Zbierz wszystkie wiersze tabeli
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip())
                i += 1

            if len(table_lines) >= 2:
                # Konwertuj tabelę na HTML
                html_lines.append('<table>\n')

                # Pierwszy wiersz to nagłówki
                headers = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]
                html_lines.append('  <thead>\n    <tr>\n')
                for header in headers:
                    html_lines.append(f'      <th>{process_inline_markdown(header)}</th>\n')
                html_lines.append('    </tr>\n  </thead>\n')

                # Pomiń drugi wiersz (separator: | --- | --- |)
                # Pozostałe wiersze to dane
                html_lines.append('  <tbody>\n')
                for row_line in table_lines[2:]:
                    cells = [cell.strip() for cell in row_line.split('|')[1:-1]]
                    html_lines.append('    <tr>\n')
                    for cell in cells:
                        html_lines.append(f'      <td>{process_inline_markdown(cell)}</td>\n')
                    html_lines.append('    </tr>\n')
                html_lines.append('  </tbody>\n')
                html_lines.append('</table>\n')
            continue

        # Headings ## (h1)
        if line.startswith('## '):
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False
            html_lines.append(f"<h1>{process_inline_markdown(line[3:])}</h1>\n")
            i += 1
            continue

        # Result boxes - "Suma końcowa:" jako nagłówek w result-box (sprawdź PRZED innymi ###)
        if line.startswith('### ') and 'Suma końcowa:' in line:
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False

            html_lines.append("<div class='result-box'>\n")
            html_lines.append(f"<h3>{process_inline_markdown(line[4:])}</h3>\n")
            i += 1

            # Zbierz zawartość result-box
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('#'):
                html_lines.append(f"<p>{process_inline_markdown(lines[i])}</p>\n")
                i += 1

            html_lines.append("</div>\n")
            continue

        # Headings ### (może być h2 lub h3 w iteration-box)
        if line.startswith('### '):
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False

            # Sprawdź czy to nagłówek iteracji lub "Przed iteracją"
            heading_text = line[4:].strip()
            if 'Iteracja' in heading_text or 'Przed iteracją' in heading_text:
                # Zbierz zawartość do następnego nagłówka ### lub końca
                html_lines.append("<div class='iteration-box'>\n")
                html_lines.append(f"<h3>{process_inline_markdown(heading_text)}</h3>\n")

                i += 1
                local_list_open = False
                while i < len(lines):
                    next_line = lines[i]

                    # Zakończ iteration-box gdy napotkamy:
                    # - kolejny nagłówek ###
                    # - nagłówek ##
                    # - linię ze "Suma końcowa" lub "SUMX dodaje" (result-box)
                    if next_line.startswith('###') or next_line.startswith('##'):
                        break
                    if next_line.strip().startswith('Suma końcowa:') or 'SUMX dodaje' in next_line:
                        break

                    # Lista
                    if next_line.startswith('- '):
                        if not local_list_open:
                            html_lines.append('<ul>\n')
                            local_list_open = True
                        html_lines.append(f"<li>{process_inline_markdown(next_line[2:])}</li>\n")
                        i += 1
                        continue

                    # Pusta linia
                    if not next_line.strip():
                        if local_list_open:
                            html_lines.append('</ul>\n')
                            local_list_open = False
                        i += 1
                        continue

                    # Zwykły paragraf
                    if local_list_open:
                        html_lines.append('</ul>\n')
                        local_list_open = False
                    html_lines.append(f"<p>{process_inline_markdown(next_line)}</p>\n")
                    i += 1

                # Zamknij otwartą listę i box
                if local_list_open:
                    html_lines.append('</ul>\n')
                html_lines.append("</div>\n")
                continue
            else:
                # Zwykły nagłówek h2
                html_lines.append(f"<h2>{process_inline_markdown(heading_text)}</h2>\n")
                i += 1
                continue

        # Result boxes - "Wynik:" lub "SUMX dodaje"
        if line.strip().startswith('Wynik:') or 'SUMX dodaje' in line:
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False

            html_lines.append(f"<div class='result-box'>\n{process_inline_markdown(line)}\n</div>\n")
            i += 1
            continue

        # Numbered lists (1., 2., etc.)
        numbered_match = re.match(r'^(\d+)\.\s+(.+)', line)
        if numbered_match:
            if not in_list:
                html_lines.append('<ol>\n')
                in_list = 'ol'
            elif in_list == 'ul':
                html_lines.append('</ul>\n')
                html_lines.append('<ol>\n')
                in_list = 'ol'

            # Sprawdź czy następne linie to wcięte bullety (należące do tego <li>)
            content = numbered_match.group(2)
            html_lines.append(f"<li>{process_inline_markdown(content)}")

            i += 1
            # Sprawdź czy następne linie są wcięte (rozpoczynają się od spacji lub tabulatora)
            nested_items = []
            while i < len(lines):
                next_line = lines[i]
                # Wcięty bullet (spacja lub tab + "- ")
                if re.match(r'^[\s\t]+-\s+(.+)', next_line):
                    nested_match = re.match(r'^[\s\t]+-\s+(.+)', next_line)
                    nested_items.append(nested_match.group(1))
                    i += 1
                # Pusta linia lub kolejny element listy głównej
                elif not next_line.strip() or re.match(r'^\d+\.\s+', next_line):
                    break
                else:
                    break

            # Jeśli są zagnieżdżone elementy, dodaj <ul>
            if nested_items:
                html_lines.append('\n<ul>\n')
                for nested_item in nested_items:
                    html_lines.append(f"<li>{process_inline_markdown(nested_item)}</li>\n")
                html_lines.append('</ul>\n')

            html_lines.append("</li>\n")
            continue

        # Unordered lists (-) - tylko na głównym poziomie (nie wcięte)
        if line.startswith('- ') and not re.match(r'^[\s\t]', line):
            if not in_list:
                html_lines.append('<ul>\n')
                in_list = 'ul'
            elif in_list == 'ol':
                html_lines.append('</ol>\n')
                html_lines.append('<ul>\n')
                in_list = 'ul'
            html_lines.append(f"<li>{process_inline_markdown(line[2:])}</li>\n")
            i += 1
            continue

        # Empty lines
        if not line.strip():
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False
            i += 1
            continue

        # Regular paragraphs
        if in_list:
            html_lines.append(f'</{in_list}>\n')
            in_list = False
        if line.strip():
            html_lines.append(f"<p>{process_inline_markdown(line)}</p>\n")
        i += 1

    # Close any open lists
    if in_list:
        html_lines.append(f'</{in_list}>\n')

    return ''.join(html_lines)


def escape_quotes_for_dax(text):
    """Zamienia wszystkie cudzysłowy na apostrofy dla kompatybilności z DAX

    W miarze DAX string jest otoczony cudzysłowami, więc wewnętrzne cudzysłowy
    muszą być zamienione na apostrofy aby nie zamykać stringa przedwcześnie.
    """
    return text.replace('"', "'")


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
    import hashlib
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

    # KRYTYCZNE: Zamień wszystkie cudzysłowy " na &quot;
    # W DAX string jest otoczony ", więc wewnętrzne " zamykają string przedwcześnie
    html_content = escape_quotes_for_dax(html_content)

    # Formatuj jako miara Power BI (zachowaj pełną nazwę z numeracją)
    measure = f'{title} = \n\n"\n\n{html_content}\n"\n'

    return measure


def create_quiz_html(title, questions):
    """Tworzy interaktywny quiz w formacie HTML

    Args:
        title: str - tytuł quizu
        questions: list[dict] - lista pytań z odpowiedziami
            [{'question': str, 'answers': [str], 'correct': int, 'explanation': str}]

    Returns:
        str: kompletny HTML z quizem (gotowy do osadzenia w miarze Power BI)
    """
    total_questions = len(questions)
    total_pages = total_questions + 1  # pytania + strona podsumowania

    html_parts = []

    # DOCTYPE i HTML header
    html_parts.append("<!DOCTYPE html>\n")
    html_parts.append("<html lang='pl'>\n")
    html_parts.append("<head>\n")
    html_parts.append("    <meta charset='UTF-8'>\n")
    html_parts.append("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    html_parts.append(f"    <title>{title}</title>\n")

    # Inline CSS (skopiowany ze wzoru)
    html_parts.append("    <style>\n")
    html_parts.append("""        * {
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
""")
    html_parts.append("    </style>\n")
    html_parts.append("</head>\n")
    html_parts.append("<body>\n\n")

    # Container i nawigacja
    html_parts.append("<div class='container'>\n")
    html_parts.append("    <!-- Nawigacja na górze -->\n")
    html_parts.append("    <div class='navigation'>\n")
    html_parts.append("        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>\n")
    html_parts.append("        <span class='page-indicator'>\n")
    html_parts.append("            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>")
    html_parts.append(str(total_pages))
    html_parts.append("</span>\n")
    html_parts.append("        </span>\n")
    html_parts.append("        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>\n")
    html_parts.append("    </div>\n\n")

    # Generuj strony z pytaniami
    for idx, q in enumerate(questions):
        page_class = "page active" if idx == 0 else "page"
        html_parts.append(f"    <!-- Pytanie {idx + 1} -->\n")
        html_parts.append(f"    <div class='{page_class}'>\n")
        html_parts.append(f"        <h1>Pytanie {idx + 1}</h1>\n")
        html_parts.append("        <div class='question-box'>\n")
        html_parts.append(f"            <p><strong>{escape_html(q['question'])}</strong></p>\n")
        html_parts.append("        </div>\n")
        html_parts.append("        <div class='answers'>\n")

        # Odpowiedzi
        for ans_idx, answer in enumerate(q['answers']):
            html_parts.append(f"            <div class='answer-option' onclick='selectAnswer({idx}, {ans_idx})'>\n")
            html_parts.append(f"                {escape_html(answer)}\n")
            html_parts.append("            </div>\n")

        html_parts.append("        </div>\n")
        html_parts.append(f"        <button class='check-button' onclick='checkAnswer({idx}, {q['correct']})'>Sprawdź odpowiedź</button>\n")
        html_parts.append(f"        <div class='feedback' id='feedback-{idx}'></div>\n")
        html_parts.append("    </div>\n\n")

    # Strona podsumowania
    html_parts.append("    <!-- Podsumowanie quizu -->\n")
    html_parts.append("    <div class='page'>\n")
    html_parts.append("        <h1>Podsumowanie quizu</h1>\n")
    html_parts.append("        <div class='score-box' id='finalScore'>\n")
    html_parts.append(f"            Twój wynik: <span id='scoreText'>0/{total_questions}</span> (<span id='percentText'>0%</span>)\n")
    html_parts.append("        </div>\n")
    html_parts.append("        <div id='summaryContent'></div>\n")
    html_parts.append("        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'>🔄 Rozpocznij quiz od nowa</button>\n")
    html_parts.append("    </div>\n")
    html_parts.append("</div>\n\n")

    # JavaScript
    html_parts.append("<script>\n")
    html_parts.append(f"    let currentPage = 1;\n")
    html_parts.append(f"    const totalPages = {total_pages};\n")
    html_parts.append(f"    const totalQuestions = {total_questions};\n")
    html_parts.append("    \n")
    html_parts.append(f"    const userAnswers = new Array(totalQuestions).fill(null);\n")
    html_parts.append(f"    const answeredQuestions = new Array(totalQuestions).fill(false);\n")
    html_parts.append("    \n")

    # Array z poprawnymi odpowiedziami
    correct_answers = [str(q['correct']) for q in questions]
    html_parts.append(f"    const correctAnswers = [{', '.join(correct_answers)}];\n")
    html_parts.append("    \n")

    # Array z wyjaśnieniami
    html_parts.append("    const explanations = [\n")
    for idx, q in enumerate(questions):
        explanation_escaped = escape_quotes_for_dax(q['explanation'])
        comma = "," if idx < len(questions) - 1 else ""
        html_parts.append(f"        '{explanation_escaped}'{comma}\n")
    html_parts.append("    ];\n")
    html_parts.append("    \n")

    # Reszta JavaScript (skopiowana ze wzoru)
    html_parts.append("""    document.getElementById('totalPages').textContent = totalPages;

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
            feedback.textContent = '⚠️ Proszę najpierw wybrać odpowiedź!';
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
""")
    html_parts.append("</script>\n\n")
    html_parts.append("</body>\n")
    html_parts.append("</html>\n")

    return ''.join(html_parts)


def parse_quiz_markdown(content):
    """Parsuje plik quizu w formacie markdown

    Format quizu:
    # Tytuł quizu

    ## Pytanie 1
    **Treść pytania**
    - A) Odpowiedź A
    - B) Odpowiedź B
    - C) Odpowiedź C
    - D) Odpowiedź D
    ---
    correct: 0
    explanation: Wyjaśnienie

    Args:
        content: str - zawartość pliku quizu (bez frontmatter)

    Returns:
        tuple: (quiz_title, questions_list)
            - quiz_title: tytuł quizu (z pierwszego # H1)
            - questions_list: lista słowników z pytaniami
              [{'question': str, 'answers': [str], 'correct': int, 'explanation': str}]
    """
    lines = content.split('\n')

    # Wyciągnij tytuł quizu (pierwszy # H1)
    quiz_title = "Quiz"
    for line in lines:
        if line.startswith('# '):
            quiz_title = line[2:].strip()
            break

    # Podziel na sekcje pytań (## Pytanie)
    questions = []
    current_question = None
    current_answers = []
    in_metadata = False
    metadata_lines = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Nowe pytanie
        if line.startswith('## '):
            # Zapisz poprzednie pytanie (jeśli istnieje)
            if current_question and current_answers:
                # Parsuj metadata
                correct_idx = 0
                explanation = ""
                for meta_line in metadata_lines:
                    if meta_line.startswith('correct:'):
                        correct_idx = int(meta_line.split(':', 1)[1].strip())
                    elif meta_line.startswith('explanation:'):
                        explanation = meta_line.split(':', 1)[1].strip()

                questions.append({
                    'question': current_question,
                    'answers': current_answers,
                    'correct': correct_idx,
                    'explanation': explanation
                })

            # Reset dla nowego pytania
            current_question = None
            current_answers = []
            in_metadata = False
            metadata_lines = []
            i += 1
            continue

        # Treść pytania (bold **text**)
        if line.startswith('**') and line.endswith('**'):
            current_question = line[2:-2]
            i += 1
            continue

        # Odpowiedzi (- A), - B), etc.)
        if line.startswith('- '):
            current_answers.append(line[2:].strip())
            i += 1
            continue

        # Separator metadata (---)
        if line == '---':
            in_metadata = True
            i += 1
            continue

        # Metadata (correct, explanation)
        if in_metadata and line:
            metadata_lines.append(line)

        i += 1

    # Zapisz ostatnie pytanie
    if current_question and current_answers:
        correct_idx = 0
        explanation = ""
        for meta_line in metadata_lines:
            if meta_line.startswith('correct:'):
                correct_idx = int(meta_line.split(':', 1)[1].strip())
            elif meta_line.startswith('explanation:'):
                explanation = meta_line.split(':', 1)[1].strip()

        questions.append({
            'question': current_question,
            'answers': current_answers,
            'correct': correct_idx,
            'explanation': explanation
        })

    return quiz_title, questions


def parse_frontmatter(content):
    """Wyciąga properties (frontmatter) z pliku Markdown w formacie Obsidian

    Args:
        content: str - pełna zawartość pliku markdown

    Returns:
        tuple: (properties_dict, content_without_frontmatter)
            - properties_dict: słownik z properties (np. {'type': 'teoria'})
            - content_without_frontmatter: treść pliku bez sekcji properties
    """
    # Sprawdź czy plik zaczyna się od ---
    if not content.strip().startswith('---'):
        return {}, content

    # Znajdź zamykający ---
    lines = content.split('\n')
    if len(lines) < 3:
        return {}, content

    # Pomiń pierwszy --- (indeks 0)
    end_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_index = i
            break

    if end_index is None:
        return {}, content

    # Parsuj properties (format: key: value)
    properties = {}
    for i in range(1, end_index):
        line = lines[i].strip()
        if ':' in line:
            key, value = line.split(':', 1)
            properties[key.strip()] = value.strip()

    # Zwróć properties i treść bez frontmatter
    content_without_frontmatter = '\n'.join(lines[end_index + 1:]).strip()
    return properties, content_without_frontmatter


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


def convert_file(input_path, output_dir, css, js):
    """Konwertuje pojedynczy plik markdown do miar Power BI

    Obsługuje dwa typy plików:
    - type='teoria': tradycyjny format z sekcjami i stronami (split by H1)
    - type='quiz': interaktywny quiz z pytaniami

    Returns:
        int - liczba wygenerowanych plików HTML
    """

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalizuj cudzysłowy już na początku (typograficzne → ASCII)
    content = normalize_quotes(content)

    # Parsuj frontmatter (properties)
    properties, content_without_frontmatter = parse_frontmatter(content)
    file_type = properties.get('type', 'teoria')  # Domyślnie 'teoria'

    # Pobierz bazową nazwę pliku (bez rozszerzenia)
    base_name = Path(input_path).stem

    # QUIZ: Obsługa plików typu 'quiz'
    if file_type == 'quiz':
        # Parsuj quiz
        quiz_title, questions = parse_quiz_markdown(content_without_frontmatter)

        if not questions:
            print(f"[WARNING] Brak pytań w quizie: {input_path.name}")
            return 0

        # Generuj HTML quizu
        quiz_html = create_quiz_html(quiz_title, questions)

        # Escapuj cudzysłowy dla DAX
        quiz_html = escape_quotes_for_dax(quiz_html)

        # Formatuj jako miara Power BI
        measure = f'{base_name} = \n\n"\n\n{quiz_html}\n"\n'

        # Zapisz do pliku
        output_filename = f"{base_name}.html"
        output_path = output_dir / output_filename

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(measure)

        print(f"[OK] Skonwertowano quiz: {output_filename}")
        return 1

    # TEORIA: Obsługa plików typu 'teoria' (oryginalna logika)
    content = content_without_frontmatter

    # Podziel na sekcje po nagłówkach H1
    sections = split_by_h1(content)

    if not sections:
        print(f"[WARNING] Brak treści w pliku: {input_path.name}")
        return 0

    # Pobierz bazową nazwę pliku (bez rozszerzenia)
    base_name = Path(input_path).stem

    generated_count = 0

    # Konwertuj każdą sekcję na osobny plik HTML
    for section_title, section_content in sections:
        # Podziel sekcję na strony po '---'
        pages_raw = section_content.split('\n---\n')

        # Konwertuj każdą stronę
        pages_html = []
        for page_md in pages_raw:
            if page_md.strip():
                page_html = convert_markdown_to_html(page_md)
                pages_html.append(page_html)

        if not pages_html:
            continue

        # Określ nazwę pliku wyjściowego
        if section_title is None:
            # Treść przed pierwszym H1
            output_filename = f"{base_name}.html"
            title = base_name
        else:
            # Sekcja z nagłówkiem H1
            output_filename = f"{base_name} - {section_title}.html"
            title = section_title

        output_path = output_dir / output_filename

        # Stwórz miarę Power BI
        measure = create_powerbi_measure(title, pages_html, css, js)

        # Zapisz do pliku
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(measure)

        print(f"[OK] Skonwertowano: {output_filename}")
        generated_count += 1

    return generated_count


def parse_arguments():
    """Parsuje argumenty linii poleceń

    Returns:
        argparse.Namespace: sparsowane argumenty
    """
    parser = argparse.ArgumentParser(
        description='Konwerter plików Markdown do miar Power BI z HTML',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Przykłady użycia:

  # Domyślnie (CSS.md i JS.md):
  python convert_md_to_powerbi.py

  # Bez CSS i JS:
  python convert_md_to_powerbi.py --css --js

  # Własne pliki CSS i JS:
  python convert_md_to_powerbi.py --css custom.css --js custom.js

  # Wiele plików CSS:
  python convert_md_to_powerbi.py --css base.css theme.css --js app.js

  # Tylko CSS, bez JS:
  python convert_md_to_powerbi.py --css styles.css --js

  # Z pliku konfiguracyjnego (.md lub .json):
  python convert_md_to_powerbi.py --config config.md
        """
    )

    parser.add_argument(
        '--css',
        nargs='*',
        default=None,
        metavar='FILE',
        help='Pliki CSS do wczytania (bez argumentów = pomiń CSS, domyślnie: CSS.md)'
    )

    parser.add_argument(
        '--js',
        nargs='*',
        default=None,
        metavar='FILE',
        help='Pliki JS do wczytania (bez argumentów = pomiń JS, domyślnie: JS.md)'
    )

    parser.add_argument(
        '--config',
        type=str,
        metavar='FILE',
        help='Plik JSON z konfiguracją (nadpisuje --css i --js)'
    )

    return parser.parse_args()


def load_config(config_path):
    """Wczytuje konfigurację z pliku .md zawierającego blok JSON lub z pliku .json

    Format pliku .md:
    ```json
    {
        "css_files": ["CSS.md", "theme.css"],
        "js_files": ["JS.md"],
        "generate_css_measures": true
    }
    ```

    Lub plik .json:
    {
        "css_files": ["CSS.md"],
        "js_files": ["JS.md"],
        "generate_css_measures": true
    }

    Args:
        config_path: str - ścieżka do pliku .md lub .json

    Returns:
        dict: słownik z kluczami 'css_files', 'js_files', 'generate_css_measures'
    """
    # Konwertuj na Path jeśli to string
    if isinstance(config_path, str):
        config_path = Path(config_path)

    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Jeśli to plik .md, wyciągnij JSON z bloku kodu
    if config_path.suffix == '.md':
        match = re.search(r'```json\s*\n(.*?)```', content, re.DOTALL)
        if match:
            json_content = match.group(1).strip()
            config = json.loads(json_content)
        else:
            raise ValueError(f"Nie znaleziono bloku ```json w pliku {config_path}")
    else:
        # Plik .json - parsuj bezpośrednio
        config = json.loads(content)

    return {
        'css_files': config.get('css_files', ['CSS.md']),
        'js_files': config.get('js_files', ['JS.md']),
        'generate_css_measures': config.get('generate_css_measures', True)
    }


def generate_css_measures(template_dir, output_dir):
    """Generuje osobne miary Power BI dla każdego pliku CSS z folderu 03. TEMPLATE

    Args:
        template_dir: Path - folder z templateami (03. TEMPLATE)
        output_dir: Path - folder wyjściowy (02. OUTPUT)

    Returns:
        int - liczba wygenerowanych miar CSS
    """
    # Znajdź wszystkie pliki zaczynające się od "CSS"
    css_files = sorted(template_dir.glob('CSS*.md'))

    if not css_files:
        print("[INFO] Nie znaleziono plików CSS*.md do wygenerowania osobnych miar")
        return 0

    generated_count = 0

    for css_file in css_files:
        # Wczytaj zawartość CSS
        css_content = read_template(css_file, '```css', '```')

        if not css_content:
            print(f"[WARNING] Pusty CSS w pliku: {css_file.name}")
            continue

        # Nazwa miary = nazwa pliku bez rozszerzenia (np. "CSS" lub "CSS - Dark Mode")
        measure_name = css_file.stem

        # Buduj miarę jako czysty HTML ze stylem
        measure_html = f"<style>\n{css_content}\n</style>"

        # Escapuj cudzysłowy dla DAX
        measure_html = escape_quotes_for_dax(measure_html)

        # Formatuj jako miarę Power BI
        measure = f'{measure_name} = \n\n"\n{measure_html}\n"\n'

        # Zapisz do pliku
        output_path = output_dir / f"{measure_name}.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(measure)

        print(f"[OK] Wygenerowano miarę CSS: {measure_name}.html")
        generated_count += 1

    return generated_count


def main():
    """Główna funkcja programu"""

    # Parsuj argumenty
    args = parse_arguments()

    # Ścieżki
    script_dir = Path(__file__).parent
    theory_dir = script_dir / '01. THEORY'
    template_dir = script_dir / '03. TEMPLATE'
    output_dir = script_dir / '02. OUTPUT'  # Output HTML
    tmdl_dir = output_dir / 'TMDL'  # Folder TMDL wewnątrz OUTPUT

    # Sprawdź czy foldery istnieją
    if not theory_dir.exists():
        print(f"[ERROR] Folder 01. THEORY nie istnieje: {theory_dir}")
        return

    if not template_dir.exists():
        print(f"[ERROR] Folder 03. TEMPLATE nie istnieje: {template_dir}")
        return

    # Utwórz folder output jeśli nie istnieje
    output_dir.mkdir(exist_ok=True)

    # Ustal które pliki CSS/JS wczytać i czy generować miary CSS
    css_files = None  # None = domyślne ['CSS.md']
    js_files = None   # None = domyślne ['JS.md']
    should_generate_css_measures = True  # Domyślnie włączone

    # Sprawdź czy podano plik konfiguracyjny
    if args.config:
        config_path = Path(args.config)
        if not config_path.exists():
            print(f"[ERROR] Plik konfiguracyjny nie istnieje: {args.config}")
            return
        print(f"\n[INFO] Wczytuję konfigurację z: {args.config}\n")
        config = load_config(config_path)
        css_files = config.get('css_files')
        js_files = config.get('js_files')
        should_generate_css_measures = config.get('generate_css_measures', True)
    else:
        # Argumenty linii poleceń nadpisują domyślne wartości
        if args.css is not None:
            css_files = args.css if args.css else []  # pusta lista = pomiń CSS
        if args.js is not None:
            js_files = args.js if args.js else []  # pusta lista = pomiń JS

    # Generuj osobne miary CSS (jeśli włączone)
    css_measures_count = 0
    if should_generate_css_measures:
        print(f"\n=== Generowanie miar CSS ===\n")
        css_measures_count = generate_css_measures(template_dir, output_dir)
    else:
        print(f"\n[INFO] Generowanie miar CSS wyłączone w konfiguracji\n")

    # Wczytaj templates
    css, js = load_templates(template_dir, css_files, js_files)

    # Przetwórz wszystkie pliki .md w 01. THEORY
    md_files = list(theory_dir.glob('*.md'))

    if not md_files:
        print(f"[ERROR] Nie znaleziono plikow .md w folderze 01. THEORY: {theory_dir}")
        return

    print(f"\n=== Konwersja plikow Markdown -> Power BI HTML ===\n")
    print(f"Zrodlo: {theory_dir}")
    print(f"Output: {output_dir}\n")

    total_generated = 0
    for md_file in md_files:
        try:
            count = convert_file(md_file, output_dir, css, js)
            total_generated += count
        except Exception as e:
            print(f"[ERROR] Blad przy konwersji {md_file.name}: {e}")

    print(f"\n=== Zakonczono konwersje Markdown! ===")
    print(f"Wygenerowano {total_generated} plik(ow) HTML z {len(md_files)} plik(ow) Markdown.")
    if css_measures_count > 0:
        print(f"Wygenerowano {css_measures_count} miar(y) CSS.")
    print()

    # Generuj plik TMDL
    print(f"\n=== Generowanie pliku TMDL ===\n")
    generate_tmdl(output_dir, tmdl_dir)
    print()

    # Podsumowanie
    total_files = total_generated + css_measures_count

    # Okienko z sukcesem
    root = tk.Tk()
    root.withdraw()  # Ukryj główne okno

    summary_message = f"✓ Pomyślnie wygenerowano {total_files} plik(ów) HTML!\n\n"
    summary_message += f"• {total_generated} miar(y) z Markdown\n"
    if css_measures_count > 0:
        summary_message += f"• {css_measures_count} miar(y) CSS\n"
    summary_message += f"\nOutput HTML: {output_dir}\n"
    summary_message += f"Plik TMDL: {tmdl_dir}\n\n"
    summary_message += f"Pliki gotowe do użycia w Power BI."

    messagebox.showinfo("Konwersja zakończona", summary_message)
    root.destroy()


def normalize_quotes(text):
    """Zamienia typograficzne cudzysłowy na zwykłe ASCII

    Zamienia:
    - " " (smart quotes) → "
    - ' ' (smart single quotes) → '
    - „ " (polskie cudzysłowy) → "
    """
    # Typograficzne double quotes
    text = text.replace('"', '"')  # Left double quotation mark
    text = text.replace('"', '"')  # Right double quotation mark
    text = text.replace('„', '"')  # Polish opening quote
    text = text.replace('"', '"')  # Polish closing quote

    # Typograficzne single quotes
    text = text.replace(''', "'")  # Left single quotation mark
    text = text.replace(''', "'")  # Right single quotation mark
    text = text.replace('‚', "'")  # Single low-9 quotation mark

    return text


def read_measure_from_html(html_file_path):
    """Czyta plik HTML i wyciąga nazwę miary oraz jej zawartość

    Returns:
        tuple(str, str) - (nazwa_miary, zawartość_miary)
    """
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Plik ma format: "NazwaMiary = \n\n"...\n\n""
    # Wyciągnij nazwę miary (pierwsza linia przed " = ")
    lines = content.split('\n')
    if not lines:
        return None, None

    measure_name = lines[0].replace(' = ', '').strip()

    # Całą zawartość od linii 2 (po " = ")
    measure_content = '\n'.join(lines[1:])

    return measure_name, measure_content


def extract_measure_metadata(measure_name):
    """Wyciąga metadane z nazwy miary do użycia w parametrze pHTML

    Args:
        measure_name: str - pełna nazwa miary (np. "01. Podstawy DAX - Funkcje filtrujące")

    Returns:
        tuple: (full_name, short_name, module_number)
            - full_name: pełna nazwa (np. "01. Podstawy DAX - Funkcje filtrujące")
            - short_name: skrócona nazwa (np. "F. FILTRUJĄCE")
            - module_number: numer modułu (np. "01")
    """
    full_name = measure_name

    # Wyciągnij numer modułu (cyfry na początku do pierwszej kropki)
    module_match = re.match(r'^(\d+)\.', measure_name)
    module_number = module_match.group(1) if module_match else "00"

    # Stwórz short_name z części po ostatnim " - " lub z całej nazwy
    if ' - ' in measure_name:
        # Weź część po ostatnim " - "
        short_part = measure_name.split(' - ')[-1]
    else:
        # Weź część po pierwszej kropce (usuń numerację)
        short_part = re.sub(r'^\d+\.\s*', '', measure_name)

    # Skróć do wielkich liter i pierwszych słów
    # Np. "Funkcje filtrujące" -> "F. FILTRUJĄCE"
    words = short_part.split()
    if len(words) > 0:
        # Pierwsza litera pierwszego słowa + ". " + reszta wielkimi literami
        if len(words) == 1:
            short_name = words[0].upper()
        else:
            short_name = f"{words[0][0].upper()}. {' '.join(words[1:]).upper()}"
    else:
        short_name = short_part.upper()

    return full_name, short_name, module_number


def generate_parameter_file(measures, tmdl_dir):
    """Generuje osobny plik _Parametr.md z tabelą kalkulowaną DAX zawierającą metadane miar

    Args:
        measures: list[(measure_name, measure_content)] - lista miar
        tmdl_dir: Path - folder docelowy (02. OUTPUT/TMDL)
    """
    param_lines = []

    # Nagłówek - struktura 1:1 jak w _pTeoria
    param_lines.append("_pHTML = {\n")

    # Dodaj wiersze z danymi jako krotki
    for idx, (measure_name, _) in enumerate(measures):
        full_name, short_name, module_number = extract_measure_metadata(measure_name)

        # Escapuj cudzysłowy dla DAX (podwójny cudzysłów)
        full_name_escaped = full_name.replace('"', '""')
        short_name_escaped = short_name.replace('"', '""')

        # Format: ("Pełna nazwa", NAMEOF('_HTML'[Nazwa]), sortowanie, "SKRÓCONA", "moduł")
        param_lines.append(f'    ("{full_name_escaped}", NAMEOF(\'_HTML\'[{measure_name}]), {idx}, "{short_name_escaped}", "{module_number}"),\n')

    # Usuń ostatni przecinek z ostatniego wiersza
    if param_lines[-1].endswith(',\n'):
        param_lines[-1] = param_lines[-1][:-2] + '\n'

    # Zamknij nawias klamrowy
    param_lines.append("}\n")

    # Zapisz do pliku
    param_file_path = tmdl_dir / "_Parametr.md"
    with open(param_file_path, 'w', encoding='utf-8') as f:
        f.writelines(param_lines)

    print(f"[OK] Wygenerowano parametr: {param_file_path}")
    print(f"     Liczba wierszy metadanych: {len(measures)}")


def generate_tmdl(output_dir, tmdl_dir):
    """Generuje plik TMDL ze wszystkimi miarami z folderu 02. OUTPUT

    Args:
        output_dir: Path - folder z plikami HTML (02. OUTPUT)
        tmdl_dir: Path - folder docelowy dla pliku TMDL (02. OUTPUT/TMDL)
    """
    # Znajdź wszystkie pliki HTML
    html_files = sorted(output_dir.glob('*.html'))

    if not html_files:
        print("[WARNING] Brak plików HTML do wygenerowania TMDL")
        return

    # Utwórz folder TMDL jeśli nie istnieje
    tmdl_dir.mkdir(exist_ok=True)

    # Wczytaj wszystkie miary
    measures = []
    for html_file in html_files:
        # Użyj nazwy pliku (bez .html) jako nazwy miary dla zachowania pełnej numeracji
        measure_name = html_file.stem  # Np. "01. Podstawy DAX - Funkcje filtrujące"
        _, measure_content = read_measure_from_html(html_file)
        if measure_content:
            measures.append((measure_name, measure_content))

    if not measures:
        print("[WARNING] Nie znaleziono miar do wygenerowania TMDL")
        return

    # Generuj lineageTag dla tabeli
    table_lineage_tag = str(uuid.uuid4())

    # Rozpocznij budowanie pliku TMDL
    tmdl_lines = []
    tmdl_lines.append("createOrReplace\n")
    tmdl_lines.append("\n")
    tmdl_lines.append("    table _HTML\n")
    tmdl_lines.append(f"        lineageTag: {table_lineage_tag}\n")
    tmdl_lines.append("\n")

    # Dodaj każdą miarę
    for measure_name, measure_content in measures:
        measure_lineage_tag = str(uuid.uuid4())

        # Miara w formacie: measure 'NazwaMiary' = ```<zawartość>```
        tmdl_lines.append(f"        measure '{measure_name}' = ```{measure_content}```\n")
        tmdl_lines.append(f"            lineageTag: {measure_lineage_tag}\n")
        tmdl_lines.append("\n")

    # Dodaj partition
    tmdl_lines.append("        partition _HTML = m\n")
    tmdl_lines.append("            mode: import\n")
    tmdl_lines.append("            source =\n")
    tmdl_lines.append('                    let\n')
    tmdl_lines.append('                        Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [HTML = _t]),\n')
    tmdl_lines.append('                        #"Removed Columns" = Table.RemoveColumns(Source,{"HTML"})\n')
    tmdl_lines.append('                    in\n')
    tmdl_lines.append('                        #"Removed Columns"\n')
    tmdl_lines.append("\n")
    tmdl_lines.append("        annotation PBI_ResultType = Table\n")
    tmdl_lines.append("\n")
    tmdl_lines.append("        annotation PBI_NavigationStepName = Navigation\n")
    tmdl_lines.append("\n")

    # Zapisz plik TMDL jako .md (łatwiejsze kopiowanie w Obsidian)
    tmdl_file_path = tmdl_dir / "_HTML.md"
    with open(tmdl_file_path, 'w', encoding='utf-8') as f:
        f.writelines(tmdl_lines)

    print(f"[OK] Wygenerowano TMDL: {tmdl_file_path}")
    print(f"     Liczba miar: {len(measures)}")

    # Generuj osobny plik z parametrem pHTML
    generate_parameter_file(measures, tmdl_dir)


if __name__ == '__main__':
    main()
