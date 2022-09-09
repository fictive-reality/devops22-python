#Exercise 1
number = int(input("Which number do you want to check? "))

if number %2:
  print("This is an odd number.")
else:
  print("This is an even number.")
  
#Exercise 2
in_name = input("What is your name? ")

my_tuple = ("Ahmed", "Mohammed", "Stanislav", "Oleg", "Pelle")

if in_name in my_tuple:
    print(f"Welcome {in_name} your are on the list.")
else:
    print("You are not on the list.")

#Exercise 3
user_input = input("Type a word ")
for x in user_input:
    print(user_input)

#Exercise 4
start = int(input("Type a starting number: "))
end = int(input("Type an ending number: "))
for i in range(start, end):
    print(i)

#4
start = int(input("Type your first number: "))
end = int(input("Type your second number: "))

total = 0
for i in range(start, end):
    print(i)
    total += i
print(f"Total is :{total}")


#Exercise 5
word = str()
while word != "stop":
    word = input("Type a word:")
    print(f"{word} = {len(word)}")
    print("Enter 'stop' to quit: ")

print("Process has been stoped")

#EXTRA
#1
word = str()  
while word != "hello":
    word = input("Type hello: ")
    print("You must type 'hello'")
print("Greetings! :)\n" * 10)

#2
number = int()
for i in range(0, 9):
    number += 1
    print(number * str(number))

#3
number = int()
while number != 69:
    number = int(input("Enter an integer: "))
    if number == 69:
        print("You guessed right!")
    if number < 69:
        print("It's higher.")
    if number > 69:
        print("It's lower.")

#4
numbers = [2, 6,10,14,18,21]

for numbers in numbers:
    print(numbers)
    if numbers % 2:
        print("Not allowed!")
        break
