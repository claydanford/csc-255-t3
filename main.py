from src.game import Game
from src.mark import Mark
from src.difficulty import Difficulty


def choose_difficulty():
    """
    Prompt the user to select a difficulty level.
    """
    options = {
        "1": Difficulty.EASY,
        "2": Difficulty.MEDIUM,
        "3": Difficulty.HARD,
        "4": Difficulty.IMPOSSIBLE,
    }
    print("Select difficulty:")
    print("1 - Easy       (AI plays randomly)")
    print("2 - Medium     (66% random, 34% optimal)")
    print("3 - Hard       (33% random, 67% optimal)")
    print("4 - Impossible (AI always plays optimally)")

    while True:
        choice = input("Enter 1, 2, 3, or 4: ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice, please enter 1, 2, 3, or 4.")


def get_human_move(game: Game):
    """
    Prompt the user for a move until they enter a valid one.
    """
    while True:
        raw = input("Your move (0-8): ").strip()
        if not raw.isdigit():
            print("Please enter a number between 0 and 8.")
            continue
        index = int(raw)
        if not game.logic.is_valid_move(index):
            print("That cell is taken or out of range. Try again.")
            continue
        return index


def play(difficulty: Difficulty):
    """
    Orchestrates a single game of tic tac toe.
    """

    game = Game(difficulty)

    print(
        "Cell positions:\n"
        " 0 | 1 | 2 \n"
        "---+---+---\n"
        " 3 | 4 | 5 \n"
        "---+---+---\n"
        " 6 | 7 | 8 \n"
    )

    print(f"Starting player: {'You (X)' if game.current == Mark.HUMAN else 'AI (O)'}")

    while not game.game_over:
        print(f"\n{game.board}\n")

        if game.current == Mark.HUMAN:
            index = get_human_move(game)
            game.human_move(index)
        else:
            index = game.ai_move()
            print(f"AI played: {index}")

    print(f"\n{game.board}\n")

    if game.winner == Mark.HUMAN:
        print("You win!")
    elif game.winner == Mark.AI:
        print("AI wins!")
    else:
        print("It's a draw!")


def main():
    """
    Main game loop.
    """

    print("=== Tic Tac Toe ===")

    difficulty = choose_difficulty()

    while True:
        play(difficulty)
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break
        change = input("Change difficulty? (y/n): ").strip().lower()
        if change == "y":
            difficulty = choose_difficulty()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
