"""
In-memory state shared between the bot thread and the Flask UI thread.
Replaces native pyautogui popups: informational events go to `log_event`,
human-input moments block on `request_decision` until the UI resolves them.
"""

import threading
from collections import deque
from datetime import datetime

_lock = threading.Lock()
_log = deque(maxlen=500)
_pending = {}
_next_id = 1


def log_event(kind: str, message: str, **fields) -> None:
    with _lock:
        _log.appendleft({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "kind": kind,
            "message": message,
            **fields,
        })


def request_decision(kind: str, message: str, options: list) -> str:
    '''
    Blocks the calling thread until the UI posts a choice for this decision.
    '''
    global _next_id
    event = threading.Event()
    with _lock:
        decision_id = _next_id
        _next_id += 1
        _pending[decision_id] = {"event": event, "choice": None, "kind": kind, "message": message, "options": options}
        _log.appendleft({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "kind": kind,
            "message": message,
            "decision_id": decision_id,
            "options": options,
        })
    event.wait()
    with _lock:
        record = _pending.pop(decision_id)
    return record["choice"]


def resolve_decision(decision_id: int, choice: str) -> bool:
    with _lock:
        record = _pending.get(decision_id)
        if not record:
            return False
        record["choice"] = choice
    record["event"].set()
    return True


def snapshot() -> dict:
    with _lock:
        log = list(_log)
        pending = [
            {"id": did, "kind": r["kind"], "message": r["message"], "options": r["options"]}
            for did, r in _pending.items()
        ]
    return {"log": log, "pending": pending}
