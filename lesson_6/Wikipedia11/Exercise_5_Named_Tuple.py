# Create a named tuple with the coordinates (x, y)
# Create two points
# Print the points in a board i.e

# Generate a board
# board = [["-"]*10 for i in range(10)]
# Print board
# for row in board:
    # print(row)

# mark x, y in board as *
# board[1][2] = '*'
# board[4][6] = '*'

# Calculate the Euclidean distance (hypotenuse) for Point1 and Point2, i.e (1, 2) and (4, 6) has the distance 5.

from collections import namedtuple
from math import sqrt
# ------------------------------------EXERCISE 1------------------------------------

point = namedtuple("point", ["x", "y"])

# ------------------------------------EXERCISE 2------------------------------------

p1 = point(x=4, y=5)
p2 = point(x=7, y=9)

# ------------------------------------EXERCISE 3------------------------------------

# Generate a board
board = [["-"]*10 for i in range(10)]

# mark x, y in board as *
board[p1.y][p1.x] = '*'
board[p2.y][p2.x] = '*'

# Print board
for row in board:
    print(row)

# ------------------------------------EXERCISE 4------------------------------------

distance = sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
print(f"The distance between {p1} & {p2} is {distance}")