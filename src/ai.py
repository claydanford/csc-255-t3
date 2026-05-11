import random
from enum import Enum
from src.board import Board
from src.logic import Logic


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    IMPOSSIBLE = "impossible"


class AI:

    def __init__(self, board: Board, difficulty: Difficulty = Difficulty.EASY):
        self.board = board
        self.logic = Logic(board)
        self.difficulty = difficulty

    def get_move(self):
        """
        Return the index the AI has chosen to play.
        """
        return getattr(self, f"_{self.difficulty.value}_move")()

    def _easy_move(self):
        """
        Pick a random empty cell.
        """
        return self._random_move()

    def _medium_move(self):
        """
        66% chance of playing randomly, 34% chance of playing optimally.
        """
        pass  # TODO: implement medium move

    def _hard_move(self):
        """
        33% chance of playing randomly, 67% chance of playing optimally.
        """
        pass  # TODO: implement hard move

    def _impossible_move(self):
        """
        Return the index with the best minimax score.
        """
        pass  # TODO: implement impossible move

    def _minimax(self, is_maximizing: bool):
        """
        Return the minimax score for the current board state.
        """
        pass  # TODO: implement minimax algorithm

    def _random_move(self):
        """
        Return a random empty cell index.
        """
        return random.choice(self.logic.get_empty_indices())
