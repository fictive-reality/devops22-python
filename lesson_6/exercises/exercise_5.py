from collections import namedtuple

# Named tuple

# 1.

Point = namedtuple('Point', ['x', 'y'])

# 2.
p_1 = Point(x=4, y=6)
p_2 = Point(x=2, y=8)

# 3.
board = [["-"]*10 for i in range(10)]
for row in board:
    print(row)
    board[4][6] = '*'
    board[2][8] = '*'

# 4.
x_distance = p_2.x - p_1.x
y_distance = p_2.y - p_1.y
print((x_distance**2 + y_distance**2) ** 0.5)

