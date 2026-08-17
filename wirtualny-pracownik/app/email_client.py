"""
Klient poczty (config/integrations.yaml wpis `microsoft_365`: mail
read+send z jednego wspólnego konta). To jest STUB — prawdziwy dostęp
(Microsoft Graph + rejestracja aplikacji w Azure AD, pakiet `msal`,
patrz app/README.md "Co jeszcze będzie potrzebne") nie jest jeszcze
podłączony w tej sesji. Przygotowane z wyprzedzeniem, żeby po dostarczeniu
dostępu wystarczyło dopisać `EmailClient`, bez zmiany reszty pipeline'u
(`email_draft_generator.py` i przyszły `email_intake_triage.py`).

`draft_email` jest już `yellow` w approval_policy.yaml — realna wysyłka
przechodzi normalną ścieżkę walidacji/auto-zatwierdzenia (sekcja 3 planu),
zanim cokolwiek pójdzie do klienta. Ten moduł sam z siebie niczego nie
wysyła bez świadomego wywołania `send_email`.
"""

import os
import re
from pathlib import Path

MOCK_OUTBOX_DIR = Path(__file__).parent / "runs" / "mock_outbox"


class EmailClient:
    """Prawdziwa implementacja — DO ZROBIENIA, gdy będzie znany mechanizm
    dostępu do skrzynki (Microsoft Graph)."""

    def __init__(self, client_id=None, client_secret=None, tenant_id=None, mailbox=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.mailbox = mailbox

    def send_email(self, to, subject, body_text, cc=None):
        raise NotImplementedError(
            "Prawdziwy Microsoft Graph nie jest jeszcze podłączony. "
            "Wymaga: rejestracji aplikacji w Azure AD, pakietu 'msal', "
            "i danych dostępowych w .env (MS_GRAPH_CLIENT_ID/SECRET/TENANT_ID/MAILBOX). "
            "Użyj MockEmailClient do testów albo uzupełnij tę metodę."
        )

    def save_draft(self, to, subject, body_text, cc=None):
        raise NotImplementedError("Jak wyżej.")


class MockEmailClient:
    """Nie wysyła niczego naprawdę — zapisuje treść jako plik tekstowy w
    runs/mock_outbox/, żeby dało się przejrzeć draft przed podłączeniem
    prawdziwej skrzynki (ten sam wzorzec co MockProjectlyClient)."""

    def __init__(self, outbox_dir=MOCK_OUTBOX_DIR):
        self.outbox_dir = outbox_dir

    def send_email(self, to, subject, body_text, cc=None):
        return self._write(to, subject, body_text, cc, action="SEND (mock — nie wysłano naprawdę)")

    def save_draft(self, to, subject, body_text, cc=None):
        return self._write(to, subject, body_text, cc, action="DRAFT")

    def _write(self, to, subject, body_text, cc, action):
        self.outbox_dir.mkdir(parents=True, exist_ok=True)
        safe_subject = re.sub(r"[^\w\-]+", "_", subject)[:60] or "bez_tematu"
        existing = list(self.outbox_dir.glob(f"{safe_subject}_*.txt"))
        path = self.outbox_dir / f"{safe_subject}_{len(existing) + 1}.txt"

        content = f"Do: {to}\nDW: {cc or '-'}\nTemat: {subject}\nAkcja: {action}\n\n{body_text}\n"
        path.write_text(content, encoding="utf-8")
        print(f"[MOCK Email] {action} -> {path.name}")
        return str(path)


def get_email_client():
    """Real klient dopiero, gdy WSZYSTKIE dane dostępowe Graph są ustawione —
    częściowa konfiguracja nie powinna cicho przełączyć na tryb realny
    (fail-closed, ten sam wzorzec co projectly_client.get_client)."""
    required = ("MS_GRAPH_CLIENT_ID", "MS_GRAPH_CLIENT_SECRET", "MS_GRAPH_TENANT_ID", "MS_GRAPH_MAILBOX")
    if all(os.environ.get(k) for k in required):
        return EmailClient(
            client_id=os.environ["MS_GRAPH_CLIENT_ID"],
            client_secret=os.environ["MS_GRAPH_CLIENT_SECRET"],
            tenant_id=os.environ["MS_GRAPH_TENANT_ID"],
            mailbox=os.environ["MS_GRAPH_MAILBOX"],
        )
    return MockEmailClient()
