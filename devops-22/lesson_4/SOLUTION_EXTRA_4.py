from math import sqrt

# upg. 4

numbers = [2, 4, 8, 3, 2, 7]
for number in numbers:
    print(number)
    if number % 2:
        print("Not allowed!")
        break

# 5

first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]

result = []
for tal in second_list:
    result.append((tal, first_list.index(tal)))
print(result)
# Output: [(2, 3), (3, 0), (6, 4), (7, 1), (9, 2)]

# 6 List comprehension

result = [(x, first_list.index(x)) for x in second_list]
print(result)

# 7

fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
basket = []
amount = int(input("Hur många frukter?"))

for i in range(amount):
    basket.append(fruits[i % len(fruits)])
print(basket)

basket_2 = []
while amount:
    for fruit in fruits:
        if not amount:
            break
        basket_2.append(fruit)
        amount -= 1
print(basket_2)

# 8

"""
from math import sqrt
test_number = 1
prime_number = []
while test_number < 10000:
    # print(f'Testing number: {test_number}')
    previous_numbers = test_number - 1
    while previous_numbers > 1:
        # print(f'{test_number} % {previous_numbers}')
        if not test_number % previous_numbers:
            # print("Not a prime")
            break
        previous_numbers -= 1
    if previous_numbers == 1:
        prime_number.append(test_number)
    test_number += 1

print(prime_number)



test_number = 3
prime_numbers = [2]
while test_number < 1000000:
    square = sqrt(test_number)
    isPrime = False
    for prime in prime_numbers:
        if prime > square:
            isPrime = True
            break
        isPrime = test_number % prime
        if not isPrime:
            break
    if isPrime:
        prime_numbers.append(test_number)
    test_number += 1

print(prime_numbers)
"""
