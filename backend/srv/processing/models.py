from backend import db


class Board(db.Model):
    id = db.Column(db.integer)
