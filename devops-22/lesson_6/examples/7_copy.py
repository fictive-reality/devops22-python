from copy import deepcopy

NEWLINE = "\n"

# https://docs.python.org/3/library/copy.html

# List comprehension
board = [[0 for y in range(10)] for x in range(10)]

print(board)

print(NEWLINE)


# Trick with map and join
def print_board(b):
    print('\n'.join(map(str, b)))


print_board(board)
print(NEWLINE)

# Create a shallow copy and a deep copy

board_assignment = board
board_copy = board.copy()
board_deep_copy = deepcopy(board)

print("----- == -----")
print(board_assignment == board)
print(board_copy == board)
print(board_deep_copy == board)

print("----- is -----")
print(board_assignment is board)
print(board_copy is board)
print(board_deep_copy is board)

for i in range(10):
    board[i][i] = 1

print("----- board ------")
print_board(board)
print(NEWLINE)

print("---- board copy ----")
print_board(board_copy)
print(NEWLINE)

print("-- board deep copy --")
print_board(board_deep_copy)

print("----- == -----")
print(board_assignment == board)
print(board_copy == board)
print(board_deep_copy == board)
