from src.board import Board
from src.mark import Mark


# Test empty board
def test_empty_board():
    board = Board()
    assert board.get(0) == Mark.EMPTY


# Test setting X
def test_setting_x():
    board = Board()
    board.set(0, Mark.HUMAN)
    assert board.get(0) == Mark.HUMAN


# Test setting O
def test_setting_o():
    board = Board()
    board.set(4, Mark.AI)
    assert board.get(4) == Mark.AI


# Test reset
def test_reset():
    board = Board()
    board.reset()
    assert board.get(0) == Mark.EMPTY


def run_tests():
    test_empty_board()
    test_setting_x()
    test_setting_o()
    test_reset()


if __name__ == "__main__":
    run_tests()
    print("All tests passed.")
