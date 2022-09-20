
# Simple function with one parameter

def add_one(x):
    return x + 1


add_one_one = add_one(1)
print(add_one_one)

add_one_float = add_one(1.0)
print(add_one_float)


# Integer values as argument

def addition(x, y):
    return x + y


result = addition(1, 2)
print(f'result {result} is of type {type(result)}')


# Float values as argument

float_addition = addition(1.0, 2.0)
print(f'result {float_addition} is of type {type(float_addition)}')


# Force function to return a float

def float_add(x, y):
    result = x + y
    return float(result)


float_addition = float_add(1, 2)
print(f'result {float_addition} is of type {type(float_addition)}')


# Return a tuple

def coordinates(x, y):
    return x, y


my_cords = coordinates(1.3, 5.3)
print(f'my_cords {my_cords} is of type {type(my_cords)}')


# Example bonus

def bonus_calculator(sales_amount, new_customers):
    return sales_amount * 0.04 + new_customers * 3000


print(bonus_calculator(1000000, 1))
print(bonus_calculator(600000, 10))


# Empty return

def empty_return():
    return


print(empty_return())


# One Expression

def one_expr():
    return 1

# One expression with optional ,


def one_expr_with_comma():
    return 1,


print(one_expr())
print(one_expr_with_comma())


def multiple_expr():
    return 1, 2, 3


def multiple_expr_with_comma():
    return 1, 2, 3,


print(multiple_expr())
print(multiple_expr_with_comma())
print(multiple_expr() == multiple_expr_with_comma())
