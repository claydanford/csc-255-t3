from src.board import Board
from src.mark import Mark


class Logic:
    WINNING_LINES = [
        (0, 1, 2),  # top row
        (3, 4, 5),  # middle row
        (6, 7, 8),  # bottom row
        (0, 3, 6),  # left column
        (1, 4, 7),  # middle column
        (2, 5, 8),  # right column
        (0, 4, 8),  # top-left diagonal
        (2, 4, 6),  # top-right diagonal
    ]

    def __init__(self, board: Board):
        self.board = board

    def check_winner(self):
        """
        Return 'X', 'O', or None.
        """
        line = self.get_winning_line()

        if line:
            return self.board.get(line[0])
        else:
            return None

    def get_winning_line(self):
        """
        Return the winning (a, b, c) index triple, or None.
        """
        for a, b, c in self.WINNING_LINES:

            a_mark = self.board.get(a)
            b_mark = self.board.get(b)
            c_mark = self.board.get(c)

            if a_mark != Mark.EMPTY and a_mark == b_mark == c_mark:
                return (a, b, c)

        return None

    def is_draw(self):
        """
        Return True if the board is full and there is no winner.
        """
        return (
            all(self.board.get(i) != Mark.EMPTY for i in range(9))
            and self.check_winner() is None
        )

    def is_valid_move(self, index: int):
        """
        Return True if index is in range and the cell is empty.
        """
        return 0 <= index <= 8 and self.board.get(index) == Mark.EMPTY

    def get_empty_indices(self):
        """
        Return a list of all empty cell indices.
        """
        return [i for i in range(9) if self.board.get(i) == Mark.EMPTY]
