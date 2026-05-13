import tkinter as tk
from src.game import Game
from src.difficulty import Difficulty
from src.mark import Mark


class UI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.difficulty = tk.StringVar(value=Difficulty.EASY.value)
        self.game = Game(Difficulty.EASY)
        self.status = tk.StringVar()
        self.buttons = []

        self._build_ui()
        self._start_if_ai_first()

    def _build_ui(self):
        top = tk.Frame(self.root)
        top.pack()
        tk.Label(top, text="Difficulty:").pack(side=tk.LEFT)
        for diff in Difficulty:
            label = diff.name.capitalize()
            tk.Radiobutton(
                top,
                text=label,
                variable=self.difficulty,
                value=diff.value,
                command=self._on_difficulty_change,
            ).pack(side=tk.LEFT)

        tk.Label(self.root, textvariable=self.status).pack()

        # Grid
        grid = tk.Frame(self.root)
        grid.pack()
        for i in range(9):
            r, c = divmod(i, 3)
            btn = tk.Button(
                grid,
                text="",
                width=4,
                height=2,
                font=("Arial", 24, "bold"),
                command=lambda idx=i: self._on_cell_click(idx),
            )
            btn.grid(row=r, column=c)
            self.buttons.append(btn)

        # Restart
        tk.Button(self.root, text="Restart", command=self._restart).pack()

        self._refresh_ui()

    def _on_cell_click(self, index: int):
        if self.game.human_move(index):
            self._refresh_ui()
            if not self.game.game_over:
                self._do_ai_move()

    def _do_ai_move(self):
        self.game.ai_move()
        self._refresh_ui()

    def _on_difficulty_change(self):
        self.game.change_difficulty(Difficulty(self.difficulty.get()))
        self._refresh_ui()
        self._start_if_ai_first()

    def _restart(self):
        self.game.restart()
        self._refresh_ui()
        self._start_if_ai_first()

    def _refresh_ui(self):
        for i, btn in enumerate(self.buttons):
            mark = self.game.board.get(i)
            btn.configure(
                text=mark.value if mark != Mark.EMPTY else "",
                state=tk.DISABLED if self.game.game_over else tk.NORMAL,
            )

        if self.game.game_over:
            if self.game.winner == Mark.HUMAN:
                self.status.set("You win!")
            elif self.game.winner == Mark.AI:
                self.status.set("AI wins!")
            else:
                self.status.set("It's a draw!")
        else:
            self.status.set(
                "Your turn (X)"
                if self.game.current == Mark.HUMAN
                else "AI thinking... (O)"
            )

    def _start_if_ai_first(self):
        if self.game.current == Mark.AI and not self.game.game_over:
            self._do_ai_move()
