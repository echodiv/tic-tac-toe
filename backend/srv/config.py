import os


class Config:
    """Contain base config for flask application
    """
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret")
