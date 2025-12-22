#!/usr/bin/env python3
"""
Moduł do ładowania templateów CSS i JS z plików markdown
Obsługuje wczytywanie wielu plików CSS/JS dla różnych typów treści
"""

import re
from pathlib import Path


def read_template(template_path):
    """Czyta template CSS lub JS z pliku markdown

    Args:
        template_path: ścieżka do pliku .md

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
            content = read_template(css_path)
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
            content = read_template(js_path)
            if content:
                js_parts.append(content)
                print(f"[OK] Wczytano JS: {js_file}")
        else:
            print(f"[WARNING] Nie znaleziono pliku JS: {js_file}")

    # Połącz zawartość (z separatorem dla czytelności)
    css = '\n\n'.join(css_parts) if css_parts else ''
    js = '\n\n'.join(js_parts) if js_parts else ''

    return css, js


def load_all_assets(template_dir, assets_config):
    """Wczytuje wszystkie pliki CSS i JS dla wszystkich typów z konfiguracji

    Args:
        template_dir: Path - folder z templateami
        assets_config: dict - konfiguracja assetów w formacie:
            {
                'teoria': {'css': ['CSS.md'], 'js': ['JS.md']},
                'quiz': {'css': ['CSS - Quiz.md'], 'js': ['JS - Quiz.md']}
            }

    Returns:
        dict: słownik mapujący typy na assety:
            {
                'teoria': {'css': str, 'js': str},
                'quiz': {'css': str, 'js': str}
            }
    """
    result = {}

    for content_type, files in assets_config.items():
        css_files = files.get('css', [])
        js_files = files.get('js', [])

        # Wczytaj CSS i JS dla tego typu
        css_content, js_content = load_templates(template_dir, css_files, js_files)

        result[content_type] = {
            'css': css_content,
            'js': js_content
        }

    return result
