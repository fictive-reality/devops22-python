# https://docs.python.org/3/reference/compound_stmts.html#while

number = int(input("enter a number: "))
while number == 5:
    print(f"number is {number}")
    number = int(input("enter a number: "))

"""
while True:
    number = int(input("enter a number: "))
    if(number != 5):
        break
    print(f"number is {number}")
"""
