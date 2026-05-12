from src.board import Board
from src.ai import AI
from src.difficulty import Difficulty
from src.mark import Mark

X = Mark.HUMAN
O = Mark.AI
E = Mark.EMPTY


def make_ai(cells, difficulty=Difficulty.EASY):
    board = Board()
    for i in range(9):
        board.set(i, cells[i])
    return AI(board, difficulty)


# get_move / _random_move (easy)


def test_easy_move_returns_valid_index():
    ai = make_ai([E] * 9)
    move = ai.get_move()
    assert 0 <= move <= 8


def test_easy_move_returns_empty_cell():
    cells = [X, O, X, O, X, O, O, E, E]
    ai = make_ai(cells)
    assert ai.get_move() in [7, 8]


def test_easy_move_on_single_empty():
    cells = [X, O, X, O, X, O, O, X, E]
    ai = make_ai(cells)
    assert ai.get_move() == 8


def run_tests():
    test_easy_move_returns_valid_index()
    test_easy_move_returns_empty_cell()
    test_easy_move_on_single_empty()


if __name__ == "__main__":
    run_tests()
    print("All tests passed.")
