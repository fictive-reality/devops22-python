# 1. Create a program that takes input and convert it to a integer
# 2. If it's not possible to convert it to a integer the program should print `Sorry, not an int`
# 3. If the input fail to convert to a int, the program should retry the input
# 4. If the number is even, raise a Exception('Even numbers is not allowed')


# ------------------------------------EXERCISE 1------------------------------------

def int_num():
    while True:
        try:
           user_input = int(input("Give me an int: "))       
        except ValueError:
            print("Sorry, you need to give me an int!")
        else:
            if user_input % 2 == False:
                print("Even number is not allowed")
            if user_input % 2 == True:
                break
# ------------------------------------EXERCISE 2------------------------------------



# ------------------------------------EXERCISE 3------------------------------------



# ------------------------------------EXERCISE 4------------------------------------