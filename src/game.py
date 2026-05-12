import random
from src.mark import Mark
from src.board import Board
from src.logic import Logic
from src.ai import AI
from src.difficulty import Difficulty


class Game:

    def __init__(self, difficulty: Difficulty = Difficulty.EASY):
        self.difficulty = difficulty
        self._setup()

    def human_move(self, index: int) -> bool:
        """
        Attempt to place X at index. Returns True if the move was accepted.
        """
        if self.game_over or self.current != Mark.HUMAN:
            return False
        if not self.logic.is_valid_move(index):
            return False

        self.board.set(index, Mark.HUMAN)
        self._check_state()

        if not self.game_over:
            self.current = Mark.AI

        return True

    def ai_move(self) -> int:
        """
        Let the AI pick and play its move. Returns the index chosen.
        """
        if self.game_over or self.current != Mark.AI:
            return -1

        index = self.ai.get_move()
        self.board.set(index, Mark.AI)
        self._check_state()

        if not self.game_over:
            self.current = Mark.HUMAN

        return index

    def restart(self):
        """
        Reset the board and all state. Randomly choose who goes first.
        """
        self._setup()

    def change_difficulty(self, difficulty: Difficulty):
        """
        Change the difficulty and restart the game.
        """
        self.difficulty = difficulty
        self._setup()

    def _check_state(self):
        """
        Checks for a winner or draw and updates game_over and winner accordingly.
        """
        winner = self.logic.check_winner()
        if winner:
            self.winner = winner
            self.game_over = True
        elif self.logic.is_draw():
            self.game_over = True

    def _setup(self):
        """
        Set up a new game with an empty board and randomly chosen first player.
        """
        self.board = Board()
        self.logic = Logic(self.board)
        self.ai = AI(self.board, self.difficulty)
        self.winner = None
        self.game_over = False
        self.current = random.choice([Mark.HUMAN, Mark.AI])
