from src.cli import cli


def main():
    print("=== Tic Tac Toe ===")

    while True:
        print("\nSelect mode:")
        print("1 - CLI")
        print("2 - UI")

        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            cli()
        elif choice == "2":
            import tkinter as tk
            from src.ui import UI

            print("Launching UI...")
            root = tk.Tk()
            UI(root)
            root.mainloop()
        else:
            print("Invalid choice, please enter 1 or 2.")
            continue

        again = input("\nReturn to mode select? (y/n): ").strip().lower()
        if again != "y":
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
