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
        c = [cell.value for cell in self.cells]
        return (
            f" {c[0]} | {c[1]} | {c[2]} \n"
            "---+---+---\n"
            f" {c[3]} | {c[4]} | {c[5]} \n"
            "---+---+---\n"
            f" {c[6]} | {c[7]} | {c[8]} "
        )
