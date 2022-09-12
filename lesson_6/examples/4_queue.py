from collections import deque

# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues

# First-in, First-out FIFO Queue

queue = deque(["Lisa", "Pelle", "Olle"])
queue.append("Elvira")
print(queue)

# pop from left

print(queue.popleft())
# Print list
print(queue)

# Restore with Append left
queue.appendleft("Lisa")

# Print list
print(queue)

# Pop from right
print(queue.pop())

# Print list
print(queue)

print(queue.append("Elvira"))

# Print list
print(queue)

# Rotate list
queue.rotate(2)

# Print list
print(queue)
