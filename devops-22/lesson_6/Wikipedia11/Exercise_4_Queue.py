# Use the deque FIFO, first in, first out. I.e if ["lisa", "olle", "pelle"] is in the list, then use pop left so that "lisa" is first to leave the queue.

# Generate a list with 50 names
# Create a Queue deque with a maximum length of 10
# Let random number of person leave the queue
# When the random number of persons has left the queue, fill the missing spots
# Iterate until all 50 has gone through the queue

from collections import deque
import random

# ------------------------------------EXERCISE 1------------------------------------

names = ["Fredrik", "Johanna", "Mari", "Lars", "Carolina", "Pontus", "Tuva", "Siri"]
name_list = random.choices(names, k=50)

# ------------------------------------EXERCISE 2------------------------------------

queue = deque(name_list, 10)
print(queue)
print(type(queue))

# ------------------------------------EXERCISE 3------------------------------------

shuffled = random.shuffle(queue)
queue.pop()
print(queue)
# ------------------------------------EXERCISE 4------------------------------------



# ------------------------------------EXERCISE 5------------------------------------
