fruit = ['apple', 'orange', 'pear', 'banana', 'grapes']
fruit_list = list()
slots = int(input("How many slots for fruits do you have in your basket? "))

i = 0
while True:
    if i <= slots:
        fruit_list.append(fruit[i])
        i += 1
    else:
        print("Your basket is full")
        print(f"It contains {fruit_list}")
        break