# 1. Create a function that uses try/except
# 2. The function should have the parameters x, y
# 3. The function should return x/y
# 4. If the user provide a y = 0, it should except the error and print 'Division by zero is not allowed'
# 5. If the argument y is a string, it should raise a TypeError'


# ------------------------------------EXERCISE 1------------------------------------

def try_except(x, y):
    try:
        sum = round(x / y, 2)
        result = print(f"result: {sum}")
    except ZeroDivisionError:
        print("Division by 0 is not allowed")  
    except TypeError:
        print("Your Y value is a string, it needs to be a int.")
