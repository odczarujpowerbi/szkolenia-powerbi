"""
Moduł narzędziowy utils.py

Zawiera główne funkcje użytkowe dla konwersji plików Markdown do miar Power BI.
Obsługuje trzy typy plików: teoria, quiz i gaps.

Funkcje:
- clean_output_directory: Czyści folder wyjściowy przed generowaniem
- parse_frontmatter: Wyciąga properties z pliku Markdown (Obsidian)
- convert_file: Główna funkcja konwersji pojedynczego pliku
- load_config: Wczytuje konfigurację z pliku .md lub .json
- generate_css_measures: Generuje osobne miary Power BI dla CSS
- read_measure_from_html: Czyta plik HTML i wyciąga nazwę i zawartość miary
- extract_measure_metadata: Wyciąga metadane z nazwy miary
- generate_parameter_file: Generuje plik z parametrem pHTML
- generate_tmdl: Generuje plik TMDL ze wszystkimi miarami

Autor: Konwersja z convert_md_to_powerbi.py
"""

import re
import os
import json
import uuid
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

from text_utils import normalize_quotes, escape_quotes_for_dax, convert_markdown_to_html
from theory_processor import split_by_h1, create_powerbi_measure
from quiz_processor import parse_quiz_markdown, create_quiz_html
from gaps_processor import parse_gaps_markdown, create_gaps_html
from template_loader import read_template


def clean_output_directory(output_dir):
    """Czyści folder wyjściowy przed generowaniem nowych plików

    Args:
        output_dir: Path - folder do wyczyszczenia
    """
    if not output_dir.exists():
        print(f"[INFO] Folder {output_dir} nie istnieje, zostanie utworzony")
        return

    print(f"[INFO] Czyszczenie folderu: {output_dir}\n")

    # Usuń folder TMDL jeśli istnieje (najpierw, bo zawiera pliki)
    tmdl_dir = output_dir / 'TMDL'
    if tmdl_dir.exists():
        try:
            import shutil
            shutil.rmtree(tmdl_dir)
            print(f"[OK] Usunięto folder TMDL")
        except PermissionError:
            print(f"[WARNING] Folder TMDL jest zablokowany (prawdopodobnie otwarty w eksploratorze)")
        except Exception as e:
            print(f"[WARNING] Nie można usunąć folderu TMDL: {e}")

    # Usuń wszystkie pliki z głównego folderu OUTPUT (wszystkie rozszerzenia)
    all_files = [f for f in output_dir.iterdir() if f.is_file()]
    deleted_count = 0
    failed_count = 0

    for file in all_files:
        try:
            file.unlink()
            deleted_count += 1
            print(f"[OK] Usunięto: {file.name}")
        except PermissionError:
            print(f"[WARNING] Plik zablokowany (prawdopodobnie otwarty): {file.name}")
            failed_count += 1
        except Exception as e:
            print(f"[WARNING] Nie można usunąć {file.name}: {e}")
            failed_count += 1

    if deleted_count > 0:
        print(f"\n[OK] Usunięto łącznie {deleted_count} plik(ów)")
    if failed_count > 0:
        print(f"[WARNING] Nie udało się usunąć {failed_count} plik(ów)")
    if deleted_count == 0 and failed_count == 0:
        print(f"[INFO] Brak plików do usunięcia")

    print()  # Pusta linia dla czytelności


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


def convert_file(input_path, output_dir, assets_dict):
    """Konwertuje pojedynczy plik markdown do miar Power BI

    Obsługuje trzy typy plików:
    - type='teoria': tradycyjny format z sekcjami i stronami (split by H1)
    - type='quiz': interaktywny quiz z pytaniami
    - type='gaps': zadania z lukami do uzupełnienia

    Args:
        input_path: Path - ścieżka do pliku źródłowego
        output_dir: Path - folder wyjściowy
        assets_dict: dict - słownik assetów dla typów:
            {'teoria': {'css': str, 'js': str}, 'quiz': {'css': str, 'js': str}, 'gaps': {'css': str, 'js': str}}

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

    # Pobierz CSS i JS dla tego typu
    assets = assets_dict.get(file_type, assets_dict.get('teoria', {'css': '', 'js': ''}))
    css = assets.get('css', '')
    js = assets.get('js', '')

    # Pobierz bazową nazwę pliku (bez rozszerzenia)
    base_name = Path(input_path).stem

    # QUIZ: Obsługa plików typu 'quiz'
    if file_type == 'quiz':
        # Parsuj quiz
        quiz_title, questions = parse_quiz_markdown(content_without_frontmatter)

        if not questions:
            print(f"[WARNING] Brak pytań w quizie: {input_path.name}")
            return 0

        # Generuj HTML quizu (z CSS z konfiguracji lub inline)
        quiz_html = create_quiz_html(quiz_title, questions, css, js)

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

    # GAPS: Obsługa plików typu 'gaps'
    if file_type == 'gaps':
        # Parsuj gaps
        tasks = parse_gaps_markdown(content_without_frontmatter)

        if not tasks:
            print(f"[WARNING] Brak zadań w pliku gaps: {input_path.name}")
            return 0

        # Generuj HTML gaps (z CSS z konfiguracji lub inline)
        gaps_html = create_gaps_html(tasks, css, js)

        # Escapuj cudzysłowy dla DAX
        gaps_html = escape_quotes_for_dax(gaps_html)

        # Formatuj jako miara Power BI
        measure = f'{base_name} = \n\n"\n\n{gaps_html}\n"\n'

        # Zapisz do pliku
        output_filename = f"{base_name}.html"
        output_path = output_dir / output_filename

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(measure)

        print(f"[OK] Skonwertowano gaps: {output_filename}")
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


def load_config(config_path):
    """Wczytuje konfigurację z pliku .md zawierającego blok JSON lub z pliku .json

    Nowy format z mapowaniem CSS/JS dla typów:
    ```json
    {
        "assets": {
            "teoria": {
                "css": ["CSS.md"],
                "js": ["JS.md"]
            },
            "quiz": {
                "css": ["CSS - Quiz.md"],
                "js": ["JS - Quiz.md"]
            }
        },
        "generate_css_measures": true
    }
    ```

    Args:
        config_path: str - ścieżka do pliku .md lub .json

    Returns:
        dict: słownik z kluczami:
            - 'assets': dict mapujący typy -> {'css': [...], 'js': [...]}
            - 'generate_css_measures': bool
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

    # Zwróć konfigurację (wymagany nowy format z 'assets')
    if 'assets' not in config:
        raise ValueError(f"Plik konfiguracyjny musi zawierać klucz 'assets'. Znaleziono: {list(config.keys())}")

    return {
        'assets': config.get('assets', {}),
        'generate_css_measures': config.get('generate_css_measures', True)
    }


def generate_css_measures(template_dir, output_dir):
    """Generuje osobne miary Power BI dla każdego pliku CSS z folderu 100. RESOURCES

    Args:
        template_dir: Path - folder z templateami (100. RESOURCES)
        output_dir: Path - folder wyjściowy (400. OUTPUTS)

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
        css_content = read_template(css_file)

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
        tmdl_dir: Path - folder docelowy (400. OUTPUTS/TMDL)
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
    """Generuje plik TMDL ze wszystkimi miarami z folderu 400. OUTPUTS

    Args:
        output_dir: Path - folder z plikami HTML (400. OUTPUTS)
        tmdl_dir: Path - folder docelowy dla pliku TMDL (400. OUTPUTS/TMDL)
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
