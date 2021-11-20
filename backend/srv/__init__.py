import sqlite3

from flask import Flask

from .config import Config
from .processing.views import GameRequestView


db = sqlite3.connect(":memory:", check_same_thread=False)


def create_app(config: Config = Config) -> Flask:
    """Crete new application instance"""
    app = Flask(__name__)
    app.config.from_object(config)

    app.add_url_rule("/api/table", view_func=GameRequestView.as_view("game"))

    return app
