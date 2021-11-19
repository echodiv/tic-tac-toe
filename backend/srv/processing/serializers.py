from pydantic import BaseModel


class TicTacRequest(BaseModel):
    x_position: int
    y_position: int
