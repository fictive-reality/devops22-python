# https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements

result = 1

# addition and assignment
result += 2
print(f'[1] {result}')

# subtraction and assignment
result -= 1
print(f'[2] {result}')

# multiplication and assignment
result *= 10
print(f'[3] {result}')

# modulus and assignment
result %= 8
print(f'[4] {result}')

# division and assignment
result /= 2
print(f'[5] {result}')

# pow and assignment
result **= 3
print(f'[6] {result}')

# floor division and assignment
result //= 2
print(f'[7] {result}')
