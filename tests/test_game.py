from src.game import Game
from src.mark import Mark
from src.difficulty import Difficulty

# human_move


def test_human_move_valid():
    game = Game()
    game.current = Mark.HUMAN
    result = game.human_move(0)
    assert result is True
    assert game.board.get(0) == Mark.HUMAN


def test_human_move_invalid_occupied():
    game = Game()
    game.current = Mark.HUMAN
    game.human_move(0)
    game.current = Mark.HUMAN
    result = game.human_move(0)
    assert result is False


def test_human_move_wrong_turn():
    game = Game()
    game.current = Mark.AI
    result = game.human_move(0)
    assert result is False


def test_human_move_out_of_range():
    game = Game()
    game.current = Mark.HUMAN
    result = game.human_move(9)
    assert result is False


# ai_move


def test_ai_move_returns_valid_index():
    game = Game()
    game.current = Mark.AI
    index = game.ai_move()
    assert 0 <= index <= 8


def test_ai_move_wrong_turn():
    game = Game()
    game.current = Mark.HUMAN
    result = game.ai_move()
    assert result == -1


# game over detection


def test_human_wins():
    game = Game()
    game.board.set(0, Mark.HUMAN)
    game.board.set(1, Mark.HUMAN)
    game.board.set(2, Mark.HUMAN)
    game._check_state()
    assert game.game_over is True
    assert game.winner == Mark.HUMAN


def test_draw_detected():
    game = Game()
    marks = [
        Mark.HUMAN,
        Mark.AI,
        Mark.HUMAN,
        Mark.AI,
        Mark.HUMAN,
        Mark.AI,
        Mark.AI,
        Mark.HUMAN,
        Mark.AI,
    ]
    for i, m in enumerate(marks):
        game.board.set(i, m)
    game._check_state()
    assert game.game_over is True
    assert game.winner is None


# restart


def test_restart_clears_board():
    game = Game()
    game.current = Mark.HUMAN
    game.human_move(0)
    game.restart()
    assert all(game.board.get(i) == Mark.EMPTY for i in range(9))
    assert game.game_over is False
    assert game.winner is None


# change_difficulty


def test_change_difficulty():
    game = Game()
    game.change_difficulty(Difficulty.HARD)
    assert game.difficulty == Difficulty.HARD
    assert game.ai.difficulty == Difficulty.HARD


def test_change_difficulty_resets_board():
    game = Game()
    game.current = Mark.HUMAN
    game.human_move(0)
    game.change_difficulty(Difficulty.MEDIUM)
    assert all(game.board.get(i) == Mark.EMPTY for i in range(9))


def run_tests():
    test_human_move_valid()
    test_human_move_invalid_occupied()
    test_human_move_wrong_turn()
    test_human_move_out_of_range()
    test_ai_move_returns_valid_index()
    test_ai_move_wrong_turn()
    test_human_wins()
    test_draw_detected()
    test_restart_clears_board()
    test_change_difficulty()
    test_change_difficulty_resets_board()


if __name__ == "__main__":
    run_tests()
    print("All tests passed.")
