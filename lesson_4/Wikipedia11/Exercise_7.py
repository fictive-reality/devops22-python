fruit = ['apple', 'orange', 'pear', 'banana', 'grapes']
fruit_list = list()
slots = int(input("How many slots for fruits do you have in your basket? "))

i = 0
while True:
    if i < slots:
        fruit_list.append(fruit[i % 5])
        i += 1
    else:
        print(f"Your basket is full\nIt contains {fruit_list}")
        break