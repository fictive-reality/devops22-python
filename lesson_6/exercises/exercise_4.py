from collections import deque
from random import randint

# Queue

# 1.
names = ["Adam", "Bertil", "Caesar", "David", "Erik"] * 10

# 2.
queue = deque(maxlen=10)

# 3.

while len(names):
    random_number = randint(0, 10)
    for i in range(random_number):
        if len(queue):
            print(queue.popleft())

    for i in range(random_number):
        if len(names):
            queue.append(names.pop())