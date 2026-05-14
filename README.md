# CSC 255 Group Project — Python Tic Tac Toe

> This readme serves as an overview and spec for this project.

## Overview

A Tic Tac Toe game in Python. One human player (X) plays against a computer opponent (O). The computer can be played in easy, medium, hard or impossible mode. The game detects wins and draws, and lets the player restart.

## Running the Program

```bash
python3 -m main

# or

uv run main.py

# Select 1 for CLI
# Select 2 for UI (a new window pops up on the desktop)
```

## Core Concepts

| Requirement              | How it appears                                           |
| ------------------------ | -------------------------------------------------------- |
| Games                    | Interactive turn-based game loop with win/draw detection |
| Random Number Generation | AI picks moves randomly via `random.choice` in easy mode |

## Features

| #   | Feature                                          |
| --- | ------------------------------------------------ |
| 1   | 3×3 grid                                         |
| 2   | Human plays as X; AI plays as O                  |
| 3   | AI can be in easy, medium, hard, or impossible   |
| 4   | Win detection across all 8 lines                 |
| 5   | Draw detection when board is full with no winner |
| 6   | Restart clears board                             |
| 7   | CLI and UI version                               |

## Project Structure

```
./
├── src/
│   ├── __init__.py
│   ├── ai.py
│   ├── board.py
│   ├── cli.py
│   ├── difficulty.py
│   ├── game.py
│   ├── logic.py
│   ├── mark.py
│   └── ui.py
├── tests/
│   ├── __init__.py
│   ├── run_all.py
│   ├── test_ai.py
│   ├── test_board.py
│   ├── test_game.py
│   └── test_logic.py
├── main.py
└── README.md
```

### Responsibility

| File            | Responsibility                                                                    |
| --------------- | --------------------------------------------------------------------------------- |
| `mark.py`       | Enum for the three cell states: `HUMAN` (X), `AI` (O), `EMPTY`.                   |
| `difficulty.py` | Enum for the four difficulty levels.                                              |
| `board.py`      | Stores the board as a flat list of 9 `Mark` values.                               |
| `logic.py`      | Game rules: win detection across all 8 lines, draw detection, move validation.    |
| `ai.py`         | Computer decision-making. Dispatches to the correct strategy based on difficulty. |
| `game.py`       | Coordinates board, logic, and AI. Tracks turn and game-over state.                |
| `cli.py`        | Text-based interface. Prompts for moves and prints the board.                     |
| `ui.py`         | Tkinter GUI interface.                                                            |
| `main.py`       | Entry point. Prompts the user to choose CLI or UI mode.                           |

## Difficulty modes

- Easy: The computer randomly picks a cell.
- Medium: 66% chance of a random move, 34% chance of an optimal move.
- Hard: 33% chance of a random move, 67% chance of an optimal move.
- Impossible: The computer always tries to win using the minimax algorithm.

## Design

### CLI vs UI

We built both a CLI and a Tkinter UI. They share the same `Game`, `Board`, `Logic`, and `AI` classes. The only difference is how moves are taken and how the board is displayed. `main.py` asks which interface you want at uses.

The CLI was developed first since it is easier to test and debug. The UI was added without changing any core logic.

The UI pops up in a new window on the desktop.

### How the classes fit together

`Board` just holds the state, a flat list of 9 cells. It doesn't know anything about rules. It can get and set marks and print a string representation of the board.

`Logic` knows the rules. It checks for winners, detects draws, and validates moves. It operates on a `Board`.

`AI` uses `Logic` to evaluate the board and picks a move based on the current difficulty. For easy it picks randomly. For impossible it runs minimax, a recursive algorithm that plays out every possible game and picks the move that leads to the best outcome. For medium and hard difficulties it randomly picks between random and minimax.

`Game` is the coordinator. It owns the board, creates the logic and AI, and handles whose turn it is. The UI and CLI only talk to `Game`, they call `human_move()` and `ai_move()` and read `game_over` and `winner`.

`Mark` and `Difficulty` are just enums used to avoid passing raw strings around.

### Minimax

Minimax works by recursively simulating all possible moves from the current board. The AI scores each outcome (+1 win, -1 loss, 0 draw) and picks the move with the best score. On impossible difficulty this means the AI cannot be beaten.

## Running Tests

```bash
python3 -m tests.run_all
# or
uv run tests/run_all.py
```

## Authors

- Clay Danford
- Joel Porras

## Group Collaboration

- The group collaborated through email, chat, and meetings. We met first to discuss the project idea and settle on an tic tac toe game.
- Clay developed the spec, setup a github repository, and a github project.
- The team took stories off the github project like an agile team. The stories were written with standard agile language and gherkin syntax.
- We peer reviewed pull requests and ensured the project was well developed.

### References
- [Github Repo](https://github.com/claydanford/csc-255-t3)
- [Github Project](https://github.com/users/claydanford/projects/1/views/1)

## Possible Errors

If running the project on MacOS and hitting the following error launching the UI, update python or use uv.

```bash
Launching UI...
macOS 26 (2603) or later required, have instead 16 (1603) !
[1]    19235 abort      python3 main.py
```
