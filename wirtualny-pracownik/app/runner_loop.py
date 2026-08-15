"""
Główna pętla: pobiera zadania, klasyfikuje ryzyko, rozdziela do właściciela,
zapisuje stan, aktualizuje heartbeat (PLAN-WDROZENIA.md sekcja 1-3, SKRYPTY.md
kategoria A). To jest szkielet Fazy 0-1 — wykonuje realny cykl
queued -> classified -> routed -> (auto | needs_human), ale bez jeszcze
podłączonych workerów (Power BI, CRM itd.) i bez prawdziwego Projectly
(patrz projectly_client.py).

Sprawdza kill switch (STOP.flag) na starcie każdej iteracji, zgodnie z
PLAN-WDROZENIA.md sekcja 17.

Użycie:
    python runner_loop.py            # jeden przebieg, tryb mock
    python runner_loop.py --loop      # ciągła pętla (Ctrl+C żeby zatrzymać)
"""

import argparse
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import heartbeat
import risk_classifier
import state_store
import task_router
from projectly_client import get_client

STOP_FLAG_PATH = Path(__file__).parent / "runs" / "STOP.flag"

# Zgrubne mapowanie: pole risk_level_hint z zadania na typ akcji z approval_policy.yaml.
# W pełnej wersji to robi risk_classifier per-krok planu, nie per-całe zadanie —
# tu upraszczamy do jednego kroku "przetwórz zadanie", żeby Faza 0 była testowalna.
HINT_TO_ACTION = {
    "green": "read_report",
    "yellow": "report_build",
    "red": "budget_change",
}


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def kill_switch_active():
    return STOP_FLAG_PATH.exists()


def process_task(task, policy, routing, client):
    task_id = task["task_id"]
    now = now_iso()

    state_store.upsert_task(task_id, payload=task, status="planning", now=now)
    state_store.record_event(task_id, "task_received", task["title"], now)

    action_type = HINT_TO_ACTION.get(task.get("risk_level_hint", "yellow"), "report_build")
    risk = risk_classifier.classify(action_type, policy)
    owner, confident = task_router.route_task(task["title"], routing)

    state_store.record_event(
        task_id,
        "classified",
        f"action_type={action_type} risk={risk} owner={owner} confident={confident}",
        now,
    )

    if risk == "green":
        status = "done"
        comment = (
            f"✅ Zadanie zielone, wykonane automatycznie.\n"
            f"Co zrobiono: klasyfikacja i routing (Faza 0 — bez realnego workera jeszcze).\n"
            f"Przypisano do: {owner}\n"
        )
    elif risk == "yellow":
        status = "needs_approval"
        comment = (
            f"⚠️ Zadanie żółte — w pełnej wersji trafiłoby do validator_pool.py.\n"
            f"Przypisano do: {owner} (pewność routingu: {confident})\n"
            f"Wymaga decyzji: tak — walidatory jeszcze niepodłączone w tym szkielecie.\n"
        )
    else:
        status = "needs_approval"
        comment = (
            f"🔴 Zadanie czerwone — zawsze do człowieka (PLAN-WDROZENIA.md sekcja 3-4).\n"
            f"Przypisano do: {owner}\n"
            f"Wymaga decyzji: tak.\n"
        )

    state_store.upsert_task(task_id, payload=task, status=status, assigned_to=owner, risk_level=risk, now=now_iso())
    state_store.record_event(task_id, "status_set", status, now_iso())

    client.post_comment(task_id, comment)
    client.update_status(task_id, status)

    return {"task_id": task_id, "risk": risk, "owner": owner, "status": status}


def run_once():
    if kill_switch_active():
        print("STOP.flag obecny — kill switch aktywny, runner nie podejmuje akcji.")
        return []

    policy = risk_classifier.load_policy()
    routing = task_router.load_routing()
    client = get_client()

    heartbeat.write_heartbeat(current_task_id=None)

    tasks = client.get_new_tasks()
    results = []
    for task in tasks:
        heartbeat.write_heartbeat(current_task_id=task["task_id"])
        results.append(process_task(task, policy, routing, client))

    heartbeat.write_heartbeat(current_task_id=None)
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--loop", action="store_true", help="Ciągła pętla zamiast jednego przebiegu")
    parser.add_argument("--interval", type=int, default=30, help="Sekundy między przebiegami w trybie --loop")
    args = parser.parse_args()

    if not args.loop:
        results = run_once()
        for r in results:
            print(r)
        return

    print(f"Runner w trybie ciągłym, interwał {args.interval}s. Ctrl+C żeby zatrzymać.")
    try:
        while True:
            if kill_switch_active():
                print("STOP.flag wykryty — zatrzymuję runner.")
                sys.exit(0)
            for r in run_once():
                print(r)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("Zatrzymano ręcznie.")


if __name__ == "__main__":
    main()
