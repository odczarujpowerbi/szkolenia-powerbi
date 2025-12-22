"""Gaps processor module for handling gaps markdown parsing and HTML generation.

This module provides functionality to parse gaps content from markdown format
and generate interactive HTML gap-filling exercises. It supports gaps metadata extraction,
answer validation, and user feedback mechanisms.

Functions:
    parse_gaps_markdown: Parses gaps markdown content into structured data
    create_gaps_html: Generates interactive HTML gaps exercises from parsed task data
"""

import re
import json
from text_utils import escape_html, escape_quotes_for_dax, highlight_dax_syntax


def parse_gaps_markdown(content):
    """Parsuje plik gaps w formacie markdown

    Format gaps:
    # Tytuł zadania

    Opis zadania

    ## Dostępne funkcje
    - FUNKCJA1
    - FUNKCJA2

    ## Kod do uzupełnienia
    ```dax
    Miara =
        [SLOT:0](
            [SLOT:1](Tabela[Kolumna])
        )
    ```

    ## Poprawne rozwiązanie
    FUNKCJA1,FUNKCJA2

    ## Feedback poprawny
    Komunikat sukcesu

    ## Feedback błędny - FUNKCJA1,FUNKCJA3
    Komunikat dla konkretnego błędu

    ## Feedback błędny - default
    Ogólny komunikat błędu

    ## Wskazówka
    Tekst wskazówki

    ---

    (kolejne zadania oddzielone ---)

    Args:
        content: str - zawartość pliku gaps (bez frontmatter)

    Returns:
        list: lista słowników z zadaniami
            [{
                'title': str,
                'description': str,
                'functions': [str],
                'code': str,
                'solution': [str],
                'feedback_correct': str,
                'feedback_incorrect': dict,  # {'pattern': 'message'}
                'hint': str
            }]
    """
    # Podziel na sekcje zadań po ---
    tasks_raw = content.split('\n---\n')
    tasks = []

    for task_content in tasks_raw:
        if not task_content.strip():
            continue

        lines = task_content.strip().split('\n')

        task = {
            'title': '',
            'description': '',
            'functions': [],
            'code': '',
            'solution': [],
            'feedback_correct': '',
            'feedback_incorrect': {},
            'hint': ''
        }

        current_section = None
        code_block = []
        in_code_block = False
        description_lines = []
        feedback_key = None

        i = 0
        while i < len(lines):
            line = lines[i]

            # Tytuł zadania (pierwszy # H1)
            if line.startswith('# ') and not task['title']:
                task['title'] = line[2:].strip()
                i += 1
                current_section = 'description'
                continue

            # Sekcja
            if line.startswith('## '):
                section_name = line[3:].strip().lower()

                if 'dostępne funkcje' in section_name or 'available functions' in section_name:
                    current_section = 'functions'
                elif 'kod do uzupełnienia' in section_name or 'code' in section_name:
                    current_section = 'code'
                elif 'poprawne rozwiązanie' in section_name or 'correct solution' in section_name:
                    current_section = 'solution'
                elif 'feedback poprawny' in section_name or 'correct feedback' in section_name:
                    current_section = 'feedback_correct'
                elif 'feedback błędny' in section_name or 'incorrect feedback' in section_name:
                    # Sprawdź czy jest wzorzec po myślniku
                    if ' - ' in line:
                        feedback_key = line.split(' - ', 1)[1].strip()
                    else:
                        feedback_key = 'default'
                    current_section = 'feedback_incorrect'
                elif 'wskazówka' in section_name or 'hint' in section_name:
                    current_section = 'hint'

                i += 1
                continue

            # Blok kodu
            if line.strip().startswith('```'):
                if not in_code_block:
                    in_code_block = True
                    code_block = []
                else:
                    # Koniec bloku kodu
                    in_code_block = False
                    task['code'] = '\n'.join(code_block)
                i += 1
                continue

            if in_code_block:
                code_block.append(line)
                i += 1
                continue

            # Zawartość sekcji
            if current_section == 'description' and line.strip() and not line.startswith('#'):
                description_lines.append(line)
            elif current_section == 'functions' and line.strip().startswith('- '):
                func = line[2:].strip()
                task['functions'].append(func)
            elif current_section == 'solution' and line.strip():
                # Rozwiązanie jako lista funkcji oddzielonych przecinkami
                task['solution'] = [f.strip() for f in line.split(',')]
            elif current_section == 'feedback_correct' and line.strip():
                task['feedback_correct'] += line + '\n'
            elif current_section == 'feedback_incorrect' and line.strip():
                if feedback_key not in task['feedback_incorrect']:
                    task['feedback_incorrect'][feedback_key] = ''
                task['feedback_incorrect'][feedback_key] += line + '\n'
            elif current_section == 'hint' and line.strip():
                task['hint'] += line + '\n'

            i += 1

        task['description'] = '\n'.join(description_lines).strip()
        task['feedback_correct'] = task['feedback_correct'].strip()
        task['hint'] = task['hint'].strip()

        # Oczyszczenie feedback_incorrect
        for key in task['feedback_incorrect']:
            task['feedback_incorrect'][key] = task['feedback_incorrect'][key].strip()

        if task['title']:  # Dodaj tylko jeśli ma tytuł
            tasks.append(task)

    return tasks


def create_gaps_html(tasks, css='', js=''):
    """Tworzy interaktywne zadania z lukami w formacie HTML

    Args:
        tasks: list[dict] - lista zadań z danymi
        css: str - opcjonalny zewnętrzny CSS
        js: str - opcjonalny zewnętrzny JS

    Returns:
        str: kompletny HTML z zadaniami (gotowy do osadzenia w miarze Power BI)
    """
    use_inline_styles = not css
    total_pages = len(tasks)

    html_parts = []

    # DOCTYPE i HTML header
    html_parts.append("<!DOCTYPE html>\n")
    html_parts.append("<html lang='pl'>\n")
    html_parts.append("<head>\n")
    html_parts.append("    <meta charset='UTF-8'>\n")
    html_parts.append("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    html_parts.append(f"    <title>DAX Gaps</title>\n")

    # CSS
    html_parts.append("    <style>\n")
    if css:
        for line in css.split('\n'):
            html_parts.append(f"    {line}\n")
    html_parts.append("    </style>\n")

    html_parts.append("</head>\n")
    html_parts.append("<body>\n\n")

    # Nawigacja paginacji (jeśli więcej niż 1 zadanie)
    if total_pages > 1:
        html_parts.append("<div class='pagination'>\n")
        html_parts.append("    <button class='nav-button' id='prevBtn' onclick='prevPage()'>← Poprzednie</button>\n")
        html_parts.append("    <span class='page-info'>Zadanie <span id='currentPage'>1</span> z <span id='totalPages'>{}</span></span>\n".format(total_pages))
        html_parts.append("    <button class='nav-button' id='nextBtn' onclick='nextPage()'>Następne →</button>\n")
        html_parts.append("</div>\n\n")

    # Strony z zadaniami
    for page_idx, task in enumerate(tasks):
        page_class = "page active" if page_idx == 0 else "page"
        html_parts.append(f"<div class='{page_class}' data-page='{page_idx + 1}'>\n")
        html_parts.append("<div class='container'>\n")

        # Opis zadania
        html_parts.append("    <div class='task-description'>\n")
        html_parts.append(f"        <h3>{task['title']}</h3>\n")
        html_parts.append(f"        {task['description']}\n")
        html_parts.append("    </div>\n\n")

        # Dostępne funkcje
        html_parts.append("    <div>\n")
        for func in task['functions']:
            html_parts.append(f"        <span class='function-chip' draggable='true' ondragstart='drag(event)' data-function='{func}'>{func}</span>\n")
        html_parts.append("    </div>\n\n")

        # Kod z lukami
        html_parts.append("    <div class='code-container'>\n")

        # Parsuj kod i wstaw drop zones
        code_lines = task['code'].split('\n')
        for code_line in code_lines:
            # Znajdź wszystkie [SLOT:N] i zamień na drop zones
            processed_line = code_line
            slot_pattern = r'\[SLOT:(\d+)\]'

            def replace_slot(match):
                slot_num = match.group(1)
                return f"<div class='drop-zone' data-slot='{slot_num}' ondrop='drop(event)' ondragover='allowDrop(event)' ondragleave='dragLeave(event)'></div>"

            processed_line = re.sub(slot_pattern, replace_slot, processed_line)
            html_parts.append(f"        <div>{processed_line}</div>\n")

        html_parts.append("    </div>\n\n")

        # Przyciski
        html_parts.append("    <div class='button-group'>\n")
        html_parts.append("        <button onclick='checkSolution()'>Sprawdź rozwiązanie</button>\n")
        html_parts.append("        <button class='reset-btn' onclick='resetTask()'>Reset</button>\n")
        html_parts.append("    </div>\n\n")

        # Wskazówka
        if task['hint']:
            html_parts.append("    <div class='hint-box'>\n")
            html_parts.append(f"        {task['hint']}\n")
            html_parts.append("    </div>\n\n")

        # Feedback
        html_parts.append("    <div class='feedback' id='feedback'></div>\n")

        html_parts.append("</div>\n")
        html_parts.append("</div>\n\n")

    # JavaScript
    html_parts.append("<script>\n")

    # Dane dynamiczne
    html_parts.append(f"    let currentPage = 1;\n")
    html_parts.append(f"    const totalPages = {total_pages};\n")

    # Liczba slotów dla każdego zadania
    slots_per_page = []
    for task in tasks:
        num_slots = len(task['solution'])
        slots_per_page.append(num_slots)

    html_parts.append(f"    const slotsPerPage = {slots_per_page};\n")
    html_parts.append(f"    let slots = new Array(slotsPerPage[0]).fill('');\n")

    # Poprawne rozwiązania
    correct_solutions = [task['solution'] for task in tasks]
    html_parts.append(f"    const correctSolutions = {json.dumps(correct_solutions)};\n")

    # Feedback poprawny - escape apostrofy przed json.dumps
    correct_feedback = []
    for task in tasks:
        # Zamień apostrofy na &#39; (HTML entity) aby nie powodować błędów po escape_quotes_for_dax
        feedback_escaped = task['feedback_correct'].replace("'", "&#39;")
        correct_feedback.append(feedback_escaped)
    html_parts.append(f"    const correctFeedback = {json.dumps(correct_feedback)};\n")

    # Feedback błędny - escape apostrofy przed json.dumps
    incorrect_feedback_list = []
    for task in tasks:
        feedback_dict = {}
        for pattern, message in task['feedback_incorrect'].items():
            # Zamień apostrofy na &#39; (HTML entity)
            message_escaped = message.replace("'", "&#39;")
            feedback_dict[pattern] = message_escaped
        incorrect_feedback_list.append(feedback_dict)

    html_parts.append(f"    const incorrectFeedback = {json.dumps(incorrect_feedback_list)};\n\n")

    # Funkcje z template lub inline
    if js:
        for line in js.split('\n'):
            html_parts.append(f"    {line}\n")

    html_parts.append("</script>\n\n")
    html_parts.append("</body>\n")
    html_parts.append("</html>\n")

    return ''.join(html_parts)
