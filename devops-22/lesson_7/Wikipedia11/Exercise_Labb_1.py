# SEE "functions_extra_labb.pdf"


"""
number = int(input("Please write a integer: "))

if number > 5:
    print(str(number) * number)
elif number < 5:
    for n in range(1, int(number)+1):
        number = str(n) * int(n)
        print(number)
"""


def number():
        number = int(input("Please write a integer: "))
        if number > 5:
            print(str(number) * number)
        elif number < 5:
            for n in range(1, int(number)+1):
                number = str(n) * int(n)
                print(number)