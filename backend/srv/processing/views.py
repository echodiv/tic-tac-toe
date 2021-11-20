from flask import jsonify
from flask.views import MethodView


class GameRequestView(MethodView):
    """Work with game table"""

    def get(self):
        """Get table status"""
        res = {"a": 1}
        return jsonify(res)

    def post(self):
        """"""
        res = {"a": 1}
        return jsonify(res)
