import random
from src.board import Board
from src.difficulty import Difficulty
from src.logic import Logic
from src.mark import Mark


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
        chance = random.randint(1, 100)
        
        if chance <= 66:
            return self._random_move()
        
        return self._minimax_move()

    def _hard_move(self):
        """
        33% chance of playing randomly, 67% chance of playing optimally.
        """
        chance = random.randint(1, 100)

        if chance <= 33:
            return self._random_move()
        
        return self._minimax_move()


    def _impossible_move(self):
        """
        Use minimax algorithm to always play the best move.
        """
        return self._minimax_move()

    def _minimax_move(self):
        """
        Return the index with the best minimax score.
        """
        best_score = float("-inf")
        best_index = None

        for i in self.logic.get_empty_indices():
            self.board.set(i, Mark.AI)
            score = self._minimax(is_maximizing=False)
            self.board.set(i, Mark.EMPTY)

            if score > best_score:
                best_score = score
                best_index = i

        return best_index

    def _minimax(self, is_maximizing: bool):
        """
        Return the minimax score for the current board state.
        """
        winner = self.logic.check_winner()
        if winner == Mark.AI:
            return 1
        if winner == Mark.HUMAN:
            return -1
        if self.logic.is_draw():
            return 0

        empty = self.logic.get_empty_indices()

        if is_maximizing:
            best = float("-inf")
            for i in empty:
                self.board.set(i, Mark.AI)
                best = max(best, self._minimax(is_maximizing=False))
                self.board.set(i, Mark.EMPTY)
            return best
        else:
            best = float("inf")
            for i in empty:
                self.board.set(i, Mark.HUMAN)
                best = min(best, self._minimax(is_maximizing=True))
                self.board.set(i, Mark.EMPTY)
            return best

    def _random_move(self):
        """
        Return a random empty cell index.
        """
        return random.choice(self.logic.get_empty_indices())
