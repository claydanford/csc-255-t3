# CSC 255 Group Project — Python Tic Tac Toe

## Overview

Build a Tic Tac Toe game in Python. One human player (X) plays against an computer opponent (O). The computer can be played in easy, medium or hard mode. The game detects wins and draws, and lets the player restart.

## Core Concepts

| Requirement | How it appears |
|---|---|
| Games | Interactive turn-based game loop with win/draw detection |
| Random Number Generation | AI picks moves randomly via `random.choice` in easy mode |

## Features

| # | Feature |
|---|---|
| 1 | 3×3 grid |
| 2 | Human plays as X; AI plays as O |
| 3 | AI can be in easy, medium, or hard |
| 4 | Win detection across all 8 lines |
| 5 | Draw detection when board is full with no winner |
| 6 | Restart clears board |

## Project Structure

```
./
├── src/
│   ├── __init__.py
│   ├── board.py
│   ├── logic.py
│   ├── ai.py
│   └── game.py
├── tests/
│   ├── __init__.py
│   ├── test_board.py
│   ├── test_logic.py
│   ├── test_ai.py
│   └── test_game.py
├── main.py
└── README.md
```

### Responsibility

| File | Responsibility |
|---|---|
| `board.py` | Manages the board as a flat list of 9 strings. Responsible for creating a fresh board and resetting it between games. |
| `logic.py` | Contains the rules of the game. Checks all 8 lines for a winner, detects draws when the board is full, and validates whether a move is legal. |
| `ai.py` | Handles all computer decision-making. |
| `game.py` | Owns game flow state. Tracks whose turn it is, handles turn switching, and manages restart logic. Acts as the coordinator between the board, logic, and AI. |
| `main.py` | The entry point. Calls into `game.py` to advance state and `logic.py` to check for a winner after each move. |

## Difficulty modes

- Easy: The computer randomly picks a cell
- Medium: The computer randomly picks between a random cell and minimax cell
- Hard: The computer always tries to win using minimax algorithm

## Running the Program

**Python:**
```bash
python main.py
```

**uv:**
```bash
uv run main.py
```

## Authors

- Clay Danford
- Joel Porras
- Zhen Li