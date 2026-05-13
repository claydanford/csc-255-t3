from enum import Enum


class Mark(Enum):
    """
    Enum for the marks on the tic tac toe board.
    """

    HUMAN = "X"
    AI = "O"
    EMPTY = " "
