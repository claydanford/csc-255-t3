

from src.board import Board

board = Board()

# Test empty board
print("Empty board:")
print(board)

# Test setting X
board.set(0, "X")
print("\nAfter placing X:")
print(board)

# Test setting O
board.set(4, "O")
print("\nAfter placing O:")
print(board)

# Test reset
board.reset()
print("\nAfter reset:")
print(board)