#Dennis Lunnelid
#Extra övningar Lektion 4. 

# Övning 1
for i in range(1, 11):
    print("Hello, user!")


#Övning 2
iterations = 2
number = 2

for x in range(8):
    print(f" {str(number) * iterations}")
    x += 1
    number +=1
    iterations +=1

#Övning 3

correct = 22
guess = int(input("Enter an Integer: ")).strip()

while guess != correct:
    if guess < correct:
        print("No, its higher")
        guess = int(input("Enter an Integer: "))
    elif guess > correct:
        print("No, its lower!")
        guess = int(input("Enter an Integer: "))
else:
    print("Congratulations! You´re correct!")

#Övning 4

# define list.

list1 = [4,4,4,3,4]

print("Kontrollerar udda tal i lista...")
for n in list1:
    if n % 2 != 0:
        print("Not Allowed!")
        break
else:
    print("No odd numbers found.")

#Övning 5

first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
my_list = []
#my_tuple = {}
for x in range(0, len(second_list)):
    temp_var = second_list[x]
    temp_var_igen = first_list.index(temp_var)
    #print(f" {temp_var} {first_list.index(temp_var)}")
    my_tup = (temp_var, first_list.index(temp_var))
    my_list.append(my_tup)
#print(first_list.index(temp_var))
#print(my_tup)
print(my_list)


#Övning 7

fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
my_basket = []

antal_frukter = int(input("Hur många frukter får du plats med i din korg? "))
list_index = 0
max_index = (len(fruits))

while len(my_basket) < antal_frukter:
    for x in range(antal_frukter):
        my_basket.append(fruits[list_index])
        list_index += 1
        if list_index == max_index:
            list_index = 0
print(my_basket)