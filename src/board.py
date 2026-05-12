from src.mark import Mark


class Board:
    def __init__(self):
        self.cells = self._empty_cells()

    def _empty_cells(self):
        return [Mark.EMPTY] * 9

    def reset(self):
        self.cells = self._empty_cells()

    def get(self, index: int):
        return self.cells[index]

    def set(self, index: int, value: Mark):
        self.cells[index] = value

    def __str__(self):
        return (
            f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} \n"
            "---+---+---\n"
            f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} \n"
            "---+---+---\n"
            f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} "
        )
