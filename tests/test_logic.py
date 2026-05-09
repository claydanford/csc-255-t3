from src.board import Board
from src.logic import Logic


def make_logic(cells):
    board = Board()
    for i in range(9):
        board.set(i, cells[i])
    return Logic(board)


E = " "


# check_winner


def test_check_winner_x_top_row():
    logic = make_logic(["X", "X", "X", E, E, E, E, E, E])
    assert logic.check_winner() == "X"


def test_check_winner_o_middle_row():
    logic = make_logic([E, E, E, "O", "O", "O", E, E, E])
    assert logic.check_winner() == "O"


def test_check_winner_x_diagonal():
    logic = make_logic(["X", E, E, E, "X", E, E, E, "X"])
    assert logic.check_winner() == "X"


def test_check_winner_none():
    logic = make_logic([E] * 9)
    assert logic.check_winner() is None


# get_winning_line


def test_get_winning_line_returns_triple():
    logic = make_logic(["X", "X", "X", E, E, E, E, E, E])
    assert logic.get_winning_line() == (0, 1, 2)


def test_get_winning_line_none():
    logic = make_logic([E] * 9)
    assert logic.get_winning_line() is None


# is_draw


def test_is_draw_true():
    # no winner, full board
    logic = make_logic(["X", "O", "X", "O", "X", "O", "O", "X", "O"])
    assert logic.is_draw() is True


def test_is_draw_false_winner():
    logic = make_logic(["X", "X", "X", "O", "O", E, E, E, E])
    assert logic.is_draw() is False


def test_is_draw_false_not_full():
    logic = make_logic([E] * 9)
    assert logic.is_draw() is False


# is_valid_move


def test_is_valid_move_empty_cell():
    logic = make_logic([E] * 9)
    assert logic.is_valid_move(0) is True


def test_is_valid_move_occupied_cell():
    logic = make_logic(["X"] + [E] * 8)
    assert logic.is_valid_move(0) is False


def test_is_valid_move_out_of_range():
    logic = make_logic([E] * 9)
    assert logic.is_valid_move(9) is False
    assert logic.is_valid_move(-1) is False


# get_empty_indices


def test_get_empty_indices_all_empty():
    logic = make_logic([E] * 9)
    assert logic.get_empty_indices() == list(range(9))


def test_get_empty_indices_none_empty():
    logic = make_logic(["X"] * 9)
    assert logic.get_empty_indices() == []


def test_get_empty_indices_partial():
    logic = make_logic(["X", E, "O", E, E, "X", E, E, "O"])
    assert logic.get_empty_indices() == [1, 3, 4, 6, 7]
