from flask import jsonify
from flask.views import MethodView


class GameRequest(MethodView):
    """Work with game table"""

    def get(self):
        res = {"a": 1}
        return jsonify(res)

    def post(self):
        res = {"a": 1}
        return jsonify(res)
