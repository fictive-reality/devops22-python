
# Division by zero
try:
    1 / 0
except ZeroDivisionError:
    print("Not allowed!")

# Wrong type for int conversion
try:
    int("abc")
except ValueError:
    print("Something went wrong")

# TypeError

my_list = ["hello", "hi", "howdy"]
try:
    my_list["wrong"]
except TypeError:
    print("Only integer allowed")
