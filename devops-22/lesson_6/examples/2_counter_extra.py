from collections import Counter
from random import sample

test_data = sample(['red', 'green', 'blue'], counts=[100, 100, 100], k=100)

c = Counter(test_data)
# Get all votes
print(f'elements: {list(c.elements())}')

# Sum all votes
print(f'elements: {sum(c.values())}')

# Extras
print(f'most common: {c.most_common()}')

# Add extra
c.update({'yellow': 1})
c.update(Counter(red=1))

# Subtract
c.subtract({'red': 2})
c.subtract(Counter(green=3))

# Sum all votes
print(f'elements: {sum(c.values())}')

# Extras
print(f'most common: {c.most_common()}')
