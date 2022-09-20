# SOLUTION EXTRA Exercise Lesson 7

## Exercise 1 - Upprepning

1. Without functions

    ```python
    user_input = int(input("Input a integer: "))

    if user_input > 5:
        print(str(user_input) * user_input)
    elif 0 < user_input <= 5:
        for number in range(user_input + 1):
            print(str(number) * number)
    ```

2. With functions

    ```python
    def get_user_input():
        return int(input("Input a integer: "))


    def echo_printing(number):
        print(str(number) * number)


    def incremental_echo_printing(number):
        for number in range(number + 1):
            echo_printing(number)


    def main():
        user_input = get_user_input()
        if user_input > 5:
            echo_printing(user_input)
        else:
            incremental_echo_printing(user_input)


    if __name__ == '__main__':
        main()
    ```

## Exercise 3 - Flödesscheman

```python
def input_number_list():
    return list(map(int, input("Enter list of numbers").split(",")))

def get_next_pair(the_list, i):
    return the_list[i], the_list[i+1]

def bigger_than(a, b):
    return a > b

def swap_elements(the_list, pos1, pos2):
    the_list[pos2], the_list[pos1] = the_list[pos1], the_list[pos2]

def at_end_of_list(the_list, i):
    return i >= len(the_list)-2

list_to_sort = input_number_list()
while True:
    swapped = False
    i = 0
    while True:
        a, b = get_next_pair(list_to_sort, i)
        if bigger_than(a,b):
            swapped = True
            swap_elements(list_to_sort, i, i+1)
        if at_end_of_list(list_to_sort, i):
            break
        else:
            i += 1
    if not swapped:
        break
print(list_to_sort)
```

## Exercise 6 - Lambda

```python
def calc_input():
    input_formula = input("Enter calculcation (e.g. '5 * 7' or '7 / 2'): ")
    parts = input_formula.split(" ")
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    return a, op, b

operations = {
    "+": lambda a,b: a + b,
    "-": lambda a,b: a - b,
    "*": lambda a,b: a * b,
    "/": lambda a,b: a / b,
    "%": lambda a,b: a % b
}
def calculate(op):
    return operations[op]

a, op, b = calc_input()
print(calculate(op)(a, b))
```
