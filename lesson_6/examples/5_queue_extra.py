from collections import deque

# First-in, First-out FIFO Queue
# Limit size
queue = deque(["a", "b", "c", "d", "e"], maxlen=5)
print(queue)

queue.appendleft("1")
print(queue)

# insert will throw IndexError if maximum size is reached
# queue.insert(1, "2")

# If you pop one element first it will work
queue.pop()
queue.insert(0, "0")

print(queue)
