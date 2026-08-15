"""
Klient Projectly (PLAN-WDROZENIA.md sekcja 2, SKRYPTY.md `projectly_poller.py`
i pokrewne). To jest STUB — prawdziwe endpointy/autoryzacja Projectly nie są
mi znane z tej sesji (nie mam dostępu do dokumentacji API Projectly ani do
Twojego konta). Tryb mock pozwala testować cały pipeline (task_router,
risk_classifier, state_store) bez czekania na te dane.

Do podłączenia prawdziwego Projectly: zaimplementuj metody klasy
ProjectlyClient używając realnego REST API/MCP, korzystając z kluczy z
lokalnego magazynu sekretów (nigdy nie wklejaj ich tutaj).
"""

import json
import os
from pathlib import Path

MOCK_TASKS_PATH = Path(__file__).parent / "mock_data" / "sample_tasks.json"


class ProjectlyClient:
    """Prawdziwa implementacja — DO ZROBIENIA, gdy będą znane endpointy/auth Projectly."""

    def __init__(self, api_key=None, base_url=None):
        self.api_key = api_key
        self.base_url = base_url

    def get_new_tasks(self):
        raise NotImplementedError(
            "Prawdziwe API Projectly nie jest jeszcze podłączone. "
            "Użyj MockProjectlyClient do testów albo uzupełnij tę metodę."
        )

    def post_comment(self, task_id, text):
        raise NotImplementedError("Jak wyżej.")

    def update_status(self, task_id, status):
        raise NotImplementedError("Jak wyżej.")


class MockProjectlyClient:
    """Symuluje Projectly przy użyciu lokalnego pliku JSON — do testowania
    Fazy 0-1 bez prawdziwego dostępu do API (PRZED-PILOTAZEM.md: sandbox vs
    produkcja; tu: mock vs realne API)."""

    def __init__(self, tasks_path=MOCK_TASKS_PATH):
        self.tasks_path = tasks_path

    def get_new_tasks(self):
        with open(self.tasks_path, encoding="utf-8") as f:
            return json.load(f)

    def post_comment(self, task_id, text):
        print(f"[MOCK Projectly] komentarz na {task_id}:\n{text}\n")
        return True

    def update_status(self, task_id, status):
        print(f"[MOCK Projectly] {task_id} -> status: {status}")
        return True


def get_client():
    """Zwraca realnego klienta, jeśli PROJECTLY_API_KEY jest ustawiony w
    środowisku, inaczej mock — żeby runner_loop.py dało się uruchomić od razu,
    bez czekania na prawdziwe dane dostępowe."""
    api_key = os.environ.get("PROJECTLY_API_KEY")
    if api_key:
        return ProjectlyClient(api_key=api_key, base_url=os.environ.get("PROJECTLY_BASE_URL"))
    return MockProjectlyClient()
