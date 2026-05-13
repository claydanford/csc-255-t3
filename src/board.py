from src.mark import Mark


class Board:
    """
    The board in the tic tac toe game.
    """

    def __init__(self):
        self.cells = self._empty_cells()

    def _empty_cells(self):
        """
        Return a list of 9 empty cells.
        """

        return [Mark.EMPTY] * 9

    def reset(self):
        """
        Reset the board to empty cells
        """

        self.cells = self._empty_cells()

    def get(self, index: int):
        """
        Return the mark at index.
        """

        return self.cells[index]

    def set(self, index: int, value: Mark):
        """
        Set the mark at index to value.
        """

        self.cells[index] = value

    def __str__(self):
        """
        Return a string representation of the board.
        """

        c = [cell.value for cell in self.cells]
        return (
            f" {c[0]} | {c[1]} | {c[2]} \n"
            "---+---+---\n"
            f" {c[3]} | {c[4]} | {c[5]} \n"
            "---+---+---\n"
            f" {c[6]} | {c[7]} | {c[8]} "
        )
