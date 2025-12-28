#!/usr/bin/env python3
"""
Moduł do przetwarzania tekstu Markdown na HTML
Zawiera funkcje do konwersji markdown, podświetlania składni DAX i escapowania znaków
"""

import re


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


def convert_markdown_to_html(md_content, characters_config=None):
    """Konwertuje zawartość markdown pojedynczej strony na HTML

    Args:
        md_content: str - zawartość markdown do konwersji
        characters_config: dict - konfiguracja zamian znaków (opcjonalnie)
    """
    lines = md_content.strip().split('\n')
    html_lines = []
    in_code_block = False
    in_list = False
    code_block = []
    code_lang = None

    # Pomocnicza funkcja do przetwarzania tekstu użytkownika z character replacements
    def process_text(text):
        """Przetwarza inline markdown i stosuje character replacements"""
        result = process_inline_markdown(text)
        if characters_config:
            result = apply_character_replacements(result, characters_config)
        return result

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

                # Znajdź minimalne wcięcie wśród niepustych linii
                non_empty_lines = [line for line in code_block if line.strip()]
                if non_empty_lines:
                    # Policz spacje na początku każdej niepustej linii
                    indents = [len(line) - len(line.lstrip()) for line in non_empty_lines]
                    min_indent = min(indents) if indents else 0

                    # Usuń minimalne wcięcie ze wszystkich linii (zachowaj relatywne wcięcia)
                    normalized_lines = []
                    for line in code_block:
                        if line.strip():  # Niepusta linia
                            normalized_lines.append(line[min_indent:] if len(line) > min_indent else line)
                        else:  # Pusta linia
                            normalized_lines.append('')
                    code_content = '\n'.join(normalized_lines)
                else:
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
                    html_lines.append(f'      <th>{process_text(header)}</th>\n')
                html_lines.append('    </tr>\n  </thead>\n')

                # Pomiń drugi wiersz (separator: | --- | --- |)
                # Pozostałe wiersze to dane
                html_lines.append('  <tbody>\n')
                for row_line in table_lines[2:]:
                    cells = [cell.strip() for cell in row_line.split('|')[1:-1]]
                    html_lines.append('    <tr>\n')
                    for cell in cells:
                        html_lines.append(f'      <td>{process_text(cell)}</td>\n')
                    html_lines.append('    </tr>\n')
                html_lines.append('  </tbody>\n')
                html_lines.append('</table>\n')
            continue

        # Headings ## (h1)
        if line.startswith('## '):
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False
            html_lines.append(f"<h1>{process_text(line[3:])}</h1>\n")
            i += 1
            continue

        # Result boxes - "Suma końcowa:" jako nagłówek w result-box (sprawdź PRZED innymi ###)
        if line.startswith('### ') and 'Suma końcowa:' in line:
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False

            html_lines.append("<div class='result-box'>\n")
            html_lines.append(f"<h3>{process_text(line[4:])}</h3>\n")
            i += 1

            # Zbierz zawartość result-box
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('#'):
                html_lines.append(f"<p>{process_text(lines[i])}</p>\n")
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
                html_lines.append(f"<h3>{process_text(heading_text)}</h3>\n")

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
                        html_lines.append(f"<li>{process_text(next_line[2:])}</li>\n")
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
                    html_lines.append(f"<p>{process_text(next_line)}</p>\n")
                    i += 1

                # Zamknij otwartą listę i box
                if local_list_open:
                    html_lines.append('</ul>\n')
                html_lines.append("</div>\n")
                continue
            else:
                # Zwykły nagłówek h2
                html_lines.append(f"<h2>{process_text(heading_text)}</h2>\n")
                i += 1
                continue

        # Result boxes - "Wynik:" lub "SUMX dodaje"
        if line.strip().startswith('Wynik:') or 'SUMX dodaje' in line:
            if in_list:
                html_lines.append(f'</{in_list}>\n')
                in_list = False

            html_lines.append(f"<div class='result-box'>\n{process_text(line)}\n</div>\n")
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
            html_lines.append(f"<li>{process_text(content)}")

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
                    html_lines.append(f"<li>{process_text(nested_item)}</li>\n")
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
            html_lines.append(f"<li>{process_text(line[2:])}</li>\n")
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
            html_lines.append(f"<p>{process_text(line)}</p>\n")
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


def apply_character_replacements(text, characters_config):
    """Aplikuje zamianę znaków zgodnie z konfiguracją

    Args:
        text: str - tekst do przetworzenia
        characters_config: dict - słownik z konfiguracją zamian:
            {'quote': str, 'single_quote': str}
            Przykład: {'quote': '"', 'single_quote': '‛'}

    Returns:
        str - tekst po zamianach znaków
    """
    if not characters_config:
        # Jeśli brak konfiguracji, użyj domyślnego escape_quotes_for_dax
        return escape_quotes_for_dax(text)

    # Pobierz znaki z konfiguracji
    quote_replacement = characters_config.get('quote', "'")
    single_quote_replacement = characters_config.get('single_quote', "'")

    # Zamień podwójne cudzysłowy
    text = text.replace('"', quote_replacement)

    # Zamień pojedyncze cudzysłowy (apostrofy)
    text = text.replace("'", single_quote_replacement)

    return text


def format_user_text(text, context='html', characters_config=None):
    """Formatuje tekst użytkownika z markdown na HTML

    Konwertuje markdown (inline code, bold, images) na HTML, zachowując
    prawidłową kolejność operacji (najpierw markdown, potem escape).

    Args:
        text: str - tekst wejściowy z markdown
        context: str - kontekst użycia:
            - 'html': dla bezpośredniego wstawienia do HTML (escape HTML po przetworzeniu)
            - 'innerHTML': dla JavaScript innerHTML w DAX (escape cudzysłowów po przetworzeniu)
            - 'raw': tylko konwersja markdown, bez escape
        characters_config: dict - konfiguracja zamian znaków (opcjonalnie)

    Returns:
        str - sformatowany tekst HTML

    Examples:
        >>> format_user_text("To jest **bold** i `kod`", 'html')
        'To jest <strong>bold</strong> i <code>kod</code>'

        >>> format_user_text("Użyj `COUNT`", 'innerHTML')
        'Użyj <code>COUNT</code>'
    """
    if not text:
        return text

    # KROK 1: Markdown → HTML (ZAWSZE PIERWSZY)
    formatted = process_inline_markdown(text)

    # KROK 2: Escape (zależnie od kontekstu, ZAWSZE DRUGI)
    if context == 'html':
        # Bezpośrednie wstawienie do HTML - escape < > &
        formatted = escape_html(formatted)
    elif context == 'innerHTML':
        # Dla JavaScript innerHTML - escape cudzysłowów dla DAX
        if characters_config:
            formatted = apply_character_replacements(formatted, characters_config)
        else:
            formatted = escape_quotes_for_dax(formatted)
    elif context == 'raw':
        # Raw - również zastosuj character replacements jeśli są dostępne
        if characters_config:
            formatted = apply_character_replacements(formatted, characters_config)
        else:
            formatted = escape_quotes_for_dax(formatted)

    return formatted


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
