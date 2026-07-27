"""
Sentinel -- Autonomous Incident Commander
Phase 0: Flask environment sanity check + a quick primer on how Flask works.

THE CORE IDEA OF FLASK:
You write small Python functions ("view functions") and attach each one
to a URL using the @app.route(...) decorator. When a browser (or another
program) requests that URL, Flask calls your function and sends back
whatever it returns as the HTTP response. That's the whole model --
everything else in Flask is a variation on this.
"""

from flask import Flask
import os
from dotenv import load_dotenv

# load_dotenv() reads the .env file and copies its values into the
# environment, so secrets (API keys, DB passwords) never get hardcoded
# into the source code. os.getenv(...) then reads them back out.
load_dotenv()


def create_app():
    """
    This is the "application factory" pattern -- instead of a single
    global `app = Flask(__name__)` sitting at module level, we build
    the app inside a function.

    Why bother? Because later we'll want multiple versions of this app
    (one for local dev, one for automated tests, maybe one for
    production) with different configs. A bare global app can't do
    that cleanly -- a factory function can, since you just call
    create_app() again with different settings.
    """

    # __name__ tells Flask which file it's running from, so it knows
    # where to look for the /static and /templates folders we'll add
    # in Phase 5 (the custom frontend).
    app = Flask(__name__)

    # SECRET_KEY is used by Flask to cryptographically sign things like
    # session cookies. Never commit a real one -- it comes from .env.
    app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "dev")

    # --- Routes -----------------------------------------------------
    # @app.route("/") means: "when someone visits the root URL with a
    # GET request, run the function right below this line, and send
    # back whatever it returns."
    #
    # Returning a Python dict here is a Flask shortcut -- Flask
    # automatically converts it to JSON with the right headers. No
    # manual json.dumps() needed.
    @app.route("/")
    def index():
        return {
            "status": "Sentinel backend is alive",
            "next_step": "Phase 1 -- Oracle DB schema",
        }

    # Every real backend has a /health endpoint. Monitoring tools ping
    # it to confirm the service is up -- and later, our own Monitor
    # Agent will poll something very similar to check on the
    # *simulated* services in the chaos engine.
    @app.route("/health")
    def health():
        # Returning a tuple of (body, status_code) lets you set the
        # HTTP status explicitly. 200 means "OK".
        return {"status": "ok"}, 200

    return app


# This block only runs when you execute `python app.py` directly --
# it does NOT run if this file gets imported elsewhere (e.g. by a
# test file, or later by a WSGI server in production). That guard is
# what `if __name__ == "__main__":` is for.
if __name__ == "__main__":
    app = create_app()
    # debug=True gives you auto-reload on save and detailed in-browser
    # error pages while developing. Always turn this off in production.
    app.run(debug=True, port=5000)
