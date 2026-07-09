'''
Entry point: starts the live dashboard (Flask, background thread), then runs the bot.
Run this instead of the old runAiBot.py: `python server.py`
'''

import threading

from modules import state
from app import app as flask_app


def start_dashboard() -> None:
    threading.Thread(target=lambda: flask_app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False), daemon=True).start()
    state.log_event("info", "Live dashboard running at http://localhost:5000")


if __name__ == "__main__":
    start_dashboard()
    # Deferred import: importing bot.orchestrator transitively opens the real Chrome
    # browser (modules.open_chrome runs at import time) - must happen after the
    # dashboard thread has already started.
    from bot.orchestrator import main
    main()
