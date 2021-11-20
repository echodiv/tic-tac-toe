from srv import create_app, db
from sqlite3 import Error

app = create_app()


@app.before_request
def migrate():
    """Create tables for game
    +-------+
    | BOARD |
    +-------+
    | id    |
    | board |
    +-------+
    """
    create_board_command = """
        CREATE TABLE IF NOT EXISTS board (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            board TEXT
        )
    """
    try:
        c = db.cursor()
        c.execute(create_board_command)
    except Error as e:
        app.log_exception(e)
