
# Input integer

def int_input(text):
    number = None
    while True:
        try:
            number = int(input(text))
            break
        except ValueError:
            print("Not a valid integer!")
    return number


my_number = int_input("Enter a number: ")
print(f'result: {my_number}')


# Alternative recursive approach

def input_retry(user_instruction):
    try:
        return int(input(user_instruction))
    except ValueError:
        print("Not valid integer!")
        return input_retry(user_instruction)


my_number = input_retry("Enter a number:")
print(f'result: {my_number}')
