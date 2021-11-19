from flask import Flask

from .config import Config


def create_app(config: Config = Config) -> Flask:
    """Crete new application instance"""
    app = Flask(__name__)
    app.config.from_object(config)
    return app
