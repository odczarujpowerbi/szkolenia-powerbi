#!/usr/bin/env python3
"""
Konwerter plików Markdown do miar Power BI z HTML
Automatyzuje proces tworzenia dokumentacji technicznej dla prezentacji Power BI

Główny plik startujący - orchestruje cały proces konwersji
"""

import argparse
import tkinter as tk
from pathlib import Path

# Import modułów lokalnych
from utils import (
    clean_output_directory,
    convert_file,
    load_config,
    generate_css_measures,
    generate_tmdl
)
from template_loader import load_all_assets


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

  # Z pliku konfiguracyjnego (wymagany):
  python main.py --config config.md

  # Używa domyślnego config.md z folderu skryptu (jeśli istnieje):
  python main.py
        """
    )

    parser.add_argument(
        '--config',
        type=str,
        metavar='FILE',
        help='Plik konfiguracyjny (.md lub .json) z ustawieniami CSS/JS'
    )

    return parser.parse_args()


def main():
    """Główna funkcja programu"""

    # Parsuj argumenty
    args = parse_arguments()

    # Ścieżki
    script_dir = Path(__file__).parent
    input_dir = script_dir / '300. INPUTS'
    resources_dir = script_dir / '100. RESOURCES'
    output_dir = script_dir / '400. OUTPUTS'  # Output HTML
    tmdl_dir = output_dir / '_Measures'  # Folder _Measures wewnątrz OUTPUTS

    # Sprawdź czy foldery istnieją
    if not input_dir.exists():
        print(f"[ERROR] Folder 300. INPUTS nie istnieje: {input_dir}")
        return

    if not resources_dir.exists():
        print(f"[ERROR] Folder 100. RESOURCES nie istnieje: {resources_dir}")
        return

    clean_output_directory(output_dir)
    output_dir.mkdir(exist_ok=True)



    # Ustal konfigurację assetów
    assets_config = None
    should_generate_css_measures = True  # Domyślnie włączone

    # Sprawdź czy podano plik konfiguracyjny, jeśli nie - szukaj domyślnego config.md
    config_path_to_use = None
    if args.config:
        config_path_to_use = Path(args.config)
    else:
        # Auto-detect config.md w folderze skryptu
        default_config = script_dir / 'config.md'
        if default_config.exists():
            config_path_to_use = default_config

    if not config_path_to_use:
        print(f"[ERROR] Nie znaleziono pliku konfiguracyjnego!")
        print(f"Utwórz plik config.md w folderze skryptu lub użyj: python main.py --config config.md")
        return

    if not config_path_to_use.exists():
        print(f"[ERROR] Plik konfiguracyjny nie istnieje: {config_path_to_use}")
        return

    print(f"\n[INFO] Wczytuję konfigurację z: {config_path_to_use}\n")
    config = load_config(config_path_to_use)
    assets_config = config.get('assets', {})
    should_generate_css_measures = config.get('generate_css_measures', True)
    characters_config = config.get('characters', {})

    # Generuj osobne miary CSS (jeśli włączone)
    css_measures_count = 0
    if should_generate_css_measures:
        print(f"\n=== Generowanie miar CSS ===\n")
        css_measures_count = generate_css_measures(resources_dir, output_dir)
    else:
        print(f"\n[INFO] Generowanie miar CSS wyłączone w konfiguracji\n")

    # Wczytaj wszystkie assety dla wszystkich typów
    assets_dict = load_all_assets(resources_dir, assets_config)

    # Przetwórz wszystkie pliki .md w 300. INPUTS (włącznie z podfolderami)
    all_md_files = list(input_dir.rglob('*.md'))

    # Pomiń pliki notes Obsidian (artefakty folder notes)
    obsidian_notes = {
        '300. INPUTS.md',
        '000. TEMPLATES.md',
        '100. RESOURCES.md',
        '200. DRAFTS.md',
        '400. OUTPUTS.md',
        '500. ARCHIVE.md'
    }
    md_files = [f for f in all_md_files if f.name not in obsidian_notes]

    if not md_files:
        print(f"[ERROR] Nie znaleziono plikow .md w folderze 300. INPUTS: {input_dir}")
        return

    print(f"\n=== Konwersja plikow Markdown -> Power BI HTML ===\n")
    print(f"Zrodlo: {input_dir}")
    print(f"Output: {output_dir}\n")

    total_generated = 0
    for md_file in md_files:
        try:
            # Oblicz względną ścieżkę względem input_dir
            relative_path = md_file.relative_to(input_dir)
            # Utwórz odpowiednią strukturę folderów w output_dir
            target_dir = output_dir / relative_path.parent
            target_dir.mkdir(parents=True, exist_ok=True)

            count = convert_file(md_file, target_dir, assets_dict, characters_config)
            total_generated += count
        except Exception as e:
            print(f"[ERROR] Blad przy konwersji {md_file.name}: {e}")

    print(f"\n=== Zakonczono konwersje Markdown! ===")
    print(f"Wygenerowano {total_generated} plik(ow) HTML z {len(md_files)} plik(ow) Markdown.")
    if css_measures_count > 0:
        print(f"Wygenerowano {css_measures_count} miar(y) CSS.")
    print()

    # Generuj pliki miar (TMDL)
    print(f"\n=== Generowanie pliku TMDL ===\n")
    generate_tmdl(output_dir, tmdl_dir)
    print()

    # Podsumowanie
    total_files = total_generated + css_measures_count

# Okienko z sukcesem (auto-zamykające się)
    root = tk.Tk()
    root.withdraw()  # Ukryj główne okno

    summary_message = f"✓ Pomyślnie wygenerowano {total_files} plik(ów) HTML!\n\n"
    summary_message += f"• {total_generated} miar(y) z Markdown\n"
    if css_measures_count > 0:
        summary_message += f"• {css_measures_count} miar(y) CSS\n"
    summary_message += f"\nOutput HTML: {output_dir}\n"
    summary_message += f"Plik TMDL: {tmdl_dir}\n\n"
    summary_message += f"Pliki gotowe do użycia w Power BI."

    # Stwórz okno sukcesu
    success_window = tk.Toplevel(root)
    success_window.title("Konwersja zakończona")
    success_window.geometry("500x280")
    success_window.resizable(False, False)

    # Wyśrodkuj okno na ekranie
    success_window.update_idletasks()
    x = (success_window.winfo_screenwidth() // 2) - (500 // 2)
    y = (success_window.winfo_screenheight() // 2) - (280 // 2)
    success_window.geometry(f"+{x}+{y}")

    # Frame dla lepszego układu
    frame = tk.Frame(success_window, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)

    # Dodaj tekst z zawijaniem
    label = tk.Label(frame, text=summary_message,
                     justify=tk.LEFT,
                     font=("Segoe UI", 10),
                     wraplength=450,  # Zawijanie tekstu
                     anchor="nw")
    label.pack(fill=tk.BOTH, expand=True)

    # Auto-zamknięcie po 3 sekundach
    success_window.after(1000, lambda: [success_window.destroy(), root.destroy()])

    root.mainloop()


if __name__ == '__main__':
    main()
