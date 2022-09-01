even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
favorites = {7, 4}

# Union
print(f'[1] even | odd union {even | odd}')

# Intersection
print(f'[2] even & odd Intersection {even & odd}')
print(f'[3] favorites intersection with odd {favorites & odd}')
print(f'[4] favorites intersection with even {favorites & even}')

# Difference
print(f'[5] even and odd difference {even - odd}')
print(f'[5] odd and even difference {odd - even}')
print(f'[6] odd and odd difference {odd - odd}')

# Add to set
favorites.add(22)
print(f'[7] added 22 to favorites {favorites}')

# Ask about numbers in set
print(f'[8] 22 in favorites: {22 in favorites}')
print(f'[9] 7 in even: {7 in even}')
print(f'[10] 7 in odd: {7 in odd}')
