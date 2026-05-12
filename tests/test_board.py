from src.board import Board
from src.mark import Mark

board = Board()

# Test empty board
def test_empty_board():
    assert board.get(0) == Mark.EMPTY

# Test setting X
def test_setting_x():
    board.set(0, "X")
    assert board.get(0) == "X"

# Test setting O
def test_setting_O():
    board.set(4, "O")
    assert board.get(4) == "O"

# Test reset
def test_reset():
    board.reset()
    assert board.get(0) == Mark.EMPTY

def run_tests():
    test_empty_board()
    test_setting_x()
    test_setting_O()
    test_reset()

if __name__ == "__main__":
    run_tests()
    print("All tests passed.")