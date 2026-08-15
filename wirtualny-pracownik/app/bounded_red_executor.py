"""
Wykonuje czerwoną akcję bez pytania, TYLKO jeśli mieści się w jawnie
zdefiniowanej granicy liczbowej w approval_policy.yaml (bounded autonomy,
PLAN-WDROZENIA.md sekcja 3). Brak wpisu w bounded_red = zwykłe czerwone,
zawsze do człowieka. Granice ustawia człowiek, ten moduł nigdy ich nie
rozszerza ani nie zgaduje.
"""

from risk_classifier import bounded_red_limit


def check_bounded_red(action_type, proposed_change, policy=None):
    """proposed_change: np. {"percent_change": 10} dla zmiany budżetu.
    Zwraca (allowed: bool, detail: str)."""
    limit = bounded_red_limit(action_type, policy)

    if limit is None:
        return False, "Brak zdefiniowanej granicy dla tego typu akcji — zwykłe czerwone, do człowieka."

    max_percent = limit.get("max_percent_change")
    if max_percent is not None:
        change = proposed_change.get("percent_change")
        if change is None:
            return False, "Nie podano wielkości zmiany do porównania z granicą."
        if abs(change) <= max_percent:
            return True, f"Zmiana {change}% mieści się w granicy ±{max_percent}%."
        return False, f"Zmiana {change}% przekracza granicę ±{max_percent}% — wraca do zwykłego czerwonego."

    return False, "Format granicy nieznany — bezpieczniej potraktować jako zwykłe czerwone."


if __name__ == "__main__":
    # Bez wpisów w bounded_red (domyślna, zalecana konfiguracja startowa) —
    # zawsze powinno wracać False.
    print(check_bounded_red("meta_ads_budget_change", {"percent_change": 5}))
