
# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks

# Last-in, First-out
# LIFO Stack

stack = [1, 2, 3]
stack.append(4)
stack.append(5)

# The stack (list)
print(stack)

"""
# Remove a element from the right side
print(stack.pop())

# The stack after a pop
print(stack)

stack.pop()
stack.pop()

# The stack after two more pop
print(stack)

stack.pop()
stack.pop()

"""
# Pop empty list generate IndexError
# stack.pop()
